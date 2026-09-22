# Critérios e aprendizado acumulado

## REGRA PRIMORDIAL — escala é o que sobrevive à repetição da medida

Gravada em 20/09/2026, a pedido explícito do usuário, depois que a R017 entregou três finalistas
descritas como "fortes indícios de escala" a partir de **uma única leitura** de cada. Está acima de
todos os outros critérios deste arquivo; quando qualquer regra abaixo conflitar com esta, esta vence.

**O que a obrigou.** Na R017 a mesma busca devolveu **28 ou 598 IDs** dependendo do IP usado, porque a
Meta responde HTTP 403 desenhando "No ads match your search criteria". Um número que muda com o
encanamento de quem mede **não é propriedade da oferta**. A contagem única nunca foi escala; a R017 só
tornou isso impossível de ignorar.

**A regra, em uma frase:** contagem tirada **uma vez** é *inventário*. Inventário vira **indício de
escala** quando sobrevive a uma segunda leitura, separada no tempo e feita com o mesmo método.

**Os quatro eixos, e o que cada um prova sozinho:**

| Eixo | Como medir | O que prova | O que NÃO prova |
|---|---|---|---|
| **Inventário** | IDs ativos distintos, deduplicados, com destino extraído de cada cartão | tamanho **naquela leitura**, naquele IP | nada sobre gasto, alcance ou venda |
| **Atribuição** | fração dos IDs cujo destino é o funil da oferta (`598/598`) | que o inventário é de **uma oferta só** — o eixo mais sólido, e o único que uma leitura basta | tamanho |
| **Persistência** | idade do mais antigo, mediana de vida, fração acima de 30 e 90 dias, início por mês | que **alguém segue pagando** — é o eixo que mais se aproxima de escala sem dado comercial | quanto se paga |
| **Repetição** | **≥ 2 leituras** da mesma busca, separadas por ≥ 24 h, mesmo método, mesma fonte | que o inventário é **real e estável**, e em que direção se move | valor absoluto de gasto |

**Gate, obrigatório antes de escrever "escala" sobre qualquer oferta:**

1. **Uma leitura só → escrever `inventário medido`**, nunca "escalada" nem "fortes indícios de escala".
   A ficha declara `leituras: 1` e `escala: pendente de segunda leitura`.
2. **Duas leituras ou mais → `indícios de escala`**, sempre com a série ao lado: as duas datas, os dois
   números e o delta. Série em [`serie-escala.jsonl`](serie-escala.jsonl), alimentada por
   [`scripts/escala_serie.py`](../../scripts/escala_serie.py).
3. **Conferir o status HTTP de toda leitura.** Contagem baixa ou zero pode ser bloqueio, não ausência
   de anúncio. Leitura sem status verificado não entra na série.
4. **Fonte independente conta como meia repetição.** A mesma oferta aparecendo na Meta e no Google ATC
   é convergência real; duas contagens do mesmo inventário continuam sendo **um** sinal, não dois.
5. **Persistência alta compensa parte da repetição, e deve ser dita assim.** 240 IDs acima de 30 dias é
   evidência de que a operação sobreviveu 30 dias — o que é, em si, uma segunda medida feita pela
   própria plataforma. Mesmo assim, não dispensa a segunda leitura: declarar qual dos dois sustenta a
   conclusão.
6. **Em nenhuma hipótese** converter inventário, persistência ou repetição em gasto, receita, ROAS,
   conversão ou vendas. Continuam inobserváveis por fonte pública.

**Cadência sugerida para os finalistas de uma rodada:** D+0 na entrega, D+1, D+3 e D+7. Não existe
agendamento automático neste laboratório — a remedição acontece quando o operador pede.

Esta regra torna gate o que o feedback do E001 (18/09/2026) já dizia em prosa — *"ativo não é muito
escalado"* — e o que [METRICAS.md](METRICAS.md) registra na linha **Tendência**.


## Escala no YouTube — views em vídeo não listado, não contagem de criativo {#escala-no-youtube}

Gravada em **22/09/2026**, a pedido do usuário, ao separar o GOAL de renda extra em um por rede. Fala
original: *"a forma que o google funciona é diferente do meta, geralmente não tem muitas campanhas ou
criativos, não significa escala; o que anda entregando mais é vídeos não listados com muita view em pouco
tempo e recente"*.

**O que muda.** A REGRA PRIMORDIAL continua valendo (uma leitura é inventário, duas são indício), mas a
**grandeza medida** troca de rede para rede:

| Eixo | Meta | YouTube |
|---|---|---|
| Inventário | IDs ativos no destino | **views** do vídeo não listado, com data/hora da leitura |
| Persistência | idade do criativo mais antigo, mediana | idade do vídeo (`publishDate`), `last_seen` do VAV, 1ª exibição no ATC |
| Repetição | 2ª contagem de IDs ≥ 24 h | **2ª leitura de views ≥ 24 h** → views/dia |
| Contagem de criativo no ATC | é o tamanho | é **inventário secundário**; 3 anúncios não reprovam |

**Por que.** No YouTube um único vídeo não listado roda como anúncio por meses e o contador público da
própria página registra a entrega; a R003 já tinha achado seis desses com milhões de views em três ofertas,
e a R013–R015 mediram por criativo mesmo assim. Vídeo **listado** com views pode ser orgânico: registrar e
pesar menos. Vídeo publicado há meses com views paradas entre duas leituras está morto, mesmo com anúncio
listado no ATC.

**Piso provisório** (botão de calibração, rever após a primeira rodada do GOAL-RENDA-EXTRA-YOUTUBE):
não listado, publicado há ≤ 90 dias, ≥ 100 mil views — ou ≥ 5 mil views/dia entre duas leituras.
Onde se aplica: [GOAL-RENDA-EXTRA-YOUTUBE](GOAL-RENDA-EXTRA-YOUTUBE.md). Campos: `viewCount`,
`publishDate`, `isUnlisted` em `ytInitialPlayerResponse`; views/`published`/`last_seen` no registro do VAV.

## ASSINATURAS DO ADVERTORIAL AGRESSIVO — o que essas ofertas têm de único, e como reconhecer em segundos

