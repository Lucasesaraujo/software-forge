#!/usr/bin/env bash
# Testa global/.forja/scripts/metricas.py com um projeto de exemplo.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
F="$TMP/forja"; mkdir -p "$F/produto" "$F/features/F-01-inscricao" "$F/melhoria"

cat > "$F/produto/status.md" <<'MD'
# Status: produto

## Histórico
| Data | De | Para | Motivo | Por |
|---|---|---|---|---|
| 2026-11-01 | (novo) | descoberta / D1 | início | Analista |
| 2026-11-04 | D1 | D2 | ok | Analista |
| 2026-11-12 | D2 | D3 | ok | Analista |
| 2026-11-14 | D3 | D5 | D4 feita junto com a D3 | Analista |
| 2026-11-20 | D5 | D4 | Portão 0 pediu revisão do TO-BE | Gerente |
| 2026-11-22 | D4 | bloqueada / D4 | cliente indisponível | Analista |
| 2026-11-25 | bloqueada / D4 | D5 | cliente voltou | Analista |
MD
cp "$RAIZ/global/templates/status.md" "$F/features/F-01-inscricao/status.md"
cp "$RAIZ/global/templates/melhoria-registro.md" "$F/melhoria/registro.md"
echo "| OBS-003 | 2026-12-04 | 0.2.0 | D2 | (produto) | lacuna | Faltou pergunta | A | Ajustar roteiro | retro 2026-12-20 |" >> "$F/melhoria/registro.md"

SAIDA="$(FORJA_HOJE=2026-11-27 python3 "$RAIZ/global/.forja/scripts/metricas.py" "$F" --json)"
python3 - "$SAIDA" <<'PY'
import json, sys
r = json.loads(sys.argv[1])
prod, feat = r["fluxos"]
def checar(cond, msg):
    if not cond:
        sys.exit(f"FALHOU: {msg}\n{json.dumps(r, ensure_ascii=False, indent=2)}")
checar(prod["nome"] == "produto" and prod["sub_etapa_atual"] == "D5", "sub-etapa atual do produto")
checar(prod["dias_por_etapa"] == {"D1": 3, "D2": 8, "D3": 2, "D4": 2, "D5": 8, "bloqueada": 3}, "dias por etapa")
checar(len(prod["retornos"]) == 1 and prod["retornos"][0].startswith("D5→D4"), "retornos")
checar(len(prod["pulos"]) == 1 and prod["pulos"][0].startswith("D3→D5"), "pulos")
checar(prod["bloqueios"] == 1, "bloqueios")
checar(feat["sub_etapa_atual"] == "D7" and feat["retornos"] == [], "feature do template")
reg = r["registro"]
checar(reg["total"] == 3 and reg["abertas"] == 2, "contagem do registro")
checar(reg["por_tipo"] == {"acerto": 1, "lacuna": 2}, "observações por tipo")
checar(reg["alto_impacto_abertas"] == [], "alto impacto aberto (OBS-003 está tratada)")
PY
FORJA_HOJE=2026-11-27 python3 "$RAIZ/global/.forja/scripts/metricas.py" "$F" | grep -q "^| produto | D5 |" || { echo "FALHOU: saída em Markdown"; exit 1; }
python3 "$RAIZ/global/.forja/scripts/metricas.py" "$TMP/nao-existe" 2>/dev/null && { echo "FALHOU: aceitou pasta inexistente"; exit 1; }
echo "ok: métricas"
