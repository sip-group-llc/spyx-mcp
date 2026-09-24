# Fontes do motor

`fontes()` mostra dez mineradores credenciados. O estado `pre_requisitos_presentes`
significa apenas que os arquivos necessários existem no servidor; a sessão, quota
e assinatura precisam ser verificadas com uma consulta limitada. Meta Ad Library
e Google ATC são mais duas fontes públicas de verificação. `youtube_video()` mede
um vídeo encontrado e não descobre ofertas.

| Fonte | Papel | Busca e país no fornecedor | Tool |
|---|---|---|---|
| AdHeart | Catálogo Meta; pistas por alcance acumulado | Termo e mercado do catálogo; país de entrega não confirmado | `minerar(fonte="adheart")` |
| AmericanSwipe | Catálogo de ofertas e criativos | Sem busca por termo ou país | `minerador(fonte="americanswipe")` |
| VAV / TubeSift | Anúncios YouTube, canais e elo domínio → vídeo | País em catálogo/leaderboard; domínio e canal sem filtro de país | `minerador(fonte="vav", modo="...")` |
| Tyver | Descoberta Meta | Termo e país | `minerador(fonte="tyver")` |
| Adyntel | Descoberta Meta | Termo obrigatório e país | `minerador(fonte="adyntel")` |
| Trendtrack | Descoberta Meta, se o login responder | Termo e país | `minerador(fonte="trendtrack")` |
| Foreplay | Descoberta Meta | Termo; sem filtro nativo de país | `minerador(fonte="foreplay")` |
| MineraROI | Catálogo de ofertas | Termo filtrado localmente; sem país | `minerador(fonte="mineraroi")` |
| Anstrex | Catálogo native | Sem filtro de termo ou país neste conector | `minerador(fonte="anstrex")` |
| SpyHouse | Criativos push neste conector, se a sessão responder | Termo e país | `minerador(fonte="spyhouse")` |
| Meta Ad Library | Confirma anúncios e Páginas atuais | Termo e país | `minerar(fonte="meta")` |
| Google ATC | Confirma anúncio Google/YouTube | Termo ou domínio e país | `google()` |

## Roteamento antes de gastar

`planejar_fontes(rede, pais, intencao="descobrir", alvo="<termo>")` não consulta
fornecedor nem gasta cota. Aceita `meta`, `youtube`, `ambas`, `native` ou `push`;
para investigar uma oferta conhecida, use `intencao="validar"` e o hostname
como `alvo`. A resposta enumera **todas as dez fontes** como `usar`,
`condicional` ou `fora_do_recorte`, além das bibliotecas públicas. Cada linha
traz se o país é filtrado de verdade e o último teste daquela pessoa. Um teste
antigo não garante que a sessão ainda funciona.

| Rede aprovada | Descoberta pertinente | Confirmação |
|---|---|---|
| Meta | Biblioteca por frase; Tyver, Adyntel, Trendtrack, Foreplay; AmericanSwipe e MineraROI como catálogos (este priorizado no BR); AdHeart se a cota justificar | Landing, Meta por marca, IDs/Páginas e segunda leitura |
| YouTube | Google ATC por termo; VAV por catálogo e por domínio | ATC por domínio, elo com `video_id`, YouTube D+0 e D+1 |
| Native | Anstrex | Fonte independente da rede ainda não integrada; escala pendente |
| Push | SpyHouse | Fonte independente da rede ainda não integrada; escala pendente |

Não rode Anstrex/SpyHouse para cumprir uma rodada exclusiva Meta ou YouTube.
Uma rodada `ambas` combina as duas primeiras linhas; não transporta o piso de
IDs Meta para vídeos. Registrar uma fonte como `fora_do_recorte` é usar seu
mapa de capacidade corretamente, sem queimar assinatura.

Comece com o plano, confira `fontes()` e use `minerador()` com
`max_pages` de 1 a 3 e `limite` de 1 a 100. Acompanhe com
`status(job, esperar=60)`; leia `minerador_resultados(job, pagina)`.
Nessa leitura, `filtro` pesquisa título, texto, nicho, domínio, anunciante e ID
**nos registros já pagos**; `tipo` separa oferta, criativo, vídeo e canal;
`ordenar="volume_catalogo"` ou `"subindo"` ajuda a triar sem transformar o
campo do fornecedor em atividade atual. Leia `total_bruto` e `total` para não
confundir filtro local com cobertura da busca original.
No AmericanSwipe, `limite` controla quantas ofertas recebem detalhes; cada
página ainda pode trazer até 500 ofertas e 500 criativos, paginados na resposta.
No VAV, `modo="catalogo", q=""` lê anúncios por país; `modo="leaderboard",
q="", max_pages=1` traz canais anunciantes; `modo="channel_id", q="<id>"`
abre os anúncios de um canal; `modo="dominio", q="<hostname>"` liga destino
a vídeos. `modo="canal", q="<termo>"` busca pelo nome do canal. O leaderboard
só entrega a página 1 nesta conta; canal e domínio não filtram país.
O leaderboard pode devolver até 80 canais nessa página; `limite` não corta
essa resposta, que permanece paginada em `minerador_resultados`.
O bruto e as credenciais ficam no servidor; o resultado paginado pertence só à
pessoa que iniciou o job. Resultados de catálogo não entram automaticamente no
acervo.

## O que vira candidato forte

Preserve uma linha por **produto e destino confirmado**, com aliases, ID/link de
anúncio quando existir, `video_id`, fontes que apontaram para ele, país
efetivamente filtrado e horário de cada leitura. URL de vídeo VAV é
`video_url`; não é landing. Uma landing sugerida por fornecedor traz
`destino_exato_confirmado=false` até a navegação ligar anúncio → página →
produto. Confirme na biblioteca da rede, mesmo quando dois catálogos concordarem.

Ordem de decisão para os candidatos da rodada:

1. **Produto e identidade:** abrir a landing, reconhecer entregável, produtor,
   domínio e aliases; excluir conhecidos e formatos fora do Goal.
2. **Anúncio pago no recorte:** biblioteca Meta/ATC com ID, país, data e elo ao
   destino. Zero válido exige resposta saudável e busca de controle; 403 ou
   sessão vazia não é contagem.
3. **Distribuição e persistência:** IDs e Páginas por destino na Meta, ou
   anúncio → `video_id` → views no YouTube, sempre com unidade e horário.
4. **Audiência própria:** medir Página/canal e verificar marca-pessoa conforme
   o Goal. Fonte extra que repete a mesma oferta desempata a triagem; não
   substitui qualquer gate acima.
5. **Repetição:** só a segunda leitura comparável após ≥24 h permite falar em
   indícios de escala. Antes dela, entregue ranking parcial de inventário.

Na cobertura da rodada, registre para cada uma das dez fontes: decisão do
plano, consulta feita ou motivo da dispensa, limite, resultado, bloqueio,
possível candidato e lacuna de atribuição. Priorize para revisão profunda quem
tem entregável correto, anúncio pago no país, ligação ao destino e série
comparável. A falta de confirmação mantém o candidato no ranking parcial.

Na ficha da oferta, registre todas as fontes pertinentes como consultada,
bloqueada, sem quota ou incompatível. Deduplicate ofertas por produto e destino;
não some anúncios, criativos, Páginas e vídeos. Abra a landing e confira o
produto antes da contagem. `volume_catalogo`, `is_climbing` e views em uma
leitura são pistas, não escala. Para afirmar indícios de escala, reconfira na
biblioteca pública da rede e faça duas leituras comparáveis separadas por
pelo menos 24 horas.
