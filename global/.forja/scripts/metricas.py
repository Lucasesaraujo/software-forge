#!/usr/bin/env python3
"""Métricas do processo da Forja num projeto.

Uso: python3 .forja/scripts/metricas.py [pasta-de-artefatos] [--json]

Lê o histórico de cada status.md (produto e features) e o registro de melhoria
(forja/melhoria/registro.md) e calcula: dias por sub-etapa, retornos, pulos,
bloqueios e observações por tipo, etapa e versão da Forja.
Só usa a biblioteca padrão do Python.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ETAPAS = [f"D{i}" for i in range(1, 10)] + [f"DV{i}" for i in range(1, 8)] + [f"DU{i}" for i in range(1, 8)]
ORDEM = {e: i for i, e in enumerate(ETAPAS)}


def linhas_tabela(texto: str, secao: str) -> list[list[str]]:
    """Linhas de dados da primeira tabela após o título `secao`."""
    m = re.search(rf"^##+ {re.escape(secao)}\s*$", texto, re.M)
    if not m:
        return []
    linhas = []
    for linha in texto[m.end():].splitlines():
        linha = linha.strip()
        if not linha:
            if linhas:
                break
            continue
        if not linha.startswith("|"):
            if linhas:
                break
            continue
        celulas = [c.strip() for c in linha.strip("|").split("|")]
        linhas.append(celulas)
    # remove cabeçalho e separador
    return [l for l in linhas[2:] if any(l)]


def sub_etapa(texto: str) -> str | None:
    m = re.search(r"\b(D[1-9]|DV[1-7]|DU[1-7])\b", texto)
    return m.group(1) if m else None


def data(texto: str) -> date | None:
    try:
        return date.fromisoformat(texto.strip()[:10])
    except ValueError:
        return None


def analisar_status(arquivo: Path, hoje: date) -> dict:
    texto = arquivo.read_text(encoding="utf-8")
    historico = linhas_tabela(texto, "Histórico")
    eventos = []
    for l in historico:
        if len(l) < 3:
            continue
        d, de, para = data(l[0]), l[1], l[2]
        if d is None:
            continue
        eventos.append({"data": d, "de": de, "para": para, "motivo": l[3] if len(l) > 3 else ""})

    dias = defaultdict(int)
    retornos, pulos, bloqueios = [], [], 0
    for i, ev in enumerate(eventos):
        fim = eventos[i + 1]["data"] if i + 1 < len(eventos) else hoje
        etapa = sub_etapa(ev["para"])
        if "bloqueada" in ev["para"]:
            bloqueios += 1
            dias["bloqueada"] += (fim - ev["data"]).days
        elif etapa:
            dias[etapa] += (fim - ev["data"]).days
        origem, destino = sub_etapa(ev["de"]), etapa
        if origem and destino and "bloqueada" not in ev["de"] + ev["para"]:
            salto = ORDEM[destino] - ORDEM[origem]
            if salto < 0:
                retornos.append(f"{origem}→{destino}: {ev['motivo']}")
            elif salto > 1 and not (origem == "D6" and destino == "D7"):
                pulos.append(f"{origem}→{destino}: {ev['motivo']}")
    atual = sub_etapa(eventos[-1]["para"]) if eventos else None
    return {
        "nome": arquivo.parent.name,
        "sub_etapa_atual": atual,
        "transicoes": len(eventos),
        "dias_por_etapa": dict(sorted(dias.items(), key=lambda kv: ORDEM.get(kv[0], 99))),
        "retornos": retornos,
        "pulos": pulos,
        "bloqueios": bloqueios,
    }


def analisar_registro(arquivo: Path) -> dict:
    if not arquivo.exists():
        return {"total": 0}
    linhas = []
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        if linha.strip().startswith("| OBS-"):
            linhas.append([c.strip() for c in linha.strip().strip("|").split("|")])
    obs = [l for l in linhas if len(l) >= 8 and l[0].startswith("OBS-")]
    return {
        "total": len(obs),
        "abertas": sum(1 for l in obs if len(l) < 10 or not l[9]),
        "por_tipo": dict(Counter(l[5] for l in obs)),
        "por_etapa": dict(sorted(Counter(l[3] for l in obs).items(), key=lambda kv: ORDEM.get(kv[0], 99))),
        "por_versao": dict(Counter(l[2] for l in obs)),
        "alto_impacto_abertas": [f"{l[0]} ({l[3]}, {l[5]}): {l[6]}" for l in obs if l[7] == "A" and (len(l) < 10 or not l[9])],
    }


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    pasta = Path(args[0] if args else "forja")
    if not pasta.is_dir():
        print(f"pasta de artefatos não encontrada: {pasta}", file=sys.stderr)
        return 1
    hoje = date.fromisoformat(os.environ["FORJA_HOJE"]) if os.environ.get("FORJA_HOJE") else date.today()
    status = []
    for arq in [pasta / "produto" / "status.md", *sorted((pasta / "features").glob("*/status.md"))]:
        if arq.exists():
            status.append(analisar_status(arq, hoje))
    resultado = {"data": hoje.isoformat(), "fluxos": status, "registro": analisar_registro(pasta / "melhoria" / "registro.md")}

    if "--json" in argv:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        return 0

    print(f"# Métricas da Forja ({hoje.isoformat()})\n")
    print("## Fluxos\n")
    print("| Fluxo | Sub-etapa atual | Transições | Dias por etapa | Retornos | Pulos | Bloqueios |")
    print("|---|---|---|---|---|---|---|")
    for s in status:
        dias = ", ".join(f"{k} {v}" for k, v in s["dias_por_etapa"].items()) or "-"
        print(f"| {s['nome']} | {s['sub_etapa_atual'] or '-'} | {s['transicoes']} | {dias} | "
              f"{len(s['retornos'])} | {len(s['pulos'])} | {s['bloqueios']} |")
    detalhes = [(s["nome"], r) for s in status for r in s["retornos"] + s["pulos"]]
    if detalhes:
        print("\n### Retornos e pulos\n")
        for nome, r in detalhes:
            print(f"- {nome}: {r}")
    reg = resultado["registro"]
    print("\n## Registro de melhoria\n")
    print(f"- Observações: {reg['total']} (abertas: {reg.get('abertas', 0)})")
    for chave, titulo in (("por_tipo", "Por tipo"), ("por_etapa", "Por etapa"), ("por_versao", "Por versão da Forja")):
        if reg.get(chave):
            print(f"- {titulo}: " + ", ".join(f"{k} {v}" for k, v in reg[chave].items()))
    if reg.get("alto_impacto_abertas"):
        print("- Alto impacto ainda abertas:")
        for o in reg["alto_impacto_abertas"]:
            print(f"  - {o}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
