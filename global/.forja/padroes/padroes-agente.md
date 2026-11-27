# Padrões para forjar um agente (subagente do Claude Code)

## Quando é um agente
- Um **papel** com julgamento próprio, que trabalha várias etapas sozinho e devolve um resultado (analisar, revisar, especificar).
- Precisa de contexto isolado (lê muito e devolve pouco) ou de permissões diferentes da sessão principal.
- Não é agente: um procedimento fixo que a sessão principal segue (skill), um cálculo determinístico (tool) ou acesso a um sistema externo (MCP).

## Formato
Arquivo `.claude/agents/<nome>.md` no projeto (ou `global/agentes/` na Forja):

```markdown
---
name: <nome-em-kebab-case>
description: <o que faz e QUANDO usar, em uma ou duas frases; é isso que decide quando ele é acionado>
tools: <lista mínima, separada por vírgula>
---

<prompt de sistema>
```

## Regras
1. **Nome**: kebab-case, prefixo do domínio (`gira-`, `forja-`), sem colidir com agentes existentes no projeto ou em `~/.claude/agents/`.
2. **Descrição**: começa pelo papel, diz o que entrega e termina com "Use quando...". Concreta o bastante para não disparar em pedidos de outro agente.
3. **Ferramentas mínimas**: revisor e checador não têm `Write`/`Edit` (ou só escrevem o próprio parecer). `Bash` só se precisar rodar algo; `WebFetch`/`WebSearch` só se precisar da web. Ferramentas MCP pelo nome completo (`mcp__<servidor>__<ferramenta>`).
4. **Prompt**, nesta ordem: quem é e o que segue (`.forja/HEFESTO.md`, `CLAUDE.local.md`); escopo (o que é e o que não é dele); entradas (arquivos que lê); passo a passo; formato da saída e onde grava; regras e "não faça"; como registra observações (`forja-observar`).
5. **Sem segredos** e sem dados pessoais no prompt.
6. **Subagente não aciona subagente**: se o papel precisa coordenar outros, ele é uma skill de orquestração, não um agente.
7. Tamanho: o necessário para agir sem perguntar o óbvio; conhecimento longo vai para um guia em arquivo que o agente lê.

## Casos de teste (obrigatórios na proposta)
- 2 pedidos que **devem** acionar o agente e o resultado esperado.
- 1 pedido parecido que **não deve** acioná-lo (vai para outro agente ou skill).
- 1 situação de falta de informação: o agente deve perguntar, não inventar.
