# Plugin Codex Multi-Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Disponibilizar o plugin analizza-leiloes para Codex sem duplicar as skills distribuídas ao Claude Code.

**Architecture:** A árvore plugins/analizza-leiloes/skills/ continua canônica. Um manifesto Codex aponta para ela; o manifesto Claude é preservado. Um validador Python verifica o contrato entre manifestos e é executado pelo Makefile e pytest.

**Tech Stack:** JSON, Markdown, GNU Make, Python 3 padrão e pytest.

**Spec:** docs/superpowers/specs/2026-08-18-plugin-codex-multi-harness-design.md

## Global Constraints

- A fonte de todas as skills é plugins/analizza-leiloes/skills/; não duplicar conteúdo nem usar links simbólicos.
- O manifesto Codex declara exatamente "skills": "./skills/".
- name e version são iguais nos manifestos Claude e Codex.
- Não adicionar hooks, MCP servers, aplicações ou assets.
- Não alterar conteúdo ou comportamento da skill analizza.
- Não incluir a alteração preexistente em docs/superpowers/specs/2026-08-17-analizza-leilao-skill-design.md.

---

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| plugins/analizza-leiloes/.codex-plugin/plugin.json | Descoberta Codex e referência à árvore canônica. |
| tools/validate_plugin_manifests.py | Validação independente dos manifestos. |
| tools/tests/test_validate_plugin_manifests.py | Contrato do validador e integração dos manifestos reais. |
| Makefile | Execução do validador em make validate. |
| README.md | Instalação e publicação por harness. |

### Task 1: Validador do contrato multi-harness

**Files:**

- Create: tools/validate_plugin_manifests.py
- Create: tools/tests/test_validate_plugin_manifests.py
- Modify: Makefile:33-35

**Interfaces:**

- Consumes: os dois plugin.json em plugins/analizza-leiloes/.
- Produces: validar_manifestos(claude: dict, codex: dict, plugin_dir: Path) -> list[str] e CLI com retorno 0/1.

- [ ] **Step 1: Escrever os testes em vermelho**

Crie tools/tests/test_validate_plugin_manifests.py. Defina manifestos_validos() retornando Claude {"name": "analizza-leiloes", "version": "0.1.0"} e Codex com os mesmos campos, "skills": "./skills/" e interface com displayName, shortDescription, longDescription, developerName, category e capabilities. Inclua estes testes:

~~~python
def test_manifestos_compativeis_nao_produzem_erros(tmp_path: Path):
    (tmp_path / "skills").mkdir()
    claude, codex = manifestos_validos()
    assert validar_manifestos(claude, codex, tmp_path) == []

def test_versao_divergente_e_reportada(tmp_path: Path):
    (tmp_path / "skills").mkdir()
    claude, codex = manifestos_validos()
    codex["version"] = "0.2.0"
    assert "version diverge" in "\n".join(validar_manifestos(claude, codex, tmp_path))

def test_caminho_de_skills_diferente_e_reportado(tmp_path: Path):
    (tmp_path / "skills").mkdir()
    claude, codex = manifestos_validos()
    codex["skills"] = "./codex-skills/"
    assert "skills deve ser './skills/'" in "\n".join(validar_manifestos(claude, codex, tmp_path))

def test_diretorio_de_skills_ausente_e_reportado(tmp_path: Path):
    claude, codex = manifestos_validos()
    assert "diretório de skills não existe" in "\n".join(validar_manifestos(claude, codex, tmp_path))

def test_interface_incompleta_e_reportada(tmp_path: Path):
    (tmp_path / "skills").mkdir()
    claude, codex = manifestos_validos()
    del codex["interface"]["category"]
    assert "interface.category ausente" in "\n".join(validar_manifestos(claude, codex, tmp_path))
~~~

- [ ] **Step 2: Executar o teste e confirmar a falha**

Run: python3 -m pytest tools/tests/test_validate_plugin_manifests.py -q

Expected: FAIL durante coleta com ModuleNotFoundError para tools.validate_plugin_manifests.

- [ ] **Step 3: Implementar o mínimo para passar**

