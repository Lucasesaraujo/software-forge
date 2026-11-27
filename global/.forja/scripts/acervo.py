#!/usr/bin/env python3
"""Acervo da Forja: listar, buscar, usar e atualizar agentes, skills, ferramentas e MCPs.

Uso: python3 .forja/scripts/acervo.py <comando> [...]  (ver --help)
Só usa a biblioteca padrão. Formato descrito em .forja/padroes/acervo.md.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

TIPOS = {"agente": "agentes", "skill": "skills", "ferramenta": "ferramentas", "mcp": "mcps"}
PASTAS = {v: k for k, v in TIPOS.items()}
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
NOME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TRAVA = Path(".claude") / "forja-acervo.json"


class Erro(Exception):
    pass


def localizar_acervo(arg: str | None) -> Path:
    candidatos = [arg, os.environ.get("FORJA_ACERVO")]
    aqui = Path(__file__).resolve().parent
    candidatos += [str(aqui.parent / "acervo"), str(aqui.parent.parent.parent / "acervo")]
    for c in candidatos:
        if c and Path(c).is_dir():
            return Path(c)
    raise Erro("acervo não encontrado; use --acervo <dir> ou FORJA_ACERVO")


def versao_tupla(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def carregar_itens(acervo: Path) -> dict[str, dict]:
    itens = {}
    for pasta_tipo, tipo in PASTAS.items():
        for arq in sorted((acervo / pasta_tipo).glob("*/item.json")):
            dados = json.loads(arq.read_text(encoding="utf-8"))
            dados["_dir"] = arq.parent
            dados["_id"] = f"{pasta_tipo}/{arq.parent.name}"
            itens[dados["_id"]] = dados
    return itens


def validar_item(item: dict) -> list[str]:
    erros, d, ident = [], item["_dir"], item["_id"]
    for campo in ("nome", "tipo", "versao", "descricao", "etiquetas", "arquivos", "historico"):
        if campo not in item:
            erros.append(f"{ident}: falta '{campo}'")
    if erros:
        return erros
    if item["nome"] != d.name:
        erros.append(f"{ident}: nome '{item['nome']}' difere da pasta")
    if not NOME.match(item["nome"]):
        erros.append(f"{ident}: nome deve ser kebab-case")
    if item["tipo"] not in TIPOS or TIPOS[item["tipo"]] != d.parent.name:
        erros.append(f"{ident}: tipo '{item['tipo']}' não bate com a pasta {d.parent.name}/")
    if not SEMVER.match(item["versao"]):
        erros.append(f"{ident}: versao deve ser semver")
    if not item["historico"] or item["historico"][-1].get("versao") != item["versao"]:
        erros.append(f"{ident}: última entrada do historico deve ser a versão atual")
    for a in item["arquivos"]:
        if not (d / a).exists():
            erros.append(f"{ident}: arquivo listado não existe: {a}")
    if item["tipo"] == "mcp":
        cfg = d / "mcp.json"
        if not cfg.exists():
            erros.append(f"{ident}: MCP sem mcp.json")
        else:
            servidores = json.loads(cfg.read_text(encoding="utf-8")).get("mcpServers", {})
            if not servidores:
                erros.append(f"{ident}: mcp.json sem mcpServers")
    return erros


def cmd_listar(a, itens):
    for i in itens.values():
        if a.tipo and i["tipo"] != a.tipo:
            continue
        print(f"{i['_id']:40} {i['versao']:8} {i['descricao']}")
    return 0


def cmd_buscar(a, itens):
    termos = [t.lower() for t in a.termos]
    achados = []
    for i in itens.values():
        texto = " ".join([i["nome"], i["descricao"], " ".join(i.get("etiquetas", [])), " ".join(i.get("etapas", []))]).lower()
        pontos = sum(texto.count(t) for t in termos)
        if pontos:
            achados.append((pontos, i))
    for _, i in sorted(achados, key=lambda x: -x[0]):
        print(f"{i['_id']:40} {i['versao']:8} {i['descricao']}")
    if not achados:
        print("nada encontrado")
    return 0


def obter(itens, ident):
    if ident not in itens:
        raise Erro(f"item não encontrado: {ident} (use <tipo-plural>/<nome>, ex.: agentes/analista-concorrencia)")
    return itens[ident]


def cmd_mostrar(a, itens):
    i = obter(itens, a.item)
    print(json.dumps({k: v for k, v in i.items() if not k.startswith("_")}, ensure_ascii=False, indent=2))
    return 0


def ler_trava(projeto: Path) -> dict:
    arq = projeto / TRAVA
    return json.loads(arq.read_text(encoding="utf-8")) if arq.exists() else {"itens": {}}


def gravar_trava(projeto: Path, trava: dict) -> None:
    arq = projeto / TRAVA
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(trava, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def instalar_item(i: dict, projeto: Path) -> list[str]:
    d, nome, tipo, feitos = i["_dir"], i["nome"], i["tipo"], []
    if tipo == "agente":
        destino = projeto / ".claude" / "agents"
        destino.mkdir(parents=True, exist_ok=True)
        for a in i["arquivos"]:
            shutil.copy2(d / a, destino / Path(a).name)
            feitos.append(str((destino / Path(a).name).relative_to(projeto)))
    elif tipo in ("skill", "ferramenta"):
        destino = projeto / ".claude" / ("skills" if tipo == "skill" else "ferramentas") / nome
        destino.mkdir(parents=True, exist_ok=True)
        for a in i["arquivos"]:
            alvo = destino / a
            alvo.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(d / a, alvo)
            feitos.append(str(alvo.relative_to(projeto)))
    elif tipo == "mcp":
        novos = json.loads((d / "mcp.json").read_text(encoding="utf-8"))["mcpServers"]
        arq = projeto / ".mcp.json"
        atual = json.loads(arq.read_text(encoding="utf-8")) if arq.exists() else {}
        servidores = atual.setdefault("mcpServers", {})
        for chave, cfg in novos.items():
            if chave in servidores and servidores[chave] != cfg:
                feitos.append(f".mcp.json: servidor '{chave}' substituído pela versão do acervo")
            servidores[chave] = cfg
        arq.write_text(json.dumps(atual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        feitos.append(".mcp.json")
        extras = [a for a in i["arquivos"] if a not in ("mcp.json", "README.md")]
        if extras:
            destino = projeto / ".claude" / "ferramentas" / f"mcp-{nome}"
            for a in extras:
                alvo = destino / a
                alvo.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(d / a, alvo)
                feitos.append(str(alvo.relative_to(projeto)))
    return feitos


def cmd_usar(a, itens):
    projeto = Path(a.projeto).resolve()
    if not projeto.is_dir():
        raise Erro(f"projeto não existe: {projeto}")
    trava = ler_trava(projeto)
    fila, vistos = [a.item], set()
    while fila:
        ident = fila.pop(0)
        if ident in vistos:
            continue
        vistos.add(ident)
        i = obter(itens, ident)
        fila += i.get("requer", [])
        for f in instalar_item(i, projeto):
            print(f"  {f}")
        trava["itens"][ident] = {"versao": i["versao"], "origem": "acervo"}
        print(f"usado: {ident} {i['versao']}")
        for p in i.get("parametros", []):
            print(f"  parâmetro: {p['nome']} ({p.get('onde', 'CLAUDE.local.md')}){' obrigatório' if p.get('obrigatorio') else ''}")
        for v in i.get("variaveis_ambiente", []):
            print(f"  variável de ambiente necessária: {v}")
    gravar_trava(projeto, trava)
    return 0


def cmd_atualizar(a, itens):
    projeto = Path(a.projeto).resolve()
    trava = ler_trava(projeto)
    pendentes = []
    for ident, info in sorted(trava["itens"].items()):
        if ident not in itens:
            print(f"{ident}: não está no acervo (item local)")
            continue
        nova = itens[ident]["versao"]
        if versao_tupla(nova) > versao_tupla(info["versao"]):
            maior = versao_tupla(nova)[0] > versao_tupla(info["versao"])[0]
            print(f"{ident}: {info['versao']} → {nova}{'  (MAJOR: revise antes)' if maior else ''}")
            pendentes.append((ident, maior))
        else:
            print(f"{ident}: em dia ({info['versao']})")
    if a.aplicar:
        for ident, maior in pendentes:
            if maior and not a.incluir_major:
                print(f"pulado {ident} (mudança major; use --incluir-major)")
                continue
            instalar_item(itens[ident], projeto)
            trava["itens"][ident]["versao"] = itens[ident]["versao"]
            print(f"atualizado: {ident}")
        gravar_trava(projeto, trava)
    return 0


def cmd_registrar(a, itens):
    if not SEMVER.match(a.versao):
        raise Erro("versão deve ser semver")
    projeto = Path(a.projeto).resolve()
    trava = ler_trava(projeto)
    trava["itens"][a.item] = {"versao": a.versao, "origem": "acervo"}
    gravar_trava(projeto, trava)
    print(f"registrado: {a.item} {a.versao}")
    return 0


def cmd_catalogar(a, itens):
    acervo = localizar_acervo(a.acervo)
    erros = [e for i in itens.values() for e in validar_item(i)]
    nomes = [i["nome"] for i in itens.values()]
    erros += [f"nome repetido no acervo: {n}" for n in sorted({n for n in nomes if nomes.count(n) > 1})]
    if erros:
        for e in erros:
            print(f"erro: {e}", file=sys.stderr)
        return 1
    linhas = ["# Catálogo do acervo", "", "<!-- Gerado por acervo.py catalogar. Não edite à mão. -->", ""]
    for pasta_tipo, tipo in PASTAS.items():
        do_tipo = [i for i in itens.values() if i["tipo"] == tipo]
        titulo = {"agentes": "Agentes", "skills": "Skills", "ferramentas": "Ferramentas", "mcps": "MCPs"}[pasta_tipo]
        linhas += [f"## {titulo} ({len(do_tipo)})", ""]
        if not do_tipo:
            linhas += ["(nenhum ainda)", ""]
            continue
        linhas += ["| Item | Versão | Descrição | Etapas | Etiquetas |", "|---|---|---|---|---|"]
        for i in sorted(do_tipo, key=lambda x: x["nome"]):
            linhas.append(f"| `{i['_id']}` | {i['versao']} | {i['descricao']} | {', '.join(i.get('etapas', []))} | {', '.join(i['etiquetas'])} |")
        linhas.append("")
    novo = "\n".join(linhas)
    destino = acervo / "CATALOGO.md"
    if a.checar:
        if not destino.exists() or destino.read_text(encoding="utf-8") != novo:
            print("CATALOGO.md desatualizado: rode acervo.py catalogar", file=sys.stderr)
            return 1
        print(f"ok: {len(itens)} itens no acervo, catálogo em dia")
        return 0
    destino.write_text(novo, encoding="utf-8")
    print(f"catálogo gerado: {len(itens)} item(ns)")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--acervo", help="pasta do acervo (padrão: FORJA_ACERVO ou a instalada)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("listar"); s.add_argument("--tipo", choices=TIPOS)
    s = sub.add_parser("buscar"); s.add_argument("termos", nargs="+")
    s = sub.add_parser("mostrar"); s.add_argument("item")
    s = sub.add_parser("usar"); s.add_argument("item"); s.add_argument("--projeto", default=".")
    s = sub.add_parser("atualizar"); s.add_argument("--projeto", default="."); s.add_argument("--aplicar", action="store_true"); s.add_argument("--incluir-major", action="store_true")
    s = sub.add_parser("registrar"); s.add_argument("item"); s.add_argument("versao"); s.add_argument("--projeto", default=".")
    s = sub.add_parser("catalogar"); s.add_argument("--checar", action="store_true", help="só confere se o CATALOGO.md está em dia")
    a = p.parse_args(argv)
    try:
        itens = carregar_itens(localizar_acervo(a.acervo))
        return globals()[f"cmd_{a.cmd}"](a, itens)
    except (Erro, json.JSONDecodeError) as e:
        print(f"erro: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
