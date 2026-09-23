"""CLI de captura y consulta: track add | update | list | pending | stats | report.

Objetivo de diseño: registrar una postulación debe costar ~20 segundos.
Si cuesta más, el sistema se abandona (ver organizador-postulaciones/, vacío
desde hace meses).
"""

from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path
from typing import Callable

from . import report, stats, store
from .model import Application, Event, ValidationError, generar_id
from .model import hoy as _hoy_str

REPO_ROOT = Path(__file__).resolve().parent.parent

DESCRIPCION = (
    "Registro y seguimiento de postulaciones. Los datos viven en dos CSV "
    "versionados en git: data/applications.csv (estado actual) y "
    "data/events.csv (historial de etapas)."
)

# Ayuda extendida de `track --help`. Se mantiene aqui, y no en el README,
# porque es lo que se consulta cuando ya se olvido como funciona el sistema:
# a esa altura nadie abre un archivo, se escribe --help.
AYUDA_EXTENDIDA = """\
COMANDOS

  add                 Registrar una postulacion (interactivo, ~20s)
  update <query>      Avanzar de etapa
  list                Listar postulaciones, con filtros
  pending             Que requiere seguimiento hoy
  stats               Embudo, segmentacion, tiempos y ritmo
  report --html       Lo mismo, como pagina HTML autocontenida


--- add ---

  ./track add

  Pregunta 14 campos: empresa*, cargo*, seniority, portal, url, modalidad,
  pais, idioma_cv, version_cv, stack (separado por ';'), salario_publicado,
  referido (si/no), modo_postulacion (automatizada/manual, default
  'automatizada') y notas. Solo empresa y cargo son obligatorios (*).

  Genera el id automatico (2026-08-27-fullstack-elixir-backend-engineer),
  deja la postulacion en estado 'postulado' y crea el evento inicial del
  historial. No acepta flags: es solo interactivo.


--- update ---

  ./track update "Lisit" --etapa respuesta --nota "escribio la reclutadora"
  ./track update "Lisit"        # interactivo si no pasas --etapa

  Busca por empresa o por id. Si el texto coincide con 2 o mas
  postulaciones falla con un error de ambiguedad en vez de adivinar.

  Etapas del embudo, en orden:
    postulado -> respuesta -> screening -> entrevista_tecnica ->
    entrevista_final -> oferta -> aceptada
  Terminales (fuera del embudo lineal): rechazado, descartado_por_mi


--- list ---

  ./track list
  ./track list --estado postulado
  ./track list --portal GetOnBoard      # no distingue mayusculas


--- pending ---

  ./track pending

  Dos motivos, segun los umbrales de config.toml:
    seguimiento    >= 7 dias sin ningun evento nuevo
    sin_respuesta  >= 21 dias todavia en 'postulado'
  Ordenado por dias sin novedades, de mayor a menor.

  'sin_respuesta' nunca se marca a mano: se deriva del tiempo transcurrido,
  asi no hay que ir cerrando a mano las postulaciones muertas.


--- stats ---

  ./track stats

  Cuatro bloques:
    EMBUDO           conteo por etapa, conversion entre etapas
                     consecutivas y estados terminales
    QUE FUNCIONA     tasa de respuesta segmentada por portal, idioma_cv,
    MEJOR            version_cv, seniority, modalidad, referido,
                     modo_postulacion y stack
    TIEMPOS          mediana de dias hasta la primera respuesta y
                     postulaciones vivas mas antiguas sin novedades
    RITMO SEMANAL    ultimas 8 semanas contra la meta semanal


--- report ---

  ./track report --html
  ./track report --html --out ~/informe.html

  Sin --out escribe report.html en la raiz del repo.


COMO SE CALCULAN LAS COSAS

  * La segmentacion es lo que da valor a largo plazo: con min_muestra=5
    ningun segmento con menos de 5 postulaciones muestra porcentaje. Con
    ~40-50 postulaciones empieza a decir si el CV en ingles responde mas
    que el que esta en castellano, si un portal convierte mejor que otro,
    o que stack contesta.
  * Dias hasta respuesta usa mediana, no promedio: una empresa que tardo
    100 dias no distorsiona el numero de las demas.
  * El embudo se calcula del historial, no del estado actual: si saltas de
    'postulado' directo a 'entrevista_tecnica', las etapas intermedias
    cuentan igual como alcanzadas.


CONFIGURACION (config.toml)

  meta_semanal               postulaciones por semana que consideras meta
  umbral_seguimiento_dias    dias sin evento antes de sugerir seguimiento
  umbral_sin_respuesta_dias  dias en 'postulado' antes de sin_respuesta
  min_muestra                minimo de n para reportar un porcentaje
  portales.opciones          portales sugeridos en 'track add'


LO QUE NO TIENE

  No hay comando delete (se edita el CSV a mano), 'add' no acepta flags no
  interactivos, no hay import masivo desde cv_job_links.md, y no hay
  comando para ver el historial de eventos de una postulacion puntual.
"""

