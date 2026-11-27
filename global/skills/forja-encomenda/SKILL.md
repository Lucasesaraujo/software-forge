---
name: forja-encomenda
description: Conduz uma encomenda à Forja - da demanda à proposta, aprovação, criação pelo Hefesto, revisão de lacunas e arquivamento no acervo - para obter um agente, skill, tool ou MCP que o projeto precisa. Use quando faltar um agente ou ferramenta, ou quando a pessoa pedir para criar um.
argument-hint: "<o que é preciso> | EN-nnn [continuar]"
---

# Encomenda à Forja

Entrada: `$ARGUMENTS`. Se for `EN-nnn`, continue a encomenda existente a partir da situação registrada em `forja/encomendas/catalogo.md`.

Situações: `demanda` → `proposta` → `aguardando aprovação` → `aprovada` → `forjando` → `em revisão` → (`correção` → `em revisão`) → `pronto` → `no acervo` | `só no projeto`. Também `reaproveitado` (algo existente resolveu) e `cancelada`.

1. **Abrir**: crie `forja/encomendas/` e `forja/encomendas/catalogo.md` (template `encomenda-catalogo.md`, sem as linhas de exemplo) se não existirem. Próximo id `EN-<nnn>`, pasta `forja/encomendas/EN-<nnn>-<slug>/`.
2. **Demanda**: agente `forja-demanda` → `01-demanda.md`. Se a classificação for **usar**, rode `python3 .forja/scripts/acervo.py usar <item> --projeto .`, marque `reaproveitado` e termine.
3. **Proposta**: agente `forja-projetista` → `02-proposta.md`.
4. **Aprovação**: mostre à pessoa um resumo da proposta (tipo, nome, o que faz, permissões, destino, riscos) e peça aprovação. Registre na proposta quem aprovou e quando. Mudança em `settings.json`, hooks ou `.mcp.json` precisa ser aprovada explicitamente. Sem aprovação, pare em `aguardando aprovação`.
5. **Forja**: o Hefesto cria os arquivos (se a sessão não for o Hefesto, siga o ofício "Forjar agentes e ferramentas" de `~/.claude/agents/hefesto.md`) → `03-criacao.md`.
6. **Revisão**: agente `forja-revisor-lacunas` → `04-revisao.md`. Com bloqueantes, volte ao passo 5 (no máximo 3 voltas; depois, leve à pessoa o que está travando).
7. **Destino**:
   - genérico: agente `forja-arquivista` leva ao acervo da Forja (branch e commit locais no repositório da Forja; o PR é da pessoa) → `no acervo`;
   - do projeto: `só no projeto`.
8. **Fecho**: diga o que foi forjado, como usar (comando, agente ou skill), variáveis de ambiente necessárias, e registre uma observação com a skill `forja-observar` sobre a encomenda.
