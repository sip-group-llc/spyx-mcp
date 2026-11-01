# Laboratório de mineração com feedback

Memória operacional persistente do Spy X. Antes de cada rodada, o agente lê este
arquivo, [critérios e lições](CRITERIOS.md), [métricas](METRICAS.md), o histórico
`avaliacoes.jsonl` e a última rodada. Isso orienta a busca nas próximas conversas
neste projeto; não altera os pesos do modelo de linguagem.

## Ciclo por prompt

1. **Preparar:** ler preferências explícitas e avaliações anteriores; declarar hipótese,
   rede, mercado pretendido, termos, limites e a mudança em relação à rodada anterior.
2. **Minerar:** consultar acervo atual; coletar dentro do orçamento autorizado; preservar
   recibos e observações originais em `spy/data/`. Meta e Google/YouTube têm o mesmo peso.
   Nenhum minerador contratado cobre YouTube (R012): para essa frente, minerar o ATC direto
   com `scripts/atc_descoberta.py` e `scripts/atc_sonda_dominio.py`, seguindo o
   [fluxo da skill](../../plugins/arasaka/skills/arasaka-ops/references/escala.md#frente-googleyoutube-minerar-o-atc-direto).
   Contar o **destino** de cada ID na Meta (188/188 no domínio separa escala real de
   correspondência por token) e reconferir todo `ad_volume` de fornecedor na biblioteca pública.
3. **Revisar:** seguir a quantidade solicitada; no plano atual, buscar pelo menos 15
   anúncios, distribuídos 8/7 entre redes, alternando a rede com oito a cada rodada.
   Vaga sem candidato qualificado fica como lacuna, sem preencher com anúncio fraco.
   Distinguir anúncio, página, domínio e oferta; não somar suas contagens.
   **Antes de concluir sobre escala, sempre acessar a biblioteca pública e validar a
   oferta específica**, registrando contagens, datas, filtros, distribuição disponível
   e contraevidências. Atividade isolada não basta. Sem revisão ou dados suficientes,
   marcar validação pendente/escala indeterminada. Ver correção pós-E001 em CRITERIOS.md.
4. **Ouvir:** o usuário pode dizer “R001-A boa pelo mecanismo; R001-B ruim pelo produto”.
   Registrar suas palavras, data, ID e boa/ruim/incerta. Motivo não informado fica `null`.
   Minha hipótese não preenche sua avaliação. R003 já tem oito avaliações importadas da planilha.
5. **Refinar:** extrair padrões de positivos e negativos; mostrar o que mudou e quais
   avaliações sustentam a alteração. Um exemplo gera hipótese, não regra universal.
6. **Medir:** comparar rodadas por rede e mercado; repetir observações dos finalistas
   em D+3, D+7 e D+14 quando houver execução solicitada. Não existe agendamento aqui.

> ⚠️ **REGRA PRIMORDIAL, gravada em 20/09/2026 a pedido do usuário e acima de todo o resto:**
> **escala é o que sobrevive à repetição da medida.** Contagem tirada uma vez é **inventário**; só
> vira *indício de escala* com **duas leituras separadas no tempo**, mesmo método, status HTTP
> conferido. Texto completo em
> [CRITERIOS.md](CRITERIOS.md#regra-primordial--escala-é-o-que-sobrevive-à-repetição-da-medida);
> série em [`serie-escala.jsonl`](serie-escala.jsonl), alimentada por
> [`scripts/escala_serie.py`](../../scripts/escala_serie.py). O que a obrigou: na R017 a mesma busca
> devolveu **28 ou 598 IDs** conforme o IP, porque a Meta responde 403 desenhado como "nenhum
> anúncio encontrado".

Antes de encerrar cada varredura, cumprir a [regra de navegação e planilha](CRITERIOS.md#navegação-e-planilha-obrigatórias--usuário-19092026):
revisar anúncio → biblioteca → página da oferta, fundamentar a conclusão de escala
e entregar Excel visual com previews, links e evidências. Acesso insuficiente mantém
a validação pendente; a planilha deve mostrar essa lacuna.

## Arquivos e contratos

- [Ofertas favoritas](../ofertas-favoritas/README.md): arquivo das aprovações explícitas,
  com pacote de entrega e evidências; primeira entrada: Reverse Health (R005-01).

- [CRITERIOS.md](CRITERIOS.md): preferências confirmadas, hipóteses e lições com origem.
- [METRICAS.md](METRICAS.md): campos obrigatórios e limites de interpretação.
- [Rodada R001](rodadas/R001-2026-09-17.md): teste real e fichas para calibrar o gosto.
- [Rodada R002](rodadas/R002-2026-09-17.md): dez buscas, oito candidatos Meta,
  lacuna Google e revisão audiovisual pendente; entrega parcial por limites da rodada.
- [Rodada R003](rodadas/R003-2026-09-17.md): oito candidatos após filtro de
  seis meses (três Google/YouTube e cinco Meta, cinco ofertas). Sete retirados por
  recência; histórico dos 15 e oito transcrições preservado. Zero buscas pagas novas.
- [Rodada R004](rodadas/R004-2026-09-19.md): oito fontes coletadas com recibo,
  validação pública Meta e Google, três finalistas comprovados e quatro falsos positivos
  ou casos sem escala atual descartados. Spy.House e VAV ficaram bloqueados por sessão.
- [Rodada R005](rodadas/R005-2026-09-19.md): varredura mundial com validação
  pública estrita; Reverse Health confirmada com 135 anúncios ativos iniciados antes
  do corte de sete dias.
- [Rodada R006 — corrigida](rodadas/R006-2026-09-19.md): primeira seleção de Maria Wendt; contagens de grupos invalidadas pela R007.
- [Rodada R007 — reauditoria, repetida na lista](rodadas/R007-2026-09-19.md): Maria Wendt já estava na lista do usuário; não atende ao pedido de oferta adicional. Preservada como correção metodológica.
- [Rodada R008](rodadas/R008-2026-09-19.md): ReciMe, ausente das listas verificadas; 403 IDs ativos, 131 antigos sem grupo, 35 perfis e alcance UE de 366.563 em um ID. Entrega comprovada em Alemanha, Áustria e França. Aguarda aprovação; fora das favoritas.
- [Índice canônico de ofertas mapeadas](OFERTAS-MAPEADAS.md): exclusão por identidade entre rodadas, com estados separados de aprovação e uso.
- [Rodada R009 — última](rodadas/R009-2026-09-19.md): prosperidade + Digistore24 + EUA. Nenhuma candidata comprovou os três requisitos; Midas foi a melhor parcial, com checkout DS24 ativo, zero anúncios ativos pelo domínio exato e rota principal atual em ClickBank. Bloqueio documentado, sem favorita.
- [Rodada R010 — última](rodadas/R010-2026-09-20.md): varredura ampla nos EUA, sem nicho ou gateway fixos. BetterMe Mental Health foi entregue como a mais forte entre as auditadas: ~870–880 resultados no domínio específico, 148 IDs carregados e 140 iniciados há mais de sete dias. WalkFit, Yoga-Go, Muscle Booster, Aura, Luvly, Dancebit, Beyond Body, Horse Boost e Lasta foram comparadas; nenhuma aprovação ou favorita foi inferida.
- [Rodada R011 — última](rodadas/R011-2026-09-20.md): recorte de renda extra. Somente Get Paid With Instagram / Maria Wendt passou pelo gate: ~80 resultados ativos na frase exata no filtro US, com persistência desde junho/julho e histórico R007 de 215 IDs, 153 >7 dias. PDF individual revisado; as demais candidatas não foram rotuladas como escaladas.
- [Rodada R012 — última](rodadas/R012-2026-09-20.md): infoprodutos com peso igual entre redes.
  Três finalistas novas: **fit4me.io / FitMe Military** (Meta, ~6.800–7.100 ativos US, 188 IDs, 130 >7 dias,
  188/188 destinos no domínio), **The Family Freezer / Freezer Meal Pro** (Meta, ~630 ativos, 163 IDs,
  30 >7 dias, checkout US$ 97 confirmado) e **HypnosisDownloads.com** (Google/YouTube, ~200 no filtro
  YouTube do ATC, vídeo confirmado, seis países informados pela plataforma, preço e garantia confirmados).
  Dois falsos positivos de fornecedor documentados. VAV, Deeptube, VidTao e Spy.House indisponíveis;
  a frente Google/YouTube foi minerada direto no ATC. Nenhuma favorita ou avaliação foi inferida.
- [Rodada R013 — última](rodadas/R013-2026-09-20.md): recorte de renda extra nos Estados Unidos.
  Três finalistas novas, com as duas redes cobertas: **HighTicket.io / Brook Hiddink** (Meta,
  **767 IDs** carregados, **759/767 no funil da oferta**, 52 >7 dias, 705 nascidos em setembro),
  **Coursiv** (Google/YouTube, ~20 mil no filtro YouTube do ATC, **≥1.200 criativos** de um único
  anunciante, 149 vídeos no VAV com 98 estreados em 7 dias, série desde 29/07/2024, **zero na Meta
  US**) e **FPA Workshop / Fiction Profits Academy** (as duas redes: ≥1.200 criativos no ATC,
  **152/152 IDs no domínio** na Meta e um vídeo com **1.581 dias no ar**). 17 identidades triadas,
  6 auditadas a fundo. **Três assinaturas de escala distintas** — velocidade, fábrica de criativo e
  longevidade — e a lição de que o platô da Ad Library é impaciência, não limite da plataforma.
  O caminho de descoberta foi o leaderboard `a/channels` do VAV, sem insumo da Meta. Tyver, Foreplay,
  Adyntel, Anstrex e Trendtrack não foram consultadas — lacuna declarada; VidTao sem token.
  Nenhuma favorita ou avaliação foi inferida.
- [Rodada R014 — última](rodadas/R014-2026-09-20.md): segunda rodada de renda extra nos EUA.
  Três finalistas novas: **She Sells / Shelby Sapp** (Meta, ~140 no funil e ~270 na marca, 125/125 no domínio,
  73 >60 dias, oito meses contínuos), **20-Minute Trader / JR Advance LLC** (YouTube, ≥1.200 criativos 100% vídeo
  desde abr/2025; VAV 50 vídeos, o mais antigo há 590 dias; preços US$ 997 / 197 por mês / 2.997 na página) e
  **Booming Bookkeeping Business** (YouTube + Meta, ≥1.200 desde jan/2025, vídeo de 37 M de views há 926 dias).
  Wealth Creators (1.185 IDs) auditada e descartada por ser consultoria financeira. A descoberta que rendeu foi a
  Meta por frase de nicho com destinos agrupados; o leaderboard do VAV só entrega a página 1 nesta conta.
- [Rodada R015 — última](rodadas/R015-2026-09-20.md): terceira rodada de renda extra nos EUA, executada
  **em paralelo à R014** por outra sessão do mesmo repositório. Três finalistas novas: **Viral VFX /
  viral-strategies.com** (Meta, 940 de 1.018 IDs no domínio, 242 acima de 90 dias, **US$ 97 com checkout
  público**), **Smartphone Freedom Lifestyle / Max Tornow** (Google + Meta, 255 criativos e 83 anúncios) e
  **Warrior Trading / Ross Cameron** (YouTube, **671 criativos**, 328 acima de 90 dias, o mais longevo com
  **715 dias**, preços públicos de US$ 499 a US$ 2.997). Duas correções de método: o **token de paginação do
  ATC ia na chave errada** e inflava toda contagem de criativo desde a R012 — a contagem corrigida bate com o
  cabeçalho da interface; e a **busca por domínio na Meta mede atribuição, não tamanho** — pela marca,
  `viral-strategies.com` vai de 19 para 940. `facelessreels.com` e `pagepilot.ai`, os dois maiores volumes da
  rodada, foram descartados por serem SaaS.
- [Rodada R016 — última](rodadas/R016-2026-09-20.md): **primeira rodada do recorte europeu** de renda extra
  (DE, GB, ES, IT, FR, NL, AT, CH, PL, PT). Três finalistas novas, as duas redes cobertas, **todas aprovadas no
  gate AUDIÊNCIA**: **Digitale Safari** (Meta 201/205 no funil, 91 acima de 90 dias, mais antigo com 367 dias;
  Google 45 criativos e 81 anúncios sob o filtro YouTube), **Golden Voice Academy** (Meta 74 no funil, 52 acima de
  90 dias, mais antigo com **492 dias**; Google 36 criativos com **6,70–7,93 milhões de impressões** e um vídeo pago
  com 3,2 M de views) e **brandyourvoice** (49 IDs, 49/49 no domínio, Página com **579 seguidores** — o exemplo
  positivo que o gate procurava desde a R014). Achado de método: **na Europa o Google publica faixa de impressões
  por criativo**, em `resposta["1"]["19"]` do `GetCreativeById` — o bloqueio da lição 22 da R013 era específico dos
  EUA. Ferramenta nova: `scripts/atc_impressoes_eu.py`. O gate AUDIÊNCIA derrubou **nove das doze** auditadas,
  entre elas PJM Investment Akademie (2.086 criativos, 37 mil seguidores) e Entrepreneurs.com (3.379 criativos,
  fora do recorte). As **três maiores contagens da rodada** — nicheur.com (695 IDs), tradingtwins (651) e
  Lebenskompass (547) — caíram no teste de entregável. Tyver e Foreplay tiveram o acesso testado pela primeira vez.
- [Rodada R017 — última](rodadas/R017-2026-09-20.md): **primeira rodada do recorte de advertorial com
  persona**, na Europa, com o nutra fora do entregável por pedido do usuário ("tudo menos nutra").
  Três finalistas novas, todas infoproduto digital e todas com a assinatura do padrão: **ErosCode**
  (`quiz.eroscode.de`, 598 IDs, 598/598 no destino, 5 Páginas-persona de 1 a 168 seguidores, quatro
  delas declarando `support@eroscode.de`; 59 € pagamento único), **Muses Academy**
  (`quiz.musesacademy.io`, 541 IDs, 8 personas anglófonas servindo copy em cinco línguas; mediana de
  4 dias na Meta mas **100 criativos no Google desde 11/09/2025**) e **Céleste Valmont**
  (`celestevalmont.com`, 446 IDs, 7 personas — uma por idioma —, mediana 39 dias, 240 acima de 30).
  2.093 destinos triados, 9 auditados a fundo. As **três maiores contagens da rodada caíram no teste de
  entregável**: `interview.lovi.care` (1.192 IDs, app + físico), `glaubensweg.com` (282, livro impresso)
  e `wholehumancollective.app` (234, doação). Achado de método principal: a Meta responde **HTTP 403 desenhado
  como "No ads match your search criteria"**, sem erro visível, e trava toda busca em ~28 cartões —
  resolvido com `--proxy auto`, que também desfez a suspeita de que `--ordenar` e `country=ALL` fossem
  a causa; a frase que acha infoproduto é a de **funil**
  (`personalisierten Plan`), não a clínica; no AdHeart, `link_search` e `domain` são ignorados em
  silêncio. **Pendência da R016 fechada:** o `pool.jsonl` nunca esteve corrompido — `read_jsonl` usava
  `splitlines()`, que quebra em ` `; corrigido, e as três finalistas entraram pela ingestão
  canônica. Nenhuma avaliação ou favorita foi inferida.
- [Rodada R018 — última](rodadas/R018-2026-09-21.md): segunda varredura do mesmo recorte da R017,
  **fechada com bloqueio documentado e ZERO finalistas**. O único candidato acima do piso —
  `thepsychology.online` / **Innerly**, com **323 IDs e 11 Páginas-persona, uma por idioma** — caiu no
  teste de entregável: é **app de bem-estar por assinatura** (funnelfox.io, anunciante Mindly Apps Ltd),
  o mesmo motivo que derrubou Yoga-Go, BetterMe e Lovi. Lição contra o próprio agente: a contagem foi
  feita **antes** de abrir a página de destino, quebrando a regra da R015. Dois bloqueios em sequência:
  o proxy do projeto esgotou o saldo (**407 TRAFFIC_EXHAUSTED**, disfarçado de `ERR_TIMED_OUT`, matou 11
  de 18 coletas) e a Meta voltou a responder **HTTP 403** mesmo pelo gateway novo. Correção de ferramenta
  mais importante: o coletor agora marca `bloqueada` e o `escala_serie.py` **recusa** gravar leitura
  bloqueada — sem isso, um 403 viraria "a oferta encolheu para zero" na série. `title_search` é o
  **quarto** filtro do AdHeart que mente. Pendência: `learndemandskills.com` (15 personas, cabeçalho 830)
  ficou sem medida final.
- [Rodada R019](rodadas/R019-2026-09-21.md): **primeira rodada de renda extra nos EUA pelo método do
  advertorial com persona** (GOAL-RENDA-EXTRA reescrito em 21/09). Fechada com **1 candidata acima do piso e bloqueio
  documentado, zero finalistas**. A candidata é **The Profile System** (`theprofilesystem.com`): **240 IDs, 240/240 no
  destino, 6 Páginas-persona de 2 a 31 seguidores** ("Ashley Harlows" em variações, "Boss Bae Community"), escola online
  de Instagram sem mostrar o rosto — a anatomia da ErosCode em renda extra, **mas todo o inventário nasceu em setembro**
  (mediana 4 dias, zero acima de 30): lançamento, D+0 gravado, decisão na 2ª leitura. 22 coletas por frase e 6 por marca
  na Meta (~16.700 IDs), 20 frases no AdHeart (18.348 anúncios), 437 destinos triados, 31 landings abertas antes de
  qualquer contagem. Achado sobre o mercado: nos EUA a Página-persona sem audiência serve **nutra, físico, app, SaaS e
  afiliado** (FacelessReels 392/10 personas, Granny Blog 166/4, mykalm/alevia 148/13); infoproduto de renda extra que escala
  é marca-pessoa + webinar. Bloqueio: o proxy DataImpulse esgotou nas **duas** contas (407 TRAFFIC_EXHAUSTED) e, sem proxy,
  a Meta bloqueia o IP direto (403) — 6 frases e a busca por marca do "WiFi Loophole" ficaram sem medida. Correções de
  ferramenta: `data_iso` lê `30 Jun 2026` (locale do IP de saída); `triar_destinos.py` reconhece a frase de funil em inglês.
  Nenhuma avaliação ou favorita foi inferida.
- [Rodada R020 — última](rodadas/R020-2026-09-21.md): retomada da R019 (renda extra, EUA, advertorial com persona). **0 finalistas.** 14 coletas Meta válidas (6.840 IDs, 42 destinos ≥ 20) em duas janelas — IP direto e proxy renovado — até a saída US ser bloqueada e o operador encerrar a coleta. Melhor achada: **JobEscape** (`jobescape.me`, quiz → assinatura de cursos de IA, 2 personas, 108 IDs, 124 dias) abaixo do piso e sem busca por marca. Annetta Powell subiu para 598 IDs (marca-pessoa, lançamento). AdHeart: 2.789 anúncios, zero útil. 2ª leitura da série liberada a partir de 22/09 05:42 UTC.
- [Rodada R021](rodadas/R021-2026-09-21.md): **relacionamento na Europa** (19 mercados) pelo GOAL-RELACIONAMENTO. **1 finalista e 2 lacunas declaradas.** Fase 1 com a Meta bloqueada (proxy 407, IP 403) rodou 56 frases no AdHeart; com o proxy renovado, 131 frases e 29 buscas por marca na Meta; uma 2ª varredura para as vagas 2 e 3 (PL a fundo, SK, HR, GR, BG, LT e as candidatas nunca medidas pela marca) não achou nenhuma — PairGrow (121 em ALL) é a mais perto, a reobservar. Finalista: **MarekG Media** (Polônia) — ebooks de reconquista e casamento a 29,99 zł, **`magiaprzyciagania.pl` 216 IDs (216/216, 55 > 90 d) e `odzyskajja.pl` 189 (189/189, mais antigo 528 d)**, 6 Páginas com nome de blog de 197 a 3,4 mil seguidores, zero no Google; D+0 gravado. Saíram: `love-coach.online` (141 IDs, Página-mãe com **70 mil** seguidores) e `mon-plan-coeur.fr` (95 > 30 d, coaching com rosto). Ferramentas: `scripts/adlib_paginas.py` (seguidores por Página), `triar_adheart.py`, `DESCARTE_PAGINA` para micronovela em domínio aleatório.
- [Rodada R022](rodadas/R022-2026-09-21.md): renda extra na **Europa** (DE, IT, ES, FR, GB), advertorial com persona. **0 finalistas; 1 candidata no piso — NiCe Publishing** (KDP por quiz de 60 s, 153/153 IDs, 13 Páginas, temáticas com 0–19 seguidores, curva jul 7 → ago 31 → set 115; D+0 na série). Fase 1 bloqueada (proxy 407, IP direto); fase 2 com proxy renovado: 31 leituras válidas até o operador encerrar as coletas (4 sessões numa conta). FR parcial e GB = lacuna. AdHeart 16.551 anúncios em 49 frases, 1.821 destinos, 29 landings. Achado: na Europa a persona com copy de dinheiro é **golpe** (BrightCraft Pay, 158 anúncios/7 personas em domínios `.xyz`/`.top`; clearrate.best); o infoproduto com quiz é **marca-pessoa com 1 Página** (NiCe Publishing/KDP, a reabrir). Numeração: R021 ficou com outra sessão.
- [Rodada R023](rodadas/R023-2026-09-21.md): **relacionamento nos EUA** pelo GOAL-RELACIONAMENTO. **0 finalistas, lacuna declarada.** Com o proxy em 407 e o IP direto em castigo, a Meta foi lida pelo **Chrome logado do usuário** (24 buscas, ~4.300 cartões; paginação pelo botão "Ver mais") — a VPS dos EUA carrega o cabeçalho mas a paginação volta `Rate limit exceeded` (1675004). Única operação acima do piso: **Zodiac Love Spell / Romance Secrets** (192 IDs, 192/192, 2 personas, tudo de setembro) — **serviço de feitiço** de US$ 27 no ClickBank, fora no gate de entregável. Melhor anatomia: **PairGrow** (quiz + personas Victoria Caldwell 77 seg. e Lucas Bennett 9 + assinatura, TIPRO UAB/Junixis LLC) com **113 IDs, abaixo do piso**; D+0 das duas na série. Mercado: nos EUA a persona escala **feitiço** (ClickBank) e **objeto** (Held & Honest, diário, 164 IDs); o infoproduto com persona fica abaixo de 150. Numeração: R021 e R022 ficaram com outras sessões.
- [Rodada R024 — última](rodadas/R024-2026-09-22.md): **renda extra na Europa, rede única YouTube** — primeira rodada do GOAL-RENDA-EXTRA-YOUTUBE (Meta fora). **2 finalistas; 3ª vaga = lacuna + bloqueio (VAV exige verificação `/verify/` do operador).** R024-01 **Goat Money** (IT, day trading por seminário; vídeo não listado com 2,61 M views em 53 d; canal 2,49 mil, IG 8.345; ATC ~3 mil desde 04/2025) e R024-02 **TradersClub24** (DACH, workshop → clube com software próprio; 121 e 102 mil em 39 d; canal 8,08 mil; Trustpilot 826). Seis operações passaram o piso de views e caíram em gate — a RETSINNAL (AMZ Masterclass) esconde o rosto de Enrique Moris (144 mil) atrás de canais de 41 e 78 inscritos. 13.473 registros VAV, 116 vídeos pelo gate, 15 ofertas auditadas e 85 anunciantes ATC em 8 países; D+0 de 15 vídeos; `escala_serie.py youtube` e `atc_videos.py` (ATC → video_id, sem VAV) novos. Nenhuma avaliação inferida.
- `avaliacoes.jsonl`: eventos humanos; oito avaliações R003 (cinco boas, três ruins), importadas de Comparativo!Z7:AA14 em 17/09/2026. Acrescentar, não sobrescrever.

Cada evento deve conter `id_evento`, `rodada`, `candidato_id`, `avaliado_em` (ISO com
fuso), `autor: usuario`, `avaliacao` (boa/ruim/incerta), `motivo`, `fala_original`,
`referencia_conversa` e `substitui_evento` (null ou ID corrigido). Antes de acrescentar,
conferir que o candidato existe e que o evento não foi registrado. Correção cria novo
evento apontando para o anterior; a visão atual usa o último, preservando o histórico.
Não guardar segredos nem resultados financeiros privados em documentação versionável.

O feedback deste laboratório é local. Uma gravação no ranking hospedado deve seguir
o contrato de `/julgar`, com identidade e chave exatas; registrar separadamente se foi
sincronizada. Nunca afirmar que feedback local já treinou o ranking da dashboard.

## Próxima rodada

**Atualização de 22/09/2026 — R024 (renda extra, YouTube, Europa):** (0) **destravar o VAV**: o login redireciona para `/verify/` desde 22/09 ~06:10 UTC — só o operador conclui; (1) **2ª leitura de views a partir de 23/09 06:00 UTC** com `escala_serie.py youtube` (comandos na rodada) — Goat Money, TradersClub24 e as registradas AMZ, Gottlebe e TBS; é o que libera "indícios de escala"; (2) o gate AUDIÊNCIA no YouTube inclui **o rosto do vídeo**, não só o canal; (3) o VAV derruba a sessão em ~45 buscas — lotes de até 12 termos e, se o bootstrap falhar, o login de `R024/dados/vav_login_diag.py`; (4) decisão pendente do usuário: apresentador com rosto em marca sem nome de pessoa conta como "sem rosto"? E o limiar de 10 mil vale para marca corporativa sem rosto (TBS 23,6 mil, Metapro 13,1 mil)?

**Atualização de 21/09/2026 — R023 (relacionamento, EUA):** (1) **2ª leitura de `pairgrow.com` e `zodiaclovespell.com` a partir de 22/09 17:05 UTC, SÓ quando o operador liberar a Meta (um coletor por vez no repositório; frase `bloqueada=true` encerra a lista por ~12 h), no MESMO método** (Chrome logado, busca por marca, "Ver mais" até estabilizar, pacote → `pack2json.py` → `escala_serie.py registrar`); PairGrow acima de 150 com a curva subindo vira candidata. (2) Teste de bloqueio mais barato: ler o corpo da `AdLibrarySearchPaginationQuery` — `Rate limit exceeded` (1675004) com HTTP 200. (3) Google ATC sem proxy: túnel `ssh -D 1080` na VPS + `outputs/a58f781b-…/R023/dados/atc_via_vps.py`. (4) Feitiço é serviço: ler o FAQ ("cast within 24-72 hours") antes de contar.

**Atualização de 21/09/2026 — R022 (Europa):** antes de qualquer coleta na Meta sem proxy, **listar os `adlib_coleta.py` ativos** — com outra sessão na Meta, não disparar. Fila pronta e retomável: `outputs/c2816d65-…/R022/dados/lote_meta.py` (43 frases DE/IT/ES/FR/GB). Primeira medida a fazer com a Meta de volta: busca pela marca `nice-publishing` (DE) e seguidores das Páginas "Cedric Mattig KDP"/"KDP Cedric Matting".

**Atualização de 21/09/2026 — R021 (relacionamento, Europa):** (1) **2ª leitura da MarekG a partir de 22/09 19:20 UTC** (`escala_serie.py remedir`, comandos na rodada); (2) **Polônia** foi o único mercado novo a render — próxima varredura do nicho começa por PL e pelas Páginas com nome de blog; (3) medir **todas** as Páginas do destino: a love-coach escondia uma Página-mãe de 70 mil atrás de personas de 4 mil; (4) no AdHeart, orçar ~1,5 busca por frase.

**Atualização de 21/09/2026 — R020:** coleta Meta **suspensa até o operador liberar**; um coletor Meta por vez no repositório (4 sessões na mesma conta de proxy); frase `bloqueada=true` encerra a lista até o cooldown (~12 h). Fila da retomada: (1) 2ª leitura de `theprofilesystem.com` e `clientzonetemplates.com` a partir de 22/09 05:42 UTC; (2) busca por marca `jobescape` + seguidores das personas + ATC; (3) frases não coletadas (`Amazon KDP`, `UGC creator`, `faceless YouTube`, `print on demand`, `earn from home`, `WiFi Loophole`).

**Atualização de 21/09/2026 — R019 (renda extra, EUA, advertorial com persona):** (1) **Sondar o proxy antes de cada
lote** (`api.ipify.org` pelo gateway): o 407 TRAFFIC_EXHAUSTED só apareceu 40 minutos depois de a Meta ter parado de
responder, disfarçado de `ERR_TIMED_OUT`; as duas contas DataImpulse do perfil solaris estão zeradas e **a retomada
depende de saldo novo**. (2) Sem proxy o IP direto já está em 403 — não gastar tentativas. (3) A frase que rendeu em
inglês foi o cruzamento numa frase só: `without showing your face`, `digital products`, `faceless`; `take this quiz`,
`answer a few questions` e `see if you qualify` sozinhas entregam quiz-arbitragem, jurídico e saúde. (4) Pendências: a
**2ª leitura de `theprofilesystem.com` (240) e `clientzonetemplates.com` (97)**, a busca por marca do "WiFi Loophole"
(oferta-mãe do advertorial-afiliado `thedispatchreview.com`), `quiz.skilario.com` (molde Coursiv, 14 IDs de setembro) e as 6
frases bloqueadas (`master resell rights`, `AI skills`, `stay at home mom`, `your first $1,000`, `money personality`,
`which side hustle`). Comandos na rodada.

**Atualização de 20/09/2026 — R017 (advertorial com persona, Europa, fora do nutra):** quatro coisas
valem para as próximas rodadas. (1) **Usar `--proxy auto` sempre, e conferir o status HTTP antes de
acreditar num platô**: a Meta devolve 403 desenhado como "No ads match your search criteria", e sem
proxy isso começa por volta da 40ª busca — contagem zero pode ser bloqueio, não ausência de anúncio.
(2) **Não culpar os parâmetros**: durante a R017 chegou-se a registrar que `--ordenar` e
`--country ALL` travavam a paginação, e está errado — com proxy os dois funcionam (`eroscode` com
`--ordenar` trouxe 598 de 600). O que travava era o bloqueio por IP. (3) **Para achar
infoproduto dentro deste padrão, buscar pela frase de funil**, não pela clínica — `personalisierten
Plan`, `piano personalizzato`, `plan personalizado`. (4) Na Europa, o advertorial com persona é
**majoritariamente nutra, app de micronovela e produto físico**: das 16 identidades acima de 100 IDs
desta varredura, só 3 eram infoproduto digital. Pendências abertas: **alcance por país na transparência
da UE da Meta** não abriu na sessão automatizada; preço de Muses Academy e Céleste Valmont atrás de
quiz e de captura de e-mail; Trustpilot e VAV não consultados.

**Atualização de 20/09/2026 — R016 (Europa):** o recorte europeu se comporta de forma diferente do americano em
quatro pontos que valem para as próximas rodadas. (1) **A escala europeia é uma ordem de grandeza menor**: a maior
contagem legítima de infoproduto de renda extra na Meta foi 201 IDs, contra 767 e 940 nos EUA — não usar o limiar
americano para julgar "escalado" aqui. (2) **O Google publica faixa de impressões na UE** e não publica nos EUA:
medir sempre com `scripts/atc_impressoes_eu.py` antes de declarar magnitude indisponível. (3) **O gate AUDIÊNCIA é
o filtro dominante**: nove de doze auditadas caíram nele, o que sugere que o infoproduto europeu deste nicho é mais
dependente de canal e produtor-rosto que o americano. (4) **Frase de nicho em alemão mistura oferta com vaga de
emprego** — `Nebenjob` e `Quereinsteiger` são termos de recrutamento; usar `Nebeneinkommen`, `passives Einkommen` e
`online Geld verdienen`. Pendência aberta: a **ingestão canônica das três finalistas** está bloqueada porque
`reports/intel/pool.jsonl` tem 27 linhas quebradas desde 12/08/2026; os cards já estão convertidos em
`reports/intel/_cards_*.json` e o comando está na rodada. Nenhuma aprovação inferida.


**Atualização de 20/09/2026 — R015:** três finalistas novas, as duas redes cobertas e **duas correções que
atingem rodadas anteriores**. (1) O token de paginação da Central de Transparência do Google era reenviado na
chave `"9"`, e a API devolvia a primeira página indefinidamente: toda contagem de criativo desde a R012 estava
multiplicada pelo número de páginas pedidas. O token vai na chave `"4"`; com ele a contagem fecha com o
cabeçalho da própria interface. Coursiv, FPA Workshop e HighTicket.io **ainda precisam ser remedidas**.
(2) `keyword_exact_phrase` com o domínio só acha anúncio cujo texto cita a URL — serve para confirmar
atribuição, não para medir tamanho; para medir, buscar pela marca e contar o hostname de destino.
Outras: o leaderboard `a/channels` do VAV ignora o filtro `lastseen`; a descoberta por **nome de canal**
(`vav_coleta.py --in channel`) rendeu os candidatos que o leaderboard não mostra; duas sessões no mesmo
repositório disputaram a pasta da rodada. Pendências: login do VidTao, Trustpilot bloqueado por verificação de
navegador, e os checkouts de Smartphone Freedom atrás de call. Nenhuma aprovação inferida.

**Atualização de 20/09/2026 — R014:** três finalistas novas com as duas redes cobertas. O que mudou
no procedimento: a página 2 do leaderboard do VAV não responde nesta conta (`status -1`), então a descoberta
Meta passou a ser por frase de nicho com rolagem real e destinos agrupados por hostname; a frase exata na
Ad Library precisa do host completo (`masterclass.shesellsremote.com`, não `shesellsremote.com`) e não carrega
domínio com hífen; o lock do executor pode estar com **outra sessão** — não matar, declarar. Pendências: login
do VidTao; checkouts das três atrás de captura. Nenhuma aprovação inferida.


**Prompt padrão de toda rodada (região e nicho como parâmetro; vazio pergunta):** `projeto/treinamento/GOAL.md`.
**Especialização pronta para a próxima rodada de renda extra (reescrita em 21/09/2026):** `projeto/treinamento/GOAL-RENDA-EXTRA.md` — agora pelo método do advertorial com persona (proxy, frase de funil cruzada com dinheiro, Páginas-persona, REGRA PRIMORDIAL, `triar_destinos.py`), com REGIÃO como parâmetro; a receita anterior (EUA por VAV) fica arquivada no fim do mesmo arquivo.
**Assinaturas do advertorial agressivo (21/09/2026, aprovadas pelo usuário nas finalistas da R017):** [CRITERIOS.md — ASSINATURAS](CRITERIOS.md#assinaturas-do-advertorial-agressivo--o-que-essas-ofertas-têm-de-único-e-como-reconhecer-em-segundos) — quiz no host, ≥ 3 Páginas-persona com audiência zero, frase de funil na copy, preço atrás do quiz, e as peças que mandam descartar sem abrir (app, micronovela, físico). Detector: `scripts/triar_destinos.py`. Eixo D em `spy/knowledge/BLACK_AD_SIGNALS.md`.
**Especialização de 21/09/2026 para RELACIONAMENTO** (o recorte das 3 finalistas aprovadas da R017): `projeto/treinamento/GOAL-RELACIONAMENTO.md` — gatilho por sub-nicho (reconquista, intimidade, atração, astrologia, comunicação, divórcio), frases que renderam e que enganam por idioma, e a tabela do que parece oferta e não é (micronovela, app de namoro, nutra de DE, físico, consultório, marca-pessoa).
**Especialização de 20/09/2026 para ofertas de advertorial com persona, em escala:** `projeto/treinamento/GOAL-ADVERTORIAL.md`. Nasceu do exemplo `myavellis.com` que o usuário mandou depois da R016: busca pela frase clínica da copy (não pelo domínio, que trava em ~30 cartões), piso de 150 IDs, contagem de Páginas-persona por destino e suplemento admitido como referência de ângulo.
Destila as 27 lições da R013 em uma sequência executável: leaderboard do VAV como porta de
descoberta, frase exata na Meta, rolagem até o platô real, atribuição de destino por ID, teste
marca-vs-domínio, métricas de intensidade e o bloqueio conhecido de gasto/receita/lucro.

**Atualização de 20/09/2026 — R013:** segunda rodada seguida a fechar com finalista comprovada em
cada frente, agora no recorte de renda extra. O que rendeu na descoberta foi o leaderboard
`a/channels` do VAV ordenado por `videocount` na janela de 1 mês: 160 canais US separaram os
anunciantes de infoproduto dos anunciantes de marca sem nenhum insumo da Meta, e o campo que decide
é `lastseen`, não `videocount`. Na Meta, a busca por domínio **precisa** ser
`search_type=keyword_exact_phrase` com o domínio entre aspas — a busca por token devolveu 2.100
resultados contaminados para `highticket.io` contra ~770 no filtro exato. Pendências abertas:
preço e gateway das três finalistas, todos atrás de formulário de captura; sessões de Tyver,
Foreplay, Adyntel, Anstrex e Trendtrack nunca testadas; VidTao aguardando um login do operador.
Ferramenta nova desta rodada: `scripts/atc_paises.py` (países, datas e faixas de impressão por
criativo via `GetCreativeById`). **Correção aplicada depois da primeira entrega:** a rolagem da
Ad Library havia sido interrompida cedo e o platô tratado como limite da plataforma — `highticket.io`
foi de 108 para **767** IDs, `fpaworkshop.com` de 24 para **152** e `1orderaway.com` de 30 para
**103**, que além disso **redireciona para o funil da HighTicket.io** e deixou de ser candidata
separada. Nenhuma das três finalistas recebeu aprovação.


**Atualização de 20/09/2026 — R012:** pela primeira vez a rodada fechou com finalista comprovada em
cada frente. O caminho que funcionou na frente Google/YouTube foi minerar o ATC direto
(`SearchSuggestions` por termo → `SearchCreatives` por anunciante → `GetCreativeById` para países,
datas e faixas de impressão), porque nenhum minerador contratado cobre YouTube hoje. Pendências
abertas: preço e recorrência do fit4me.io; reconciliação `anúncio Google → vídeo YouTube` da
HypnosisDownloads; sessões de VAV e Spy.House. Nenhuma das três finalistas recebeu aprovação.


**Preferência explícita de 20/09/2026 — após a R014, vale para tudo daqui em diante:** o usuário
rejeitou She Sells, 20-Minute Trader e Booming Bookkeeping porque todas se apoiam em Facebook ou
YouTube fortes (Página de 41 mil seguidores; canais de ≈20 mil inscritos com o produtor-rosto como
marca). O que ele procura é **marca sem seguidor, em escala**: Página/canal pequenos, sem rosto, e
ainda assim muitos anúncios persistentes. Virou gate AUDIÊNCIA em [CRITERIOS.md](CRITERIOS.md) e no
[GOAL-RENDA-EXTRA.md](GOAL-RENDA-EXTRA.md); eventos “ruim” gravados em `avaliacoes.jsonl`. Nenhuma das
7 do gate completo é exemplo positivo desse alvo — a próxima rodada procura o primeiro.

**Atualização de 20/09/2026 — R011:** no recorte de renda extra, Maria Wendt continua
com atividade e persistência públicas, mas é repetida na lista e depende fortemente da
autoridade da produtora. Business Lending, Midas, Money Wave e Wood Craft Blueprints
não receberam PDF de “escalada” por falta de evidência atual equivalente ou por não
serem ofertas centrais de renda extra.

**Atualização de 20/09/2026 — R010:** BetterMe Mental Health foi registrada como
auditada e entregue, pendente de avaliação. O inventário individual validado superou
as demais candidatas desta rodada: 148 IDs, 140 com mais de sete dias. WalkFit e
Yoga-Go mostraram cabeçalhos grandes, porém lançamentos recentes; Lasta continuou como
benchmark já conhecido. Preço, trial e garantia do fluxo BetterMe continuam não
confirmados. O renderizador de planilha não mostrou desenhos, mas o pacote XLSX contém
nove mídias e o relacionamento de desenho; abrir no Excel/LibreOffice é uma verificação
adicional recomendada quando um desses motores estiver disponível.

**Atualização de 19/09/2026 — R009:** o recorte prosperidade + Digistore24 + anúncios
entregues nos EUA terminou em bloqueio concreto. Midas comprovou produto e checkout,
mas zero ativos pelo domínio exato e a rota atual usa ClickBank. Billionaire Brainwave
e Money Wave existem no catálogo DS24, porém os anúncios observados não eram dessas
ofertas. Divine Frequency teve três IDs US, mas gateway não confirmado. Usar
[OFERTAS-MAPEADAS.md](OFERTAS-MAPEADAS.md) antes de toda nova busca. Reverse Health
permanece a única favorita; R008 segue pendente; nenhuma aprovação foi inferida.

**Aprendizado mais recente — 18/09/2026:** o usuário considerou que o lote E001 não parecia tão escalado. Feedback literal e lições em [CRITERIOS.md](CRITERIOS.md), com calibração em [METRICAS.md](METRICAS.md). A revisão sustentou escala alta em 0/11 ofertas; a próxima seleção deve validar distribuição antes de aprofundar funis e promover finalistas. Não equivale a rejeições individuais; aprovações R003 preservadas. Sem nova coleta por este registro.

Expansão E001 autorizada em cinco forks: [missão e contrato compartilhado](expansao/E001/README.md).
Primeira exploração em paralelo por nichos, usando acervo e fontes públicas, com pastas
exclusivas e propostas de expansão de coleta. IDs das tarefas em `expansao/E001/forks.json`.
Essa exploração não multiplica a autorização paga das rodadas anteriores.

R003 está encerrada e avaliada: Blood Sugar Fix, Black Book e Little Dictator aprovados;
BLB e Upgrade Your Life rejeitados. R001 e R002 continuam sem avaliações individuais. Não iniciar
coleta automaticamente. Próxima distribuição pretendida: oito Meta e sete Google;
a R003 originalmente entregou oito Google e sete Meta; após o filtro de seis meses,
restam três Google e cinco Meta. Sete reposições pendentes, sem execução automática.
Revisar as lacunas e hipóteses antes de buscar semelhantes aos aprovados. Priorizar
replicabilidade sem depender da audiência do produtor, percurso de venda direta e
vários ângulos para o mesmo produto. Ver regras e exceções em CRITERIOS.md.
Manifestação e relacionamento não limitam os nichos. Manter peso igual entre redes;
o resultado desta pequena amostra não muda essa preferência.

Planilha de avaliação: https://docs.google.com/spreadsheets/d/1c0s3qq0vOs0jJSUbUmGK-PLYUDHUplu9YKxOrye4qkY/edit
ID e oferta ficam em A:B; feedback atual em Z:AA. Conferir cabeçalhos a cada importação,
pois a inserção de colunas muda os endereços. Reimportação idêntica não duplica eventos.
Aprendizado persistido nos arquivos locais; ranking hospedado não sincronizado.
