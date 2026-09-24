# GOAL — <nicho> · <padrão> · <região> · <rede>

> Copie este arquivo com outro nome, preencha os `<campos>` e refine a cada rodada: este arquivo é seu.
> Para Meta, leia `base/GOAL-RENDA-EXTRA.md` e `base/GOAL-ADVERTORIAL.md`.
> Para YouTube, leia `base/GOAL-RENDA-EXTRA-YOUTUBE.md`. Copie apenas a seção da rede escolhida.

Encontrar e auditar as ofertas de **<nicho>** no padrão **<padrão: ex. advertorial com persona — marca
sem rosto, Páginas-persona, quiz>** mais escaladas em **<região>** e entregar **<quantidade: ex. até 3
finalistas com evidência própria da rede>**, NOVAS (fora das exclusões em `meu/CRITERIOS-meu.md`), sem audiência
própria. Rede: <Meta, YouTube ou ambas>.

**Antes de ativar este goal:** executar `docs/goal-preflight.md`, preencher nicho, rede e país/região,
mostrar o texto final à pessoa e esperar aprovação explícita. `base/CRITERIOS.md` (REGRA PRIMORDIAL,
ASSINATURAS), `meu/CRITERIOS-meu.md`, `meu/DESCOBERTAS.md` quando existir e últimas 3 rodadas entram
na exclusão e na hipótese inicial.

**Plano das fontes (depois da aprovação do Goal):**
`planejar_fontes(rede="<meta|youtube|ambas>", pais="<PAIS>", alvo="<termo local>")`.
Registrar as dez fontes como elegíveis, condicionais ou fora do recorte, com motivo.
Usar cada fonte elegível em lote limitado; `fontes()` mostra último teste, que pode
estar vencido. [Roteamento e limites](../../docs/fontes.md).

**Busca Meta — descobrir, depois medir (use somente quando a rede incluir Meta):**
1. Meta Ad Library por frase ampla para o primeiro inventário. Complementar candidatos
   com Tyver, Adyntel, Trendtrack e Foreplay se o plano os marcar elegíveis;
   AmericanSwipe e MineraROI são catálogos para filtrar localmente com
   `minerador_resultados(filtro="<nicho>")`. AdHeart é condicional e consome cota
   por termo; use poucos termos amplos quando acrescentar cobertura útil.
2. Medir na Meta, na ordem **volume → assinatura → formato**: primeiro o termo que o nicho inteiro usa
   (<ex.: "renda extra", "ganhar dinheiro online">), depois a assinatura pra separar, e só então frase de
   FUNIL (<"faça o teste", "plano personalizado", "descubra se">) pra achar o quiz que o termo comum não pega.
   Nunca termo de recrutamento/vaga. **Alterne o país a cada busca** (1–2 por país e a Meta trava ~12 h).
   `bloqueada=true` não é contagem. Agrupar por destino; usar a `triagem` do `status` antes de contar por marca.
3. **Piso**: <≥ N IDs no mesmo destino — na 1ª rodada de um mercado novo, deixe em branco e fixe a partir do
   maior destino medido>.

**Busca YouTube (use somente quando a rede incluir YouTube):**
1. `google(modo="descobrir", q="<1–3 termos locais separados por ;>", pais)` → `status(job, esperar=60)`
   → `google_resultados(job)`. Para cada domínio candidato: `google(modo="dominio", q="<host>", pais)`.
2. `minerador(fonte="vav", modo="catalogo", q="", pais)` lê anúncios no país;
   `modo="leaderboard", max_pages=1` acha canais e `modo="channel_id",
   q="<id>"` abre seus anúncios. `modo="dominio", q="<host>"` liga destino
   a vídeo. Canal/domínio não filtram país: confirme entrega no ATC.
3. `youtube_video(ids, pais="<PAIS>")` para os vídeos ligados a creative_id. Salve as leituras em `meu/dados/` e registre
   com `scripts/escala_serie.py registrar-youtube-json`; repita os mesmos IDs após ≥24 h.
4. Confirme anúncio pago, destino, país, canal e entregável. Poucos criativos ATC não reprovam YouTube;
   vídeo listado pode ter views orgânicas. Sem video_id, declare a lacuna.

**Entregável antes da contagem:** abrir a landing. Fora: app, SaaS, serviço, corretora, vaga, físico,
micronovela. Persona nova da mesma operação não é oferta nova.

**Audiência:** na Meta, verificar Páginas-persona com `anuncios(job, destino)` e `paginas(q, pais)`;
no YouTube, verificar canal e produtor. Marca-pessoa ou audiência grande: registrar, não promover.

**Escala:** contagem única é inventário. Meta usa `medir` + `registrar-json`; YouTube usa views +
`registrar-youtube-json`. "Escalada" só com 2 leituras comparáveis ≥24 h.

**Fechar:** `meu/rodadas/Rnnn.md` com cobertura e finalistas comprovados **mais os 3–5 melhores achados
parciais**, links e limites. Registrar achados relevantes em `meu/DESCOBERTAS.md` para não reapresentá-los
como inéditos. Só após avaliação explícita da pessoa escrever em `meu/avaliacoes.jsonl` e refinar
este goal e `meu/CRITERIOS-meu.md`.
