# Prompt de busca — ofertas de ADVERTORIAL com persona, em escala

> **Execução pelo MCP:** use este Goal como critério; monte o texto a ativar pelo
> [modelo atual](../meu/goals/GOAL-EXEMPLO.md), sem colar a versão curta abaixo.
> Antes de ativar, siga [o pré-voo](../docs/goal-preflight.md).
> Defina a rede com a pessoa; Meta é a frente principal deste método e YouTube
> só entra se estiver no recorte aprovado. Depois da aprovação, chame
> `planejar_fontes(rede, pais, alvo)` e siga [o mapa atual](../docs/fontes.md)
> para registrar os dez mineradores como usados, condicionais ou fora da rede.
> Comandos locais e listas de fontes abaixo são registros do laboratório.

> Especialização do prompt padrão do operador, criada em 20/09/2026 a partir do exemplo que o
> usuário mandou (`myavellis.com`) e do que a varredura dele revelou. Para outro recorte, usar o padrão.
> A preferência que originou este arquivo está em [CRITERIOS.md](CRITERIOS.md), seção
> "ESCALA MAIOR E ÂNGULO DE ADVERTORIAL".

O `/goal` aceita no máximo **4.000 caracteres**. A **versão curta** é o que se cola; o **procedimento
completo** fica aqui e o agente lê no início da rodada.

---

## Versão curta — copiar isto depois de `/goal`

