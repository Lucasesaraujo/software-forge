# language: pt
# Salvar em forja/features/<F>/07-<slug>.feature. O texto acordado no Portão 1 não muda na DV4.

@F-01 @HU-03
Funcionalidade: Inscrição em curso
  Como aluna
  Quero me inscrever numa turma
  Para saber na hora se consegui a vaga

  Contexto:
    Dado que a turma "Python Básico 2027.1" tem capacidade de 20 alunos
    E que a aluna "Maria" está autenticada

  @RF-04
  Cenário: Inscrição confirmada
    Dado que a turma tem 19 inscritos
    Quando Maria se inscreve na turma
    Então a inscrição é confirmada
    E a turma passa a ter 20 inscritos

  @RN-02
  Cenário: Turma sem vaga
    Dado que a turma tem 20 inscritos
    Quando Maria se inscreve na turma
    Então a inscrição é recusada com a mensagem "Turma sem vagas"
    E é oferecida a lista de espera

  @RN-03
  Cenário: Pré-requisito pendente
    Dado que o curso exige "Lógica de Programação" concluído
    E que Maria não concluiu "Lógica de Programação"
    Quando Maria se inscreve na turma
    Então a inscrição é recusada com a mensagem "Pré-requisito pendente: Lógica de Programação"

  @RF-04
  Cenário: Inscrição repetida
    Dado que Maria já está inscrita na turma
    Quando Maria se inscreve na turma
    Então a inscrição é recusada com a mensagem "Você já está inscrita nesta turma"
