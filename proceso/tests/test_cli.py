import pytest

from src import cli, store
from src.model import ValidationError


DEFAULTS = cli.DEFAULT_CONFIG


@pytest.fixture
def rutas(tmp_path):
    apps = tmp_path / "applications.csv"
    events = tmp_path / "events.csv"
    store.ensure_files(apps, events)
    return apps, events


# --- configuracion --------------------------------------------------------------


def test_cargar_config_sin_archivo_devuelve_defaults(tmp_path):
    config = cli.cargar_config(tmp_path / "no-existe.toml")
    assert config["general"]["meta_semanal"] == DEFAULTS["general"]["meta_semanal"]
    assert "GetOnBoard" in config["portales"]["opciones"]


def test_cargar_config_lee_archivo_y_completa_faltantes(tmp_path):
    config_path = tmp_path / "config.toml"
    config_path.write_text(
        '[general]\nmeta_semanal = 10\n', encoding="utf-8"
    )
    config = cli.cargar_config(config_path)
    assert config["general"]["meta_semanal"] == 10
    # los campos no sobreescritos siguen viniendo del default
    assert config["general"]["min_muestra"] == DEFAULTS["general"]["min_muestra"]
    assert "GetOnBoard" in config["portales"]["opciones"]


# --- construir/registrar postulacion ---------------------------------------------


def test_construir_postulacion_genera_id_y_estado_postulado():
    app = cli.construir_postulacion(
        fecha_postulacion="2026-08-26",
        empresa="Equifax",
        cargo="Fullstack Senior",
        respuestas={"portal": "LinkedIn"},
    )
    assert app.id == "2026-08-26-equifax-fullstack-senior"
    assert app.estado_actual == "postulado"
    assert app.fecha_ultimo_evento == "2026-08-26"
    assert app.portal == "LinkedIn"


def test_registrar_postulacion_persiste_application_y_evento(rutas):
    apps_path, events_path = rutas
    app = cli.construir_postulacion(
        fecha_postulacion="2026-08-26", empresa="Equifax", cargo="Fullstack"
    )
    cli.registrar_postulacion(apps_path, events_path, app)

    guardadas = store.load_applications(apps_path)
    eventos = store.load_events(events_path)
    assert guardadas == [app]
    assert len(eventos) == 1
    assert eventos[0].etapa == "postulado"
    assert eventos[0].id_postulacion == app.id


def test_registrar_postulacion_duplicada_lanza_error(rutas):
    apps_path, events_path = rutas
    app = cli.construir_postulacion(
        fecha_postulacion="2026-08-26", empresa="Equifax", cargo="Fullstack"
    )
    cli.registrar_postulacion(apps_path, events_path, app)
    with pytest.raises(ValidationError):
        cli.registrar_postulacion(apps_path, events_path, app)


# --- flujo interactivo de add -------------------------------------------------------


def test_flujo_interactivo_add_usa_respuestas_en_orden():
    respuestas = iter(
        [
            "2026-08-26",  # fecha
            "Equifax",  # empresa
            "Fullstack",  # cargo
            "senior",  # seniority
            "LinkedIn",  # portal
            "",  # url
            "remoto",  # modalidad
            "Chile",  # pais
            "es",  # idioma_cv
            "generico-es",  # version_cv
            "elixir;react",  # stack
            "",  # salario_publicado
            "no",  # referido
            "manual",  # modo_postulacion
            "una nota",  # notas
        ]
    )
    app = cli.flujo_interactivo_add(entrada=lambda _prompt: next(respuestas))
    assert app.empresa == "Equifax"
    assert app.stack_tecnologias() == ("elixir", "react")
    assert app.modo_postulacion == "manual"
    assert app.notas == "una nota"


def test_flujo_interactivo_add_modo_postulacion_por_defecto_automatizada():
    respuestas = iter(
        [
            "2026-08-26",  # fecha
            "Equifax",  # empresa
            "Fullstack",  # cargo
        ]
        + [""] * 12  # el resto de campos opcionales vacios, incluyendo modo_postulacion
    )
    app = cli.flujo_interactivo_add(entrada=lambda _prompt: next(respuestas))
    assert app.modo_postulacion == "automatizada"


def test_flujo_interactivo_add_reintenta_campos_obligatorios_vacios():
    respuestas = iter(
        [
            "2026-08-26",  # fecha
            "",  # empresa vacia -> reintenta
            "Equifax",  # empresa
            "Fullstack",  # cargo
        ]
        + [""] * 12  # el resto de campos opcionales vacios (incluye modo_postulacion)
    )
    app = cli.flujo_interactivo_add(entrada=lambda _prompt: next(respuestas))
    assert app.empresa == "Equifax"


