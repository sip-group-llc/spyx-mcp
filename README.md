# HackingAds MCP

<p align="center"><img src="docs/img/hero.svg" alt="anúncios minerados: quiz com persona, atribuição, série de escala" width="100%"></p>

<p align="center">
<img src="https://img.shields.io/badge/motor-MCP%20remoto%20%C2%B7%2014%20tools-e5484d?style=flat-square" alt="motor">
<img src="https://img.shields.io/badge/base-local%20%C2%B7%20.md%20editados%20pelo%20seu%20Claude-3fb950?style=flat-square" alt="base">
<img src="https://img.shields.io/badge/fontes-10%20mineradores%20%C2%B7%20Meta%20%C2%B7%20Google-2f81f7?style=flat-square" alt="fontes">
<img src="https://img.shields.io/badge/regra-escala%20%3D%202%20leituras%20%E2%89%A5%2024h-d29922?style=flat-square" alt="regra">
</p>

Inteligência de anúncios e catálogos, com confirmação de veiculação atual nas bibliotecas públicas,
operada pelo seu Claude. Você clona esta pasta, cola a sua chave
e opera em conversa: o motor coleta, o seu Claude audita com um critério já calibrado em 24 rodadas, você
dá o veredito, e o que você aprende fica gravado em `.md` que só você edita. A base do operador chega por
`git pull`; a sua nunca é sobrescrita.

## Em 30 segundos

| | |
|---|---|
| **O que é** | um motor que descobre ofertas e mede indícios de escala, separando *inventário* de *escala* e *anúncio* de *oferta* |
| **O que você precisa** | Codex ou Claude Code, git, Python 3 e a chave do operador |
| **O que você não precisa** | conta em fonte nenhuma, proxy, infraestrutura: tudo isso mora no motor, atrás da chave |
| **O que fica com você** | goals, critério, rodadas, avaliações e séries em `meu/`, na sua máquina |

## Comece

```bash
git clone https://github.com/sip-group-llc/hackingads-mcp
cd hackingads-mcp
```

Escolha o cliente:

**Claude Code:** troque `<SUA_CHAVE>` no [`.mcp.json`](.mcp.json) pela sua chave individual e rode na pasta:

```bash
claude
```

Na primeira abertura, aceite a confiança na pasta para carregar o `.mcp.json` e as ferramentas do motor.

**Codex:** adicione ao `~/.codex/config.toml` do seu usuário (no Windows,
`%USERPROFILE%\.codex\config.toml`) e substitua `<SUA_CHAVE>`:

```toml
[mcp_servers.hackingads]
url = "https://arasaka.corex11.tech/mcp"
http_headers = { Authorization = "Bearer <SUA_CHAVE>" }
```

Abra esta pasta em uma nova tarefa do Codex; o [AGENTS.md](AGENTS.md) orienta o fluxo. Confira se o MCP
`hackingads` aparece com `planejar_fontes`, `fontes`, `minerador`, `minerador_resultados`, `google`, `minerar` e `status`. O
`config.toml` é pessoal; não coloque a chave em arquivos versionados nem publique seu `.mcp.json` editado.
Se atualizar o pacote, `python scripts/check_mcp_contract.py` confere se as
ferramentas documentadas, as permissões e o roteamento continuam coerentes.

Primeira conversa: **"como eu uso isso?"** ou
**"prepare uma rodada de renda extra no YouTube, região ES"**. O agente confere o escopo, mostra o Goal
exato e pergunta se você aprova ativá-lo. Envie `/goal` somente depois dessa revisão se quiser a trava
antes da ativação; o aplicativo pode ativar um `/goal` colado diretamente antes de o agente ler a mensagem.

Sem chave? Abra uma issue [pedindo acesso](../../issues/new?template=acesso.md).

## Como funciona

<p align="center"><img src="docs/img/ciclo.svg" alt="sua máquina: meu/ + base/ + o seu Claude + escala_serie · motor remoto: minerar, paginas, status, anuncios, medir" width="100%"></p>

Uma rodada é uma conversa em seis passos: **preparar** (ler o critério e as suas rodadas;
`planejar_fontes` escolhe as fontes pela rede) → **minerar**
(Meta: biblioteca + mineradores compatíveis → `minerar(fonte="meta")` → `anuncios`; YouTube:
`google` → `google_resultados` → VAV quando a sessão responder →
`youtube_video`) → **revisar** (abrir a landing e medir a audiência) →
**ouvir** (o seu veredito, com as suas palavras) → **refinar** (editar o seu critério e o seu goal) →
**medir** (`medir` → série local). Fecha em `meu/rodadas/Rnnn.md`. As capacidades e limitações de cada
fonte estão em [docs/fontes.md](docs/fontes.md); o ciclo completo está em [docs/ciclo.md](docs/ciclo.md).

