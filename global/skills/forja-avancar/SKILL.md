---
name: forja-avancar
description: Leva o produto (D1 a D6) ou uma feature da Forja para a próxima sub-etapa depois de checar a saída mínima da etapa atual, atualizando estado e histórico no status.md. Não atravessa portões sem decisão registrada. Use ao concluir uma etapa.
argument-hint: "<produto|F-nn> [justificativa para pular]"
---

# Avançar uma feature

Argumentos: `$ARGUMENTS`.

1. Leia o `status.md` do fluxo (`forja/produto/status.md` para `produto`, `forja/features/<F-nn>-*/status.md` para uma feature) e a tabela de estados em `.forja/HEFESTO.md`.
2. Confira a **saída mínima** da sub-etapa atual (tabelas de etapas no HEFESTO) e, se houver guia em `.forja/guias/`, o checklist de qualidade dele. Para cada item, indique `ok` ou `falta`, com o arquivo de evidência. Se algo faltar, não avance: liste o que falta.
3. Se a próxima transição atravessa um portão (D6 → fim da descoberta do produto, D9 → DV2, DV6 → DV7, DU5 → DU6), exija o registro de aprovação no arquivo do portão (`portao-0.md`, `portao-1.md`, `dv6-revisao.md`, `du5-homologacao.md`) com decisão, data, papel e nome. Sem isso, sugira a skill `forja-portao` e pare.
4. Se a feature estiver em DV2, confirme a DoR de novo (`forja/acordos/dor.md`).
   No modo `descoberta-completa` (ver `CLAUDE.local.md`), a transição `pronta` → DV2 também exige o Portão 1 do conjunto aprovado em `forja/produto/portao-1-conjunto.md`.
5. Determine a próxima sub-etapa e o estado correspondente. Pular sub-etapa só com justificativa em `$ARGUMENTS`; registre-a no histórico.
6. Atualize o `status.md`: campos de estado e sub-etapa, e uma linha nova no histórico (`data | de | para | motivo | por`).
7. Se a próxima sub-etapa tem template, copie-o para a pasta da feature (se ainda não existir) e diga qual agente conduz a etapa.
8. Se a transição pulou sub-etapa ou voltou, registre uma observação do tipo `retorno` (ou `atrito`, para pulo) com a skill `forja-observar`.
9. Pergunte, em uma linha, se algo da etapa concluída deve ir para o registro de melhoria (o que atrapalhou ou funcionou) e registre com a skill `forja-observar`.
