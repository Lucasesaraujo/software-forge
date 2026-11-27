# Guia D2: pesquisa com usuários

**Objetivo**: trocar opinião por evidência sobre quem usa, o que precisa e o que dói.
**Conduz**: `forja-pesquisador`.
**Artefatos**: `produto/02-roteiro-entrevista.md`, `produto/pesquisa/E-xx.md` (uma nota por entrevista), `produto/02-pesquisa.md` (síntese).

## Planejar
1. Liste as **perguntas de pesquisa** (o que precisamos aprender), derivadas das suposições da D1.
2. Defina os perfis a entrevistar a partir da matriz de partes interessadas. Mínimo: 5 por perfil principal, 2 por perfil secundário.
3. Escreva o roteiro (template `d2-roteiro-entrevista.md`) e teste com uma pessoa da equipe.
4. Combine consentimento e gravação; registre que dados pessoais serão guardados e por quanto tempo (LGPD).

## Entrevistar
- Pergunte sobre **o passado concreto**, não sobre o futuro hipotético: "conte a última vez que..." em vez de "você usaria...".
- Siga a dor: "e o que você fez então?", "quanto tempo levou?", "o que acontece se der errado?".
- Não apresente a solução. Não conduza a resposta.
- Anote citações literais; elas são a evidência.

## Sintetizar
1. Uma nota por entrevista (template `d2-nota-entrevista.md`), com citações e observações separadas de interpretações.
2. Rode a skill `forja-registrar-reuniao` em cada nota/transcrição para extrair dores e citações.
3. Agrupe por afinidade: dores (`DOR-xx`), necessidades, comportamentos. Conte em quantas entrevistas cada uma aparece.
4. Monte personas (`PER-xx`) só a partir de padrões que aparecem em 2 ou mais entrevistas.
5. Preencha a síntese (template `d2-pesquisa.md`) e diga quais suposições da D1 foram confirmadas, derrubadas ou continuam abertas.

## Checklist de qualidade
- [ ] Toda dor tem evidência (quantas entrevistas, citação).
- [ ] Toda persona se apoia em padrões, não em uma pessoa só.
- [ ] Suposições da D1 revisitadas.
- [ ] Dados pessoais dos entrevistados anonimizados na síntese.

## Armadilhas
- Entrevistar só quem o cliente indicou (viés de seleção).
- Perguntas que pedem opinião sobre funcionalidades.
- Personas inventadas antes das entrevistas.
