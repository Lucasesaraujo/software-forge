---
name: forja-feature
description: Abre uma feature nova na Forja a partir de uma ou mais histórias do backlog aprovado no Portão 0 - cria a pasta forja/features/<id>-<slug>/ com status.md em rascunho/D7. Use quando for começar a especificar uma história.
argument-hint: "<HU-xx [nome curto] | lote>"
---

# Abrir uma feature

Argumentos: `$ARGUMENTS` (ex.: `HU-03 inscricao em curso`). Com `lote`, abra uma feature para cada história do escopo da descoberta (modo `descoberta-completa`: as histórias definidas no `CLAUDE.local.md`, por padrão todas as Must), na ordem do backlog, agrupando histórias que formam uma mesma funcionalidade; mostre a lista proposta antes de criar.

1. Leia `forja/produto/portao-0.md`. Se o Portão 0 não estiver aprovado, avise que a feature começaria antes da validação do produto e pergunte se deve seguir. Se seguir, registre isso no histórico do `status.md`.
2. Localize as histórias informadas em `forja/produto/06-backlog.md`. Se não existirem, liste as histórias disponíveis e pare.
3. Defina o identificador `F-<nn>` (próximo número livre em `forja/features/`) e o slug (minúsculas, sem acento, com hífens).
4. Crie `forja/features/F-<nn>-<slug>/` e copie `.forja/templates/status.md` para dentro, preenchendo:
   - feature, histórias, RF e RN relacionados;
   - estado `rascunho`, sub-etapa `D7`;
   - primeira linha do histórico com a data de hoje: "Feature aberta a partir de HU-xx".
5. Copie `.forja/templates/d7-criterios.md` para `07-criterios.md` e `.forja/templates/d7-cenarios.feature` para `07-<slug>.feature`.
6. Responda com o caminho criado e o próximo passo: "D7 com o agente `forja-especificador`".
