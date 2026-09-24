"""Check that the public skill, permissions and generated MCP contract agree."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tools = (root / "docs/tools.md").read_text(encoding="utf-8")
documented = set(re.findall(r"^## `([a-z_]+)\(", tools, re.M))
settings = json.loads((root / ".claude/settings.json").read_text(encoding="utf-8"))
allowed = {item.removeprefix("mcp__hackingads__") for item in settings["permissions"]["allow"]
           if item.startswith("mcp__hackingads__")}
sources = (root / "docs/fontes.md").read_text(encoding="utf-8").casefold()
errors = []
if documented != allowed:
    errors.append("docs/tools.md e permissões Claude têm tools diferentes")
if len(documented) != 14:
    errors.append(f"tools documentadas: {len(documented)}, esperado 14")
for source in ("adheart", "americanswipe", "vav", "anstrex", "trendtrack", "mineraroi",
               "foreplay", "adyntel", "tyver", "spyhouse"):
    if source not in sources:
        errors.append(f"fonte sem mapa: {source}")
for name in ("AGENTS.md", "CLAUDE.md", "docs/ciclo.md", "docs/goal-preflight.md",
             "docs/fontes.md", "meu/goals/GOAL-EXEMPLO.md"):
    if "planejar_fontes" not in (root / name).read_text(encoding="utf-8"):
        errors.append(f"roteamento ausente: {name}")
for goal in sorted((root / "base").glob("GOAL-*.md")):
    opening = goal.read_text(encoding="utf-8").splitlines()[:12]
    if not any("planejar_fontes" in line for line in opening):
        errors.append(f"Goal sem roteamento MCP no início: {goal.name}")
    if goal.name != "GOAL-RENDA-EXTRA-YOUTUBE.md" and not any(
        "sem colar a versão curta" in line for line in opening
    ):
        errors.append(f"Goal histórico sem aviso de cópia: {goal.name}")
active_docs = ("README.md", "AGENTS.md", "CLAUDE.md", "docs/ciclo.md", "docs/fontes.md",
               "docs/goal-preflight.md", "docs/rodada-exemplo.md", "meu/goals/GOAL-EXEMPLO.md")
for name in active_docs:
    doc = root / name
    content = doc.read_text(encoding="utf-8")
    if "youtube_video(ids)" in content:
        errors.append(f"país omitido na leitura YouTube: {name}")
    for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", content):
        path = link.split("#", 1)[0].split("?", 1)[0]
        if not path or path.startswith(("http:", "https:", "/", "../../issues/")):
            continue
        if not (doc.parent / path).exists():
            errors.append(f"link local ausente: {name} → {path}")
readme = (root / "README.md").read_text(encoding="utf-8")
if "14%20tools" not in readme:
    errors.append("badge README não acompanha a quantidade de tools")
if errors:
    for error in errors:
        print("FAIL", error)
    raise SystemExit(1)
print("ok — 14 tools, permissões, dez fontes e roteamento nos guias")
