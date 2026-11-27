# Changelog

## 0.3.0 (2026-11-27)

### Orquestração
- Skill `forja` (`/forja`): ponto de entrada que lê o estado, propõe o próximo passo, aciona o agente certo e roteia pedidos livres. É uma skill porque só a sessão principal do Claude Code aciona subagentes.

### Modo de condução
- `descoberta-completa` (no `CLAUDE.local.md`): todo o escopo passa por especificação, protótipo e revisões antes do desenvolvimento, com o novo **Portão 1 do conjunto** (`portao-1-conjunto.md`). `incremental` mantém o fluxo por feature.
- Estados do produto `em-especificacao`, `especificado` e `em-desenvolvimento`; `forja-feature lote` abre todas as features do escopo.

### Novos agentes
- `forja-requisitos`: D5, glossário, matriz de rastreabilidade e controle de mudanças de requisito.
- `forja-prototipador`: base de design e protótipos HTML navegáveis com todos os estados, ligados aos cenários Gherkin.
- `forja-revisor-design`: cobertura de cenários, heurísticas de Nielsen, WCAG 2.1 AA e consistência entre features.
- `forja-revisor-spec`: completude, ambiguidade, testabilidade, consistência e DoR.

### Templates
- `d5-rastreabilidade.md`, `d8-design-base.md`, `d8-prototipo-base.html`, `revisao-spec.md`, `revisao-design.md`, `portao-1-conjunto.md`; histórico de mudanças em `d5-requisitos.md`; condução no `claude-local.md`.

## 0.2.0 (2026-11-27)

### Descoberta mais robusta
- Guias de condução para D1 a D6 em `global/.forja/guias/` (preparação, perguntas-chave, passo a passo, checklist de qualidade e armadilhas).
- Novos agentes: `forja-facilitador` (kickoff, oficinas, atas) e `forja-pesquisador` (D2). O `forja-analista` passa a coordenar a descoberta e seguir os guias.
- `forja/produto/status.md`: a descoberta tem estado, sub-etapa e histórico como as features.
- Novos templates: pauta de kickoff, matriz de partes interessadas, ata de reunião, roteiro e nota de entrevista, glossário, status do produto.
- Nova skill `forja-registrar-reuniao`: leva ata, notas ou transcrição para os artefatos.

### Melhoria contínua
- Registro de observações (`forja/melhoria/registro.md`) com tipo, impacto e versão da Forja; skill `forja-observar`.
- `metricas.py`: dias por etapa, retornos, pulos, bloqueios e observações por tipo, etapa e versão.
- Retrospectivas com dados: skill `forja-retro` e agente `forja-melhoria`, gerando ações e propostas anonimizadas.
- Skill `forja-incorporar-melhoria`, `docs/processo-de-melhoria.md` e `docs/melhorias/`.
- Todos os agentes registram observações ao concluir etapas; `forja-avancar` e `forja-portao` registram retornos e decisões automaticamente.

## 0.1.0 (2026-11-27)
- MVP: HEFESTO.md, 7 agentes, 5 skills, 31 templates, instalador e verificação.
