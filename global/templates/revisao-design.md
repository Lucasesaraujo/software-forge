# Revisão de design: F-01 Inscrição em curso

<!-- Salvar em forja/features/<F>/revisao-design.md. Escrito pelo agente forja-revisor-design. -->

- Data: 2026-12-10
- Telas revisadas: `forja/prototipo/F-01-inscricao/detalhe-turma.html`
- Personas consideradas: PER-01

## Cobertura de cenários
| Cenário | Tela e estado | Situação |
|---|---|---|
| Inscrição confirmada | detalhe-turma / sucesso | ok |
| Turma sem vaga | detalhe-turma / sem-vaga | ok |
| Pré-requisito pendente | (falta) | falta |

## Achados
| Severidade | Critério | Tela e elemento | Achado | Situação |
|---|---|---|---|---|
| bloqueante | Cobertura | detalhe-turma | Sem estado para pré-requisito pendente (RN-03) | aberto |
| importante | Prevenção de erro | botão "Inscrever-me" | Mostrar pré-requisitos antes do clique | aberto |
| sugestão | Consistência | cabeçalho | Usar "Meus cursos" também na F-02 | aberto |

## Acessibilidade (WCAG 2.1 AA)
| Item | Situação |
|---|---|
| Contraste | ok |
| Foco visível | ok |
| Mensagens com `aria-live` ou `role="alert"` | ok |

## Parecer
Não pronto para o Portão 1 enquanto houver achado bloqueante.