DEFAULT_CONFIG: dict = {
    "general": {
        "meta_semanal": 5,
        "umbral_seguimiento_dias": 7,
        "umbral_sin_respuesta_dias": 21,
        "min_muestra": 5,
    },
    "portales": {
        "opciones": [
            "GetOnBoard",
            "Computrabajo",
            "LinkedIn",
            "Michael Page",
            "RemoteOK",
            "Indeed",
            "Trabajando",
            "Himalayas",
            "ElixirRadar",
            "Directo",
            "Referido",
        ]
    },
}

CAMPOS_INTERACTIVOS: tuple[tuple[str, str, bool], ...] = (
    ("empresa", "Empresa", True),
    ("cargo", "Cargo", True),
    ("seniority", "Seniority (junior/mid/senior/staff)", False),
    ("portal", "Portal", False),
    ("url", "URL de la oferta", False),
    ("modalidad", "Modalidad (remoto/hibrido/presencial)", False),
    ("pais", "Pais", False),
    ("idioma_cv", "Idioma del CV usado (es/en)", False),
    ("version_cv", "Version de CV usada", False),
    ("stack", "Stack, separado por ; (ej: elixir;react)", False),
    ("salario_publicado", "Salario publicado", False),
    ("referido", "Referido (si/no)", False),
    ("modo_postulacion", "Modo de postulacion (automatizada/manual)", False),
    ("notas", "Notas", False),
)

CAMPOS_SEGMENTACION: tuple[str, ...] = (
    "portal",
    "idioma_cv",
    "version_cv",
    "seniority",
    "modalidad",
    "referido",
    "modo_postulacion",
    "stack",
)


# --- configuracion y rutas -----------------------------------------------------------


def _merge_config(base: dict, override: dict) -> dict:
    resultado = {seccion: dict(valores) for seccion, valores in base.items()}
    for seccion, valores in override.items():
        resultado.setdefault(seccion, {})
        resultado[seccion].update(valores)
    return resultado


def cargar_config(path: Path | None) -> dict:
    if path is None or not Path(path).exists():
        return _merge_config(DEFAULT_CONFIG, {})
    with open(path, "rb") as f:
        datos = tomllib.load(f)
    return _merge_config(DEFAULT_CONFIG, datos)


def ruta_config(base_dir: Path | None = None) -> Path:
    return (base_dir or REPO_ROOT) / "config.toml"


def rutas_datos(base_dir: Path | None = None) -> tuple[Path, Path]:
    data_dir = (base_dir or REPO_ROOT) / "data"
    return data_dir / "applications.csv", data_dir / "events.csv"


# --- construir / registrar postulacion ------------------------------------------------


def construir_postulacion(
    fecha_postulacion: str,
    empresa: str,
    cargo: str,
    respuestas: dict | None = None,
) -> Application:
    respuestas = dict(respuestas or {})
    id_ = generar_id(fecha_postulacion, empresa, cargo)
    return Application(
        id=id_,
        fecha_postulacion=fecha_postulacion,
        empresa=empresa,
        cargo=cargo,
        estado_actual="postulado",
        fecha_ultimo_evento=fecha_postulacion,
        **respuestas,
    )


