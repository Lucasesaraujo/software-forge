# D5 Requisitos

<!-- Salvar em forja/produto/05-requisitos.md. Identificadores nunca são renumerados. MoSCoW: Must, Should, Could, Won't. -->

## Requisitos funcionais
| Id | Requisito | MoSCoW | Origem |
|---|---|---|---|
| RF-04 | O aluno se inscreve numa turma com vaga | Must | D4 TO-BE |
| RF-05 | O aluno entra na lista de espera de turma lotada | Should | D2 DOR-01 |

## Requisitos não funcionais
| Id | Requisito | Meta | MoSCoW | Origem |
|---|---|---|---|---|
| RNF-02 | Tempo de resposta da inscrição | p95 < 800 ms com 200 usuários simultâneos | Must | OBJ-01 |
| RNF-03 | Acessibilidade | WCAG 2.1 AA | Must | D3 |

## Regras de negócio
| Id | Regra | Origem |
|---|---|---|
| RN-02 | Uma turma não aceita inscrições acima da capacidade | OBJ-02 |
| RN-03 | O aluno só se inscreve se tiver concluído os pré-requisitos do curso | Secretaria |

## Histórico de mudanças
<!-- Depois do Portão 0, toda mudança é registrada aqui pelo forja-requisitos, com o impacto pela matriz de rastreabilidade. -->
| Data | Requisito | Mudança | Motivo | Pedido por | Aprovado por | Afeta |
|---|---|---|---|---|---|---|
| 2026-12-08 | RN-03 | Pré-requisito pode ser dispensado pela secretaria | Caso real de aluno transferido | Secretaria | Gerente | F-01 (volta para D7) |
