# GOAL — <nicho> · <padrão> · <região>

> Copie este arquivo com outro nome, preencha os `<campos>` e refine a cada rodada: este arquivo é seu.
> O método completo está em `base/GOAL-RENDA-EXTRA.md` e `base/GOAL-ADVERTORIAL.md`; leia antes.

Encontrar e auditar as ofertas de **<nicho>** no padrão **<padrão: ex. advertorial com persona — marca
sem rosto, Páginas-persona, quiz>** mais escaladas em **<região>** e entregar **<quantidade: ex. 3
finalistas com ≥ 150 IDs ativos>**, NOVAS (fora das exclusões em `meu/CRITERIOS-meu.md`), sem audiência
própria. Rede única: Meta.

**Antes de buscar:** `base/CRITERIOS.md` (REGRA PRIMORDIAL, ASSINATURAS), `meu/CRITERIOS-meu.md`, últimas
3 rodadas. Declarar hipótese e o que muda.

**Busca — descobrir, depois medir:**
1. `minerar(fonte="adheart", q="<2–3 termos amplos do nicho>", pais, sort="total_reach")`: os de maior
   alcance, com amostra. É de onde saem os candidatos.
2. Meta, na ordem **volume → assinatura → formato**: primeiro o termo que o nicho inteiro usa
   (<ex.: "renda extra", "ganhar dinheiro online">), depois a assinatura pra separar, e só então frase de
   FUNIL (<"faça o teste", "plano personalizado", "descubra se">) pra achar o quiz que o termo comum não pega.
   Nunca termo de recrutamento/vaga. **Alterne o país a cada busca** (1–2 por país e a Meta trava ~12 h).
   `bloqueada=true` não é contagem. Agrupar por destino; usar a `triagem` do `status` antes de contar por marca.
3. **Piso**: <≥ N IDs no mesmo destino — na 1ª rodada de um mercado novo, deixe em branco e fixe a partir do
   maior destino medido>.

**Entregável antes da contagem:** abrir a landing. Fora: app, SaaS, serviço, corretora, vaga, físico,
micronovela. Persona nova da mesma operação não é oferta nova.

**Personas:** ≥ 3 Páginas no mesmo destino com nome de pessoa (`anuncios(job, destino)`). Marca-pessoa ou
Página grande: registrar, não promover.

**Escala:** contagem única é inventário. `medir` + `escala_serie.py registrar-json` na entrega (D+0);
"escalada" só com 2 leituras ≥ 24 h.

**Fechar:** `meu/rodadas/Rnnn.md` + pedir veredito por candidato → `meu/avaliacoes.jsonl` → refinar
este goal e `meu/CRITERIOS-meu.md`.
