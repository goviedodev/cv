"""Cálculo de insights: embudo, segmentación, tiempos, ritmo y pendientes.

Todo se calcula a partir de events.csv (historial), no del estado actual —
es la razón por la que separamos Application de Event en model.py.
"""

from __future__ import annotations

import statistics
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Sequence

from .model import ETAPAS, SIN_RESPUESTA, TERMINALES, Application, Event
from .model import hoy as _hoy_str


def _parse(fecha: str) -> date:
    return datetime.strptime(fecha, "%Y-%m-%d").date()


def eventos_por_aplicacion(events: Sequence[Event]) -> dict[str, list[Event]]:
    agrupados: dict[str, list[Event]] = defaultdict(list)
    for ev in events:
        agrupados[ev.id_postulacion].append(ev)
    return {id_: sorted(evs, key=lambda e: e.fecha) for id_, evs in agrupados.items()}


def maxima_etapa_alcanzada(events_app: Sequence[Event]) -> str | None:
    """Etapa de mayor índice en ETAPAS entre los eventos de una postulación.

    Ignora estados terminales (rechazado/descartado_por_mi): se reportan
    aparte porque no forman parte de la escalera lineal del embudo.
    """
    indices = [ETAPAS.index(ev.etapa) for ev in events_app if ev.etapa in ETAPAS]
    if not indices:
        return None
    return ETAPAS[max(indices)]


# --- embudo -------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class ResultadoEmbudo:
    conteos: dict[str, int]
    conversiones: dict[str, float | None]
    terminales: dict[str, int]


def calcular_embudo(
    applications: Sequence[Application], events: Sequence[Event]
) -> ResultadoEmbudo:
    por_app = eventos_por_aplicacion(events)
    max_por_app = {
        app.id: maxima_etapa_alcanzada(por_app.get(app.id, [])) for app in applications
    }

    conteos = {etapa: 0 for etapa in ETAPAS}
    for etapa_max in max_por_app.values():
        if etapa_max is None:
            continue
        idx_max = ETAPAS.index(etapa_max)
        # Alcanzar una etapa implica haber pasado por todas las anteriores,
        # aunque no haya un evento explícito registrado para cada una.
        for i in range(idx_max + 1):
            conteos[ETAPAS[i]] += 1

    conversiones: dict[str, float | None] = {}
    for i in range(len(ETAPAS) - 1):
        origen, destino = ETAPAS[i], ETAPAS[i + 1]
        base = conteos[origen]
        conversiones[f"{origen}->{destino}"] = (
            conteos[destino] / base if base else None
        )

    terminales = {t: 0 for t in TERMINALES}
    for app in applications:
        if app.estado_actual in TERMINALES:
            terminales[app.estado_actual] += 1

    return ResultadoEmbudo(
        conteos=conteos, conversiones=conversiones, terminales=terminales
    )


# --- segmentación ---------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class SegmentoResultado:
    n: int
    tasa_respuesta: float | None  # None si n < min_muestra: "muestra insuficiente"


def _reached_respuesta(events_app: Sequence[Event]) -> bool:
    etapa_max = maxima_etapa_alcanzada(events_app)
    if etapa_max is None:
        return False
    return ETAPAS.index(etapa_max) >= ETAPAS.index("respuesta")


def _valores_segmento(app: Application, campo: str) -> tuple[str, ...]:
    if campo == "stack":
        tecnologias = app.stack_tecnologias()
        return tecnologias or ("(sin dato)",)
    valor = (getattr(app, campo) or "").strip()
    return (valor,) if valor else ("(sin dato)",)


def segmentar_tasa_respuesta(
    applications: Sequence[Application],
    events: Sequence[Event],
    campo: str,
    min_muestra: int = 5,
) -> dict[str, SegmentoResultado]:
    """Tasa de respuesta agrupada por `campo`, con guardrail de muestra mínima.

    Un segmento con menos de `min_muestra` postulaciones nunca reporta un
    porcentaje: sin esto, "100% de respuesta" con n=2 se lee como señal
    cuando es ruido.
    """
    por_app = eventos_por_aplicacion(events)
    respondio = {
        app.id: _reached_respuesta(por_app.get(app.id, [])) for app in applications
    }

    grupos: dict[str, list[bool]] = defaultdict(list)
    for app in applications:
        for valor in _valores_segmento(app, campo):
            grupos[valor].append(respondio[app.id])

    resultado: dict[str, SegmentoResultado] = {}
    for valor, respuestas in grupos.items():
        n = len(respuestas)
        tasa = sum(respuestas) / n if n >= min_muestra else None
        resultado[valor] = SegmentoResultado(n=n, tasa_respuesta=tasa)
    return resultado


