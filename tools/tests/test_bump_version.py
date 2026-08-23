import pytest

from tools.bump_version import aplicar_versao, bump, versao_atual

CLAUDE_JSON = """{
  "name": "analizza-leiloes",
  "description": "Skills da Analizza para análise de risco em leilão de imóveis",
  "version": "0.1.1",
  "author": {
    "name": "Diego Lirio",
    "email": "diegolirio.dl@gmail.com"
  }
}
"""

CODEX_JSON = """{
  "name": "analizza-leiloes",
  "version": "0.1.1",
  "description": "Skills da Analizza para análise de risco em leilão de imóveis",
  "keywords": ["leilão", "imóveis"]
}
"""


@pytest.mark.parametrize(
    "versao,tipo,esperado",
    [
        ("0.1.1", "patch", "0.1.2"),
        ("0.1.1", "minor", "0.2.0"),
        ("0.1.1", "major", "1.0.0"),
        ("1.4.9", "patch", "1.4.10"),
        ("1.4.9", "minor", "1.5.0"),
        ("1.4.9", "major", "2.0.0"),
    ],
)
def test_bump_calcula_proxima_versao(versao, tipo, esperado):
    assert bump(versao, tipo) == esperado


def test_bump_rejeita_tipo_invalido():
    with pytest.raises(ValueError):
        bump("0.1.1", "revision")


def test_versao_atual_le_o_campo_version(tmp_path):
    caminho = tmp_path / "plugin.json"
    caminho.write_text(CLAUDE_JSON, encoding="utf-8")
    assert versao_atual(caminho) == "0.1.1"


def test_versao_atual_falha_sem_campo_version(tmp_path):
    caminho = tmp_path / "plugin.json"
    caminho.write_text('{"name": "sem-versao"}', encoding="utf-8")
    with pytest.raises(RuntimeError):
        versao_atual(caminho)


def test_aplicar_versao_atualiza_so_o_campo_version_preservando_o_resto(tmp_path):
    claude = tmp_path / "claude_plugin.json"
    codex = tmp_path / "codex_plugin.json"
    claude.write_text(CLAUDE_JSON, encoding="utf-8")
    codex.write_text(CODEX_JSON, encoding="utf-8")

    aplicar_versao("0.2.0", (claude, codex))

    claude_novo = claude.read_text(encoding="utf-8")
    codex_novo = codex.read_text(encoding="utf-8")

    assert '"version": "0.2.0"' in claude_novo
    assert '"version": "0.2.0"' in codex_novo
    # o resto do arquivo não deve ser tocado
    assert claude_novo == CLAUDE_JSON.replace('"version": "0.1.1"', '"version": "0.2.0"')
    assert codex_novo == CODEX_JSON.replace('"version": "0.1.1"', '"version": "0.2.0"')


def test_aplicar_versao_falha_se_campo_version_ausente(tmp_path):
    caminho = tmp_path / "plugin.json"
    caminho.write_text('{"name": "sem-versao"}', encoding="utf-8")
    with pytest.raises(RuntimeError):
        aplicar_versao("0.2.0", (caminho,))
