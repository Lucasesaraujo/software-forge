# Registro de decisões da Forja

## 2026-11-27: implementação do MVP (v0.1.0)

1. **Formato do kit**: agentes e skills no formato nativo do Claude Code (Markdown com frontmatter). No repositório ficam em `global/agentes/` e `global/skills/`; o instalador os coloca em `~/.claude/agents/` e `~/.claude/skills/`, que são as pastas que o Claude Code lê.
2. **Templates dentro de `.forja/`**: na instalação, os templates vão para `~/.claude/.forja/templates/`. Assim o link `.forja` de cada projeto dá acesso ao método e aos templates pelo mesmo caminho relativo.
3. **Ligação do projeto por link simbólico**: `instalar.sh --projeto` cria `.forja` → `~/.claude/.forja` e adiciona `.forja` e `CLAUDE.local.md` ao `.git/info/exclude`. Atualizar o kit atualiza todos os projetos.
4. **Artefatos do projeto em `forja/`** na raiz do repositório do projeto, configurável no `CLAUDE.local.md`. A decisão de versionar essa pasta é de cada projeto.
5. **Um agente por bloco de etapas**, mais um guardião de portões somente leitura. Agentes preparam e checam; portões só são aprovados com o registro da decisão de uma pessoa no papel responsável.
6. **Instalação só toca itens `forja-*`**: agentes e skills de outras origens em `~/.claude` não são alterados.
7. **31 dos 50 templates** no MVP, um por etapa mais os transversais. Os demais estão em `docs/roadmap.md`.

## 2026-11-27: descoberta robusta e melhoria contínua (v0.2.0)

1. **Guias separados dos agentes**: o "como conduzir" de cada etapa fica em `global/.forja/guias/`, não no prompt do agente. Agentes ficam curtos e o guia pode ser melhorado sem mexer no agente.
2. **Equipe da descoberta**: o analista coordena e é dono dos artefatos; facilitador cuida de reuniões e pesquisador da D2. Reunião e pesquisa são habilidades diferentes de escrever requisitos.
3. **Produto com `status.md`**: a descoberta passa a ter histórico, o que permite medir dias por etapa e retornos também antes das features.
4. **Registro de melhoria em Markdown, só acrescenta**: legível por pessoas e por script; nada se apaga, a retro marca o que tratou. Cada linha guarda a versão da Forja para comparar antes e depois de uma mudança.
5. **Métricas sem dependências**: `metricas.py` usa só a biblioteca padrão e lê os artefatos que já existem; nenhum dado extra é exigido.
6. **Duas metades do ciclo**: retro e ações ficam no projeto; o que é do método volta como proposta anonimizada e entra na Forja por PR, com versão e changelog.

## 2026-11-27: orquestração, protótipo e revisores (v0.3.0)

1. **Orquestrador como skill, não agente**: no Claude Code, subagentes não acionam outros subagentes. A skill `/forja` roda na sessão principal, que pode delegar a qualquer agente. As regras de base seguem no `HEFESTO.md`, sempre carregado.
2. **Modo de condução configurável**: `descoberta-completa` atende projetos que querem idear, documentar e prototipar tudo antes de desenvolver; `incremental` continua disponível. O método não muda de etapas: muda quando a DV pode começar.
3. **Portão 1 do conjunto**: no modo descoberta completa, um portão a mais olha o produto inteiro (cobertura dos Must, consistência entre features, protótipo navegável completo) antes de liberar a DV1.
4. **Requisitos e protótipo com agentes próprios**: requisitos (D5 e mudanças) e protótipo (D8) viraram trabalho central na descoberta completa; separá-los do analista e do especificador deixa cada prompt focado.
5. **Revisores separados de quem produz**: spec e design são revisados por agentes que não os escreveram, como a DV6 faz com código.
6. **Protótipo em HTML no repositório**: sem dependências nem contas, versionável e navegável; Figma fica como opção quando o MCP estiver configurado.

## 2026-11-27: Hefesto, equipe de forja e acervo (v0.4.0)

1. **Hefesto é o agente principal**, iniciado com `claude --agent hefesto`. Como sessão principal ele pode acionar subagentes, o que resolve a orquestração. A skill `/forja` continua para sessões comuns, com as mesmas regras de roteamento.
2. **Hefesto forja; a equipe prepara e revisa**: demanda, projetista, revisor de lacunas e arquivista são subagentes; a criação fica com o Hefesto, que tem todas as ferramentas e a conversa com a pessoa.
3. **Uma equipe para os quatro tipos**, com padrões por tipo (`padroes-agente|skill|tool|mcp.md`), em vez de uma equipe por tipo. O que muda entre tipos é o padrão, não o fluxo.
4. **Tool = script ou hook**: as ferramentas nativas do Claude Code não se forjam; forja-se script com README e teste, ou hook com aprovação explícita.
5. **MCP: configurar antes de construir**: oficial > comunidade revisada com versão fixa > servidor próprio.
6. **Aprovação humana antes de forjar** e para qualquer mudança em `settings.json`, hooks ou `.mcp.json`.
7. **Acervo no próprio repositório da Forja**, com versões semver por item, catálogo gerado e instalação sob demanda (`acervo.py usar`), para não carregar todos os itens em toda sessão. O projeto registra o que usa em `.claude/forja-acervo.json`, o que permite atualizar.
8. **Entrada no acervo por PR**: o arquivista cria branch e commit locais; a pessoa abre o PR e faz o merge.
