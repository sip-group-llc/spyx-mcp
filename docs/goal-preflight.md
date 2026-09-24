# Pré-voo de Goal e contrato de entrega

Use este fluxo quando a pessoa pedir para minerar, mandar um goal como texto ou pedir para preparar/injetar `/goal`. É uma única revisão do escopo antes de começar; depois dela a execução autorizada segue até a condição de parada.

## Antes de ativar

1. Leia o pedido, o goal pessoal indicado (se existir), `meu/CRITERIOS-meu.md`, `meu/DESCOBERTAS.md` quando existir e as últimas rodadas relevantes. Não faça coleta nem grave uma rodada nessa fase.
2. Resolva **nicho e tipo de oferta**, **rede** (Meta, YouTube ou ambas), **país/região**, idioma dos termos, quantidade desejada e exclusões pessoais. País/região ausente, placeholder (`<PAIS>`, `REGIÃO:` vazia) ou mercados incompatíveis impedem a ativação: faça uma pergunta curta e espere. Se a rede não foi dita, proponha Meta + YouTube no resumo, sem deixar um goal antigo escolhê-la. Idioma pode ser inferido de país inequívoco, mas mostre a inferência.
3. Defina antes da execução o que provaria uma finalista e o que será entregue quando o gate falhar. Não transporte piso de criativos da Meta para YouTube. Use os limites normais das tools; não transforme a escolha de `max_pages` em nova pergunta ao usuário.
4. Mostre **o texto exato do Goal** (até 4.000 caracteres) e um resumo curto de país, rede, alvo, exclusões e entregáveis. Pergunte: **“Aprova ativar este Goal?”** Espere um “sim/aprovado” referente a esse texto. Se a pessoa mudar o escopo, revise o texto e peça aprovação da versão nova. Só então acione a ferramenta de Goal disponível ou peça que a pessoa cole o `/goal` aprovado no app.

Enviar parâmetros (“Estados Unidos”, por exemplo) resolve a lacuna, mas não aprova automaticamente a ativação. Se a pessoa já enviou `/goal` literalmente, o aplicativo pode ter ativado o objetivo; suspenda a coleta até resolver o pré-voo e explique que a revisão prévia depende de enviar primeiro o pedido sem `/goal`.

## Durante a rodada

- `planejar_fontes` relaciona os dez mineradores pelo recorte aprovado. Na rodada,
  anote fonte elegível consultada, bloqueada, sem quota ou dispensada com motivo;
  não substitua uma rede ausente por outra em silêncio. Catálogo sem filtro de país
  ou termo exige triagem local e confirmação independente.
- Trabalhe no país/rede aprovados. Salve respostas do MCP em `meu/dados/`; não confunda URL técnica da prévia com landing nem anunciante, domínio, anúncio e oferta.
- Antes de encerrar a descoberta, confira `cobertura`, termos solicitados/consultados, sugestões sem sondagem, anunciantes distintos, `video_id` distintos, vídeos lidos e vídeos ainda sem leitura. Priorize por aderência ao nicho e recência; investigue os candidatos plausíveis que ainda podem mudar a conclusão. Se uma limitação impedir o restante, registre-a como cobertura parcial.
- Em YouTube, leia vídeos dos anunciantes plausíveis para identificar produto, canal e audiência mesmo quando o destino ainda for hipótese. Views acumuladas e poucos/muitos criativos não provam escala. Para uma oferta atribuída, grave D+0 e repita o mesmo vídeo após ≥24 horas antes de falar em crescimento.
- Não encerre a rodada apenas porque não houve finalistas: entregue também **3–5 achados mais fortes da amostra**, ou todos se houver menos, com links diretos para anúncio/ATC e vídeo quando disponíveis, data da leitura, sinais observados e o gate que falta. Chame isso de ranking de **indícios observados**, nunca de “mais escaladas” sem série comparável. Não force candidato fraco a virar finalista.
- Crie ou atualize `meu/DESCOBERTAS.md` com os achados relevantes abaixo do gate, sua identidade/aliases e estado `mapeada` ou `hipótese`, para não reapresentá-los como inéditos. Não grave julgamento em `avaliacoes.jsonl` nem favorita sem fala explícita da pessoa.

## Condição de parada e resposta

`meu/rodadas/Rnnn.md` deve trazer (1) finalistas comprovados ou “nenhum comprovado nesta cobertura”, (2) ranking parcial com links e motivos, (3) cobertura numérica e lacunas, (4) descobertas persistidas, (5) o que ainda depende de fonte, operador ou leitura D+1. Se restarem candidatos plausíveis sem triagem dentro do escopo aprovado, continue ou declare explicitamente a limitação que impede avançar. A mera criação do arquivo da rodada não comprova que o Goal foi cumprido.

**Teste de mesa:** goal de YouTube sem país → perguntar país, sem coleta; resposta “Estados Unidos” → mostrar versão US/inglês e pedir aprovação, sem coleta; “aprovado” → ativar uma vez; zero finalistas com vídeos encontrados → entregar ranking parcial, cobertura e descobertas persistidas.
