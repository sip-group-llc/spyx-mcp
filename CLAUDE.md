# HackingAds — operar o minerador com a base de treinamento local

Você opera para UMA pessoa. O **motor** é o MCP `hackingads` (`minerar · status · cancelar · anuncios ·
medir · adheart`); ele coleta e devolve dado. A **base de treinamento** e tudo o que a pessoa aprende
moram nesta pasta, em `.md` que você lê e edita diretamente.

## Onde está o quê

| Pasta | O que é | Você |
|---|---|---|
| `base/` | o critério do operador: `CRITERIOS.md`, `README.md` (o ciclo), `METRICAS.md`, `GOAL-*.md` | **lê, nunca edita** — `git pull` atualiza |
| `meu/` | o que é da pessoa: `CRITERIOS-meu.md`, `goals/`, `rodadas/`, `avaliacoes.jsonl`, `serie-escala.jsonl`, `dados/` | **escreve só aqui** |
| `scripts/escala_serie.py` | a série da REGRA PRIMORDIAL (`registrar-json`, `ver`) | roda |

Conflito entre `base/` e `meu/`: `meu/` vence, porque é a pessoa refinando o critério dela. Anote a
divergência em `meu/CRITERIOS-meu.md` com data e origem.

## O ciclo (é o de `base/README.md`, "Ciclo por prompt")

0. **Alvo.** A pessoa aponta um goal em `meu/goals/` ou diz o alvo; nesse caso crie o arquivo a partir
   de `meu/goals/GOAL-EXEMPLO.md`. Região vazia: UMA pergunta, nenhuma busca antes.
1. **Preparar.** Ler `base/CRITERIOS.md` (REGRA PRIMORDIAL e ASSINATURAS primeiro), `meu/CRITERIOS-meu.md`
   inteiro, as 3 últimas `meu/rodadas/` e `meu/avaliacoes.jsonl`. Declarar hipótese, rede, país, frases
   e o que muda em relação à rodada anterior.
2. **Minerar.** `minerar(q, pais)` → `status(job)` a cada ~2 min até `pronto`. Uma coleta por vez.
   `bloqueada=true` **não é contagem**: encerre o país por ~12 h e registre a lacuna. Salve o resumo em
   `meu/dados/<job>.json`. `anuncios(job, destino)` traz o bruto (id, início, Página, destino, copy): é com
   ele que você conta Páginas-persona por destino, lê o funil e confere atribuição.
3. **Revisar.** Abrir a landing (WebFetch) **antes** de contar por marca. Fora: app, SaaS, serviço,
   corretora, vaga, físico, micronovela. Distinguir anúncio, página, domínio e oferta.
4. **Ouvir.** A pessoa avalia ("R003-B ruim pelo produto"). Acrescente uma linha em `meu/avaliacoes.jsonl`:
   `{"data","rodada","item","veredito","motivo"}` — veredito `boa|ruim|incerta`, motivo omitido = `null`.
   Sua hipótese nunca preenche a avaliação dela.
5. **Refinar.** Editar `meu/CRITERIOS-meu.md` e `meu/goals/*.md` diretamente: promover hipótese, retirar
   o que refutou, reescrever frases. Um exemplo gera hipótese, não regra.
6. **Medir.** `medir(job, chave)` devolve a leitura pronta → salve em `meu/dados/<job>-<chave>.json` →
   `python scripts/escala_serie.py registrar-json --de meu/dados/<arquivo>`. `ver --chave <chave>` mostra a
   série. **1 leitura = inventário**; "indícios de escala" só com 2 leituras separadas por ≥ 24 h.

**Fechar:** `meu/rodadas/Rnnn.md` no formato de `docs/rodada-exemplo.md`.

## Tradução: a base foi escrita para o ambiente do operador

| Onde a base diz | Aqui é |
|---|---|
| `scripts/adlib_coleta.py --proxy auto` | `minerar(q, pais)` — o proxy já vem embutido |
| `scripts/triar_destinos.py` | o campo `triagem` do `status(job)` |
| `scripts/escala_serie.py registrar --de <json>` / `remedir` | `medir(job, chave)` + `scripts/escala_serie.py registrar-json`; remedir = `minerar` de novo com a mesma frase, depois `medir` |
| `scripts/adlib_paginas.py` (seguidores da Página) | não existe; tente WebFetch na Página, senão escreva "seguidores: não medido" |
| `scripts/adheart_frases.py` | `minerar(fonte="adheart")` + `adheart(aprovar|descartar)` |
| `arasaka.py doctor`, `/meus`, favoritas, utilizadas | não existem; a exclusão da pessoa é a seção *Exclusões* de `meu/CRITERIOS-meu.md` |
| `atc_*`, `vav_*`, Google/YouTube | não coberto: registre "Google: não sondado" |
| `D:/Projetos/…`, `outputs/<sessão>/` | esta pasta e `meu/dados/` |
| `OFERTAS-MAPEADAS.md`, rodadas R0xx do operador | não vêm no pacote; o que a pessoa mapeou fica em `meu/` |

## Regras

- Nunca escreva em `base/`. Nunca invente avaliação. Número só com leitura, e "escala" só com a série.
- Responda em português. Ao terminar uma rodada, diga o que foi salvo em `meu/` e o que fica pendente.
