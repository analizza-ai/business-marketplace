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
