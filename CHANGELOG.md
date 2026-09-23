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
- `minerar(fonte="adheart", sort="total_reach")`: descoberta dos mais escalados por alcance; CLAUDE.md com "descobrir → medir", volume → assinatura → formato, alternância de país e piso por mercado; seção BR no GOAL-RENDA-EXTRA (lições da R001 do 1º fork).
- `CLAUDE.md` "Rodar até o fim": ao pedir uma rodada inteira, o Claude entrega o texto do `/goal` (≤ 4.000 chars) com condição de parada; alternativas `/loop` e "continua".
- `status(job, esperar=60)`: espera no servidor (150 chamadas viram ~10); AdHeart recusa >2 termos por chamada (cota é por termo); `escala_serie.py` só libera "indícios" com mesma busca e ≥24 h; o Claude responde SÓ com o texto do `/goal` quando a pessoa pede rodada sem tê-lo colado.
