# Índice de templates da Forja

Todos usam o exemplo neutro **Portal de Cursos**. Copie, substitua o exemplo e remova os comentários `<!-- -->`.

| Template | Etapa | Destino no projeto |
|---|---|---|
| `claude-local.md` | Início | `CLAUDE.local.md` |
| `acordo-dor.md` | Acordos | `forja/acordos/dor.md` |
| `acordo-dod.md` | Acordos | `forja/acordos/dod.md` |
| `status.md` | Toda feature | `forja/features/<F>/status.md` |
| `adr.md` | DV1 e depois | `forja/arquitetura/adr/ADR-<nnnn>-<slug>.md` |
| `status-produto.md` | Descoberta | `forja/produto/status.md` |
| `reuniao-ata.md` | Qualquer reunião | `forja/produto/atas/AAAA-MM-DD-<assunto>.md` |
| `d1-kickoff-pauta.md` | D1 (e outras reuniões) | `forja/produto/00-kickoff-pauta.md` |
| `d1-partes-interessadas.md` | D1 | `forja/produto/01-partes-interessadas.md` |
| `d2-roteiro-entrevista.md` | D2 | `forja/produto/02-roteiro-entrevista.md` |
| `d2-nota-entrevista.md` | D2 | `forja/produto/pesquisa/E-<nn>.md` |
| `d5-glossario.md` | D5 | `forja/produto/glossario.md` |
| `d5-rastreabilidade.md` | D5 a D8 | `forja/produto/rastreabilidade.md` |
| `d8-design-base.md` | D8 (uma vez) | `forja/prototipo/design-base.md` |
| `d8-prototipo-base.html` | D8 | `forja/prototipo/index.html` e telas |
| `revisao-spec.md` | D9 | `forja/features/<F>/revisao-spec.md` |
| `revisao-design.md` | D8 e D9 | `forja/features/<F>/revisao-design.md` |
| `portao-1-conjunto.md` | Portão 1 do conjunto | `forja/produto/portao-1-conjunto.md` |
| `encomenda-catalogo.md` | Encomendas | `forja/encomendas/catalogo.md` |
| `encomenda-demanda.md` | Encomendas | `forja/encomendas/EN-<nnn>-<slug>/01-demanda.md` |
| `encomenda-proposta.md` | Encomendas | `forja/encomendas/EN-<nnn>-<slug>/02-proposta.md` |
| `encomenda-criacao.md` | Encomendas | `forja/encomendas/EN-<nnn>-<slug>/03-criacao.md` |
| `encomenda-revisao.md` | Encomendas | `forja/encomendas/EN-<nnn>-<slug>/04-revisao.md` |
| `melhoria-registro.md` | Melhoria contínua | `forja/melhoria/registro.md` |
| `melhoria-retro.md` | Melhoria contínua | `forja/melhoria/retros/AAAA-MM-DD-<escopo>.md` |
| `melhoria-proposta.md` | Melhoria contínua | `forja/melhoria/propostas/PM-<nnn>-<slug>.md` |
| `d1-alinhamento.md` | D1 | `forja/produto/01-alinhamento.md` |
| `d2-pesquisa.md` | D2 (síntese) | `forja/produto/02-pesquisa.md` |
| `d3-sistema-atual.md` | D3 | `forja/produto/03-sistema-atual.md` |
| `d4-processos.md` | D4 | `forja/produto/04-processos.md` |
| `d5-requisitos.md` | D5 | `forja/produto/05-requisitos.md` |
| `d6-backlog.md` | D6 | `forja/produto/06-backlog.md` |
| `portao-0.md` | Portão 0 | `forja/produto/portao-0.md` |
| `d7-criterios.md` | D7 | `forja/features/<F>/07-criterios.md` |
| `d7-cenarios.feature` | D7 | `forja/features/<F>/07-<slug>.feature` |
| `d8-prototipo.md` | D8 | `forja/features/<F>/08-prototipo.md` |
| `d9-spec.md` | D9 | `forja/features/<F>/09-spec.md` |
| `portao-1.md` | Portão 1 | `forja/features/<F>/portao-1.md` |
| `dv1-arquitetura.md` | DV1 | `forja/arquitetura/01-arquitetura.md` |
| `dv2-plano.md` | DV2 | `forja/features/<F>/dv2-plano.md` |
| `dv3-contratos.md` | DV3 | `forja/features/<F>/dv3-contratos.md` |
| `dv4-testes.md` | DV4 | `forja/features/<F>/dv4-testes.md` |
| `dv5-pr.md` | DV5 | descrição do PR |
| `dv6-revisao.md` | DV6, Portão 2 | `forja/features/<F>/dv6-revisao.md` |
| `dv7-integracao.md` | DV7 | `forja/features/<F>/dv7-integracao.md` |
| `du1-qualidade.md` | DU1 | `forja/features/<F>/du1-qualidade.md` |
| `du2-seguranca.md` | DU2 | `forja/features/<F>/du2-seguranca.md` |
| `du3-desempenho.md` | DU3 | `forja/features/<F>/du3-desempenho.md` |
| `du4-operacao.md` | DU4 | `forja/features/<F>/du4-operacao.md` |
| `du5-homologacao.md` | DU5, Portão 3 | `forja/features/<F>/du5-homologacao.md` |
| `du6-producao.md` | DU6 | `forja/features/<F>/du6-producao.md` |
| `du7-aprendizado.md` | DU7 | `forja/features/<F>/du7-aprendizado.md` |

Guias de condução da descoberta: `.forja/guias/`. Padrões para forjar agentes, skills, tools e MCPs: `.forja/padroes/`. Templates previstos para as próximas versões estão em `docs/roadmap.md` do repositório da Forja.
