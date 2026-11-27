# Roadmap de construção da Forja

## v0.1.0 (MVP) - entregue
- `HEFESTO.md` com o método v2.1 completo: fases, etapas, saídas mínimas, portões, estados da feature, DoR e DoD, Gherkin como ponte.
- 7 agentes: analista, especificador, arquiteto, dev, revisor, durabilidade e guardião de portões.
- 5 skills: `forja-iniciar`, `forja-feature`, `forja-status`, `forja-avancar`, `forja-portao`.
- 31 templates com o exemplo Portal de Cursos (um por etapa, mais os transversais).
- `instalar.sh` (kit em `~/.claude`, ligação de projeto, desinstalação) e verificação em CI.

## v0.2 - completar os 50 templates
Templates previstos no método e ainda não escritos:
- Descoberta: roteiro de entrevista (D2), matriz de stakeholders (D1), mapa de jornada (D2), checklist LGPD (D3), mapa de histórias (D6), glossário do domínio.
- Desenvolvimento: plano de migração de dados (DV3), contrato de evento assíncrono (DV3), checklist de revisão por linguagem (DV6), registro de débito técnico.
- Durabilidade: plano de testes de carga (DU3), relatório de incidente/postmortem (DU4/DU7), plano de comunicação de implantação (DU6), checklist de acessibilidade (DU1), modelo de ameaças detalhado (DU2).
- Gestão: ata de portão, relatório de iteração, matriz de rastreabilidade (RF → HU → cenário → teste), registro de riscos.

## v0.3 - automação
- Script que gera a matriz de rastreabilidade a partir dos identificadores nos artefatos.
- Hook opcional que lembra de atualizar o `status.md` ao fim de uma etapa.
- Skill de retrospectiva (DU7) que propõe mudanças no método sem dados do projeto.

## v1.0 - validação
- Usar a Forja de ponta a ponta numa feature real e ajustar o método com o aprendizado (DU7).
