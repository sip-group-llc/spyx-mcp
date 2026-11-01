# Prompt de busca — RELACIONAMENTO em formato de advertorial com persona, em escala

> **Execução pelo MCP:** use este Goal como critério; monte o texto a ativar pelo
> [modelo atual](../meu/goals/GOAL-EXEMPLO.md), sem colar a versão curta abaixo.
> Antes de ativar, siga [o pré-voo](../docs/goal-preflight.md).
> Defina a rede com a pessoa; Meta é a frente principal deste método e YouTube
> só entra se estiver no recorte aprovado. Depois da aprovação, chame
> `planejar_fontes(rede, pais, alvo)` e siga [o mapa atual](../docs/fontes.md)
> para registrar os dez mineradores como usados, condicionais ou fora da rede.
> Comandos locais e listas de fontes abaixo são registros do laboratório.

> Criado em **21/09/2026** a pedido do usuário. É o recorte onde o método do
> [GOAL-ADVERTORIAL](GOAL-ADVERTORIAL.md) mais rendeu até agora: **as três finalistas da R017 são de
> relacionamento** (ErosCode, Muses Academy, Céleste Valmont), aprovadas como "boa" pelo usuário. Este
> GOAL parte delas — as frases que as acharam, as personas que elas usam, e o que no nicho parece oferta
> e não é. Regras gerais em [CRITERIOS.md](CRITERIOS.md) (REGRA PRIMORDIAL e ASSINATURAS primeiro).

O `/goal` aceita no máximo **4.000 caracteres**. A **versão curta** é o que se cola; o **procedimento
completo** fica aqui e o agente lê no início da rodada.

---

## Versão curta — copiar isto depois de `/goal` (3990 caracteres)

```
Encontrar e auditar as ofertas de RELACIONAMENTO em formato de ADVERTORIAL COM PERSONA mais escaladas da REGIÃO declarada no fim e entregar 3 finalistas NOVAS, SEM AUDIÊNCIA PRÓPRIA, com ≥150 IDs ativos cada.

PARÂMETRO. REGIÃO vazia: UMA pergunta, nada de busca antes. NICHO fixo: relacionamento — reconquista, intimidade no casamento, atração, astrologia aplicada ao casal, comunicação/ciúme, divórcio. Sexualidade só com entregável digital.

O PADRÃO, JÁ MEDIDO NESTE NICHO (R017): quiz.eroscode.de 598 IDs/5 personas (homens 30+, 59 € único); quiz.musesacademy.io 541/8 (mulheres, assinatura, 1 ano no Google); celestevalmont.com 446/7 (astrologia, uma persona por idioma, 240 >30d). Marca sem rosto, Páginas com nome de pessoa e 1–350 seguidores, quiz como porta, preço atrás do quiz. É isso, em operações NOVAS.

Trabalhar em D:/Projetos/Spy X. Antes de buscar, ler GOAL-RELACIONAMENTO.md (procedimento completo), CRITERIOS.md inteiro, OFERTAS-MAPEADAS.md, README.md e R017–R018.

EXCLUSÃO. Cruzar /meus (solaris), favoritas, utilizadas e OFERTAS-MAPEADAS por identidade (nome, aliases, produtor, domínio, produto, entregável). Persona nova da mesma operação NÃO é oferta nova: conferir destino e e-mail do perfil. Já mapeadas: ErosCode, Muses Academy, Céleste Valmont, ilsegretodellariconquista, Liebesschicksal, Couples Therapy workbooks, BetterMe Relationship, nuclever.fr, protocolodelreconquista.

BUSCA. scripts/adlib_coleta.py --proxy auto SEMPRE, por país (sem proxy a Meta devolve 403 desenhado como "No ads match your search criteria"; contagem zero se confere contra o status). Gatilho do nicho cruzado com frase de FUNIL: DE "dass er zurückkommt", "meine Ehe", "Weibliches Verlangen", "Mach den Test"; IT "il tuo ex", "riconquistare", "mio marito", "Fai il test"; ES "recuperar a tu ex", "tu relación", "Haz el test"; FR "récupérer mon ex", "ta relation", "Faites le test"; EN "get him back", "make him obsessed", "why he pulls away", "take the quiz". Signo ("il suo segno", "son signe") acha o veio Céleste mas vem tomado por micronovela: triar antes. 8+ frases por idioma; agrupar por hostname; scripts/triar_destinos.py <pasta> antes de contar por marca; achou em DE, conferir AT e CH.

ENTREGÁVEL ANTES DA CONTAGEM. Abrir a landing antes da busca por marca. Fora: micronovela/microdrama (w2a./fb./drama./read./novel/reel — a maior contaminação do nicho), app de namoro/casal, nutra de disfunção erétil, físico (sex toy, joia), coaching com rosto, consultório local.

PERSONAS. ≥3 Páginas no mesmo destino, nome de pessoa sem "with <Marca>" e sem número; ou uma persona por idioma com o mesmo nome traduzido. Medir seguidores (1–350 é o alvo, "Blog pessoal", "Seguindo 0"). E-mail da marca no perfil amarra. Marca-pessoa ou ≥10 mil: registrar, não promover.

ESCALA (REGRA PRIMORDIAL). Contagem única é INVENTÁRIO. "Escalada" exige DUAS leituras ≥24h, mesmo método, gravadas com scripts/escala_serie.py (D+0 na entrega). Atribuição (IDs no destino/total) e persistência (mais antigo, mediana, >30d, >90d, início por mês) valem com uma leitura; tamanho não. Sem ATC não distinguir lançamento de rotatividade.

DINHEIRO. Gasto/ROAS inobserváveis. Preço só se público; termos de assinatura dizem o modelo; quiz que termina em e-mail = captura, não preencher. UE: atc_impressoes_eu.py.

FONTES. Meta principal; ATC por domínio (proxy da região); AdHeart só text_search via adheart_frases.py, cota conferida; VAV só com vídeo. doctor no início; registrar cada fonte.

QUANTIDADE. Triar ≥15 destinos, auditar ≥6. Lacuna declarada vale mais que finalista fraca.

ENTREGA. Próxima rodada, sem sobrescrever. Excel padrão R003, PDF por finalista, dossiê com placar, personas e dinheiro; PDFs em PNG revisados; ingestão canônica; D+0 na série; OFERTAS-MAPEADAS, README, CRITERIOS e índice atualizados e reconferidos. WhatsApp: prévia direto aos dados, sem saudação, enviar só com ok.

PARADA. 3 novas acima do piso com registros persistidos, ou bloqueio documentado.

REGIÃO:
```

