# ADR 0001: a Forja passa a ser uma forja de sistemas agênticos

- **Status:** proposta
- **Data:** 27/11/2026

## Contexto

Até a v2.1, a Forja era um kit de desenvolvimento com agentes: método SDD, agentes, skills e templates instalados em `~/.claude` de cada pessoa, com o contexto do projeto num `CLAUDE.local.md`. Na prática, cada projeto precisa de mais do que o kit genérico: agentes de domínio (normas, sistema legado), papéis ocupados por pessoas concretas, a stack e os padrões do cliente, portões ligados ao contrato. Esse sistema adaptado era montado à mão, e o que se aprendia nele não voltava para a Forja.

## Decisão

A Forja deixa de ser o kit usado diretamente nos projetos e passa a ser a **fábrica** desses kits. Este repositório guarda:

1. **Núcleo**: tudo que serve para qualquer projeto, sem nenhuma referência a projeto real. Método, agentes base, skills base, templates.
2. **Moldes**: o contrato de adaptação, ou seja, o que cada projeto precisa informar e quais pontos do núcleo podem ser estendidos ou substituídos.
3. **Processo de forja**: como montar, a partir do núcleo e de um perfil de projeto, o **sistema agêntico do projeto** (a instância).
4. **Exemplo**: uma instância completa de um projeto fictício (Portal de Cursos), que serve de referência e de teste do processo.

A instância de cada projeto real (por exemplo, o sistema agêntico de um projeto de cliente) **não vive aqui**. Ela fica num lugar do próprio projeto, privado, e referencia a versão do núcleo da qual foi forjada.

O aprendizado volta pelo caminho inverso: o que uma instância provar ser genérico entra no núcleo por PR, sem o contexto do projeto (etapa DU7 do método).

## Consequências

- O que antes estava em `global/` passa a se chamar `nucleo/`, para deixar claro que é a parte que entra em todo projeto.
- O método SDD (fases, portões, DoR/DoD) vira um componente do núcleo. Ele continua sendo o processo padrão, mas uma instância pode ajustar responsáveis e etapas pelos pontos de extensão dos moldes.
- Toda mudança no núcleo precisa ser avaliada pelo efeito nas instâncias já forjadas. Versões do núcleo (`vX.Y`) passam a ter importância prática: cada instância declara de qual versão saiu.
- O repositório continua público. A separação núcleo x instância é o que garante que nenhum dado de cliente entre aqui.

## Em aberto

- **Onde ficam as instâncias:** repositório privado por projeto, pasta dentro do repositório do cliente, ou só local em cada máquina.
- **Como forjar:** uma skill interativa que lê o perfil e gera a instância, ou cópia do núcleo com preenchimento manual guiado pelos moldes.
- **Como atualizar uma instância** quando o núcleo ganha versão nova.
