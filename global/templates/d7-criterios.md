# D7 Critérios de aceite: F-01 Inscrição em curso

<!-- Salvar em forja/features/<F>/07-criterios.md. Os cenários ficam no .feature ao lado. -->

## História
HU-03: Como aluna, quero me inscrever numa turma e saber na hora se consegui a vaga.

## Critérios
| Id | Critério | Regra | Cenário |
|---|---|---|---|
| CA-01 | Com vaga e pré-requisitos, a inscrição é confirmada na hora | RF-04 | Inscrição confirmada |
| CA-02 | Turma lotada recusa a inscrição e oferece a lista de espera | RN-02 | Turma sem vaga |
| CA-03 | Sem pré-requisito, a inscrição é recusada com o motivo | RN-03 | Pré-requisito pendente |
| CA-04 | A mesma aluna não se inscreve duas vezes na mesma turma | RF-04 | Inscrição repetida |

## Fora do escopo desta feature
- Lista de espera em si (HU-04).
