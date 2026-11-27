# Revisão de spec: F-01 Inscrição em curso

<!-- Salvar em forja/features/<F>/revisao-spec.md. Escrito pelo agente forja-revisor-spec. -->

- Data: 2026-12-10
- Arquivos revisados: `07-criterios.md`, `07-inscricao-em-curso.feature`, `09-spec.md`
- Features comparadas: F-02 (lista de espera)

## Achados
| Severidade | Critério | Arquivo e trecho | Achado | Situação |
|---|---|---|---|---|
| bloqueante | Consistência entre features | F-02 `.feature`: "Turma lotada" | F-01 diz "Turma sem vagas"; usar uma mensagem só | aberto |
| importante | Testabilidade | `09-spec.md`: "confirmação imediata" | Trocar por "em até 1 segundo (RNF-02)" | aberto |
| sugestão | Completude | `.feature` | Cenário para turma com capacidade 0 | aberto |

## DoR
| Item | Situação | Evidência |
|---|---|---|
| Cenários cobrem cada RN | ok | RN-02 e RN-03 têm cenário |
| Sem perguntas em aberto | ok | `09-spec.md` |

## Parecer
Não pronta para o Portão 1 enquanto houver achado bloqueante.
