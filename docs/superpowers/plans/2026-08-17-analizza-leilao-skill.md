# Skill `/analizza` — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar o marketplace `business-marketplace` com o plugin `analizza-leiloes` v0.1.0, contendo a skill `/analizza`, que analisa material de leilão de imóveis e aponta riscos com citação de trecho e da aula do curso que explica cada risco.

**Architecture:** A skill é dirigida por um catálogo de riscos pré-compilado a partir das 62 transcrições do curso. A análise percorre o catálogo inteiro contra o documento — em duas passadas, por sinal e por ausência — em vez de reagir só ao vocabulário presente no texto. Um validador Python executável guarda os invariantes do catálogo e do índice de aulas, e roda como gate de cada tarefa de compilação.

**Tech Stack:** Markdown (skill, catálogo, índice), JSON (manifestos de marketplace e plugin), Make (release), Python 3 + pytest (validador), `claude plugin validate` / `claude plugin tag` (CLI).

**Spec:** `docs/superpowers/specs/2026-08-17-analizza-leilao-skill-design.md`

## Global Constraints

- Repositório de destino: `/Users/diegolirio/Documents/Github/business-marketplace`, remote `git@github.com:analizza-ai/business-marketplace.git`, branch `main`, sem commits anteriores além do spec.
- Nome do marketplace: `business-marketplace`. Nome do plugin: `analizza-leiloes`. Nome da skill: `analizza`.
- Versão inicial do plugin: `0.1.0`. Tag de release: `analizza-leiloes--v0.1.0`.
- Autor em todos os manifestos: `Diego Lirio`, `diegolirio.dl@gmail.com`.
- Todo conteúdo voltado ao usuário — SKILL.md, catálogo, índice, README — em português do Brasil.
- Severidades do catálogo, sem acento, exatamente: `CRITICO`, `ALTO`, `MEDIO`, `BAIXO`.
- Categorias do catálogo, exatamente: `MATRICULA`, `EDITAL`, `OCUPACAO`, `DIVIDAS`, `PROCESSUAL`, `MODALIDADE`, `TRIBUTARIO`, `PAGAMENTO`.
- `Aplica-se a:` aceita exatamente `judicial`, `extrajudicial` ou `ambos`.
- `Disparar por ausência:` aceita exatamente `SIM` ou `NAO`.
- IDs `R-NNN` são estáveis: nunca renumerados, nunca reusados.
- Origem das transcrições: `/Users/diegolirio/Documents/CursoLeiloes/analizza-auction-agent/__Transcripts/` — 62 arquivos `.vtt` mais `Notas - Modulo 3.txt`. Contagem por módulo: M1=12, M2=18, M3=26, M4=6.
- Lacunas reais do material, a respeitar sem inventar aulas: Módulo 1 não tem Aula 7; Módulo 3 Aula 14 existe só como "Parte 3"; Módulo 4 Aula 2 existe só como "parte2".
- `.DS_Store` nunca é copiado nem versionado.
- Atenção operacional: comandos `git` na pasta montada pelo bridge deixam um `.git/index.lock` que não pode ser removido pelo agente. Rodar `git` diretamente na máquina do usuário, ou mover os locks residuais para `_to_delete/` e avisar.

---

### Task 1: Scaffold do marketplace e manifesto do plugin

**Files:**
- Create: `.gitignore`
- Create: `.claude-plugin/marketplace.json`
- Create: `Makefile`
- Create: `README.md`
- Create: `plugins/analizza-leiloes/.claude-plugin/plugin.json`

**Interfaces:**
- Consumes: nada.
- Produces: a estrutura de diretórios `plugins/analizza-leiloes/skills/analizza/` que todas as tarefas seguintes preenchem; o alvo `make validate`, que é o gate de todas as tarefas seguintes.

- [ ] **Step 1: Escrever o `.gitignore`**

```gitignore
.DS_Store
__pycache__/
.pytest_cache/
_to_delete/
```

- [ ] **Step 2: Escrever `.claude-plugin/marketplace.json`**

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "business-marketplace",
  "description": "Marketplace de plugins de negócio da Analizza",
  "owner": {
    "name": "Diego Lirio",
    "email": "diegolirio.dl@gmail.com"
  },
  "plugins": [
    {
      "name": "analizza-leiloes",
      "description": "Skills da Analizza para análise de leilão de imóveis. Inclui analizza, que recebe edital, matrícula, anúncio ou print de um lote e devolve um mapa de riscos com o trecho exato que originou cada apontamento, a aula do curso que explica aquele risco e um veredito de triagem.",
      "author": {
        "name": "Diego Lirio",
        "email": "diegolirio.dl@gmail.com"
      },
      "source": "./plugins/analizza-leiloes",
      "category": "business"
    }
  ]
}
```

- [ ] **Step 3: Escrever `plugins/analizza-leiloes/.claude-plugin/plugin.json`**

```json
{
  "name": "analizza-leiloes",
  "description": "Skills da Analizza para análise de risco em leilão de imóveis",
  "version": "0.1.0",
  "author": {
    "name": "Diego Lirio",
    "email": "diegolirio.dl@gmail.com"
  }
}
```

- [ ] **Step 4: Escrever o `Makefile`**

Copiar a estrutura de `analizza-marketplace/Makefile`, trocando apenas as quatro variáveis do topo.

```makefile
REPO        := analizza-ai/business-marketplace
MARKETPLACE := business-marketplace
PLUGIN      := analizza-leiloes
PLUGIN_DIR  := plugins/analizza-leiloes

.DEFAULT_GOAL := help
SHELL := /bin/bash

##@ Geral

