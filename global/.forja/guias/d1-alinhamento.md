# Guia D1: alinhamento e escopo (kickoff)

**Objetivo**: todos saem do kickoff concordando com o problema, os objetivos mensuráveis, quem decide e o que está fora do escopo.
**Conduz**: `forja-facilitador` (reunião) e `forja-analista` (artefato).
**Artefatos**: `produto/00-kickoff-pauta.md`, `produto/atas/AAAA-MM-DD-kickoff.md`, `produto/01-alinhamento.md`, `produto/01-partes-interessadas.md`.

## Antes do kickoff
1. Reúna o que já existe: e-mails, propostas, contrato, apresentações. Leia tudo e escreva uma **hipótese de problema** em uma frase.
2. Monte a primeira versão da matriz de partes interessadas (template `d1-partes-interessadas.md`). Confirme quem é o **decisor** de cada assunto.
3. Prepare a pauta (template `d1-kickoff-pauta.md`), com as perguntas abaixo priorizadas. Mande aos participantes com antecedência.

## Perguntas-chave
- **Problema**: o que acontece hoje que não deveria? Para quem? Com que frequência? Quanto custa (tempo, dinheiro, risco)?
- **Por que agora**: o que muda se nada for feito em 6 meses?
- **Sucesso**: como saberemos que deu certo? Qual número muda, de quanto para quanto, até quando?
- **Usuários**: quem usa, quem paga, quem é afetado sem usar?
- **Limites**: o que, explicitamente, **não** vamos fazer? Prazo, orçamento, tecnologia ou norma que restringe?
- **Riscos**: o que pode fazer o projeto falhar? Quem pode bloquear?
- **Decisão**: quem aprova o Portão 0? Com que frequência nos reunimos?

## Durante
- Comece pela hipótese de problema e peça para derrubarem. Discordância cedo é barata.
- Transforme cada objetivo vago em métrica na hora: "melhorar o atendimento" → "tempo de resposta de 3 dias para menos de 1 dia até 2027.1".
- Faça a lista "fora do escopo" em voz alta; ela evita mais retrabalho que a lista "dentro".
- Registre decisões, pendências (com dono e prazo) e suposições separadamente.

## Depois (até 24 h)
1. Escreva a ata (template `reuniao-ata.md`) e circule para correção.
2. Rode a skill `forja-registrar-reuniao` com a ata para atualizar `01-alinhamento.md` e a matriz de partes interessadas.
3. Registre no `forja/melhoria/registro.md` o que funcionou ou não no kickoff (skill `forja-observar`).

## Checklist de qualidade
- [ ] Problema descrito sem citar solução.
- [ ] Cada objetivo tem indicador, linha de base, meta e prazo.
- [ ] Lista "fora do escopo" com ao menos 3 itens.
- [ ] Decisor do Portão 0 nomeado.
- [ ] Toda suposição marcada e com dono para confirmar.
- [ ] Pendências com dono e prazo.

## Armadilhas
- Sair do kickoff com uma lista de funcionalidades em vez de objetivos.
- Aceitar "todos" como usuário.
- Confundir o patrocinador com o usuário.
