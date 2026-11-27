# Forja de Sistemas Agênticos

Fábrica de sistemas agênticos para desenvolvimento de software, seguindo Spec-Driven Development (SDD).

A Forja guarda a parte **coringa**, que entra em todo projeto, e o processo para adaptá-la. De cada projeto real se forja um sistema agêntico próprio (agentes, skills, método e contexto do projeto), que vive fora deste repositório. Veja [docs/visao.md](docs/visao.md).

## Estrutura

```
nucleo/      O que é coringa: método, agentes, skills e templates base
moldes/      O que cada projeto preenche ou estende
forjar/      Como montar o sistema agêntico de um projeto
exemplos/    Instâncias de projetos fictícios (Portal de Cursos)
docs/        Visão, método e decisões (ADRs)
```

## O método

O processo padrão do núcleo tem três fases e quatro portões:

- **Descoberta (D1 a D9)**: do alinhamento de escopo à spec consolidada. Portão 0 (validação do produto) na D6 e Portão 1 (spec) na D9.
- **Desenvolvimento (DV1 a DV7)**: da arquitetura à integração. Portão 2 (código) na DV6.
- **Durabilidade (DU1 a DU7)**: qualidade, segurança, operação e entrega. Portão 3 (entrega) na DU5.

Detalhes em [docs/metodo-v2.1.md](docs/metodo-v2.1.md).

## Decisões

- [ADR 0001](docs/decisoes/0001-forja-de-sistemas-agenticos.md): a Forja passa a ser uma forja de sistemas agênticos.
