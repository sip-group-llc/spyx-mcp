# O ciclo de uma rodada

Cada rodada é uma conversa. O Claude segue estes seis passos com as tools; você entra no 1 (alvo) e no 4 (veredito).

## 0. Alvo

`goal(nicho, regiao, padrao?, quantidade?)`

Devolve o pedido da rodada com o método embutido. As frases de busca por idioma, as exclusões e o formato de
entrega vêm daí — você não precisa saber montar. Tool comum: funciona em qualquer cliente.

## 1. Preparar

`base("CRITERIOS", secao="REGRA PRIMORDIAL")` · `base("CRITERIOS", secao="ASSINATURA")` · `base("meu", secao="*")` · `rodadas(ultimas=3)`

Ele lê o critério do operador, o **seu** critério (fork) e as suas últimas rodadas, e declara: hipótese, rede, país, frases de busca e o que muda em relação à rodada anterior. Região vazia → uma pergunta, nenhuma busca antes.

## 2. Minerar

`minerar(q, pais)` → `status(job)` até `pronto`

Frases de funil cruzadas com o nicho, no idioma do país. Uma coleta por vez: a fila é automática. Resultado: cabeçalho, IDs, destinos por hostname e uma triagem pela assinatura do advertorial.

`bloqueada=true` **não é contagem.** O país é encerrado por algumas horas e a lacuna fica registrada.

Enquanto roda, `status` devolve `decorrido_min` e as últimas linhas do coletor. Tentativas `t1, t2…` com
`0 IDs` e `cabecalho None` significam sessão travada: o coletor insiste até 8 vezes (~15 min) antes de declarar
`bloqueada`. Não vale a pena esperar: `cancelar(job)` e tente outra frase ou outro país.

## 3. Revisar

Abrir a landing **antes** de contar por marca. Fora: app, SaaS, serviço, corretora, vaga, produto físico, micronovela. Persona nova da mesma operação não é oferta nova. Distinguir anúncio, página, domínio e oferta — nunca somar as contagens.

## 4. Ouvir

`avaliar(rodada, item, veredito, motivo)`

Você diz "R003-B ruim pelo produto". Ele grava exatamente isso. Motivo que você não deu fica `null`; a hipótese dele nunca preenche a sua avaliação.

## 5. Refinar

`anotar(tipo, texto, origem)` — `preferencia` · `licao` · `hipotese` · `exclusao`

O que a rodada ensinou vai pro seu fork, datado e com a origem. Um exemplo gera hipótese, não regra: vira `preferencia` quando repete.

## 6. Medir

`escala(chave, job)` registra a leitura D+0 do destino. `escala(chave)` mostra a série e o veredito:

| Leituras | O que pode ser escrito |
|---|---|
| 1 | **inventário** — "escala: pendente de segunda leitura" |
| 2+, separadas por ≥ 24 h, mesmo método | **indícios de escala** — sempre com a série ao lado |

Atribuição (IDs no destino / total) e persistência (> 30 d, > 90 d) valem com uma leitura. Tamanho, não.

## Fechar

`rodada_salvar(id, markdown)` — hipótese, buscas (q, país, IDs, bloqueada?), candidatos com inventário/atribuição/persistência/personas, lacunas e o que muda na próxima. A próxima rodada começa lendo isto.
