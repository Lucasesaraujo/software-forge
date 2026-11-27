# HEFESTO: o método da Forja (v2.1, kit 0.4)

A Forja de Software é a oficina; **Hefesto** é o seu agente principal. Ele conduz o método com a equipe de agentes e forja, com a equipe de forja, os agentes, skills, tools e MCPs que cada projeto precisa, guardando no **acervo** o que for reaproveitável.

Este arquivo é importado pelo `CLAUDE.local.md` de cada projeto (`@.forja/HEFESTO.md`). Ele diz como trabalhar; o contexto do projeto (papéis, ADRs, roadmap, onde ficam os artefatos) vem do próprio `CLAUDE.local.md`.

## Princípios

1. **Spec antes de código.** Nenhuma linha de produção é escrita para uma feature que não passou pelo Portão 1.
2. **Testes antes da implementação.** O Gherkin da D7 vira teste automatizado na DV4, antes da DV5.
3. **Portões são decisões humanas.** Agentes preparam evidências e checam critérios; quem aprova é o papel responsável. Nunca marque um portão como aprovado sem o registro explícito da pessoa.
4. **Papéis, não nomes.** O método fala em papéis. Quem ocupa cada papel está no `CLAUDE.local.md` do projeto.
5. **Tudo rastreável.** Requisito (RF/RNF/RN) → história → critério de aceite → teste → código → evidência de homologação. Use os identificadores em todos os artefatos.
6. **O estado mora no `status.md`.** O produto (`forja/produto/status.md`) e cada feature têm um `status.md` com estado e sub-etapa atuais e o histórico de transições. Atualize-o a cada mudança.
7. **O processo aprende.** Cada etapa deixa ao menos uma observação no registro de melhoria; cada ciclo termina numa retrospectiva baseada nesses dados. O que é do método volta para a Forja como proposta anonimizada.

## Orquestração e modos de condução

- **Ponto de entrada**: o agente principal `hefesto`, iniciado com `claude --agent hefesto`. Como sessão principal, ele aciona todos os outros agentes. Numa sessão comum, a skill `forja` (`/forja`) faz o mesmo papel de orquestração: lê o estado, diz onde estamos, propõe o próximo passo e aciona o agente certo. Subagentes não acionam subagentes, por isso a orquestração fica sempre na sessão principal.
- **Modo de condução** (no `CLAUDE.local.md`):
  - `descoberta-completa`: depois do Portão 0, todo o escopo da descoberta (por padrão, as histórias Must) passa por D7 a D9, com protótipo e revisões, e pelo **Portão 1 do conjunto**. Só então começam a DV1 e a DV2. Nenhum código de produção antes disso.
  - `incremental`: cada feature segue para a DV2 assim que passa no próprio Portão 1.
  - Sem indicação, vale `incremental`.

## Onde ficam os artefatos

Por padrão, em `forja/` na raiz do projeto (o `CLAUDE.local.md` pode mudar com `Pasta de artefatos:`):

```
forja/
  produto/                 D1 a D6 (nível do produto)
    status.md              estado, sub-etapa e histórico da descoberta
    00-kickoff-pauta.md
    01-alinhamento.md
    01-partes-interessadas.md
    02-roteiro-entrevista.md
    02-pesquisa.md         síntese
    pesquisa/E-<nn>.md     uma nota por entrevista
    atas/AAAA-MM-DD-*.md   atas de reunião
    03-sistema-atual.md
    04-processos.md
    05-requisitos.md
    06-backlog.md
    glossario.md
    rastreabilidade.md     objetivo → requisito → história → cenário → tela
    portao-0.md
    portao-1-conjunto.md   só no modo descoberta-completa
  prototipo/               D8 (produto inteiro)
    design-base.md
    index.html             mapa navegável das telas
    F-<nn>-<slug>/*.html
  arquitetura/             DV1 e ADRs
    01-arquitetura.md
    adr/ADR-0001-*.md
  acordos/                 DoR e DoD
    dor.md
    dod.md
  features/<id>-<slug>/    D7 a DU7 (por feature)
    status.md
    07-criterios.md
    07-<slug>.feature
    08-prototipo.md
    09-spec.md
    revisao-design.md
    revisao-spec.md
    portao-1.md
    dv2-plano.md
    dv3-contratos.md
    dv4-testes.md
    dv6-revisao.md         (Portão 2)
    dv7-integracao.md
    du1-qualidade.md
    du2-seguranca.md
    du3-desempenho.md
    du4-operacao.md
    du5-homologacao.md     (Portão 3)
    du6-producao.md
    du7-aprendizado.md
  melhoria/                sistema de melhoria do processo
    registro.md            observações (OBS-nnn), só acrescenta
    retros/AAAA-MM-DD-*.md retrospectivas
    propostas/PM-<nnn>-*.md propostas anonimizadas para a Forja
```

