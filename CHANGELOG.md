# Changelog

## 2026-09-24 — revisão do roteamento e do ciclo

- `planejar_fontes` relaciona os dez mineradores em cada recorte, com papel,
  filtro geográfico real, decisão e último teste, sem consumir quota.
- Resultados de catálogo aceitam filtro e ordenação locais, evitando repetir
  consulta paga para procurar um nicho entre centenas de linhas.
- VAV expõe catálogo, leaderboard (página 1), nome/ID de canal e domínio;
  a URL do vídeo é identificada como vídeo, sem fingir ser landing.
- O Goal de exemplo e a rodada de exemplo seguem as tools atuais e registram
  cobertura por fonte. Jobs interrompidos por reinício são identificados sem
  repetição automática.

## 2026-09-24 — todos os conectores no MCP

- `fontes` inventaria dez mineradores credenciados e as bibliotecas Meta/Google, distinguindo
  pré-requisito de acesso testado.
- `minerador` e `minerador_resultados` dão acesso limitado e privado por pessoa a AmericanSwipe,
  VAV, Anstrex, Trendtrack, MineraROI, Foreplay, Adyntel, Tyver e SpyHouse.
- O uso por rede, filtros reais e confirmação pública está em `docs/fontes.md`.

## 2026-09-23 — setup por cliente

- README distingue `.mcp.json` do Claude Code de `~/.codex/config.toml` do Codex para o MCP remoto.
  A chave individual permanece fora do repositório.

## 2026-09-23 — pré-voo e entrega completa

- `AGENTS.md` orienta o Codex e `docs/goal-preflight.md` exige país/rede definidos, prévia do Goal e
  aprovação explícita antes da ativação assistida. Um `/goal` colado diretamente pode ser ativado pelo app.
- Toda rodada entrega também ranking dos melhores achados parciais, cobertura medida e registro de
  descobertas em `meu/`, mesmo sem finalistas comprovados. O histórico da R006 mostrou por que isso importa.

## 2026-09-23 — correção da amostragem ATC

- `google(descobrir)` distribui o limite global de anunciantes entre todos os termos pedidos e informa
  sugestões não sondadas em `cobertura`.
- Domínios vistos no payload do criativo são apenas pistas em `dominios_observados`; a URL técnica da prévia
  não é apresentada como landing. `destino_exato_confirmado=false` explicita a atribuição pendente.

## 2026-09-23 — frente Google/YouTube

- MCP: `google` descobre por termo e sonda por domínio no ATC; `google_resultados` pagina o resultado;
  `youtube_video` mede o vídeo público. Google roda em fila própria com limites de páginas e anunciantes.
- `base/GOAL-RENDA-EXTRA-YOUTUBE.md` e `CLAUDE.md` escolhem a rede pelo pedido; goals pessoais Meta seguem Meta.
- `scripts/escala_serie.py registrar-youtube-json` grava no arquivo pessoal as leituras do MCP sem exigir
  outra consulta à página do vídeo. VAV segue dependente da verificação da conta do operador.

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
