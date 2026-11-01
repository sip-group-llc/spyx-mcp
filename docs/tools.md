# Tools

Gerado de `mcp_minerador.py` por `gerar_docs.py` — não edite à mão.

`?` marca argumento opcional. Toda tool exige a sua chave no header `Authorization`.

## `conta_identidade()`

Confirma a conta da chave pessoal ar_ deste conector. Não associa por nome nem usa chave do operador.

## `conta_saldo()`

Créditos disponíveis, reservados e consumidos da sua conta; não compra nem renova plano.

## `conta_extrato(limite?: integer)`

Últimos lançamentos de créditos da sua conta, até 100.

## `acervo_buscar(idioma?: string, rede?: string, nicho?: string, escalando?: boolean, ativas?: boolean, top?: integer, offset?: integer)`

Pesquisa o acervo existente, sem coleta paga. Filtros e paginação explícitos; sinais do fornecedor não provam vendas/escala.

## `acervo_oferta(chave: string)`

Dossiê de uma oferta do acervo pela chave/domínio retornado na pesquisa. Não visita URLs fornecidas.

## `acervo_criativos(oferta?: string, idioma?: string, rede?: string, nicho?: string, com_views?: boolean, top?: integer, offset?: integer)`

Criativos já coletados, com preview e views quando medidas. oferta usa raw.id da oferta; null não significa zero.

## `acervo_facetas()`

Valores e contagens disponíveis para filtrar idioma, rede, nicho e fonte no acervo.

## `acervo_fontes()`

Ofertas existentes por fonte. Inventário do acervo não comprova acesso atual ao fornecedor.

## `ranking(top?: integer, offset?: integer, nao_julgadas?: boolean, idioma?: string, rede?: string, nicho?: string, fonte?: string, com_volume?: boolean, ordenar?: string, explorar?: number, incluir_paradas?: boolean)`

Ranking personalizado da sua conta, com filtros e paginação. A API informa se o modelo ainda é preliminar.

## `registrar_acao(chave: string, acao: string, valor?: string)`

Registra sua ação. usou exige domínio da SUA versão; resultado aceita pagou/nao_pagou/rodando. Não invente resultado comercial.

## `julgar_oferta(chave: string, bom: boolean, nota?: string)`

Registra seu julgamento e motivo; atualiza somente o modelo da sua conta.

## `minhas_ofertas(incluir_descurtidas?: boolean, top?: integer)`

Suas ofertas e ações registradas; não lê o histórico de outra pessoa.

## `minhas_pendencias()`

Ofertas que você marcou como usadas e ainda não tiveram resultado declarado.

## `meu_relatorio()`

Seu histórico de ações, funil e aprendizado do ranking; não prova lucro ou atribuição de vendas.

## `treinar_modelo()`

Recalcula seu modelo com seus julgamentos existentes. Não gera anúncios, não chama IA paga.

## `coleta_politica()`

Custos, fontes, limites e disponibilidade confirmada da fila da sua conta. Leia antes de solicitar coleta.

## `coleta_solicitar(fonte: string, q: string, chave_idempotencia: string, pais?: string, max_paginas?: integer, limite?: integer)`

Solicita coleta COM RESERVA DE CRÉDITOS. Requer consentimento de gasto e política disponível. Reuse a mesma chave somente para repetir o MESMO pedido após dúvida de entrega; não há retry automático.

## `coletas()`

Lista somente as coletas da sua conta, para acompanhar ou resolver resultado incerto.

## `coleta_consultar(job: string)`

Consulta estado e resultados da sua coleta. Job de outra pessoa é recusado pela API.

## `coleta_cancelar(job: string)`

Solicita cancelamento da sua coleta. A API decide reserva/reembolso; trabalho já enviado pode ficar incerto.

## `minerar(q: string, pais?: string, fonte?: string, search_type?: string, max_rodadas?: integer, nicho?: string, max_pages?: integer, last_active?: integer, sort?: string)`

Coleta anúncios NO AR agora. Duas fontes com papéis diferentes: `fonte="adheart"` = DESCOBRIR candidatos no catálogo: busca por termo (q = termos amplos separados por vírgula, pais = br/de/us…), `sort="total_reach"` (alcance acumulado estimado, o default) ou `"creation_date"` (recentes); GASTA COTA por termo, então poucos termos amplos e páginas fundas. Devolve staging_id + amostra — nada entra no acervo até adheart(acao="aprovar"). `fonte="meta"` = MEDIR e ATRIBUIR: Biblioteca de Anúncios (q = frase; rola até o platô no país; devolve `job` — status(job), 2–10 min). Uma coleta Meta por vez; 1–2 buscas por país e a fonte trava por ~12 h: comece por termo de volume, alterne país entre buscas. Limites por chamada: até 8 páginas AdHeart ou até 80 rodadas Meta. Esses tetos não substituem quota disponível.

## `google(q: string, pais?: string, modo?: string, max_pages?: integer, max_anunciantes?: integer, max_videos?: integer)`

Google/YouTube sem depender da Meta. `modo="descobrir"`: q = 1–3 termos do nicho separados por `;`, retorna anunciantes ATC, domínios observados e IDs dos vídeos pagos encontrados nos previews. `modo="dominio"`: q = hostname de uma oferta; mede inventário, datas, anunciantes e vídeos do domínio. Uma consulta ATC por vez, limites explícitos: páginas <=10, anunciantes <=12, vídeos <=10. Devolve job: use status(job, esperar=60), depois google_resultados(job). O ATC confirma anúncio pago, mas contagem de criativos não mede escala no YouTube; use youtube_video() e a série >=24h.

