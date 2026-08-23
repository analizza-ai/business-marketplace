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
	claude plugin marketplace update $(MARKETPLACE) && claude plugin update $(PLUGIN)@$(MARKETPLACE)

##@ Release

.PHONY: validate
validate: ## Valida os manifestos do marketplace, Claude e Codex
	claude plugin validate . && claude plugin validate $(PLUGIN_DIR) && python3 tools/validate_plugin_manifests.py

ifneq (,$(filter tag,$(MAKECMDGOALS)))
_TAG_EXTRA  := $(filter-out tag,$(MAKECMDGOALS))
_TAG_INVALID := $(filter-out patch minor major,$(_TAG_EXTRA))
ifneq ($(_TAG_INVALID),)
$(error argumento inválido para 'make tag': '$(_TAG_INVALID)' — use patch, minor ou major)
endif
ifneq ($(word 2,$(_TAG_EXTRA)),)
$(error passe no máximo um tipo de bump para 'make tag' — recebido: $(_TAG_EXTRA))
endif
BUMP := $(if $(_TAG_EXTRA),$(_TAG_EXTRA),patch)
endif

.PHONY: tag
tag: ## Sobe a versão (patch por padrão; make tag minor|major) e cria a tag {plugin}--v{version}
	@set -e; \
	branch="$$(git rev-parse --abbrev-ref HEAD)"; \
	if [ "$$branch" != "main" ]; then \
		echo "make tag só roda na branch main (branch atual: $$branch)" >&2; \
		exit 1; \
	fi; \
	nova="$$(python3 tools/bump_version.py $(BUMP))"; \
	echo "Nova versão ($(BUMP)): $$nova"; \
	$(MAKE) validate; \
	git add $(PLUGIN_DIR)/.claude-plugin/plugin.json $(PLUGIN_DIR)/.codex-plugin/plugin.json; \
	git commit -m "chore($(PLUGIN)): bump version to $$nova ($(BUMP))"; \
	claude plugin tag $(PLUGIN_DIR)

.PHONY: patch minor major
patch minor major: ;

##@ Qualidade

.PHONY: check
check: ## Valida o catálogo de riscos e o índice de aulas
	python3 -m pytest tools/tests -q && python3 tools/validate_knowledge.py