Os templates de cada artefato ficam em `.forja/templates/` (ver `.forja/templates/INDICE.md`). Copie o template, troque o exemplo do Portal de Cursos pelo conteúdo real e remova as instruções entre `<!-- -->`.

Cada etapa da descoberta tem um **guia de condução** em `.forja/guias/` (`d1-alinhamento.md` a `d6-backlog.md`): como preparar, perguntas-chave, passo a passo, checklist de qualidade e armadilhas. Siga o guia e mostre o checklist preenchido antes de concluir a etapa.

## Fases e etapas

### Descoberta (nível do produto: D1 a D6)

| Etapa | Objetivo | Artefato | Saída mínima |
|---|---|---|---|
| D1 alinhamento e escopo | Kickoff: problema, objetivos, partes interessadas, limites do escopo | `produto/01-alinhamento.md`, `01-partes-interessadas.md`, ata do kickoff | Objetivos mensuráveis, decisores e o que está fora do escopo |
| D2 pesquisa com usuários | Entender quem usa e o que precisa | `produto/02-roteiro-entrevista.md`, `pesquisa/E-xx.md`, `02-pesquisa.md` | Personas e dores com evidência; suposições da D1 revisitadas |
| D3 sistema atual e normas | O que existe hoje, integrações, leis e normas aplicáveis | `produto/03-sistema-atual.md` | Inventário e restrições normativas (ex.: LGPD) |
| D4 processos AS-IS e TO-BE | Como é e como será | `produto/04-processos.md` | Fluxos atual e futuro, com ganhos |
| D5 requisitos | RF, RNF e RN com prioridade MoSCoW, rastreáveis | `produto/05-requisitos.md`, `glossario.md`, `rastreabilidade.md` | Requisitos identificados (RF-01, RNF-01, RN-01) |
| D6 épicos, histórias e backlog | Quebrar em entregas | `produto/06-backlog.md` | Backlog priorizado. **Portão 0** |

### Descoberta (por feature: D7 a D9)

| Etapa | Objetivo | Artefato | Saída mínima |
|---|---|---|---|
| D7 critérios de aceite e Gherkin | Definir "pronto" do ponto de vista do usuário | `07-criterios.md`, `07-<slug>.feature` | Cenários Gherkin cobrindo caminho feliz, erros e regras de negócio |
| D8 prototipação e UX | Telas e fluxos | `08-prototipo.md`, telas em `prototipo/`, `revisao-design.md` | Protótipo navegável com todos os estados, revisado |
| D9 spec consolidada | Uma fonte única para desenvolver | `09-spec.md`, `revisao-spec.md` | Spec revisada sem bloqueantes. **Portão 1** |

### Desenvolvimento (DV1 a DV7)

| Etapa | Objetivo | Artefato | Saída mínima |
|---|---|---|---|
| DV1 arquitetura e fundações | Decisões estruturais do produto (uma vez, revisitada quando preciso) | `arquitetura/01-arquitetura.md`, ADRs | Visão de componentes, stack, ADRs |
| DV2 refinamento e planejamento | Checar a DoR e quebrar em tarefas | `dv2-plano.md` | DoR atendida e tarefas estimadas |
| DV3 contratos e dados | APIs, eventos, modelo de dados | `dv3-contratos.md` | Contratos versionados e migrações planejadas |
| DV4 testes primeiro | Automatizar o Gherkin e os testes de unidade antes do código | `dv4-testes.md` | Testes escritos e falhando pelo motivo certo |
| DV5 implementação | Fazer os testes passarem | código | Testes verdes, sem pular nem desativar testes |
| DV6 revisão de código | Revisão por outra pessoa contra a DoD | `dv6-revisao.md` | DoD atendida. **Portão 2** |
| DV7 integração e homologação | Integrar e validar em ambiente de homologação | `dv7-integracao.md` | Feature integrada e cenários Gherkin passando em homologação |

