# Rodada de exemplo (anonimizada)

O que `rodada_salvar("R002", …)` guarda. Nomes de oferta e domínios trocados; números reais de uma rodada de teste.

```markdown
# R002 — Renda extra · advertorial com persona · ES

## Hipótese
Frases de funil em espanhol ("haz el test", "plan personalizado") cruzadas com "ingresos extra" trazem
mais quiz de marca sem rosto do que termos diretos ("ganar dinero"). Muda em relação à R001: só
frases de funil, sem termo genérico.

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
| R002-B | app.exemplo-b.io | 17 | 1,00 | 3 | 11 | — | **app** (descartado antes da contagem) |
| R002-C | exemplo-c.es | 7 | 0,58 | 1 | 2 | 1 (inventário) | marca-pessoa, registrada, não promovida |

## Lacunas
- 3ª frase bloqueada: remedir amanhã.
- R002-A: escala pendente de segunda leitura (D+1).

## Próxima
Remedir R002-A em D+1 com `escala("quiz.exemplo-a.com", job)`; testar as mesmas frases em PT.
```

E o que você disse, gravado com `avaliar`:

```json
{"rodada": "R002", "item": "A", "veredito": "boa", "motivo": "mecanismo do quiz"}
{"rodada": "R002", "item": "C", "veredito": "ruim", "motivo": null}
```

E o que virou aprendizado, com `anotar`:

```
## hipotese · 2026-09-22 · R002-A
Em ES, quiz com preço escondido até o fim do teste aparece mais em "haz el test" do que em "plan personalizado".
```
