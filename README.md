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
  .forja/        HEFESTO.md (o método), guias/ de condução e scripts/ (métricas)
scripts/         Verificação do kit e teste do instalador
instalar.sh      Instala o kit e liga projetos
```

## Instalação

```bash
git clone https://github.com/Lucasesaraujo/software-forge.git
cd software-forge
./instalar.sh                     # kit em ~/.claude (use --link se for manter a Forja)
./instalar.sh --projeto ~/meu-app # liga um projeto: .forja, CLAUDE.local.md e .git/info/exclude
```

Depois, dentro do projeto, rode a skill `/forja-iniciar` no Claude Code para preencher o `CLAUDE.local.md` (papéis, página do projeto) e criar a pasta `forja/` com os acordos. Daí em diante, o ponto de entrada é `/forja`: ele diz onde o projeto está, propõe o próximo passo e chama o agente certo (também aceita pedidos livres, como `/forja quero entender os stakeholders`).

No `CLAUDE.local.md`, o **modo de condução** escolhe entre `descoberta-completa` (especificar e prototipar todo o escopo, com o Portão 1 do conjunto, antes de desenvolver) e `incremental` (cada feature segue ao desenvolvimento quando passa no próprio Portão 1).

| No repositório | Instalado em |
|---|---|
| `global/agentes/forja-*.md` | `~/.claude/agents/` |
| `global/skills/forja-*/` | `~/.claude/skills/` |
| `global/.forja/HEFESTO.md` | `~/.claude/.forja/HEFESTO.md` |
| `global/templates/` | `~/.claude/.forja/templates/` |
| `global/.forja/guias/` e `scripts/` | `~/.claude/.forja/guias/` e `scripts/` |

## Agentes e skills

| Agente | Etapas |
|---|---|
| `forja-analista` | D1 a D6 (coordena a descoberta) |
| `forja-facilitador` | Kickoff, oficinas e atas da descoberta |
| `forja-pesquisador` | D2: entrevistas e síntese |
| `forja-requisitos` | D5, glossário, rastreabilidade e mudanças de requisito |
| `forja-especificador` | D7 e D9 |
| `forja-prototipador` | D8: base de design e protótipos HTML navegáveis |
| `forja-revisor-design` | Revisão dos protótipos |
| `forja-revisor-spec` | Revisão de critérios, Gherkin e spec |
| `forja-arquiteto` | DV1 a DV3 |
| `forja-dev` | DV4 e DV5 (testes primeiro) |
| `forja-revisor` | DV6 |
| `forja-durabilidade` | DV7, DU1 a DU4, DU6, DU7 |
| `forja-portao` | Checagem dos portões (somente leitura) |
| `forja-melhoria` | Retrospectivas com métricas e propostas de melhoria |

Skills: `forja` (orquestrador), `forja-iniciar`, `forja-feature`, `forja-status`, `forja-avancar`, `forja-portao`, `forja-registrar-reuniao`, `forja-observar`, `forja-retro`, `forja-incorporar-melhoria`.

## Melhoria contínua

Durante o uso, cada etapa e cada portão deixam observações em `forja/melhoria/registro.md` no projeto. As retrospectivas (`/forja-retro`) cruzam essas observações com as métricas dos históricos (`metricas.py`), geram ações para o projeto e propostas anonimizadas para a Forja, que entram aqui com `/forja-incorporar-melhoria` e viram uma nova versão. Detalhes em [docs/processo-de-melhoria.md](docs/processo-de-melhoria.md).

## Verificação

```bash
python3 scripts/verificar.py        # consistência de agentes, skills, templates e referências
bash scripts/testar-instalacao.sh   # instalador num ~/.claude temporário
bash scripts/testar-metricas.sh     # métricas com um projeto de exemplo
```

As três rodam no CI a cada push.

Cada projeto usa a Forja localmente com um `CLAUDE.local.md` que importa o método com `@.forja/HEFESTO.md`, ignorado via `.git/info/exclude` no repositório do projeto.

## Visão geral do método

Três fases e quatro portões:

- **Descoberta (D1 a D9)**: do alinhamento de escopo à spec consolidada. Portão 0 (validação do produto) na D6 e Portão 1 (spec) na D9.
- **Desenvolvimento (DV1 a DV7)**: da arquitetura à integração. Portão 2 (código) na DV6.
- **Durabilidade (DU1 a DU7)**: qualidade, segurança, operação e entrega. Portão 3 (entrega) na DU5.

Detalhes em [docs/metodo-v2.1.md](docs/metodo-v2.1.md) e, no formato que o Claude usa, em [global/.forja/HEFESTO.md](global/.forja/HEFESTO.md). Próximos passos em [docs/roadmap.md](docs/roadmap.md); decisões de implementação em [docs/decisoes.md](docs/decisoes.md).
