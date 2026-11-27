# Forja v2.1: método e decisões (23/11/2026)

## Separação método x projeto
- A Forja (método, agentes, skills, templates e o roadmap de construção da Forja) é genérica e não cita nenhum projeto.
- Cada projeto tem uma página própria com contexto, papéis (quem ocupa cada papel), ADRs e o próprio roadmap.
- No kit: `global/` (agentes, skills, `.forja/HEFESTO.md` e templates) e `projetos/<nome>/CLAUDE.local.md`, que importa o método com `@.forja/HEFESTO.md`.

## Estrutura do método

### Descoberta
- D1 alinhamento e escopo
- D2 pesquisa com usuários
- D3 sistema atual e normas
- D4 processos AS-IS e TO-BE
- D5 requisitos (RF, RNF, RN, MoSCoW)
- D6 épicos, histórias e backlog (**Portão 0**)
- D7 critérios de aceite e Gherkin
- D8 prototipação e UX
- D9 spec consolidada (**Portão 1**)

D1 a D6 no nível do produto; D7 a D9 por feature.

### Desenvolvimento
- DV1 arquitetura e fundações
- DV2 refinamento e planejamento
- DV3 contratos e dados
- DV4 testes primeiro
- DV5 implementação
- DV6 revisão de código (**Portão 2**)
- DV7 integração e homologação

### Durabilidade
- DU1 qualidade
- DU2 segurança e privacidade
- DU3 desempenho
- DU4 observabilidade e operação
- DU5 homologação com o cliente (**Portão 3**)
- DU6 produção
- DU7 aprendizado

## Portões por papel
| Portão | O que valida | Responsáveis |
|---|---|---|
| 0 | Produto | Coordenação e gerente, com o cliente |
| 1 | Spec | Líder de design e gerente |
| 2 | Código | Líder técnico ou dev designado, com revisão de outro dev |
| 3 | Entrega | Líder técnico e gerente, após aceite do cliente |

## Acordos da equipe
- Definition of Ready (Portão 1, DV2).
- Definition of Done (Portão 2).

## Templates
50 templates com exemplo neutro (Portal de Cursos).

## Mudanças em relação à versão anterior
- Novo Portão 0 (validação de produto) antes do ciclo por feature.
- DoR e DoD formalizados como acordos da equipe.
- Gherkin como ponte: escrito na D7, automatizado na DV4, usado na homologação (DU5).
- Estados da feature mapeados para sub-etapas; `status.md` registra também a sub-etapa.
- Papéis em vez de nomes nas etapas.
