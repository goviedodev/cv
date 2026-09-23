import pytest

from src.model import Application, Event, ValidationError
from src import store


@pytest.fixture
def apps_csv(tmp_path):
    return tmp_path / "applications.csv"


@pytest.fixture
def events_csv(tmp_path):
    return tmp_path / "events.csv"


def _app(id="2026-08-26-equifax-fullstack", **kwargs):
    datos = dict(
        id=id,
        fecha_postulacion="2026-08-26",
        empresa="Equifax",
        cargo="Fullstack",
    )
    datos.update(kwargs)
    return Application(**datos)


def test_ensure_files_crea_csv_con_headers_si_no_existen(tmp_path):
    apps_csv = tmp_path / "applications.csv"
    events_csv = tmp_path / "events.csv"
    store.ensure_files(apps_csv, events_csv)
    assert apps_csv.exists()
    assert events_csv.exists()
    assert store.load_applications(apps_csv) == []
    assert store.load_events(events_csv) == []


def test_save_y_load_applications_roundtrip(apps_csv):
    app = _app(notas="con tildes ñ, comas y \"comillas\"")
    store.save_applications(apps_csv, [app])
    cargadas = store.load_applications(apps_csv)
    assert cargadas == [app]


def test_save_y_load_events_roundtrip(events_csv):
    ev = Event(id_postulacion="x", fecha="2026-08-26", etapa="postulado")
    store.save_events(events_csv, [ev])
    assert store.load_events(events_csv) == [ev]


def test_load_applications_con_campos_vacios(apps_csv):
    apps_csv.write_text(
        "id,fecha_postulacion,empresa,cargo,seniority,portal,url,modalidad,"
        "pais,idioma_cv,version_cv,stack,salario_publicado,referido,"
        "modo_postulacion,estado_actual,fecha_ultimo_evento,notas\n"
        "x,2026-08-26,Equifax,Fullstack,,,,,,,,,,no,automatizada,postulado,,\n"
    )
    cargadas = store.load_applications(apps_csv)
    assert len(cargadas) == 1
    assert cargadas[0].seniority == ""
    assert cargadas[0].portal == ""


def test_agregar_postulacion_devuelve_nueva_lista_sin_mutar(apps_csv):
    store.save_applications(apps_csv, [])
    original = store.load_applications(apps_csv)
    app = _app()
    nueva_lista = store.agregar_postulacion(original, app)
    assert original == []
    assert nueva_lista == [app]


def test_agregar_postulacion_rechaza_id_duplicado():
    app = _app()
    with pytest.raises(ValidationError):
        store.agregar_postulacion([app], _app())


def test_agregar_evento_devuelve_nueva_lista(events_csv):
    ev = Event(id_postulacion="x", fecha="2026-08-26", etapa="postulado")
    nueva = store.agregar_evento([], ev)
    assert nueva == [ev]


def test_actualizar_estado_aplicacion_reemplaza_solo_la_indicada():
    a1 = _app(id="a1")
    a2 = _app(id="a2", empresa="Otra")
    actualizadas = store.actualizar_estado_aplicacion(
        [a1, a2], "a1", "respuesta", "2026-08-30"
    )
    a1_actualizada = next(a for a in actualizadas if a.id == "a1")
    a2_intacta = next(a for a in actualizadas if a.id == "a2")
    assert a1_actualizada.estado_actual == "respuesta"
    assert a1_actualizada.fecha_ultimo_evento == "2026-08-30"
    assert a2_intacta == a2
    # el original no debe mutarse
    assert a1.estado_actual == "postulado"


def test_actualizar_estado_aplicacion_id_inexistente_lanza_error():
    with pytest.raises(ValidationError):
        store.actualizar_estado_aplicacion([_app()], "no-existe", "respuesta", "2026-08-30")


def test_buscar_por_empresa_o_id_es_insensible_a_mayusculas():
    a1 = _app(id="a1", empresa="Equifax")
    a2 = _app(id="a2", empresa="Otra Empresa")
    resultados = store.buscar_por_empresa_o_id([a1, a2], "equifax")
    assert resultados == [a1]
    resultados_por_id = store.buscar_por_empresa_o_id([a1, a2], "a2")
    assert resultados_por_id == [a2]


def test_save_applications_ordena_por_fecha_e_id_para_diffs_estables(apps_csv):
    a1 = _app(id="2026-08-27-b", fecha_postulacion="2026-08-27")
    a2 = _app(id="2026-08-26-a", fecha_postulacion="2026-08-26")
    store.save_applications(apps_csv, [a1, a2])
    cargadas = store.load_applications(apps_csv)
    assert [a.id for a in cargadas] == ["2026-08-26-a", "2026-08-27-b"]
