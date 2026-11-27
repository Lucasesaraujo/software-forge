# Registro de decisões da Forja

## 2026-11-27: implementação do MVP (v0.1.0)

1. **Formato do kit**: agentes e skills no formato nativo do Claude Code (Markdown com frontmatter). No repositório ficam em `global/agentes/` e `global/skills/`; o instalador os coloca em `~/.claude/agents/` e `~/.claude/skills/`, que são as pastas que o Claude Code lê.
2. **Templates dentro de `.forja/`**: na instalação, os templates vão para `~/.claude/.forja/templates/`. Assim o link `.forja` de cada projeto dá acesso ao método e aos templates pelo mesmo caminho relativo.
3. **Ligação do projeto por link simbólico**: `instalar.sh --projeto` cria `.forja` → `~/.claude/.forja` e adiciona `.forja` e `CLAUDE.local.md` ao `.git/info/exclude`. Atualizar o kit atualiza todos os projetos.
4. **Artefatos do projeto em `forja/`** na raiz do repositório do projeto, configurável no `CLAUDE.local.md`. A decisão de versionar essa pasta é de cada projeto.
5. **Um agente por bloco de etapas**, mais um guardião de portões somente leitura. Agentes preparam e checam; portões só são aprovados com o registro da decisão de uma pessoa no papel responsável.
6. **Instalação só toca itens `forja-*`**: agentes e skills de outras origens em `~/.claude` não são alterados.
7. **31 dos 50 templates** no MVP, um por etapa mais os transversais. Os demais estão em `docs/roadmap.md`.
