"""Renderizado de reportes: tabla de texto para terminal y página HTML."""

from __future__ import annotations

import html as _html
from typing import Sequence

from .model import ETAPAS
from .stats import ResultadoEmbudo, SegmentoResultado


def formatear_tabla(headers: Sequence[str], filas: Sequence[Sequence[object]]) -> str:
    filas_str = [[str(v) for v in fila] for fila in filas]
    anchos = []
    for i, h in enumerate(headers):
        ancho = len(str(h))
        for fila in filas_str:
            ancho = max(ancho, len(fila[i]))
        anchos.append(ancho)

    def fmt(vals: Sequence[object]) -> str:
        return "  ".join(str(v).ljust(anchos[i]) for i, v in enumerate(vals))

    lineas = [fmt(headers), "  ".join("-" * a for a in anchos)]
    lineas.extend(fmt(fila) for fila in filas_str)
    return "\n".join(lineas)


def render_embudo(resultado: ResultadoEmbudo) -> str:
    filas = [[etapa, resultado.conteos[etapa]] for etapa in ETAPAS]
    tabla = formatear_tabla(["Etapa", "Llegaron a esta etapa"], filas)

    conv_lineas = []
    for clave, tasa in resultado.conversiones.items():
        origen, destino = clave.split("->")
        if tasa is None:
            conv_lineas.append(f"  {origen} -> {destino}: sin datos")
        else:
            conv_lineas.append(f"  {origen} -> {destino}: {tasa:.0%}")

    term_lineas = [f"  {etapa}: {n}" for etapa, n in resultado.terminales.items()]

    return (
        tabla
        + "\n\nConversion entre etapas:\n"
        + "\n".join(conv_lineas)
        + "\n\nEstados terminales:\n"
        + "\n".join(term_lineas)
    )


def render_segmentacion(campo: str, resultado: dict[str, SegmentoResultado]) -> str:
    if not resultado:
        return "(sin datos)"
    filas = []
    for valor, seg in sorted(resultado.items(), key=lambda kv: -kv[1].n):
        if seg.tasa_respuesta is None:
            tasa_txt = f"muestra insuficiente (n={seg.n})"
        else:
            tasa_txt = f"{seg.tasa_respuesta:.0%}"
        filas.append([valor, seg.n, tasa_txt])
    return formatear_tabla([campo, "n", "tasa de respuesta"], filas)


def render_tiempos(mediana: float | None, edades: list[tuple[str, int]]) -> str:
    mediana_txt = f"{mediana:.0f} dias" if mediana is not None else "sin datos"
    top_edades = edades[:10]
    if top_edades:
        tabla = formatear_tabla(
            ["id", "dias sin novedades"], [[id_, dias] for id_, dias in top_edades]
        )
    else:
        tabla = "(sin postulaciones vivas)"
    return (
        f"Mediana de dias hasta la primera respuesta: {mediana_txt}\n\n"
        f"Postulaciones vivas mas antiguas sin novedades:\n{tabla}"
    )


def render_ritmo(ritmo: list[dict[str, object]]) -> str:
    filas = [
        [r["semana"], r["postulaciones"], "si" if r["cumplio_meta"] else "no"]
        for r in ritmo
    ]
    return formatear_tabla(["semana (lunes)", "postulaciones", "cumplio meta"], filas)


def render_pendientes(pendientes: list[dict[str, object]]) -> str:
    if not pendientes:
        return "(nada pendiente - al dia)"
    filas = [[p["id"], p["motivo"], p["dias"]] for p in pendientes]
    return formatear_tabla(["id", "motivo", "dias sin novedades"], filas)


def render_lista(apps: Sequence) -> str:
    if not apps:
        return "(sin postulaciones)"
    filas = [
        [a.id, a.empresa, a.cargo, a.portal, a.estado_actual, a.fecha_postulacion]
        for a in apps
    ]
    return formatear_tabla(
        ["id", "empresa", "cargo", "portal", "estado", "fecha"], filas
    )


def render_resumen_terminal(resumen: dict) -> str:
    partes = [
        f"Total de postulaciones: {resumen['total_postulaciones']}",
        "",
        "== EMBUDO ==",
        render_embudo(resumen["embudo"]),
        "",
        "== QUE FUNCIONA MEJOR ==",
    ]
    for campo, seg in resumen["segmentaciones"].items():
        partes.append(f"\npor {campo}:")
        partes.append(render_segmentacion(campo, seg))
    partes += [
        "",
        "== TIEMPOS ==",
        render_tiempos(resumen["mediana_dias_respuesta"], resumen["edades_vivas"]),
        "",
        "== RITMO SEMANAL ==",
        render_ritmo(resumen["ritmo"]),
        "",
        "== PENDIENTES ==",
        render_pendientes(resumen["pendientes"]),
    ]
    return "\n".join(partes)


def render_resumen_html(resumen: dict) -> str:
    """Página HTML autocontenida (sin dependencias externas)."""
    cuerpo = render_resumen_terminal(resumen)
    escapado = _html.escape(cuerpo)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Reporte de postulaciones</title>
<style>
  :root {{ color-scheme: dark light; }}
  body {{
    font-family: -apple-system, system-ui, sans-serif;
    background: #0b0b0f; color: #e8e8ec;
    margin: 0; padding: 2rem;
  }}
  @media (prefers-color-scheme: light) {{
    body {{ background: #f5f5f7; color: #16161a; }}
    pre {{ background: #ffffff !important; border-color: #dcdce2 !important; }}
  }}
  pre {{
    white-space: pre-wrap; font-family: ui-monospace, monospace;
    font-size: 0.95rem; line-height: 1.5;
    background: #15151b; padding: 1.5rem; border-radius: 12px;
    border: 1px solid #26262e;
  }}
  h1 {{ font-size: 1.4rem; margin-bottom: 1rem; }}
</style>
</head>
<body>
<h1>Reporte de postulaciones</h1>
<pre>{escapado}</pre>
</body>
</html>
"""
