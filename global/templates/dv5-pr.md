# <F-01> Inscrição em curso

<!-- Descrição de PR ao final da DV5. -->

## Feature
- Spec: `forja/features/F-01-inscricao-em-curso/09-spec.md`
- História e regras: HU-03, RF-04, RN-02, RN-03

## O que muda
- Endpoint `POST /turmas/{id}/inscricoes` conforme `dv3-contratos.md`.
- Tela de inscrição com mensagens das regras.

## Testes
- Cenários Gherkin: 4 de 4 passando.
- Unidade: 3 de 3 passando.
- Nenhum teste pulado ou desativado.

## Para a revisão (DV6)
- Ponto de atenção: controle de concorrência em RN-02.
