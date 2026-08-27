import pytest

from src import stats
from src.model import Application, Event


def _app(id, fecha_postulacion="2026-08-01", estado_actual="postulado", **kwargs):
    datos = dict(
        id=id,
        fecha_postulacion=fecha_postulacion,
        empresa=kwargs.pop("empresa", "Empresa"),
        cargo=kwargs.pop("cargo", "Cargo"),
        estado_actual=estado_actual,
    )
    datos.update(kwargs)
    return Application(**datos)


def _ev(id, fecha, etapa, nota=""):
    return Event(id_postulacion=id, fecha=fecha, etapa=etapa, nota=nota)


# --- embudo -----------------------------------------------------------------


def test_embudo_con_cero_postulaciones_no_falla():
    resultado = stats.calcular_embudo([], [])
    assert resultado.conteos["postulado"] == 0
    assert resultado.conversiones["postulado->respuesta"] is None


def test_embudo_todas_sin_respuesta():
    apps = [_app("a1"), _app("a2")]
    events = [_ev("a1", "2026-08-01", "postulado"), _ev("a2", "2026-08-01", "postulado")]
    resultado = stats.calcular_embudo(apps, events)
    assert resultado.conteos["postulado"] == 2
    assert resultado.conteos["respuesta"] == 0
    assert resultado.conversiones["postulado->respuesta"] == 0.0


def test_embudo_postulacion_que_salta_etapas_cuenta_intermedias():
    # Llega directo a entrevista_tecnica sin evento explícito de respuesta/screening.
    apps = [_app("a1")]
    events = [
        _ev("a1", "2026-08-01", "postulado"),
        _ev("a1", "2026-08-05", "entrevista_tecnica"),
    ]
    resultado = stats.calcular_embudo(apps, events)
    assert resultado.conteos["postulado"] == 1
    assert resultado.conteos["respuesta"] == 1
    assert resultado.conteos["screening"] == 1
    assert resultado.conteos["entrevista_tecnica"] == 1
    assert resultado.conteos["entrevista_final"] == 0


def test_embudo_conversion_entre_etapas():
    apps = [_app("a1"), _app("a2"), _app("a3")]
    events = [
        _ev("a1", "2026-08-01", "postulado"),
        _ev("a2", "2026-08-01", "postulado"),
        _ev("a2", "2026-08-05", "respuesta"),
        _ev("a3", "2026-08-01", "postulado"),
        _ev("a3", "2026-08-05", "respuesta"),
    ]
    resultado = stats.calcular_embudo(apps, events)
    assert resultado.conteos["postulado"] == 3
    assert resultado.conteos["respuesta"] == 2
    assert resultado.conversiones["postulado->respuesta"] == pytest.approx(2 / 3)


def test_embudo_cuenta_terminales_aparte():
    apps = [_app("a1", estado_actual="rechazado"), _app("a2", estado_actual="descartado_por_mi")]
    events = [_ev("a1", "2026-08-01", "postulado"), _ev("a2", "2026-08-01", "postulado")]
    resultado = stats.calcular_embudo(apps, events)
    assert resultado.terminales["rechazado"] == 1
    assert resultado.terminales["descartado_por_mi"] == 1


# --- segmentación -------------------------------------------------------------


def test_segmentacion_suprime_tasa_con_muestra_insuficiente():
    apps = [_app("a1", portal="RemoteOK")]
    events = [_ev("a1", "2026-08-01", "postulado")]
    resultado = stats.segmentar_tasa_respuesta(apps, events, "portal", min_muestra=5)
    assert resultado["RemoteOK"].n == 1
    assert resultado["RemoteOK"].tasa_respuesta is None


def test_segmentacion_reporta_tasa_con_muestra_suficiente():
    apps = [_app(f"a{i}", portal="LinkedIn") for i in range(5)]
    events = [_ev("a0", "2026-08-01", "respuesta")] + [
        _ev(f"a{i}", "2026-08-01", "postulado") for i in range(5)
    ]
    resultado = stats.segmentar_tasa_respuesta(apps, events, "portal", min_muestra=5)
    assert resultado["LinkedIn"].n == 5
    assert resultado["LinkedIn"].tasa_respuesta == pytest.approx(1 / 5)


