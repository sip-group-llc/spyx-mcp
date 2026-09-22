# Tools

Gerado de `mcp_minerador.py` por `gerar_docs.py` — não edite à mão.

`?` marca argumento opcional. Toda tool exige a sua chave no header `Authorization`.

## `minerar(q: string, pais?: string, fonte?: string, search_type?: string, max_rodadas?: integer, nicho?: string, max_pages?: integer, last_active?: integer)`

Coleta anúncios NO AR agora. `fonte="meta"`: Biblioteca de Anúncios (q = frase; rola até o platô no país pedido; devolve `job` — acompanhe com status(job), leva 2–10 min). Uma coleta Meta por vez: se houver outra, a sua espera na fila. `fonte="adheart"`: busca por termo (q = termos separados por vírgula, pais = br/de/us…; GASTA COTA, então poucos termos e páginas fundas); devolve staging_id — nada entra no acervo até adheart(acao="aprovar").

## `paginas(q: string, pais?: string)`

O gate AUDIÊNCIA/PERSONAS: abre o perfil de cada Página que anuncia na busca `q` no país e devolve seguidores, "seguindo 0", categoria e e-mail — por Página. Job em segundo plano (1–5 min, entra na mesma fila da Meta): acompanhe com status(job). Persona = 1–350 seguidores, "Blog pessoal"; Página ≥ 10 mil = marca, registrar sem promover.

## `cancelar(job: string)`

Interrompe um job de minerar() que ainda está rodando (por exemplo, preso em tentativas com 0 IDs). O que já foi coletado não é aproveitado; o job vira `cancelado`.

## `status(job: string)`

Andamento ou resultado de um job de minerar(): rodando (minutos, últimas linhas, dica se a sessão travou) ou pronto (cabeçalho, IDs, bloqueada, destinos por hostname e triagem pela assinatura do advertorial). Guarde o resumo em meu/dados/<job>.json; o dado bruto vem por anuncios(job).

## `anuncios(job: string, destino?: string, pagina?: integer, por_pagina?: integer)`

O dado bruto de um job pronto, paginado: por anúncio, id, data de início, nome da Página, destino (hostname) e a copy resumida. Filtre por `destino` pra contar Páginas-persona de uma oferta e ler o funil. Salve o que usar em meu/dados/.

## `medir(job: string, chave: string, rodada?: string)`

REGRA PRIMORDIAL: a leitura de um job pronto para o destino `chave` (hostname), com os quatro eixos (inventário, atribuição, personas, persistência), pronta pra sua série local: `python scripts/escala_serie.py registrar-json --de <arquivo>`. Leitura bloqueada nunca vira medida. 1 leitura = inventário; só 2 leituras separadas por ≥24 h autorizam "indícios de escala".

## `adheart(acao: string, staging_id: string)`

Fecha uma busca AdHeart: `aprovar` baixa o staging para o acervo (aí entra no ranking); `descartar` apaga.

# Prompt