Crie tools/validate_plugin_manifests.py com json, sys e pathlib.Path. Implementar validar_manifestos para retornar, nesta ordem: erro contendo "name diverge" se os nomes diferirem; erro contendo "version diverge" se as versões diferirem; erro "skills deve ser './skills/'" se skills não for "./skills/"; erro "diretório de skills não existe" se plugin_dir / "skills" faltar; e "interface.<campo> ausente" para cada campo obrigatório ausente na interface.

O CLI calcula raiz = Path(__file__).resolve().parent.parent, lê os manifests Claude e Codex, transforma JSON malformado em "JSON inválido: <caminho>", imprime erros e retorna 1. Sem erros, imprime "manifestos multi-harness válidos" e retorna 0.

- [ ] **Step 4: Executar os testes unitários**

Run: python3 -m pytest tools/tests/test_validate_plugin_manifests.py -q

Expected: PASS, 5 testes.

- [ ] **Step 5: Integrar ao Makefile**

Substitua a receita validate por:

~~~make
validate: ## Valida os manifestos do marketplace, Claude e Codex
	claude plugin validate . && claude plugin validate $(PLUGIN_DIR) && python3 tools/validate_plugin_manifests.py
~~~

- [ ] **Step 6: Rodar a qualidade existente**

Run: make check

Expected: PASS, incluindo os cinco testes novos.

- [ ] **Step 7: Commit**

~~~bash
git add Makefile tools/validate_plugin_manifests.py tools/tests/test_validate_plugin_manifests.py
git commit -m "test: validate multi-harness plugin manifests"
~~~

### Task 2: Manifesto Codex para a skill canônica

**Files:**

- Create: plugins/analizza-leiloes/.codex-plugin/plugin.json
- Modify: tools/tests/test_validate_plugin_manifests.py

**Interfaces:**

- Consumes: validar_manifestos da Task 1 e plugins/analizza-leiloes/skills/.
- Produces: manifesto Codex de produção apontando para ./skills/.

- [ ] **Step 1: Escrever o teste de integração em vermelho**

Adicione:

~~~python
def test_manifestos_reais_respeitam_o_contrato():
    raiz = Path(__file__).resolve().parents[2]
    plugin_dir = raiz / "plugins/analizza-leiloes"
    claude = json.loads((plugin_dir / ".claude-plugin/plugin.json").read_text())
    codex = json.loads((plugin_dir / ".codex-plugin/plugin.json").read_text())
    assert validar_manifestos(claude, codex, plugin_dir) == []
~~~

- [ ] **Step 2: Executar o teste e confirmar a falha**

Run: python3 -m pytest tools/tests/test_validate_plugin_manifests.py::test_manifestos_reais_respeitam_o_contrato -q

Expected: FAIL com FileNotFoundError para .codex-plugin/plugin.json.

- [ ] **Step 3: Criar o manifesto Codex**

Crie plugins/analizza-leiloes/.codex-plugin/plugin.json:

~~~json
{
  "name": "analizza-leiloes",
  "version": "0.1.0",
  "description": "Skills da Analizza para análise de risco em leilão de imóveis",
  "author": {"name": "Diego Lirio", "email": "diegolirio.dl@gmail.com"},
  "homepage": "https://github.com/analizza-ai/business-marketplace",
  "repository": "https://github.com/analizza-ai/business-marketplace",
  "keywords": ["leilão", "imóveis", "análise de risco", "analizza"],
  "skills": "./skills/",
  "hooks": {},
  "interface": {
    "displayName": "Analizza Leilões",
    "shortDescription": "Triagem de riscos em leilões de imóveis",
    "longDescription": "Analise editais, matrículas, anúncios e laudos de leilões de imóveis com riscos ancorados no material fornecido.",
    "developerName": "Diego Lirio",
    "category": "Business",
    "capabilities": ["Read"],
    "defaultPrompt": ["Analise os riscos deste lote de leilão."]
  }
}
~~~

- [ ] **Step 4: Verificar o manifesto**

Run: python3 -m pytest tools/tests/test_validate_plugin_manifests.py -q && python3 tools/validate_plugin_manifests.py

Expected: PASS e saída final manifestos multi-harness válidos.

- [ ] **Step 5: Commit**

