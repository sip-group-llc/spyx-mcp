# Rodada de exemplo (anonimizada)

Exemplo do arquivo que a pessoa grava em `meu/rodadas/`. Nomes e domínios são ilustrativos;
contagens servem apenas para mostrar o formato. A antiga tool `rodada_salvar` não existe no motor atual.

```markdown
# R002 — Renda extra · advertorial com persona · ES

## Hipótese
Frases de funil em espanhol ("haz el test", "plan personalizado") cruzadas com "ingresos extra" trazem
mais quiz de marca sem rosto do que termos diretos ("ganar dinero"). Muda em relação à R001: só
frases de funil, sem termo genérico.

## Plano e cobertura das fontes
`planejar_fontes(rede="meta", pais="ES", alvo="ingresos extra")` foi lido antes da coleta.

| fonte | decisão | resultado ou motivo |
|---|---|---|
| Meta Ad Library | confirmar | 2 buscas válidas; 1 bloqueada, não contada como zero |
| Tyver | usar | 1 página; 5 registros do catálogo para triar |
| Adyntel | usar | 1 página; 3 registros para triar |
| Trendtrack | usar | sessão expirada; bloqueio declarado |
| Foreplay | usar | 1 página; país não filtrado pelo fornecedor |
| AmericanSwipe | condicional | catálogo sem termo ou país; dispensado após cobertura suficiente |
| MineraROI | fora do recorte | catálogo misto sem país, priorizado para BR |
| AdHeart | condicional | dispensado para preservar cota; Meta já trouxe candidatos |
| VAV | fora do recorte | rede exclusiva Meta |
| Anstrex | fora do recorte | native |
| SpyHouse | fora do recorte | push neste conector |

## Buscas
| q | país | IDs | cabeçalho | bloqueada |
|---|---|---|---|---|
| haz el test ingresos extra | ES | 78 | 3.600 | não |
| plan personalizado ingresos | ES | 41 | 1.200 | não |
| descubre si puedes ganar | ES | 0 | — | **sim** (país encerrado por 12 h) |

## Candidatos
| item | destino | IDs no destino | atribuição | personas | > 30 d | leituras | entregável |
|---|---|---|---|---|---|---|---|
| R002-A | quiz.exemplo-a.com | 23 | 0,92 | 4 | 9 | 1 (inventário) | quiz → curso, preço após o teste |
| R002-B | app.exemplo-b.io | 17 na busca inicial | — | — | — | — | **app** (excluído antes da busca por marca) |
| R002-C | exemplo-c.es | 7 | 0,58 | 1 | 2 | 1 (inventário) | marca-pessoa, registrada, não promovida |

## Lacunas
- 3ª frase bloqueada: remedir amanhã.
- R002-A: escala pendente de segunda leitura (D+1).

## Próxima
Após ≥24 h, repetir a mesma busca Meta para R002-A, chamar `medir(novo_job, "quiz.exemplo-a.com")`
e registrar a segunda leitura em `meu/serie-escala.jsonl`; testar as mesmas frases em PT.
```

E o que você disse, gravado em `meu/avaliacoes.jsonl`:

```json
{"data": "2026-09-22T20:10:00+00:00", "rodada": "R002", "item": "A", "veredito": "boa", "motivo": "mecanismo do quiz"}
{"data": "2026-09-22T20:10:00+00:00", "rodada": "R002", "item": "C", "veredito": "ruim", "motivo": null}
```

E o que virou aprendizado, editado em `meu/CRITERIOS-meu.md`:

```
## Hipóteses
- 2026-09-22 · R002-A: em ES, quiz com preço escondido até o fim do teste aparece mais em "haz el test"
  do que em "plan personalizado". Vira preferência se repetir na R003.
```

E a leitura D+0, em `meu/serie-escala.jsonl` via `medir` + `scripts/escala_serie.py registrar-json`:

```
quiz.exemplo-a.com · 2026-09-22 · 23 IDs no destino
  LEITURA 1 — isto e INVENTARIO, nao escala. A ficha declara 'escala: pendente de segunda leitura'.
```
