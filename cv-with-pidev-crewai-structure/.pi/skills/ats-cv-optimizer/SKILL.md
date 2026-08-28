---
name: ats-cv-optimizer
description: >-
  Reescribe un CV en Markdown de este proyecto para maximizar el paso de filtros ATS (Applicant Tracking System) — formato, estructura y keywords — sin inventar información nueva. Úsalo cuando el usuario diga "optimiza mi CV para ATS", "pásalo por el filtro ATS", "que mi CV pase los bots de reclutamiento", "hazlo compatible con ATS", "revisa mi CV contra esta vacante para ATS", "por qué mi CV no pasa el ATS". Skill de un solo propósito: NO busca empleos, NO hace scraping, NO genera PDF.
allowed-tools: read, write, edit
required-files: >-
  cv.md (o el archivo Markdown de CV que el usuario indique). Opcional pero recomendado: descripción de la vacante objetivo (texto o URL ya extraído).
output-files: <archivo-origen>_ats.md (o el nombre que indique el usuario) + reporte de verificación en la respuesta al usuario
---

# 🧩 ATS CV Optimizer

Skill de propósito único: toma un CV en Markdown de este proyecto (típicamente `cv.md`, o un CV ya personalizado como los de `companies/`) y lo reescribe para maximizar la probabilidad de superar el parsing y el scoring de un ATS (Workday, Taleo, iCIMS, Greenhouse, Lever, SmartRecruiters, BrassRing, SAP SuccessFactors), sin inventar ni tergiversar experiencia.

No reemplaza el pipeline completo de `AGENTS.md` — es una herramienta enfocada que puede usarse sola o como refinamiento adicional dentro de la Tarea 3 (`resume_skills_customizer`) de ese pipeline. No genera el PDF final: eso lo hace exclusivamente el agente `pdf_exporter` (Tarea 8 de `AGENTS.md`) vía `/usr/local/bin/m2pdf`.

Ver `ATS-CHECKLIST.md` en esta misma carpeta para el detalle completo de reglas y fuentes de la investigación en la que se basa esta skill.

## Cuándo usar esta skill

- El usuario quiere optimizar un CV existente para pasar filtros automáticos, con o sin una vacante específica de referencia.
- El usuario pregunta por qué un CV fue rechazado automáticamente o no recibe respuestas.
- Como paso de refinamiento antes de la Tarea 5 (`audit_cv_anti_ai`), la Tarea 6 (`markdown_format_polisher`) y la Tarea 8 (`pdf_exporter`) del pipeline principal.

## Reglas duras (no negociables)

1. **Nunca inventar** empresas, cargos, fechas, tecnologías, certificaciones ni logros que no estén ya en el CV de origen. Solo reorganizar, reformular y cuantificar lo existente.
2. **Respetar las restricciones ya definidas en `AGENTS.md`**: prohibido usar "CTO" o "Co-founder"; usar "Tech Lead", "Lead Software Engineer", "Senior Full-Stack Engineer" o equivalentes de liderazgo técnico.
3. **Salida 100% Markdown lineal**, sin tablas usadas como layout, sin columnas, sin text boxes, sin artefactos de conversión (`.unnumbered`, `:::center`, clases LaTeX). Esto es crítico porque el PDF final se genera con `m2pdf` (pandoc/xelatex): un Markdown de origen limpio es la única garantía de que el PDF resultante tenga texto seleccionable y parseable.
4. **Cero iconos/emoji en la información de contacto** (nombre, título, ubicación, email, teléfono, LinkedIn) — deben ir como texto plano en el cuerpo principal, nunca en un formato que dependa de imágenes o símbolos gráficos.
5. **Cero buzzwords vacíos**: "passionate", "results-driven", "team player", "responsible for", "hard worker", "innovative", "good communicator". Sustituir siempre por un logro concreto con verbo de acción + cifra/resultado.

## Proceso

1. **Leer** el CV de origen (`cv.md` u otro indicado) y, si el usuario la proporciona, la descripción de la vacante objetivo.
2. **Extraer keywords** de la vacante (si existe): herramientas, frameworks, metodologías, certificaciones, nivel de seniority, y el título exacto del puesto. Meta: 15–25 keywords cubriendo 70–80% de las de la vacante.
3. **Normalizar la estructura** a secciones canónicas (ver tabla en `ATS-CHECKLIST.md`), en este orden: Contacto → Resumen Profesional → Habilidades → Experiencia Laboral → Educación → Certificaciones/Idiomas.
4. **Ajustar el headline** (línea bajo el nombre) para reflejar el título exacto de la vacante objetivo cuando exista una, siempre respetando la regla 2 de arriba y sin fabricar el cargo.
5. **Reescribir bullets de experiencia**: 3–5 por rol (hasta 6 en el más reciente), 15–25 palabras cada uno, con cifra o resultado medible cuando el CV original lo permita. Insertar las keywords con contexto real, no como lista pegada.
6. **Expandir siglas** la primera vez que aparecen: "término completo (SIGLA)".
7. **Eliminar** cualquier tabla, columna, icono decorativo, bullet no estándar (usar solo `-`), o residuo de formato que rompa el parsing.
8. **Verificar fechas**: formato consistente `Month YYYY – Present` (o equivalente en español) en todo el documento, orden cronológico inverso.
9. **Autoverificar** el resultado contra el checklist de 20 ítems de `ATS-CHECKLIST.md` antes de entregar.
10. **Guardar** como archivo nuevo (no sobrescribir el CV original salvo que el usuario lo pida explícitamente), por defecto `<nombre-original>_ats.md`.
11. **Reportar al usuario**: qué cambió, qué keywords de la vacante quedaron cubiertas y cuáles no, y el resultado del checklist de verificación.

## Reglas de comportamiento

- Si no hay job description disponible, optimizar solo por formato/estructura/claridad general (reglas 1, 3–9 de esta skill) y avisar al usuario que sin vacante de referencia no se puede maximizar el keyword-matching.
- Nunca generar el PDF directamente ni sugerir otra herramienta de conversión distinta a `/usr/local/bin/m2pdf` (ver `AGENTS.md`).
- Si el CV de origen ya tiene keyword stuffing evidente (>30 keywords repetidas sin contexto), reducir densidad en vez de aumentarla.
- Señalar explícitamente al usuario cualquier requisito de la vacante que el candidato genuinamente no cumple — no forzar un match falso.

## Ejemplos de uso

```
Optimiza cv.md para ATS usando esta descripción de vacante: <pegar job description>
```

```
Revisa companies/cv_gonzalo_bc_tecnologia.md, ¿por qué crees que no pasó el ATS? Corrígelo.
```

```
Pásame cv.md por el filtro ATS sin ninguna vacante en particular, solo mejora formato y estructura.
```

## Archivos relacionados

| Archivo | Descripción |
|---------|-------------|
| `ATS-CHECKLIST.md` | Reglas detalladas de formato, contenido, headers canónicos, checklist de 20 ítems y fuentes de la investigación. |
| `../../../AGENTS.md` | Pipeline general del proyecto (Tareas 1–8); esta skill se integra como refinamiento de la Tarea 3 y precede a las Tareas 5, 6 y 8. |