.PHONY: help
help: ## Mostra esta ajuda
	@awk 'BEGIN {FS = ":.*##"; printf "\nUso:\n  make \033[36m<alvo>\033[0m\n"} \
		/^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2 } \
		/^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }' $(MAKEFILE_LIST)
	@echo ""

##@ Instalação

.PHONY: marketplace-add
marketplace-add: ## Registra este repositório como marketplace
	claude plugin marketplace add $(REPO)

.PHONY: install
install: ## Instala o plugin a partir do marketplace
	claude plugin install $(PLUGIN)@$(MARKETPLACE)

##@ Atualização

.PHONY: update
update: ## Atualiza o marketplace e depois o plugin
	claude plugin marketplace update $(MARKETPLACE) && claude plugin update $(PLUGIN)

##@ Release

.PHONY: validate
validate: ## Valida os manifestos do marketplace e do plugin
	claude plugin validate . && claude plugin validate $(PLUGIN_DIR)

.PHONY: tag
tag: ## Cria a tag {plugin}--v{version} validando os manifestos
	claude plugin tag $(PLUGIN_DIR)

##@ Qualidade

.PHONY: check
check: ## Valida o catálogo de riscos e o índice de aulas
	python3 -m pytest tools/tests -q && python3 tools/validate_knowledge.py
