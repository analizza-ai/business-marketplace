"""Sobe a versão do plugin analizza-leiloes nos dois manifestos (Claude e Codex)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent / "plugins" / "analizza-leiloes"
MANIFESTOS = (
    PLUGIN_DIR / ".claude-plugin" / "plugin.json",
    PLUGIN_DIR / ".codex-plugin" / "plugin.json",
)
TIPOS_VALIDOS = ("patch", "minor", "major")

VERSION_RE = re.compile(r'("version":\s*")(\d+)\.(\d+)\.(\d+)(")')


def bump(versao: str, tipo: str) -> str:
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"tipo de bump inválido: {tipo}")
    major, minor, patch = (int(p) for p in versao.split("."))
    if tipo == "major":
        return f"{major + 1}.0.0"
    if tipo == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def versao_atual(caminho: Path) -> str:
    texto = caminho.read_text(encoding="utf-8")
    match = VERSION_RE.search(texto)
    if match is None:
        raise RuntimeError(f'campo "version" não encontrado em {caminho}')
    return f"{match.group(2)}.{match.group(3)}.{match.group(4)}"


def aplicar_versao(nova_versao: str, caminhos: tuple[Path, ...]) -> None:
    for caminho in caminhos:
        texto = caminho.read_text(encoding="utf-8")
        novo_texto, n = VERSION_RE.subn(rf"\g<1>{nova_versao}\g<5>", texto, count=1)
        if n != 1:
            raise RuntimeError(f'campo "version" não encontrado em {caminho}')
        caminho.write_text(novo_texto, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in TIPOS_VALIDOS:
        print(f"uso: bump_version.py <{'|'.join(TIPOS_VALIDOS)}>", file=sys.stderr)
        return 1
    tipo = sys.argv[1]
    atual = versao_atual(MANIFESTOS[0])
    nova = bump(atual, tipo)
    aplicar_versao(nova, MANIFESTOS)
    print(nova)
    return 0


if __name__ == "__main__":
    sys.exit(main())
