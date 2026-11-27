# ADR-0001: Banco de dados relacional para inscrições

<!-- Salvar em forja/arquitetura/adr/ADR-<nnnn>-<slug>.md. ADR aceito não se edita: um novo ADR o substitui. -->

- Situação: proposto | aceito | substituído por ADR-xxxx
- Data: 2026-11-23
- Decisores: líder técnico (Diego, exemplo)
- Requisitos relacionados: RN-02, RNF-02

## Contexto
O controle de vagas (RN-02) exige que duas inscrições simultâneas não ultrapassem o limite da turma.

## Opções consideradas
1. PostgreSQL com transação e bloqueio na linha da turma.
2. Banco de documentos com contador atômico.

## Decisão
Opção 1. Garantias transacionais resolvem RN-02 sem lógica extra na aplicação.

## Consequências
- Positivas: consistência simples de provar em teste.
- Negativas: exige migrações versionadas (ferramenta definida na DV1).