~~~bash
git add plugins/analizza-leiloes/.codex-plugin/plugin.json tools/tests/test_validate_plugin_manifests.py
git commit -m "feat: add Codex plugin manifest"
~~~

### Task 3: Documentação da distribuição

**Files:**

- Modify: README.md:1-61
- Modify: tools/tests/test_validate_plugin_manifests.py

**Interfaces:**

- Consumes: manifesto Codex e comandos Claude existentes.
- Produces: instruções verdadeiras para os dois harnesses sem inventar um CLI Codex.

- [ ] **Step 1: Escrever o teste em vermelho**

Adicione:

~~~python
def test_readme_documenta_claude_e_codex_sem_comando_inventado():
    raiz = Path(__file__).resolve().parents[2]
    readme = (raiz / "README.md").read_text(encoding="utf-8")
    assert "### Claude Code" in readme
    assert "### Codex" in readme
    assert "Plugins" in readme
    assert "codex plugin install" not in readme
~~~

- [ ] **Step 2: Executar o teste e confirmar a falha**

Run: python3 -m pytest tools/tests/test_validate_plugin_manifests.py::test_readme_documenta_claude_e_codex_sem_comando_inventado -q

Expected: FAIL porque o README não possui a seção Claude Code.

- [ ] **Step 3: Atualizar README.md**

Renomeie a seção Instalação para Instalação por harness. Sob ### Claude Code mantenha exatamente os comandos make marketplace-add e make install. Sob ### Codex instrua: abrir Plugins no app Codex, localizar Analizza Leilões após publicação no marketplace Codex e seguir o fluxo da interface; em desenvolvimento local, manter o manifesto .codex-plugin/plugin.json e usar o fluxo local suportado pela instalação. Na publicação, exija aumentar a mesma versão nos dois manifests, executar make validate e make check, então make tag. Atualize a árvore para mostrar os dois manifestos.

- [ ] **Step 4: Executar os testes e verificar o conteúdo**

Run: python3 -m pytest tools/tests/test_validate_plugin_manifests.py -q && rg -n '### Claude Code|### Codex|\.codex-plugin/plugin\.json' README.md

Expected: PASS; rg encontra as duas seções e o manifesto Codex.

- [ ] **Step 5: Commit**

~~~bash
git add README.md tools/tests/test_validate_plugin_manifests.py
git commit -m "docs: document Codex plugin distribution"
~~~

### Task 4: Verificação final

**Files:**

- Verify: plugins/analizza-leiloes/.claude-plugin/plugin.json
- Verify: plugins/analizza-leiloes/.codex-plugin/plugin.json
- Verify: tools/validate_plugin_manifests.py
- Verify: Makefile
- Verify: README.md

**Interfaces:**

- Consumes: Tasks 1–3.
- Produces: evidência reproduzível da distribuição com uma única árvore de skills.

- [ ] **Step 1: Rodar a suíte local**

Run: make check && python3 tools/validate_plugin_manifests.py

Expected: PASS, nenhum erro de catálogo e saída manifestos multi-harness válidos.

- [ ] **Step 2: Rodar a validação de release**

Run: make validate

Expected: PASS; Claude valida os manifestos próprios e Python valida o contrato Codex.

- [ ] **Step 3: Verificar ausência de duplicação**

Run: find plugins/analizza-leiloes -path '*/skills/analizza/SKILL.md' -type f -print

Expected: exatamente plugins/analizza-leiloes/skills/analizza/SKILL.md.

- [ ] **Step 4: Inspecionar o estado final**

Run: git diff --check && git status --short

Expected: nenhum erro de whitespace; a única modificação fora dos commits desta implementação é o arquivo preexistente docs/superpowers/specs/2026-08-17-analizza-leilao-skill-design.md.

## Plan Self-Review

- Cobertura: Tasks 1–2 implementam manifesto, caminho canônico, paridade e validação; Task 3 cobre documentação e release; Task 4 cobre todos os critérios de aceite.
- Placeholders: cada passo contém arquivos, testes, comandos e conteúdo concreto.
- Consistência: validar_manifestos é definido na Task 1 e consumido nas Tasks 2 e 3; versão 0.1.0 coincide com o manifesto Claude atual.