# --- actualizar postulacion --------------------------------------------------------


def test_actualizar_postulacion_agrega_evento_y_cambia_estado(rutas):
    apps_path, events_path = rutas
    app = cli.construir_postulacion(
        fecha_postulacion="2026-08-01", empresa="Equifax", cargo="Fullstack"
    )
    cli.registrar_postulacion(apps_path, events_path, app)

    actualizada = cli.actualizar_postulacion(
        apps_path, events_path, "equifax", "respuesta", "respondieron por correo",
        hoy_str="2026-08-05",
    )
    assert actualizada.estado_actual == "respuesta"
    assert actualizada.fecha_ultimo_evento == "2026-08-05"

    eventos = store.load_events(events_path)
    assert len(eventos) == 2
    assert eventos[-1].etapa == "respuesta"


def test_actualizar_postulacion_sin_coincidencias_lanza_error(rutas):
    apps_path, events_path = rutas
    with pytest.raises(ValidationError):
        cli.actualizar_postulacion(apps_path, events_path, "no-existe", "respuesta", "")


def test_actualizar_postulacion_ambigua_lanza_error(rutas):
    apps_path, events_path = rutas
    a1 = cli.construir_postulacion("2026-08-01", "Equifax Chile", "Backend")
    a2 = cli.construir_postulacion("2026-08-02", "Equifax Global", "Frontend")
    cli.registrar_postulacion(apps_path, events_path, a1)
    cli.registrar_postulacion(apps_path, events_path, a2)
    with pytest.raises(ValidationError):
        cli.actualizar_postulacion(apps_path, events_path, "equifax", "respuesta", "")


def test_actualizar_postulacion_etapa_invalida_lanza_error(rutas):
    apps_path, events_path = rutas
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, app)
    with pytest.raises(ValidationError):
        cli.actualizar_postulacion(apps_path, events_path, "equifax", "en proceso segun me dijeron", "")


# --- listar / pendientes / resumen --------------------------------------------------


def test_listar_filtra_por_estado_y_portal(rutas):
    apps_path, events_path = rutas
    a1 = cli.construir_postulacion(
        "2026-08-01", "Equifax", "Backend", respuestas={"portal": "LinkedIn"}
    )
    a2 = cli.construir_postulacion(
        "2026-08-02", "Otra", "Frontend", respuestas={"portal": "RemoteOK"}
    )
    cli.registrar_postulacion(apps_path, events_path, a1)
    cli.registrar_postulacion(apps_path, events_path, a2)

    solo_linkedin = cli.listar(apps_path, portal="linkedin")
    assert [a.id for a in solo_linkedin] == [a1.id]

    solo_postulado = cli.listar(apps_path, estado="postulado")
    assert len(solo_postulado) == 2


def test_obtener_pendientes_usa_umbrales_de_config(rutas):
    apps_path, events_path = rutas
    vieja = cli.construir_postulacion("2026-01-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, vieja)
    config = cli.cargar_config(None)
    pend = cli.obtener_pendientes(apps_path, config, hoy_str="2026-08-26")
    assert any(p["id"] == vieja.id and p["motivo"] == "sin_respuesta" for p in pend)


def test_calcular_resumen_agrega_todas_las_secciones(rutas):
    apps_path, events_path = rutas
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, app)
    config = cli.cargar_config(None)

    resumen = cli.calcular_resumen(apps_path, events_path, config, hoy_str="2026-08-26")
    assert resumen["total_postulaciones"] == 1
    assert "embudo" in resumen
    assert "segmentaciones" in resumen
    assert "ritmo" in resumen
    assert "pendientes" in resumen


# --- main() end-to-end (no interactivo) ---------------------------------------------


@pytest.fixture
def main_env(tmp_path, monkeypatch):
    apps_path = tmp_path / "data" / "applications.csv"
    events_path = tmp_path / "data" / "events.csv"
    apps_path.parent.mkdir(parents=True)
    monkeypatch.setattr(cli, "rutas_datos", lambda base_dir=None: (apps_path, events_path))
    monkeypatch.setattr(cli, "ruta_config", lambda base_dir=None: tmp_path / "config.toml")
    return apps_path, events_path


