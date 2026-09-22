# HackingAds — operar o minerador com a base de treinamento local

Você opera para UMA pessoa. O **motor** é o MCP `hackingads` (`minerar · status · cancelar · anuncios ·
paginas · medir · adheart`); ele coleta e devolve dado. O proxy por país já vem embutido em `minerar` e
`paginas`: você não configura nada disso. A **base de treinamento** e tudo o que a pessoa aprende
moram nesta pasta, em `.md` que você lê e edita diretamente.

## Onde está o quê

| Pasta | O que é | Você |
|---|---|---|
| `base/` | o critério do operador: `CRITERIOS.md`, `README.md` (o ciclo), `METRICAS.md`, `GOAL-*.md` | **lê, nunca edita** — `git pull` atualiza |
| `meu/` | o que é da pessoa: `CRITERIOS-meu.md`, `goals/`, `rodadas/`, `avaliacoes.jsonl`, `serie-escala.jsonl`, `dados/` | **escreve só aqui** |
| `scripts/escala_serie.py` | a série da REGRA PRIMORDIAL (`registrar-json`, `ver`) | roda |

Conflito entre `base/` e `meu/`: `meu/` vence, porque é a pessoa refinando o critério dela. Anote a
divergência em `meu/CRITERIOS-meu.md` com data e origem.

## A base, por dentro

| Arquivo | O que é | Quando ler |
|---|---|---|
| `base/CRITERIOS.md` | o critério inteiro: **REGRA PRIMORDIAL** (topo, vence tudo), **ASSINATURAS** do advertorial agressivo, regra de navegação e planilha, preferências confirmadas, hipóteses e lições datadas com origem | as duas primeiras seções em toda rodada; o resto na primeira sessão e quando uma lição for citada |
| `base/README.md` | o laboratório: o ciclo em 6 passos, contratos dos arquivos, índice das rodadas do operador (R001…) | primeira sessão; "Ciclo por prompt" em toda rodada |
| `base/METRICAS.md` | campos obrigatórios de cada candidato e limites de interpretação (o que um número prova e o que não prova) | ao escrever a ficha de um candidato |
| `base/GOAL-*.md` | goals do operador: `ADVERTORIAL` (o método-mãe), `RENDA-EXTRA`, `RELACIONAMENTO`. Cada um tem versão curta (o que se cola) e procedimento completo | ao criar ou refinar um goal em `meu/goals/` |
| `meu/CRITERIOS-meu.md` | o que a pessoa aprendeu por cima da base; vence a base em conflito | inteiro, em toda rodada |

A base é escrita em primeira pessoa pelo operador e cita rodadas dele (R017, R018…) que **não vêm no pacote**:
trate a citação como evidência de método, não como arquivo a abrir.

## Quando o operador atualizar a base

`git pull` traz `base/` nova e nunca toca em `meu/`. Depois de um pull, antes da rodada:

```bash
git log --oneline -5 -- base/ && git diff HEAD~1 --stat -- base/
```

Leia o que mudou (em geral CRITERIOS ou um GOAL) e verifique se contradiz algo em `meu/CRITERIOS-meu.md`;
se contradisser, `meu/` vence, e você registra a divergência com data. `CHANGELOG.md` diz o que mudou no
pacote e no motor (tools novas ou renomeadas).

## O ciclo (é o de `base/README.md`, "Ciclo por prompt")

0. **Alvo.** A pessoa aponta um goal em `meu/goals/` ou diz o alvo; nesse caso crie o arquivo a partir
   de `meu/goals/GOAL-EXEMPLO.md`. Região vazia: UMA pergunta, nenhuma busca antes.
1. **Preparar.** Ler `base/CRITERIOS.md` (REGRA PRIMORDIAL e ASSINATURAS primeiro), `meu/CRITERIOS-meu.md`
   inteiro, as 3 últimas `meu/rodadas/` e `meu/avaliacoes.jsonl`. Declarar hipótese, rede, país, frases
   e o que muda em relação à rodada anterior.
