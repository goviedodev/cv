# Notas de decisiones — ProntoPaga (Full-Stack Engineer, Semi Senior)

## Vacante y modo de ejecución

- **URL:** https://www.getonbrd.com/jobs/programming/full-stack-engineer-semi-senior-prontopaga-santiago/ (Get on Board, Job ID 63341, publicada 27-08-2026).
- **Modo directo** (Restricción de `AGENTS.md` §4): el usuario trajo la oferta por URL, se saltaron las Tareas 1–2 y ejecutó `cv_tailor`.
- **Extracción:** `WebFetch` agotó el timeout de 60 s; se resolvió con `curl` + conversión HTML→texto en el scratchpad. La oferta completa quedó archivada en `job_description.md`.

## Decisiones confirmadas por el usuario

1. **Idioma: CV y materiales en inglés.** El aviso marca explícitamente *"Requires applying in English"*. Todo (CV, mensaje al reclutador, carta y respuestas) está en inglés.
2. **Formato: ambas versiones.** ATS-safe (`cv_gonzalo_prontopaga_fullstack.md/pdf`) para subir al portal, y Harvard (`..._harvard.md/pdf`) para envío directo o entrega en mano. Restricción global n.º 5 satisfecha: se preguntó antes de aplicar Harvard.
3. **Ubicación en el encabezado: "Valparaíso Region / Santiago Metropolitan Region, Chile"** — opción elegida por el usuario. No se usó dirección falsa de Santiago (regla previa del usuario) ni se declaró disponibilidad explícita de reubicación.

## Perfil y ángulo

- **Perfil A** (Chile local, empresa chilena vía Get on Board), pero **redactado en inglés** por exigencia del aviso. Renta publicada USD $2.000–$3.000 brutos/mes; en `respuestas_postulacion.md` se declara alineación con esa banda sin pedir más.
- **Título espejado:** "Full-Stack Engineer" (exacto del aviso) + cola de stack real: `React · TypeScript · REST APIs · Cloud & CI/CD`. **No** se puso "AWS Serverless" en el título porque la experiencia real no lo sostiene (ver gaps).
- **Ángulo principal: dominio de pagos/fintech.** ProntoPaga hace recaudación y dispersión de pagos; el respaldo real es fuerte y verificable: 17 años en Santander/Isban (préstamos, medios de pago, cuentas corrientes, tarjetas), Citibank, integración Transbank (Webpay) y Khipu en la plataforma de movilidad (checkout, confirmación, conciliación, callbacks asincrónicos), módulo transaccional de pagos en Seven IT y facturación electrónica en Nubox. Es el diferenciador frente a otros postulantes semi-senior.
- **Ángulo secundario: desarrollo asistido por IA.** El aviso **nombra Claude Code explícitamente** y descarta el *"vibe coding"*. Se redactó el flujo real (spec → plan → ejecución → verificación, con revisión y propiedad de cada línea que se mergea) como hecho verificable, sin cifras de productividad. Es probablemente el punto de mayor calce y se trató como tal, no como adorno.
- **Liderazgo técnico:** el aviso pide "experiencia comprobable liderando técnicamente equipos o proyectos" — respaldado con los 4 desarrolladores liderados en Seven IT vía Merge Requests en GitLab.

## Gaps reales — declarados, no inflados

Verificados contra el repositorio antes de escribir (`michael-page/mensaje_reclutador.md`, `Alegra/`, `autopostulacion/getonboard/perfil_getonboard.md`):

| Requisito del aviso | Realidad | Cómo se declaró |
|---|---|---|
| Arquitecturas **serverless en AWS** | Ha usado **Lambda y S3**; su cloud productiva es **GCP** (Pulumi IaC). Nunca diseñó/operó una arquitectura serverless completa en AWS en producción | Declarado de frente en `mensaje_reclutador.md` y en las respuestas 4 y 5; en Habilidades se escribe literalmente "AWS Lambda and S3", no "AWS Serverless" |
| Modelamiento de datos en **DynamoDB** | **Cero experiencia.** NoSQL = MongoDB; profundidad de modelado = relacional | Declarado; se menciona además que *single-table design* no se transfiere del modelo relacional y que lo estudiaría deliberadamente |
| Manejo de estado **Redux** | Context API sí; Redux sin uso productivo | Se listó "state management (Context API)" sin reclamar Redux |
| **Contenedores** (deseable) | Docker sí (builds multi-etapa); Kubernetes no | Se listó solo Docker |