def test_main_list_no_interactivo(main_env, capsys):
    apps_path, events_path = main_env
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    store.ensure_files(apps_path, events_path)
    cli.registrar_postulacion(apps_path, events_path, app)

    codigo = cli.main(["list"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert "Equifax" in salida


def test_main_add_delega_en_flujo_interactivo(main_env, capsys, monkeypatch):
    apps_path, events_path = main_env
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    monkeypatch.setattr(cli, "flujo_interactivo_add", lambda: app)

    codigo = cli.main(["add"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert app.id in salida
    assert store.load_applications(apps_path) == [app]


def test_main_update_no_interactivo_con_flags(main_env, capsys):
    apps_path, events_path = main_env
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, app)

    codigo = cli.main(["update", "Equifax", "--etapa", "respuesta", "--nota", "llamaron"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert "respuesta" in salida


def test_main_update_con_etapa_sin_query_falla(main_env, capsys):
    codigo = cli.main(["update", "--etapa", "respuesta"])
    salida = capsys.readouterr().err
    assert codigo == 1
    assert "falta la empresa o id" in salida


def test_main_update_etapa_invalida_reporta_error(main_env, capsys):
    apps_path, events_path = main_env
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, app)

    codigo = cli.main(["update", "Equifax", "--etapa", "no-es-una-etapa"])
    salida = capsys.readouterr().err
    assert codigo == 1
    assert "error:" in salida


def test_main_update_interactivo_sin_flags(main_env, capsys, monkeypatch):
    apps_path, events_path = main_env
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, app)
    monkeypatch.setattr(
        cli, "flujo_interactivo_update", lambda: ("Equifax", "respuesta", "nota")
    )

    codigo = cli.main(["update"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert "respuesta" in salida


def test_main_pending(main_env, capsys):
    apps_path, events_path = main_env
    codigo = cli.main(["pending"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert "al dia" in salida


def test_main_stats(main_env, capsys):
    apps_path, events_path = main_env
    app = cli.construir_postulacion("2026-08-01", "Equifax", "Backend")
    cli.registrar_postulacion(apps_path, events_path, app)

    codigo = cli.main(["stats"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert "EMBUDO" in salida


def test_main_report_genera_html(main_env, capsys, tmp_path):
    apps_path, events_path = main_env
    salida_html = tmp_path / "reporte.html"

    codigo = cli.main(["report", "--out", str(salida_html)])
    consola = capsys.readouterr().out
    assert codigo == 0
    assert salida_html.exists()
    assert "doctype html" in salida_html.read_text(encoding="utf-8").lower()
    assert str(salida_html) in consola


def test_main_report_acepta_flag_html(main_env, capsys, tmp_path):
    apps_path, events_path = main_env
    salida_html = tmp_path / "reporte2.html"

    codigo = cli.main(["report", "--html", "--out", str(salida_html)])
    assert codigo == 0
    assert salida_html.exists()


def test_ruta_config_y_rutas_datos_usan_repo_root_por_default():
    assert cli.ruta_config().name == "config.toml"
    apps_path, events_path = cli.rutas_datos()
    assert apps_path.name == "applications.csv"
    assert events_path.name == "events.csv"


def test_flujo_interactivo_update_arma_query_etapa_nota():
    respuestas = iter(["Equifax", "respuesta", "llamaron"])
    query, etapa, nota = cli.flujo_interactivo_update(
        entrada=lambda _prompt: next(respuestas)
    )
    assert (query, etapa, nota) == ("Equifax", "respuesta", "llamaron")


# --- --help ---------------------------------------------------------------------------


def test_help_no_falla_y_documenta_los_seis_comandos(capsys):
    with pytest.raises(SystemExit) as exc:
        cli.main(["--help"])
    assert exc.value.code == 0
    salida = capsys.readouterr().out
    for comando in ("add", "update", "list", "pending", "stats", "report"):
        assert comando in salida


def test_help_incluye_epilogo_con_etapas_y_config(capsys):
    with pytest.raises(SystemExit):
        cli.main(["--help"])
    salida = capsys.readouterr().out
    # etapas del embudo (contrato de negocio que mas se olvida)
    assert "entrevista_tecnica" in salida
    assert "descartado_por_mi" in salida
    # umbrales de config.toml, para no tener que abrir el archivo
    assert "umbral_sin_respuesta_dias" in salida
    # la limitacion mas importante para no asumir que existe
    assert "no acepta flags no" in salida or "no interactivos" in salida
