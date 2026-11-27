#!/usr/bin/env bash
# Testa o instalador num CLAUDE_HOME e num projeto temporários.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
export CLAUDE_HOME="$TMP/claude"
falha() { echo "FALHOU: $*" >&2; exit 1; }

# Um agente que não é da Forja não pode ser tocado
mkdir -p "$CLAUDE_HOME/agents"; echo "meu" > "$CLAUDE_HOME/agents/meu-agente.md"

for modo in "" --link; do
  "$RAIZ/instalar.sh" $modo >/dev/null
  [ -f "$CLAUDE_HOME/.forja/HEFESTO.md" ] || falha "HEFESTO.md ausente ($modo)"
  [ -f "$CLAUDE_HOME/agents/forja-dev.md" ] || falha "agente ausente ($modo)"
  [ -f "$CLAUDE_HOME/skills/forja-iniciar/SKILL.md" ] || falha "skill ausente ($modo)"
  [ -f "$CLAUDE_HOME/.forja/templates/status.md" ] || falha "templates ausentes ($modo)"
  [ -x "$CLAUDE_HOME/.forja/instalar.sh" ] || falha "instalador não copiado ($modo)"
  [ -f "$CLAUDE_HOME/.forja/guias/d1-alinhamento.md" ] || falha "guias ausentes ($modo)"
  [ -f "$CLAUDE_HOME/.forja/scripts/metricas.py" ] || falha "scripts ausentes ($modo)"
done
"$RAIZ/instalar.sh" >/dev/null   # volta para cópia
[ -L "$CLAUDE_HOME/agents/forja-dev.md" ] && falha "reinstalação em cópia deixou link"
grep -qx meu "$CLAUDE_HOME/agents/meu-agente.md" || falha "agente alheio alterado"

# Ligar projeto (usando o instalador copiado, sem o repositório)
PROJ="$TMP/projeto"; git init -q "$PROJ"
"$CLAUDE_HOME/.forja/instalar.sh" --projeto "$PROJ" >/dev/null
[ -L "$PROJ/.forja" ] || falha ".forja não é link"
[ -f "$PROJ/.forja/HEFESTO.md" ] || falha "link .forja quebrado"
grep -qF "@.forja/HEFESTO.md" "$PROJ/CLAUDE.local.md" || falha "CLAUDE.local.md sem import"
"$CLAUDE_HOME/.forja/instalar.sh" --projeto "$PROJ" >/dev/null   # idempotente
[ "$(grep -cxF .forja "$PROJ/.git/info/exclude")" = 1 ] || falha "exclude duplicado"
[ -z "$(git -C "$PROJ" status --porcelain)" ] || falha "arquivos da Forja aparecem no git do projeto"

# Pasta que não é git
mkdir "$TMP/semgit"
"$RAIZ/instalar.sh" --projeto "$TMP/semgit" 2>/dev/null && falha "aceitou pasta sem git"

"$RAIZ/instalar.sh" --desinstalar >/dev/null
[ -e "$CLAUDE_HOME/.forja" ] && falha "desinstalar deixou .forja"
[ -f "$CLAUDE_HOME/agents/meu-agente.md" ] || falha "desinstalar removeu agente alheio"
echo "ok: instalação, ligação de projeto e desinstalação"
