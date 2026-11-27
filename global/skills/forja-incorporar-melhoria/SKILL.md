---
name: forja-incorporar-melhoria
description: No repositório da Forja, incorpora uma proposta de melhoria (PM) vinda da retro de um projeto - confere a anonimização, aplica a mudança em método, guia, template, agente ou skill, registra em docs/melhorias, atualiza CHANGELOG e VERSAO e roda as verificações. Use quando uma proposta PM for aceita para virar parte da Forja.
argument-hint: "<caminho da proposta PM>"
---

# Incorporar uma melhoria na Forja

Rode **no repositório da Forja** (precisa existir `global/` e `docs/melhorias/`). Proposta: `$ARGUMENTS`.

1. Leia a proposta e `docs/processo-de-melhoria.md`.
2. **Anonimização**: procure nomes próprios, nomes de clientes, sistemas internos, e-mails, links e números que identifiquem um projeto. Se encontrar, pare e peça para reescrever. Nada de projeto entra no repositório da Forja.
3. **Avaliação**: a mudança resolve o problema descrito? Conflita com alguma regra do `HEFESTO.md` ou com outra melhoria em `docs/melhorias/`? Se houver dúvida de mérito, apresente os prós e contras e peça a decisão de quem mantém a Forja.
4. **Aplicação**: faça a menor mudança que resolve, no alvo indicado. Se mudar regra do método, atualize também `docs/metodo-v2.1.md` (ou a versão vigente) e o `HEFESTO.md`.
5. **Registro**: copie a proposta para `docs/melhorias/PM-<nnn>-<slug>.md` com situação `aceita`, a versão em que entrou e o que foi alterado. Acrescente a linha no índice `docs/melhorias/README.md`.
6. **Versão**: incremente `VERSAO` (patch para texto e templates, minor para agente, skill ou regra nova, major para mudança de fases ou portões) e escreva a entrada no `CHANGELOG.md`.
7. Rode `python3 scripts/verificar.py` e `bash scripts/testar-instalacao.sh`. Só termine com os dois verdes.
8. Diga que os projetos recebem a mudança rodando `./instalar.sh` de novo, e que as próximas observações já sairão com a versão nova, o que permite comparar antes e depois na próxima retro.