def registrar_postulacion(apps_path: Path, events_path: Path, app: Application) -> None:
    apps = store.load_applications(apps_path)
    events = store.load_events(events_path)
    nuevas_apps = store.agregar_postulacion(apps, app)  # valida duplicados
    evento = Event(
        id_postulacion=app.id,
        fecha=app.fecha_postulacion,
        etapa="postulado",
        nota="postulacion creada",
    )
    nuevos_events = store.agregar_evento(events, evento)
    store.save_applications(apps_path, nuevas_apps)
    store.save_events(events_path, nuevos_events)


def flujo_interactivo_add(
    entrada: Callable[[str], str] = input, hoy_str: str | None = None
) -> Application:
    fecha_default = hoy_str or _hoy_str()
    fecha = entrada(f"Fecha de postulacion [{fecha_default}]: ").strip() or fecha_default

    respuestas: dict[str, str] = {}
    for campo, etiqueta, obligatorio in CAMPOS_INTERACTIVOS:
        valor = entrada(f"{etiqueta}: ").strip()
        while obligatorio and not valor:
            valor = entrada(f"{etiqueta} (obligatorio, no puede quedar vacio): ").strip()
        respuestas[campo] = valor

    empresa = respuestas.pop("empresa")
    cargo = respuestas.pop("cargo")
    if not respuestas.get("referido"):
        respuestas["referido"] = "no"
    if not respuestas.get("modo_postulacion"):
        respuestas["modo_postulacion"] = "automatizada"

    return construir_postulacion(fecha, empresa, cargo, respuestas)


# --- actualizar postulacion -----------------------------------------------------------


def actualizar_postulacion(
    apps_path: Path,
    events_path: Path,
    query: str,
    nueva_etapa: str,
    nota: str,
    hoy_str: str | None = None,
) -> Application:
    apps = store.load_applications(apps_path)
    events = store.load_events(events_path)

    coincidencias = store.buscar_por_empresa_o_id(apps, query)
    if not coincidencias:
        raise ValidationError(f"no se encontro ninguna postulacion para {query!r}")
    if len(coincidencias) > 1:
        ids = ", ".join(a.id for a in coincidencias)
        raise ValidationError(
            f"la busqueda {query!r} es ambigua ({len(coincidencias)} coincidencias): {ids}"
        )

    app = coincidencias[0]
    fecha = hoy_str or _hoy_str()

    nuevas_apps = store.actualizar_estado_aplicacion(apps, app.id, nueva_etapa, fecha)
    evento = Event(id_postulacion=app.id, fecha=fecha, etapa=nueva_etapa, nota=nota)
    nuevos_events = store.agregar_evento(events, evento)

    store.save_applications(apps_path, nuevas_apps)
    store.save_events(events_path, nuevos_events)

    return next(a for a in nuevas_apps if a.id == app.id)


def flujo_interactivo_update(
    entrada: Callable[[str], str] = input,
) -> tuple[str, str, str]:
    from .model import ETAPAS, TERMINALES

    query = entrada("Empresa o id de la postulacion: ").strip()
    opciones = ", ".join((*ETAPAS, *TERMINALES))
    etapa = entrada(f"Nueva etapa ({opciones}): ").strip()
    nota = entrada("Nota (opcional): ").strip()
    return query, etapa, nota


# --- listar / pendientes / resumen -----------------------------------------------------


def listar(
    apps_path: Path, estado: str | None = None, portal: str | None = None
) -> list[Application]:
    apps = store.load_applications(apps_path)
    if estado:
        apps = [a for a in apps if a.estado_actual == estado]
    if portal:
        apps = [a for a in apps if a.portal.lower() == portal.lower()]
    return apps


def obtener_pendientes(
    apps_path: Path, config: dict, hoy_str: str | None = None
) -> list[dict]:
    apps = store.load_applications(apps_path)
    general = config["general"]
    return stats.pendientes(
        apps,
        umbral_seguimiento_dias=general["umbral_seguimiento_dias"],
        umbral_sin_respuesta_dias=general["umbral_sin_respuesta_dias"],
        hoy_str=hoy_str,
    )


