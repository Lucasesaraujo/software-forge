---
name: forja-portao
description: Conduz um portão da Forja (0, 1, 2 ou 3) - aciona o agente forja-portao para o parecer com evidências e, quando a pessoa informar a decisão do papel responsável, registra aprovação ou reprovação no arquivo do portão e no status.md. Use quando um portão estiver para ser decidido.
argument-hint: "<0|1|2|3> [F-nn] [aprovado|reprovado por <nome>]"
---

# Conduzir um portão

Argumentos: `$ARGUMENTS`.

1. Identifique o portão e, para os portões 1, 2 e 3, a feature.
2. Use o agente `forja-portao` para gerar o parecer com evidências.
3. Garanta que o arquivo do portão existe (crie do template se não existir):
   - 0: `forja/produto/portao-0.md` (template `portao-0.md`)
   - 1: `forja/features/<F>/portao-1.md` (template `portao-1.md`)
   - 2: `forja/features/<F>/dv6-revisao.md` (template `dv6-revisao.md`)
   - 3: `forja/features/<F>/du5-homologacao.md` (template `du5-homologacao.md`)
   Cole o parecer na seção "Parecer da checagem".
4. **Decisão**: só registre se `$ARGUMENTS` ou a conversa trouxer a decisão explícita de uma pessoa que ocupa o papel responsável (confira no `CLAUDE.local.md`). Registre decisão, data, papel, nome e condições. Se quem decidiu não ocupa o papel responsável, avise e não registre.
5. Atualize o `status.md` da feature (portões 1 a 3):
   - aprovado: avance para o estado seguinte ao portão;
   - reprovado: volte para a sub-etapa indicada na decisão, com o motivo no histórico.
6. Sem decisão, termine dizendo quem precisa decidir e o que o parecer recomenda.
