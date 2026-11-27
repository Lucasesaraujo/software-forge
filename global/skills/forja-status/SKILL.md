---
name: forja-status
description: Mostra o estado da Forja no projeto - etapa atual do produto (D1 a D6, Portão 0) e, para cada feature, estado, sub-etapa, próximo portão e pendências. Use para saber onde as coisas estão.
argument-hint: "[F-nn]"
---

# Status da Forja

Se `$ARGUMENTS` trouxer uma feature (`F-nn`), mostre só ela, com o histórico completo.

Caso contrário:

1. **Produto**: verifique quais de `forja/produto/01` a `06` existem e se ainda têm conteúdo do exemplo (procure por "Portal de Cursos"). Leia `portao-0.md` para a decisão.
2. **Arquitetura**: diga se `forja/arquitetura/01-arquitetura.md` existe e quantos ADRs há (por situação).
3. **Features**: para cada `forja/features/*/status.md`, extraia estado, sub-etapa, data da última transição e bloqueios.
4. Responda com uma tabela:

   | Feature | Estado | Sub-etapa | Próximo portão | Desde | Pendências |

   Ordene por estado (bloqueadas primeiro, depois da mais atrasada no fluxo para a mais avançada).
5. Aponte inconsistências: arquivo de etapa posterior à sub-etapa registrada, estado que não corresponde à sub-etapa, portão marcado como aprovado sem nome e data de quem aprovou.

Não altere arquivos.