Preencher a última linha: `REGIÃO: Europa` · `REGIÃO: EUA` · `REGIÃO: DE, AT, CH` · `REGIÃO: IT, ES, FR`.
Vazio pergunta.

---

## Procedimento completo — lido pelo agente no início da rodada

### Por que este é o recorte mais maduro da base

| Finalista (R017) | Sub-nicho | IDs | Personas | O que ensinou |
|---|---|---|---|---|
| **ErosCode** `quiz.eroscode.de` | intimidade no casamento, homens 30+ | 598 | 5 | preço público (59 € único), 4 Páginas com o e-mail da marca no perfil, curva jul 59 → ago 245 → set 294 |
| **Muses Academy** `quiz.musesacademy.io` | atração / "high-value woman", mulheres | 541 | 8 | nomes anglófonos servindo 5 idiomas; assinatura de atrito; **1 ano no Google com 4 dias de mediana na Meta** |
| **Céleste Valmont** `celestevalmont.com` | astrologia aplicada ao casal | 446 | 7 | uma persona por idioma com o mesmo nome traduzido; a mais persistente (240 > 30 d) |

E o que ficou abaixo do piso mas confirma o veio: `ilsegretodellariconquista.online` (60 IDs, 1 persona,
**82 dias, 37 > 30 d** — persistente e pequeno), `nuclever.fr` (42, 4 personas), `quiz.innerflo.me`
(70, mas app), `protocolodelreconquista.shop` (34), `getmyrelations.com` (15), `recuperaex.com` (11).

### Sub-nichos e o gatilho de cada um

| Sub-nicho | Gatilho na copy | Público | Exemplo medido |
|---|---|---|---|
| **Reconquista** | "ele foi embora", "5 erros que todas cometem", "sem contato" | mulheres 25–45 | Muses, Céleste, ilsegretodellariconquista |
| **Intimidade no casamento** | "ela não me quer mais", "gatilhos biológicos", "7 dias" | homens 30–55 | ErosCode |
| **Atração / "high-value"** | "faça ele ficar obcecado", "torne-se a mulher que ele não larga" | mulheres | Muses |
| **Astrologia aplicada** | "entenda o homem de Leão", "compatibilidade por signo" | mulheres | Céleste |
| **Comunicação e ciúme** | "reduzir conflitos", "sem cobranças" | casais | ilsegretodellariconquista (aula gratuita) |
| **Divórcio / recomeço** | "depois dos 40", "recomeçar" | ambos | ainda não medido |

### Sementes de frase por idioma — as que renderam e as que enganam