2. **Minerar — descobrir primeiro, medir depois.** (Lição da R001 do primeiro fork, 22/09/2026: começar
   por frase de funil na Meta devolveu 107 anúncios no país inteiro e a 2ª busca travou.)
   - **Descobrir os mais escalados**: `minerar(fonte="adheart", q="<2–3 termos AMPLOS do nicho>", pais,
     sort="total_reach")`. Vem ordenado por alcance, com amostra; é a única fonte que ranqueia. Gasta cota
     por termo: poucos termos, páginas fundas.
   - **Medir e atribuir na Meta**: `minerar(q, pais)` → `status(job)` a cada ~2 min até `pronto`. Ordem das
     frases: **volume → assinatura → formato** (termo comum do nicho primeiro; frase de funil só para achar o
     quiz que o termo comum não pega). **1 a 2 buscas por país e a Meta trava por ~12 h**: alterne o país a
     cada busca e não repita país na mesma hora. Uma coleta por vez.
   - `bloqueada=true` **não é contagem**: encerre o país por ~12 h e registre a lacuna. Salve o resumo em
     `meu/dados/<job>.json`. `anuncios(job, destino)` traz o bruto (id, início, Página, destino, copy): é com
     ele que você conta Páginas-persona por destino, lê o funil e confere atribuição.
   - **Piso por mercado**: o "≥ 150 IDs" da base foi medido em DE/IT/ES. Num mercado novo, a 1ª rodada mede o
     teto real (maior destino da busca de volume) e o goal da pessoa fixa o piso a partir dele; até lá,
     candidato com a assinatura certa entra como inventário, não some.
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
| `scripts/adlib_paginas.py --seguidores` (gate AUDIÊNCIA/PERSONAS) | `paginas(q, pais)` → `status(job)`: seguidores, "seguindo 0", categoria e e-mail por Página |
| `scripts/adheart_frases.py` | `minerar(fonte="adheart")` + `adheart(aprovar|descartar)` |
| `arasaka.py doctor`, `/meus`, favoritas, utilizadas | não existem; a exclusão da pessoa é a seção *Exclusões* de `meu/CRITERIOS-meu.md` |
| `atc_*`, `vav_*`, Google/YouTube | não coberto: registre "Google: não sondado" |
| `D:/Projetos/…`, `outputs/<sessão>/` | esta pasta e `meu/dados/` |
| `OFERTAS-MAPEADAS.md`, rodadas R0xx do operador | não vêm no pacote; o que a pessoa mapeou fica em `meu/` |

## Rodar até o fim: o texto do `/goal`

Uma rodada inteira (descobrir → medir → revisar → série → relatório) leva horas e várias buscas com
espera. Sem um modo de objetivo, cada turno seu termina no fim de um passo e a pessoa precisa te cutucar.
Por isso, **quando a pessoa pedir uma rodada inteira ("minera X em Y", "traz os mais escalados de…"),
antes de começar entregue o texto pronto pra ela colar no `/goal` do app** (≤ 4.000 caracteres, sem
markdown pesado), montado a partir do goal em `meu/goals/`:

- alvo (nicho, região, padrão, quantidade), a ordem descobrir (AdHeart por alcance) → medir (Meta,
  volume → assinatura → formato, alternando país), o gate do entregável, a regra primordial, e o que
  fechar (`meu/rodadas/Rnnn.md`, avaliações, série, refinar `meu/`);
- a condição de parada explícita: "só pare quando a rodada estiver escrita em `meu/rodadas/` com os
  candidatos medidos ou a lacuna registrada; `bloqueada` num país não encerra a rodada, alterna o país";
- o que **não** é motivo pra parar: esperar `status` (chame de novo), fila, uma busca vazia.

Se a pessoa já colou o `/goal`, execute sem parar entre passos: espera de coleta é `status` repetido,
não fim de turno. Alternativas quando não há `/goal`: no Claude Code de terminal, `/loop 5m <mesmo
texto>`; ou a pessoa manda "continua" e você retoma de `meu/rodadas/` e `meu/dados/`.

## Primeira sessão

Se `.mcp.json` ainda tem `<SUA_CHAVE>`, ou uma tool do motor responder "chave inválida", pare e peça à
pessoa a chave que o operador mandou: sem ela nada do motor funciona. Se `meu/` estiver vazio, explique
o ciclo em poucas linhas e peça o alvo (nicho, região, padrão); crie o goal a partir de
`meu/goals/GOAL-EXEMPLO.md`.

## Regras

- Nunca escreva em `base/`. Nunca invente avaliação. Número só com leitura, e "escala" só com a série.
- Responda em português. Ao terminar uma rodada, diga o que foi salvo em `meu/` e o que fica pendente.
