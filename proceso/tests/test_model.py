import pytest

from src.model import (
    Application,
    Event,
    ValidationError,
    generar_id,
    validar_etapa,
    validar_fecha,
)


def test_validar_fecha_ok():
    assert validar_fecha("2026-08-26") == "2026-08-26"


@pytest.mark.parametrize(
    "valor",
    ["2026-8-26", "26-08-2026", "2026-08-26 16:47", "no es fecha", "", "2026-13-01"],
)
def test_validar_fecha_rechaza_formatos_invalidos(valor):
    with pytest.raises(ValidationError):
        validar_fecha(valor)


def test_validar_etapa_ok():
    assert validar_etapa("postulado") == "postulado"
    assert validar_etapa("rechazado") == "rechazado"


def test_validar_etapa_rechaza_prosa_libre():
    # Esto es exactamente el defecto de cv_job_links.md: prosa en el campo estado.
    with pytest.raises(ValidationError):
        validar_etapa("Descartada - backend Node.js no calza")


def test_generar_id_es_slug_ascii_estable():
    id_ = generar_id("2026-08-26", "Equifax", "Fullstack Sénior")
    assert id_ == "2026-08-26-equifax-fullstack-senior"


def test_generar_id_valida_fecha():
    with pytest.raises(ValidationError):
        generar_id("26/08/2026", "Equifax", "Fullstack")


def test_application_minima_valida():
    app = Application(
        id="2026-08-26-equifax-fullstack",
        fecha_postulacion="2026-08-26",
        empresa="Equifax",
        cargo="Fullstack",
    )
    assert app.estado_actual == "postulado"
    assert app.referido == "no"


def test_application_rechaza_empresa_vacia():
    with pytest.raises(ValidationError):
        Application(
            id="x", fecha_postulacion="2026-08-26", empresa="  ", cargo="Fullstack"
        )


def test_application_rechaza_estado_invalido():
    with pytest.raises(ValidationError):
        Application(
            id="x",
            fecha_postulacion="2026-08-26",
            empresa="Equifax",
            cargo="Fullstack",
            estado_actual="Generado",  # no es una etapa del embudo
        )


def test_application_es_inmutable():
    app = Application(
        id="x", fecha_postulacion="2026-08-26", empresa="Equifax", cargo="Fullstack"
    )
    with pytest.raises(AttributeError):
        app.empresa = "Otra"  # type: ignore[misc]


def test_application_con_cambios_no_muta_original():
    app = Application(
        id="x", fecha_postulacion="2026-08-26", empresa="Equifax", cargo="Fullstack"
    )
    app2 = app.con_cambios(estado_actual="respuesta", fecha_ultimo_evento="2026-08-27")
    assert app.estado_actual == "postulado"
    assert app2.estado_actual == "respuesta"
    assert app is not app2


def test_application_stack_tecnologias_parsea_separador():
    app = Application(
        id="x",
        fecha_postulacion="2026-08-26",
        empresa="Equifax",
        cargo="Fullstack",
        stack="elixir; react ;postgres",
    )
    assert app.stack_tecnologias() == ("elixir", "react", "postgres")


def test_application_roundtrip_row():
    app = Application(
        id="x",
        fecha_postulacion="2026-08-26",
        empresa="Equifax",
        cargo="Fullstack",
        notas="notas con comas, tildes y ñ",
    )
    row = app.to_row()
    app2 = Application.from_row(row)
    assert app == app2


def test_event_valido():
    ev = Event(id_postulacion="x", fecha="2026-08-26", etapa="postulado")
    assert ev.etapa == "postulado"


def test_event_rechaza_id_vacio():
    with pytest.raises(ValidationError):
        Event(id_postulacion="  ", fecha="2026-08-26", etapa="postulado")


def test_event_roundtrip_row():
    ev = Event(id_postulacion="x", fecha="2026-08-26", etapa="oferta", nota="nota, con comas")
    assert Event.from_row(ev.to_row()) == ev
