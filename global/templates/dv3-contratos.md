# DV3 Contratos e dados: F-01

<!-- Salvar em forja/features/<F>/dv3-contratos.md. -->

## API
`POST /turmas/{turma_id}/inscricoes`

| Resultado | Status | Corpo | Cenário |
|---|---|---|---|
| Confirmada | 201 | `{"inscricao_id": "...", "situacao": "confirmada"}` | Inscrição confirmada |
| Sem vaga | 409 | `{"erro": "turma_sem_vagas", "mensagem": "Turma sem vagas", "lista_espera": true}` | Turma sem vaga |
| Pré-requisito | 422 | `{"erro": "pre_requisito_pendente", "mensagem": "Pré-requisito pendente: Lógica de Programação"}` | Pré-requisito pendente |
| Repetida | 409 | `{"erro": "inscricao_repetida", "mensagem": "Você já está inscrita nesta turma"}` | Inscrição repetida |

## Dados
| Entidade | Campos | Restrições |
|---|---|---|
| inscricao | id, aluna_id, turma_id, criada_em | único (aluna_id, turma_id) |
| turma | id, curso_id, capacidade, inscritos | inscritos <= capacidade |

## Migrações
- `0003_cria_inscricao`: reversível.

## Dados pessoais
- Nenhum campo pessoal novo. Retenção segue a política do produto (D3).
