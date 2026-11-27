# D4 Processos AS-IS e TO-BE

<!-- Salvar em forja/produto/04-processos.md. Use Mermaid para os fluxos. -->

## AS-IS: inscrição
```mermaid
flowchart LR
  A[Aluno envia e-mail] --> B[Secretaria confere planilha] --> C{Tem vaga?}
  C -- sim --> D[Responde confirmando em até 3 dias]
  C -- não --> E[Responde recusando]
```

## TO-BE: inscrição
```mermaid
flowchart LR
  A[Aluno escolhe turma no portal] --> B{Tem vaga e pré-requisito?}
  B -- sim --> C[Inscrição confirmada na hora]
  B -- sem vaga --> D[Oferece lista de espera]
  B -- sem pré-requisito --> E[Explica o que falta]
```

## Ganhos esperados
| Processo | Antes | Depois | Objetivo |
|---|---|---|---|
| Confirmação | até 3 dias | < 1 minuto | OBJ-01 |
