import json
from pathlib import Path

from tools.validate_plugin_manifests import validar_manifestos


def manifestos_validos():
    claude = {"name": "analizza-leiloes", "version": "0.1.0"}
    codex = {
        "name": "analizza-leiloes",
        "version": "0.1.0",
        "skills": "./skills/",
        "interface": {
            "displayName": "Analizza Leilões",
            "shortDescription": "Triagem de riscos",
            "longDescription": "Análise de riscos em leilões de imóveis.",
            "developerName": "Diego Lirio",
            "category": "Business",
            "capabilities": ["Read"],
        },
    }
    return claude, codex


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
    assert "skills deve ser './skills/'" in "\n".join(
        validar_manifestos(claude, codex, tmp_path)
    )


def test_diretorio_de_skills_ausente_e_reportado(tmp_path: Path):
    claude, codex = manifestos_validos()
    assert "diretório de skills não existe" in "\n".join(
        validar_manifestos(claude, codex, tmp_path)
    )


def test_interface_incompleta_e_reportada(tmp_path: Path):
    (tmp_path / "skills").mkdir()
    claude, codex = manifestos_validos()
    del codex["interface"]["category"]
    assert "interface.category ausente" in "\n".join(
        validar_manifestos(claude, codex, tmp_path)
    )


def test_manifestos_reais_respeitam_o_contrato():
    raiz = Path(__file__).resolve().parents[2]
    plugin_dir = raiz / "plugins/analizza-leiloes"
    claude = json.loads((plugin_dir / ".claude-plugin/plugin.json").read_text())
    codex = json.loads((plugin_dir / ".codex-plugin/plugin.json").read_text())
    assert validar_manifestos(claude, codex, plugin_dir) == []


def test_readme_documenta_claude_e_codex_sem_comando_inventado():
    raiz = Path(__file__).resolve().parents[2]
    readme = (raiz / "README.md").read_text(encoding="utf-8")
    assert "### Claude Code" in readme
    assert "### Codex" in readme
    assert "Plugins" in readme
    assert "codex plugin install" not in readme
