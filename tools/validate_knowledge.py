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
