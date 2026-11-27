# Base de design: Portal de Cursos

<!-- Salvar em forja/prototipo/design-base.md. Uma por produto. Mantida pelo forja-prototipador; toda tela usa só o que está aqui. -->

## Princípios
- Celular primeiro (PER-01 acessa à noite pelo celular).
- Resultado de toda ação visível na hora (OBJ-01).

## Tokens
| Token | Valor | Uso |
|---|---|---|
| `--cor-primaria` | #1f5fbf | Ações principais |
| `--cor-erro` | #b3261e | Mensagens de regra e erro |
| `--cor-sucesso` | #1e7a3a | Confirmações |
| `--cor-texto` | #1b1b1f | Texto (contraste 15:1 sobre o fundo) |
| `--cor-fundo` | #ffffff | Fundo |
| `--fonte` | system-ui, sans-serif | Todo o texto |
| `--espaco` | 8px (múltiplos) | Margens e espaçamentos |

## Componentes
| Componente | Quando usar | Estados |
|---|---|---|
| Botão primário | Uma ação principal por tela | normal, foco, desabilitado, carregando |
| Card de turma | Listas e detalhe de turma | normal, sem vagas |
| Mensagem | Resultado de ação | sucesso, erro, aviso (com `aria-live`) |
| Esqueleto | Carregando conteúdo | |

## Navegação
- Cabeçalho com nome do produto e link "Meus cursos".
- Toda tela tem caminho de volta.

## Acessibilidade
- WCAG 2.1 AA (RNF-03): contraste ≥ 4.5:1, foco visível, rótulos em todos os campos, alvos de toque ≥ 44 px.
