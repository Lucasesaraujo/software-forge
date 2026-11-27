---
name: forja-avancar
description: Leva uma feature da Forja para a próxima sub-etapa depois de checar a saída mínima da etapa atual, atualizando estado e histórico no status.md. Não atravessa portões sem decisão registrada. Use ao concluir uma etapa.
argument-hint: "<F-nn> [justificativa para pular]"
---

# Avançar uma feature

Argumentos: `$ARGUMENTS`.

1. Leia `forja/features/<F-nn>-*/status.md` e a tabela de estados em `.forja/HEFESTO.md`.
2. Confira a **saída mínima** da sub-etapa atual (tabelas de etapas no HEFESTO). Para cada item, indique `ok` ou `falta`, com o arquivo de evidência. Se algo faltar, não avance: liste o que falta.
3. Se a próxima transição atravessa um portão (D9 → DV2, DV6 → DV7, DU5 → DU6), exija o registro de aprovação no arquivo do portão (`portao-1.md`, `dv6-revisao.md`, `du5-homologacao.md`) com decisão, data, papel e nome. Sem isso, sugira a skill `forja-portao` e pare.
4. Se a feature estiver em DV2, confirme a DoR de novo (`forja/acordos/dor.md`).
5. Determine a próxima sub-etapa e o estado correspondente. Pular sub-etapa só com justificativa em `$ARGUMENTS`; registre-a no histórico.
6. Atualize o `status.md`: campos de estado e sub-etapa, e uma linha nova no histórico (`data | de | para | motivo | por`).
7. Se a próxima sub-etapa tem template, copie-o para a pasta da feature (se ainda não existir) e diga qual agente conduz a etapa.
