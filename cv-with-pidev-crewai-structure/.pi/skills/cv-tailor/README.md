# ✂️ CV Tailor

Skill de propósito único para este proyecto: genera un CV adaptado a **una oferta laboral específica** a partir del CV maestro (`cv.md`), corrigiendo las cifras autorreportadas no verificables y espejando las keywords de la vacante. Nunca produce un CV genérico: si no hay oferta en el input, pide una antes de escribir.

## Qué hace

- **Clasifica la oferta** en uno de 3 perfiles con estrategia propia (título, idioma, pesos y expectativa de renta):
  - **A. Chile local** (CLP, empresa chilena)
  - **B. Remoto internacional USD** (EOR o contractor)
  - **C. Nicho Elixir / BEAM**
- **Corrige la verificabilidad**: elimina las cifras de la lista negra ("300% de aceleración", "99.98% de estabilidad", etc.) y las reemplaza por hechos que resisten una entrevista técnica. Conserva solo métricas de dominio duro comprobables.
- **Espeja keywords** de la oferta con la ortografía exacta (densidad 2–3 apariciones por keyword crítica), sin inventar tecnologías que el candidato no tenga.
- **Entrega 3 artefactos**: CV en Markdown (máx. 2 páginas), mensaje de contacto para LinkedIn (máx. 120 palabras) y nota de decisiones auditable (máx. 5 líneas).

## Qué NO hace

- No busca empleos ni hace scraping (eso es la Tarea 1 / `multi_portal_scraper`).
- No inventa experiencia, empresas, títulos ni tecnologías — el CV maestro es la única fuente de verdad.
- No genera el PDF final — el único conversor autorizado del proyecto es `/usr/local/bin/m2pdf` (ver Tarea 8 de `AGENTS.md`).

## Integración en el pipeline

Es el motor del agente `cv_tailor` de `AGENTS.md`. Puede usarse de dos formas:

1. **Dentro del pipeline**: como refinamiento de la **Tarea 3** (`resume_skills_customizer`) cuando ya hay una vacante seleccionada por la Tarea 2 — aplica la clasificación de perfil y la corrección de verificabilidad antes de las Tareas 4–8.
2. **De forma independiente**: cuando el usuario pega una oferta, un job posting o pide adaptar/corregir el CV para una vacante concreta, sin ejecutar el pipeline de scraping completo.

Compatible con las restricciones globales del proyecto: prohibido "CTO"/"Co-founder" (usar "Tech Lead" / "Lead Software Engineer"), y auditoría Anti-IA (Tarea 5) + `m2pdf` (Tarea 8) siguen aplicando al entregable final.

Ver `SKILL.md` en esta misma carpeta para la lista negra completa, los 3 perfiles de oferta y el checklist de verificación.