def calcular_resumen(
    apps_path: Path, events_path: Path, config: dict, hoy_str: str | None = None
) -> dict:
    apps = store.load_applications(apps_path)
    events = store.load_events(events_path)
    general = config["general"]
    min_muestra = general["min_muestra"]

    segmentaciones = {
        campo: stats.segmentar_tasa_respuesta(apps, events, campo, min_muestra=min_muestra)
        for campo in CAMPOS_SEGMENTACION
    }
    ritmo = stats.cumplimiento_meta(
        stats.ritmo_semanal(apps, hoy_str=hoy_str), general["meta_semanal"]
    )

    return {
        "total_postulaciones": len(apps),
        "embudo": stats.calcular_embudo(apps, events),
        "segmentaciones": segmentaciones,
        "mediana_dias_respuesta": stats.mediana_dias_hasta_respuesta(apps, events),
        "edades_vivas": stats.edad_postulaciones_vivas(apps, hoy_str=hoy_str),
        "ritmo": ritmo,
        "pendientes": stats.pendientes(
            apps,
            umbral_seguimiento_dias=general["umbral_seguimiento_dias"],
            umbral_sin_respuesta_dias=general["umbral_sin_respuesta_dias"],
            hoy_str=hoy_str,
        ),
    }


# --- wiring de argparse ----------------------------------------------------------------


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="track",
        description=DESCRIPCION,
        epilog=AYUDA_EXTENDIDA,
        # Raw: el epilogo ya viene maquetado a mano y argparse lo reflowearia.
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    sub.add_parser("add", help="Registrar una postulacion nueva (interactivo)")

    p_update = sub.add_parser("update", help="Actualizar la etapa de una postulacion")
    p_update.add_argument("query", nargs="?", help="Empresa o id de la postulacion")
    p_update.add_argument("--etapa", help="Nueva etapa")
    p_update.add_argument("--nota", default="", help="Nota del evento")

    p_list = sub.add_parser("list", help="Listar postulaciones")
    p_list.add_argument("--estado")
    p_list.add_argument("--portal")

    sub.add_parser("pending", help="Postulaciones que requieren seguimiento hoy")
    sub.add_parser("stats", help="Reporte de estadisticas en terminal")

    p_report = sub.add_parser("report", help="Generar reporte HTML")
    p_report.add_argument(
        "--html",
        action="store_true",
        help="Explicito: hoy es el unico formato de reporte, ya se genera por defecto",
    )
    p_report.add_argument("--out", help="Ruta de salida (default: report.html)")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)

    apps_path, events_path = rutas_datos()
    config = cargar_config(ruta_config())
    store.ensure_files(apps_path, events_path)

    if args.comando == "add":
        app = flujo_interactivo_add()
        registrar_postulacion(apps_path, events_path, app)
        print(f"Postulacion registrada: {app.id}")
        return 0

    if args.comando == "update":
        if args.etapa:
            query = args.query
            if not query:
                print("error: falta la empresa o id (usa --etapa junto a un query)", file=sys.stderr)
                return 1
            etapa, nota = args.etapa, args.nota
        else:
            query, etapa, nota = flujo_interactivo_update()
        try:
            actualizada = actualizar_postulacion(
                apps_path, events_path, query, etapa, nota
            )
        except ValidationError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        print(f"{actualizada.id} -> {actualizada.estado_actual}")
        return 0

    if args.comando == "list":
        apps = listar(apps_path, estado=args.estado, portal=args.portal)
        print(report.render_lista(apps))
        return 0

    if args.comando == "pending":
        pend = obtener_pendientes(apps_path, config)
        print(report.render_pendientes(pend))
        return 0

    if args.comando == "stats":
        resumen = calcular_resumen(apps_path, events_path, config)
        print(report.render_resumen_terminal(resumen))
        return 0

    if args.comando == "report":
        resumen = calcular_resumen(apps_path, events_path, config)
        salida = Path(args.out) if args.out else REPO_ROOT / "report.html"
        salida.write_text(report.render_resumen_html(resumen), encoding="utf-8")
        print(f"Reporte HTML generado en {salida}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