**DynamoDB aparece 0 veces en el PDF** — verificado con `pdftotext`. No se espejó la keyword porque no hay respaldo.

## Cumplimiento de restricciones globales (`AGENTS.md`)

- **n.º 1 (prohibido CTO/Co-founder):** se usó "Tech Lead" en los dos roles correspondientes.
- **n.º 2 (no inventar):** todo sale de `cv.md` + proyecto público `niuro`. Nada agregado.
- **n.º 3 (verificabilidad):** sin cifras de la lista negra. La única métrica es "over 15 million records, no data loss" (Sybase→Oracle), ya validada en CVs anteriores. Sin adjetivos sueltos.
- **n.º 4 (PDF solo con `m2pdf`):** ambos PDFs generados con `/usr/local/bin/m2pdf`. Como está documentado, el primer intento falla por `FreeSerif` y el PDF lo produce el reintento de emergencia.
- **n.º 5 (ATS por defecto, Harvard opt-in):** se preguntó; el usuario pidió ambos.
- **n.º 6 (registro en `../proceso/track`):** **cumplida.** Postulación **enviada el 2026-08-28** y registrada en `$HOME/proyectos/cv/proceso` con id `2026-08-28-prontopaga-full-stack-engineer-semi-senior` (etapa `postulado`, modalidad `presencial`, `idioma_cv=en`). El `add` del CLI es solo interactivo, así que se escribió con las funciones de `src/store.py`, la vía que contempla `AGENTS.md`.
- **n.º 7 (orden de secciones):** verificado en el texto extraído del PDF — `Professional Summary → Professional Experience → Featured Public Project → Technical Skills → Education & Languages`. Habilidades Técnicas queda inmediatamente antes de Educación e Idiomas.
- **n.º 8 (bloque de Competencias):** presente al cierre de *Education & Languages*, en inglés, con la evidencia concreta entre paréntesis para cada competencia (incluidas "results orientation" e "initiative", que sin evidencia caerían en la lista negra de la n.º 3).

## Nota de maquetación

Las dos versiones salieron inicialmente en **3 páginas**. `m2pdf` fuerza `-V geometry:margin=2cm` por línea de comandos, que pisa cualquier `geometry` puesto como metadato YAML; el override efectivo es `\geometry{...}` dentro de `header-includes` con valla `{=latex}`. Se aplicó a ambas (márgenes, interlineado y espaciado de listas, **sin tocar contenido**) y las dos quedaron en **2 páginas**. En la versión ATS el preámbulo solo ajusta márgenes: no introduce tablas ni columnas de layout, y se verificó con `pdftotext` que el texto sigue extrayéndose lineal, completo y en orden de lectura.

## ⚠️ Advertencias al usuario antes de enviar

1. **La vacante es 100% presencial en Santiago** ("Position is on-site and must be performed entirely in: Santiago"). El usuario vive en Limache y su criterio declarado es híbrido/remoto. Esto es incompatible con su filtro habitual salvo que decida reubicarse o asumir el traslado. **Es el mayor riesgo de esta postulación y no lo resuelve el CV.**
2. **El cargo es Semi Senior con 2–3 años de experiencia mínima**, y el perfil tiene 15+. Puede leerse como sobrecalificación; la banda USD $2.000–$3.000 brutos está en el límite inferior de la expectativa declarada del usuario ($1.800.000–$3.000.000 **líquidos**) — USD $3.000 brutos no equivale a $3.000.000 líquidos.
3. **AWS serverless + DynamoDB son requisitos centrales del aviso**, no accesorios, y ahí hay un gap real. La estrategia elegida fue declararlo de entrada y compensar con el dominio de pagos. Si el filtro técnico es estricto en AWS, esta postulación cae — conviene tenerlo presente al calibrar expectativas.
