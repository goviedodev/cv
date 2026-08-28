# 🧩 ATS CV Optimizer

Skill de un solo propósito para este proyecto: reescribir un CV en Markdown (`cv.md` u otro) para maximizar el paso de filtros ATS, sin inventar información.

## Qué hace

1. Lee el CV objetivo (y opcionalmente una job description).
2. Extrae keywords de la vacante y calcula cobertura objetivo (70–80%).
3. Normaliza estructura a secciones canónicas de una sola columna.
4. Reescribe bullets con verbos de acción, cifras y contexto real.
5. Elimina tablas, iconos, buzzwords vacíos y artefactos de conversión.
6. Verifica el resultado contra un checklist de 20 ítems.
7. Entrega un archivo nuevo (`<origen>_ats.md`) + reporte de cambios y keywords cubiertas/faltantes.

## Qué NO hace

- No busca empleos ni hace scraping de portales (eso es `job-hunter-linkedin`).
- No genera el PDF final — el único conversor autorizado del proyecto es `/usr/local/bin/m2pdf` (ver Tarea 8 de `AGENTS.md`).
- No inventa ni tergiversa experiencia, cargos, fechas o tecnologías.

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `SKILL.md` | Definición de la skill: frontmatter, proceso paso a paso, reglas de comportamiento. |
| `ATS-CHECKLIST.md` | Reglas detalladas de formato/contenido, headers canónicos, checklist de 20 ítems y fuentes de investigación (2025–2026). |

## Uso

```
Optimiza cv.md para ATS usando esta descripción de vacante: <pegar job description>
```

```
Revisa companies/cv_gonzalo_bc_tecnologia.md, ¿por qué crees que no pasó el ATS? Corrígelo.
```

## Relación con el pipeline principal

Se integra en el flujo de `AGENTS.md` como refinamiento de la **Tarea 3** (`resume_skills_customizer`), antes de la **Tarea 5** (`audit_cv_anti_ai`, skill `anti-ai-cv-auditor`), la **Tarea 6** (`markdown_format_polisher`) y la **Tarea 8** (`pdf_exporter` vía `m2pdf`).
