"""Serie temporal de inventario por oferta — a ferramenta da REGRA PRIMORDIAL do projeto.

Existe porque contagem tirada UMA vez e inventario, nao escala: na R017 (20/09/2026) a mesma busca
devolveu 28 ou 598 IDs conforme o IP, porque a Meta responde HTTP 403 desenhando "No ads match your
search criteria". Escala e o que sobrevive a repeticao da medida.

Acrescenta (nunca sobrescreve) uma linha por leitura em projeto/treinamento/serie-escala.jsonl e
imprime o delta contra a leitura anterior da mesma chave.

Uso:
  # registrar uma leitura ja coletada, sem ir a rede de novo
  python scripts/escala_serie.py registrar --chave quiz.eroscode.de --de saida.json --rodada R017

  # remedir: roda o coletor com proxy e acrescenta a leitura
  python scripts/escala_serie.py remedir --chave quiz.eroscode.de --q eroscode --country DE \\
      --search-type keyword_unordered --rodada R018

  # ver a serie
  python scripts/escala_serie.py ver [--chave quiz.eroscode.de]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SERIE = RAIZ / "meu" / "serie-escala.jsonl"


def pagina_do_card(copy: str | None) -> str | None:
    """O nome da Pagina e a linha imediatamente antes de 'Sponsored'/'Patrocinado'."""
    linhas = (copy or "").split("\n")
    for i, l in enumerate(linhas):
        if l.strip() in ("Sponsored", "Patrocinado") and i > 0:
            return linhas[i - 1].strip()
    return None


def medir(coleta: dict, chave: str) -> dict:
    """Um JSON do adlib_coleta -> os quatro eixos da regra, para o destino `chave`."""
    ads = coleta.get("ads") or []
    no_destino = [a for a in ads if a.get("destino") == chave]
    datas = sorted(a["inicio"] for a in no_destino if a.get("inicio"))
    hoje = datetime.now(timezone.utc).date()
    idades = [(hoje - datetime.fromisoformat(d).date()).days for d in datas]
    idades.sort()
    personas = {p for p in (pagina_do_card(a.get("copy")) for a in no_destino) if p}
    return {
        "ids_total": len(ads),
        "ids_no_destino": len(no_destino),
        "atribuicao": round(len(no_destino) / len(ads), 3) if ads else None,
        "personas": len(personas),
        "mais_antigo_dias": max(idades) if idades else None,
        "mediana_dias": idades[len(idades) // 2] if idades else None,
        "acima_30d": sum(1 for i in idades if i > 30),
        "acima_90d": sum(1 for i in idades if i > 90),
        "cabecalho": coleta.get("cabecalho"),
    }


def leituras(chave: str | None = None) -> list[dict]:
    if not SERIE.exists():
        return []
    fora = []
    for linha in SERIE.read_text(encoding="utf-8").split("\n"):
        if linha.strip():
            r = json.loads(linha)
            if chave is None or r.get("chave") == chave:
                fora.append(r)
    return fora


def acrescentar(registro: dict) -> dict | None:
    """Grava a leitura e devolve a anterior da mesma chave, se houver."""
    anteriores = leituras(registro["chave"])
    SERIE.parent.mkdir(parents=True, exist_ok=True)
    with SERIE.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(registro, ensure_ascii=False) + "\n")
    return anteriores[-1] if anteriores else None


def relatar(registro: dict, anterior: dict | None) -> str:
    m = registro["medida"]
    cab = f"{registro['chave']} · {registro['observado_em'][:10]} · {m['ids_no_destino']} IDs no destino"
    if not anterior:
        return (f"{cab}\n  LEITURA 1 — isto e INVENTARIO, nao escala. "
                f"A ficha declara 'escala: pendente de segunda leitura'.")
    a = anterior["medida"]
    d = m["ids_no_destino"] - a["ids_no_destino"]
    pct = f"{d / a['ids_no_destino'] * 100:+.1f}%" if a["ids_no_destino"] else "n/d"
    n = len(leituras(registro["chave"]))
    return (f"{cab}\n  LEITURA {n} — anterior {anterior['observado_em'][:10]}: "
            f"{a['ids_no_destino']} -> {m['ids_no_destino']} ({d:+d}, {pct})\n"
            f"  personas {a['personas']} -> {m['personas']} · "
            f"acima de 30d {a['acima_30d']} -> {m['acima_30d']}\n"
            f"  Com {n} leituras, 'indicios de escala' pode ser escrito — sempre com a serie ao lado.")


def cmd_registrar(a) -> int:
    coleta = json.loads(Path(a.de).read_text(encoding="utf-8"))
    reg = {"chave": a.chave, "rodada": a.rodada, "fonte": "meta_ad_library",
           "observado_em": a.quando or datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "busca": {"q": coleta.get("q"), "country": coleta.get("country"),
                     "search_type": coleta.get("search_type"), "proxy": a.proxy},
           "http_ok": a.http_ok, "medida": medir(coleta, a.chave), "origem": str(a.de)}
    print(relatar(reg, acrescentar(reg)))
    return 0


def cmd_registrar_json(a) -> int:
    """A leitura ja vem pronta do motor (tool medir); aqui so entra na serie e sai o delta."""
    reg = json.loads(Path(a.de).read_text(encoding="utf-8"))
    if reg.get("erro") or "medida" not in reg:
        raise SystemExit(reg.get("erro") or "arquivo nao e uma leitura de medir()")
    print(relatar(reg, acrescentar(reg)))
    return 0


def _num(txt: str | None) -> int | None:
    """'1.23K subscribers' / '12,345' / '2.1M' -> int. None se ausente."""
    if not txt:
        return None
    t = re.sub(r"\s*thousand", "K", re.sub(r"\s*million", "M", txt.replace(" ", " ")))
    m = re.search(r"([\d.,]+)\s*([KMB]?)", t)
    if not m:
        return None
    n, suf = m.group(1), m.group(2)
    if suf:
        return int(float(n.replace(",", "")) * {"K": 1e3, "M": 1e6, "B": 1e9}[suf])
    return int(re.sub(r"[.,]", "", n))


def ler_video(vid: str) -> dict:
    """Pagina publica youtube.com/watch sem login -> views, publicacao, nao-listado, canal, inscritos."""
    import httpx
    r = httpx.get("https://www.youtube.com/watch", params={"v": vid, "hl": "en", "gl": "US"},
                  cookies={"CONSENT": "YES+cb", "SOCS": "CAI"}, timeout=30, follow_redirects=True,
                  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36",
                           "Accept-Language": "en-US,en;q=0.9"})
    html = r.text
    i = html.find("ytInitialPlayerResponse = ")
    if r.status_code != 200 or i < 0:
        return {"video_id": vid, "http": r.status_code, "erro": "sem ytInitialPlayerResponse"}
    pr, _ = json.JSONDecoder().raw_decode(html, i + len("ytInitialPlayerResponse = "))
    vd = pr.get("videoDetails") or {}
    mf = (pr.get("microformat") or {}).get("playerMicroformatRenderer") or {}
    subs = re.search(r'"subscriberCountText":\{"accessibility":\{"accessibilityData":\{"label":"([^"]*)"', html) \
        or re.search(r'"subscriberCountText":\{[^}]*"simpleText":"([^"]*)"', html)
    pub = (mf.get("publishDate") or mf.get("uploadDate") or "")[:10] or None
    views = int(vd["viewCount"]) if vd.get("viewCount") else None
    return {"video_id": vid, "http": r.status_code,
            "status": (pr.get("playabilityStatus") or {}).get("status"),
            "views": views, "publicado": pub, "nao_listado": mf.get("isUnlisted"),
            "canal_id": vd.get("channelId"), "canal": vd.get("author"),
            "inscritos_txt": subs.group(1) if subs else None, "inscritos": _num(subs.group(1)) if subs else None,
            "duracao_s": int(vd["lengthSeconds"]) if vd.get("lengthSeconds") else None,
            "titulo": vd.get("title")}


def views_dia(med: dict, quando: str) -> float | None:
    if not med.get("views") or not med.get("publicado"):
        return None
    dias = max((datetime.fromisoformat(quando[:10]).date()
                - datetime.fromisoformat(med["publicado"]).date()).days, 1)
    return round(med["views"] / dias, 1)


def cmd_youtube(a) -> int:
    """Leitura de views por video_id (REGRA PRIMORDIAL no YouTube: 2 leituras >=24h -> delta/dia)."""
    for vid in [v.strip() for v in a.ids.split(",") if v.strip()]:
        agora = datetime.now(timezone.utc).isoformat(timespec="seconds")
        med = ler_video(vid)
        if not med.get("views"):
            print(f"yt:{vid} · leitura FALHOU ({med.get('http')}, {med.get('erro') or med.get('status')}) — nao entra na serie")
            continue
        med["views_dia_desde_publicacao"] = views_dia(med, agora)
        reg = {"chave": f"yt:{vid}", "oferta": a.oferta, "rodada": a.rodada, "fonte": "youtube_watch",
               "observado_em": agora, "http_ok": med["http"] == 200, "medida": med, "origem": "escala_serie.youtube"}
        ant = acrescentar(reg)
        cab = (f"yt:{vid} · {a.oferta} · {med['views']:,} views · pub {med['publicado']} · "
               f"nao_listado={med['nao_listado']} · {med['canal']} ({med['inscritos_txt']})")
        if not ant:
            print(f"{cab}\n  LEITURA 1 — INVENTARIO; {med['views_dia_desde_publicacao']} views/dia desde a publicacao")
        else:
            h = (datetime.fromisoformat(agora) - datetime.fromisoformat(ant["observado_em"])).total_seconds() / 3600
            d = med["views"] - ant["medida"]["views"]
            print(f"{cab}\n  LEITURA {len(leituras(reg['chave']))} — {d:+,} views em {h:.1f} h "
                  f"= {d / h * 24:,.0f} views/dia{'' if h >= 24 else ' (intervalo <24h: nao conta como repeticao)'}")
    return 0


def cmd_ver(a) -> int:
    rs = leituras(a.chave)
    if not rs:
        print("serie vazia")
        return 0
    for r in rs:
        m = r["medida"]
        if r.get("fonte") == "youtube_watch":
            print(f"{r['observado_em'][:16]} · {r['chave']:28s} · {r['rodada']:6s} · "
                  f"{m['views']:>12,} views · pub {m['publicado']} · nao_listado={m['nao_listado']}")
            continue
        print(f"{r['observado_em'][:16]} · {r['chave']:28s} · {r['rodada']:6s} · "
              f"{m['ids_no_destino']:5d} no destino / {m['ids_total']:5d} · "
              f"personas {m['personas']:3d} · >30d {m['acima_30d']:4d}")
    porchave: dict[str, int] = {}
    for r in rs:
        porchave[r["chave"]] = porchave.get(r["chave"], 0) + 1
    print()
    for k, n in sorted(porchave.items()):
        print(f"  {k}: {n} leitura(s) — {'INVENTARIO' if n < 2 else 'indicios de escala liberados'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("registrar", help="grava uma leitura de um JSON ja coletado")
    r.add_argument("--chave", required=True, help="hostname de destino da oferta")
    r.add_argument("--de", required=True, help="JSON do adlib_coleta")
    r.add_argument("--rodada", required=True)
    r.add_argument("--quando", help="ISO; default = agora")
    r.add_argument("--proxy", default="auto")
    r.add_argument("--http-ok", action="store_true", default=True)
    r.set_defaults(func=cmd_registrar)

    j = sub.add_parser("registrar-json", help="grava a leitura devolvida por medir(job, chave) do motor")
    j.add_argument("--de", required=True, help="JSON salvo de medir()")
    j.set_defaults(func=cmd_registrar_json)

    y = sub.add_parser("youtube", help="le views de video_ids na pagina publica e grava a leitura")
    y.add_argument("--ids", required=True, help="video_ids separados por virgula")
    y.add_argument("--oferta", required=True, help="hostname de destino da oferta")
    y.add_argument("--rodada", required=True)
    y.set_defaults(func=cmd_youtube)

    v = sub.add_parser("ver", help="imprime a serie")
    v.add_argument("--chave")
    v.set_defaults(func=cmd_ver)

    a = ap.parse_args()
    return a.func(a)


def _autoteste():
    assert pagina_do_card("x\nEvelyn Taylor\nSponsored\ncopy") == "Evelyn Taylor"
    assert pagina_do_card("Sponsored\ncopy") is None  # sem linha antes
    assert pagina_do_card(None) is None
    hoje = datetime.now(timezone.utc).date()
    antigo = hoje.replace(year=hoje.year - 1).isoformat()
    coleta = {"cabecalho": 10, "ads": [
        {"id": "1", "destino": "a.com", "inicio": antigo, "copy": "x\nDr. Fulano\nSponsored\n."},
        {"id": "2", "destino": "a.com", "inicio": hoje.isoformat(), "copy": "x\nBeltrana\nSponsored\n."},
        {"id": "3", "destino": "outro.com", "inicio": hoje.isoformat(), "copy": None},
    ]}
    m = medir(coleta, "a.com")
    assert m["ids_total"] == 3 and m["ids_no_destino"] == 2 and m["personas"] == 2
    assert m["atribuicao"] == 0.667 and m["acima_90d"] == 1 and m["acima_30d"] == 1
    assert medir({"ads": []}, "a.com")["atribuicao"] is None
    reg = {"chave": "a.com", "observado_em": "2026-09-20T00:00:00", "medida": m}
    assert "INVENTARIO" in relatar(reg, None)
    ant = {"observado_em": "2026-09-19T00:00:00",
           "medida": {"ids_no_destino": 1, "personas": 1, "acima_30d": 0}}
    assert "+1" in relatar(reg, ant)
    assert _num("1.23K subscribers") == 1230 and _num("2.1M subscribers") == 2100000
    assert _num("1.76 thousand subscribers") == 1760 and _num("2.3 million subscribers") == 2300000
    assert _num("12,345") == 12345 and _num(None) is None and _num("845 subscribers") == 845
    assert views_dia({"views": 1000, "publicado": "2026-09-12"}, "2026-09-22T10:00:00") == 100.0
    assert views_dia({"views": None, "publicado": "2026-09-12"}, "2026-09-22") is None
    print("autoteste ok")


if __name__ == "__main__":
    if "--autoteste" in sys.argv:
        _autoteste()
    else:
        raise SystemExit(main())
