# Tools

Gerado de `mcp_minerador.py` por `gerar_docs.py` — não edite à mão.

`?` marca argumento opcional. Toda tool exige a sua chave no header `Authorization`.

## `minerar(q: string, pais?: string, fonte?: string, search_type?: string, max_rodadas?: integer, nicho?: string, max_pages?: integer, last_active?: integer, sort?: string)`

Coleta anúncios NO AR agora. Duas fontes com papéis diferentes: `fonte="adheart"` = DESCOBRIR os mais escalados do nicho: busca por termo (q = termos amplos separados por vírgula, pais = br/de/us…), `sort="total_reach"` (alcance, o default) ou `"creation_date"` (recentes); GASTA COTA por termo, então poucos termos amplos e páginas fundas. Devolve staging_id + amostra — nada entra no acervo até adheart(acao="aprovar"). `fonte="meta"` = MEDIR e ATRIBUIR: Biblioteca de Anúncios (q = frase; rola até o platô no país; devolve `job` — status(job), 2–10 min). Uma coleta Meta por vez; 1–2 buscas por país e a fonte trava por ~12 h: comece por termo de volume, alterne país entre buscas.

## `google(q: string, pais?: string, modo?: string, max_pages?: integer, max_anunciantes?: integer, max_videos?: integer)`

Google/YouTube sem depender da Meta. `modo="descobrir"`: q = 1–3 termos do nicho separados por `;`, retorna anunciantes ATC, domínios observados e IDs dos vídeos pagos encontrados nos previews. `modo="dominio"`: q = hostname de uma oferta; mede inventário, datas, anunciantes e vídeos do domínio. Uma consulta ATC por vez, limites explícitos: páginas <=10, anunciantes <=12, vídeos <=10. Devolve job: use status(job, esperar=60), depois google_resultados(job). O ATC confirma anúncio pago, mas contagem de criativos não mede escala no YouTube; use youtube_video() e a série >=24h.

## `google_resultados(job: string, pagina?: integer, por_pagina?: integer)`

Resultados de google() paginados por anunciante/domínio, com IDs de vídeos e creative_id. Só a pessoa que iniciou o job pode ler. Vídeo sem ID ou domínio é lacuna explícita, não zero de escala.

## `youtube_video(ids: string, pais?: string)`

Lê 1–3 vídeos públicos do YouTube por video_id: views, publicação, não listado, canal e inscritos, com horário UTC. A leitura isolada é inventário; repita os mesmos IDs após >=24h para medir views/dia. Um ID vindo do ATC liga o vídeo a anúncio pago; views sozinhas não provam entrega paga nem vendas.

## `paginas(q: string, pais?: string)`

O gate AUDIÊNCIA/PERSONAS: abre o perfil de cada Página que anuncia na busca `q` no país e devolve seguidores, "seguindo 0", categoria e e-mail — por Página. Job em segundo plano (1–5 min, entra na mesma fila da Meta): acompanhe com status(job). Persona = 1–350 seguidores, "Blog pessoal"; Página ≥ 10 mil = marca, registrar sem promover.

## `cancelar(job: string)`

Interrompe um job de minerar(), paginas() ou google() que ainda está rodando. O que já foi coletado não é aproveitado; o job vira `cancelado`.

## `status(job: string, esperar?: integer)`

Andamento ou resultado de um job de minerar()/paginas()/google(): rodando (minutos, últimas linhas, dica se a sessão travou) ou pronto (cabeçalho, IDs, bloqueada, destinos por hostname e triagem pela assinatura do advertorial). `esperar=60` segura a resposta no servidor até 60 s enquanto o job roda — use SEMPRE em vez de chamar em sequência. Guarde o resumo em meu/dados/<job>.json; o dado bruto vem por anuncios(job).

## `anuncios(job: string, destino?: string, pagina?: integer, por_pagina?: integer)`

O dado bruto de um job pronto, paginado: por anúncio, id, data de início, nome da Página, destino (hostname) e a copy resumida. Filtre por `destino` pra contar Páginas-persona de uma oferta e ler o funil. Salve o que usar em meu/dados/.

## `medir(job: string, chave: string, rodada?: string)`

REGRA PRIMORDIAL: a leitura de um job pronto para o destino `chave` (hostname), com os quatro eixos (inventário, atribuição, personas, persistência), pronta pra sua série local: `python scripts/escala_serie.py registrar-json --de <arquivo>`. Leitura bloqueada nunca vira medida. 1 leitura = inventário; só 2 leituras separadas por ≥24 h autorizam "indícios de escala".

## `adheart(acao: string, staging_id: string)`

Fecha uma busca AdHeart: `aprovar` baixa o staging para o acervo (aí entra no ranking); `descartar` apaga.

# Prompt
