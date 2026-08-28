# 🕵️ Anti-AI CV Auditor

Skill de propósito único para este proyecto: audita y reescribe un CV en Markdown para eliminar las huellas de texto generado por IA (clichés de LLM, redacción robótica, bullets simétricos, logros sin métricas) y dejarlo con sonido humano, técnico y orientado a impacto real.

## Qué hace

- Diagnostica el CV contra **9 reglas de auditoría** en 3 fases: purgado de lenguaje, densidad de contenido y refactorización estratégica.
- Reescribe el CV aplicando esas reglas, sin inventar información nueva.
- Se detiene y pregunta al usuario cuando faltan métricas reales o hay incoherencias de fechas/tecnologías.

## Qué NO hace

- No busca empleos ni hace scraping.
- No adapta el CV a una vacante (eso es la Tarea 3 / skill `ats-cv-optimizer`).
- No genera el PDF final — el único conversor autorizado del proyecto es `/usr/local/bin/m2pdf` (ver Tarea 8 de `AGENTS.md`).

## Integración en el pipeline

Se integra en el flujo de `AGENTS.md` como la **Tarea 5** (`audit_cv_anti_ai`, agente `anti_ai_cv_auditor`): recibe el CV enriquecido de la **Tarea 4** (`ai_profile_enhancer`) y entrega el CV auditado a la **Tarea 6** (`markdown_format_polisher`). También puede invocarse de forma independiente sobre cualquier CV del repositorio.

Ver `SKILL.md` en esta misma carpeta para las 9 reglas completas y el flujo de trabajo.