### Durabilidade (DU1 a DU7)

| Etapa | Objetivo | Artefato | Saída mínima |
|---|---|---|---|
| DU1 qualidade | Cobertura, regressão, testes exploratórios | `du1-qualidade.md` | Relatório de qualidade |
| DU2 segurança e privacidade | Ameaças, dados pessoais, dependências | `du2-seguranca.md` | Riscos tratados ou aceitos por quem pode aceitar |
| DU3 desempenho | Metas de RNF medidas | `du3-desempenho.md` | Medições contra as metas |
| DU4 observabilidade e operação | Logs, métricas, alertas, runbook | `du4-operacao.md` | Runbook e alertas configurados |
| DU5 homologação com o cliente | Cliente valida usando os cenários Gherkin | `du5-homologacao.md` | Aceite registrado. **Portão 3** |
| DU6 produção | Implantar com plano de retorno | `du6-producao.md` | Implantação registrada |
| DU7 aprendizado | Medir resultado e retrospectiva | `du7-aprendizado.md` | Lições e ajustes no método ou no backlog |

## Portões

| Portão | Etapa | O que valida | Responsáveis |
|---|---|---|---|
| 0 | D6 | Produto: problema, requisitos e backlog fazem sentido para o cliente | Coordenação e gerente, com o cliente |
| 1 | D9 | Spec da feature: completa, testável, prototipada, revisada | Líder de design e gerente |
| 1c | fim da D9 do conjunto | Conjunto (modo descoberta-completa): todo o escopo especificado e prototipado, consistente entre features | Líder de design e gerente (recomendado com o cliente) |
| 2 | DV6 | Código: DoD atendida, revisado por outro dev | Líder técnico ou dev designado, com revisão de outro dev |
| 3 | DU5 | Entrega: cliente aceitou | Líder técnico e gerente, após aceite do cliente |

Regras:
- Um portão só é aprovado com o registro no arquivo `portao-N.md` (`portao-1-conjunto.md` para o 1c) (ou `dv6-revisao.md` e `du5-homologacao.md`): decisão, data, papel e nome de quem aprovou.
- Reprovado volta para a etapa indicada no registro, e o `status.md` registra o retorno.
- O agente `forja-portao` checa os critérios e prepara o parecer; não aprova.

## Acordos da equipe

- **Definition of Ready (DoR)**: checada no Portão 1 e de novo na DV2. Feature sem DoR não entra em desenvolvimento.
- **Definition of Done (DoD)**: checada no Portão 2.
- Os textos ficam em `forja/acordos/dor.md` e `forja/acordos/dod.md` (templates `acordo-dor.md` e `acordo-dod.md`). A equipe pode ajustar; o método exige que existam.

## Estados do produto

O `forja/produto/status.md` usa os estados `descoberta` (D1 a D6) e `bloqueado`, e depois:
- modo `incremental`: `validado` (Portão 0 aprovado; as features seguem pelos próprios `status.md`);
- modo `descoberta-completa`: `em-especificacao` (Portão 0 aprovado, features do escopo em D7 a D9), `especificado` (Portão 1 do conjunto aprovado) e `em-desenvolvimento`. As sub-etapas e as regras de transição são as mesmas das features.

## Estados da feature

Cada estado corresponde a uma faixa de sub-etapas. O `status.md` registra o estado **e** a sub-etapa.

| Estado | Sub-etapas | Entra quando |
|---|---|---|
| `rascunho` | D7, D8 | A feature sai do backlog aprovado no Portão 0 |
| `em-spec` | D9 | Critérios e protótipo prontos |
| `pronta` | DV2 | Portão 1 aprovado (no modo descoberta-completa, fica aqui até o Portão 1 do conjunto) |
| `em-desenvolvimento` | DV3, DV4, DV5 | DoR confirmada na DV2 |
| `em-revisao` | DV6 | Testes verdes, PR aberto |
| `em-integracao` | DV7 | Portão 2 aprovado |
| `em-durabilidade` | DU1, DU2, DU3, DU4 | Integrada em homologação |
| `em-homologacao` | DU5 | Relatórios DU1 a DU4 concluídos |
| `aceita` | DU6 | Portão 3 aprovado |
| `em-producao` | DU7 | Implantada |
| `concluida` | (fim) | Aprendizado registrado |
| `bloqueada` | (qualquer) | Impedimento registrado; guarda a sub-etapa onde parou |

