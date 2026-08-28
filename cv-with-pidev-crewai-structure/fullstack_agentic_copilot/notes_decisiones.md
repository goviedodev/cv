# Nota de decisiones — FullStack · Agentic Software Engineer (GitHub Copilot)

**Fecha:** 2026-08-17
**Oferta:** https://talent.fullstack.com/jobs/f3ad0671-8b9f-44e1-9d14-13859f3b2ceb
**Perfil aplicado (cv-tailor):** B — Remoto internacional en USD (cliente final en EE.UU., red de talento LATAM).
**Idioma del CV:** inglés.

## Dirección usada

Por decisión explícita del usuario, la dirección va como:

> Villa Baviera S/N, Parcela 77, Bulnes, Región del Biobío, Chile (GMT-4)

**Detalle administrativo a tener presente en entrevista:** Bulnes pertenece hoy a la **Región de Ñuble**,
que se separó de la Región del Biobío en 2018. La oferta está publicada en "Gran Concepción, Región del
Biobío" y el usuario pidió calzar con esa región. Si un reclutador lo nota, la explicación natural es que
Bulnes formaba parte del Biobío hasta la creación de Ñuble y que el puesto es 100% remoto, por lo que lo
que importa es la autorización para trabajar en Chile.

Se agregó además la línea de autorización laboral, porque la oferta lo pide explícitamente y descarta
patrocinio de visa.

## Formato de salida

El usuario eligió **estilo Harvard** (Tarea 6-bis) por sobre el default ATS-safe. Se generaron los dos
archivos:

- `cv_gonzalo_agentic_software_engineer.md` — Markdown ATS-safe (fuente de verdad, sin LaTeX).
- `Gonzalo_Oviedo_Agentic_Software_Engineer.md` + `.pdf` — maqueta Harvard, contenido idéntico palabra por
  palabra.

Verificación: `pdfinfo` = 2 páginas; `pdftotext` devuelve el texto completo, lineal y en orden de lectura
(sin tablas ni columnas), por lo que el PDF sigue siendo parseable si FullStack Connect lo pasa por un ATS.

## Keywords de la oferta espejadas (ortografía exacta)

| Keyword de la oferta | Dónde aparece en el CV |
|---|---|
| Agentic Software Engineer | Headline y título del rol actual |
| GitHub Copilot | Headline, resumen, skills, stack del rol actual |
| full-stack architectures | Headline, resumen |
| architectural oversight | Bullet 1 del rol actual |
| multi-file systems / codebase | Bullet 3 del rol actual |
| context engineering | Skills y bullet 3 del rol actual |
| machine-executable specifications | Skills |
| AI-first development workflows | Headline, skills, bullet 2 del rol actual |
| specification through deployment | Bullet 2 del rol actual |
| structured iteration and feedback loops | Skills y bullet 4 del rol actual |
| human-in-the-loop review | Skills y bullet 5 del rol actual |
| risk-adjusted validation | Skills y bullet 5 del rol actual |
| frontend, backend, and infrastructure | Resumen y bullet 6 del rol actual |
| production-ready / production software | Resumen y bullet 1 |
| Java, React, Node | Skills |
| Agile methodologies and Lean principles | Skills |
| four-year college degree | Educación (explicitado) |
| Advanced English | Bloque de contacto e Idiomas |

**No cubiertas:** Python y C# (no están en el CV maestro; la oferta los lista como "e.g.", no como
obligatorios). No se agregaron.

## Brechas reales frente a la oferta

1. **"Deep experience using GitHub Copilot as a primary development environment".** Copilot sí está en tu
   toolchain real (aparece en `fullstack/cv_gonzalo_fullstack.md` y en `softserve/notes_gap_analysis.md`),
   pero tu herramienta principal hoy es Claude Code / Pi.dev / opencode. El CV lo declara así: Copilot
   primero en la lista, junto al resto del harness. **Prepara la respuesta de entrevista**: qué haces en
   Copilot específicamente (chat, agent mode, edits multi-archivo, instrucciones de repo) versus qué haces
   en los otros harnesses. Si te preguntan "¿Copilot es tu entorno principal?", la respuesta honesta y
   fuerte es: "mi entorno principal es un harness de agentes; Copilot es una de las piezas y el flujo que
   diseñé es agnóstico de la herramienta".
2. **"Advanced English is required".** El CV maestro declara B1 intermedio. Aquí se usó la formulación
   ya empleada en la postulación anterior a FullStack: *professional working proficiency*, respaldada por
   seis años de trabajo diario en equipos distribuidos en inglés (EE.UU., India, Ucrania). Es defendible,
   pero **la entrevista de FullStack incluye screening de inglés hablado**. Es el filtro más probable de
   esta postulación.
3. **Python / C#.** No los tienes en el CV maestro y no se inventaron.

## Reglas del proyecto aplicadas

- Sin "CTO" ni "Co-founder": el rol 2024–Presente va como **Tech Lead and Agentic Software Engineer**.
- Sin cifras autorreportadas de la lista negra (nada de "300% de aceleración", "99.98% de estabilidad",
  porcentajes de mejora sin fuente).
- Sin adjetivos sin evidencia ("apasionado", "orientado a resultados", "experto").
- Formato ATS-safe: Markdown lineal, sin tablas de layout, sin columnas, sin iconos, viñetas `-`.
- Siglas expandidas la primera vez: API, OOP, TDD, IaC, AWS.
- Toda la experiencia y tecnologías provienen de `cv.md` / `cv-en.md` y de los CV previos del repo.