> **Corrigida em 20/09/2026 pela R017:** a linha BUSCA não exigia proxy, e sem proxy a Meta devolve
> 403 desenhado como "nenhum anúncio encontrado". Detalhe e medição em
> [CRITERIOS.md](CRITERIOS.md#correções-de-método-medidas--20092026-r017-a-biblioteca-de-anúncios-mente-por-omissão).

```
Encontrar e auditar as ofertas de ADVERTORIAL EM PRIMEIRA PESSOA mais escaladas do recorte declarado no fim deste prompt (REGIÃO e NICHO) e entregar 3 finalistas NOVAS, com pelo menos 150 IDs ativos cada.

PARÂMETROS. REGIÃO ou NICHO vazios nas duas últimas linhas: fazer UMA pergunta pedindo os dois e não buscar nada antes da resposta.

O PADRÃO. Anúncio que não parece anúncio: história em primeira pessoa, persona com nome e profissão, número clínico concreto, antes/depois, "meu médico disse". Várias Páginas-persona (médico, paciente, diário) apontando para o MESMO destino. Página sem seguidor, criada para anunciar. Referência (20/09/2026): haferloewe.de 504 IDs, gesundgelesen.com 258, gentilia.it 162 (3 personas), myavellis.com 132 (2 personas, site cloakeado).

Trabalhar em D:/Projetos/Spy X. Antes de buscar, ler projeto/treinamento/GOAL-ADVERTORIAL.md (procedimento completo), CRITERIOS.md inteiro, OFERTAS-MAPEADAS.md, README.md do treinamento e as três últimas rodadas.

EXCLUSÃO. Cruzar /meus (solaris, paginação completa), favoritas, utilizadas e OFERTAS-MAPEADAS. Excluir por identidade: nome, aliases, produtor, domínio, produto, entregável. Persona nova da mesma operação NÃO é oferta nova: conferir o destino.

BUSCA. scripts/adlib_coleta.py --proxy auto SEMPRE. Medido na R017: sem proxy, a partir de ~40 buscas a Meta devolve HTTP 403 DESENHADO como "No ads match your search criteria" — sem erro visivel — e toda busca trava em ~28 cartoes de forma intermitente. Com proxy, --ordenar e --country ALL funcionam normalmente; nao culpar os parametros, conferir o status HTTP. A frase CLINICA entrega nutra; a frase de FUNIL entrega infoproduto ("personalisierten Plan", "piano personalizzato", "plan personalizado"). Rodar 8+ frases por idioma, agrupar por hostname e so entao medir.

ESCALA. REGRA PRIMORDIAL: contagem tirada UMA vez e INVENTARIO, nao escala — na R017 a mesma busca devolveu 28 ou 598 IDs conforme o IP. Escrever 'escalada' exige DUAS leituras separadas por >=24h, mesmo metodo, status HTTP conferido, gravadas com scripts/escala_serie.py. Uma leitura so: escrever 'inventario medido' e declarar 'escala: pendente de segunda leitura'. Atribuicao (598/598 no destino) e persistencia (idade, mediana, fracao acima de 30 e 90 dias) valem com uma leitura; tamanho nao.

PERSONAS. Contar Páginas anunciantes distintas por destino e classificar cada uma: médico, paciente, diário, marca. Três ou mais personas para um destino é a assinatura do padrão. Medir seguidores de cada Página: persona de anúncio tem quase zero, e isso é o alvo, não defeito. Marca-pessoa com audiência real continua fora.

INTENSIDADE. Novos em 7 e 30 dias, vida mediana, idade do mais antigo, fração acima de 90 dias, início por mês. Referência: haferloewe 193 novos em 7 dias, mediana 13 dias. Datas todas na mesma semana é lançamento.

ENTREGÁVEL. Neste recorte SUPLEMENTO E NUTRA ENTRAM, ao contrário do GOAL padrão — são a referência de ângulo. Infoproduto com o mesmo ângulo é preferível: registrar os dois separados. Fora: serviço e SaaS.

CLOAKER. Site que devolve "Access Denied"/Blockify a visita direta é SINAL, não obstáculo: registrar a tecnologia e seguir pela copy e pelo cabeçalho. Não tentar burlar, não comprar.

DINHEIRO. Gasto, receita e ROAS não são observáveis. Na UE, medir o que é público: faixa de impressões do Google por criativo (scripts/atc_impressoes_eu.py) e alcance por país na transparência da UE da Meta. Persistência e Trustpilot como ordem de grandeza.

FONTES. Meta Ad Library é a principal: este padrão é nativo de Meta. ATC por domínio para checar se há YouTube. AdHeart por collect --execute com --market do recorte e --last-active 1, cota conferida. VAV só se houver vídeo. arasaka.py doctor no início; registrar a situação de cada fonte.

QUANTIDADE. Triar ≥15 destinos e auditar ≥6 a fundo. Lacuna declarada vale mais que finalista fraca.

ENTREGA. Próxima rodada, sem sobrescrever. Excel padrão R003, um PDF por finalista, dossiê consolidado com placar, página de personas e página sobre dinheiro, linha de WhatsApp por oferta sem enviar, cobertura das fontes. PDFs em PNG e revisar. Finalistas no acervo pela ingestão canônica. Atualizar OFERTAS-MAPEADAS, README, CRITERIOS e o índice; reabrir e conferir. Não inventar avaliação, favorita, uso ou sincronização.

PARADA. Só terminar com 3 novas qualificadas acima do piso e registros persistidos, ou com bloqueio documentado.

REGIÃO:
NICHO:
```

Preencher na última linha: `REGIÃO: Itália, Alemanha` · `NICHO: glicemia e diabetes`. Vale nicho amplo
(`NICHO: qualquer saúde`), desde que declarado — vazio pergunta.

---

## Procedimento completo — lido pelo agente no início da rodada

### O que é este padrão, medido

O exemplo do usuário é `myavellis.com`: **Cannella di Ceylon em softgel de óleo MCT**, vendida na Itália.
O anúncio é um texto longo em primeira pessoa assinado por "Francesca Martini" — enfermeira de
diabetologia com 22 anos de carreira que teria saído da metformina e levado a hemoglobina glicada de 8,2
para 5,9. O site responde **Access Denied** (Blockify) a visita direta. Nada nele parece publicidade: nem
o formato, nem o autor, nem a página.

Os quatro marcadores do padrão, todos observáveis sem login:

1. **Copy de história** — primeira pessoa, linha do tempo ("Dia 1…", "Oito meses depois"), número clínico
   concreto, objeção respondida no título ("Posso tomar junto com a metformina?").
2. **Páginas-persona** — o mesmo destino recebe tráfego de várias Páginas com nome de pessoa e papel
   distinto. `gentilia.it`: "Dott. Fabrizio Galli — Endocrinologo" (53 IDs), "Lucia Casali" (50) e
   "Il Diario della Glicemia" (49). `myavellis.com`: "Alessandra Rossi" (86) e "Francesca Martini" (38).
3. **Escala de centenas** — `haferloewe.de` tem **504 IDs** ativos, `gesundgelesen.com` **258**.
4. **Infraestrutura de suporte** — subdomínio de teste (`test.haferloewe.de`, 39 IDs), quiz
   (`zuckerquiz.haferloewe.de`), **typo-domain** (`haferloeve.de`, 6 IDs) e portal de conteúdo próprio
   (`gesundgelesen.com` é um site inteiro de "testes independentes").

### A busca que mede — e a que engana

`scripts/adlib_coleta.py` aceita `--country ALL` (que adiciona `is_targeted_country=false`) e `--ordenar`
(`sort_data[mode]=total_impressions&sort_data[direction]=desc`), os parâmetros que o usuário passou.

**Medido em 20/09/2026:** a busca por **domínio ou marca trava em ~30 cartões**, com e sem ordenação —
`myavellis.com` devolveu 30 de um cabeçalho de 170, `Gentilia` 29 de 180, `glycowohl` 30 de 77. A busca
pela **frase clínica da copy** não trava: `emoglobina glicata` carregou **402 IDs** e revelou
`gentilia.it` com 162 e `myavellis.com` com **132** — quatro vezes o que a busca pelo domínio mostrava.
`Blutzucker` carregou 659 IDs sobre um cabeçalho de 5.200.

> ⚠️ **Corrigido em 20/09/2026 pela [R017](rodadas/R017-2026-09-20.md), com medição.** O travamento em
> ~30 cartões descrito acima **não vem dos parâmetros**: vem de **bloqueio por IP**. A partir de ~40
> buscas a Meta responde **HTTP 403 e desenha "No ads match your search criteria"**, sem erro visível.
> Com `--proxy auto` (o mesmo pool que o ATC já usava): `emoglobina glicata` trouxe **384 IDs de um
> cabeçalho de 380**, `eroscode` **com `--ordenar`** trouxe **598 de 600**, e `musesacademy` com
> **`--country ALL`** trouxe 488. Rotina corrigida: **sempre com proxy**, e conferir o status HTTP
> antes de acreditar num platô. E a frase **clínica** entrega nutra; para achar infoproduto, usar a
> frase de **funil** (`personalisierten Plan`, `piano personalizzato`, `plan personalizado`,
> `plan personnalisé`, `persoonlijk plan`, `spersonalizowany plan`).

**Rotina:** frase da copy para descobrir e medir → domínio para confirmar atribuição → marca para achar
as personas. Nunca o contrário.

Sementes de frase por idioma (ampliar conforme o nicho do recorte):

| Idioma | Frases que renderam |
|---|---|
| IT | `emoglobina glicata`, `la mia glicemia`, `il mio medico`, `Metformina` |
| DE | `Blutzucker`, `mein Arzt`, `Blutzuckerspiegel`, `Zuckerwerte` |
| ES | `mi médico`, `azúcar en sangre`, `hemoglobina glicosilada` |
| FR | `ma glycémie`, `mon médecin`, `hémoglobine glyquée` |
| EN | `my A1c`, `my doctor told me`, `blood sugar` |

**As frases acima entregam nutra.** Para o infoproduto agressivo (R017: ErosCode, Muses Academy, Céleste
Valmont), a chave é a **frase de funil** — a promessa de resultado personalizado em troca de responder
perguntas:

| Idioma | Frase de funil que rendeu |
|---|---|
| DE | **`personalisierten Plan`**, `persönlichen Plan`, **`Mach den Test`**, `60-Sekunden-Check` |
| IT | **`piano personalizzato`**, **`Fai il test`** |
| ES | **`plan personalizado`**, **`Haz el test`** |
| FR | `plan personnalisé`, `Faites le test` |

E o que reconhece a oferta antes de abrir a página: hostname `quiz.*`, ≥ 3 Páginas com nome de pessoa e
audiência zero, e-mail da marca no perfil da persona, preço escondido atrás do quiz. A anatomia completa,
com os sinais de descarte (app, micronovela, físico) está em
[CRITERIOS.md — ASSINATURAS DO ADVERTORIAL AGRESSIVO](CRITERIOS.md#assinaturas-do-advertorial-agressivo--o-que-essas-ofertas-têm-de-único-e-como-reconhecer-em-segundos),
e o detector executável é `scripts/triar_destinos.py <pasta de dados>`.

Termo muito amplo (`mein Arzt`, `mi médico`, cabeçalhos de 8 a 50 mil) trava cedo no carregamento:
subir `--plato` e `--max-rodadas`, e preferir a frase específica do nicho.

### Gate de escala

Piso de **150 IDs ativos** para virar finalista — calibrado pelas referências acima, e não pelo padrão
europeu de infoproduto da R016 (49 a 201 IDs), que o usuário considerou fraco. Contar por ID, deduplicar,
extrair o hostname de destino de cada um e somar os subdomínios e typo-domains do mesmo funil, declarando
cada um em separado. Abrir todo destino aparentemente alheio antes de contá-lo contra.

### Gate de personas — o que substitui o gate AUDIÊNCIA neste recorte

O gate AUDIÊNCIA de 20/09/2026 procura marca sem seguidor em escala. **Este padrão é a forma extrema
disso:** a Página anunciante não tem audiência porque foi criada para o anúncio. Então:

- Contar Páginas anunciantes distintas por destino e classificar o papel de cada uma (médico, paciente,
  diário, marca). **Três ou mais personas para um destino** é a assinatura.
- Medir seguidores de cada Página. Número baixo aqui **confirma** o padrão.
- O que continua eliminando: marca-pessoa com audiência real (produtor conhecido, canal grande),
  porque aí a venda se apoia na autoridade e não na estrutura.

### Entregável — a exceção declarada

O GOAL padrão manda excluir suplemento. **Neste recorte o suplemento entra**, porque é onde o ângulo vive
e porque foi o exemplo que o usuário escolheu. Regras:

- Registrar sempre o que é: suplemento, alimento funcional, dispositivo, infoproduto.
- **Infoproduto com este mesmo ângulo é preferível** — se aparecer, promover na frente do nutra e
  registrar a diferença.
- Continuam fora: serviço e SaaS.

### Cloaker

Site que devolve "Access Denied", Blockify, ou uma página branca para visita direta está cloakeado. Isso
é **sinal de operação agressiva**, e entra na ficha como evidência. Registrar a tecnologia detectada e
seguir medindo pela copy do anúncio, pelo cabeçalho da biblioteca e pelas personas. **Não** tentar burlar
o filtro, **não** usar proxy para se passar por tráfego pago, **não** comprar o produto.

### Dinheiro

Gasto, faturamento e ROAS continuam inobserváveis. O que a Europa dá, e deve ser medido sempre:

- **Faixa de impressões do Google** por criativo — `scripts/atc_impressoes_eu.py`, campo
  `resposta["1"]["19"]` do `GetCreativeById`. Vem preenchido na UE e nulo nos EUA (R016).
- **Transparência da UE na Meta** — alcance por país no card do anúncio. Para oferta entregue na UE isso
  é mercado real, não transbordo (diferente do caso americano da R013).
- Trustpilot e contagem de clientes declarada na própria página, sempre marcadas como alegação do
  vendedor (`haferloewe.de` declara 103.048 clientes; `gentilia.it`, 9.300 avaliações).

### Fontes

Meta Ad Library é a fonte principal — este padrão é **nativo de Meta**. O ATC entra para responder se a
oferta também roda no Google/YouTube (e para a faixa de impressões). AdHeart ajuda a achar a persona e o
`page_name`, que a Ad Library não devolve na listagem: `collect --source adheart --market it|de|es|fr
--last-active 1 --execute`, com a cota conferida antes e depois. VAV só quando houver vídeo.

### Quantidade e entrega

Triar no mínimo **15 destinos** e auditar a fundo no mínimo **6**. Entrega igual à da R016: Excel padrão
R003, um PDF por finalista, dossiê consolidado — com uma **página de personas** a mais, mostrando quem
anuncia para cada destino — linha de WhatsApp por oferta, quadro de cobertura das fontes, PDFs
renderizados em PNG e revisados página a página, finalistas no acervo pela ingestão canônica e
OFERTAS-MAPEADAS, README, CRITERIOS e índice atualizados e reconferidos.

### Parada

Só terminar com 3 novas acima do piso de 150 IDs e registros persistidos, ou com bloqueio concreto
documentado. Busca vazia não encerra.
