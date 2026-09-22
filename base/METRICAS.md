# Métricas que acompanham cada rodada

> **Acima de tudo o que está aqui:** a [REGRA PRIMORDIAL](CRITERIOS.md#regra-primordial--escala-é-o-que-sobrevive-à-repetição-da-medida)
> — contagem tirada uma vez é **inventário**, não escala. Nenhuma métrica desta página vira "escalada"
> sem **duas leituras separadas no tempo**, registradas em [`serie-escala.jsonl`](serie-escala.jsonl).
> A linha **Tendência** da tabela abaixo passa a ser obrigatória para toda finalista, não opcional.

Todo valor tem fonte, unidade, entidade, janela, data de observação e link/arquivo de
evidência. Campo ausente é `null`/desconhecido, nunca zero. Campos públicos e estimativas
de fornecedor permanecem separados. Registrar limites inferior/superior quando for faixa.

| Dimensão | Registrar | Limite |
|---|---|---|
| Identidade | ID anúncio, página/anunciante, domínio, caminho da landing, oferta | Mesmo domínio pode vender várias ofertas; IDs de fornecedores não são IDs públicos |
| Produto | Entregável, nicho, preço/moeda, recorrência, mecanismo e promessa | Preço anunciado não confirma checkout; promessa não é resultado comprovado |
| Geografia | Mercado pretendido, filtro aplicado, países com evidência, idioma | AdHeart market filtra idioma; país do anunciante não é país de entrega |
| Atividade | Status, início/fim informados, primeira/última observação, dias entre datas | Dias decorridos não garantem gasto contínuo; datas invertidas ficam inválidas |
| Volume criativo | IDs distintos, contagem da página e da amostra, formatos/duração | Não confundir variações, anúncios e criativos únicos; contagem aproximada mantém ~ |
| Alcance | Meta UE e países quando disponíveis, unidade original | Contas alcançadas não são impressões; não somar públicos sobrepostos |
| Impressões | Faixa pública quando exibida, ex.: <100, com anúncio/recorte | Não transformar faixa em valor exato; ausência não é zero |
| Views | Fonte, vídeo e data; delta apenas com observações comparáveis | Views públicas podem incluir orgânico; não equivalem a views pagas |
| **Tendência (obrigatória)** | **Número de leituras**, data e valor de cada uma, delta entre elas; novos IDs, persistência, delta/dia na mesma fonte | Replay não cresce; fonte mudou ou contador caiu exige revisão. **Uma leitura só = inventário**; ver REGRA PRIMORDIAL |
| Funil | Imagem/vídeo/texto, VSL/TSL/quiz, CTA, checkout, caminho verificado | Vídeo de anúncio não comprova VSL; root sem página não derruba toda a oferta |
| Replicabilidade | Dependência de marca/audiência pessoal (baixa/alta/incerta), evidência, mecanismo adaptável, venda direta versus captura/call, ângulos distintos por produto | Preferência confirmada no feedback R003; rosto/nome não bastam para excluir. Afinidade e escala são avaliações separadas |
| Resultado comercial | Gasto, vendas, receita, CPA, ROAS, conversão, reembolso | Só com origem verificável e período; biblioteca pública não os fornece por padrão |
| Qualidade da evidência | Fonte primária/fornecedor, frescor, conflitos e faltantes | Campo ATC RPC13 sem contrato fica em quarentena |

## Métricas do nosso processo

- Rendimento: candidatos aderentes confirmados / anúncios únicos revisados, por termo/rede.
- Precisão pessoal: boas / (boas + ruins), com tamanho da amostra; incertas e pendentes à parte.
- Apresentar também aprovação por oferta distinta; dois anúncios da mesma oferta não são dois exemplos independentes. R003: 5/8 anúncios e 3/5 ofertas aprovados, sem inferir preferência por Meta sobre Google.
- Cobertura: revisados e pendentes por rede/país; confirmar origem geográfica separadamente.
- Custo: buscas reservadas, páginas, tempo e custo monetário apenas se documentado.
- Novidade: ofertas novas verificadas / ofertas revisadas, com critério explícito de dedup.
- Evolução: comparar rodadas com escopo comparável; avaliação posterior não muda o bruto anterior.

## Estado de conclusão por candidato

### Calibração após E001 — 18/09/2026

- Resultado observado: **0/11 ofertas com sustentação de escala alta** na revisão visual E001; 13 IDs Meta com 9 ativos, 3 inativos e 1 indisponível. Denominadores diferentes: ofertas versus anúncios. Isso não é taxa de rejeição humana nem estimativa de vendas do mercado.
- Registrar rendimento de fortes indícios separadamente de aderência criativa, produto confirmado, atividade e funil acessível. Uma ficha completa pode continuar com escala indeterminada.
- Em cada contagem, registrar total retornado, cartões efetivamente inspecionados, IDs vinculados à landing/produto, grupos e criativos deduplicados (ou null). Mostrar a data de cada inventário, mesmo quando o status do anúncio tiver sido atualizado depois.
- Distinguir intensidade recente de alcance acumulado: datas de início/fim do anúncio não definem automaticamente a janela do contador. Não dividir alcance por dias desde início e apresentar como entrega diária observada.
- Para deltas, exigir mesma fonte, mesmo ID, região, unidade e definição, horários dos snapshots e ressalva de atraso/revisão da estimativa. Um delta de curto intervalo não comprova ritmo sustentado nem resultado comercial.
- Registrar status do ID e evidência de outros IDs ativos da oferta separadamente. Indisponível não equivale a inativo, zero impressões, banimento ou oferta encerrada.
- Acrescentar custo de revisão por oferta promovida e motivos de não promoção quando esses dados forem medidos; não estimar retroativamente tempo/custo sem registro.

Feedback humano e exemplos: [CRITERIOS.md — lições de 18/09](CRITERIOS.md#feedback-do-lote-e001-e-lições-da-revisão--18092026).

### Gate obrigatório da biblioteca — feedback humano pós-E001, 17/09/2026

Cada ficha deve registrar `validacao_biblioteca` (concluida/parcial/bloqueada/pendente),
`verificado_em` com fuso, URL e evidência preservada, filtros aplicados, IDs examinados,
contagem e escopo (oferta/anunciante/amostra), ativos versus inativos, datas observadas,
criativos distintos versus variações, métricas de distribuição disponíveis e suas
janelas, sinais contrários e justificativa da classificação. Ausentes continuam null.

Revisão concluída não garante indícios fortes. Exigir convergência de evidências
relacionadas à mesma oferta; duas contagens do mesmo inventário não são dois sinais
independentes. Sem distribuição mensurável, explicitar essa lacuna e não promover
atividade/contagem isoladas a escala forte. Revisão parcial ou bloqueada impede
confirmação: escala indeterminada, e não “não escalada”. Não inferir vendas ou lucro.

Medir por rodada: ofertas com biblioteca revisada / ofertas apresentadas; ofertas com
fortes indícios sustentados / ofertas revisadas; pendências de validação em separado.

Registrar separadamente: afinidade humana (pendente/boa/ruim/incerta), entregável digital
(confirmado/pendente/fora), atividade (fonte/data), escala (desconhecida/indícios).
Só elevar a conclusão com evidência nova. Volume, longevidade e variações sustentam
indícios; faturamento e rentabilidade exigem dados comerciais verificáveis.