def test_segmentacion_por_stack_cuenta_una_postulacion_en_cada_tecnologia():
    apps = [_app("a1", stack="elixir;react")]
    events = [_ev("a1", "2026-08-01", "postulado")]
    resultado = stats.segmentar_tasa_respuesta(apps, events, "stack", min_muestra=1)
    assert resultado["elixir"].n == 1
    assert resultado["react"].n == 1


def test_segmentacion_agrupa_valor_vacio_como_sin_dato():
    apps = [_app("a1", portal="")]
    events = [_ev("a1", "2026-08-01", "postulado")]
    resultado = stats.segmentar_tasa_respuesta(apps, events, "portal", min_muestra=1)
    assert "(sin dato)" in resultado


# --- tiempos -------------------------------------------------------------------


def test_mediana_dias_hasta_respuesta_usa_mediana_no_promedio():
    # Días: 1, 2, 100 -> mediana 2, promedio ~34.3. Un outlier no debe distorsionar.
    apps = [_app("a1", "2026-08-01"), _app("a2", "2026-08-01"), _app("a3", "2026-08-01")]
    events = [
        _ev("a1", "2026-08-01", "postulado"),
        _ev("a1", "2026-08-02", "respuesta"),
        _ev("a2", "2026-08-01", "postulado"),
        _ev("a2", "2026-08-03", "respuesta"),
        _ev("a3", "2026-08-01", "postulado"),
        _ev("a3", "2026-11-09", "respuesta"),
    ]
    mediana = stats.mediana_dias_hasta_respuesta(apps, events)
    assert mediana == 2


def test_mediana_dias_hasta_respuesta_sin_datos_es_none():
    assert stats.mediana_dias_hasta_respuesta([], []) is None


def test_edad_postulaciones_vivas_excluye_terminales():
    apps = [
        _app("a1", "2026-08-01"),
        _app("a2", "2026-08-01", estado_actual="rechazado"),
    ]
    edades = stats.edad_postulaciones_vivas(apps, hoy_str="2026-08-11")
    ids = [id_ for id_, _dias in edades]
    assert ids == ["a1"]
    assert edades[0][1] == 10


# --- pendientes / follow-up -----------------------------------------------------


def test_pendientes_marca_seguimiento_y_sin_respuesta_por_separado():
    apps = [
        _app("a1", "2026-08-01", fecha_ultimo_evento="2026-08-01"),  # 10 dias, en curso
        _app("a2", "2026-07-01", fecha_ultimo_evento="2026-07-01"),  # 41 dias, postulado
    ]
    resultado = stats.pendientes(
        apps, umbral_seguimiento_dias=7, umbral_sin_respuesta_dias=21, hoy_str="2026-08-11"
    )
    por_id = {r["id"]: r for r in resultado}
    assert por_id["a1"]["motivo"] == "seguimiento"
    assert por_id["a2"]["motivo"] == "sin_respuesta"


def test_pendientes_ignora_terminales():
    apps = [_app("a1", "2026-01-01", estado_actual="rechazado", fecha_ultimo_evento="2026-01-01")]
    resultado = stats.pendientes(apps, hoy_str="2026-08-11")
    assert resultado == []


# --- ritmo semanal ---------------------------------------------------------------


def test_ritmo_semanal_agrupa_por_semana_iso():
    apps = [_app("a1", "2026-08-03"), _app("a2", "2026-08-04"), _app("a3", "2026-08-10")]
    ritmo = stats.ritmo_semanal(apps, semanas=2, hoy_str="2026-08-11")
    assert len(ritmo) == 2
    assert ritmo[0]["postulaciones"] == 2
    assert ritmo[1]["postulaciones"] == 1


def test_cumplimiento_meta_marca_semanas_bajo_meta():
    ritmo = [{"semana": "2026-08-03", "postulaciones": 2}]
    resultado = stats.cumplimiento_meta(ritmo, meta_semanal=5)
    assert resultado[0]["cumplio_meta"] is False
