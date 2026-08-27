# proceso

Tracker de postulaciones a empleo. Registra cada postulación y su historial
de etapas en dos CSV versionados en git, y calcula embudo, segmentación,
tiempos y ritmo a partir de ese historial.

Reemplaza a `cv-with-pidev-crewai-structure/cv_job_links.md`, que quedó
congelado como archivo histórico: ese archivo mezclaba fechas, y el campo
`Estado` se volvió texto libre en vez de valores agregables. Este sistema
separa **estado actual** (`data/applications.csv`) de **historial de
eventos** (`data/events.csv`) para que sí se puedan calcular tiempos y un
embudo real. Ver `data/model.py` para el porqué del diseño.

Cero dependencias externas: corre con el `python3` del sistema.

## Uso

```bash
./track add                        # registrar una postulacion (interactivo, ~20s)
./track update "Equifax"           # actualizar etapa (interactivo)
./track update "Equifax" --etapa respuesta --nota "llamaron por telefono"
./track list --portal LinkedIn     # listar, filtrable por --estado / --portal
./track pending                    # que requiere seguimiento hoy
./track stats                      # embudo, segmentacion, tiempos y ritmo en terminal
./track report --html              # lo mismo, como pagina HTML autocontenida
```

## Modelo de datos

- **`data/applications.csv`**: una fila por postulación, con su estado actual.
- **`data/events.csv`**: una fila por cada cambio de etapa, con fecha.

Etapas del embudo, en orden:
`postulado → respuesta → screening → entrevista_tecnica → entrevista_final → oferta → aceptada`

Terminales (no forman parte del embudo lineal): `rechazado`, `descartado_por_mi`.

`sin_respuesta` **no se registra a mano**: se deriva cuando una postulación
sigue en `postulado` más allá de `umbral_sin_respuesta_dias` (config.toml).
Así no hay que "cerrar" manualmente postulaciones muertas.

## Configuración

`config.toml`: meta semanal, umbrales de días para seguimiento/sin-respuesta,
`min_muestra` (ningún segmento con menos postulaciones que esto reporta un
porcentaje — evita leer ruido como señal) y los portales que aparecen como
sugerencia en `track add`.

## Desarrollo

```bash
python3 -m pytest tests/ --cov=src --cov-report=term-missing
```

Estructura: `src/model.py` (dataclasses inmutables + validación), `src/store.py`
(persistencia CSV), `src/stats.py` (embudo/segmentación/tiempos/ritmo),
`src/report.py` (render terminal + HTML), `src/cli.py` (comandos).
