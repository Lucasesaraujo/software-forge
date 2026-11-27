---
name: forja-retro
description: Faz a retrospectiva de um ciclo da Forja (iteração, fase de descoberta, feature, portão ou DU7) a partir dos dados guardados - métricas dos status.md, registro de melhoria e retros anteriores - e gera ações para o projeto e propostas anonimizadas de melhoria para a Forja. Use ao fim de cada iteração, depois de cada portão e na DU7.
argument-hint: "<descoberta|iteracao-N|F-nn|portao-N>"
---

# Retrospectiva

Escopo: `$ARGUMENTS` (se vazio, pergunte).

1. Rode `python3 .forja/scripts/metricas.py <pasta-de-artefatos>` e guarde a saída.
2. Use o agente `forja-melhoria` com o escopo, a saída das métricas, `forja/melhoria/registro.md`, as retros anteriores e as propostas existentes.
3. Revise com a pessoa (ou com a equipe, se a retro for em reunião):
   - o que funcionou e deve continuar;
   - os padrões encontrados, com a evidência;
   - até 3 ações para o projeto, com dono e prazo;
   - propostas `PM-<nnn>` para a Forja, com a checagem de anonimização.
4. Salve a retro em `forja/melhoria/retros/AAAA-MM-DD-<escopo>.md` e as propostas em `forja/melhoria/propostas/`.
5. Marque as observações tratadas no registro (coluna "Tratada em").
6. Para levar uma proposta à Forja, diga à pessoa: no repositório da Forja, rode a skill `forja-incorporar-melhoria` com o caminho da proposta.