## `google_resultados(job: string, pagina?: integer, por_pagina?: integer)`

Resultados de google() paginados por anunciante/domínio, com IDs de vídeos e creative_id. Só a pessoa que iniciou o job pode ler. `cobertura` informa sugestões não sondadas. Domínio observado no criativo não é landing confirmada; `destino_exato_confirmado=false` exige verificação do elo anúncio → oferta. Vídeo sem ID ou domínio é lacuna, não zero de escala.

## `fontes()`

Inventário das dez fontes credenciadas e das bibliotecas Meta/Google. `pre_requisitos_presentes` confirma apenas arquivos e nomes de credencial; consulte um job limitado antes de afirmar que a sessão, assinatura, quota ou resposta do fornecedor funcionam.

## `planejar_fontes(rede: string, pais: string, intencao?: string, alvo?: string)`

Planeja sem coleta e sem custo: Meta, YouTube, ambas, native ou push; descobrir ou validar um hostname. Devolve as dez fontes credenciadas como usar, condicional ou fora do recorte, mais bibliotecas públicas, capacidades e último teste da pessoa. Use no início de cada rodada e registre a decisão de cada fonte. Acesso anterior não garante sessão atual; `volume_catalogo` não é escala nem substitui confirmação na biblioteca pública.

## `minerador(fonte: string, q?: string, pais?: string, max_pages?: integer, limite?: integer, modo?: string)`

Consulta limitada de AmericanSwipe, VAV, Anstrex, Trendtrack, MineraROI, Foreplay, Adyntel, Tyver ou SpyHouse. VAV: modo catalogo, dominio (q=hostname), canal (q=nome), channel_id (q=id) ou leaderboard (uma página); modo vazio escolhe domínio quando q existe e catálogo quando não. AmericanSwipe, Anstrex e MineraROI são catálogos; Foreplay não filtra país. Devolve job: use status(job, esperar=60) e minerador_resultados(job). O resultado fica privado por pessoa, sem publicação automática no acervo. Catálogo não confirma veiculação atual.

## `minerador_resultados(job: string, pagina?: integer, por_pagina?: integer, filtro?: string, tipo?: string, ordenar?: string)`

Resultado paginado de minerador(job). `filtro` busca no resultado já coletado, sem gastar nova cota; útil para catálogos grandes sem busca nativa. `tipo` = oferta|criativo|video|canal; `ordenar` = original|volume_catalogo|subindo|recente. Volume e `subindo` são sinais do fornecedor, nunca escala confirmada. Devolve bruto e filtrado como contagens separadas.

## `youtube_video(ids: string, pais?: string)`

Lê 1–3 vídeos públicos do YouTube por video_id: views, publicação, não listado, canal e inscritos, com horário UTC. Passe `pais` do Goal explicitamente; o default US existe só por compatibilidade. A leitura isolada é inventário; repita os mesmos IDs após >=24h para medir views/dia. Um ID vindo do ATC liga o vídeo a anúncio pago; views sozinhas não provam entrega paga nem vendas.

## `paginas(q: string, pais?: string)`

O gate AUDIÊNCIA/PERSONAS: abre o perfil de cada Página que anuncia na busca `q` no país e devolve seguidores, "seguindo 0", categoria e e-mail — por Página. Job em segundo plano (1–5 min, entra na mesma fila da Meta): acompanhe com status(job). Persona = 1–350 seguidores, "Blog pessoal"; Página ≥ 10 mil = marca, registrar sem promover.

## `cancelar(job: string)`

Interrompe um job de minerar(), paginas(), google() ou minerador() que ainda está rodando. O que já foi coletado não é aproveitado; o job vira `cancelado`.

## `status(job: string, esperar?: integer)`

Andamento ou resultado de um job de minerar()/paginas()/google()/minerador(): rodando (minutos, últimas linhas, dica se a sessão travou) ou pronto (cabeçalho, IDs, bloqueada, destinos por hostname e triagem pela assinatura do advertorial). `esperar=60` segura a resposta no servidor até 60 s enquanto o job roda — use SEMPRE em vez de chamar em sequência. Guarde o resumo em meu/dados/<job>.json; o dado bruto vem por anuncios(job).

## `anuncios(job: string, destino?: string, pagina?: integer, por_pagina?: integer)`

O dado bruto de um job pronto, paginado: por anúncio, id, data de início, nome da Página, destino (hostname) e a copy resumida. Filtre por `destino` pra contar Páginas-persona de uma oferta e ler o funil. Salve o que usar em meu/dados/.

## `medir(job: string, chave: string, rodada?: string)`

REGRA PRIMORDIAL: a leitura de um job pronto para o destino `chave` (hostname), com os quatro eixos (inventário, atribuição, personas, persistência), pronta pra sua série local: `python scripts/escala_serie.py registrar-json --de <arquivo>`. Leitura bloqueada nunca vira medida. 1 leitura = inventário; só 2 leituras separadas por ≥24 h autorizam "indícios de escala".

## `adheart(acao: string, staging_id: string)`

Fecha a própria busca AdHeart: `aprovar` baixa o staging para o acervo; `descartar` apaga. Stagings de outra pessoa ou antigos sem vínculo registrado exigem revisão do operador.

# Prompt
