# HackingAds MCP

Inteligência de anúncios **no ar agora**, operada pelo seu Claude. Você conecta um servidor MCP, recebe
uma base de critério já calibrada (o que é uma oferta escalada, o que é armadilha) e roda o ciclo de
mineração em conversa: alvo → busca → auditoria → avaliação → refinamento. O que você aprende fica
no **seu fork**; a base do operador continua chegando por baixo, atualizada, sem merge.

Não há código pra instalar. Só uma URL e uma chave.

## Conecte em 2 minutos

**claude.ai** → Configurações → Conectores → *Adicionar conector personalizado*

| Campo | Valor |
|---|---|
| URL | `https://arasaka.corex11.tech/mcp` |
| Header | `Authorization: Bearer <SUA_CHAVE>` |

**Claude Code**

```bash
claude mcp add --transport http hackingads https://arasaka.corex11.tech/mcp --header "Authorization: Bearer <SUA_CHAVE>"
```

Ou copie o [`.mcp.json`](.mcp.json) deste repositório pra raiz do seu projeto e troque a chave.

Sem chave? Abra uma issue [pedindo acesso](../../issues/new?template=acesso.md).

## Como se usa

1. Peça ao Claude: **"chame `goal` com nicho X, região Y"** (padrão e quantidade são opcionais). `goal` é uma
   tool comum, então funciona em qualquer cliente; no Claude Code também existe como `/mcp__hackingads__goal`.
   O método já vem embutido; você só diz o alvo.
2. O Claude lê a base (`base`), as suas rodadas anteriores (`rodadas`) e declara a hipótese.
3. Minera (`minerar` → `status` a cada ~2 min; `cancelar` se travar), abre as landings, agrupa por destino, mede (`escala`).
4. Você dá o veredito por candidato; ele grava (`avaliar`) e anota o que aprendeu (`anotar`).
5. Fecha a rodada (`rodada_salvar`). A próxima começa de onde essa parou.

Detalhes: [o ciclo](docs/ciclo.md) · [as tools](docs/tools.md) · [uma rodada de exemplo](docs/rodada-exemplo.md)

**O que o seu Claude precisa ter:** as tools deste conector e a capacidade de abrir páginas na web
(no claude.ai já vem; no Claude Code, deixe `WebFetch` permitido). Sem isso o passo 3 (abrir a landing) não acontece.

**Quanto tempo leva uma busca:** 2–10 min. Se a fonte travar a sessão, o coletor insiste com esperas
crescentes por até ~15 min e então devolve `bloqueada=true` (que **não** é contagem). O `status` mostra os
minutos decorridos e avisa quando é isso; `cancelar(job)` interrompe e você tenta outra frase ou país.

## A regra que governa tudo

> **Escala é o que sobrevive à repetição da medida.** Contagem tirada uma vez é *inventário*.
> Só vira *indício de escala* com duas leituras separadas no tempo, mesmo método.

A tool `escala` aplica isso por você: com uma leitura ela escreve "inventário", nunca "escalada".

## O que fica com quem

| Seu | Do operador |
|---|---|
| Suas rodadas, avaliações, anotações e séries (`pessoas/<você>/`) | A base de critério (lida ao vivo, você não precisa mantê-la) |
| Sua chave, sua sessão, seus tokens de Claude | Coletores, fontes e infraestrutura |

Ninguém lê o fork de outra pessoa.

## Fontes

Biblioteca de Anúncios da Meta e AdHeart (busca por termo, com cota). Uma coleta por vez por fonte:
se outra pessoa estiver coletando, a sua entra na fila e o `status` mostra.
