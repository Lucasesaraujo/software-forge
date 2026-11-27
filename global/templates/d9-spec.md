# D9 Spec consolidada: F-01 Inscrição em curso

<!-- Salvar em forja/features/<F>/09-spec.md. Fonte única para o desenvolvimento. Depois, preparar portao-1.md. -->

## Objetivo
Permitir que a aluna se inscreva numa turma e saiba na hora o resultado (OBJ-01, OBJ-02).

## Escopo
- Dentro: inscrição, validação de vagas e pré-requisitos, mensagens de recusa.
- Fora: lista de espera (HU-04), pagamento.

## Regras
- RN-02: limite de capacidade, garantido mesmo com inscrições simultâneas.
- RN-03: pré-requisitos concluídos.

## Cenários
Ver `07-inscricao-em-curso.feature` (4 cenários) e `07-criterios.md`.

## Telas
Ver `08-prototipo.md`.

## Dados envolvidos
- Aluna (id, nome, e-mail), turma (capacidade, inscritos), histórico de cursos concluídos.
- Dados pessoais: nome e e-mail (base legal: execução de contrato).

## Requisitos não funcionais
- RNF-02: p95 < 800 ms com 200 usuários simultâneos.
- RNF-03: WCAG 2.1 AA.

## Perguntas resolvidas
| Pergunta | Resposta | Quem respondeu |
|---|---|---|
| Inscrição pode ser cancelada? | Sim, mas fica para outra feature | Cliente |

## DoR
Checada em `portao-1.md`.
