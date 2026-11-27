#!/usr/bin/env bash
# Instala a Forja.
#
#   ./instalar.sh                  instala (ou atualiza) o kit em ~/.claude
#   ./instalar.sh --link           idem, com links simbólicos (para quem mantém a Forja)
#   ./instalar.sh --projeto <dir>  liga um projeto ao kit já instalado
#   ./instalar.sh --desinstalar    remove o kit de ~/.claude (só os itens forja-*)
#
# Destino: $CLAUDE_HOME (padrão ~/.claude).
set -euo pipefail

DESTINO="${CLAUDE_HOME:-$HOME/.claude}"
ORIGEM="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

erro() { echo "erro: $*" >&2; exit 1; }
info() { echo "forja: $*"; }

instalar_kit() {
  local modo="$1"
  [ -d "$ORIGEM/global" ] || erro "rode a partir do repositório da Forja (não encontrei global/)"
  mkdir -p "$DESTINO/agents" "$DESTINO/skills"

  local item nome alvo
  colocar() { # origem alvo
    rm -rf "$2"
    if [ "$modo" = link ]; then ln -s "$1" "$2"; else cp -R "$1" "$2"; fi
  }

  for item in "$ORIGEM"/global/agentes/hefesto.md "$ORIGEM"/global/agentes/forja-*.md; do
    nome="$(basename "$item")"; alvo="$DESTINO/agents/$nome"
    colocar "$item" "$alvo"
  done
  for item in "$ORIGEM"/global/skills/forja "$ORIGEM"/global/skills/forja-*; do
    nome="$(basename "$item")"; alvo="$DESTINO/skills/$nome"
    colocar "$item" "$alvo"
  done

  # .forja: método, templates e este instalador (para --projeto funcionar sem o repositório)
  rm -rf "$DESTINO/.forja"
  mkdir -p "$DESTINO/.forja"
  colocar "$ORIGEM/global/.forja/HEFESTO.md" "$DESTINO/.forja/HEFESTO.md"
  colocar "$ORIGEM/global/templates" "$DESTINO/.forja/templates"
  colocar "$ORIGEM/global/.forja/guias" "$DESTINO/.forja/guias"
  colocar "$ORIGEM/global/.forja/scripts" "$DESTINO/.forja/scripts"
  colocar "$ORIGEM/global/.forja/padroes" "$DESTINO/.forja/padroes"
  colocar "$ORIGEM/acervo" "$DESTINO/.forja/acervo"
  cp "$ORIGEM/instalar.sh" "$DESTINO/.forja/instalar.sh"
  cp "$ORIGEM/VERSAO" "$DESTINO/.forja/VERSAO"

  info "kit $(cat "$ORIGEM/VERSAO") instalado em $DESTINO ($modo)"
  info "acervo: $(find "$DESTINO/.forja/acervo/" -name item.json | wc -l | tr -d ' ') item(ns); comece com: claude --agent hefesto"
  info "agentes: $(ls "$DESTINO/agents" | grep -c '^forja-\|^hefesto.md$'), skills: $(ls "$DESTINO/skills" | grep -c '^forja'), templates: $(ls "$DESTINO/.forja/templates" | grep -vc '^INDICE.md$')"
}

ligar_projeto() {
  local projeto="$1"
  [ -d "$projeto" ] || erro "pasta não existe: $projeto"
  projeto="$(cd "$projeto" && pwd)"
  [ -f "$DESTINO/.forja/HEFESTO.md" ] || erro "kit não instalado em $DESTINO; rode ./instalar.sh primeiro"
  local gitdir
  gitdir="$(git -C "$projeto" rev-parse --git-dir 2>/dev/null)" || erro "$projeto não é um repositório git"
  case "$gitdir" in /*) ;; *) gitdir="$projeto/$gitdir" ;; esac

  if [ -e "$projeto/.forja" ] && [ ! -L "$projeto/.forja" ]; then
    erro "$projeto/.forja existe e não é um link; remova ou renomeie antes"
  fi
  ln -sfn "$DESTINO/.forja" "$projeto/.forja"

  mkdir -p "$gitdir/info"
  touch "$gitdir/info/exclude"
  local padrao
  for padrao in ".forja" "CLAUDE.local.md"; do
    grep -qxF "$padrao" "$gitdir/info/exclude" || echo "$padrao" >> "$gitdir/info/exclude"
  done

  if [ ! -f "$projeto/CLAUDE.local.md" ]; then
    cp "$DESTINO/.forja/templates/claude-local.md" "$projeto/CLAUDE.local.md"
    info "CLAUDE.local.md criado a partir do template; preencha com a skill forja-iniciar"
  else
    grep -qF "@.forja/HEFESTO.md" "$projeto/CLAUDE.local.md" \
      || info "aviso: CLAUDE.local.md existe mas não importa @.forja/HEFESTO.md"
  fi
  info "projeto ligado: $projeto"
}

desinstalar() {
  rm -rf "$DESTINO"/agents/hefesto.md "$DESTINO"/agents/forja-*.md "$DESTINO"/skills/forja "$DESTINO"/skills/forja-* "$DESTINO/.forja"
  info "kit removido de $DESTINO"
}

case "${1:-}" in
  "")            instalar_kit copia ;;
  --link)        instalar_kit link ;;
  --projeto)     [ -n "${2:-}" ] || erro "uso: $0 --projeto <dir>"; ligar_projeto "$2" ;;
  --desinstalar) desinstalar ;;
  -h|--help)     sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//' ;;
  *)             erro "opção desconhecida: $1 (use --help)" ;;
esac
