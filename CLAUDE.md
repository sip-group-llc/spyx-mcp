# HackingAds — operar o minerador com a base de treinamento local

Você opera para UMA pessoa. O **motor** é o MCP `hackingads` (`minerar · google · google_resultados ·
youtube_video · status · cancelar · anuncios · paginas · medir · adheart`); ele coleta e devolve dado.
O proxy por país já vem embutido em `minerar`, `paginas` e `google`. A **base de treinamento** e tudo o que a pessoa aprende
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
| `base/GOAL-*.md` | goals do operador: `ADVERTORIAL`, `RENDA-EXTRA` (Meta), `RENDA-EXTRA-YOUTUBE` e `RELACIONAMENTO` | ao criar ou refinar um goal em `meu/goals/` |
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

0. **Alvo e rede.** A pessoa aponta um goal em `meu/goals/` ou diz o alvo; nesse caso crie o arquivo a partir
   de `meu/goals/GOAL-EXEMPLO.md`. Goal com "Rede única: Meta" continua Meta; pedido de YouTube usa
   `base/GOAL-RENDA-EXTRA-YOUTUBE.md` como referência. Pedido genérico sem rede cobre Meta e Google/YouTube,
   sem deixar os goals Meta antigos escolherem a rede por ele. Região vazia: UMA pergunta, nenhuma busca antes.
1. **Preparar.** Ler `base/CRITERIOS.md` (REGRA PRIMORDIAL e ASSINATURAS primeiro), `meu/CRITERIOS-meu.md`
   inteiro, as 3 últimas `meu/rodadas/` e `meu/avaliacoes.jsonl`. Declarar hipótese, rede, país, frases
   e o que muda em relação à rodada anterior.
2. **Minerar — descobrir primeiro, medir depois, na rede do pedido.** Na frente Meta, siga a lição da R001: começar
   por frase de funil na Meta devolveu 107 anúncios no país inteiro e a 2ª busca travou.)
    - **Descobrir candidatos Meta**: `minerar(fonte="adheart", q="<1–2 termos AMPLOS do nicho>", pais,
     sort="total_reach", max_pages=8)`. Vem ordenado por alcance, com amostra; é a única fonte que ranqueia.
     **Cota é por termo** (a tool recusa mais de 2): no máximo 4 chamadas por rodada; página funda é grátis.
   - **Medir e atribuir na Meta**: `minerar(q, pais)` → `status(job, esperar=60)` até `pronto` (a espera
     é no servidor; nunca chame `status` em sequência sem `esperar`). Ordem das
     frases: **volume → assinatura → formato** (termo comum do nicho primeiro; frase de funil só para achar o
     quiz que o termo comum não pega). **1 a 2 buscas por país e a Meta trava por ~12 h**: alterne o país a
     cada busca e não repita país na mesma hora. Uma coleta por vez.
   - `bloqueada=true` **não é contagem**: encerre o país por ~12 h e registre a lacuna. Salve o resumo em
     `meu/dados/<job>.json`. `anuncios(job, destino)` traz o bruto (id, início, Página, destino, copy): é com
     ele que você conta Páginas-persona por destino, lê o funil e confere atribuição.
    - **Piso por mercado**: o "≥ 150 IDs" da base foi medido em DE/IT/ES. Num mercado novo, a 1ª rodada mede o
      teto real (maior destino da busca de volume) e o goal da pessoa fixa o piso a partir dele; até lá,
      candidato com a assinatura certa entra como inventário, não some.
   Na frente **Google/YouTube**, descubra pelo próprio ATC: `google(modo="descobrir", q="termo1;termo2", pais)` →
   `status(job, esperar=60)` → `google_resultados(job)`. Sonde candidatos por `google(modo="dominio", q="host", pais)`.
   Leia `cobertura`: o limite global de anunciantes é uma amostra, e sugestões não sondadas não são resultados
   negativos. `dominios_observados` são pistas; a prévia do Google não é landing nem prova do produto.
   Use os `video_id` ligados a `creative_id` para `youtube_video(ids)` e salve a resposta em `meu/dados/`.
   Uma leitura de views é inventário; repita os mesmos vídeos após ≥24 h e registre cada resposta com
   `python scripts/escala_serie.py registrar-youtube-json --de meu/dados/<arquivo> --oferta <host> --rodada Rnnn`.
   ATC sem `video_id` é lacuna, não ausência de anúncio. Um vídeo listado pode ter views orgânicas;
   confirme anúncio, destino, país e audiência antes de promover. VAV não integra o MCP enquanto a sessão
   exigir verificação do operador; a rota ATC → vídeo funciona sem ele.
3. **Revisar.** Abrir a landing (WebFetch) **antes** de contar por marca. Fora: app, SaaS, serviço,
   corretora, vaga, físico, micronovela. Distinguir anúncio, página, domínio e oferta.
4. **Ouvir.** A pessoa avalia ("R003-B ruim pelo produto"). Acrescente uma linha em `meu/avaliacoes.jsonl`:
   `{"data","rodada","item","veredito","motivo"}` — veredito `boa|ruim|incerta`, motivo omitido = `null`.
   Sua hipótese nunca preenche a avaliação dela.
5. **Refinar.** Editar `meu/CRITERIOS-meu.md` e `meu/goals/*.md` diretamente: promover hipótese, retirar
   o que refutou, reescrever frases. Um exemplo gera hipótese, não regra.
6. **Medir.** Na Meta, `medir(job, chave)` devolve a leitura pronta → salve em `meu/dados/<job>-<chave>.json` →
   `python scripts/escala_serie.py registrar-json --de meu/dados/<arquivo>`. `ver --chave <chave>` mostra a
   série. No YouTube, registre `youtube_video()` com `registrar-youtube-json`; repita o mesmo `video_id` ≥24 h.
   **1 leitura = inventário**; "indícios de escala" só com 2 leituras separadas por ≥ 24 h.

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
| `atc_descoberta.py`, `atc_sonda_dominio.py`, `atc_videos.py` | `google(descobrir|dominio)` → `status` → `google_resultados` |
| página do vídeo YouTube | `youtube_video(ids)` → `registrar-youtube-json` no arquivo pessoal |
| VAV | sessão do fornecedor em verificação; declare indisponibilidade quando fizer diferença |
| `D:/Projetos/…`, `outputs/<sessão>/` | esta pasta e `meu/dados/` |
| `OFERTAS-MAPEADAS.md`, rodadas R0xx do operador | não vêm no pacote; o que a pessoa mapeou fica em `meu/` |

## Rodar até o fim: o texto do `/goal`

Uma rodada inteira (descobrir → medir → revisar → série → relatório) leva horas e várias buscas com
espera. Sem um modo de objetivo, cada turno seu termina no fim de um passo e a pessoa precisa te cutucar.
Por isso, **quando a pessoa pedir uma rodada inteira ("minera X em Y", "traz os mais escalados de…"),
responda SÓ com o texto pronto pra ela colar no `/goal` do app e PARE — sem chamar tool nenhuma.**
Regra mecânica: se a mensagem da pessoa não contém a linha `CONDIÇÃO DE PARADA`, ela ainda não colou o
`/goal`; entregue o texto (≤ 4.000 caracteres, sem markdown pesado, terminando na linha `CONDIÇÃO DE
PARADA: …`), montado a partir do goal em `meu/goals/`:

- alvo (nicho, região, rede, padrão, quantidade), a ordem de descoberta e medida da rede selecionada
  (Meta: AdHeart → Meta; YouTube: ATC → vídeo → views), o gate do entregável, a regra primordial, e o que
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
