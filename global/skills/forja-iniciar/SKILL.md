---
name: forja-iniciar
description: Prepara um projeto para usar a Forja - cria a pasta de artefatos (forja/), os acordos DoR e DoD e o CLAUDE.local.md com papéis, importando o método HEFESTO. Use ao começar um projeto novo com a Forja.
---

# Iniciar um projeto na Forja

1. Confirme que está na raiz de um repositório git (`git rev-parse --show-toplevel`).
2. Verifique se `.forja/HEFESTO.md` existe no projeto. Se não existir, rode `~/.claude/.forja/instalar.sh --projeto .` (ou peça que a pessoa rode `instalar.sh --projeto <caminho>` a partir do repositório da Forja). Esse passo cria o link `.forja` e adiciona `.forja` e `CLAUDE.local.md` ao `.git/info/exclude`.
3. Se `CLAUDE.local.md` ainda não existe, copie `.forja/templates/claude-local.md` para `CLAUDE.local.md` e pergunte à pessoa, de uma vez:
   - nome do projeto e uma frase sobre ele;
   - quem ocupa cada papel (coordenação, gerente, líder de design, líder técnico, devs, cliente);
   - onde fica a página do projeto (contexto, ADRs, roadmap);
   - se a pasta de artefatos deve ser outra que não `forja/`.
   Preencha com as respostas. Papel sem pessoa fica como `(a definir)`.
4. Crie a estrutura (usando a pasta configurada):
   ```
   forja/produto/
   forja/arquitetura/adr/
   forja/acordos/
   forja/features/
   forja/produto/atas/
   forja/produto/pesquisa/
   forja/melhoria/retros/
   forja/melhoria/propostas/
   ```
5. Copie `.forja/templates/acordo-dor.md` para `forja/acordos/dor.md` e `.forja/templates/acordo-dod.md` para `forja/acordos/dod.md`. Diga que a equipe deve revisar os dois acordos.
6. Copie `.forja/templates/status-produto.md` para `forja/produto/status.md`, com o nome do produto, estado `descoberta`, sub-etapa `D1`, a versão de `.forja/VERSAO` e a primeira linha do histórico com a data de hoje.
7. Copie `.forja/templates/melhoria-registro.md` para `forja/melhoria/registro.md` e apague as linhas de exemplo (mantenha o cabeçalho da tabela).
8. Copie `.forja/templates/d1-alinhamento.md` para `forja/produto/01-alinhamento.md` e `.forja/templates/d1-partes-interessadas.md` para `forja/produto/01-partes-interessadas.md` como ponto de partida.
9. Responda com o que foi criado e o próximo passo: "preparar o kickoff com o agente `forja-facilitador` (guia `.forja/guias/d1-alinhamento.md`)".

Não faça commit do `CLAUDE.local.md`. A pasta `forja/` pode ser versionada no repositório do projeto, se a equipe quiser.
