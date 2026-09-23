# GOAL — renda extra no YouTube

Este é o método para buscar ofertas de renda extra anunciadas no YouTube. Região e idioma são parâmetros
da rodada. A rede é YouTube; a Meta não entra como filtro. Guarde ajustes pessoais em `meu/goals/`.

## Objetivo

Encontrar até três ofertas **novas** de infoproduto, sem audiência própria grande, com vídeo de anúncio
recente e crescimento de views. Abra o destino para confirmar o que é vendido antes de comparar números.
Não promova serviço, aplicativo, produto físico ou marca sustentada pela fama do produtor.

## Descobrir pelo MCP

1. `google(modo="descobrir", q="<1–3 termos locais separados por ;>", pais="<PAIS>", max_pages=3)`.
   Use `status(job, esperar=60)` até terminar e leia todas as páginas de `google_resultados(job)`.
   O limite de anunciantes é uma amostra, distribuída entre os termos. Leia `cobertura` e
   `sugestoes_nao_sondadas`; uma busca ampla sem candidato não encerra o nicho. A busca por termo pode
   achar apenas a razão social. `dominios_observados` são pistas, não destinos confirmados.
2. Para cada domínio candidato, `google(modo="dominio", q="<hostname>", pais="<PAIS>", max_pages=10)`.
   Registre anunciantes, formatos, datas, limite da paginação e `video_id` ligado ao `creative_id`.
   A sonda confirma o hostname no recorte ATC, mas não a URL final do criativo. Um resultado sem
   `video_id` não descarta a oferta. Nunca trate `displayads-formats.googleusercontent.com` como landing.
3. `youtube_video(ids="<id1,id2>")` lê views, data de publicação, estado não listado e canal.
   Salve a resposta em `meu/dados/` e registre a leitura com
   `python scripts/escala_serie.py registrar-youtube-json --de meu/dados/<arquivo>.json --oferta <hostname> --rodada Rnnn`.
   Repita os **mesmos vídeos** após pelo menos 24 horas para medir views por dia.

## Julgar a evidência

- **Uma leitura de views é inventário.** Duas leituras separadas por ≥24 h sustentam um indício de escala,
  com intervalo e delta explícitos. A média desde a publicação não substitui a segunda leitura.
- **Poucos criativos não reprovam YouTube.** O ATC confirma anúncio pago, período e região; o contador do
  próprio vídeo mede views. Vídeo listado pode acumular tráfego orgânico. Views não são gasto nem vendas.
- Confirme o elo `anunciante → creative_id → video_id → destino → oferta`. Ausência de qualquer elo fica
  registrada como pendência. País da busca não prova entrega naquele país sem evidência da plataforma.
- Consulte canal e produtor; registre inscritos, rosto e nome pessoal. Exclua audiência própria grande
  conforme `base/CRITERIOS.md` e anote casos limítrofes para calibração.
- Use o histórico pessoal em `meu/` para excluir ofertas já mapeadas. Não transforme julgamento do agente
  em avaliação da pessoa.

## Entrega

Escreva a rodada em `meu/rodadas/Rnnn.md`: termos, região, limites, candidatos, vínculos comprovados,
leituras com data/hora e descartes. Se a busca ATC não achar vídeo auditável, declare a lacuna e a cobertura
efetiva; não substitua silenciosamente por candidatos Meta.
