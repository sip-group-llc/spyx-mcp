# Changelog

## 2026-09-22 (v2 — base local)

- A base de treinamento passa a viver na pasta da pessoa: `base/` (do operador, via `git pull`) e `meu/`
  (da pessoa, editado direto pelo Claude dela). `CLAUDE.md` traz o ciclo e a tradução base → motor.
- O motor encolhe a 6 tools: `minerar · status · cancelar · anuncios · medir · adheart`. Saem `base`,
  `anotar`, `avaliar`, `rodadas`, `rodada_salvar`, `goal`, `escala` — viraram arquivo.
- Novas: `anuncios` (dado bruto paginado) e `medir` (leitura pronta pra série local).
- `scripts/escala_serie.py` no pacote, com `registrar-json`.
- `.claude/settings.json`: tools do motor, WebFetch e o script de série pré-aprovados; `base/` bloqueado para escrita.
- `CLAUDE.md`: seção "A base, por dentro" e "Quando o operador atualizar a base".

## 2026-09-22

- Primeira versão pública: 9 tools + prompt `goal`, fork de critério por pessoa, fontes Meta e AdHeart.
- Regra primordial aplicada pela tool `escala`: uma leitura é inventário, nunca escala.
