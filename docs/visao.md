# Visão: como a Forja funciona

A Forja é a fábrica de sistemas agênticos de desenvolvimento. Ela não é usada diretamente num projeto: dela se **forja** o sistema de cada projeto.

```
             ┌──────────────────────────────┐
             │  Forja (este repositório)    │
             │                              │
             │  nucleo/   o que é coringa   │
             │  moldes/   o que se adapta   │
             │  forjar/   como se monta     │
             └──────────────┬───────────────┘
                            │ núcleo vX.Y + perfil do projeto
                            ▼
             ┌──────────────────────────────┐
             │  Sistema agêntico do projeto │  (privado, fora daqui)
             │                              │
             │  núcleo adaptado             │
             │  + agentes de domínio        │
             │  + papéis, stack, normas     │
             └──────────────┬───────────────┘
                            │ aprendizado genérico (DU7), sem contexto
                            ▼
                     PR para o núcleo
```

## As três camadas

| Camada | O que é | Exemplo | Onde vive |
|---|---|---|---|
| Núcleo | Serve para qualquer projeto, sem adaptação | Método SDD, agente revisor de código, template de história de usuário | `nucleo/` |
| Molde | Contrato do que o projeto preenche ou estende | Perfil do projeto (papéis, stack, domínio), molde de agente de domínio | `moldes/` |
| Instância | Núcleo + molde preenchido para um projeto real | Sistema agêntico de um projeto de cliente | Fora deste repositório |

## Critério para algo entrar no núcleo

Um componente entra no núcleo quando:
1. resolve um problema que aparece em mais de um projeto;
2. funciona sem saber nada do projeto, ou recebe o que precisa por um ponto de extensão do molde;
3. tem um exemplo usando o Portal de Cursos.

O que não passa nesse critério fica na instância. Se depois se repetir em outro projeto, é candidato ao núcleo.

## O ciclo

1. **Perfil:** o projeto preenche o molde de perfil (contexto, papéis, stack, normas, restrições de uso de IA).
2. **Forja:** o núcleo é combinado com o perfil, gerando a instância. Agentes de domínio são criados a partir do molde de agente.
3. **Uso:** a equipe trabalha com a instância, seguindo o método.
4. **Retorno:** na etapa DU7 (aprendizado), o que se mostrou genérico volta ao núcleo por PR.
