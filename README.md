# Forja de Software

Método de desenvolvimento apoiado por agentes, seguindo Spec-Driven Development (SDD).

A Forja é genérica: método, agentes, skills, templates e o roadmap de construção da própria Forja. Nada aqui cita um projeto específico. O contexto de cada projeto (papéis, ADRs, roadmap) fica fora deste repositório.

## Estrutura

```
docs/            Documentação do método e registro de decisões
global/          Kit instalado em ~/.claude de cada pessoa
  agentes/       Definições de agentes
  skills/        Skills
  templates/     Templates de artefatos (exemplo neutro: Portal de Cursos)
  .forja/        HEFESTO.md, o método importado pelos projetos
```

Cada projeto usa a Forja localmente com um `CLAUDE.local.md` que importa o método com `@.forja/HEFESTO.md`, ignorado via `.git/info/exclude` no repositório do projeto.

## Visão geral do método

Três fases e quatro portões:

- **Descoberta (D1 a D9)**: do alinhamento de escopo à spec consolidada. Portão 0 (validação do produto) na D6 e Portão 1 (spec) na D9.
- **Desenvolvimento (DV1 a DV7)**: da arquitetura à integração. Portão 2 (código) na DV6.
- **Durabilidade (DU1 a DU7)**: qualidade, segurança, operação e entrega. Portão 3 (entrega) na DU5.

Detalhes em [docs/metodo-v2.1.md](docs/metodo-v2.1.md).
