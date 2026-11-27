# <Nome do projeto>

<!-- Copie para a raiz do projeto como CLAUDE.local.md. Este arquivo fica fora do git (.git/info/exclude). -->

@.forja/HEFESTO.md

## Projeto
Portal de Cursos: portal para alunos se inscreverem em cursos livres de uma escola de formação.

- Página do projeto (contexto, ADRs, roadmap): <link>
- Pasta de artefatos: `forja/`
- Repositório: <link>

## Condução
- Modo de condução: `descoberta-completa`
  <!-- descoberta-completa: todo o escopo passa por especificação e protótipo (D7 a D9) e pelo Portão 1 do conjunto antes de qualquer desenvolvimento. incremental: cada feature segue para o desenvolvimento assim que passa no próprio Portão 1. -->
- Escopo da descoberta: todas as histórias Must
- Protótipo: HTML em `forja/prototipo/` (Figma: não)
- Ponto de entrada: `claude --agent hefesto` (ou `/forja` numa sessão comum)
- Repositório da Forja: `~/software-forge` <!-- usado pelo forja-arquivista para levar itens ao acervo -->

## Papéis
| Papel | Pessoa |
|---|---|
| Coordenação | Ana (exemplo) |
| Gerente | Bruno (exemplo) |
| Líder de design | Carla (exemplo) |
| Líder técnico | Diego (exemplo) |
| Devs | Elisa, Fábio (exemplo) |
| Cliente | Escola Exemplo, representada por Gabriela (exemplo) |

## Convenções do projeto
- Stack e comandos: ver `forja/arquitetura/01-arquitetura.md`.
- Rodar testes: `<comando>`
- Framework BDD: `<ex.: Cucumber, Behave, pytest-bdd>`
