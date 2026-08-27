"""Modelo de datos del tracker de postulaciones.

Dos entidades inmutables: Application (estado actual) y Event (historial).
Separarlas es lo que permite calcular tiempos y embudo real en vez de solo
el estado final, que era el defecto de fondo de cv_job_links.md.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from datetime import date, datetime

# Etapas del embudo, en orden. El orden importa: se usa para calcular
# "máxima etapa alcanzada" y tasas de conversión entre etapas consecutivas.
ETAPAS: tuple[str, ...] = (
    "postulado",
    "respuesta",
    "screening",
    "entrevista_tecnica",
    "entrevista_final",
    "oferta",
    "aceptada",
)

# Estados terminales que no son parte del avance del embudo lineal.
TERMINALES: tuple[str, ...] = (
    "rechazado",
    "descartado_por_mi",
)

# Estado derivado (nunca se escribe a mano, ver stats.py / cli.py).
SIN_RESPUESTA = "sin_respuesta"

ETAPAS_VALIDAS: frozenset[str] = frozenset(ETAPAS) | frozenset(TERMINALES)

_FECHA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

APPLICATION_FIELDS: tuple[str, ...] = (
    "id",
    "fecha_postulacion",
    "empresa",
    "cargo",
    "seniority",
    "portal",
    "url",
    "modalidad",
    "pais",
    "idioma_cv",
    "version_cv",
    "stack",
    "salario_publicado",
    "referido",
    "estado_actual",
    "fecha_ultimo_evento",
    "notas",
)

EVENT_FIELDS: tuple[str, ...] = (
    "id_postulacion",
    "fecha",
    "etapa",
    "nota",
)


class ValidationError(ValueError):
    """Error de validación de datos de dominio (fecha, etapa, etc.)."""


def validar_fecha(valor: str) -> str:
    """Valida que una fecha venga en formato YYYY-MM-DD y sea una fecha real.

    Esto existe porque cv_job_links.md mezcla '2026-08-19' con
    '2026-08-19 16:47' — el formato inconsistente no vuelve a pasar aquí.
    """
    if not isinstance(valor, str) or not _FECHA_RE.match(valor):
        raise ValidationError(
            f"fecha invalida: {valor!r} (se esperaba YYYY-MM-DD)"
        )
    try:
        datetime.strptime(valor, "%Y-%m-%d")
    except ValueError as exc:
        raise ValidationError(f"fecha invalida: {valor!r}") from exc
    return valor


def validar_etapa(valor: str) -> str:
    if valor not in ETAPAS_VALIDAS:
        validas = ", ".join(ETAPAS_VALIDAS)
        raise ValidationError(f"etapa invalida: {valor!r} (validas: {validas})")
    return valor


def slugify(texto: str) -> str:
    """Convierte texto libre en un slug ascii en minúsculas con guiones."""
    texto = texto.strip().lower()
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n", "ü": "u",
    }
    for origen, destino in reemplazos.items():
        texto = texto.replace(origen, destino)
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-") or "sin-nombre"


def generar_id(fecha_postulacion: str, empresa: str, cargo: str) -> str:
    """Genera el slug id: 2026-08-26-equifax-fullstack-senior."""
    validar_fecha(fecha_postulacion)
    return f"{fecha_postulacion}-{slugify(empresa)}-{slugify(cargo)}"


@dataclass(frozen=True, slots=True)
class Application:
    id: str
    fecha_postulacion: str
    empresa: str
    cargo: str
    seniority: str = ""
    portal: str = ""
    url: str = ""
    modalidad: str = ""
    pais: str = ""
    idioma_cv: str = ""
    version_cv: str = ""
    stack: str = ""  # valores separados por ';'
    salario_publicado: str = ""
    referido: str = "no"
    estado_actual: str = "postulado"
    fecha_ultimo_evento: str = ""
    notas: str = ""

    def __post_init__(self) -> None:
        validar_fecha(self.fecha_postulacion)
        validar_etapa(self.estado_actual)
        if self.fecha_ultimo_evento:
            validar_fecha(self.fecha_ultimo_evento)
        if self.referido not in ("si", "no"):
            raise ValidationError(
                f"referido invalido: {self.referido!r} (si|no)"
            )
        if not self.empresa.strip():
            raise ValidationError("empresa no puede estar vacia")
        if not self.cargo.strip():
            raise ValidationError("cargo no puede estar vacio")

    def stack_tecnologias(self) -> tuple[str, ...]:
        return tuple(t.strip() for t in self.stack.split(";") if t.strip())

    def con_cambios(self, **cambios: str) -> "Application":
        """Devuelve una copia con los campos indicados actualizados.

        Nunca se muta una Application existente (regla de inmutabilidad).
        """
        return replace(self, **cambios)

    def to_row(self) -> dict[str, str]:
        return {campo: getattr(self, campo) for campo in APPLICATION_FIELDS}

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "Application":
        datos = {campo: row.get(campo, "") or "" for campo in APPLICATION_FIELDS}
        return cls(**datos)


@dataclass(frozen=True, slots=True)
class Event:
    id_postulacion: str
    fecha: str
    etapa: str
    nota: str = ""

    def __post_init__(self) -> None:
        validar_fecha(self.fecha)
        validar_etapa(self.etapa)
        if not self.id_postulacion.strip():
            raise ValidationError("id_postulacion no puede estar vacio")

    def to_row(self) -> dict[str, str]:
        return {campo: getattr(self, campo) for campo in EVENT_FIELDS}

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "Event":
        datos = {campo: row.get(campo, "") or "" for campo in EVENT_FIELDS}
        return cls(**datos)


def hoy() -> str:
    return date.today().strftime("%Y-%m-%d")
