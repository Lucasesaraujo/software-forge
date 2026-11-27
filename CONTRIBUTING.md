# Como contribuir com a Forja

## Fluxo de branches (Gitflow)

| Branch | Papel | Sai de | Volta para |
|---|---|---|---|
| `main` | Versões publicadas da Forja. Cada merge recebe uma tag. | — | — |
| `develop` | Integração do que vai para a próxima versão. | `main` | — |
| `feature/<assunto>` | Uma mudança: novo agente, skill, template, ajuste no método. | `develop` | `develop` |
| `release/vX.Y` | Preparação de uma versão: revisão final, changelog. | `develop` | `main` e `develop` |
| `hotfix/<assunto>` | Correção urgente numa versão publicada. | `main` | `main` e `develop` |

Regras:
- Ninguém commita direto na `main` ou na `develop`. Toda mudança entra por pull request.
- Uma branch trata um assunto só. Nome em minúsculas, com hífens: `feature/agente-analise-legado`.
- Antes de abrir o PR, atualize a branch com a `develop` (rebase).
- Versões seguem `vMAJOR.MINOR` do método (ex.: `v2.1`). Mudança na estrutura de fases ou portões sobe o MAJOR; o resto sobe o MINOR.

## Commits

Seguimos [Conventional Commits](https://www.conventionalcommits.org/pt-br/), com a descrição em português.

```
<tipo>(<escopo>): <resumo no imperativo, até 72 caracteres>

<corpo: o que muda e por quê. Contexto que não está no diff:
o problema, a decisão tomada, alternativas descartadas.>

<rodapé: referências, BREAKING CHANGE, coautoria>
```

**Tipos**
- `feat`: novo agente, skill, template ou etapa do método
- `fix`: correção de algo que estava errado
- `docs`: documentação que não muda o comportamento do kit
- `refactor`: reorganização sem mudar o resultado
- `chore`: manutenção do repositório (gitignore, CI, configuração)

**Escopos**: `metodo`, `agentes`, `skills`, `templates`, `repo`.

**Exemplo**

```
feat(agentes): adiciona agente de análise de sistema legado

Apoia a etapa D3 (sistema atual e normas) fazendo engenharia
reversa a partir do esquema do banco e da documentação, sem acesso
a dados reais. Sem ele, o mapeamento do legado era manual e ficava
fora do status.md.

O agente gera um rascunho do template D3-sistema-atual para revisão
humana; não decide escopo.
```

Boas práticas:
- Resumo diz o que o commit faz, não o que você fez ("adiciona", não "adicionei").
- O corpo é obrigatório quando a razão da mudança não é óbvia pelo diff.
- Commits pequenos e coesos. Se o corpo precisa de "e também", provavelmente são dois commits.

## Pull requests

- Título no mesmo formato do commit principal.
- Descrição com: o que muda, por quê, como revisar, e etapa ou portão do método afetado.
- Pelo menos uma revisão antes do merge.

## O que não entra aqui

O repositório é público. Contexto de projetos (clientes, nomes da equipe, ADRs, documentos de contrato) fica fora. A pasta `projetos/` e os arquivos `CLAUDE.local.md` são ignorados pelo `.gitignore`. Antes de commitar um agente ou template, confira se ele não cita nenhum projeto real.
