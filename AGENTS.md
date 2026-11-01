# HackingAds MCP — instruções para Codex

Leia `CLAUDE.md` para o ciclo e `docs/goal-preflight.md` quando o pedido envolver preparar, ativar ou executar uma rodada. A base do operador fica em `base/` e é somente leitura; dados, goals, descobertas e rodadas da pessoa ficam em `meu/`.

Para as ferramentas de conta, leia `docs/conta.md` e confirme `conta_identidade`
antes de qualquer escrita. Não peça chaves ou senhas na conversa: a pessoa deve
configurá-las no cliente. Reserva de créditos exige autorização de gasto; timeout
não autoriza repetir a coleta com outra chave de idempotência. Uma recusa de
acesso não autoriza usar credenciais de operador ou inferir vínculo por nome.

## Trava antes de um Goal

Um pedido de mineração ou um texto de goal enviado em conversa é **rascunho**. Antes de criar/ativar um Goal, produzir texto para `/goal` ou iniciar coleta, confira os campos e faça o pré-voo de `docs/goal-preflight.md`. Pergunte pelos campos essenciais ausentes; com o escopo completo, mostre o texto exato e espere a aprovação explícita da pessoa. Não interprete silêncio, resposta sobre parâmetros ou o simples envio do rascunho como aprovação. Depois de aprovado, execute o fluxo sem microconfirmações.

Se a pessoa colar literalmente `/goal ...`, a aplicação pode ativá-lo antes de estas instruções serem lidas. Nesse caso, valide o escopo e peça o dado faltante antes de minerar; não alegue que o arquivo impediu a ativação no aplicativo. Para garantir revisão **antes** da ativação, oriente a pessoa a enviar o pedido como mensagem comum e só usar `/goal` após aprovar o rascunho.

## Escolha das fontes

Os quatro Goals em `base/` preservam critérios e exemplos do operador. Para
executar um deles neste MCP, prepare um Goal pessoal com
`meu/goals/GOAL-EXEMPLO.md`; não cole literalmente a versão curta histórica de
`base/` em `/goal`. Use o pré-voo e o roteamento atual abaixo para escolher
ferramentas. Comandos `scripts/...`, listas antigas de fontes e estados de sessão
registrados na base não descrevem a disponibilidade atual do servidor.

Depois da aprovação do Goal, chame `planejar_fontes(rede, pais, alvo)` e leia
`docs/fontes.md`. Registre a decisão para cada um dos dez mineradores e consulte
os compatíveis em lotes limitados. `fontes()` mostra pré-requisitos e o último
teste, não saldo nem sessão garantida. Catálogos servem para descoberta;
atividade e indícios de escala exigem a biblioteca pública da rede e leituras
comparáveis separadas por pelo menos 24 horas. Use filtro local em
`minerador_resultados` para não ler centenas de linhas nem repetir uma busca paga.

## Entrega de pesquisa

Toda rodada entrega os candidatos que passaram o gate **e** uma lista ordenada dos achados mais fortes que ficaram abaixo dele, com links diretos, sinais observados e motivo da pendência. `0 finalistas` significa nenhum comprovado na cobertura medida. Conte termos solicitados/consultados, anunciantes e vídeos distintos, vídeos lidos/não lidos e limites da amostra. Registre descobertas relevantes em `meu/DESCOBERTAS.md` como inventário ou hipótese, sem inventar avaliação humana, favorita, venda ou escala. Uma leitura de views não é tendência; a segunda leitura comparável exige intervalo de pelo menos 24 horas.
