"""Persistencia en CSV para Application y Event.

Todas las operaciones de mutación de listas devuelven listas NUEVAS
(inmutabilidad) — el llamador decide cuándo persistir con save_*.
Escribimos el archivo completo cada vez: son cientos de filas como mucho,
y así se evita la complejidad de un formato de log append-only.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Sequence

from .model import (
    APPLICATION_FIELDS,
    EVENT_FIELDS,
    Application,
    Event,
    ValidationError,
)


def ensure_files(apps_path: Path, events_path: Path) -> None:
    """Crea los CSV con headers si todavía no existen."""
    if not apps_path.exists():
        save_applications(apps_path, [])
    if not events_path.exists():
        save_events(events_path, [])


def load_applications(path: Path) -> list[Application]:
    if not Path(path).exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [Application.from_row(row) for row in reader]


def save_applications(path: Path, apps: Sequence[Application]) -> None:
    # Orden estable por fecha_postulacion, luego id: hace que `git diff`
    # sobre el CSV sea legible en vez de un revoltijo por orden de inserción.
    ordenadas = sorted(apps, key=lambda a: (a.fecha_postulacion, a.id))
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=APPLICATION_FIELDS)
        writer.writeheader()
        for app in ordenadas:
            writer.writerow(app.to_row())


def load_events(path: Path) -> list[Event]:
    if not Path(path).exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [Event.from_row(row) for row in reader]


def save_events(path: Path, events: Sequence[Event]) -> None:
    ordenados = sorted(events, key=lambda e: (e.id_postulacion, e.fecha))
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=EVENT_FIELDS)
        writer.writeheader()
        for ev in ordenados:
            writer.writerow(ev.to_row())


def agregar_postulacion(
    apps: Sequence[Application], nueva: Application
) -> list[Application]:
    if any(a.id == nueva.id for a in apps):
        raise ValidationError(f"ya existe una postulacion con id {nueva.id!r}")
    return [*apps, nueva]


def agregar_evento(events: Sequence[Event], nuevo: Event) -> list[Event]:
    return [*events, nuevo]


def actualizar_estado_aplicacion(
    apps: Sequence[Application],
    id_postulacion: str,
    nuevo_estado: str,
    fecha: str,
) -> list[Application]:
    if not any(a.id == id_postulacion for a in apps):
        raise ValidationError(f"no existe postulacion con id {id_postulacion!r}")

    def _actualizar(app: Application) -> Application:
        if app.id != id_postulacion:
            return app
        return app.con_cambios(
            estado_actual=nuevo_estado, fecha_ultimo_evento=fecha
        )

    return [_actualizar(a) for a in apps]


def buscar_por_empresa_o_id(
    apps: Sequence[Application], query: str
) -> list[Application]:
    q = query.strip().lower()
    return [
        a for a in apps if q in a.empresa.lower() or q == a.id.lower()
    ]
