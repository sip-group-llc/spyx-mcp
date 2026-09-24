# Fontes do motor

`fontes()` mostra dez mineradores credenciados. O estado `pre_requisitos_presentes`
significa apenas que os arquivos necessários existem no servidor; a sessão, quota
e assinatura precisam ser verificadas com uma consulta limitada. Meta Ad Library
e Google ATC são mais duas fontes públicas de verificação. `youtube_video()` mede
um vídeo encontrado e não descobre ofertas.

| Fonte | Papel | Busca e país no fornecedor | Tool |
|---|---|---|---|
| AdHeart | Catálogo Meta; pistas por alcance acumulado | Termo e geografia | `minerar(fonte="adheart")` |
| AmericanSwipe | Catálogo de ofertas e criativos | Sem busca por termo ou país | `minerador(fonte="americanswipe")` |
| VAV / TubeSift | Anúncios YouTube e elo domínio → vídeo | Domínio; país só ao navegar catálogo | `minerador(fonte="vav")` |
| Tyver | Descoberta Meta | Termo e país | `minerador(fonte="tyver")` |
| Adyntel | Descoberta Meta | Termo obrigatório e país | `minerador(fonte="adyntel")` |
| Trendtrack | Descoberta Meta, se o login responder | Termo e país | `minerador(fonte="trendtrack")` |
| Foreplay | Descoberta Meta | Termo; sem filtro nativo de país | `minerador(fonte="foreplay")` |
| MineraROI | Catálogo de ofertas | Termo filtrado localmente; sem país | `minerador(fonte="mineraroi")` |
| Anstrex | Catálogo native | Sem filtro de termo ou país neste conector | `minerador(fonte="anstrex")` |
| SpyHouse | Criativos push/native, se a sessão responder | Termo e país | `minerador(fonte="spyhouse")` |
| Meta Ad Library | Confirma anúncios e Páginas atuais | Termo e país | `minerar(fonte="meta")` |
| Google ATC | Confirma anúncio Google/YouTube | Termo ou domínio e país | `google()` |

Comece com `fontes()`, escolha pela rede do Goal e use `minerador()` com
`max_pages` de 1 a 3 e `limite` de 1 a 100. Acompanhe com
`status(job, esperar=60)`; leia `minerador_resultados(job, pagina)`.
No AmericanSwipe, `limite` controla quantas ofertas recebem detalhes; cada
página ainda pode trazer até 500 ofertas e 500 criativos, paginados na resposta.
O bruto e as credenciais ficam no servidor; o resultado paginado pertence só à
pessoa que iniciou o job. Resultados de catálogo não entram automaticamente no
acervo.

Na ficha da oferta, registre todas as fontes pertinentes como consultada,
bloqueada, sem quota ou incompatível. Deduplicate ofertas por produto e destino;
não some anúncios, criativos, Páginas e vídeos. Abra a landing e confira o
produto antes da contagem. `volume_catalogo`, `is_climbing` e views em uma
leitura são pistas, não escala. Para afirmar indícios de escala, reconfira na
biblioteca pública da rede e faça duas leituras comparáveis separadas por
pelo menos 24 horas.
