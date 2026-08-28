# 📋 ATS Checklist — Reglas y Referencia

Documento de referencia para la skill `ats-cv-optimizer`. Basado en investigación de fuentes actuales (2025–2026) sobre cómo parsean y puntúan los CVs los sistemas ATS más usados (Workday, Taleo, iCIMS, Greenhouse, Lever, SmartRecruiters, BrassRing, SAP SuccessFactors). Ver fuentes al final.

---

## 1. Reglas de formato/estructura — qué NO hacer

- **Nunca usar tablas, columnas múltiples, text boxes, headers/footers de Word ni cuadros de texto flotantes.** La mayoría de los parsers ATS (especialmente Taleo, iCIMS, BrassRing) leen el documento linealmente y descartan o desordenan ese contenido.
- **Nunca poner el email o teléfono en un header/footer.** Es invisible para el parser; debe ir en el cuerpo principal, arriba del todo.
- **Sin iconos, gráficos, barras de habilidades, WordArt, imágenes de fondo ni fotos.** Las plantillas con foto o elementos gráficos tienen ~88% de tasa de rechazo en sistemas antiguos.
- **Sin viñetas no estándar** (▶, ➤, ❖, etc.) — usar solo `-` o `•`.
- **Fuente estándar** (Arial, Calibri, Helvetica, Times New Roman, Georgia), 10–12pt cuerpo, 14–16pt títulos. Nada decorativo.
- **Layout de una sola columna.** Orden recomendado: Contacto → Resumen → Habilidades → Experiencia → Educación → Certificaciones.
- **PDF con texto seleccionable, nunca generado desde imagen ni con maquetación LaTeX compleja** (columnas, cajas, `:::center`, clases custom). Con `m2pdf` (pandoc + xelatex, config del proyecto) esto se cumple siempre que el Markdown de origen sea lineal y simple. Verificación rápida: si se puede seleccionar y copiar todo el texto del PDF en orden y sin basura, pasa.
- **PDF vs DOCX (2026):** DOCX sigue teniendo tasa de parseo más alta en sistemas antiguos (Taleo: 97% DOCX vs 83% PDF), pero un PDF de texto plano bien formado funciona bien en sistemas modernos (Greenhouse/Workday/Lever: 95%+). Como este proyecto genera siempre PDF vía `m2pdf`, la mitigación es mantener el Markdown de origen extremadamente simple y lineal.
- **Dato clave:** ~43% de los rechazos automáticos en 2026 son por "technical non-compliance" (errores de parsing/formato), no por falta de calificación del candidato.

## 2. Reglas de contenido/keywords

- **Extraer keywords directamente de la job description**: sustantivos y frases nominales que describan skills, herramientas, metodologías, certificaciones y nivel de seniority.
- **Meta de densidad:** 15–25 keywords totales distribuidas en el CV, cubriendo 70–80% de las de la vacante. Menos de 10 = ranking bajo; más de 30 sin contexto = keyword stuffing (penaliza ~30% el score).
- **Ubicación estratégica:** 3–4 keywords principales en el resumen (2–3 frases), el resto repartidas entre Habilidades y bullets de Experiencia **con contexto real** (acción + alcance + resultado), no como lista pegada.
- **Match exacto > sinónimo.** Aunque los ATS modernos (2026) hacen matching semántico (ej. "team leadership" ≈ "led cross-functional teams"), el match literal sigue pesando más. Si la vacante dice "business development representative", usar esa frase textual, no solo "sales rep".
- **Siglas:** escribir siempre el término completo + sigla la primera vez: "Search Engine Optimization (SEO)", "Machine Learning (ML)". Los parsers no siempre equivalen sigla ↔ término completo.
- **Headline del CV** (línea bajo el nombre): debe reflejar el título exacto de la vacante objetivo — los CVs que espejan el título exacto reciben ~10.6x más invitaciones a entrevista. Esto no equivale a mentir sobre cargos pasados: el headline apunta al puesto target, pero el historial de Experiencia debe seguir siendo veraz (coherente con la regla ya existente en `AGENTS.md` de evitar "CTO"/"Co-founder" y usar equivalentes honestos).
- **Cuantificar todo lo posible.** Los ATS con IA en 2026 puntúan "achievement density" (bullets con números/%/resultados). Reemplazar frases genéricas por logros medibles aumenta ~40% las callbacks.
- **Evitar buzzwords/clichés vacíos:** "passionate", "results-driven", "team player", "responsible for", "hard worker", "innovative", "good communicator". Son invisibles o negativos para ATS con IA en 2026 — sustituir por logro concreto con verbo de acción + cifra.
- **Fechas consistentes:** "Month YYYY – Present" en todo el documento, sin abreviaturas tipo `'21`. Orden cronológico inverso siempre.
- **Longitud de bullets:** 15–25 palabras, 1–2 líneas máx.; 3–5 bullets por rol (hasta 6 en el más reciente/relevante, 2–3 en roles antiguos).
- **Contexto importa más que la keyword pelada.** En 2026, con casi todos los candidatos usando IA generativa para postular, los sistemas de screening con IA también evalúan especificidad y verosimilitud del logro, no solo presencia de la keyword.

## 3. Encabezados de sección canónicos

