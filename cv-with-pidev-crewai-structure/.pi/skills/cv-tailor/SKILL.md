---
name: cv-tailor
description: Genera un CV adaptado a UNA oferta laboral específica a partir del CV maestro de Gonzalo Oviedo Lambert. Úsala SIEMPRE que se mencione postular, adaptar el CV, una oferta de trabajo, un job posting, una vacante, LinkedIn, un reclutador, o se pegue el texto de una descripción de cargo — incluso si no se pide explícitamente "adapta mi CV". También aplica para generar la versión en inglés, la carta de presentación breve y el mensaje de outreach asociado.
---

# CV Tailor — Gonzalo Oviedo Lambert

Generas un CV por oferta. Nunca un CV genérico. Si no hay oferta en el input, **pídela antes de escribir nada**.

## Regla número uno: verificabilidad sobre impresión

El CV maestro contiene cifras autorreportadas que dañan la credibilidad ante un revisor técnico senior. Tu trabajo es reemplazarlas por hechos que resistan una entrevista.

**PROHIBIDO escribir (lista negra literal):**
- "300% de aceleración", "picos sobre 2000%", "99.98% de estabilidad"
- Cualquier porcentaje de mejora superior a 50% sin fuente medible
- Combinaciones de más de 3 métricas porcentuales en la misma sección
- Adjetivos sin evidencia: "experto", "apasionado", "orientado a resultados", "proactivo"

**Sustituir por hechos comprobables:**
| En vez de | Escribe |
|---|---|
| "Aceleración del ciclo de desarrollo de 300%" | "Definí e implanté el flujo de trabajo con agentes de código del equipo (spec → plan → ejecución → verificación), con suite de tests automatizados como puerta de calidad" |
| "99.98% de estabilidad en producción" | "Plataforma en producción con usuarios reales en app.tellevoapp.cl desde 2024" |
| "Reducción de costos cloud del 45%" | "Infraestructura GCP completamente automatizada con Pulumi (IaC), migrada a Cloud Run serverless" |

**Excepción — cifras que SÍ se conservan** porque son verificables y de dominio duro:
- Migración Sybase → Oracle: 15M+ registros financieros, 0% de pérdida de datos (Citibank)
- Plataforma educativa en 1.800 escuelas, 500k+ peticiones diarias
- Equipo de 4 desarrolladores liderado (Seven IT)

Criterio: si en una entrevista no puede explicar **baseline, instrumento de medición y ventana temporal**, la cifra no va.

## Paso 1 — Clasifica la oferta

Lee la oferta y determina el perfil. Si es ambiguo, elige el de mayor pago.

**A. Chile local (CLP, empresa chilena)**
- Idioma: español. Título: "Lead Software Engineer / Arquitecto de Software"
- Peso: 60% experiencia banca/regulado (Citibank, Santander, Coopeuch) + 40% arquitectura cloud
- La IA agéntica va como último bullet de habilidades, no como titular — en el mercado local todavía genera ruido, no premium
- Expectativa de renta si la piden: **$5.500.000 – $8.000.000 brutos**. Nunca menos de $5.500.000

**B. Remoto internacional USD (empresa extranjera, EOR o contractor)**
- Idioma: **inglés siempre**, aunque la oferta esté en español
- Título: "Staff Software Engineer" o "AI-Augmented Engineering Lead"
- Peso: 50% arquitectura end-to-end y ownership + 30% IA agéntica + 20% escala/banca
- Frase obligatoria cerca del inicio: propiedad de la arquitectura de punta a punta y mentoría de equipo sin supervisión — es el criterio literal que usan las plataformas de vetting para clasificar lead vs. senior
- Inglés: escribe "Professional working proficiency — 6+ years in fully English-speaking distributed teams (US, India, Ukraine)". No escribas "B1"
- Expectativa: **USD 4.000 – 6.000/mes** o **USD 45–60/hora**. Nunca menos de USD 3.500

**C. Nicho Elixir / BEAM**
- Idioma: inglés
- Título: "Senior Elixir Engineer" o "Elixir/Phoenix Architect"
- Elixir/Phoenix/OTP/LiveView/Ash sube a la primera línea del resumen y encabeza habilidades
- Java baja a una línea de contexto histórico
- Este es el mercado de menor competencia: casi no hay ofertas junior, y la escasez de candidatos senior es real
- Expectativa: **USD 6.000 – 9.000/mes**

## Paso 2 — Extrae keywords de la oferta y espéjalas

Los filtros automáticos comparan literales, no sinónimos.

1. Extrae de la oferta: tecnologías, versiones, metodologías, verbos del rol, nombre exacto del cargo
2. Cruza contra lo que Gonzalo **realmente** tiene. Si no lo tiene, **no lo inventes** — la honestidad no es negociable aquí
3. Usa la ortografía exacta de la oferta: si dice "Spring Boot 3", no escribas "Spring"; si dice "GCP", no escribas "Google Cloud"
4. El título del CV debe coincidir palabra por palabra con el título de la vacante cuando sea razonable
5. Densidad objetivo: cada keyword crítica aparece 2–3 veces (resumen, habilidades, un bullet de experiencia)

## Paso 3 — Estructura del output

Máximo **2 páginas**. Orden fijo:

1. **Encabezado** — nombre, título espejado de la oferta, ciudad, email, teléfono, LinkedIn. Sin foto, sin RUT, sin estado civil, sin fecha de nacimiento
2. **Resumen (3–4 líneas)** — reescrito por oferta. Debe responder: qué construye, para qué dominio, con qué stack, a qué escala. Sin adjetivos de la lista negra
3. **Habilidades técnicas** — máximo 6 categorías, keywords de la oferta primero
4. **Experiencia** — TeLlevoApp y las 2 más relevantes con 3–4 bullets; el resto comprimido en una línea agrupada. Cada bullet: verbo en pasado + qué construiste + restricción técnica real. No todos los bullets llevan métrica
5. **Educación e idiomas** — 2 líneas

Formato de bullet: `Verbo + sistema + decisión técnica + resultado verificable (opcional)`

## Paso 4 — Verificación antes de entregar

Recorre esta lista y reporta el resultado. Si algo falla, corrígelo y vuelve a pasar.

- [ ] ¿Cero cifras de la lista negra?
- [ ] ¿Toda afirmación resistiría "cuénteme más sobre eso" en una entrevista?
- [ ] ¿El título del CV coincide con el título de la oferta?
- [ ] ¿Las 5 keywords principales de la oferta aparecen al menos dos veces?
- [ ] ¿Ninguna tecnología listada que Gonzalo no haya usado de verdad?
- [ ] ¿Máximo 2 páginas?
- [ ] ¿Idioma correcto según el perfil A/B/C?
- [ ] ¿Cero adjetivos vacíos?

## Paso 5 — Entregables

Junto al CV, genera siempre:

1. **CV** en Markdown limpio, exportable a PDF, nombre de archivo `Gonzalo_Oviedo_[Empresa]_[Cargo].md`
2. **Mensaje de contacto (máx. 120 palabras)** — para el reclutador o el hiring manager en LinkedIn. Nunca empieza con "Estoy buscando trabajo". Empieza con qué construyó que se parece a lo que ellos necesitan
3. **Nota de decisiones (máx. 5 líneas)** — qué perfil elegiste, qué keywords espejaste, qué dejaste fuera y por qué. Es para que Gonzalo pueda auditar y corregir el criterio, no relleno

## Fuente de verdad

El CV maestro es el archivo de referencia. Nunca agregues experiencia, empresa, título o tecnología que no esté ahí. Reordenar, comprimir, traducir y reformular está permitido. Inventar, no.