| Idioma | Gatilho do nicho (rendeu) | Funil (cruzar) | Engana |
|---|---|---|---|
| DE | `dass er zurückkommt`, `meine Ehe`, `meine Beziehung`, `Weibliches Verlangen`, `Ex zurück` | `Mach den Test`, `personalisierten Plan`, `60-Sekunden-Check` | `Sternzeichen` sozinho (micronovela + astro-shop) |
| IT | `il tuo ex`, `riconquistare`, `mio marito`, `la tua relazione`, `Quando un uomo si allontana` | `Fai il test`, `piano personalizzato` | `il suo segno` (GoodNovel/BuenNovela) |
| ES | `recuperar a tu ex`, `mi ex`, `tu relación`, `mi marido` | `Haz el test`, `plan personalizado` | `su signo` (novela), `mi marido` puro traz nutra |
| FR | `récupérer mon ex`, `ta relation`, `mon mari`, `Quand un homme prend ses distances` | `Faites le test`, `plan personnalisé` | `son signe` (ReelShort) |
| EN | `get him back`, `make him obsessed`, `why he pulls away`, `high-value woman` | `take the quiz`, `see if he`, `find out why` | `high-value woman` no AdHeart vem 90% micronovela |

Lição da R018: **as frases de signo e "high-value" estão tomadas por apps de micronovela** — dos 48
destinos acima de 20 linhas no AdHeart, a maioria era GoodNovel, BuenNovela, ReelShort, DramaBox. Rodar
`triar_destinos.py` antes de olhar qualquer contagem; o hostname já descarta (`w2a.`, `fb.`, `drama.`,
`read.`, `novel`, `reel`).

### O que neste nicho parece oferta e não é

| Parece | É | Sinal para descartar sem abrir |
|---|---|---|
| "história de amor em primeira pessoa" com 20 Páginas | **app de micronovela/microdrama** | hostname `w2a.`/`fb.`/`drama.`/`read.`/`h5.`, nomes de Página numerados (`Drama Shorts-03`) |
| "encontre o par ideal" | **app de namoro** (SaaS) | `play.google`, `itunes`, "download" |
| "seu casamento em 7 dias" com persona médica | **nutra de disfunção erétil** | copy de "Dr. med.", "Facharzt für Urologie" (elvantera-tipo); no recorte fora de nutra, sai |
| "presente que salva a relação" | **físico** (joia, sex toy, travesseiro) | "Versand", "frete grátis", "Discreet Packaging" |
| "terapia de casal" | **consultório local / serviço** | endereço, "Praxis", agenda, 1 Página, 300+ dias |
| "coach de relacionamento" com 40 mil seguidores | **marca-pessoa** | gate AUDIÊNCIA — registrar, não promover |

### Triagem, na ordem que economiza coleta

1. Coletar por gatilho do nicho **e** por frase de funil, por país, com `--proxy auto`.
2. `scripts/triar_destinos.py <pasta>` — quiz no host, ≥ 3 Páginas, nome de pessoa, frase de funil, sem
   peça de descarte. Micronovela sai aqui.
3. Para ≥ 3 pontos: **abrir a landing** e testar o entregável (tabela acima). Só depois, busca por marca.
4. Busca por marca → hostname de cada ID → personas com seguidores → e-mail no perfil.
5. Achou em DE, conferir **AT e CH**; achou em FR, **BE e CH**; achou em ES, **MX e AR** só como
   registro (fora da região).
6. ATC por domínio: frente Google e idade real da operação.
7. `scripts/escala_serie.py registrar` — D+0 na entrega; segunda leitura em 24 h libera "escalada".

### Gates, resumidos

- **Entregável:** programa/curso digital, relatório por quiz, assinatura de conteúdo. Fora: app, SaaS,
  serviço, físico, nutra, marca-pessoa.
- **Personas:** ≥ 3 Páginas no mesmo destino **ou** uma por idioma com o mesmo nome traduzido; 1–350
  seguidores; e-mail da marca no perfil amarra.
- **Audiência:** marca-pessoa ou ≥ 10 mil → registrar, não promover.
- **Escala (REGRA PRIMORDIAL):** piso 150 IDs no mesmo destino; uma leitura = inventário.
- **Intensidade:** novos 7/30 d, mediana, mais antigo, > 30 e > 90 d, início por mês; cruzar com o ATC.

### Fontes, entrega e parada

Iguais ao GOAL-ADVERTORIAL: Meta com proxy (principal), ATC por domínio, AdHeart só `text_search`
(`adheart_frases.py`), VAV só com vídeo, `doctor` no início. Excel padrão R003, PDF por finalista,
dossiê com placar/personas/dinheiro, PNGs revisados, ingestão canônica, D+0 na série, índices
atualizados, prévia de WhatsApp direto aos dados e envio só com ok. Parada: 3 novas acima do piso com
registro persistido, ou bloqueio documentado.
