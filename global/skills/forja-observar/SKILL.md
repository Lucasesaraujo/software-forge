---
name: forja-observar
description: Registra uma observação sobre o processo da Forja no registro de melhoria do projeto (atrito, retrabalho, retorno de portão, lacuna de guia/template/agente, acerto ou ideia), com etapa, feature, impacto e versão da Forja. Use ao concluir uma etapa, quando algo atrapalhar ou funcionar bem, e sempre que um portão reprovar.
argument-hint: "<tipo> <etapa> <observação>"
---

# Registrar uma observação de processo

Entrada: `$ARGUMENTS` ou o que foi dito na conversa.

1. Abra `forja/melhoria/registro.md`. Se não existir, crie a partir de `.forja/templates/melhoria-registro.md`, apagando as linhas de exemplo.
2. Monte a linha:
   - **Id**: próximo `OBS-<nnn>`.
   - **Data**: hoje.
   - **Versão da Forja**: conteúdo de `.forja/VERSAO`.
   - **Etapa** (D1 a DU7) e **Feature** (`F-xx` ou `(produto)`).
   - **Tipo**: `atrito`, `retrabalho`, `retorno`, `lacuna`, `acerto` ou `ideia`. Na dúvida, pergunte.
   - **Observação**: o fato, numa frase, sem culpar pessoas.
   - **Impacto**: `A` (atrasou dias ou causou retorno de portão), `M` (horas de retrabalho), `B` (incômodo).
   - **Sugestão**: o que mudaria, se houver (no projeto ou na Forja).
   - **Tratada em**: vazio.
3. Acrescente a linha no fim da tabela. Nunca apague nem reescreva linhas existentes.
4. Se já houver 2 ou mais observações abertas do mesmo tipo na mesma etapa, avise que é um padrão e sugira a skill `forja-retro`.
