# business-marketplace

Marketplace de plugins de negócio do Claude Code da Analizza.

| Plugin | Descrição |
| --- | --- |
| `analizza-leiloes` | Skills para análise de leilão de imóveis |

## Instalação

```bash
make marketplace-add   # claude plugin marketplace add analizza-ai/business-marketplace
make install           # claude plugin install analizza-leiloes@business-marketplace
```

Para atualizar depois:

```bash
make update
```

## Skills do plugin `analizza-leiloes`

| Skill | O que faz |
| --- | --- |
| `analizza` | Recebe edital, matrícula, anúncio ou print de um lote de leilão — em PDF, imagem ou texto — e devolve um mapa de riscos. Cada apontamento traz o trecho literal que o originou, a consequência prática, a aula do curso que explica aquele risco e o que fazer a respeito. Fecha com um veredito de triagem: passa, cuidado ou não arremate. Também lista o que o material fornecido não permite verificar. |

## Publicando uma versão

Suba a `version` em `plugins/analizza-leiloes/.claude-plugin/plugin.json`, valide e crie a tag:

```bash
make validate
make check
make tag        # cria a tag analizza-leiloes--v{version}
```

## Estrutura

```
.claude-plugin/marketplace.json     # manifesto do marketplace
plugins/analizza-leiloes/
├── .claude-plugin/plugin.json      # manifesto do plugin
└── skills/                         # uma pasta por skill
tools/                              # validador do catálogo
docs/superpowers/specs/             # decisões de design
docs/superpowers/plans/             # planos de implementação
```
