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

### GitHub Copilot CLI

```bash
claude plugin marketplace add analizza-ai/business-marketplace
claude plugin install analizza-leiloes@business-marketplace
```

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

`make tag` sobe a `version` nos dois manifestos (`.claude-plugin/plugin.json` e
`.codex-plugin/plugin.json`), valida, commita e cria a tag
`analizza-leiloes--v{version}`. Só roda a partir da branch `main`.

```bash
make tag          # bump de patch (padrão): 0.1.1 -> 0.1.2
make tag minor    # 0.1.1 -> 0.2.0
make tag major    # 0.1.1 -> 1.0.0
```

O comando cria o commit do bump e a tag localmente — publique com:

```bash
git push origin main
git push origin refs/tags/analizza-leiloes--v{version}
```

Ou dispare pela aba **Actions** do GitHub o workflow **Release tag
(analizza-leiloes)** (`workflow_dispatch`, escolhendo `patch`/`minor`/`major`),
que roda `make tag` e publica o commit e a tag automaticamente. Só executa a
partir da branch `main`.

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
