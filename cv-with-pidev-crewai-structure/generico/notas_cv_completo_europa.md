# Notas de decisiones — CV completo para Europa (base Knowmad Mood)

**Fecha:** 2026-09-10 · **Archivos:** `cv_gonzalo_completo_europa_es.md` / `.pdf` (A4, 5 páginas, ATS-safe)

## Propósito

CV maestro extenso (sin límite de páginas) en español de España, con resumen orientado a un reclutador europeo. Pensado como base para Knowmad Mood (cubre sus dos vacantes vistas: Software Engineer Java remoto y Fullstack Java + React en logística) y reutilizable para cualquier empresa de la UE.

## Fuentes usadas (nada inventado)

- `cv.md` (fuente de verdad) para roles, fechas y stacks.
- Salcobrand 2023–2024: respaldado por `gft_technologies/respuestas_whatsapp.md` y `agtec_servicios/qa_agtec.md`, ya usado en `alegra/`, `abenis-automatizacion-ia/` y `knowmad/`.
- Detalle de infraestructura GCP/Pulumi/Cloud Armor: `alegra/cv_gonzalo_alegra_cloud_engineer.md`.
- Proyectos de IA (RAG Spring AI, farma Jido.AI, zapatería Cloudflare): memoria `proyecto-rag-ley-datos-personales` y `abenis-automatizacion-ia/`.
- Proyecto niuro (Next.js/NestJS/Jest/JWT): `factor-it-2/`.
- Pagos Transbank/Khipu y Google Maps: `factor-it-2/` y `cv.md`.
- Movilidad a Madrid, Tarjeta Azul-UE, contractor/EOR: memoria `objetivo-empleo-espana` y `JOB-PORTALS.md`.
- Inglés B2 y "titulación universitaria completa": memoria `datos-para-formularios-postulacion`.

## Ganchos "para Europa" del resumen

1. 17 años para Santander/Isban (grupo bancario español) en cinco países.
2. Tres años en equipos distribuidos 100% en inglés (Citibank, Perficient–Caterpillar).
3. RAG sobre la Ley 21.719, inspirada en el RGPD.
4. IA con proceso (Claude Code + openspec + tests), no "vibe coding".
5. Reubicación inmediata a Madrid + vías de contratación declaradas (Tarjeta Azul-UE, B2B, EOR).

## Qué se dejó fuera y por qué

- **WebClass, Creasys, Coopeuch (2008–2017):** el `cv.md` maestro actual ya no los lista (fueron reemplazados por Nubox, Cencosud, Portal Inmobiliario y Santander/Isban en el commit `c09c9d2`). Siguen en `profile/achievements.md` (plataforma educativa en 1.800 escuelas). Si quieres recuperarlos, hay que reincorporarlos primero al `cv.md`.
- **OAuth/OpenID, Kubernetes, Kafka, RabbitMQ, Terraform, Redux:** gaps declarados en notas previas (`knowmad/`, `factor-it-2/`, `alegra/`); no se reclaman.
- **"Java 21" en Perficient (2022–2023):** se escribió "Java, Spring Boot" porque Java 21 se publicó en septiembre de 2023 y un revisor europeo podría objetarlo. Java 21 sí se declara en Te Llevo.
- **Cifras de la lista negra:** ninguna. Únicas métricas: 15M+ registros (Citibank), 4 desarrolladores (Seven IT), 17 años (Santander/Isban), 15+ años.
- **CTO / Co-founder:** no se usan (Restricción global n.º 1); se usa "Tech Lead y Arquitecto".

## Formato

- ATS-safe por defecto (Restricción n.º 5). **Harvard no aplicado**: se genera solo si lo pides explícitamente.
- Sin itálicas; fuente por defecto del contenedor `pandoc/extra` (no tiene Tahoma/Calibri/Times). Papel A4 vía YAML (`papersize: a4`), estándar europeo.
- Orden: Resumen → Por qué Europa → Experiencia → Proyectos → Cómo trabajo → Habilidades Técnicas → Educación e Idiomas (+ Movilidad + Competencias con evidencia), conforme a Restricciones n.º 7 y 8.

## Pendiente

- No es una postulación enviada: no se registra en `cv_job_links.md` ni en `../proceso/track`. Cuando lo uses para una vacante concreta, adaptar título/keywords y registrar ahí.
