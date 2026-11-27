# Changelog

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
