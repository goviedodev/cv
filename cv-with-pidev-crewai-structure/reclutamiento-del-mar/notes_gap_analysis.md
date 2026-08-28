# Del Mar Technology Group — Arquitecto de Soluciones Cloud Semi-Senior — análisis de encaje

Fecha de preparación: 2026-08-19 · Canal: correo a postulaciones@delmartg.com (exige mencionar pretensión salarial)

## Nota de decisiones (cv-tailor)

- **Perfil elegido: A (Chile local, CLP, español)** — Del Mar TG es consultora chilena (fundada 2015, LinkedIn cl.linkedin.com), aviso en español, ubicación Latam.
- **Keywords espejadas:** GCP, Cloud Run, microservicios, APIs REST, Java / Spring Boot, Docker, IaC, GitLab, IAM, Logging/Monitoring, JWT, manejo de secretos, Confluence, células ágiles, SPA.
- **Dejado fuera (no verificable, prohibido inventar):** Cloud SQL, Pub/Sub, Kubernetes/GKE, Angular, OAuth2/OIDC como implementación productiva, ADRs como práctica formal, Draw.io/Lucidchart/Miro (solo Confluence está en cv.md), Hexagonal/DDD, BigQuery/Dataflow, certificaciones GCP.
- **Pretensión declarada: $3.000.000 líquidos** (techo de la banda de Gonzalo $1.8M–$3.0M; rol de arquitecto justifica el techo). ⚠️ La skill cv-tailor dice "nunca menos de $5.500.000 brutos" para perfil A, pero la práctica real de hoy (Deloitte, Stefanini: $2.800.000 líq. declarados) y la memoria de datos de formularios usan la banda baja — la skill parece desactualizada; Gonzalo debería resolver esa contradicción.
- Formato **ATS-safe por defecto** (sin confirmación explícita no se aplica Harvard).

## Cobertura de requisitos excluyentes

| Requisito excluyente | Estado | Evidencia |
|---|---|---|
| GCP: Storage, IAM, Logging/Monitoring | Cubierto | Te Llevo App: operación diaria de GCP con Pulumi desde 2024; Seven IT en GCP 2017–2020 |
| GCP: **Cloud SQL** | Parcial | PostgreSQL sobre GCP sí; el servicio administrado Cloud SQL no está declarado en cv.md — no se reclamó |
| GCP: **Pub/Sub** | **GAP** | Sin experiencia declarada en mensajería/eventos GCP. No reclamado |
| Microservicios, APIs REST, Java/Spring Boot | Cubierto | Cloud Run en Te Llevo, e-commerce Caterpillar, 15+ años Java |
| **Angular**/SPA | Parcial — divulgado | SPA con Vue.js/Nuxt y React; Angular NO (exclusión declarada en memoria). Divulgado abiertamente en el email |
| Docker, Cloud Run | Cubierto | Uso diario en Te Llevo |
| **Kubernetes / GKE** | **GAP — divulgado** | Solo Docker + Cloud Run. Divulgado en el email como "no he operado GKE en producción" |
| OAuth2, **OIDC**, JWT, secretos | Parcial | JWT + roles en producción (niuro/backend propio); secretos vía IaC. OAuth2/OIDC como protocolo completo no reclamado en el CV |
| CI/CD con GitLab | Cubierto | GitLab en Seven IT y Te Llevo; además Jenkins, Azure DevOps |
| Draw.io/Lucidchart/Miro o **Confluence** | Cubierto (por el "o") | Confluence en Citibank (está en cv.md). Draw.io no reclamado — gap trivial de cerrar |

## Deseables

- **Banca/fintech (pagos):** FUERTE — Citibank, Coopeuch, Santander, módulos de pago en Seven IT y Te Llevo. Es el ángulo principal del email.
- Hexagonal/DDD/EDA, BigQuery/Dataflow, certificaciones: no reclamados.

## Riesgos reales de esta postulación

1. **Tres excluyentes con gap o parcial (Pub/Sub, GKE, Angular).** Estrategia: divulgación honesta de Angular y GKE en el email (misma táctica GraphQL/SoftServe); Pub/Sub y Cloud SQL no se mencionan — si preguntan, la respuesta honesta es "no en producción, pero opero GCP a diario con IaC".
2. **Sobrecalificación:** piden 3–5 años y semi-senior; Gonzalo tiene 15+. Puede jugar a favor (consultora que revende seniority) o en contra (presupuesto semi-senior). La pretensión de $3.0M líq. está probablemente en el rango alto de un semi-senior chileno.
3. **⚠️ Inconsistencia de datos a resolver por Gonzalo:** cv.md dice UBB **2005–2009**; la memoria de formularios (confirmada 2026-08-19) dice **1998–2005**. En este CV se omitieron las fechas de educación para no propagar el error. Corregir cv.md o la memoria.

## Preparación pre-entrevista sugerida

- Repasar Pub/Sub y GKE a nivel de arquitectura (cuándo Cloud Run vs GKE, patrones pub/sub vs REST) — es un rol de arquitecto, preguntarán por criterio de diseño, no por comandos.
- Tener a mano 1–2 diagramas reales de la arquitectura de Te Llevo App (blueprint + flujo de datos): el rol pide literalmente "definir blueprints, diagramas y flujos de datos".
- OAuth2/OIDC: repasar el flujo Authorization Code + PKCE para poder contrastar con el JWT propio que sí implementó.

## Archivos de esta carpeta

| Archivo | Propósito |
|---|---|
| `Gonzalo_Oviedo_DelMar_Arquitecto_Soluciones_Cloud.md` / `.pdf` | CV adaptado (ATS-safe) |
| `email_postulacion.md` | Email listo para enviar + mensaje LinkedIn corto |
| `job_description.md` | Aviso archivado |
| `notes_gap_analysis.md` | Este archivo |
