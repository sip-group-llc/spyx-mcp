# O ciclo de uma rodada

Cada rodada é uma conversa. O Claude segue o `CLAUDE.md`; você entra no alvo (0) e no veredito (4).
Motor = tools do MCP. Memória = arquivos em `meu/`.

## 0. Alvo

Um arquivo em `meu/goals/` (comece por `GOAL-EXEMPLO.md`). Nicho, região, **rede**, padrão, quantidade. O método
(frases por idioma, exclusões, gate de escala) já está na base; você refina o seu goal quando quiser,
editando o `.md`.

Antes de ativar `/goal`, siga [o pré-voo](goal-preflight.md): resolva país e campos ausentes, mostre o
texto final e espere a aprovação explícita da pessoa. O texto enviado em conversa é um rascunho.

## 1. Preparar

Lê `base/CRITERIOS.md` (REGRA PRIMORDIAL e ASSINATURAS primeiro), `meu/CRITERIOS-meu.md`, as 3 últimas
`meu/rodadas/` e `meu/avaliacoes.jsonl`. Declara hipótese, rede, país, frases e o que muda em relação à
rodada anterior.

## 2. Minerar

**Meta:** `minerar(fonte="adheart", ...)` para descobrir; `minerar(q, pais)` → `status(job)` até `pronto`
→ `anuncios(job, destino)` para o bruto.

**Google/YouTube:** `google(modo="descobrir", ...)` → `status(job)` → `google_resultados(job)`;
`google(modo="dominio", q="<host>", pais)` para sondar a oferta. Com `video_id` ligado ao criativo,
`youtube_video(ids)` mede views, data, não listado e canal. Salve a leitura em `meu/dados/`.

Termos do nicho no idioma do país. Uma coleta por fonte por vez. Na Meta, `bloqueada=true` **não é
contagem**: país encerrado por algumas horas, lacuna registrada. Enquanto roda, `status` mostra minutos e
avisa se a sessão travou; `cancelar(job)` interrompe.

## 3. Revisar

Abrir a landing **antes** de contar por marca. Fora: app, SaaS, serviço, corretora, vaga, físico,
micronovela. Com o bruto de `anuncios`: Páginas-persona por destino, copy, atribuição. Com
`paginas(q, pais)`: seguidores e categoria de cada Página (persona = 1–350 seguidores, "seguindo 0";
≥ 10 mil = marca, registrar sem promover). No YouTube, confirme o elo anúncio → vídeo → destino e
verifique canal, produtor e entregável; vídeo listado pode acumular views orgânicas.

## 4. Ouvir

Você diz "R003-B ruim pelo produto". Vira uma linha em `meu/avaliacoes.jsonl`, com as suas palavras. Motivo
que você não deu fica `null`.

## 5. Refinar

O Claude edita `meu/CRITERIOS-meu.md` e `meu/goals/*.md`: promove hipótese, retira o que refutou,
reescreve frase. Um exemplo é hipótese; vira regra quando repete.

## 6. Medir

Meta: `medir(job, chave)` → `scripts/escala_serie.py registrar-json`. YouTube: salve a resposta de
`youtube_video(ids)` → `scripts/escala_serie.py registrar-youtube-json --de <arquivo> --oferta <host> --rodada Rnnn`.
Ambos gravam a série em `meu/serie-escala.jsonl`.

| Leituras | O que pode ser escrito |
|---|---|
| 1 | **inventário** — "escala: pendente de segunda leitura" |
| 2+, separadas por ≥ 24 h, mesmo método | **indícios de escala** — sempre com a série ao lado |

Atribuição e persistência valem com uma leitura. Tamanho, não.

## Fechar

`meu/rodadas/Rnnn.md`: hipótese, buscas, candidatos (inventário/atribuição/persistência/personas),
lacunas, o que muda na próxima. Entregue também o ranking dos melhores achados abaixo do gate, mesmo com
zero finalistas, e grave descobertas relevantes em `meu/DESCOBERTAS.md` como inventário ou hipótese. A
próxima rodada começa lendo ambos.
