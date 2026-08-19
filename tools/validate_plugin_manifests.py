import json
import sys
from pathlib import Path
from typing import Optional


CAMPOS_INTERFACE_OBRIGATORIOS = (
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
    "capabilities",
)


def validar_manifestos(claude: dict, codex: dict, plugin_dir: Path) -> list[str]:
    erros = []

    if claude.get("name") != codex.get("name"):
        erros.append("name diverge entre os manifestos")
    if claude.get("version") != codex.get("version"):
        erros.append("version diverge entre os manifestos")
    if codex.get("skills") != "./skills/":
        erros.append("skills deve ser './skills/'")
    if not (plugin_dir / "skills").is_dir():
        erros.append("diretório de skills não existe")

    interface = codex.get("interface", {})
    if not isinstance(interface, dict):
        interface = {}
    for campo in CAMPOS_INTERFACE_OBRIGATORIOS:
        if campo not in interface:
            erros.append(f"interface.{campo} ausente")

    return erros


def carregar_manifesto(caminho: Path) -> Optional[dict]:
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"JSON inválido: {caminho}")
        return None


def main() -> int:
    raiz = Path(__file__).resolve().parent.parent
    plugin_dir = raiz / "plugins" / "analizza-leiloes"
    caminho_claude = plugin_dir / ".claude-plugin" / "plugin.json"
    caminho_codex = plugin_dir / ".codex-plugin" / "plugin.json"

    claude = carregar_manifesto(caminho_claude)
    codex = carregar_manifesto(caminho_codex)
    if claude is None or codex is None:
        return 1

    erros = validar_manifestos(claude, codex, plugin_dir)
    if erros:
        print("\n".join(erros))
        return 1

    print("manifestos multi-harness válidos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
