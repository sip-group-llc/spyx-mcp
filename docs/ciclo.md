# O ciclo de uma rodada

Cada rodada é uma conversa. O Claude segue o `CLAUDE.md`; você entra no alvo (0) e no veredito (4).
Motor = tools do MCP. Memória = arquivos em `meu/`.

## 0. Alvo

Um arquivo em `meu/goals/` (comece por `GOAL-EXEMPLO.md`). Nicho, região, padrão, quantidade. O método
(frases por idioma, exclusões, gate de escala) já está na base; você refina o seu goal quando quiser,
editando o `.md`.

## 1. Preparar

Lê `base/CRITERIOS.md` (REGRA PRIMORDIAL e ASSINATURAS primeiro), `meu/CRITERIOS-meu.md`, as 3 últimas
`meu/rodadas/` e `meu/avaliacoes.jsonl`. Declara hipótese, rede, país, frases e o que muda em relação à
rodada anterior.

## 2. Minerar

`minerar(q, pais)` → `status(job)` até `pronto` → `anuncios(job, destino)` pro dado bruto.

Frases de funil cruzadas com o nicho, no idioma do país. Uma coleta por vez. `bloqueada=true` **não é
contagem**: país encerrado por algumas horas, lacuna registrada. Enquanto roda, `status` mostra minutos e
avisa se a sessão travou; `cancelar(job)` interrompe.

## 3. Revisar

Abrir a landing **antes** de contar por marca. Fora: app, SaaS, serviço, corretora, vaga, físico,
micronovela. Com o bruto de `anuncios`: Páginas-persona por destino, copy, atribuição. Com
`paginas(q, pais)`: seguidores e categoria de cada Página (persona = 1–350 seguidores, "seguindo 0";
≥ 10 mil = marca, registrar sem promover).

## 4. Ouvir

Você diz "R003-B ruim pelo produto". Vira uma linha em `meu/avaliacoes.jsonl`, com as suas palavras. Motivo
que você não deu fica `null`.

## 5. Refinar

O Claude edita `meu/CRITERIOS-meu.md` e `meu/goals/*.md`: promove hipótese, retira o que refutou,
reescreve frase. Um exemplo é hipótese; vira regra quando repete.

## 6. Medir

`medir(job, chave)` → `scripts/escala_serie.py registrar-json` → série em `meu/serie-escala.jsonl`.

| Leituras | O que pode ser escrito |
|---|---|
| 1 | **inventário** — "escala: pendente de segunda leitura" |
| 2+, separadas por ≥ 24 h, mesmo método | **indícios de escala** — sempre com a série ao lado |

Atribuição e persistência valem com uma leitura. Tamanho, não.

## Fechar

`meu/rodadas/Rnnn.md`: hipótese, buscas, candidatos (inventário/atribuição/persistência/personas),
lacunas, o que muda na próxima. A próxima rodada começa lendo isto.