## A teoria por trás

Tudo o que está abaixo é a base pública em `base/`, desenhada. O seu Claude aplica isso sozinho; você só
precisa saber que existe.

### Escala é o que sobrevive à repetição da medida

<p align="center"><img src="docs/img/regra-primordial.svg" alt="regra primordial: inventário, atribuição, persistência, repetição" width="100%"></p>

A regra que vence todas as outras. Contagem única é inventário; "escalada" só com duas leituras separadas
por 24 h, mesmo método. Atribuição e persistência valem com uma leitura; tamanho, nunca. A tool `medir` e o
script de série aplicam isso por você: com uma leitura, o texto diz "inventário".

### Leitura bloqueada não é contagem

<p align="center"><img src="docs/img/bloqueada.svg" alt="a mesma busca: 28 ou 598 conforme o medidor" width="100%"></p>

Um número que muda com quem mede não é propriedade da oferta. Por isso o motor devolve `bloqueada=true` em
vez de zero, e o zero nunca entra na série.

### A assinatura do advertorial agressivo

<p align="center"><img src="docs/img/assinatura.svg" alt="marca sem rosto, páginas-persona, copy em primeira pessoa, quiz com preço escondido" width="100%"></p>

O padrão que o critério sabe reconhecer: marca sem rosto, várias Páginas com nome de pessoa e audiência
quase zero, copy em primeira pessoa com frase de funil, quiz cujo preço só aparece depois. `status` já
devolve a triagem por esses sinais; `paginas` mede os seguidores.

### O gate: entregável antes da contagem

<p align="center"><img src="docs/img/gate.svg" alt="anúncio, página, domínio, oferta: abrir a landing antes de contar" width="100%"></p>

Anúncio, Página, domínio e oferta são coisas diferentes e nunca se somam. Abrir a landing vem antes de
qualquer contagem por marca: app, SaaS, serviço, corretora, vaga, físico e micronovela saem antes de virar
número.

### O fork: a base do operador por baixo, a sua por cima

<p align="center"><img src="docs/img/fork.svg" alt="base/ do operador via git pull, meu/ da pessoa, como evolui" width="100%"></p>

`base/` é do operador e atualiza sozinha. `meu/` é seu, nunca é tocado, e vence em conflito. Um exemplo
vira hipótese; repetição vira preferência; o que foi refutado sai.

## Uma rodada inteira, sem cutucar

Uma rodada leva horas: várias buscas, esperas, medição. Peça a rodada ("minera renda extra no BR,
traz os mais escalados") em mensagem comum. O agente pergunta apenas o que faltar, mostra o texto final
e espera sua aprovação antes de ativar `/goal`. A rodada entrega finalistas comprovados **e** os achados
mais fortes que ficaram abaixo dos critérios, com links e motivos; registra descobertas em `meu/`.
O procedimento está em [docs/goal-preflight.md](docs/goal-preflight.md).

## Quanto tempo leva uma busca

Uma busca pode levar minutos. A Meta pode bloquear a sessão e devolver `bloqueada=true`; isso não é zero
anúncios. `status(job, esperar=60)` acompanha a execução e `cancelar(job)` interrompe. Mineradores pagos
dependem da sessão, da assinatura e da quota atuais. `fontes()` confirma pré-requisitos, e a resposta do job
confirma a execução. Consulte uma fonte compatível por vez dentro dos limites informados.

## O que tem na pasta

```
CLAUDE.md          o ciclo, a base por dentro, a tradução base → motor, as regras
AGENTS.md          entrada do Codex e trava de aprovação antes do Goal
base/              CRITERIOS · README (ciclo) · METRICAS · GOAL-ADVERTORIAL · GOAL-RENDA-EXTRA · GOAL-RENDA-EXTRA-YOUTUBE · GOAL-RELACIONAMENTO
meu/               CRITERIOS-meu · goals/ · rodadas/ · avaliacoes.jsonl · serie-escala.jsonl · dados/
scripts/           escala_serie.py — a série da regra primordial
docs/              tools do motor (gerado) · pré-voo do Goal · ciclo · exemplo · diagramas
.claude/           permissões pré-aprovadas: tools do motor, WebFetch, o script; base/ bloqueada para escrita
```

## Atualizar a base do operador

```bash
git pull
```

O pacote atualiza `base/`, instruções e docs. Seus registros em `meu/` continuam pessoais. Leia o diff
antes da próxima rodada; se um arquivo pessoal seu tiver o mesmo nome de um novo arquivo do pacote, resolva
o conflito preservando seus dados.

Mais: [as tools do motor](docs/tools.md) · [as fontes](docs/fontes.md) · [o ciclo](docs/ciclo.md) · [uma rodada de exemplo](docs/rodada-exemplo.md) · [changelog](CHANGELOG.md)
