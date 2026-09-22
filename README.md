# HackingAds MCP

Inteligência de anúncios **no ar agora**, operada pelo seu Claude, com uma base de critério já calibrada
que você leva pra sua máquina e refina do seu jeito.

Duas peças:

| Peça | O que é | Onde vive |
|---|---|---|
| **Motor** | coleta nas fontes (Meta, AdHeart), fila, cota | servidor remoto, via MCP, com a sua chave |
| **Base de treinamento** | o critério do operador (`base/`) + o que você aprende (`meu/`) | **esta pasta**, em `.md` que o seu Claude edita direto |

Você clona, cola a chave, abre o Claude Code na pasta e opera em conversa. Sua base evolui com você;
a do operador chega por `git pull`, sem apagar a sua.

## Comece

Precisa de um Claude que edite arquivos locais: **Claude Code** (ou Claude Desktop com acesso à pasta).

```bash
git clone https://github.com/SolarisSy/hackingads-mcp
cd hackingads-mcp
```

Troque `<SUA_CHAVE>` no [`.mcp.json`](.mcp.json) pela sua chave e abra o Claude Code na pasta:

```bash
claude
```

Primeira conversa: **"leia meu/goals/GOAL-EXEMPLO.md e rode uma rodada em renda extra, região ES"**.
O `CLAUDE.md` já diz ao Claude o ciclo, onde ler, onde escrever e como traduzir a base pro motor.

Sem chave? Abra uma issue [pedindo acesso](../../issues/new?template=acesso.md).

## O que tem na pasta

```
CLAUDE.md          o ciclo e as regras que o seu Claude segue
base/              CRITERIOS · README (ciclo) · METRICAS · GOAL-ADVERTORIAL · GOAL-RENDA-EXTRA · GOAL-RELACIONAMENTO
meu/               CRITERIOS-meu · goals/ · rodadas/ · avaliacoes.jsonl · serie-escala.jsonl · dados/
scripts/           escala_serie.py — a série da regra primordial
docs/              tools do motor (gerado) · o ciclo · uma rodada de exemplo
```

## A regra que governa tudo

> **Escala é o que sobrevive à repetição da medida.** Contagem tirada uma vez é *inventário*.
> Só vira *indício de escala* com duas leituras separadas no tempo, mesmo método.

`medir` + `scripts/escala_serie.py` aplicam isso: com uma leitura, "inventário"; nunca "escalada".

## Quanto tempo leva uma busca

2–10 min. Se a fonte travar a sessão, o coletor insiste com esperas crescentes por até ~15 min e então
devolve `bloqueada=true` (que **não** é contagem). O `status` mostra os minutos decorridos e avisa;
`cancelar(job)` interrompe e você tenta outra frase ou país. Uma coleta por vez: se outra pessoa estiver
coletando, a sua entra na fila.

## Atualizar a base do operador

```bash
git pull
```

Só `base/` muda. `meu/` é seu e nunca é tocado.

Detalhes: [o ciclo](docs/ciclo.md) · [as tools do motor](docs/tools.md) · [uma rodada de exemplo](docs/rodada-exemplo.md)
