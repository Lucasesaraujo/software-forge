# Padrões para forjar uma skill do Claude Code

## Quando é uma skill
- Um **procedimento** repetível que a sessão principal executa (passos, checagens, onde gravar), acionado por `/nome` ou automaticamente pela descrição.
- Orquestração de agentes (só a sessão principal aciona subagentes).
- Não é skill: um papel com julgamento e contexto próprio (agente), um cálculo que um script faz melhor (tool).

## Formato
Pasta `.claude/skills/<nome>/` com `SKILL.md` (e arquivos de apoio, se precisar):

```markdown
---
name: <nome-em-kebab-case, igual ao da pasta>
description: <o que faz e quando usar; até ~300 caracteres de preferência, nunca mais de 1024>
argument-hint: "<argumentos esperados>"
---

# <Título>

<passos numerados; use $ARGUMENTS para os argumentos>
```

## Regras
1. **Nome** igual ao da pasta, kebab-case, até 64 caracteres, sem colidir com skills do projeto ou de `~/.claude/skills/`.
2. **Descrição** diz o resultado e o gatilho ("Use quando..."). Evite descrições genéricas que disparem em qualquer pedido.
3. **Passos** verificáveis: cada passo diz o que ler, o que fazer e o que gravar. Pontos de confirmação da pessoa antes de mudanças grandes.
4. **Argumentos**: documente em `argument-hint` e trate o caso sem argumento.
5. Arquivos de apoio (modelos, listas) ficam na pasta da skill e são citados pelo caminho relativo.
6. Skill não guarda segredo; se precisar de credencial, use variável de ambiente e diga qual.
7. Ao fim, a skill diz o que mudou e o próximo passo.

## Casos de teste (obrigatórios na proposta)
- Execução com argumentos típicos e o resultado esperado (arquivos criados ou alterados).
- Execução sem argumentos.
- Um caso de erro (arquivo de entrada ausente, estado inválido) e a mensagem esperada.