Transições válidas: sempre para a sub-etapa seguinte, para `bloqueada` (e de volta para onde parou) ou para trás quando um portão reprova. Pular sub-etapa exige justificativa registrada no histórico do `status.md`.

## Gherkin como ponte

1. **D7**: escrito em português (`# language: pt`), com `Funcionalidade`, `Cenário`, `Dado`, `Quando`, `Então`. Cada cenário referencia a história e as regras (`@HU-03 @RN-02`).
2. **DV4**: os mesmos cenários são automatizados sem alterar o texto acordado. Se o texto precisar mudar, volta para a D7 e reabre o Portão 1.
3. **DU5**: o cliente homologa executando ou acompanhando os mesmos cenários.

## Agentes e skills

| Agente | Etapas |
|---|---|
| `hefesto` | Agente principal: conduz o método e forja agentes e ferramentas |
| `forja-analista` | D1 a D6 (coordena a descoberta e é dono dos artefatos) |
| `forja-facilitador` | Reuniões da descoberta: kickoff, oficinas, validações; pauta e ata |
| `forja-pesquisador` | D2: roteiro, entrevistas, síntese |
| `forja-requisitos` | D5, glossário, rastreabilidade e mudanças de requisito |
| `forja-especificador` | D7 e D9 (coordena a feature na descoberta) |
| `forja-prototipador` | D8: base de design e protótipos HTML navegáveis |
| `forja-revisor-design` | Revisão de protótipos (D8, antes do Portão 1) |
| `forja-revisor-spec` | Revisão de critérios, Gherkin e spec (D9, antes do Portão 1) |
| `forja-arquiteto` | DV1 a DV3 |
| `forja-dev` | DV4 e DV5 |
| `forja-revisor` | DV6 |
| `forja-durabilidade` | DV7, DU1 a DU4, DU6 e DU7 |
| `forja-portao` | Checagem dos portões 0 a 3 (somente leitura) |
| `forja-melhoria` | Retrospectivas: cruza métricas e observações e gera ações e propostas |
| `forja-demanda` | Encomendas: entende a necessidade e procura no acervo |
| `forja-projetista` | Encomendas: escolhe o tipo e desenha o item |
| `forja-revisor-lacunas` | Encomendas: revisa o que foi forjado |
| `forja-arquivista` | Encomendas: leva itens genéricos ao acervo |

| Skill | Para quê |
|---|---|
| `forja` | Orquestrar: onde estamos, próximo passo, acionar o agente certo |
| `forja-iniciar` | Criar a estrutura `forja/`, acordos e o `CLAUDE.local.md` do projeto |
| `forja-feature` | Abrir uma feature nova a partir de uma história do backlog |
| `forja-status` | Mostrar onde cada feature está e o que falta |
| `forja-avancar` | Levar uma feature para a próxima sub-etapa, checando a saída mínima |
| `forja-portao` | Preparar o parecer de um portão (0, 1, 1c, 2, 3) e registrar a decisão humana |
| `forja-registrar-reuniao` | Levar ata, notas ou transcrição de uma reunião ou entrevista para os artefatos |
| `forja-observar` | Registrar uma observação de processo no registro de melhoria |
| `forja-retro` | Retrospectiva de iteração, fase, feature ou portão, com métricas |
| `forja-encomenda` | Encomendar um agente, skill, tool ou MCP à equipe de forja |
| `forja-incorporar-melhoria` | No repositório da Forja: incorporar uma proposta aceita e gerar nova versão |

## Forjar agentes e ferramentas

Quando um projeto precisa de um agente, skill, tool ou MCP que não existe, abre-se uma **encomenda** (skill `forja-encomenda`, ou pedindo ao Hefesto):