Gravado em 21/09/2026 a pedido do usuário, depois de aprovar as três finalistas da R017 ("bons resultados
gostei, adicione à base de treinamento as características e detalhes que eles têm de único que facilita
encontrar essas ofertas mais agressivas"). Tudo abaixo foi **medido** na R017 e na R018 — ErosCode, Muses
Academy, Céleste Valmont, e os descartes que pareciam iguais e não eram. Nada é hipótese.

### A anatomia, em uma frase

**Uma marca sem rosto, servida por várias Páginas com nome de pessoa e audiência zero, que empurram um
quiz cujo preço só aparece depois de você responder.** Cada pedaço dessa frase é detectável antes de abrir
qualquer página, e os cinco juntos são a assinatura.

### 1. O destino é um quiz — e o hostname entrega isso de graça

| Sinal | Medido em |
|---|---|
| hostname começa com **`quiz.`** | `quiz.eroscode.de`, `quiz.musesacademy.io`, `quiz.tryinnerly.com`, `quiz.innerflo.me` |
| path **`/pages/quiz`** ou **`/quiz`** | `celestevalmont.com/pages/quiz` |
| o quiz **não renderiza sem parâmetro** (`landing_uuid`, `?key=`) | Muses Academy, Innerly |
| domínio do anúncio é **camada de rastreio** que redireciona por JS para a marca real | `thepsychology.online/click?key=` → `tryinnerly.com`; `better-life-designer.xyz/cf/r/` → travesseiro |

**Regra operacional:** ao agrupar destinos por hostname, **`quiz.*` vai para o topo da fila** de auditoria
antes mesmo de contar. E quando o domínio do anúncio não é o da marca, **medir os dois** — a Ad Library só
conta o que está na copy, e o `tryinnerly` ficou invisível.

### 2. A copy é de funil, não de produto — e essa frase é a chave de busca

A frase clínica (`mein Arzt`, `il mio medico`) entrega nutra. A frase de **funil** entrega o infoproduto
agressivo. Foram estas, e só estas, que acharam as três finalistas:

| Idioma | Frase que rendeu | Achou |
|---|---|---|
| DE | **`personalisierten Plan`**, `persönlichen Plan`, **`Mach den Test`**, `60-Sekunden-Check` | ErosCode, Muses, Innerly |
| IT | **`piano personalizzato`**, **`Fai il test`** | Muses, Céleste, Innerly |
| ES | **`plan personalizado`**, **`Haz el test`** | Muses, learndemandskills |
| FR | `plan personnalisé`, `Faites le test` | Muses, Céleste |
| HR | `personalizirani plan` (apareceu na copy de Muses) | — |
| NL / PL | `persoonlijk plan`, `spersonalizowany plan` | pouco — o padrão é fraco nesses mercados |

O que essas frases têm em comum: prometem um **resultado personalizado em troca de responder perguntas**.
É o contrato do quiz-funnel. Variantes a testar em rodadas futuras: `dein persönliches Ergebnis`,
`il tuo profilo`, `tu perfil`, `descubre tu tipo`.

**Frases que NÃO servem, medidas:** `60 segundos` sozinho (traz e-commerce coreano de cosmético),
`meine Geschichte` / `la mia storia` (traz nutra e micronovela), qualquer coisa com `Ich hätte nie
gedacht` (nutra puro). E nos nórdicos (`personlig plan` em SE/DK) o padrão simplesmente não existe.

### 3. As Páginas-persona têm uma cara — e ela se lê no perfil público, sem login

Toda persona medida cabia em **um** destes três moldes:

| Molde | Como é | Exemplo medido |
|---|---|---|
| **Pessoa anglófona genérica** servindo copy em língua local | dois nomes, sem sobrenome étnico local, categoria "Blog pessoal" | Muses: Evelyn Taylor, Michael Collins, James Harrison, Andrew Parker, Thomas Blake — servindo alemão, italiano, croata |
| **Uma persona por idioma, mesmo nome traduzido** | o "diário" localizado: *Les Carnets de* / *I taccuini di* / *Notizbuch* / *Os Cadernos de* | Céleste Valmont (7), Innerly (Kowalski, Sabater, Clarté, Mądry, Moudrý — 11) |
| **Marca + diário + pessoa** no mesmo destino | `Marca.Official` + `Ratgeber/Aktuell` + 2 nomes de pessoa | ErosCode: ErosCode.Official, Beziehungs-Ratgeber, Partnerschaft Aktuell, Thomas Krause, Lorena Brandt |

E as três propriedades do perfil que confirmam persona de anúncio, medidas em todas:

- **Seguidores entre 1 e ~350** (medidos: 1, 2, 16, 30, 51, 88, 168, 338) e **"Seguindo 0"**;
- categoria **"Blog pessoal"**, **"Blogueiro(a)"** ou uma profissão solta (**"Astrólogo"**);
- **zero ou um post**, quase sempre "atualizou a foto do perfil/capa" — a Página nasceu para anunciar.

**O amarrador barato:** o **e-mail da marca no perfil da persona**. Quatro das cinco Páginas do ErosCode
declaram `support@eroscode.de`. É a prova de "mesma operação" mais barata que existe — antes de comparar
destino, olhar o campo de contato do perfil.

**O que parece persona e não é:** nome com sufixo **`with <Marca>`** (`Claudina in cucina with Mylky`) é
colab de influenciador — audiência emprestada, o oposto do padrão. Nome com **número** (`Kira Loes 12`,
`Drama Shorts&Reels-03`) é fábrica de app de micronovela, não de infoproduto.

### 4. O preço se esconde — e o jeito de esconder diz o modelo de cobrança

| O que se vê | O que significa | Medido em |
|---|---|---|
| preço público na página de venda, com contador e "só hoje" | pagamento único, funil clássico de infoproduto | ErosCode: 59 € (de 99), garantia 60 dias + 100 € |
| preço só depois do quiz; **Termos de Assinatura** falam em trial + renovação + "cancele pelo chat de suporte" | **assinatura de atrito**: o dinheiro está na renovação | Muses Academy |
| quiz termina em **nome + e-mail** antes de qualquer preço | captura primeiro, venda por e-mail depois | Céleste Valmont |
| landing raiz **vazia** (HTTP 200, corpo 0 bytes) | cloaking leve: só o tráfego pago vê a oferta | Innerly |

Nenhum deles mostra preço no anúncio. **Ausência de preço no anúncio + quiz = sinal**, não lacuna.

### 5. A infraestrutura repete — e algumas peças já dizem "não é o que você procura"

| Peça | Lê-se como |
|---|---|
| **FunnelCockpit** (DE), checkout próprio no subdomínio | infoproduto alemão de resposta direta — **alvo** |
| **Vercel** + editora **SAS** francesa no rodapé | operação europeia enxuta, marca-persona — **alvo** |
| **funnelfox.io** rodando o quiz | onboarding de **app de assinatura** (Yoga-Go, BetterMe, Innerly) — **descartar** |
| anunciante no Google com **"Apps Ltd"** no nome | app — **descartar** |
| hostname `w2a.`, `fb.`, `drama.`, `read.`, `h5.`, `novel`, `reel` | micronovela/microdrama — **descartar sem abrir** |
| `play.google.com`, `itunes.apple.com`, `app.adjust.com`, `onelink.me` como destino | app — **descartar** |
| "Versand", "frete grátis", "Spedizione gratuita", "Discreet Packaging" | produto físico — **descartar** |
| "fundraiser", "501(c)(3)" | doação — **descartar** |
| `/cf/r/`, `/click?key=`, TLD `.xyz`/`.online`/`.shop` | redirecionador de afiliado ou rastreio: **medir o destino final**, não o domínio |

### 6. A curva de inventário separa dois tipos de agressividade

As duas são alvo. Mas se distinguem, e a distinção muda o que se conclui:

| Curva | Lê-se como | Medido em |
|---|---|---|
| **cresce mês a mês** (jul 59 → ago 245 → set 294) com mediana de 3 semanas | escalada sustentada: quem paga está dobrando a aposta | ErosCode |
| **tudo na mesma semana**, mediana de 4 dias, **mas com um ano de criativo no Google** | rotatividade agressiva — a operação é velha, o inventário da Meta é descartável | Muses Academy |
| mediana de 39 dias, 240 IDs acima de 30 | persistência: o criativo que funciona fica no ar | Céleste Valmont |
| tudo na mesma semana **e nada no Google** | lançamento de verdade — só o tempo diz | Cryptory (R016) |

Sem a frente do Google, o segundo caso se confunde com o quarto. **Cruzar o ATC é obrigatório antes de
chamar de lançamento.**

### 7. Multi-país é assinatura, não coincidência

As três finalistas foram encontradas no filtro de **mais de um país** — e reapareceram em AT e CH sem
serem procuradas lá. A persona localizada existe justamente para isso. Regra: achou em DE, **conferir AT e
CH** custa uma busca e amplia a evidência; achou em FR, conferir BE e CH.

### Checklist de 10 segundos — antes de gastar uma coleta de marca

Um destino merece a busca por marca quando bate **três** destes cinco, sem abrir a landing:

1. hostname `quiz.*` ou path `/quiz` — ou domínio que não é a marca (redirecionador);
2. a copy contém frase de funil (`plano personalizado` / `faça o teste` na língua local);
3. **≥ 3 Páginas** distintas apontando para ele na mesma busca;
4. ao menos um nome de Página é pessoa **sem** sufixo `with`, **sem** número;
5. nenhuma peça de descarte da tabela 5 no hostname.

E o teste de entregável — **abrir a landing** — vem **antes** da contagem por marca, não depois. A R018
quebrou isso com o Innerly e pagou uma coleta inteira para descobrir que era app.

Detector executável do checklist: [`scripts/triar_destinos.py`](../../scripts/triar_destinos.py).

## Preferências explícitas — usuário, conversa de 17/09/2026

- Prioridade: infoprodutos de resposta direta, ofertas mais agressivas, produtores e
  afiliados; excluir grandes empresas e catálogos institucionais como referências centrais.
- EUA e Europa; produtor brasileiro ou estrangeiro pode entrar.
- Meta e Google/YouTube com o mesmo peso.
- Recência, refinada após R003: retirar vídeos com mais de seis meses, mesmo ainda
  anunciados. Em 17/09/2026, corte em 17/03/2026. Usar publicação quando conhecida;
  início de anúncio anterior ao corte também demonstra que o criativo já é antigo.
  Início recente não comprova publicação recente; deixar essa lacuna explícita.
- Refinamento explícito após R002: buscar **indícios de escala**, aceitando que dados
  comerciais estarão ausentes. O usuário pediu 15 anúncios para avaliar e calibrar
  o treinamento. Não exigir vendas comprovadas como condição de descoberta; tampouco
  converter volume ou persistência em vendas, lucro ou certeza de escala.
- O usuário avalia boa/ruim para refinar buscas futuras. Primeiro lote recebido pela planilha R003 em 17/09/2026: cinco boas e três ruins, em cinco ofertas.

Usar também os critérios canônicos em [BLACK_AD_SIGNALS](../../spy/knowledge/BLACK_AD_SIGNALS.md)
e [NICHE_FOCUS_MAP](../../spy/knowledge/NICHE_FOCUS_MAP.md), sem duplicá-los aqui.

## Preferência explícita do usuário — 20/09/2026: ESCALA SEM AUDIÊNCIA PRÓPRIA

Origem: conversa deste projeto (8dc59a51-50ee-4f8c-80fd-4c322119d901), após a entrega da R014 e dos links das três finalistas.
Fala original: “o que pude perceber e que todas tem um facebook ou youtube ou ambos forte nao e o que procuro procuro marcas sem muito seguidor mas em escala anota isso grava nas bases do minerador deixa claro”.

**O que o usuário procura, dito de forma clara:** marca **sem** seguidores — Página, canal e perfil pequenos,
sem rosto conhecido, sem autoridade pessoal — mas **em escala** de anúncio pago: muitos IDs ativos, muitos
criativos, persistência. A escala tem de vir do tráfego pago, não de audiência acumulada. Oferta apoiada em
Facebook, YouTube ou ambos “fortes” (Página/canal grande ou produtor-rosto como marca) **não é o alvo**, mesmo
com inventário enorme. Vale para todas as rodadas e frentes daqui em diante.

Medido nas finalistas da R014, em 20/09/2026, para ancorar o critério:

| Oferta | Audiência própria | Escala paga | Veredito do usuário |
|---|---|---|---|
| She Sells / Shelby Sapp | Página “Shelby Sapp” **41 mil seguidores**; a marca é a pessoa | 125 IDs Meta | não é o que procuro |
| 20-Minute Trader / Jeremy Russell | canal `@20minutetrader` **20,7 mil inscritos**; a marca é a pessoa; vídeo pago de 926 dias | ≥1.200 criativos ATC | não é o que procuro |
| Booming Bookkeeping / Bill Von Fumetti | canal `@BoomingBookkeepingBusiness` **22,1 mil inscritos**; a marca é a pessoa; 37 M de views num vídeo pago | ≥1.200 criativos ATC | não é o que procuro |

Lição da medição: os canais de YouTube são pequenos em inscritos (≈20 mil); o que o usuário percebeu como
“YouTube forte” é o **produtor-rosto virado marca** e o vídeo pago de longa vida. Portanto o rosto pesa mais
que o número.

**Regra operacional (gate AUDIÊNCIA, antes da auditoria funda):**

1. Tem **audiência própria** quem cumpre um dos dois: (a) a marca é uma pessoa — nome ou rosto do produtor
   é o nome da Página, do canal, do domínio ou do produto; (b) Página Meta com ≥ 10 mil seguidores **ou**
   canal YouTube com ≥ 10 mil inscritos. O limiar de 10 mil é botão de calibração, não lei: rever quando o
   usuário avaliar as próximas rodadas.
2. Como medir, sem login e sem gastar cota: o texto público da Página (`facebook.com/<page_id>/`) mostra
   “N mil seguidores” mesmo atrás do modal de login (`get_page_text`); o HTML público do canal
   (`youtube.com/channel/<id>`) traz `subscriberCountText`. Registrar número, data e URL na tabela do gate,
   numa coluna própria **“audiência própria”**.
3. Oferta com audiência própria: medir, registrar em OFERTAS-MAPEADAS com o número e **não promover a
   finalista**. Fica classificada como “escalada com audiência”, para não ser reauditada.
4. Alvo da promoção: Página/canal abaixo do limiar, marca sem rosto (empresa, produto ou método como nome),
   e ainda assim inventário grande e persistente. Wealth Creators (1.185 IDs, Página “Marvin Mitchell”) é
   o contraexemplo do lado do rosto; o exemplo positivo ainda não apareceu — é o que a próxima rodada procura.
5. O critério de replicabilidade que já estava no README (“sem depender da audiência do produtor”) deixa de
   ser desejo e vira gate.

Eventos gravados em [avaliacoes.jsonl](avaliacoes.jsonl): R014-01, R014-02 e R014-03 como “ruim”, motivo
“audiência própria”. Não é rejeição da escala medida; é rejeição do tipo de marca.

## Preferência explícita do usuário — 20/09/2026: ESCALA MAIOR E ÂNGULO DE ADVERTORIAL

Origem: conversa desta sessão, depois da entrega da R016 (Europa, renda extra).
Fala original: "ainda to achando a escala fraca e o angulo da oferta tambem queria achar mais coisas tipo
https://www.facebook.com/ads/library/?...&country=ALL&is_targeted_country=false&...&q=myavellis.com&sort_data[mode]=total_impressions&sort_data[direction]=desc".

**O que o exemplo dele é, medido em 20/09/2026:** `myavellis.com` (marca Avellis) vende **Cannella di
Ceylon em softgel de óleo MCT** na Itália. O anúncio não é anúncio: é **advertorial em primeira pessoa**,
assinado por uma persona ("Francesca Martini"), contando a história de uma enfermeira de diabetes com 22
anos de carreira que saiu da metformina e levou a hemoglobina glicada de 8,2 para 5,9. O site é
**cloakeado** (Blockify devolve "Access Denied" a visitante direto). 170 no cabeçalho pelo domínio;
**132 IDs** quando medido pela frase da copy.

**O que isso muda no alvo:**

1. **Escala**: o que ele chama de "fraca" é a ordem de grandeza europeia de infoproduto — 49 a 201 IDs.
   O alvo agora são as operações de **centenas de IDs com cabeçalho de milhares** (`Blutzucker` na
   Alemanha: cabeçalho **5.200**, 659 IDs carregados numa varredura).
2. **Ângulo**: a preferência é por **copy de história em primeira pessoa** — persona, número clínico
   concreto, antes/depois, "meu médico disse" — e não pela página institucional de curso.
3. **Entregável**: o exemplo é **suplemento**, que o GOAL exclui do recorte de infoproduto
   (`OFERTA. Testar o entregável ANTES da contagem: fora serviço, SaaS, físico e suplemento`).
   **Conflito declarado, não resolvido por inferência:** enquanto o usuário não disser o contrário, o
   nutra entra como referência de ângulo e escala, e a regra do GOAL continua valendo para promoção.

**Método que ele passou, e a correção medida:** os parâmetros `country=ALL&is_targeted_country=false` e
`sort_data[mode]=total_impressions&sort_data[direction]=desc` ordenam a biblioteca pelas impressões
totais. Suportados agora em `scripts/adlib_coleta.py` (`--country ALL`, `--ordenar`). **Mas a busca por
domínio ou por marca trava em ~30 cartões**, com ou sem ordenação (`myavellis.com` 30 de 170;
`Gentilia` 29 de 180). **O que mede é a frase da copy:** `emoglobina glicata` carregou **402 IDs** e
mostrou `gentilia.it` com **162** e `myavellis.com` com **132** — quatro vezes mais que a busca pelo
domínio. Regra nova: para oferta com persona e muitos criativos, buscar pela **frase clínica da copy**.

## Correções de método medidas — 20/09/2026, R017: a Biblioteca de Anúncios mente por omissão

Origem: [R017](rodadas/R017-2026-09-20.md), primeira rodada do recorte de advertorial fora do nutra.

**A armadilha, e é a pior já registrada neste projeto.** A partir de algumas dezenas de buscas do mesmo
IP, a Meta Ad Library responde **HTTP 403** e desenha a página com *"No ads match your search criteria"*.
Não há mensagem de erro, não há captcha, não há sinal na interface. Uma rodada inteira pode concluir
"essa oferta não existe mais" ou "o platô é 28" quando o que houve foi bloqueio por IP.

Sintomas que o bloqueio produz, e que apontam para o lugar errado:

- toda busca para em ~28 cartões sobre cabeçalhos de milhares, e nunca cresce;
- o travamento é **intermitente** — quatro tentativas na mesma URL deram `29, 29, 29, 216`;
- some quando se muda um parâmetro qualquer e volta depois, o que incrimina o parâmetro errado.

**Correção única: `--proxy auto` em `scripts/adlib_coleta.py`**, que usa o mesmo pool do projeto que o
ATC já usava. Medido em 20/09/2026, com proxy:

| Busca | Resultado |
|---|---|
| `emoglobina glicata`, IT | **384 IDs** de um cabeçalho de 380, na primeira tentativa |
| `eroscode`, DE, **com `--ordenar`** | **598 IDs** de um cabeçalho de 600 |
| `musesacademy`, **`--country ALL`** | 488 IDs |

> ⚠️ **Não culpar os parâmetros.** Durante a R017 chegou-se a registrar que `--ordenar` e
> `--country ALL` travavam a paginação. **Está errado**: as duas últimas linhas da tabela acima mostram
> os dois funcionando. A comparação que os incriminou não era controlada — uma amostra de cada lado,
> num intervalo em que o bloqueio ia e vinha. Antes de atribuir um platô a um parâmetro, **conferir o
> status HTTP da resposta**.

**Calibração:** com proxy, `emoglobina glicata` no filtro IT devolveu `gentilia.it` **157** e
`myavellis.com` **129**, contra os 162 e 132 do GOAL.

**Semente nova, que é o que achou as finalistas fora do nutra:** a frase **clínica** (`mein Arzt`,
`il mio medico`) entrega nutra; a frase de **funil** entrega infoproduto. Usar
`personalisierten Plan` (DE), `piano personalizzato` (IT), `plan personalizado` (ES),
`plan personnalisé` (FR), `persoonlijk plan` (NL), `spersonalizowany plan` (PL).

**Teste barato de "mesma operação":** o e-mail declarado no perfil da Página. Quatro das cinco
Páginas-persona do ErosCode declaram `support@eroscode.de` — mais barato que comparar destino.

**AdHeart — quatro filtros que mentem.** `link_search`, `domain`, `title_search` (nome da Página) e
`facebook_page` são **ignorados em silêncio**: devolvem resultado com HTTP 200, sem relação nenhuma com
o que foi pedido, e gastam busca da cota. Medido em 20/09/2026: `title_search=Tagebuch` devolveu 400
anúncios de confeitaria tailandesa e clínica estética. **Só `text_search` filtra de verdade** — toda
descoberta no AdHeart tem de passar por frase da copy.

**`read_jsonl` e o pool "corrompido":** a pendência que a R016 deixou aberta (27 linhas quebradas em
`reports/intel/pool.jsonl` desde 12/08/2026) **não era dado corrompido**. `read_jsonl` usava
`splitlines()`, que quebra também em ` `, ` ` e `` — caracteres que
`json.dump(ensure_ascii=False)` grava crus dentro das strings. O pool tem 24 ` ` em títulos.
Corrigido para `split("
")` em `scripts/arasaka_runtime.py`, com teste; a ingestão canônica voltou a
funcionar na mesma rodada.

## Correção explícita do usuário após E001 — 17/09/2026

Origem: conversa deste projeto, após a entrega da planilha visual E001.
Fala original: “acho que falta aprofundar mais nos dados ao acessar a biblioteca de anuncio de uns percebi que nao tava tao escalado assim tem que fazer acessar a biblioteca e validar a escala SEMPRE antes de confirmar se ta escalado ou nao anota isso no treinamento”.

- **Validação obrigatória na biblioteca pública em toda rodada:** antes de concluir sobre escala, abrir a Meta Ad Library ou o Google Ads Transparency Center e examinar os anúncios da oferta específica, além do cartão isolado. Acervo, fornecedor, preview ou classificação anterior não substituem essa revisão.
- Registrar URL, data/hora, filtros de país/período/status, IDs revisados, contagem com escopo e limites de cobertura. Separar anúncios ativos, inativos, variações e criativos realmente distintos; não atribuir o inventário inteiro do anunciante a um produto.
- Cruzar atividade e persistência com volume/distribuição disponíveis (alcance, impressões, views e sua janela), diversidade criativa e vínculo com a landing. Registrar sinais contrários, inclusive pouco alcance ou poucos anúncios da oferta apesar de um anunciante grande.
- Estar ativo, ter dois anúncios, uma copy forte ou uma página persuasiva não basta para classificar como fortes indícios de escala. Justificar a força da evidência da oferta, sem limiar numérico universal inventado.
- Biblioteca inacessível ou dados insuficientes: **validação pendente / escala indeterminada**. Não afirmar nem escala forte nem ausência de escala. Forte classificação exige revisão concluída e convergência de evidências; ainda assim usar “fortes indícios de escala”, sem tratar vendas/lucro como comprovados.
- Esta correção vale para todas as frentes e futuras consolidações. Os candidatos E001 precisam passar por este procedimento antes de serem reapresentados como escalados. O usuário não identificou quais ofertas contestou: não registrar rejeições individuais nem alterar suas avaliações por inferência.

## Feedback do lote E001 e lições da revisão — 18/09/2026

**Feedback humano literal:** “no fim parece que nada ta tao escalado assim anota no aprendizado tudo que e relevante”. Origem: conversa deste projeto, após a atualização da aba Funis da planilha E001. Escopo: qualidade da seleção do lote em relação ao objetivo de ofertas muito escaladas. Não é rejeição individual de todas as ofertas e não revoga as aprovações R003.

**Conclusão do agente sobre o processo:** a entrega ampliou a cobertura de ofertas e funis, mas não atingiu o objetivo de encontrar fortes indícios de escala alta. No consolidado revisado, 0/11 ofertas foram sustentadas como escala alta; isso mede o rendimento da seleção, não prova que nenhuma venda muito. O gargalo observado foi promover presença publicitária, afinidade e quantidade de IDs antes de demonstrar intensidade de distribuição. Limitações de acesso e dados também existem; esta amostra não permite culpar um nicho ou uma rede inteira.

Evidência: [revisão de 18/09](expansao/E001/consolidado/previews-escala-2026-09-18.json), [auditoria de 17/09](expansao/E001/consolidado/revalidacao-2026-09-17.json) e respectivos brutos. Aprendizados do agente:

1. **Ativo não é muito escalado.** Dos 13 IDs Meta revisitados, 9 estavam ativos, 3 inativos e 1 indisponível. Revalidar os finalistas perto da entrega; uma revisão de ontem não autoriza dizer “ativo agora”.
2. **A unidade decisiva é a oferta.** Nerdy tinha ~880 resultados da página, ~130 no filtro específico e apenas 23 cartões inicialmente revisados em 17/09. Não transformar esse conjunto em 880 criativos da oferta. Em 18/09, Calm trouxe ~6 resultados, mas só 1 tinha a landing exata; Phonics trouxe ~9, com 7 IDs da landing correta.
3. **Anúncio e oferta têm estados diferentes.** As peças selecionadas de Phonics e Calm ficaram inativas, mas outros IDs das ofertas continuavam ativos. Smoothie estava indisponível e a busca Lygia/ativos/EUA não trouxe resultados; isso não demonstra encerramento global nem cobre todos os afiliados.
4. **Distribuição precisa de contexto temporal e geográfico.** Unstuck exibia UE 34.729 / UK 5.858 contas e Popcorn UE 31.909 / UK 29.259 em 18/09, em IDs iniciados em maio/junho. São evidências de entrega acumulada; não demonstram intensidade diária alta. Baixo alcance UE não prova baixo volume EUA. Não somar alcances de IDs com públicos possivelmente sobrepostos.
5. **Quantidade e diversidade não são sinônimos.** Grupos de anúncios, cópias e variações podem inflar inventários. Contar IDs, grupos e criativos distintos separadamente; diversidade desconhecida permanece desconhecida. Diversos ângulos precisam de revisão de conteúdo.
6. **Funil confirmado resolve identidade, não escala.** Checkout, preço, produto digital, bônus e boa copy ajudam na aderência. Números de alunos, reviews e pop-ups de compra da própria landing são alegações do vendedor, não auditoria comercial. Psoas tinha divergência entre título e corpo Endo Body Reset: conferir anúncio → página → produto antes de tratar como uma oferta coerente.
7. **Cobertura continua incompleta.** A seleção visual revisada é Meta; dois registros Google são históricos. Não apresentar essa consolidação como cobertura atual equilibrada das duas redes. A preferência de pesos iguais continua válida.
8. **Apresentação não compensa evidência fraca.** Prévia real do criativo e screenshot da página devem ficar ao lado da conclusão. Imagens nativas nas células funcionaram; fórmulas IMAGE com URL temporária/acesso externo não são solução persistente. Screenshot de página não equivale a preview da VSL.

### Procedimento para a próxima seleção (agente, derivado do feedback)

- Fazer triagem curta de entregável/aderência, depois validar distribuição e inventário específico na biblioteca **antes** de investir em extração completa de funil e planilha extensa.
- Separar fila de descoberta de finalistas com fortes indícios. Presença expressiva sem distribuição mensurável permanece candidata a aprofundar; não entra como escala alta por quantidade de IDs.
- Para promover, apresentar uma tese explícita com evidência de distribuição contextualizada e sua corroboração por persistência, renovação ou diversidade real, vinculadas à mesma oferta. Contagens derivadas do mesmo inventário não são corroboração independente. Sem limiar universal inventado e sem exigir vendas privadas como pré-requisito.
- Quando só houver alcance acumulado de meses, buscar snapshots comparáveis ou outra evidência de intensidade recente. Dois snapshots próximos, atraso da fonte ou contador estimado não bastam para generalizar crescimento sustentável. Reobservações apenas quando houver execução solicitada; nenhum monitoramento automático foi criado.
- Priorizar sementes que já tragam sinal de distribuição relevante e depois testar aderência, incluindo o caminho VAV/domínio → YouTube → ATC que rendeu views na R003, respeitando recência e mistura orgânico/pago. Isso é hipótese de busca a testar, não garantia de melhores resultados.
- Entregar menos finalistas se necessário, com a lacuna explícita. Não reapresentar os mesmos candidatos moderados como fortes sem nova evidência. Medir rendimento por oferta qualificada, e não pelo tamanho ou beleza da planilha.

Registro coletivo mantido aqui; `avaliacoes.jsonl` continua reservado a avaliações individuais identificadas. Ranking hospedado não sincronizado. Este pedido atualiza aprendizado; não inicia coleta.

## Navegação e planilha obrigatórias — usuário, 19/09/2026

Origem: conversa deste projeto. Pedido explícito: “o sistema tem que verificar navegar
ate a pagina e ver se a escala confirma” e “no final sempre vai montar em planilha no
padrao que eu gosto”. Reforça o gate pós-E001 e vale para toda varredura de ofertas,
salvo mudança explícita do pedido.

- **Navegar antes de promover cada finalista:** abrir o anúncio/criativo, a biblioteca
  pública da rede e a página de destino exata; seguir até a oferta/produto para
  confirmar que as evidências pertencem ao mesmo item. URL ou HTTP 200 não comprova
  revisão da página. Registrar URLs finais, data/hora, conteúdo observado e evidência
  preservada da navegação.
- **Verificar se a escala se sustenta:** aplicar o gate pós-E001 acima, confrontando
  distribuição, janela, inventário específico e contraevidências. A landing confirma
  identidade e funil; alegações do vendedor não comprovam escala. Navegação concluída
  não equivale a escala confirmada. Bloqueio ou dados insuficientes exigem “validação
  pendente / escala indeterminada”; não resolver lacuna de auditoria mudando o texto.
- **Sempre finalizar com planilha visual Excel `.xlsx`:** preview real incorporado
  do criativo ao lado da análise e links clicáveis para anúncio/vídeo, biblioteca,
  landing e evidências. Screenshot da landing deve ser identificado como página,
  nunca como preview do criativo. Mídia indisponível fica como lacuna.
- **Padrão visual:** fichas legíveis por oferta, imagens com proporção preservada,
  texto sem cortes e URLs completas clicáveis na própria célula. Preferência mais
  recente: modelo `D:/Downloads/Arasaka R003 — anúncios, previews e funis.xlsx`, abas
  Comparativo, Previews e Funis; números, contagens e datas centralizados horizontal
  e verticalmente. Substitui a referência anterior R004 com Ranking/Fontes/Descartes.
  Cada ficha traz oferta, rede/mercado, análise do criativo, métricas com fonte,
  escopo e data, status da navegação, evidências favoráveis e contrárias e conclusão
  de escala. Distinguir sinal da oferta de sinal do criativo específico.
- **Conferir antes de entregar:** abrir/renderizar a planilha e revisar previews,
  legibilidade e destinos dos links; informar o que foi efetivamente verificado.
  Fórmula de hyperlink presente não prova destino funcionando. Entregar o arquivo
  e, quando a rodada usar Google Sheets, o link atualizado. Sem finalistas
  qualificados, entregar lacunas e descartes, sem completar com anúncios fracos.
  Evidência pública não comprova faturamento, lucro ou conversões.

## Hipóteses do agente — ainda não preferências do usuário

- Promessa forte, mecanismo específico, VSL/TSL, checkout direto e variações criativas
  ajudam a identificar o perfil procurado. Confirmar o entregável antes de chamar de info.
- Manifestação e reconquista foram apenas o primeiro recorte exploratório.
- Separar afinidade pessoal, aderência a infoproduto, atividade e evidência de escala.
  Uma oferta pode agradar e ter escala desconhecida; anúncio ativo não comprova lucro.

## Lições da R001 — 17/09/2026

1. `get him back`: 105 de 114 anúncios retornados com tag de fornecedor `novel`.
   Evitar repetir como termo amplo. Próximo teste deve usar mecanismo/entregável dos
   exemplos que o usuário aprovar; não inventar suporte a palavras negativas na API.
2. `manifestation`: 57 de 118 com tag `novel`. A própria Her Cosmic Secret tinha essa
   tag e apareceu na biblioteca pública com oferta direta; tag sozinha não decide exclusão.
3. AdHeart `--market us` mapeia para idioma `en`, sem filtro de país de entrega.
   País precisa de verificação pública adicional; idioma retornado também pode divergir.
4. Três anúncios no recorte AdHeart e ~52 resultados na página pública são escopos
   diferentes. Não calcular crescimento 3→52 nem somar as contagens.
5. Raiz de domínio vazia não prova funil indisponível. A biblioteca revelou o caminho
   `/desert-spell`, ausente do bruto reduzido pelo coletor.
6. As duas sementes Google verificadas não deram candidato atual nos recortes usados.
   Preservar essa lacuna e renovar sementes; não compensar silenciosamente com Meta.

## Lições da R002 — 17/09/2026

Observações do agente; nenhuma delas substitui avaliação humana. Evidência e limites
na [rodada R002](rodadas/R002-2026-09-17.md).

1. Dez buscas retornaram 1.080 registros de anúncios / 1.049 IDs do fornecedor.
   Expansão de páginas a partir de `woodworking plans`, `somatic` e `Hypnose` gerou
   oito candidatos de copy/funil, em quatro anunciantes. Isso não é precisão literal
   por termo nem revisão audiovisual completa.
2. `Abnehmprogramm` trouxe 97 registros Oviva entre 120; filtro por programa ainda
   pode concentrar empresas institucionais. `sourdough` também trouxe muito produto
   físico. Reavaliar termos por entregável e mecanismo após feedback.
3. O Google continuou com baixo rendimento nas sementes históricas: dez anunciantes
   revisados, nenhum candidato atual qualificado. Um anunciante associado a energia
   mostrava software de escrita; validar criativo atual antes de herdar nicho/domínio.
4. Planos DIY, educação infantil e workbooks são hipóteses de diversidade. Não concluir
   que o usuário prefere essas categorias antes de ele avaliar as fichas.
5. Oito produtos/entradas não equivalem a oito anunciantes independentes. R002 tem
   quatro anunciantes e uma masterclass gratuita sem produto pago confirmado.
6. Nenhum candidato recebeu conclusão de escala. Anúncios recentes e contagens de
   página não provam volume; um ID exibiu faixa inferior a 100 impressões no cartão.

## Lições da R003 — 17/09/2026

Observações do agente, não preferências individuais. Ver [R003](rodadas/R003-2026-09-17.md).

1. Sementes VAV com landing identificada, seguidas de busca pública por domínio no
   Google, localizaram seis vídeos não listados com milhões de views, em três ofertas.
   Isso justifica testar esse caminho antes de gastar em termos genéricos recentes.
2. Oito vídeos distintos tiveram transcrições exportadas. Separar views do vídeo,
   data de publicação, último visto pelo fornecedor e última exibição no ATC.
   Publicação antiga e anúncio atual não demonstram gasto contínuo nesse intervalo.
3. Alcance europeu pode ser baixo mesmo em páginas com centenas de anúncios.
   Registrar essa contraevidência; não atribuir contagem de página a uma oferta nem
   atribuir alcance de um ID aos demais criativos da mesma oferta.
4. ESA é híbrido de software/afiliado com cursos; Retirement Trade confirma guia
   gratuito, sem produto pago posterior verificado. Interesse nessas estruturas
   permanece hipótese até o usuário avaliar.
5. Os 15 candidatos têm força desigual: seis vídeos com milhões de views, dois
   com distribuição recente menor e sete Meta com persistência/portfólio. Não
   promover todos a escala forte individual para cumprir quantidade.

## Feedback humano R003 — 17/09/2026

Origem: Google Sheets `1c0s3qq0vOs0jJSUbUmGK-PLYUDHUplu9YKxOrye4qkY`, aba
Comparativo, Z7:AA14. Falas literais e células preservadas em `avaliacoes.jsonl`;
snapshot bruto em `spy/data/playground/R003/feedback-sheets-2026-09-17.json`.

### Preferências confirmadas pelos exemplos

- **Replicabilidade operacional:** priorizar ofertas que não dependam da audiência
  ou autoridade pessoal já construída pelo apresentador. BLB (03) foi rejeitada
  por essa dependência percebida, apesar dos milhões de views. Isso registra a
  avaliação do usuário, não uma medição da origem do tráfego do anunciante.
- **Venda direta e entrega identificável:** Upgrade Your Life (07/08) foi rejeitada,
  embora o conceito tenha agradado. O usuário questiona captura para curso versus
  produto com checkout e entrega direta, e rejeita dependência de branding pessoal.
  Captura sem produto/compra confirmados não passa automaticamente para finalista.
- **Referências positivas:** Blood Sugar Fix (09/10), Black Book (11/12) e Little
  Dictator (13). O usuário chamou as três estruturas de replicáveis e excelentes.
- **Vários ângulos para um produto:** preferência explicitada em 11/12/13. Buscar
  abordagens distintas ligadas ao mesmo entregável, distinguindo ângulo de simples
  variação visual ou reutilização de mídia.
- Nome de autor ou rosto no anúncio, por si só, **não exclui**: Stan Taylor foi
  aprovado. O fator é a dependência percebida de reputação/audiência prévia.

### Aplicação na próxima triagem (procedimento do agente)

1. Antes de ordenar por views, verificar: produto pago/entregável, percurso de venda,
   dependência de audiência pessoal e adaptação possível do mecanismo/ângulo.
2. Registrar `dependencia_marca_pessoal` como baixa/alta/incerta, com evidência e
   justificativa; não inferir audiência paga/orgânica apenas pelo rosto conhecido.
3. Produto com checkout e entrega direta ganha prioridade. Checkout não acessível
   permanece lacuna, não exclusão universal: Blood Sugar Fix foi aprovado mesmo
   sem checkout confirmado. Funil exclusivamente de captura/call fica pendente
   para revisão antes de entrar na lista principal.
4. Usar as ofertas aprovadas como sementes de estrutura e mecanismo em ambas as
   redes, sem restringir o universo a saúde, livros ou Meta.
5. Só então comparar atividade, views e idade, alcance e diversidade de anúncios.
   Aceitar indícios com limites claros; afinidade humana não comprova escala.

### Hipóteses de busca para testar, ainda não preferências universais

- Saúde com programa digital: mecanismos de rotina/refeição, guia ou protocolo,
  pré-venda → VSL → produto. Exemplos de termos: `blood sugar guide`,
  `morning meal protocol`, `blutzucker programm`. Confirmar que não é suplemento.
- Comportamento: ebook/workbook/protocolo com diversos problemas de entrada.
  Exemplos: `21 day protocol`, `boundaries workbook`, `persuasion ebook`.
- Parentalidade: autonomia infantil e mudança de hábitos dos pais, com entrega
  digital. Exemplos: `parenting workbook`, `independent kids`, `parenting protocol`.
- Nas três frentes, expandir por landing/oferta/anunciante associado aos aprovados
  e procurar criativos atuais em Google/YouTube e Meta com o mesmo peso.
- Não interpretar 5/5 Meta e 0/3 Google como preferência de rede: a amostra contém
  só três ofertas Meta e duas Google, com estruturas diferentes.

Resultado descritivo do lote: 5/8 anúncios aprovados (62,5%), 3/5 ofertas aprovadas
(60%). Duplicatas de oferta não contam como evidências independentes de preferência.
Sem nova coleta ou mudança de pesos do ranking hospedado nesta atualização.

## Aprendizados e entrega R005 — 19/09/2026

Origem: conversa `01a0bb0a-9019-70c2-9e00-bc032957f89e`, aprovação de Reverse Health.

Preferências explícitas desta rodada:
- Guardar ofertas que gostou em [favoritas](../ofertas-favoritas/README.md). Registrar
  aprovação individual em avaliacoes.jsonl; motivo não dito continua ausente.
- PDF executivo para compartilhar com sócio, com imagens reais do site/app, legendas,
  provas e URLs completas clicáveis; número de páginas deve acomodar a evidência.
- Excel no modelo R003, números/datas centralizados e links diretos, sem “ver coluna X”.
- Acompanhar o PDF de uma linha para WhatsApp: `Nicho / Entregável ou APP / Região
  comprovada / Gasto simulado + período (não confirmado)`.
- Mostrar simulação pelo período total observado, não arbitrariamente sete dias.
  Preferência final: um único cenário médio, sem destacar cenário superior.

Lições de evidência (agente, derivadas das correções e auditoria):
1. Domínio, oferta, ângulo e página não são intercambiáveis: 135 anúncios antigos do
   domínio não comprovam 135 do mesmo funil. As amostras 145/191 não são somáveis.
2. Idioma, filtro ALL/BR e parâmetro region=MX não comprovam entrega. Abrir detalhes
   → transparência por localização → alcance por país. Confirmamos Portugal e outros
   países UE para Nia 1032053193151588; não generalizar para toda a operação.
3. Preservar discrepâncias: UE 101.811 no total versus 100.583 nas linhas demográficas.
   Alcance não é impressão, gasto ou janela de sete dias; não somar públicos de IDs.
4. Separar idade dos anúncios: 37 dias no mais antigo do ângulo; 12 no ID com alcance
   UE. Nenhum desses valores prova veiculação ininterrupta de todo o inventário.
5. Média de cenários é aritmética de premissas, não gasto médio observado. 135 ×
   US$ 27,50 × 37 = US$ 137.362,50 é simulação; inventário constante não foi comprovado.
   Não reaproveitar US$ 5–50 como benchmark. Para estimar histórico, obter entrega e
   gasto por período; não converter números hipotéticos em “600k gastos”.
6. App pode conter conteúdo de info e assinatura: explicar entregável concreto,
   recorrência, preço e pacote ainda não confirmados. A aprovação de Reverse Health
   é um exemplo positivo, não uma preferência universal por apps ou grandes marcas.

### Promoção de lições — critério geral

Toda mudança deve apontar para rodada/avaliação, dizer se é preferência explícita,
observação ou hipótese e registrar a data. Para generalizações de gosto, procurar
repetição em exemplos distintos e preservar contraexemplos. Não concluir que todo um
nicho é ruim porque uma oferta foi reprovada por formato ou ausência de métricas.

## Aprendizados R006 — 19/09/2026

> **Ressalva R007:** itens 1–3 abaixo são registro histórico corrigido. Os 486 anúncios não foram deduplicados por ID individual, e os checkouts possuem variantes distintas. Aplicar as regras R007 a seguir.

Origem: [R006](rodadas/R006-2026-09-19.md). Observações do agente; a oferta ainda não
foi aprovada pelo usuário.

1. Contagem de perfil e contagem de oferta podem divergir em sentidos diferentes:
   o cabeçalho mostrou ~420 resultados para todo o perfil, enquanto 56 grupos do
   bundle representavam 486 anúncios subjacentes. Registrar grupos e anúncios únicos,
   deduplicar pelo ID representativo e explicitar o recorte de copy/destino.
2. Migração de landing não cria automaticamente outra oferta. Nesta rodada,
   `learn.coachmariawendt.com/instagram-bundle-8/` e `enroll.coachmariawendt.com/`
   usavam a mesma promessa, entregável e checkout; foram separados por domínio e só
   depois consolidados no mesmo funil.
3. Um único ID com alcance UE de 213.325 superou a evidência unitária da R005, mas
   continua sendo evidência daquele anúncio. Não extrapolar alcance para 486 ativos.
4. Provar escala não elimina risco de replicabilidade: o volume é forte, enquanto a
   dependência da autoridade pessoal é uma contraevidência relevante e deve aparecer
   antes de eventual promoção a favorita.
5. Falha de coleta sem recibo não autoriza retry automático. Preservar a quota e seguir
   com fontes públicas/acervo quando a investigação ainda puder avançar.

## Aprendizados R007 — 19/09/2026

> **Correção explícita do usuário após a entrega:** “essa oferta ja estava na minha lista”. R007 não cumpriu o pedido de trazer mais uma oferta: reauditoria não conta como descoberta adicional. Antes de selecionar nova oferta, cruzar rodadas, favoritas, avaliações e `/meus` com a identidade correta. Não limitar exclusão às favoritas nem somente à Reverse Health. O comentário não é rejeição do produto nem autorização para favoritas. Substituída por ReciMe na [R008](rodadas/R008-2026-09-19.md), aguardando avaliação.

Origem: [R007](rodadas/R007-2026-09-19.md). Observações metodológicas do agente, não feedback comercial do usuário.

1. Nunca multiplicar a idade de um representante pelo tamanho de seu grupo. Membros do mesmo grupo podem ter datas diferentes. Contar IDs explícitos uma vez; expansão incompleta fica como limite inferior, e grupos/criativos únicos ficam indeterminados.
2. Priorizar texto nativo Meta: extensões podem mostrar “Today”, “0 days” ou “creatives” de modo incompatível com a data/unidade nativa. Não usar esses rótulos auxiliares para idade ou inventário.
3. Separar hostname e caminho antes de consolidar oferta. `/carousel` não pertence automaticamente ao bundle da raiz. Mesma oferta pode ter checkouts variantes; preservar os percursos A e B.
4. Busca ampla por marca pode misturar anunciantes alheios. Copy que cita Coursiv com destino certipath.ai não comprova identidade/controle da oferta. Busca exata sem resultados não prova inatividade global.
5. País comprovado exige entrega positiva nas linhas de transparência. Se soma demográfica divergir do cabeçalho, preservar ambos e explicitar a divergência; não substituir nem somar públicos entre IDs.
6. Resultado vigente do bundle: 215 IDs, 153 iniciados >7 dias, um perfil. Alcance de 213.502 em um ID; não extrapolar aos demais. Escala não elimina a limitação de replicabilidade por autoridade pessoal. Nenhuma aprovação inferida.

## Aprendizados R008 — 19/09/2026

Origem: [R008](rodadas/R008-2026-09-19.md). Observações metodológicas do agente; ReciMe ainda não aprovada pelo usuário.

1. Fazer exclusão de novidade antes de aprofundar: lista pessoal `/meus`, favoritas, avaliações e rodadas. Catálogo geral de mercado não equivale à lista do usuário; reauditoria de oferta conhecida não cumpre “mais uma”.
2. Para superar 100 anúncios antigos sem expansão completa, usar corte conservador de IDs sem rótulo de grupo. ReciMe: 403 IDs, 237 com data antiga no card, **131 sem grupo e >7 dias**. A rota principal sozinha tem 110.
3. App, plano pago e percurso de aquisição são escopos distintos. Quatro rotas da ReciMe levam ao mesmo app, mas não comprovam um único checkout/plano Plus. Separar smart link, quiz, Google Play e App Store.
4. Parcerias não duplicam a contagem por perfil. Atribuir cada ID ao perfil primário e manter parceiro separado; 35 perfis não demonstram 35 contas publicitárias independentes.
5. Ficha de compras internas pode listar preços sem duração. Registrar SKUs observados e recorrência comprovada na ajuda, sem inventar vínculo preço/período. Instalação gratuita não é assinatura paga comprovada.
6. Na Meta, uma extensão de análise ocultou o corpo dos detalhes. Fechar só a sobreposição restaurou a transparência nativa; não declarar bloqueio da biblioteca antes de conferir a interface. Datas e métricas de extensões não substituem dados nativos.
7. Comparações entre rodadas devem confrontar unidades e períodos. Os 191/135 derivados dos grupos da R005 não são equivalentes a 131 IDs sem grupo. O alcance unitário 366.563 supera 101.811 na evidência registrada, sem provar maior gasto ou vendas totais.
8. QA dos arquivos: formatar IDs como texto antes da escrita evita notação científica; validar hyperlinks, fórmulas, imagens embutidas e datas reais. Se o renderizador não mostrar imagens, conferir mídias/âncoras e registrar a limitação, sem alegar teste no Excel nativo.

## Aprendizados R009 — 19/09/2026

Origem: [R009](rodadas/R009-2026-09-19.md). Observações metodológicas do agente; nenhuma preferência comercial nova foi expressa pelo usuário.

1. Produto Digistore24 ativo e página de vendas ativa não bastam separadamente: provar o caminho real anúncio → landing/VSL → checkout. Midas tinha produtos DS24 `439785` e `439776`, mas sua rota principal atual identificava ClickBank.
2. Frase de produto não é identidade de oferta. A busca “The Billionaire Brainwave” retornou Destiny Engine e Your Wish Is Your Command; domínio, entregável e pagamento distintos zeram a atribuição à oferta DS24 homônima.
3. Catálogo oficial comprova existência no marketplace, não atividade publicitária, preço atual ou entrega nos EUA. AOV/comissão são métricas do fornecedor, não vendas, gasto ou preço.
4. Coleta com recibo pode ser integralmente ruidosa. Nesta rodada, 1.316 registros brutos e 139 normalizados produziram zero correspondências reais; não transformar volume coletado em evidência de escala.
5. Quando nenhum candidato fecha nicho + gateway + país, registrar pendentes e descartados e terminar com bloqueio concreto. Não trocar o recorte nem promover o “menos errado”.
6. Manter [OFERTAS-MAPEADAS.md](OFERTAS-MAPEADAS.md) como porta de exclusão por identidade. Estados de pesquisa, entrega, favorita e uso são independentes.

## Aprendizados R010 — 20/09/2026

Origem: [R010](rodadas/R010-2026-09-20.md). Itens 1–5 são observações metodológicas do agente. O item 6 registra o escopo expresso pelo usuário nesta rodada, não uma preferência comercial permanente.

1. Cabeçalho alto pode representar lançamento sem persistência. WalkFit mostrou ~1.300 resultados, mas os 88 IDs carregados começaram entre 15 e 19/09 e nenhum atendia `>7 dias`. Separar volume atual de idade individual.
2. Busca por domínio hifenizado pode sofrer correspondência por tokens. `dance-bit.com` trouxe milhares de anúncios alheios; o domínio oficial `dancebit.dance` isolou apenas um ID. Exigir destino/perfil coerente antes de contar.
3. Domínio amplo de marca mistura produtos. `betterme.world` reuniu saúde mental, fitness e loja; o recorte defensável da oferta escolhida foi `mind-quiz.betterme.world`.
4. Persistência superou o cabeçalho como critério de desempate nesta rodada. BetterMe teve 148 IDs carregados e 140 >7 dias; Yoga-Go teve 110/9, Muscle Booster 91/20 e WalkFit 88/0.
5. QA de imagens em XLSX precisa distinguir renderização e incorporação. Quando o preview do Artifact Tool omitir desenhos, verificar `xl/media/` e relacionamentos em `xl/drawings/`, registrar a lacuna e não afirmar revisão em Excel nativo.
6. Escopo expresso pelo usuário: para esta varredura, remover nicho e gateway fixos e buscar as ofertas mais escaladas nos Estados Unidos. Isso não altera avaliações anteriores nem cria favorita.

## Aprendizados R011 — 20/09/2026

Origem: [R011](rodadas/R011-2026-09-20.md). Observações do agente; nenhuma preferência humana nova foi inferida.

1. Gerar um PDF por oferta não autoriza chamar toda candidata de escalada. Primeiro aplicar o gate; candidatas sem atividade atribuível ficam sem PDF de “escala”.
2. Uma busca por domínio pode misturar outras ofertas do mesmo produtor. Para o bundle de oito cursos, a frase exata `"8 Instagram courses"` isolou ~80 resultados ativos no filtro US.
3. Inventário atual e histórico não são aditivos. Os ~80 atuais da frase exata não foram somados aos 215 IDs consolidados na R007.
4. Escala e replicabilidade continuam separadas: Maria Wendt tem volume e persistência, mas depende fortemente de autoridade pessoal e audiência própria.

## Aprendizados R012 — 20/09/2026

Origem: [R012](rodadas/R012-2026-09-20.md). Observações metodológicas do agente; nenhuma preferência humana nova foi inferida.

1. **`ad_volume` de minerador não é inventário ativo.** Tyver indicou 1.600 anúncios para `rachelkarlauthor.com` e 1.096 para `thefunktionalnutritionist.mykajabi.com`; a Ad Library no filtro US devolveu **0** e **~18**. O campo do fornecedor é acervo histórico do catálogo dele, não anúncios ativos no recorte. Sempre reconferir na biblioteca pública antes de promover.
2. **Contar o destino, não só o ID.** Em `fit4me.io`, os 188 IDs carregados tinham **188 destinos no próprio domínio** — atribuição de 100%. Esse teste separa escala real de correspondência por token (armadilha da R010 com `dance-bit.com`) e deve virar rotina: extrair o hostname de cada `l.facebook.com/l.php?u=` e contar.
3. **Nenhum minerador contratado cobre YouTube.** Anstrex é nativa, Tyver/Foreplay/Adyntel/Trendtrack são Meta, MineraROI é catálogo BR. VAV/TubeSift, Deeptube e VidTao — as três rotas de YouTube — estavam indisponíveis. A frente Google/YouTube só avançou porque foi minerada direto no ATC.
4. **O ATC é minerável e tem descoberta própria — e o repositório já sabia.** `suggestions_blaster.py`, `advertiser_amplifier.py`, `f020_searchsuggestions_nutra_us.py` e `T-044_advertiser_scraper.py` em `spy/code/` usavam os mesmos RPCs desde maio/2026 para nutra. As sondas da R012 foram escritas sem conferir esse acervo: antes de criar coletor, procurar em `spy/code/discover` e `spy/code/scout`. `SearchService/SearchSuggestions` com payload `{"1": termo, "2": codigo_regiao}` devolve anunciantes com `advertiser_id` e contagem; `SearchCreatives` com `{"2": n, "3": {"1": advertiser_id, "8": [regiao]}, "7": {"1": 1}}` lista criativos; `GetCreativeById` devolve **países com primeira/última exibição e faixas de impressão** por país. É a evidência mais rica de qualquer fonte usada até aqui. Sonda em `scripts` de sessão do ATC; sofre `RateLimitError` com duas execuções paralelas — rodar uma por vez, com pausa.
5. **O filtro de plataforma do ATC precisa de controle antes de virar evidência.** `?region=US&platform=YOUTUBE` na URL funciona, mas o cabeçalho satura em "Cerca de 200". Para provar que o filtro discrimina, medir um anunciante-controle: `MANIFESTING REALITY` tem 200 no total e **0** sob YouTube. Sem esse controle, "200 no YouTube" seria indistinguível de "filtro ignorado".
6. **Teto de exibição não é inventário.** Tanto "~200" do ATC quanto o cabeçalho aproximado da Meta são limites da interface. Registrar sempre como teto/estimativa e apoiar a conclusão na amostra explícita de IDs.
7. **Anúncio de vídeo no ATC não entrega o `video_id` do YouTube.** O preview roda em `safeframe` de origem cruzada (`tpc.googlesyndication.com`) e nem o DOM nem os RPCs expõem o identificador. A reconciliação `anúncio Google → vídeo YouTube` fica como **elo faltante declarado**; os demais elos (anúncio → destino → produto → checkout) fecham normalmente.
8. **Anunciante sem landing confirmável não vira finalista.** `Bigseo Academy SL` tinha ~200 anúncios YouTube e criativos majoritariamente em vídeo, mas o ATC não expõe o destino e `bigseo.es` retornou 0. Sem identidade de oferta não há auditoria — descartar, não promover.
9. **Infoproduto BR do acervo não anuncia no Google.** Os 50 domínios mais fortes de relacionamento e renda extra do acervo foram sondados no ATC região BR: **0 criativos em todos os 50**. Para a frente Google/YouTube, partir de domínios de Meta é caminho improdutivo; partir do próprio ATC é o caminho que rende.
10. **Serviço não é infoproduto.** `Psychic Samira LLC` tinha 67 anúncios no filtro YouTube, mas leitura psíquica é prestação de serviço, sem entregável digital identificável. Volume alto não dispensa o teste de entregável.
11. **Paywall pós-quiz mantém preço em aberto.** O funil `fit4me.io/military/v1/` só revela a oferta após 36 etapas. Percorrer até o fim exige interação real (cliques por coordenada; `element.click()` via JS não dispara o framework) e esbarra no risco de campo de dado pessoal. Registrar preço como **não confirmado** é preferível a inventar, e a evidência de escala não depende dele.

## Aprendizados R013 — 20/09/2026

Origem: [R013](rodadas/R013-2026-09-20.md). Observações metodológicas do agente; nenhuma
preferência humana nova foi inferida e nenhuma avaliação foi criada.

1. **O teto de "Cerca de 200" do ATC não é universal — a lição 5 da R012 generalizou cedo demais.**
   Sob `?region=US&platform=YOUTUBE`, `COURSIV LIMITED` marca **~20 mil anúncios** e
   `Digital Doers LP` **~2 mil**. A saturação em 200 era característica daqueles anunciantes,
   não um limite da interface. O cabeçalho continua sendo estimativa, e o controle continua
   obrigatório: `MANIFESTING REALITY` (`AR13664194876038709249`) devolve **tela vazia** sob o
   mesmo filtro, o que prova que ele discrimina.

2. **`GetCreativeById` responde embrulhado em `"1"`.** O campo `"17"` com países não está na raiz
   da resposta: está em `resposta["1"]["17"]`, e cada item vem como `{"1": codigo_regiao,
   "5": yyyymmdd}` — não como os objetos de epoch que a documentação da R012 descrevia.
   Ferramenta criada nesta rodada: `scripts/atc_paises.py`. As faixas de impressão vieram
   **nulas** em todos os criativos US consultados; ausente continua ausente, não zero.

3. **Qualquer script novo do ATC precisa de `next_proxy("us")`.** `build_session()` sem proxy
   leva a `RateLimitError` na homepage já na terceira tentativa. As sondas da R012 já faziam
   isso; a primeira versão de `atc_paises.py` não fazia e falhou de imediato.

4. **Captura de tela do ATC com Playwright headless cai em reCAPTCHA.** O QA dos PDFs só
   descobriu isso porque as páginas foram **renderizadas e olhadas**, não apenas geradas — a
   imagem estava lá, com o tamanho certo, e era a tela de "unusual traffic". A saída é usar o
   mesmo proxy residencial da sessão do ATC também no navegador de captura. Conferir arquivo
   gerado não é conferir conteúdo do arquivo.

5. **`&` quebra o texto do hyperlink no reportlab.** `Paragraph` parseia mini-HTML, então
   `?region=US&platform=YOUTUBE` era exibido como `platform;=YOUTUBE`. O `href` funcionava e a
   URL visível estava errada — exatamente o tipo de defeito que "fórmula de hyperlink presente
   não prova destino funcionando" antecipa, mas na direção inversa. Escapar `&` como `&amp;`.

6. **O leaderboard `a/channels` do VAV é a porta de entrada de renda extra nos EUA.** Duas páginas
   (160 canais, janela de 1 mês, ordenado por `videocount`) separaram, sem nenhum insumo da Meta,
   os anunciantes de infoproduto de renda extra dos anunciantes de marca: Coursiv, FPA Workshop,
   Tax Lien Code, Aleric Heck, Grant Cardone, Jon Penberthy, The Multifamily Mindset, Awesomely.
   **O campo que decide é `lastseen`, não `videocount`:** Multifamily Mindset tem 860 vídeos e
   parou em 25/04; PublishingDotCom tem 718 e parou em 20/05/2025.

7. **A contagem de vídeos vistos nos últimos sete dias separa rotação viva de acervo.** Coursiv:
   135 de 149. FPA Workshop: 13 de 139. Tax Lien Code: **0** de 150. Aleric Heck: 6 de 150. É o
   equivalente, no VAV, ao corte de sete dias da Meta, e deve entrar na rotina do pivô por canal.

8. **A busca por frase exata na Meta é obrigatória para domínio.** `q=highticket.io` com
   `keyword_unordered` devolveu ~2.100 resultados contaminados por qualquer anúncio que
   escrevesse "high-ticket" — inclusive Cole Gordon / closers.io. A mesma busca como
   `search_type=keyword_exact_phrase` com o domínio entre aspas caiu para ~770 e passou a ser
   auditável. É a armadilha de token da R010 reaparecendo em outra forma.

9. **O platô da Ad Library é impaciência, não limite da plataforma — e essa foi a pior medição
   desta rodada.** `window.scrollTo` não carrega nada: o scroll é de um `div` interno com
   `scrollHeight > clientHeight`. Achado esse contêiner, a primeira leitura ainda parou em 108 IDs
   para um cabeçalho de ~770 e registrou isso como "o carregamento estabilizou". Não estabilizou:
   chamadas sucessivas de rolagem levaram `highticket.io` de **108 → 257 → 357 → 625 → 767**,
   `fpaworkshop.com` de **24 → 152** e `1orderaway.com` de **30 → 103**. A primeira leitura
   subestimou o inventário em até **sete vezes** e distorceu conclusões: `1orderaway.com` parecia
   "lote único de 23/07" quando tem série de julho a setembro. **Regra:** só declarar platô quando
   várias chamadas seguidas de rolagem não moverem a contagem, e comparar sempre o total carregado
   com o cabeçalho antes de concluir. Enquanto a contagem sobe, a amostra não está pronta.

10. **Contagem de anúncio ativo responde "se", não "quanto".** O que mede intensidade é a
   combinação de volume, velocidade de renovação e permanência — e as três finalistas mostraram
   assinaturas opostas com contagens parecidas. HighTicket.io: 705 dos 767 anúncios nasceram em
   setembro e **nenhum** passa de 60 dias (velocidade). Coursiv: 98 vídeos novos em 7 dias, vida
   mediana de **0 dia**, mas operação ininterrupta desde julho/2024 (fábrica de criativo). FPA:
   só 13% de criativo novo, 51 vídeos acima de 90 dias e o mais antigo com **1.581 dias no ar**
   (longevidade). Calcular sempre: novos na janela, vida mediana, idade do mais antigo e fração
   acima de 90 dias. Sem isso, "escalado" é uma palavra, não uma medida.

11. **Longevidade é o sinal mais próximo de dinheiro que a evidência pública permite.** Anúncio
   pago não fica no ar por inércia: quem sustenta um criativo por 1.581 dias renova essa decisão
   todo dia com dados de retorno que não vemos. Volume alto por pouco tempo prova orçamento;
   volume alto por muito tempo prova que o orçamento está voltando. Isso **não** é faturamento e
   não autoriza número nenhum de receita, gasto ou ROAS — é a ponte honesta entre distribuição
   observável e a pergunta "faz dinheiro?".

12. **Trustpilot é proxy de terceiro para volume de clientes, com ressalva obrigatória.** Coursiv
   142.745 avaliações (4,6), FPA 3.551 (4,8), HighTicket.io 2.779 (4,7) — as três com perfil
   reivindicado e assinatura paga, o que significa que solicitam avaliação ativamente. Serve como
   ordem de grandeza; nunca como contagem auditada de clientes e jamais como receita.

13. **Domínio alheio no recorte pode ser a mesma oferta.** Os 10 IDs de `1orderaway.com` foram
   registrados como contraevidência de atribuição — até o domínio ser aberto e **redirecionar para
   `go.highticket.io`**, o mesmo funil. A atribuição real subiu de 91% para 99%. **Abrir cada
   destino "alheio" antes de contá-lo contra a oferta**, e quando for alias, medir os domínios em
   separado sem somar.

14. **Zero na Meta é resultado, não falha.** `"coursiv.io"` no filtro US + ativos devolveu
    "nenhum anúncio corresponde": Coursiv é oferta **nativa de Google/YouTube**. Antes de
    concluir que uma oferta forte "não foi encontrada" na outra rede, confirmar que a busca
    exata foi feita — e então registrar a ausência como a informação que ela é.

15. **O vertical `novel` contamina termos de renda extra no AdHeart.** `affiliate marketing` e
    `make money online` trouxeram `h5.reelshortnovel.com` como domínio nº 1 do recorte, com 66
    anúncios — aplicativo de micronovelas. Filtrar o vertical antes de ordenar por `n_ads`.

16. **Cabeçalho alto com data única é lançamento, não escala.** `workshopsforretirement.com`
    exibia ~1.100 resultados e `highticketlandflipping.com` ~66, mas **todos** os IDs carregados
    de cada um começaram dentro de uma janela de três dias. É a lição 1 da R010 (WalkFit)
    confirmada por dois casos novos: a distribuição das datas de início vale mais que o cabeçalho.

17. **Funil de renda extra escalado nos EUA esconde o preço atrás de captura.** As três
    finalistas — evento ao vivo (HighTicket.io), masterclass ao vivo (FPA) e quiz (Coursiv) —
    só revelam a oferta paga depois de um formulário. O checkout ficou **não confirmado** nas
    três, sem que isso enfraquecesse a evidência de escala. O US$ 20 que aparece no criativo da
    Coursiv é promessa do anúncio, não preço verificado; registrar como alegação.

18. **Teste de dono-vs-afiliado: buscar pela marca, não pelo domínio, e contar anunciantes.**
   A busca por domínio mostra o inventário; a busca pela **marca** mostra quem mais está usando
   aquele nome. Combinada com a contagem de entidades anunciantes do ATC, separa dono de rede de
   afiliados em duas consultas. Nas três finalistas da R013 deu **um anunciante para cada**:
   `Brook Hiddink` (~1.300 resultados) sobre `BERH Stores & Consulting - FZCO Inc.`,
   `Fiction Profits Academy` (~180) sobre `Digital Doers LP`, e `COURSIV LIMITED` sozinha no ATC
   com a Coursiv **sem nenhum anúncio próprio na Meta**. Atribuição de destino entre 99% e 100%,
   nenhum domínio de rastreio, nenhum redirecionador de terceiro. **Nenhuma era afiliado escalando.**

19. **Citação de marca no criativo não é afiliado — pode ser concorrente pegando carona.**
   Buscar `coursiv` na Meta devolveu ~33 anúncios, todos da Página `Peter Brown`, copy em espanhol
   citando a Coursiv e destino em `certipath.ai` — **zero** em `coursiv.io`. Não manda tráfego para
   a marca citada, logo não é afiliado dela. Confirma e amplia a lição 4 da R007: antes de contar
   um anúncio a favor de uma oferta, **conferir o destino**, não a menção.

20. **Marca corporativa e marca pessoal são eixos separados de "é do dono".** As três finalistas
   eram todas operação própria, mas com branding oposto: Coursiv é pessoa jurídica sem rosto
   (Limassol, categoria "Education Center"), enquanto HighTicket.io e FPA vendem o rosto de uma
   pessoa (Brook Hiddink, Karla Marie) com a PJ no rodapé. Pela preferência de replicabilidade da
   R003, o primeiro perfil é o interessante — mas é também o mais caro de copiar, porque o ativo
   deixa de ser a autoridade e passa a ser a linha de produção de criativo. Registrar os dois
   campos: **quem anuncia** (dono/afiliado) e **o que é vendido como marca** (empresa/pessoa).

21. **Classificar a rede de uma oferta exige consultar as duas, mesmo com evidência forte em uma.**
   A HighTicket.io entrou na R013 como "Meta" porque a descoberta veio do AdHeart e a Meta bastava
   para o gate. A sonda do ATC feita depois devolveu **400 criativos, 390 em vídeo**, do mesmo
   anunciante, desde **22/02/2026** — cinco meses antes do anúncio mais antigo da Meta. A oferta
   roda nas duas redes e foi rotulada errado por não ter sido perguntado. Sondar as duas antes de
   escrever a rede no registro.

22. **As três vias públicas de magnitude foram esgotadas na R013 e nenhuma entrega gasto,
   receita ou lucro.** Pedido do usuário em 20/09/2026 ("quanto de lucro no mínimo"). O que foi
   tentado, e o que cada uma devolveu:
   - **Faixa de impressões do ATC (`GetCreativeById`, campo `"4"`)**: `null` em todos os criativos
     US consultados **e também** nos criativos servidos em região europeia (IT), onde a R012
     supunha que apareceriam. A suposição da R012 não se confirmou para estes anunciantes.
   - **Transparência da UE na Meta**: existe para a HighTicket.io, mas o alcance de um ID é de
     **33 contas em toda a UE**, com a própria ficha declarando que o anunciante *não direcionou*
     público na UE. É transbordo, não mercado — inútil como magnitude para uma oferta de EUA.
     A FPA tem **zero** anúncios na Alemanha.
   - **Preço no checkout**: atrás de formulário de captura nas três.
   Conclusão operacional: para oferta entregue nos EUA, **não existe caminho público até gasto,
   faturamento ou lucro**. Registrar isso como bloqueio conhecido e parar de reabrir a questão a
   cada rodada; o que a evidência pública sustenta é distribuição (volume, persistência, países).

23. **Copy de retargeting entrega sinal de faixa de preço que a landing esconde.** Os anúncios da
   HighTicket.io para quem abandonou o checkout citam, em texto nativo da Meta, o nome do produto
   (**High Ticket E-Commerce Academy**), uma **garantia** e **financiamento "from zero down"**.
   Oferta que precisa de financiamento parcelado está na faixa de milhares de dólares — é
   qualitativo e vem do próprio vendedor, mas é mais informativo que "preço não confirmado".
   Quando o checkout estiver atrás de captura, **ler a copy de retargeting** antes de desistir.

24. **Eixo emocional: medo de perder o que se tem × desejo de ter outra coisa.** Observação do
   usuário em 20/09/2026, conferida contra as peças capturadas. As três finalistas da R013 vendem
   a mesma saída — deixar de depender do emprego — por portas opostas:
   - **Medo de perda (obsolescência):** só a **Coursiv**. A landing abre com bloco de estatísticas
     de demissão creditadas a PwC, Challenger, Layoffs.fyi e Stanford AI Index — "55K empregos
     perdidos para a IA em 2025", "100K+ demissões", "45K+ vagas de tecnologia cortadas" — e
     resume em "A IA não vai substituir você. Quem usa IA vai." O criativo aperta com
     **"especially if you're over 40"** e "em 2 semanas você saberá mais que 90% dos seus colegas":
     obsolescência + idade + comparação com o par.
   - **Desejo de ganho:** **HighTicket.io** ("A.I. Just Leveled The Playing Field — Now Anyone With
     a Laptop Can Sell...") e **FPA** (royalty recorrente, de casa, sem estoque). Nas duas, a IA é
     **mecanismo**, não ameaça.
   Registrar esse campo por oferta na próxima triagem. A do medo é a que tem 142.745 avaliações no
   Trustpilot e 39 países num único criativo — é hipótese de que a porta do medo escala mais, não
   conclusão: a amostra tem três ofertas.

25. **Ângulo não se lê no título do VAV.** O campo `title` traz o **codinome interno do criativo**
   (`RoyKindleNoInvAI_H3_T7_DIS_001`, `V118_KFebShoot_$600_16x9`) e `description` costuma ser só
   "Learn How - <url>". Para ler ângulo é preciso a **peça** (thumbnail e vídeo) e a **landing**.
   O codinome ainda assim informa: `NoInv` = sem estoque, `KRecurringRoyalties`, `KStayathome`,
   `$600` revelam os eixos que o anunciante testa e como ele nomeia seus próprios ângulos.

26. **Regex de classificação precisa ser validada contra a amostra antes de virar percentual.**
   A primeira tentativa de medir medo × oportunidade devolveu "99% de oportunidade" para a FPA.
   Era falso: o termo `earn` casava dentro de **`Learn`**, presente em toda descrição
   "Learn How - …". Antes de reportar qualquer proporção, imprimir as linhas que casaram e
   conferir na mão. Percentual errado com aparência de medição é pior que nenhum número.

27. **Infoproduto de renda extra escalado nos EUA não vende curso puro — vende curso + software
   proprietário + suporte humano.** As três finalistas repetem a estrutura: HighTicket.io entrega
   material do curso, 6 meses de coaching em grupo, comunidade e a **Supplier HQ Database**;
   FPA entrega treinamento mais o **FictionPub Ai** (módulos Market Intelligence, Story Engine e
   Book Blueprint), exclusivo para alunos, mais coaches nomeados; Coursiv entrega biblioteca de
   cursos, app e **certificado**. O software é a trava que sustenta ticket alto e justifica o
   financiamento parcelado. Ao auditar, perguntar **o que trava o aluno dentro**, não só qual é o
   conteúdo.

## Aprendizados — conserto dos mineradores de YouTube, 20/09/2026

Origem: sessão de conserto após a R012, a pedido do usuário ("tua base tá fraca em YouTube"). Observações do agente.

1. **VAV/TubeSift busca por domínio de destino e devolve o `video_id`.** Contrato do T-067, que já estava no repositório: `mode=search&order=firstseen|lastseen&keyword=<termo>&searchindomain=1&page=N` — sem `country`. Aceita o domínio com TLD, pagina de 50 em 50, e o `keyword` é substring (filtrar o ruído pelo domínio de cada linha). É a rota que fecha `oferta → vídeo YouTube` que o ATC não fecha: `fit4me.io` → 6 vídeos (um com 559 mil views), `hypnosisdownloads.com` → `jVrudNg5ju4` (163 mil views, canal Uncommon Knowledge). Ligado no executor: `collect --source vav --keywords dom1,dom2`.
2. **Busca por título no VAV é inútil para infoproduto**: qualquer termo devolve os clipes de música mais vistos do YouTube. Por canal (`searchinchannelname=1`) rende — `Recipes` trouxe as VSLs de `livercleanseprotocol.com`.
3. **Três buscas emendadas sem pausa devolvem "sem results".** Uma por vez funcionava; o executor com três domínios falhou até entrar `sleep(2)` entre buscas. O erro agora carrega o corpo enviado e a resposta, para não repetir a investigação.
4. **O normalizador colapsa VAV por domínio.** 138 vídeos da Queima Diária viraram 1 oferta no pool; os vídeos individuais só existem no `seed/vav_ads.jsonl` da execução. Para auditar criativos de YouTube, ler a seed, não o pool.
5. **Sessão do VAV morre no servidor com cookie "válido".** `/library/` redireciona para Login e `/a/library` devolve `-1`. `scripts/vav_bootstrap.py` refaz o login com a credencial do env; em 20/09 passou sem CAPTCHA. Quando pedir CAPTCHA, é do operador.
6. **VidTao: o problema nunca foi o cliente, foi o Bearer de 1h.** O SDK do Firebase guarda `refreshToken` no IndexedDB do perfil; um refresh em `securetoken.googleapis.com` renova o accessToken indefinidamente. O perfil salvo em 05/09 estava sem sessão, então falta **um** login do operador (`scripts/vidtao_bootstrap.py`); daí em diante `scripts/vidtao_token.py` renova sozinho. O AisTruct é somente leitura pelo `REPOS.txt`: token e scripts ficam neste repositório e o cliente recebe o caminho por `from_token(path)`.
7. **Deeptube foi a fonte que dava o infoproduto BR pronto** (325 ofertas com ticket, checkout, `qtd_ads`, player e VSL, 100% da base BR de infoproduto em jul/2026) e sumiu inteira com a pasta `~/Desktop/video-ad-vault-skill/`: cliente, credencial e host. Nada disso foi versionado. Lição de infra: cliente de fonte paga tem que morar no repositório e a credencial no env canônico; ferramenta no Desktop é ferramenta perdida.
8. **Antes de escrever coletor, ler `spy/code/scrape` e `spy/findings`.** O contrato de busca do VAV estava no T-067 e o método inteiro no F-028; a sonda por tentativa custou uma hora para chegar onde o grep chegaria em um minuto.
9. **`a/channels` do VAV é descoberta nativa de YouTube.** `POST /a/channels` com `mode=browse&country=<cc>&order=videocount|views&lastseen=<janela>&page=N` devolve 80 canais por página com `channelid`, contagem de vídeos de anúncio, views agregadas e primeira/última vez visto — quem gasta em YouTube aparece aqui sem precisar de domínio vindo da Meta. Ferramenta: `scripts/vav_canais.py`. Na primeira leitura (20/09/2026, 1 mês): BR por volume = Empiricus 2.554, Tiago Tessmann 1.206, WendellCarvalho 1.168; US = V Shred 3.665.
10. **Confirmação por segunda via vale mais que uma fonte a mais.** Os 80 domínios BR de infoproduto deram 0 no ATC e 9/80 no VAV, com um único caso relevante. Duas fontes independentes dizendo "não roda YouTube" fecham a questão; não insistir numa terceira.
11. **O ciclo de descoberta de YouTube fecha dentro do VAV.** `a/channels` (quem roda muito vídeo) → `/a/library` com `mode=search&channelid=<cid>` (anúncios do canal com domínio de destino; Tiago Tessmann → `conversaoextrema.com`, `amaquinaextrema.com`) → `searchindomain` (todos os vídeos do domínio) → funil no browser. Nenhuma etapa depende da Meta ou do ATC. `searchChannelId` não é o campo: devolve lista genérica com HTTP 200 — o teste é contar quantas linhas têm o `channelid` pedido.

## Aprendizados R014 — 20/09/2026

Origem: [R014](rodadas/R014-2026-09-20.md). Observações metodológicas do agente; nenhuma preferência humana nova.

1. **O leaderboard `a/channels` do VAV só entrega a página 1 nesta conta.** Páginas 2+ devolvem `{"status": "-1", "message": ""}` em qualquer ordem (`videocount`, `views`), janela (`1_week`, `1_month`, `3_month`) e país — mesmo com sessão recém-refeita. A R013 registrou 160 canais em duas páginas; não se reproduz. Os 80 do topo são marca, fitness e já mapeados. `vav_canais.py` agora trata página vazia como soluço (retry) e aceita `--start-page`, mas o teto real é o do plano.
2. **A descoberta que rendeu na Meta foi frase de nicho + rolagem real + destinos agrupados por hostname.** `"side hustle"`, `"make money online"`, `"passive income"` e `"work from home"` (ordenadas por impressões, ~100–130 IDs carregados por frase) apontaram She Sells, AI Dropshipping Builder, Wealth Creators, 20-Minute Trader e Booming Bookkeeping. É a porta de descoberta desta rodada, e não depende de minerador.
3. **A frase exata precisa do host completo.** `"shesellsremote.com"` devolve nada; `"masterclass.shesellsremote.com"` devolve ~140. Extrair o hostname do destino e buscar por ele — o domínio raiz não casa quando o anúncio aponta para subdomínio.
4. **Domínio com hífen não carrega na frase exata.** `"muslim-preneur.com"` deixa a página sem cabeçalho e sem "nenhum anúncio"; a busca por token (`keyword_unordered`) devolve ~33. Registrar como leitura por token, não como zero.
5. **O lock do executor pode estar com outra sessão.** Doze coletas de Tyver/Foreplay/Adyntel foram recusadas por "outra coleta em execução"; o processo era um `collect --source adheart` de outra sessão (pid 63684), com termos próprios. Não matar, não apagar lock: declarar a lacuna e seguir por fontes que não usam o lock.
6. **Candidato do ATC por domínio é o que fecha a frente YouTube.** Sondar no ATC os domínios achados na Meta revelou que `20mintrader.com` e `thebookkeepingchallenge.com` rodam ≥1.200 criativos cada de um único anunciante — invisíveis na descoberta por termo (que casa no nome civil) e na página 1 do leaderboard do VAV. Rotina: todo candidato Meta passa por `atc_sonda_dominio.py --max-pages 30` antes de rotular a rede.
7. **Cabeçalho gigante fora do recorte vira registro, não finalista.** `wealthcreationclass.com` teve 1.185 IDs (platô real), 1.185/1.185 no domínio e 539 acima de 60 dias — melhor que a HighTicket.io — e é captação para consultoria financeira. Auditar até o fim, gravar os números no índice como descarte no recorte, e não reauditar.
8. **`n_ads` de fornecedor caiu de novo.** AdHeart: `alilokhandwalaofficial.com` 28, `amzsyndicate.com` 12, `mermcro.com` 15 → **zero** ativos na frase exata. Tyver na R012, AdHeart na R014: o campo é acervo.
9. **Com o leaderboard limitado, o fluxo VAV que rende é o pivô por domínio**, `collect --source vav --keywords dom1,dom2`, para fechar `domínio → video_id` — não descoberta.
10. **Screenshot do painel falha com a janela minimizada e a rolagem por coordenada exige screenshot prévio.** Repetir resolveu sempre. `browser_batch` tem teto de **25 ações**: 20 rolagens + 1 extração cabem.
11. **Sessão do VAV morre em horas e o perfil do Chrome fica travado por zumbi.** O segundo re-login do dia falhou com `TargetClosedError` até matar 9 processos presos em `spy/.vav_profile` e apagar `SingletonLock`. Antes de rerodar o bootstrap, procurar processos com `vav_profile` na linha de comando.

## Aprendizados R015 — 20/09/2026

Origem: [R015](rodadas/R015-2026-09-20.md). Rodada executada em paralelo à R014, por outra sessão
no mesmo repositório. As duas convergiram em vários candidatos de forma independente, o que é
confirmação; mas a R015 achou dois defeitos de medição que atingem a R012, a R013 e a R014.

1. **O token de paginação do ATC estava na chave errada, e isso inflou toda contagem de criativo
   desde a R012.** `SearchCreatives` devolve o token de continuação, e os coletores o reenviavam
   em `payload["9"]`. Com `"9"` a API **devolve a página 1 de novo, indefinidamente**, sempre com
   `tem_mais: true`. Cinco páginas seguidas para `thebookkeepingchallenge.com` trouxeram o mesmo
   primeiro `creative_id` (`CR061337064124`) e zero itens novos das páginas 2 a 5. O mesmo com o
   filtro por anunciante. **O token vai na chave `"4"`**: com ela, a página 2 traz 39 itens novos
   e o total fecha em **79 distintos — exatamente o número do cabeçalho da página do anunciante.**
   Antes da correção, a contagem por RPC nunca batia com a interface; agora bate.
   **Consequência:** `--max-pages 30` produzindo "1.200 criativos" era 30 × os mesmos 40. Ficam
   sem lastro os "≥1.200 criativos" da R013 (Coursiv, FPA Workshop), os "400" da HighTicket.io,
   a lição 1 da R013 ("5 páginas dão 200 e 30 dão 1.200") e a lição 6 da R014 ("≥1.200 criativos
   cada" para `20mintrader.com` e `thebookkeepingchallenge.com`). Números reais medidos em
   20/09/2026 com a chave certa: `thebookkeepingchallenge.com` 79, `20mintrader.com` 73,
   `freedomteamtrade.com` 59, `smartphonefreedomlifestyle.com` 255, `warriortrading.com` 671.
   Corrigido em `scripts/atc_sonda_dominio.py` e `scripts/atc_descoberta.py`.

2. **Buscar na Meta pelo domínio mede atribuição, não tamanho.** `keyword_exact_phrase` com o
   domínio só encontra anúncio cujo **texto** cita a URL. `"viral-strategies.com"` devolve
   cabeçalho 23 e 19 IDs; a busca pela **marca** `Viral VFX` devolve cabeçalho ~1.100, 1.018 IDs
   carregados e **940 com destino em `viral-strategies.com`**. Quase 50× de diferença. O mesmo
   padrão em `facelessreels.com`: 61 pelo domínio contra 325 destinos numa varredura por tema.
   Rotina nova: frase exata para **confirmar atribuição**, busca por marca para **medir tamanho**.

3. **Contagem de qualquer API paginada só vale depois de deduplicar pela chave do item.** Os dois
   defeitos acima foram detectados pelo mesmo sinal barato: totais múltiplos exatos do tamanho da
   página (40, 400, 1.200) e histograma por mês também em múltiplos de 40. Somar `len(batch)` sem
   `set()` de identificador esconde repetição; deduplicar e parar quando a página não traz item
   novo é o mínimo.

4. **O teste de entregável derruba o maior volume da rodada.** `facelessreels.com` teve 325
   destinos numa única varredura e `pagepilot.ai` 182 IDs com 36 acima de 90 dias — os dois são
   **SaaS por assinatura**, fora do recorte. Aplicar o teste de entregável **antes** de investir
   na contagem economiza a rodada inteira.

5. **Preço público existe, e aparece quando a oferta vende direto.** Duas das três finalistas
   expõem checkout sem captura: `viral-strategies.com` a US$ 97 com order bump de US$ 59 e
   garantia de 14 dias, e `warriortrading.com` com tabela pública de US$ 499, US$ 1.999 e
   US$ 2.997 mais um teste de duas semanas por US$ 19. A regra "funil de renda extra escalado nos
   EUA esconde o preço atrás de captura" (lição 17 da R013) vale para funil de evento e de call,
   **não** para oferta de venda direta.

6. **O leaderboard `a/channels` do VAV ignora o filtro `lastseen`.** `1_week` e `1_month` com
   `order=videocount` para os EUA devolveram **as mesmas 80 linhas**, na mesma ordem. O campo que
   decide continua sendo a data `lastseen` **de cada linha**, não o parâmetro da consulta.

7. **Descoberta por nome de canal no VAV rende onde o leaderboard não rende.**
   `vav_coleta.py --in channel` com 15 termos de renda extra devolveu 2.292 anúncios com domínio
   de destino e 123 domínios vivos, entre eles `warriortrading.com`, `smartphonefreedomlifestyle.com`,
   `freedomteamtrade.com` e o trio da FinMC LLC — nenhum deles no top 80 do leaderboard.

8. **`SearchSuggestions` do ATC casa no nome civil do anunciante, não no criativo.** Trinta e um
   termos de renda extra devolveram sobretudo empresas cujo nome contém a palavra ("Freelancer
   International", "SHOP TRADING s.r.o."). Para descobrir oferta, o caminho é domínio → sonda;
   para descobrir domínio, o caminho é VAV ou Meta.

9. **Duas sessões no mesmo repositório disputam a pasta da rodada.** A captura desta rodada e a da
   R014 gravaram na mesma `outputs/.../R014/img` por alguns minutos. Antes de criar a pasta da
   rodada, conferir se outra sessão está ativa; se estiver, tomar o número seguinte e registrar.

10. **Concorrente citando o mesmo nicho não é afiliado — e às vezes é candidato.** Dos 78 IDs
    fora do domínio na varredura do Viral VFX, `contentcreator.com` (44), `motioncreators.co` (17)
    e `unrealforvfx.com` (9) têm produto, domínio e checkout próprios. `motioncreators.co` vende a
    US$ 97 via Stripe e entra na fila de candidatas.


## Preferência explícita do usuário — corte de audiência, 20/09/2026

Fala original, na R015: *"tira da lista todos que tem canal no youtube com mais de 30mil seguidor
e o mesmo para facebook ou instagram"*.

**Regra permanente:** oferta cuja audiência própria passe de **30 mil seguidores ou inscritos em
qualquer uma das três redes** — YouTube, Instagram ou Facebook — sai da lista. Vale para o perfil
da marca e para o perfil pessoal do fundador quando é ele quem assina o anúncio. É a forma
mensurável da preferência de replicabilidade registrada na R003, que até aqui era julgada por
impressão.

**Como medir, e o que deu errado ao medir:**

1. **A Página que anuncia nem sempre é a que o site divulga.** `smartphonefreedomlifestyle.com`
   linka a Página "iPhone Freedom Lifestyle" (3,2 mil), mas quem roda os anúncios é
   `maxtornowofficial` (4,7 mil). O número que vale é o da Página do cartão na Biblioteca de
   Anúncios — extrair o link da Página a partir do resultado da busca.
2. **O canal que roda o anúncio no YouTube costuma ser descartável.** Smartphone Freedom anuncia
   por um canal com 4,36 mil inscritos; o canal pessoal de Max Tornow tem 5,12 mil. O VAV entrega
   o `channel_id` de cada anúncio, e é por ele que se chega ao canal certo — não por busca de nome.
3. **Instagram e Facebook não abrem para `httpx`.** A contagem só aparece com um navegador que
   executa JavaScript; o texto da página traz "X seguidores" e é daí que se lê.
4. **Handle parecido não é a marca.** `@optionpub` no Instagram é uma agência francesa homônima,
   sem relação com `optionpub.com`. Confirmar pela bio e pelo link antes de contar.

**Efeito medido na R015:** o corte eliminou as quatro maiores ofertas da rodada — Viral VFX
(Instagram 558 mil), Warrior Trading (YouTube 2,1 milhões), Booming Bookkeeping (Instagram
75,8 mil) e 20-Minute Trader (Facebook 62 mil) — que eram também as duas únicas com preço e
checkout públicos. **Consequência para as próximas rodadas:** medir a audiência **antes** de
investir na auditoria profunda, junto com o teste de entregável. Descobrir tarde custa a rodada.

## Aprendizados R021 — 21/09/2026 (relacionamento na Europa: 1 finalista, MarekG Media)

Origem: [R021](rodadas/R021-2026-09-21.md). Observações metodológicas do agente; nenhuma preferência humana nova.

1. **A micronovela trocou o hostname de app por domínio aleatório.** `qweasdzxcshop.com` (398 anúncios), `topzxcv.com`
   (182), `huazxc.com` (147), `game.pixelzenivo.com` (136) e `brgbook.com` (479) passavam pelo `DESCARTE_HOST`. O que
   entrega é o **nome da Página** ("Romans Romantiques", "Goodnovel", "Club de Lectura Romántica-8", "Sehnsucht &
   Seiten"). `DESCARTE_PAGINA` no `triar_destinos.py`: descarta quando a maioria dos anúncios vem de Página com nome
   de leitura/drama. Autoteste com as personas das finalistas da R017, que não podem cair.
2. **No AdHeart, o retry depois de 429 é cobrado.** 41 frases custaram 65 buscas. Orçar ~1,5 por frase e não
   relançar lote inteiro depois de falha: retomar da frase que parou.
3. **AdHeart descobre, não mede o piso.** A ErosCode aparece com 57 no AdHeart e tinha 598 na Meta. Candidata achada só
   no AdHeart fica `pendente da contagem por marca`, nunca abaixo nem acima do piso.
4. **Persona com sufixo de profissão** (`Brad Brunelli - Love Coach`) é um molde novo: não é colab (`with <Marca>`) nem
   pessoa comum. Registrar e decidir com o usuário se conta como "coaching com rosto"; até lá, não promove sozinha.
5. **Divórcio, ciúme e signo**, nas quatro línguas, devolvem micronovela em mais de 90% dos anúncios. Como gatilho do
   nicho, só cruzados com frase de funil.
6. **Página-mãe com audiência se esconde atrás das personas.** Na `love-coach.online` as personas tinham 4,3 mil
   seguidores; a Página `Sosrelazioni.it`, que assina 11 dos anúncios e declara o mesmo e-mail, tem **70 mil**. O gate
   AUDIÊNCIA mede **todas** as Páginas do destino — `scripts/adlib_paginas.py --q <marca> --country <cc> --seguidores`.
7. **Busca pelo nome da Página acha o funil irmão.** "Dojrzała Miłość" revelou `odzyskajja.pl` (189 IDs) que nenhuma frase
   de funil mostrava acima de 9; o regulamento amarrou três domínios pelo mesmo NIP. Mesmo produtor = **uma** oferta.
8. **A Polônia tem o padrão; os outros mercados do Leste, não.** PL deu a MarekG Media (ebook a 29,99 zł, Páginas com nome
   de blog); NL, CZ, RO e HU devolveram apps e coaches com rosto. Hipótese para a próxima varredura, não regra.
9. **Cabeçalho de Página agrupada não é ID contado**: "Serena Savelli" = cabeçalho 130, 42 cartões em 7 tentativas.
10. **Um coletor Meta por vez, e `bloqueada=true` encerra o país.** Na R021, 11 de 16 frases voltaram bloqueadas nas saídas
    DE/IT/FR/GB/RO/HU com o proxy vivo; 4 sessões dividiam a mesma conta. Repetir gasta ~11 min e tráfego pago por frase para
    trazer zero. Cooldown medido: ~12 h.

## Aprendizados R019 — 21/09/2026 (renda extra nos EUA pelo método do advertorial com persona)

Origem: [R019](rodadas/R019-2026-09-21.md). Observações metodológicas do agente; nenhuma preferência humana nova foi
inferida e nenhuma avaliação foi criada.

1. **O padrão ErosCode existe em renda extra nos EUA — em um caso, e como lançamento.** `theprofilesystem.com`: 240 IDs,
   240/240 no destino, 6 Páginas-persona (2 a 31 seguidores, "Seguindo 0", "Personal blog"), VSL sem preço. Todos os IDs de
   setembro/2026. É a primeira vez que a anatomia inteira (marca sem rosto + personas + preço escondido) aparece no nicho;
   e é a lição 16 da R013 de novo: cabeçalho com data única é lançamento. Só a 2ª leitura diz se vira escala.
2. **Nos EUA a Página-persona sem audiência é ferramenta de nutra, físico, app, SaaS e afiliado — não de infoproduto.**
   Das 7 operações com ≥ 3 personas acima de 100 IDs: 1 infoproduto, 1 SaaS (FacelessReels, 10 personas), 1 físico (Granny
   Blog, 4), 3 nutra/cosmético, 1 microdrama (Farsun, 15). Quem escala infoproduto de renda extra usa **marca-pessoa +
   webinar** (Ecom Degree, Lux Blueprint, Cardone, Client Ascension, Her Closing Academy). O gate AUDIÊNCIA continua sendo o
   filtro dominante — como na Europa (R016).
3. **Frase de funil em inglês não separa nicho; o que separa é o cruzamento numa frase só.** `take this quiz` (1.238 IDs),
   `answer a few questions` (1.087) e `see if you qualify` (904) entregam portal de quiz, jurídico, saúde e benefício. O que
   achou as candidatas foi `without showing your face` (315 IDs: Profile System, Skilario, Rolecure, FacelessReels),
   `digital products` e `faceless`. `keyword_unordered` é **OU**, não E: "take the quiz side hustle" trouxe cosmético em 1º.
4. **O advertorial de história de dinheiro em primeira pessoa existe nos EUA, mas é afiliado.** `c.thedispatchreview.com`
   (persona "Thomas Jones" → VSL "WiFi Loophole"), `go.makemoredaily.com` ("Kira Marlo", cartão EBT → Surveoo) e
   `globalvisitlog.com` ("Patsy, 58, single-wide" → `/cf/r/`): 10–15 IDs cada, redirecionador no meio. Medir a **oferta-mãe**
   pela frase do produto, não o redirecionador — ficou bloqueado nesta rodada.
5. **O locale do IP de saída muda o formato da data da Ad Library.** Com proxy US: `30 Jun 2026`, sem vírgula; 776/776 IDs
   de `side hustle` vieram sem data. `data_iso` corrigido em `scripts/adlib_coleta.py` (autoteste cobre os três formatos).
   Sintoma barato: `mais_antigo = None` numa coleta grande.
6. **Proxy esgotado não avisa — sondar antes de cada lote.** O 407 TRAFFIC_EXHAUSTED apareceu como `ERR_TIMED_OUT` numa
   landing 40 minutos depois de a Meta ter parado; até lá, 6 coletas rodaram para nada (o coletor as marcou `bloqueada`, o que
   salvou a série). **As duas contas DataImpulse do perfil solaris zeraram no mesmo dia** — o legado `.proxy` e o
   `.bak.proxycheap` também. `GET api.ipify.org` pelo gateway custa 2 s.
7. **Sem proxy, o IP direto já está em 403.** Busca por marca sem proxy: 0 IDs, cabeçalho nulo, 8 tentativas. Não gastar
   tentativas nem tempo de espera — declarar o bloqueio.
8. **Seguidores da Página: contexto novo por Página.** Na mesma sessão da Ad Library a Meta devolve a tela de login com
   `body` vazio; `wait_until="load"` + 7 s num contexto limpo mostra "31 followers • 0 following" e "Page · Community". Dois
   perfis abriram sem a contagem — registrar "não lido", nunca zero.
9. **AdHeart `text_search` em `exact_phrase` não é exato para palavras comuns.** "Profile System" devolveu 998 anúncios de
   micronovela e loja; "make money online" devolveu advertorial de lençol. Conferir a frase na copy antes de contar; e
   `text_search` não casa URL (`theprofilesystem` = 0).
10. **`passive income` trava em 65 IDs sobre cabeçalho 4.400, duas vezes, com e sem `--ordenar`, proxy vivo.** Não é
    bloqueio; causa desconhecida. Registrado como anomalia — não repetir a busca esperando outro resultado.
11. **`quiz.skilario.com` é o molde da Coursiv nascendo:** quiz em web2wave ("web2app funnels builder"), persona "Linda
    Morgan", copy faceless, 14 IDs de setembro. Reobservar; se o inventário subir, é o segundo caso do padrão no nicho.

## Aprendizados R020 — 21/09/2026 (retomada da R019, fechada por bloqueio)

Origem: [R020](rodadas/R020-2026-09-21.md). Observações metodológicas do agente; nenhuma preferência humana nova.

1. **Bloqueio por IP direto: ~12 h de castigo, ~3 buscas completas de janela.** Livre às 15:04 UTC (bloqueado às
   02:26), travado de novo por volta das 15:10. Sem proxy, a janela só serve para remedir a série — nunca para
   descoberta. Corrige a lição 7 da R019 ("não gastar tentativas"): o bloqueio expira, mas volta rápido.
2. **Teste de bloqueio é a busca-controle, não o `curl`.** `curl` deu 403 enquanto o Playwright carregava 128 IDs.
   Controle certo: `side hustle` (cabeçalho conhecido) no mesmo IP; sem cabeçalho e sem "nenhum anúncio" = bloqueio.
3. **Proxy: todas as saídas do projeto são o mesmo gateway DataImpulse** — `.proxy_gateway`, `.bak-r018`, e também
   `PROXY_US`/`PROXY_BR` do perfil solaris. Esgotou um, esgotaram todos.
4. **AdHeart `text_search` em inglês não serve para renda extra:** 10 frases de história × dinheiro, 2.789 anúncios,
   zero infoproduto (micronovela, nutra/físico em primeira pessoa, seguro). E em lote seguido toma `HTTPError` depois da
   1ª frase, sem cobrar — rodar uma por vez com pausa.
5. **MRR nos EUA é pulverizado em revendedoras-pessoa** (Tina Ghazi US$ 17, Digital Jilly, lojas Stan): muitas Páginas,
   cada uma com seu destino — o oposto da anatomia ErosCode.
6. **Proxy renovado não é proxy livre.** A saída US voltou com saldo novo, rendeu 14 coletas e horas depois passou a ser
   bloqueada pela Meta. Regra do operador (21/09): **um coletor Meta por vez no repositório** (4 sessões dividem a conta) e
   **frase `bloqueada=true` encerra a lista até o cooldown (~12 h)** — cada frase morta queima 8 tentativas de tráfego pago.
7. **`TaskStop` não mata o `lote.sh`.** O loop sobreviveu e gravou leituras bloqueadas em paralelo com o lote novo. Encerrar
   pelo PID do `bash lote.sh` e **filtrar pela pasta da rodada** — nunca `*adlib_coleta*` solto, que pega coletor de outra sessão.
8. **O molde Coursiv tem concorrente com persona nos EUA:** JobEscape (`jobescape.me`) serve quiz → assinatura por "Marcus
   Levin" e "Daniel Blake". Primeiro caso de quiz + persona + assinatura de atrito em renda extra/IA nos EUA; frase `learn AI`.

## Aprendizados R022 — 21/09/2026 (renda extra na Europa, advertorial com persona, fechada por bloqueio)

Origem: [R022](rodadas/R022-2026-09-21.md). Observações metodológicas do agente; nenhuma preferência humana nova.

1. **Na Europa, o advertorial de dinheiro com persona é golpe, não infoproduto.** "Santiago"/BrightCraft Pay: 158
   anúncios, 7 personas anglófonas, **uma persona por domínio descartável** (`x29qb.xyz`, `cau0z.top`, `2rmwk.xyz`…),
   todas as datas em 20–21/09, destino = tarefa paga em casa. clearrate.best: "mamma single di Torino", cloaker por
   país, molde de plataforma de investimento. **Sinal de descarte:** mesma copy em vários `.xyz`/`.top` com persona
   diferente em cada um.
2. **O infoproduto europeu de renda extra com quiz é marca-pessoa com uma Página.** NiCe Publishing (Cedric Mattig),
   Erfolgsmethode, Digital Growth Club, Atena: quiz de 60 s + FunnelCockpit/Perspective + preço atrás do quiz — a
   infraestrutura da ErosCode sem a camada de personas. Terceira rodada (R016, R019, R022) sem o padrão ErosCode em
   renda extra. Hipótese: **no nicho de dinheiro, o rosto é o produto**.
3. **AdHeart `exact_phrase` em frases "faceless" e de persona europeias devolve micronovela** (`joyreadland`,
   `lightreader`, `drama.*reel*`, `peakshort`) — ao contrário de `without showing your face` nos EUA (R019).
4. **Três sessões na mesma Meta derrubam as três.** O IP direto aguentou 1 coleta. Listar os `adlib_coleta.py` ativos
   antes de disparar; havendo outro, esperar. A cota do AdHeart também é compartilhada: 230 → 144 em 1h30, 49 desta
   rodada — medir antes e depois e atribuir por sessão.
5. **ATC responde sem proxy para sonda pequena** (4 domínios, região DE, sem `RateLimitError`) via
   `dados/atc_direto.py`, que força `next_proxy -> ""`.
6. **Com proxy, o padrão aparece — no piso, e com um pé em marca-pessoa.** NiCe Publishing (DE): 153 IDs em 13
   Páginas, 11 delas temáticas sem rosto ("KDP Nebenbei Frei", "Der KDP Kompass") com 0–19 seguidores e "seguindo 0",
   mais **subdomínios com sobrenome que são clones do mesmo quiz** — rede de parceiros num funil só. Variante nova
   da anatomia: em vez de Páginas com nome de pessoa, **Páginas com nome de tema**. Adicionar ao checklist: Página
   temática (`<Tema> Erfolgsschmiede`, `Der <Tema> Kompass`, `<Tema> Nebenbei Frei`) com ID `6159…` conta como persona.
7. **A busca pela marca subconta a rede.** `nice-publishing` pela marca: 105 no domínio; `KDP` por palavra achou mais
   48 em `perspectivefunnel.co` das mesmas Páginas. Medir marca **e** mecanismo, e unir por ID.
8. **Um coletor Meta por vez no repositório, por ordem do operador (21/09/2026, 20:10).** Quatro sessões com seis
   Chromium na mesma conta DataImpulse bloquearam DE, IT e US em menos de uma hora de proxy renovado.

9. **`scripts/coleta_inteligente.py` roda o ciclo ao ser importado** (sem guarda `__main__`) e **publica o
   `pool.jsonl` no pod `arasaka-api`**. Nunca importar para usar `quota_restante()`; usar `_adheart_quota.py`.

## Aprendizados R016 — 20/09/2026 (primeiro recorte europeu)

Origem: [R016](rodadas/R016-2026-09-20.md). Observações metodológicas do agente; nenhuma preferência
humana nova foi inferida e nenhuma avaliação foi criada.

1. **Na Europa o Google publica faixa de impressões por criativo — o bloqueio da lição 22 da R013 era
   específico dos Estados Unidos.** `GetCreativeById` devolve, para criativo servido na UE, o bloco
   agregado em `resposta["1"]["19"]`: `"2"`/`"3"` = faixa mínima e máxima de impressões, `"4"`/`"5"` =
   primeira e última exibição em `yyyymmdd`, e `"8"` = a mesma faixa repartida por região. O
   `scripts/atc_paises.py` procurava em `"17"` e em `"4"` e por isso reportava `null` mesmo com o dado
   presente. Ferramenta nova, com autoteste: **`scripts/atc_impressoes_eu.py`**. Medido:
   `goldenvoiceacademy.de` 6.697.000–7.931.000 em 33 criativos; `digitale-safari.de`
   2.604.000–3.031.000 em 26. Continua sem gasto, receita ou lucro — isto é **distribuição**.

2. **A escala europeia é uma ordem de grandeza menor que a americana.** A maior contagem legítima de
   infoproduto de renda extra na Meta foi **201 IDs** (Digitale Safari), contra 767 da HighTicket.io
   (R013) e 940 da Viral VFX (R015). Não transportar o limiar americano: na Europa, centenas de IDs
   com persistência longa é o topo do nicho, não o meio.

3. **O gate AUDIÊNCIA é o filtro dominante no mercado europeu deste nicho.** Nove das doze auditadas
   caíram nele: 13,1 mil (Metapro), 14,3 mil (Unger), 37 mil (PJM), 38,2 mil (KAF), 41,9 mil
   (TradingFreaks), 51,9 mil (Vivir de tu Pasión), 85,7 mil (Cryptory), 173 mil (Learning Heroes) e
   227 mil (The BIG). Hipótese a testar, não conclusão: o infoproduto europeu de renda extra depende
   mais de canal e produtor-rosto que o americano.

4. **O limiar de 10 mil precisa de recalibração, e a R016 dá o caso de teste.** Metapro Academy tem
   13,1 mil inscritos — 31% acima do limiar — e é **marca corporativa sem nenhum rosto**, com 1.468
   criativos de vídeo de um anunciante único desde janeiro/2025. Pelo número está fora; pela intenção
   do critério ("escala paga sem autoridade pessoal") seria a mais forte da rodada. Registrada como
   "escalada com audiência" e destacada para quando o usuário revisar o limiar.

5. **O teste de entregável derrubou as três maiores contagens da rodada.** `nicheur.com` (695 IDs,
   695/695, cabeçalho ~1.800) é dropshipping de acessórios automotivos; `tradingtwins.com` (651 IDs,
   651/651, mais 340 criativos no Google desde 2021) é comparador B2B de cafeteiras e impressoras;
   `lebenskompass.eu` (547 IDs, 544/547, 443 criativos desde ago/2022) é papelaria física. Somadas,
   1.893 IDs que não são infoproduto — e as três vieram de frases legítimas do nicho.

6. **Frase de nicho em alemão mistura oferta com vaga de emprego.** `Nebenjob` (668 IDs) e
   `Quereinsteiger` (638 IDs) devolvem recrutamento — Lidl, Picnic, portais de vaga, agências de
   pessoal. O que devolve oferta é `Nebeneinkommen` (410), `passives Einkommen` (310) e
   `online Geld verdienen` (95). É a armadilha de token da R010 em outra forma: o termo casa, o
   anunciante é outro mercado.

7. **O leaderboard do VAV por país é a porta de entrada fora da Alemanha.** Learning Heroes (ES),
   Metapro Academy (ES), The BIG (ES), Vivir de tu Pasión (ES), Entrepreneurs.com (FR) e Unger
   Academy (IT) só apareceram por ali — nenhum casava com frase de nicho na Meta, e todos têm
   inventário grande no Google. Portugal devolveu **zero** canais vivos na janela de 1 mês.

8. **`SearchSuggestions` do ATC em alemão confirma a lição 8 da R015.** `Nebeneinkommen` e
   `Immobilien Cashflow` devolveram **zero** anunciantes; `Akademie` devolveu 555, quase todos
   instituições de ensino tradicionais (Haufe, IHK, BA). Para descobrir oferta na Europa o caminho
   continua sendo VAV ou Meta → domínio → sonda.

9. **Tyver e Foreplay respondem — primeiro teste de acesso.** A lacuna declarada desde a R013 está
   parcialmente fechada: as duas sessões são válidas. O normalizador do Tyver, porém, grava **IP no
   lugar do domínio** (16 linhas para `57.144.62.1`), o que inviabiliza agrupar por domínio sem
   tratamento. Nenhuma das duas trouxe identidade que a Meta já não tivesse mostrado.

10. **O controle `MANIFESTING REALITY` responde diferente por região.** Sob `platform=YOUTUBE`, ele
    devolve tela vazia na região US (R012) e **1 anúncio** na região DE, contra 24 da Golden Voice e
    81 da Digitale Safari. O controle continua válido — mas o valor esperado é "quase zero", não
    "exatamente zero".

11. **Lançamento europeu tem a mesma assinatura do americano.** `cryptory.de`: 57 IDs, 57/57 no
    domínio, **todos iniciados em setembro/2026**, vida mediana de 2 dias, mais antigo com 16.
    Cabeçalho respeitável, zero persistência. É a lição 16 da R013 confirmada fora dos EUA.

12. **Um escritor por vez, de novo — agora com dano visível.** `reports/intel/pool.jsonl` passou de
    21,5 MB para 72 MB às 18:15 de 20/09 por outra sessão, e carrega **27 linhas quebradas** desde
    12/08/2026 (registros do AdHeart com quebra de linha real no `titulo`). `read_jsonl` aborta e a
    ingestão canônica das finalistas ficou bloqueada. Não corrigido aqui, por ser trabalho de outra
    sessão em voo; cards convertidos e comando registrados na rodada.

## Aprendizados R023 — 21/09/2026 (relacionamento nos EUA, advertorial com persona)

Origem: [R023](rodadas/R023-2026-09-21.md). Observações metodológicas do agente; nenhuma preferência humana nova foi
inferida e nenhuma avaliação foi criada.

1. **A trava da Ad Library tem assinatura legível no corpo da resposta.** A chamada `AdLibrarySearchPaginationQuery`
   responde **HTTP 200** com `{"errors":[{"message":"Rate limit exceeded","code":1675004}]}` — é por isso que a busca para
   em ~27 cartões com cabeçalho de milhares. Ler esse corpo depois de uma rolagem é o teste de bloqueio mais barato
   (substitui a busca-controle da R020 quando se tem o navegador na mão).
2. **IP de datacenter nos EUA não destrava a Meta, mas destrava o Google ATC.** VPS Hostinger (Boston) por `ssh -D 1080`:
   cabeçalho da Meta sim (`side hustle` = 7.400), paginação não (1675004); ATC com sessão NID e controle ok
   (`warriortrading.com` = 80). Ferramenta: `outputs/a58f781b-…/R023/dados/atc_via_vps.py` (troca `next_proxy` por
   `socks5h://127.0.0.1:1080`).
3. **A sessão logada do usuário no Chrome pagina a Ad Library sem proxy** — 24 buscas numa tarde, até 792 cartões numa só.
   Mecânica: a paginação é o **botão "Ver mais"** (rolagem não carrega); a CSP proíbe `eval` e `fetch` para `127.0.0.1`,
   então o coletor é colado inteiro a cada navegação; o retorno da ferramenta corta em ~1.000 caracteres, então os IDs saem
   agrupados por `data.página.caminho` (`chrome/*.txt` → `pack2json.py` → formato do `adlib_coleta`). A URL é reescrita com
   `is_targeted_country=false` e ordenação por impressões, e **inativos aparecem**: filtrar por "Veiculação iniciada em".
   É a conta pessoal do usuário — usar com moderação e declarar a fonte na série (`proxy: chrome_logado`); a 2ª leitura
   tem de usar o mesmo método.
4. **Feitiço é serviço, mesmo com a forma exata do alvo.** Zodiac Love Spell tinha tudo — quiz de signo, persona, carta de
   vendas, ClickBank, 192 IDs — e o FAQ diz *"your spell will be cast within 24-72 hours"*. Ler o FAQ/entrega antes de
   contar; é a lição 10 da R012 (Psychic Samira) em forma de infoproduto.
5. **Nos EUA, neste nicho, a persona escala feitiço e objeto; o infoproduto com persona fica abaixo de 150.** Romance
   Secrets 192+77, Lunar Spell ~170, Held & Honest 164 (diário físico) × PairGrow 113, Angelical 138 (1 persona), Solspace
   35 de relacionamento. Hipótese, não conclusão: uma leitura só.
6. **Molde de slug amarra operação** como o e-mail do perfil: `zlsvr-…-cb`, `ztft-…-cb`, `glsec-fe-tsl-cb-v2` →
   Romance Secrets. E **copy espelhada entre gêneros** denuncia persona nova de operação já mapeada
   (`yourconnectguide.com` "…didn't bring **her** back" × Muses "…didn't bring **him** back").
7. **Frases EN do nicho:** renderam oferta `relationship quiz`, `why he pulls away`, `make him obsessed`, `his zodiac sign`,
   `attachment style`, `make him miss you`; vêm tomadas por micronovela/spell caster `get him back`, `get your ex back`,
   `sexless marriage`, `love spell`, `lost interest`, `wife doesn't want`; `after divorce` = advogados.
8. **`splitlines()` de novo**: o agrupador do AdHeart abortou em `JSONDecodeError` pela mesma razão da R017 (U+2028 nas
   copies). Em JSONL do projeto, sempre `split("\n")`.
9. **Três sessões, numeração em corrida**: esta rodada nasceu R021 e foi entregue como R023. Conferir `rodadas/` também
   **na entrega**, e gravar a série só depois de fixar o número (aqui foi corrigido à mão em 2 linhas).

## Aprendizados R024 — 22/09/2026 (renda extra, rede única YouTube, Europa: 2 finalistas e 1 lacuna)

Origem: [R024](rodadas/R024-2026-09-22.md), primeira rodada do GOAL-RENDA-EXTRA-YOUTUBE. Observações metodológicas do agente;
nenhuma preferência humana nova foi inferida e nenhuma avaliação foi criada.

1. **Canal pequeno não prova falta de audiência: olhar quem aparece no vídeo.** A RETSINNAL GROUP (Andorra) roda 19 vídeos não
   listados, até 1,55 M de views cada, por dois canais "Entiende la Bolsa" com 41 e 78 inscritos. O homem do vídeo é Enrique
   Moris (144 mil, verificado), rosto da Tradeando, do mesmo grupo. É a Página-persona da Meta transposta para o YouTube, com o
   produtor-rosto dentro do criativo. O gate AUDIÊNCIA no YouTube tem três leituras: canal do vídeo, canal do produtor e **rosto
   do vídeo** (abrir o vídeo e comparar com o canal do produtor).
2. **A raiz do domínio pode ser outra oferta.** `amz-masterclass-exclusiva.com` na raiz vende finanças pessoais a 297/497/997 €
   ("3.200 alunos"); o subdomínio `empieza.` do anúncio vende trading com mesa proprietária ("75.000 alunos"). Abrir o destino
   **exato** do anúncio, nunca só a raiz.
3. **O filtro `published` do browse do VAV funciona e corta o acervo antigo.** `published=3_month` devolveu só vídeos de jun–set.
   `vav_coleta.py` fixava `published=any`; o browse livre está em `R024/dados/vav_browse.py` (variáveis `PUB` e `P0`).
4. **O browse do VAV pagina até a página 10 por views**, mas por estreia (`firstseen`) para em 2 páginas (100 vídeos). O
   leaderboard `a/channels` continua só com a página 1 e só marca.
5. **Busca por TLD não funciona no VAV** (`.it`, `.de` = 0): o ponto parece ignorado. Buscar por palavra do domínio.
6. **O canal genérico "Video ad upload channel for <conta>" é canal sem audiência por construção**, criado pelo Google Ads.
   Buscado por nome, trouxe 550 vídeos, quase todos de marca; mas é por ele que a Traders Business School anuncia, com o canal
   próprio de 23,6 mil fora do anúncio. Registrar os dois canais.
7. **A sessão do VAV cai depois de ~45 buscas seguidas**, e o `vav_bootstrap.py` falhou três vezes seguidas com `Connection
   closed while reading from the driver`. O mesmo login sem `--start-maximized`/`no_viewport` (`R024/dados/vav_login_diag.py`)
   passou na 1ª tentativa. Rodar lotes de até ~12 termos.
8. **A página do canal traz o número de outros canais.** O 1º `"N subscribers"` do HTML de `youtube.com/channel/<id>` é de canal
   em destaque (TradersClub24 saiu 829 em vez de 8,08 mil). O número do canal está em `metadataParts…content`. O
   `subscriberCountText` da página do **vídeo** vem em rótulo por extenso ("1.76 thousand subscribers"): tratado no `_num`.
9. **Contador de views do YouTube pode parar entre leituras próximas.** `cuqOCdObehg` ficou em 780.022 em duas leituras com ~1,5 h
   de intervalo, enquanto o VAV já mostrava 780.938. Intervalo < 24 h não é repetição; o subcomando `youtube` avisa.
10. **Piso provisório, primeira calibração.** Oito ofertas passaram "não listado, ≤ 90 d, ≥ 100 mil" na Europa; seis caíram em
    gate de audiência ou entregável. O piso de views não é o filtro que decide aqui: o de audiência é. TradersClub24 passa por
    margem pequena (102 e 121 mil), Goat Money com folga (2,6 M em 53 d). Se o usuário quiser mais finalistas europeias, o botão
    a rever é o limiar de 10 mil (TBS 23,6 mil, Metapro 13,1 mil: marcas sem rosto), não o de views.
11. **Rosto como apresentador × marca-pessoa.** As duas finalistas têm um rosto na peça (Orso Locatelli na Goat Money, Carlos
    Martins no TradersClub24), com marca, canal e domínio sem o nome dele e audiência abaixo de 10 mil em todas as redes. Fica
    registrado como ressalva, para o usuário decidir se "sem rosto" exige ausência de apresentador.
12. **ATC fora dos EUA: faixa UE com cobertura baixa.** 1 de 15 criativos da Goat Money (IT) e 4 de 13 do TradersClub24 (DE)
    trouxeram faixa. `atc_impressoes_eu.py --region` exige código numérico (IT = 2380, DE = 2276), não sigla.
13. **Duas lições da 2ª passada.** (a) O campo `_country` do registro do VAV vem da busca (padrão `br` na busca por termo), não do
    país onde o anúncio rodou: para dizer "Europa" usar `countries` do registro e o ATC da região — The Empath Closing School passou
    no filtro frouxo e era JP/TH/CR. (b) Depois de ~5 re-logins no mesmo dia, o VAV passou a redirecionar para `/verify/`: tratar
    como bloqueio do operador e parar, sem novas tentativas de login. A tela de verificação avisa que automação e raspagem violam
    os Termos de Uso do VAV: o volume de buscas por sessão é risco para a conta, não só para a sessão.
14. **O ATC entrega o `video_id` do YouTube — corrige a lição da R013 ("ATC sem video_id").** O criativo em vídeo traz, em
    `SearchCreatives`, a URL `displayads-formats…/ads/preview/content.js`; o JS dessa prévia contém o id do vídeo (`ytimg.com/vi/<id>`).
    Validado em Goat Money (`Ns8biAlvtC8`, `fyVqj9SlE50`) e TradersClub24 (`BxQ9Rpnhpbc`, igual ao do VAV). Ferramenta:
    `scripts/atc_videos.py` (`videos --advertiser … --region …` e `descobrir`), com autoteste. É a rota de vídeo que não depende
    do VAV. **Limite medido:** a descoberta continua presa ao SearchSuggestions (nome civil): 85 anunciantes em IT, DE, ES, FR, UK, NL, PL e PT
    com 6–30 termos por região deram escolas tradicionais, comparadores e acervo antigo — zero candidata de renda extra. Serve para fechar
    anunciante → vídeo, não para descobrir.
