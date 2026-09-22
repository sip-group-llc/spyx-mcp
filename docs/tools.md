# Tools

Gerado de `mcp_minerador.py` por `gerar_docs.py` — não edite à mão.

`?` marca argumento opcional. Toda tool exige a sua chave no header `Authorization`.

## `base(arquivo?: string, secao?: string)`

Lê a base de treinamento. `arquivo`: CRITERIOS · README · METRICAS · MAPEADAS (upstream do operador, sempre atual) ou `meu` (o seu fork). Sem `secao`: só o sumário de títulos. `secao="*"`: o arquivo inteiro. `secao="trecho"`: as seções cujo título contém o trecho (ex.: "REGRA PRIMORDIAL").

## `anotar(tipo: string, texto: string, origem?: string)`

Grava no SEU critério (fork) o que a rodada ensinou. `tipo`: preferencia · licao · hipotese · exclusao (oferta que você já mapeou/usou). `origem`: rodada ou ID que sustenta ("R003-B"). Um exemplo gera hipótese, não regra — use `hipotese` até o padrão repetir.

## `avaliar(rodada: string, item: string, veredito: string, motivo?: any)`

Registra a avaliação DA PESSOA sobre um candidato ("R003-B ruim pelo produto"). `veredito`: boa · ruim · incerta. Motivo não dito fica null — a sua hipótese nunca preenche a avaliação dela.

## `rodada_salvar(id: string, markdown: string)`

Salva o relatório da rodada (R001, R002…) no seu fork. Conteúdo: hipótese · buscas (q, país, IDs, bloqueada?) · candidatos com inventário/atribuição/persistência/personas · lacunas · o que muda na próxima.

## `rodadas(id?: string, ultimas?: integer, de?: string)`

Lê rodadas anteriores. `de`: minhas (seu fork) · upstream (as do operador). Com `id`: o texto inteiro; sem: as últimas N resumidas mais as suas avaliações — é daqui que sai o refinamento.

## `minerar(q: string, pais?: string, fonte?: string, search_type?: string, max_rodadas?: integer, nicho?: string, max_pages?: integer, last_active?: integer)`

Coleta anúncios NO AR agora. `fonte="meta"`: Biblioteca de Anúncios (q = frase; rola até o platô no país pedido; devolve `job` — acompanhe com status(job), leva 2–10 min). Uma coleta Meta por vez: se houver outra, a sua espera na fila. `fonte="adheart"`: busca por termo (q = termos separados por vírgula, pais = br/de/us…; GASTA COTA, então poucos termos e páginas fundas); devolve staging_id — nada entra no acervo até adheart(acao="aprovar").

## `status(job: string)`

Andamento ou resultado de um job de minerar(): rodando (últimas linhas) ou pronto (cabeçalho, IDs, bloqueada, destinos por hostname e triagem pela assinatura do advertorial).

## `adheart(acao: string, staging_id: string)`

Fecha uma busca AdHeart: `aprovar` baixa o staging para o acervo (aí entra no ranking); `descartar` apaga.

## `escala(chave: string, job?: string, rodada?: string)`

REGRA PRIMORDIAL. Com `job`: registra a leitura desse job para o destino `chave` (hostname) na SUA série e devolve o delta contra a anterior. Sem `job`: mostra a série e o veredito. 1 leitura = INVENTÁRIO ("escala: pendente de segunda leitura"); só ≥2 leituras separadas por ≥24 h, mesmo método, autorizam escrever "indícios de escala". Leitura bloqueada nunca vira medida.

# Prompt

## `goal(nicho, regiao, padrao?, quantidade?)`

O /goal de uma rodada: o alvo é seu; o método já vem embutido.

No Claude Code aparece como `/mcp__hackingads__goal`; no claude.ai, como prompt do conector.