```

O alvo `check` referencia arquivos criados na Task 3; até lá ele falha, o que é esperado.

- [ ] **Step 5: Escrever o `README.md`**

```markdown
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
```

- [ ] **Step 6: Criar o diretório da skill**

```bash
mkdir -p plugins/analizza-leiloes/skills/analizza/knowledge
mkdir -p plugins/analizza-leiloes/skills/analizza/transcripts
```

- [ ] **Step 7: Rodar a validação dos manifestos**

Run: `make validate`
Expected: PASS nos dois manifestos. Se `claude plugin validate` reclamar de skill ausente, criar um `SKILL.md` mínimo temporário não é a solução — a Task 9 escreve o definitivo. Registrar a mensagem e seguir; o gate real de manifesto é a Task 10.

- [ ] **Step 8: Commit**

```bash
git add .gitignore .claude-plugin Makefile README.md plugins/
git commit -m "feat: scaffold do business-marketplace com o plugin analizza-leiloes"
```

---

### Task 2: Transcrições e índice de aulas

**Files:**
- Create: `plugins/analizza-leiloes/skills/analizza/transcripts/*.vtt` (62 arquivos) mais `transcripts/Notas - Modulo 3.txt`
- Create: `plugins/analizza-leiloes/skills/analizza/knowledge/indice-aulas.md`

**Interfaces:**
- Consumes: a estrutura de diretórios da Task 1.
- Produces: `indice-aulas.md`, cuja coluna `Arquivo` é a chave que o validador da Task 3 confere contra `transcripts/`, e cujo par `Módulo`+`Aula` é o alvo do campo `Fonte` de toda entrada do catálogo.

- [ ] **Step 1: Copiar as transcrições**

```bash
SRC="/Users/diegolirio/Documents/CursoLeiloes/analizza-auction-agent/__Transcripts"
DST="plugins/analizza-leiloes/skills/analizza/transcripts"
rsync -a --exclude='.DS_Store' "$SRC"/ "$DST"/
```

- [ ] **Step 2: Conferir a contagem**

```bash
ls plugins/analizza-leiloes/skills/analizza/transcripts/*.vtt | wc -l
for m in 1 2 3 4; do
  echo "M$m: $(ls plugins/analizza-leiloes/skills/analizza/transcripts/Modulo_$m\ -*.vtt | wc -l)"
done
ls plugins/analizza-leiloes/skills/analizza/transcripts/ | grep -c '\.DS_Store' || echo "sem .DS_Store"
```

Expected: `62`, depois `M1: 12`, `M2: 18`, `M3: 26`, `M4: 6`, e `sem .DS_Store`.

- [ ] **Step 3: Escrever o cabeçalho e as linhas do Módulo 1 em `indice-aulas.md`**

O `Arquivo` é o nome exato do `.vtt`, sem o caminho. `Temas` são as palavras-chave que permitem escolher a aula certa para aprofundar um risco.

```markdown
# Índice de aulas

Uma linha por transcrição em `../transcripts/`. O campo `Fonte` de cada
entrada de `riscos.md` deve apontar para um par Módulo+Aula presente aqui.

Lacunas do material original, mantidas como são: o Módulo 1 não tem Aula 7;
o Módulo 3 Aula 14 existe apenas como "Parte 3"; o Módulo 4 Aula 2 existe
apenas como "parte2".

| Módulo | Aula | Arquivo | Temas |
| --- | --- | --- | --- |
| 1 | 0 | Modulo_1 - Aula 0 - Bem Vindo.vtt | apresentação do curso |
| 1 | 1 | Modulo_1 - Aula 1 - Desmistificando o leilão.vtt | mitos, riscos gerais, expectativa de desconto |
| 1 | 2 | Modulo_1 - Aula 2 - Por que o imóvel vai a leilão E modalidades de leilão.vtt | inadimplência, leilão judicial, leilão extrajudicial, modalidades |
| 1 | 3 | Modulo_1 - Aula 3 - Tipos de leilão online, presencial, híbrido.vtt | leilão online, presencial, híbrido, plataformas |
| 1 | 4 | Modulo_1 - Aula 4 - Quem pode participar dos leilões.vtt | habilitação, impedimentos, pessoa física, pessoa jurídica |
| 1 | 5 | Modulo_1 - Aula 5 - Matrícula do imóvel.vtt | matrícula, registro, averbação, ônus reais, cadeia dominial |
| 1 | 6 | Modulo_1 - Aula 6 - Bem de família.vtt | bem de família, impenhorabilidade, exceções |
| 1 | 8 | Modulo_1 - Aula 8 - Edital do leilão.vtt | edital, cláusulas, condições, obrigações do arrematante |
| 1 | 9 | Modulo_1 - Aula 9 - Primeira e segunda praça. Incremento. Lance condicional. Proposta.vtt | primeira praça, segunda praça, incremento, lance condicional, proposta |
| 1 | 10 | Modulo_1 - Aula 10 - Ferramentas online de avaliação do imóvel e informações sobre os ocupantes.vtt | avaliação de mercado, pesquisa de ocupantes, due diligence |
| 1 | 11 | Modulo_1 - Aula 11 - Calculadora do leilão – definindo o lance máximo (parte 1).vtt | lance máximo, custos, viabilidade financeira |
| 1 | 11 | Modulo_1 - Aula 11 - Calculadora do leilão – definindo o lance máximo (parte 2).vtt | lance máximo, custos, viabilidade financeira |
```

- [ ] **Step 4: Acrescentar as linhas dos Módulos 2, 3 e 4**

Mesmo formato. Preencher os `Temas` a partir do título de cada aula e de uma leitura rápida do início de cada `.vtt` — os títulos já são descritivos, e os primeiros trinta segundos de cada aula costumam enunciar o tema. Os 62 arquivos e seus nomes exatos estão em `transcripts/`; listar com `ls` e transcrever literalmente.

Aulas que existem em múltiplas partes ocupam uma linha por parte, com o mesmo número de Aula, como no Módulo 1 Aula 11 acima.

`Notas - Modulo 3.txt` não entra na tabela: não é transcrição de aula. Registrar em uma seção separada no fim do arquivo:

```markdown
## Material complementar

| Arquivo | Conteúdo |
| --- | --- |
| Notas - Modulo 3.txt | Links de referência citados no Módulo 3: consulta processual, artigos 879–903 do CPC, certidões trabalhistas por TRT, CNA/OAB |
```

- [ ] **Step 5: Conferir que toda linha aponta para um arquivo existente**

```bash
cd plugins/analizza-leiloes/skills/analizza
grep -oP '(?<=\| )Modulo_[^|]+\.vtt(?= \|)' knowledge/indice-aulas.md \
  | sed 's/ *$//' \
  | while read -r f; do
      [ -f "transcripts/$f" ] || echo "AUSENTE: $f"
    done
echo "linhas no índice: $(grep -c '^| [0-9] |' knowledge/indice-aulas.md)"
```

Expected: nenhuma linha `AUSENTE`, e `linhas no índice: 62`.

- [ ] **Step 6: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/
git commit -m "feat: empacota as transcrições do curso e o índice de aulas"
```

---

### Task 3: Validador do catálogo e do índice

Escrito antes do catálogo, para que o catálogo nasça válido e cada tarefa de compilação tenha um gate objetivo.

**Files:**
- Create: `tools/__init__.py` (vazio)
- Create: `tools/validate_knowledge.py`
- Create: `tools/tests/__init__.py` (vazio)
- Create: `tools/tests/test_validate_knowledge.py`
- Create: `tools/tests/fixtures/riscos_valido.md`
- Create: `tools/tests/fixtures/riscos_invalido.md`
- Create: `tools/tests/fixtures/indice_valido.md`

**Interfaces:**
- Consumes: o formato de `indice-aulas.md` definido na Task 2.
- Produces: o módulo `tools/validate_knowledge.py`, expondo:
  - `parse_riscos(texto: str) -> list[dict]` — cada dict tem as chaves `id`, `titulo`, `categoria`, `severidade`, `aplica_se_a`, `fonte_modulo`, `fonte_aula`, `disparar_por_ausencia` (bool ou None), `disparar_por_ausencia_raw` (a string original, para o validador poder reportar valores inválidos como `TALVEZ`) e `corpo`.
  - `parse_indice(texto: str) -> list[dict]` — cada dict tem `modulo` (int), `aula` (str), `arquivo` (str), `temas` (str).
  - `validar(riscos: list[dict], indice: list[dict], arquivos_transcripts: set[str]) -> list[str]` — devolve a lista de mensagens de erro, vazia quando tudo está válido.
  - `main() -> int` — lê os caminhos reais, imprime os erros, devolve 0 ou 1.

- [ ] **Step 1: Escrever a fixture de catálogo válido**

`tools/tests/fixtures/riscos_valido.md`:

```markdown
# Catálogo de riscos

### R-001 · Imóvel ocupado pelo antigo mutuário
Categoria: OCUPACAO · Severidade: ALTO
Aplica-se a: extrajudicial
Fonte: Módulo 2 — Aula 8 (Desocupação do imóvel nos leilões extrajudiciais)

O que é: o antigo devedor permanece no imóvel após a consolidação.

Sinais no documento: "imóvel ocupado", "na posse do antigo mutuário".

Disparar por ausência: SIM

Consequência prática: a desocupação corre por conta do arrematante.

O que fazer: orçar a desocupação antes de definir o lance máximo.

### R-002 · Hipoteca registrada na matrícula
Categoria: MATRICULA · Severidade: MEDIO
Aplica-se a: ambos
Fonte: Módulo 3 — Aula 8.2 (Hipoteca)

O que é: o imóvel foi dado em garantia de um empréstimo.

Sinais no documento: "hipoteca", "credor hipotecário", "R-4 hipoteca".

Disparar por ausência: NAO

Consequência prática: verificar se a hipoteca se extingue com a arrematação.

O que fazer: conferir se o credor hipotecário foi intimado do leilão.
```

- [ ] **Step 2: Escrever a fixture de índice válido**

`tools/tests/fixtures/indice_valido.md`:

```markdown
# Índice de aulas

| Módulo | Aula | Arquivo | Temas |
| --- | --- | --- | --- |
| 2 | 8 | Modulo_2 - Aula 8 - Desocupação do imóvel nos leilões extrajudiciais.vtt | desocupação, imissão na posse |
| 3 | 8.2 | Modulo_3 - Aula 8.2 - Hipoteca.vtt | hipoteca, garantia real |
```

- [ ] **Step 3: Escrever a fixture de catálogo inválido**

Cada entrada carrega um defeito diferente, para que cada regra do validador tenha um caso negativo.

`tools/tests/fixtures/riscos_invalido.md`:

```markdown
# Catálogo de riscos

### R-001 · Categoria inexistente
Categoria: JURIDICO · Severidade: ALTO
Aplica-se a: ambos
Fonte: Módulo 2 — Aula 8 (Desocupação do imóvel nos leilões extrajudiciais)

O que é: entrada com categoria fora da lista.

Sinais no documento: "teste".

Disparar por ausência: SIM

Consequência prática: nenhuma.

O que fazer: nada.

### R-001 · Identificador duplicado
Categoria: EDITAL · Severidade: CRÍTICO
Aplica-se a: talvez
Fonte: Módulo 9 — Aula 1 (Aula que não existe)

O que é: id repetido, severidade acentuada, aplica-se a inválido, fonte fantasma.

Sinais no documento: "teste".

Disparar por ausência: TALVEZ

Consequência prática: nenhuma.

O que fazer: nada.

### R-003 · Campos obrigatórios faltando
Categoria: EDITAL · Severidade: BAIXO
Aplica-se a: ambos
Fonte: Módulo 3 — Aula 8.2 (Hipoteca)

O que é: falta Sinais no documento, Disparar por ausência, Consequência e O que fazer.
```

- [ ] **Step 4: Escrever os testes que falham**

`tools/tests/test_validate_knowledge.py`:

```python
from pathlib import Path

import pytest

from tools.validate_knowledge import parse_riscos, parse_indice, validar

FIXTURES = Path(__file__).parent / "fixtures"


def ler(nome):
    return (FIXTURES / nome).read_text(encoding="utf-8")


@pytest.fixture
def indice():
    return parse_indice(ler("indice_valido.md"))


@pytest.fixture
def arquivos():
    return {
        "Modulo_2 - Aula 8 - Desocupação do imóvel nos leilões extrajudiciais.vtt",
        "Modulo_3 - Aula 8.2 - Hipoteca.vtt",
    }


def test_parse_riscos_extrai_todos_os_campos():
    riscos = parse_riscos(ler("riscos_valido.md"))
    assert len(riscos) == 2
    primeiro = riscos[0]
    assert primeiro["id"] == "R-001"
    assert primeiro["titulo"] == "Imóvel ocupado pelo antigo mutuário"
    assert primeiro["categoria"] == "OCUPACAO"
    assert primeiro["severidade"] == "ALTO"
    assert primeiro["aplica_se_a"] == "extrajudicial"
    assert primeiro["fonte_modulo"] == 2
    assert primeiro["fonte_aula"] == "8"
    assert primeiro["disparar_por_ausencia"] is True


def test_parse_indice_extrai_linhas():
    linhas = parse_indice(ler("indice_valido.md"))
    assert len(linhas) == 2
    assert linhas[0]["modulo"] == 2
    assert linhas[0]["aula"] == "8"
    assert linhas[0]["arquivo"].endswith(".vtt")


def test_catalogo_valido_nao_produz_erros(indice, arquivos):
    riscos = parse_riscos(ler("riscos_valido.md"))
    assert validar(riscos, indice, arquivos) == []


def test_aplica_se_a_ausente_assume_ambos(indice, arquivos):
    texto = ler("riscos_valido.md").replace("Aplica-se a: extrajudicial\n", "")
    riscos = parse_riscos(texto)
    assert riscos[0]["aplica_se_a"] == "ambos"
    assert validar(riscos, indice, arquivos) == []


def test_categoria_invalida_e_reportada(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "JURIDICO" in erros


def test_id_duplicado_e_reportado(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "duplicado" in erros.lower()


def test_severidade_acentuada_e_reportada(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "CRÍTICO" in erros


def test_aplica_se_a_invalido_e_reportado(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "talvez" in erros.lower()


def test_fonte_fora_do_indice_e_reportada(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "Módulo 9" in erros


def test_disparar_por_ausencia_invalido_e_reportado(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "TALVEZ" in erros


def test_campos_obrigatorios_faltando_sao_reportados(indice, arquivos):
    riscos = parse_riscos(ler("riscos_invalido.md"))
    erros = "\n".join(validar(riscos, indice, arquivos))
    assert "R-003" in erros
    assert "Sinais no documento" in erros


def test_arquivo_do_indice_ausente_no_disco(indice):
    riscos = parse_riscos(ler("riscos_valido.md"))
    erros = "\n".join(validar(riscos, indice, set()))
    assert "não existe em transcripts" in erros
```

- [ ] **Step 5: Rodar os testes e confirmar que falham**

Run: `python3 -m pytest tools/tests -q`
Expected: FAIL com `ModuleNotFoundError: No module named 'tools.validate_knowledge'`

- [ ] **Step 6: Escrever o validador**

`tools/validate_knowledge.py`:

```python
"""Valida os invariantes de knowledge/riscos.md e knowledge/indice-aulas.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

CATEGORIAS = {
    "MATRICULA", "EDITAL", "OCUPACAO", "DIVIDAS",
    "PROCESSUAL", "MODALIDADE", "TRIBUTARIO", "PAGAMENTO",
}
SEVERIDADES = {"CRITICO", "ALTO", "MEDIO", "BAIXO"}
APLICA_SE_A = {"judicial", "extrajudicial", "ambos"}
CAMPOS_OBRIGATORIOS = [
    "O que é:",
    "Sinais no documento:",
    "Disparar por ausência:",
    "Consequência prática:",
    "O que fazer:",
]

CABECALHO = re.compile(r"^### (R-\d{3}) · (.+)$", re.MULTILINE)
LINHA_CAT = re.compile(r"^Categoria:\s*(\S+)\s*·\s*Severidade:\s*(\S+)\s*$", re.MULTILINE)
LINHA_APLICA = re.compile(r"^Aplica-se a:\s*(\S+)\s*$", re.MULTILINE)
LINHA_FONTE = re.compile(r"^Fonte:\s*Módulo\s+(\d+)\s+—\s+Aula\s+(\S+)", re.MULTILINE)
LINHA_AUSENCIA = re.compile(r"^Disparar por ausência:\s*(\S+)", re.MULTILINE)
LINHA_INDICE = re.compile(r"^\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|$", re.MULTILINE)


def parse_riscos(texto: str) -> list[dict]:
    cabecalhos = list(CABECALHO.finditer(texto))
    riscos = []
    for i, m in enumerate(cabecalhos):
        inicio = m.end()
        fim = cabecalhos[i + 1].start() if i + 1 < len(cabecalhos) else len(texto)
        corpo = texto[inicio:fim]

        cat = LINHA_CAT.search(corpo)
        aplica = LINHA_APLICA.search(corpo)
        fonte = LINHA_FONTE.search(corpo)
        ausencia = LINHA_AUSENCIA.search(corpo)

        riscos.append({
            "id": m.group(1),
            "titulo": m.group(2).strip(),
            "categoria": cat.group(1) if cat else None,
            "severidade": cat.group(2) if cat else None,
            "aplica_se_a": aplica.group(1) if aplica else "ambos",
            "fonte_modulo": int(fonte.group(1)) if fonte else None,
            "fonte_aula": fonte.group(2) if fonte else None,
            "disparar_por_ausencia_raw": ausencia.group(1) if ausencia else None,
            "disparar_por_ausencia": (
                ausencia.group(1) == "SIM" if ausencia else None
            ),
            "corpo": corpo,
        })
    return riscos


def parse_indice(texto: str) -> list[dict]:
    return [
        {
            "modulo": int(m.group(1)),
            "aula": m.group(2),
            "arquivo": m.group(3).strip(),
            "temas": m.group(4).strip(),
        }
        for m in LINHA_INDICE.finditer(texto)
    ]


def validar(riscos, indice, arquivos_transcripts) -> list[str]:
    erros = []

    vistos = set()
    for r in riscos:
        rid = r["id"]
        if rid in vistos:
            erros.append(f"{rid}: identificador duplicado")
        vistos.add(rid)

        if r["categoria"] not in CATEGORIAS:
            erros.append(f"{rid}: categoria inválida {r['categoria']!r}")
        if r["severidade"] not in SEVERIDADES:
            erros.append(f"{rid}: severidade inválida {r['severidade']!r}")
        if r["aplica_se_a"] not in APLICA_SE_A:
            erros.append(f"{rid}: 'Aplica-se a' inválido {r['aplica_se_a']!r}")
        if r["disparar_por_ausencia_raw"] not in {"SIM", "NAO"}:
            erros.append(
                f"{rid}: 'Disparar por ausência' inválido "
                f"{r['disparar_por_ausencia_raw']!r}"
            )

        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in r["corpo"]:
                erros.append(f"{rid}: campo obrigatório ausente: {campo.rstrip(':')}")

        if r["fonte_modulo"] is None:
            erros.append(f"{rid}: campo Fonte ausente ou malformado")
        else:
            par = (r["fonte_modulo"], r["fonte_aula"])
            if par not in {(l["modulo"], l["aula"]) for l in indice}:
                erros.append(
                    f"{rid}: Fonte aponta para Módulo {r['fonte_modulo']} "
                    f"Aula {r['fonte_aula']}, ausente do índice"
                )

    for linha in indice:
        if linha["arquivo"] not in arquivos_transcripts:
            erros.append(
                f"índice: {linha['arquivo']!r} não existe em transcripts/"
            )

    return erros


def main() -> int:
    raiz = Path(__file__).resolve().parent.parent
    skill = raiz / "plugins/analizza-leiloes/skills/analizza"

    riscos = parse_riscos((skill / "knowledge/riscos.md").read_text(encoding="utf-8"))
    indice = parse_indice((skill / "knowledge/indice-aulas.md").read_text(encoding="utf-8"))
    arquivos = {p.name for p in (skill / "transcripts").glob("*.vtt")}

    erros = validar(riscos, indice, arquivos)
    for e in erros:
        print(e)
    print(f"\n{len(riscos)} riscos, {len(indice)} aulas, {len(erros)} erros")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
```

Criar também `tools/__init__.py` e `tools/tests/__init__.py`, ambos vazios, para que o import `from tools.validate_knowledge import ...` funcione a partir da raiz do repositório.

- [ ] **Step 7: Rodar os testes e confirmar que passam**

Run: `python3 -m pytest tools/tests -q`
Expected: PASS, 12 testes.

- [ ] **Step 8: Commit**

```bash
git add tools/
git commit -m "test: validador dos invariantes do catálogo de riscos"
```

---

### Task 4: Catálogo — Módulo 1

**Files:**
- Create: `plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md`

**Interfaces:**
- Consumes: `parse_riscos` e `validar` da Task 3; `indice-aulas.md` da Task 2.
- Produces: as entradas `R-001` em diante, no formato que as Tasks 5 a 7 continuam.

O Módulo 1 cobre fundamentos e o edital: modalidades, quem pode participar, matrícula, bem de família, edital, praças e incremento, avaliação. As 12 transcrições estão em `transcripts/Modulo_1 - *.vtt`.

- [ ] **Step 1: Ler as 12 transcrições do Módulo 1**

Ler cada `.vtt` por inteiro. Para cada risco que a aula ensina, anotar: o que é, como ele aparece num documento real, o que acontece com quem não percebe, e o que fazer.

Um risco só entra no catálogo se satisfizer os três critérios:

1. É detectável a partir de edital, matrícula, anúncio ou laudo — não depende de diligência externa.
2. Tem consequência concreta em dinheiro, prazo ou perda do bem.
3. A aula explica a consequência, não apenas menciona o termo.

Conteúdo que não vira risco: definições sem consequência prática, ferramentas e sites, história do instituto, e o cálculo de lance máximo da Aula 11, que está fora de escopo por decisão do spec.

- [ ] **Step 2: Escrever o cabeçalho e as entradas do Módulo 1**

Cabeçalho do arquivo, escrito uma única vez:

```markdown
# Catálogo de riscos

Cada entrada descreve um risco que o curso ensina a identificar em material
de leilão. A análise percorre este catálogo inteiro contra o documento, em
duas passadas: por sinal, casando o vocabulário do documento contra `Sinais
no documento`; e por ausência, avaliando toda entrada marcada `Disparar por
ausência: SIM` mesmo sem gatilho no texto.

`Sinais no documento` lista gatilhos exemplificativos, não exaustivos. O
casamento é semântico: "remanescendo o antigo mutuário no bem" dispara o
risco de ocupação sem usar nenhum dos termos listados.

Identificadores `R-NNN` são estáveis. Nunca renumerar, nunca reusar.

Categorias: MATRICULA, EDITAL, OCUPACAO, DIVIDAS, PROCESSUAL, MODALIDADE,
TRIBUTARIO, PAGAMENTO.
Severidades: CRITICO, ALTO, MEDIO, BAIXO.
`Aplica-se a`: judicial, extrajudicial, ambos. Ausente equivale a ambos.

---
```

Cada entrada segue exatamente este formato, com todos os campos presentes:

```markdown
### R-001 · Bem de família não afastado no edital
Categoria: MODALIDADE · Severidade: ALTO
Aplica-se a: ambos
Fonte: Módulo 1 — Aula 6 (Bem de família)

O que é: imóvel que serve de residência à família é impenhorável, salvo
nas exceções legais. Se a impenhorabilidade for reconhecida depois da
arrematação, o negócio pode ser desfeito.

Sinais no documento: "única residência", "bem de família", "imóvel
residencial do executado", ausência de menção à natureza da ocupação.

Disparar por ausência: SIM

Consequência prática: risco de anulação da arrematação, com devolução do
valor pago sujeita ao rito processual e sem indenização pelo tempo parado.

O que fazer: verificar se o executado discutiu impenhorabilidade nos autos
e se a decisão já transitou.
```

Escrever uma entrada por risco identificado, numeradas em sequência a partir de `R-001`.

- [ ] **Step 3: Rodar o validador**

Run: `python3 tools/validate_knowledge.py`
Expected: `0 erros`. Qualquer erro de categoria, severidade, campo faltando ou fonte fora do índice deve ser corrigido antes de seguir.

- [ ] **Step 4: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
git commit -m "feat: catálogo de riscos do Módulo 1"
```

---

### Task 5: Catálogo — Módulo 2

**Files:**
- Modify: `plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md`

**Interfaces:**
- Consumes: o formato de entrada e a numeração corrente da Task 4.
- Produces: entradas continuando a numeração; nenhuma renumeração das anteriores.

O Módulo 2 é o leilão extrajudicial: alienação fiduciária, regras de primeiro e segundo leilão, dação, formas de pagamento, imóvel financiado, documentação, desocupação, locação vigente, taxa de ocupação, condomínio e IPTU, penhoras, consignação e evicção, ação anulatória, e o checklist prático em três partes. São 18 transcrições.

Este é o módulo mais denso em riscos com consequência financeira direta. A Aula 15, nas três partes, é um checklist explícito do instrutor — cada item dela deve ter uma entrada correspondente no catálogo, e a ausência de correspondência é sinal de lacuna.

- [ ] **Step 1: Ler as 18 transcrições do Módulo 2**

Aplicar os mesmos três critérios de inclusão da Task 4.

- [ ] **Step 2: Acrescentar as entradas ao `riscos.md`**

Continuar a numeração de onde a Task 4 parou. Entradas específicas do rito extrajudicial levam `Aplica-se a: extrajudicial`.

- [ ] **Step 3: Conferir a cobertura do checklist da Aula 15**

Listar os itens do checklist ditados nas três partes da Aula 15 e apontar, para cada um, a entrada do catálogo que o cobre. Item sem entrada correspondente é lacuna: ou vira entrada, ou é registrado como fora de escopo com justificativa em comentário no próprio arquivo.

- [ ] **Step 4: Rodar o validador**

Run: `python3 tools/validate_knowledge.py`
Expected: `0 erros`.

- [ ] **Step 5: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
git commit -m "feat: catálogo de riscos do Módulo 2, leilão extrajudicial"
```

---

### Task 6: Catálogo — Módulo 3

**Files:**
- Modify: `plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md`

**Interfaces:**
- Consumes: o formato de entrada e a numeração corrente da Task 5.
- Produces: entradas continuando a numeração.

O Módulo 3 é o leilão judicial, e concentra a categoria `MATRICULA`: as aulas 8.1 a 8.9 percorrem penhora, hipoteca, parte ideal, nua propriedade, direitos sobre o imóvel, indisponibilidade, inalienabilidade, dação e usucapião, uma a uma, cada qual com a consequência prática de encontrá-la na matrícula. São 26 transcrições.

- [ ] **Step 1: Ler as 26 transcrições do Módulo 3**

A Aula 8 principal tem apenas 1,3 KB — é uma introdução às subaulas 8.1 a 8.9, que carregam o conteúdo. Cada subaula corresponde a pelo menos um termo de matrícula e deve produzir pelo menos uma entrada `MATRICULA`.

A Aula 11, em três partes, trata de concurso de credores e da Súmula 478 do STJ: quais dívidas seguem o imóvel e quais seguem o executado. É a base das entradas `DIVIDAS` do rito judicial, e a distinção entre dívida propter rem e dívida pessoal precisa ficar explícita nas entradas.

- [ ] **Step 2: Acrescentar as entradas ao `riscos.md`**

Continuar a numeração. Entradas específicas do rito judicial levam `Aplica-se a: judicial`.

Atenção às fontes: a Aula 14 existe apenas como "Parte 3". Citar `Módulo 3 — Aula 14`, que é o que o índice registra.

- [ ] **Step 3: Rodar o validador**

Run: `python3 tools/validate_knowledge.py`
Expected: `0 erros`.

- [ ] **Step 4: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
git commit -m "feat: catálogo de riscos do Módulo 3, leilão judicial e matrícula"
```

---

### Task 7: Catálogo — Módulo 4

**Files:**
- Modify: `plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md`

**Interfaces:**
- Consumes: o formato de entrada e a numeração corrente da Task 6.
- Produces: as últimas entradas do catálogo.

O Módulo 4 é o pós-arrematação: ITBI, imposto de renda sobre lucro imobiliário, estratégias e procedimento de venda, locação, consultoria. São 6 transcrições.

Boa parte deste módulo é estratégia comercial, não risco detectável num documento. Espera-se, portanto, um número pequeno de entradas — concentradas em `TRIBUTARIO`, e apenas onde o custo tributário for detectável a partir do material do lote, como alíquota de ITBI incidente sobre o valor de arrematação ou sobre o valor venal, o que for maior.

- [ ] **Step 1: Ler as 6 transcrições do Módulo 4**

Aplicar os três critérios de inclusão com rigor. Resistir à tentação de transformar conselho comercial em risco: uma entrada fraca no catálogo custa atenção em toda análise futura.

- [ ] **Step 2: Acrescentar as entradas ao `riscos.md`**

- [ ] **Step 3: Rodar o validador**

Run: `python3 tools/validate_knowledge.py`
Expected: `0 erros`.

- [ ] **Step 4: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
git commit -m "feat: catálogo de riscos do Módulo 4, tributário e pós-arrematação"
```

---

### Task 8: Consolidação do catálogo

**Files:**
- Modify: `plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md`

**Interfaces:**
- Consumes: o catálogo completo das Tasks 4 a 7.
- Produces: o catálogo final, que a Task 9 referencia no `SKILL.md`.

- [ ] **Step 1: Deduplicar**

Riscos aparecem em mais de um módulo com recortes diferentes. Desocupação, por exemplo, é ensinada no Módulo 2 para o rito extrajudicial e no Módulo 3 para o judicial.

A regra: se a consequência prática e a ação recomendada são as mesmas nos dois ritos, fundir numa entrada com `Aplica-se a: ambos` e citar a aula mais completa em `Fonte`. Se diferem, manter duas entradas com `Aplica-se a` distintos. Não fundir por semelhança de título.

Ao fundir, o ID que sobrevive é o menor. O ID descartado não é reaproveitado por nenhuma entrada futura.

- [ ] **Step 2: Conferir o balanço do catálogo**

```bash
grep -c '^### R-' plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
grep -oP '(?<=^Categoria: )\w+' plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md | sort | uniq -c
grep -oP '(?<=· Severidade: )\w+' plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md | sort | uniq -c
grep -c '^Disparar por ausência: SIM' plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
```

Expected: total entre 60 e 90 entradas. As oito categorias todas presentes. `CRITICO` reservado a risco de perder o bem ou de anulação da arrematação — se houver mais de dez, a severidade foi inflacionada e precisa ser revista. Pelo menos quinze entradas com `Disparar por ausência: SIM`, já que é esse conjunto que resolve o problema da omissão.

- [ ] **Step 3: Rodar o validador e os testes**

Run: `make check`
Expected: PASS nos testes e `0 erros` no validador.

- [ ] **Step 4: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/knowledge/riscos.md
git commit -m "refactor: deduplica e consolida o catálogo de riscos"
```

- [ ] **Step 5: Revisão humana do catálogo**

Parar aqui e pedir a Diego que leia `riscos.md` por inteiro. É o critério de aceite 5 do spec, e o único gate que nenhuma verificação automática substitui: o validador confere a forma das entradas, não se o direito está certo.

Pedir atenção especial a: consequências práticas descritas de forma imprecisa, severidades infladas, riscos do rito judicial atribuídos ao extrajudicial e vice-versa, e riscos importantes do curso que ficaram de fora.

Aplicar as correções que ele apontar, rodar `make check` de novo e commitar antes de seguir para a Task 9.

---

### Task 9: SKILL.md

**Files:**
- Create: `plugins/analizza-leiloes/skills/analizza/SKILL.md`

**Interfaces:**
- Consumes: `knowledge/riscos.md`, `knowledge/indice-aulas.md`, `transcripts/`.
- Produces: a skill invocável como `/analizza`.

- [ ] **Step 1: Escrever o frontmatter**

```yaml
---
name: analizza
description: Analisa material de leilão de imóveis — edital, matrícula, anúncio, laudo, print ou link — e aponta os riscos e pontos de atenção, com o trecho literal que originou cada apontamento e a aula do curso que explica aquele risco. Fecha com veredito de triagem e lista o que o material não permite verificar. Use quando o usuário pedir "analisar leilão", "analisar edital", "analisar matrícula", "vale a pena arrematar", "riscos desse lote", "analisar esse imóvel de leilão", ou invocar /analizza.
---
```

- [ ] **Step 2: Escrever o corpo da skill**

O corpo cobre, nesta ordem, e sem exceder cerca de 150 linhas:

**Ingestão.** PDF por extração de texto; se vier digitalizado, OCR. Imagem por leitura visual direta. Texto ou link colado usado como está. Vários documentos do mesmo lote numa invocação produzem **uma** análise consolidada, com cada citação identificando seu documento de origem.

**Classificação.** Identificar tipo de documento e modalidade, judicial ou extrajudicial. A modalidade governa quais entradas do catálogo se aplicam, via campo `Aplica-se a`. Se o material não deixar a modalidade clara, perguntar. Esta é a única pergunta permitida antes de analisar.

**Varredura.** Ler `knowledge/riscos.md` por inteiro. Primeira passada por sinal: casar semanticamente o conteúdo do documento contra `Sinais no documento` de cada entrada aplicável, lembrando que os termos são exemplificativos. Segunda passada por ausência: para cada entrada `Disparar por ausência: SIM` que não foi confirmada nem descartada pela primeira passada, decidir entre confirmar o risco, descartá-lo com base em algo que o documento diz, ou classificá-lo como não verificável.

Instrução explícita a incluir no texto da skill: nunca tratar uma entrada como aprovada só porque o documento não a menciona. Silêncio não é aprovação.

**Aprofundamento.** Para riscos confirmados em `CRITICO` ou `ALTO`, localizar o `.vtt` da aula-fonte em `knowledge/indice-aulas.md` e lê-lo antes de escrever a consequência prática. Não citar uma aula sem tê-la lido nesta execução.

**Saída.** Reproduzir integralmente o formato da seção "Formato da saída" do spec, incluindo os emojis de severidade, o bloco de citação com negrito no trecho gatilho, a seção "Não verificável com este documento", os três vereditos e a linha de rodapé fixa.

Regras de citação a explicitar: a citação é literal, copiada do documento, com negrito apenas no trecho que dispara o risco; a localização é cláusula e página quando o documento é texto estruturado, e página e região quando é imagem ou PDF digitalizado, porque nesses casos não há numeração confiável; nunca inventar número de cláusula.

**Veredito.** Qualquer risco `CRITICO` confirmado força `🛑 NÃO ARREMATE`. A ausência de riscos confirmados não basta para `✅ PASSA` se a seção "Não verificável" estiver substancial — nesse caso o veredito é `⚠️ CUIDADO`, e a justificativa diz o que falta.

**Limites.** A skill não calcula lance máximo, não consulta cartório, processo ou certidão, e não substitui a análise da matrícula por advogado.

- [ ] **Step 3: Verificar que a skill é reconhecida**

Run: `make validate`
Expected: PASS nos dois manifestos, sem aviso de skill malformada.

- [ ] **Step 4: Commit**

```bash
git add plugins/analizza-leiloes/skills/analizza/SKILL.md
git commit -m "feat: skill analizza de análise de risco de leilão"
```

---

### Task 10: Teste ponta a ponta e release

**Files:**
- Modify: `README.md` (se a tabela de skills precisar de ajuste após o teste)
- Create: a tag `analizza-leiloes--v0.1.0`

**Interfaces:**
- Consumes: tudo das tarefas anteriores.
- Produces: o plugin instalável.

- [ ] **Step 1: Instalar o plugin localmente**

```bash
make marketplace-add
make install
```

- [ ] **Step 2: Rodar `/analizza` sobre um edital real**

Pedir a Diego um edital de leilão real, de preferência extrajudicial e com imóvel ocupado, já que é o caso que exercita a maior parte do catálogo.

Conferir na saída:

1. O cabeçalho identifica tipo de documento e modalidade corretamente.
2. Cada risco apontado traz citação literal que **existe** no documento — conferir palavra por palavra em pelo menos três apontamentos.
3. A localização citada corresponde à cláusula e página reais.
4. Cada `Fonte` aponta para uma aula que existe e que de fato trata daquele assunto.
5. A seção "Não verificável" está preenchida, já que um edital sozinho não permite avaliar riscos de matrícula.
6. O veredito é coerente com as severidades apontadas.
7. A linha de rodapé sobre triagem está presente.

Falha em qualquer um dos sete pontos é defeito da skill, não do teste: corrigir `SKILL.md` ou o catálogo, e repetir.

- [ ] **Step 3: Rodar `/analizza` sobre um print de anúncio**

Confirmar o comportamento degradado esperado: análise majoritariamente composta pela seção "Não verificável", sem apontamentos inventados para preencher espaço. Se a skill produzir muitos riscos confirmados a partir de um anúncio raso, ela está alucinando e o `SKILL.md` precisa de instrução mais firme.

- [ ] **Step 4: Rodar a validação completa**

```bash
make validate
make check
```

Expected: PASS em ambos.

- [ ] **Step 5: Criar a tag de release**

```bash
make tag
git push origin main
git push origin analizza-leiloes--v0.1.0
```

- [ ] **Step 6: Confirmar a instalação a partir do remoto**

```bash
make update
```

Expected: o plugin atualiza para 0.1.0 a partir do GitHub, e `/analizza` continua disponível.
