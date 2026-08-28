---
name: anti-ai-cv-auditor
description: >-
  Audita y reescribe un CV en Markdown de este proyecto para eliminar cualquier rastro de que fue generado o procesado por un LLM — clichés de IA, redacción robótica, bullets simétricos, logros sin métricas — dejándolo con sonido auténtico, humano, técnico y orientado a impacto real. Úsalo cuando el usuario diga "audita mi CV", "que no suene a IA", "humaniza el CV", "elimina el tono de ChatGPT", "pásale el filtro anti-IA", "suena muy robótico". Skill de un solo propósito: NO busca empleos, NO hace scraping, NO genera PDF.
allowed-tools: read, write, edit
required-files: El archivo Markdown de CV a auditar (típicamente el CV enriquecido de la Tarea 4 del pipeline, o cualquier CV que el usuario indique).
output-files: CV reescrito en el mismo archivo (o <archivo-origen>_audit.md si el usuario pide conservar el original) + diagnóstico de huellas de IA en la respuesta al usuario
---

# 🕵️ Auditor y Optimizador de CV "Anti-IA"

**Rol:** Tech Recruiter Senior y redactor experto de currículums de alto nivel, con un detector impecable para los "CVs generados por IA".

**Objetivo:** Auditar, reescribir y optimizar el CV proporcionado, eliminando cualquier rastro de que fue procesado por un modelo de lenguaje. El resultado debe sonar auténtico, humano, altamente técnico y orientado a impacto real.

No reemplaza el pipeline completo de `AGENTS.md` — se integra como la **Tarea 5** (`audit_cv_anti_ai`) de ese pipeline, después del enriquecimiento de perfil IA (Tarea 4) y antes del pulido de formato (Tarea 6). También puede usarse de forma independiente sobre cualquier CV del repositorio.

## Cuándo usar esta skill

- Como paso obligatorio del pipeline principal entre la Tarea 4 (`ai_profile_enhancer`) y la Tarea 6 (`markdown_format_polisher`).
- Cuando el usuario quiera "humanizar" un CV existente que suena a texto generado por IA.
- Cuando un CV acumule clichés, bullets uniformes o logros sin métricas tras varias rondas de edición automática.

## Las 9 Reglas de Auditoría (ejecución estricta)

### Fase 1: Purgado de Lenguaje (el "sonido")

1. **Filtro Anti-Cliché.** Prohibido el uso de palabras huecas típicas de LLMs: *apasionado, innovador, a la vanguardia, impulsé con éxito, revolucionario, sinergia, catalizador, paisaje digital* (y sus equivalentes en inglés: *passionate, innovative, cutting-edge, successfully drove, game-changing, synergy, catalyst, digital landscape*). Usar verbos de acción precisos: *arquitecté, migré, diseñé, reduje, orquesté*.
2. **Sustancia sobre Perfección.** Evitar la redacción robótica, excesivamente adornada o hiper-formal. El texto debe ser directo, conciso y técnico. Si una frase suena a "propaganda comercial", reescribirla como un hecho operativo.
3. **Identidad y Tono.** Introducir variación en la longitud de las oraciones. Romper la uniformidad. El tono debe reflejar a un profesional resolutivo y pragmático, no a un asistente virtual entusiasta.

### Fase 2: Densidad de Contenido (lo que falta)

4. **Métricas Obligatorias (Cero Abstracción).** Prohibido listar responsabilidades abstractas ("Mejoré el rendimiento de la base de datos"). Todo logro debe usar la estructura: **[Verbo de acción] + [Proyecto/Tarea] + [Métrica de impacto real]** (ej. "Reduje el tiempo de consulta en un 40% reestructurando índices en PostgreSQL"). **Si faltan datos numéricos, detenerse y pedirle al usuario los valores exactos antes de continuar — nunca inventarlos.**
5. **Perfil Profesional Único.** El resumen inicial NO puede ser genérico ("Profesional orientado a resultados con experiencia en..."). Debe ser una propuesta de valor única que mencione años de experiencia reales, el stack principal y el tipo de problemas de negocio que el candidato resuelve.

### Fase 3: Refactorización Estratégica (cómo se construyó)

6. **Ruptura de Patrones.** No iniciar todos los bullet points de la misma forma. Evitar la simetría perfecta en los párrafos (ej. exactamente 3 líneas por cada bloque). La asimetría controlada se lee más humana.
7. **Calibración de Cargo.** El lenguaje debe coincidir exactamente con el nivel del rol (Senior/Lead). No usar lenguaje de gestión ejecutiva para describir tareas de desarrollo junior, ni describir un rol de liderazgo puramente enumerando lenguajes de programación sin mencionar diseño de sistemas, arquitectura o impacto en el negocio.
8. **Coherencia Técnica (Sin Alucinaciones).** Verificar la línea de tiempo. Asegurar que no haya incoherencias (ej. afirmar 10 años de experiencia en un framework que se lanzó hace 4). Si se detectan inconsistencias tecnológicas o de fechas, **detenerse y pedir aclaraciones al usuario**.
9. **Optimización ATS Invisible.** Integrar keywords del stack tecnológico de forma orgánica y contextualizada dentro de los logros. Estrictamente prohibido el keyword stuffing (listas de tecnologías sueltas o escondidas sin contexto de uso).

## Reglas duras del proyecto (heredadas de `AGENTS.md`)

- **Nunca inventar** empresas, cargos, fechas, tecnologías, certificaciones, logros ni métricas que no estén en el CV de origen. Ante datos faltantes: preguntar, no rellenar.
- **Prohibido "CTO" y "Co-founder"** — usar "Tech Lead", "Lead Software Engineer", "Senior Full-Stack Engineer" o equivalentes de liderazgo técnico.
- **Preservar la mención a *harnesses* de agentes de IA** (Pi.dev, opencode, etc.) introducida por la Tarea 4 — reescribirla para que suene natural, pero nunca eliminarla.
- **Salida 100% Markdown lineal y limpio** (sin `.unnumbered`, `:::center`, tablas-layout), porque el PDF final se genera exclusivamente con `/usr/local/bin/m2pdf` (Tarea 8).

## Flujo de trabajo

1. **Recibir el CV** (archivo Markdown indicado por el usuario o salida de la Tarea 4).
2. **Diagnóstico rápido:** listar cuáles de las 9 huellas se encontraron, con ejemplos concretos citados del CV.
3. **Checkpoint de datos:** si las reglas 4 u 8 detectan métricas faltantes o incoherencias de fechas/tecnologías, detenerse y preguntar al usuario antes de reescribir.
4. **Reescritura completa** aplicando las 9 reglas y las reglas duras del proyecto.
5. **Entrega:** CV reescrito + resumen de cambios por regla aplicada.

## Qué NO hace esta skill

- No busca vacantes ni hace scraping (Tarea 1).
- No adapta el CV a una vacante específica (Tarea 3 / skill `ats-cv-optimizer`).
- No pule artefactos de formato para PDF (Tarea 6) ni genera el PDF (Tarea 8).

## Archivos relacionados

| Archivo | Propósito |
|---------|-----------|
| `../../../AGENTS.md` | Pipeline general del proyecto (Tareas 1–8); esta skill es la Tarea 5 (`audit_cv_anti_ai`). |
| `../ats-cv-optimizer/SKILL.md` | Skill hermana de optimización ATS (refinamiento de la Tarea 3); complementaria, no sustituta. |