| Español | Inglés |
|---|---|
| Resumen Profesional | Professional Summary |
| Experiencia Laboral / Experiencia Profesional | Work Experience / Professional Experience |
| Habilidades / Habilidades Técnicas | Skills / Technical Skills |
| Educación | Education |
| Certificaciones | Certifications |
| Idiomas | Languages |
| Proyectos | Projects |

Evitar títulos creativos ("Mi trayectoria", "Lo que aporto", "Career Journey", "My Strengths"): el parser está entrenado en estos términos estándar; un header no reconocido puede hacer que esa sección entera se pierda o se clasifique mal.

## 4. Checklist final accionable (verificar antes de entregar)

1. ¿El PDF tiene texto 100% seleccionable/copiable (no imagen)?
2. ¿Una sola columna, sin tablas ni text boxes?
3. ¿Contacto (email/teléfono) en el cuerpo, no en header/footer?
4. ¿Fuente estándar, 10–12pt cuerpo?
5. ¿Encabezados de sección estándar (ver tabla arriba)?
6. ¿Orden cronológico inverso en experiencia y educación?
7. ¿Fechas en formato consistente Month YYYY en todo el documento?
8. ¿El headline del CV usa el título exacto de la vacante target?
9. ¿15–25 keywords de la vacante cubiertas, 70–80% de coincidencia?
10. ¿Cada sigla técnica está escrita completa + sigla la primera vez?
11. ¿Cero tablas markdown/gráficos/iconos en la versión final?
12. ¿Viñetas estándar (`-` o `•`), sin símbolos raros?
13. ¿3–5 bullets por rol, 15–25 palabras cada uno?
14. ¿Cada bullet relevante tiene cifra/resultado medible (no solo tarea)?
15. ¿Cero buzzwords vacíos ("team player", "results-driven", etc.)?
16. ¿Cero errores ortográficos/gramaticales (77% de hiring managers descartan por esto)?
17. ¿No se inventó ni tergiversó ningún dato (cargos, fechas, empresas)?
18. ¿El Markdown no tiene artefactos de conversión (`.unnumbered`, `:::center`, clases LaTeX)?
19. ¿Longitud coherente con la experiencia (1 página junior, 2 páginas 5+ años)?
20. ¿Se validó copiando el texto del PDF final a un editor plano para confirmar que se lee todo, en orden y sin basura?

## Fuentes

- [ATS Resume Guide 2026 — bestjobsearchapps](https://bestjobsearchapps.com/articles/en/ats-resume-guide-2026-format-keywords-and-best-practices-to-beat-applicant-tracking-systems)
- [How ATS Systems Actually Work in 2026 — QuickCV](https://quickcv.io/blog/how-ats-systems-work-2026)
- [PDF vs DOCX for ATS in 2026 — CVCraft](https://cvcraft.roynex.com/blog/pdf-vs-docx-resume-ats-2026)
- [Workday ATS Guide 2025 — atshiring.com](https://www.atshiring.com/en/learn/workday-ats-guide-2025)
- [Greenhouse ATS Resume Guide — Resume Optimizer Pro](https://resumeoptimizerpro.com/blog/greenhouse-ats-resume-guide)
- [ATS Resume Format 2026 — scale.jobs](https://scale.jobs/blog/ats-resume-format-2026-design-guide)
- [Anatomy of an ATS Friendly Resume Format — Jobscan](https://www.jobscan.co/blog/20-ats-friendly-resume-templates/)
- [500+ Resume Keywords for the ATS 2026 — Jobscan](https://www.jobscan.co/blog/top-resume-keywords-boost-resume/)
- [Resume Trends 2026 — Skills-First, Semantic & AI — Resumefry](https://resumefry.com/blog/resume-trends-2026)
- [Semantic Search Resume Optimization 2026 — Resumefin](https://www.resumefin.com/post/semantic-search-resume-optimization-2026)
- [How Many Bullet Points Per Job — Extern](https://www.extern.com/post/resume-bullet-points-guide)
- [The Resume Format To Beat ATS in 2026 — Forbes](https://www.forbes.com/sites/rachelwells/2026/03/11/the-resume-format-to-beat-ats-and-get-hired-in-2026/)
- [AI Recruiting Platform Comparison 2026 — GoMokka](https://www.gomokka.com/resources/choosing-ai-recruiting-partner.html)
- [AI in Recruitment 2026 — GoPerfect](https://www.goperfect.com/blog/ai-recruitment-the-2026-complete-guide-to-everything-you-need)
- [How to Write an ATS Resume That Gets Past the Bots in 2026 — Jobscan](https://www.jobscan.co/blog/ats-resume/)
- [Top 10 ATS Resume Mistakes to Avoid in 2026 — Careerflow](https://www.careerflow.ai/blog/ats-resume-mistakes-to-avoid)
- [Words Recruiters Hate on Your Resume in 2026 — CareerEnlightenment](https://careerenlightenment.com/words-recruiters-hate-on-resume-2026)
- [Resume Title Examples 2026 — The Interview Guys](https://blog.theinterviewguys.com/resume-title-examples/)
- [ATS Resume Keywords in 2026 — moncvhub](https://www.moncvhub.fr/en/blog/ats-resume-keywords-2026)