# --- tiempos --------------------------------------------------------------------


def dias_hasta_primera_respuesta(
    app: Application, events_app: Sequence[Event]
) -> int | None:
    respuestas = [ev for ev in events_app if ev.etapa == "respuesta"]
    if not respuestas:
        return None
    primera = min(respuestas, key=lambda e: e.fecha)
    return (_parse(primera.fecha) - _parse(app.fecha_postulacion)).days


def mediana_dias_hasta_respuesta(
    applications: Sequence[Application], events: Sequence[Event]
) -> float | None:
    # Mediana, no promedio: una postulación que tardó 100 días en responder
    # no debe distorsionar el número que ves para las demás.
    por_app = eventos_por_aplicacion(events)
    dias = [
        d
        for app in applications
        if (d := dias_hasta_primera_respuesta(app, por_app.get(app.id, []))) is not None
    ]
    if not dias:
        return None
    return statistics.median(dias)


def edad_postulaciones_vivas(
    applications: Sequence[Application], hoy_str: str | None = None
) -> list[tuple[str, int]]:
    hoy_d = _parse(hoy_str) if hoy_str else _parse(_hoy_str())
    vivas = [
        (
            app.id,
            (hoy_d - _parse(app.fecha_ultimo_evento or app.fecha_postulacion)).days,
        )
        for app in applications
        if app.estado_actual not in TERMINALES
    ]
    return sorted(vivas, key=lambda t: -t[1])


# --- pendientes / follow-up -------------------------------------------------------


def pendientes(
    applications: Sequence[Application],
    umbral_seguimiento_dias: int = 7,
    umbral_sin_respuesta_dias: int = 21,
    hoy_str: str | None = None,
) -> list[dict[str, object]]:
    """Postulaciones vivas que requieren atención.

    `sin_respuesta` se deriva del tiempo transcurrido, nunca se marca a
    mano: así no hay que "cerrar" manualmente decenas de postulaciones
    muertas, que es donde el sistema anterior se abandonó.
    """
    hoy_d = _parse(hoy_str) if hoy_str else _parse(_hoy_str())
    resultado = []
    for app in applications:
        if app.estado_actual in TERMINALES:
            continue
        referencia = _parse(app.fecha_ultimo_evento or app.fecha_postulacion)
        dias = (hoy_d - referencia).days
        if app.estado_actual == "postulado" and dias >= umbral_sin_respuesta_dias:
            resultado.append({"id": app.id, "motivo": SIN_RESPUESTA, "dias": dias})
        elif dias >= umbral_seguimiento_dias:
            resultado.append({"id": app.id, "motivo": "seguimiento", "dias": dias})
    return sorted(resultado, key=lambda r: -r["dias"])


# --- ritmo semanal ------------------------------------------------------------------


def _inicio_semana(d: date) -> date:
    return d - timedelta(days=d.weekday())  # lunes de esa semana


def ritmo_semanal(
    applications: Sequence[Application],
    semanas: int = 8,
    hoy_str: str | None = None,
) -> list[dict[str, object]]:
    hoy_d = _parse(hoy_str) if hoy_str else _parse(_hoy_str())
    inicio_actual = _inicio_semana(hoy_d)
    semanas_inicio = [
        inicio_actual - timedelta(weeks=i) for i in range(semanas - 1, -1, -1)
    ]
    conteo = {inicio: 0 for inicio in semanas_inicio}
    for app in applications:
        inicio = _inicio_semana(_parse(app.fecha_postulacion))
        if inicio in conteo:
            conteo[inicio] += 1
    return [
        {"semana": inicio.isoformat(), "postulaciones": conteo[inicio]}
        for inicio in semanas_inicio
    ]


def cumplimiento_meta(
    ritmo: list[dict[str, object]], meta_semanal: int
) -> list[dict[str, object]]:
    return [
        {**semana, "cumplio_meta": semana["postulaciones"] >= meta_semanal}
        for semana in ritmo
    ]