| Passo | Quem | Artefato em `forja/encomendas/EN-<nnn>-<slug>/` |
|---|---|---|
| Demanda e busca no acervo | `forja-demanda` | `01-demanda.md` |
| Tipo e desenho, com casos de teste | `forja-projetista` | `02-proposta.md` |
| Aprovação | a pessoa | registro na proposta |
| Forja | `hefesto` | arquivos no projeto, `03-criacao.md` |
| Revisão de lacunas | `forja-revisor-lacunas` | `04-revisao.md` |
| Arquivamento no acervo (se genérico) | `forja-arquivista` | item em `acervo/` no repositório da Forja |

- Padrões de cada tipo: `.forja/padroes/padroes-agente.md`, `padroes-skill.md`, `padroes-tool.md`, `padroes-mcp.md`; acervo: `.forja/padroes/acervo.md`.
- Validação: `python3 .forja/scripts/validar_claude.py .` (formato, nomes, permissões, segredos, MCP).
- **Acervo**: biblioteca incremental e versionada no repositório da Forja (`acervo/`), instalada em `.forja/acervo/`. Use com `python3 .forja/scripts/acervo.py buscar|usar|atualizar`. O projeto registra o que usa em `.claude/forja-acervo.json`.
- Reaproveite antes de criar; nunca grave segredos; nada do projeto entra no acervo; hooks, `settings.json` e `.mcp.json` só com aprovação registrada.
- Lacunas recorrentes apontadas pelo revisor viram observações de melhoria e, com o tempo, melhores padrões.

## Melhoria contínua

O ciclo de melhoria usa os dados que o próprio processo já produz:

1. **Observar**: ao concluir cada etapa, quando um portão decide, e sempre que algo atrapalhar ou funcionar bem, registre uma linha em `forja/melhoria/registro.md` (skill `forja-observar`). Tipos: `atrito`, `retrabalho`, `retorno`, `lacuna`, `acerto`, `ideia`. Cada linha guarda a versão da Forja em uso.
2. **Medir**: `python3 .forja/scripts/metricas.py forja` lê os históricos dos `status.md` e o registro e calcula dias por etapa, retornos, pulos, bloqueios e observações por tipo, etapa e versão.
3. **Retrospectiva**: ao fim de cada iteração, depois de cada portão e na DU7 (skill `forja-retro`, agente `forja-melhoria`). Confere se as ações da retro anterior surtiram efeito, encontra padrões (2 ou mais observações do mesmo tipo na mesma etapa, etapas mais longas, retornos de portão) e gera até 3 ações.
4. **Separar**: o que é do projeto vira ação na retro; o que é do método vira proposta `PM-nnn`, anonimizada.
5. **Incorporar**: no repositório da Forja, a skill `forja-incorporar-melhoria` aplica a proposta aceita, registra em `docs/melhorias/`, gera nova versão e o `CHANGELOG`.
6. **Atualizar e comparar**: `./instalar.sh` leva a versão nova aos projetos. Como as observações guardam a versão, a retro seguinte compara antes e depois.

Regras: o registro só cresce (nunca apague linhas; marque "Tratada em"); observação descreve fatos, não culpa pessoas; nada de dado do projeto vai para a Forja.

## Regras de conduta para o Claude

- Antes de trabalhar numa feature, leia o `status.md` dela e diga em que estado e sub-etapa está.
- Não produza artefato de uma etapa posterior à sub-etapa atual sem avisar que isso é antecipar trabalho.
- Não escreva código de produção para feature que não esteja em `em-desenvolvimento` ou depois. No modo `descoberta-completa`, nada de DV1 em diante antes do Portão 1 do conjunto.
- Na DV5, nunca pule, desative ou apague testes para ficar verde.
- Ao terminar uma etapa, atualize o `status.md` (estado, sub-etapa e linha no histórico) e registre ao menos uma observação no registro de melhoria.
- Antes de começar uma etapa, leia o registro de melhoria e a última retro, e aplique as ações e os acertos que valem para ela.
- Use os nomes dos papéis; consulte o `CLAUDE.local.md` para saber quem ocupa cada papel.
- Nada do projeto volta para o repositório da Forja. Melhorias no método seguem o ciclo de melhoria contínua acima.
