# business-marketplace

Marketplace de plugins de negócio da Analizza.

| Plugin | Descrição |
| --- | --- |
| `analizza-leiloes` | Skills para análise de leilão de imóveis |

## Instalação por harness

### Claude Code

```bash
claude plugin marketplace add analizza-ai/business-marketplace
claude plugin install analizza-leiloes@business-marketplace
```

Para atualizar depois:

```bash
claude plugin marketplace update business-marketplace
claude plugin update analizza-leiloes
```

### Codex

O Codex não tem um comando de instalação de plugin via CLI. Abra o app Codex, vá em **Plugins**, localize **Analizza Leilões** depois que o marketplace Codex publicar o plugin e siga o fluxo da interface para instalar.

Para desenvolvimento local, o plugin mantém o manifesto `plugins/analizza-leiloes/.codex-plugin/plugin.json` na mesma pasta do plugin; use o fluxo de instalação local que o app Codex suporta para plugins nesse formato.

### Antigravity

```bash
agy plugin install https://github.com/analizza-ai/business-marketplace
```

O `agy` reconhece este repositório como um diretório de plugins em lote (bulk plugins directory) pelo próprio layout `plugins/<nome>/.claude-plugin/plugin.json`, o mesmo formato usado pelo Claude Code — não é preciso nenhum manifesto adicional. Para atualizar, rode o mesmo comando novamente.

## Skills do plugin `analizza-leiloes`

| Skill | O que faz |
| --- | --- |
| `analizza` | Recebe edital, matrícula, anúncio ou print de um lote de leilão — em PDF, imagem ou texto — e devolve um mapa de riscos. Cada apontamento traz o trecho literal que o originou, a consequência prática, a aula do curso que explica aquele risco e o que fazer a respeito. Fecha com um veredito de triagem: passa, cuidado ou não arremate. Também lista o que o material fornecido não permite verificar. |

## Publicando uma versão

Suba a mesma `version` em `plugins/analizza-leiloes/.claude-plugin/plugin.json` e em `plugins/analizza-leiloes/.codex-plugin/plugin.json`, valide e crie a tag:

```bash
claude plugin validate .
claude plugin validate plugins/analizza-leiloes
python3 tools/validate_plugin_manifests.py
python3 -m pytest tools/tests -q
python3 tools/validate_knowledge.py
claude plugin tag plugins/analizza-leiloes   # cria a tag analizza-leiloes--v{version}
```

## Estrutura

```
.claude-plugin/marketplace.json     # manifesto do marketplace
plugins/analizza-leiloes/
├── .claude-plugin/plugin.json      # manifesto do plugin (Claude Code)
├── .codex-plugin/plugin.json       # manifesto do plugin (Codex)
└── skills/                         # uma pasta por skill, fonte única para os dois harnesses
tools/                              # validador do catálogo e dos manifestos multi-harness
docs/superpowers/specs/             # decisões de design
docs/superpowers/plans/             # planos de implementação
```
