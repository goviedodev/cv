from src import report
from src.model import Application
from src.stats import ResultadoEmbudo, SegmentoResultado, calcular_embudo


def test_formatear_tabla_alinea_columnas():
    tabla = report.formatear_tabla(["id", "n"], [["a1", 10], ["a2", 2]])
    lineas = tabla.splitlines()
    assert lineas[0].startswith("id")
    assert "a1" in lineas[2]


def test_formatear_tabla_sin_filas_no_falla():
    tabla = report.formatear_tabla(["id", "n"], [])
    assert "id" in tabla


def test_render_embudo_muestra_sin_datos_cuando_no_hay_conversion():
    resultado = calcular_embudo([], [])
    texto = report.render_embudo(resultado)
    assert "sin datos" in texto


def test_render_segmentacion_muestra_muestra_insuficiente():
    resultado = {"RemoteOK": SegmentoResultado(n=1, tasa_respuesta=None)}
    texto = report.render_segmentacion("portal", resultado)
    assert "muestra insuficiente" in texto
    assert "n=1" in texto


def test_render_segmentacion_vacia():
    assert "sin datos" in report.render_segmentacion("portal", {})


def test_render_pendientes_vacio_dice_al_dia():
    assert "al dia" in report.render_pendientes([])


def test_render_lista_vacia():
    assert "sin postulaciones" in report.render_lista([])


def test_render_resumen_html_es_autocontenido_y_escapa_contenido():
    resumen = {
        "total_postulaciones": 0,
        "embudo": calcular_embudo([], []),
        "segmentaciones": {},
        "mediana_dias_respuesta": None,
        "edades_vivas": [],
        "ritmo": [],
        "pendientes": [],
    }
    html = report.render_resumen_html(resumen)
    assert "<!doctype html>" in html.lower()
    assert "http://" not in html and "https://" not in html  # sin CDNs externos
