# Notas de decisiones — Alegra (Cloud Engineer Mid/Sr, 100% remoto)

**Fecha:** 2026-08-28 · **Modo:** directo (texto de la oferta pegado por el usuario, sin scraping) · **Perfil:** A (LATAM / español, Get on Board)

## Decisión central: reposicionamiento de desarrollador a Cloud Engineer

El `cv.md` maestro está redactado como **Senior Backend Architect Java/Spring Boot**. Esta vacante no es de desarrollo: es de operación de infraestructura (serverless, IaC, seguridad cloud, observabilidad, costos). Se reescribió el CV completo poniendo al frente la capa de infraestructura que ya existía en el material del usuario pero estaba subordinada al backend:

- **Fuente principal:** `reclutamiento-del-mar/email_respuestas_gcp_devops_java.md` (2026-08-27), donde el usuario ya documentó Cloud Run, IAM, Logging/Monitoring, **Cloud Armor (WAF)**, Load Balancer y **Pulumi (IaC)** con reglas de firewall, balanceo, permisos y secretos versionados en Git.
- **Fuente secundaria:** `profile/achievements.md` — "Automated cloud infrastructure with Pulumi IaC on GCP" y "microservices architecture transitioning from monolithic systems to cloud-native, event-driven services".
- El rol de Seven IT se recontó como **operación** (servidores Linux, base de datos, respaldos, disponibilidad, escalamiento de incidentes) en vez de como desarrollo del sistema de salud.
- Citibank se recontó por su lado **DevOps** (Jenkins) y de dato crítico (migración Sybase→Oracle), no por el framework Java interno.
- Santander/Isban se recontó por **gestión de incidentes en producción** y migraciones de plataforma.

## Gap duro: AWS y Terraform — cómo se resolvió

El aviso pide 4–5 años operando nube con dominio de Lambda, API Gateway, SQS, SNS, ECS, EC2, S3, Aurora y VPC, más Terraform. La experiencia real del usuario es **GCP con Pulumi**.

- **Pregunta al usuario (2026-08-28):** respondió "Solo GCP + Pulumi (nada productivo en AWS)".
- **Palanca usada:** el aviso dice literalmente **"(o sus equivalentes)"** en el requisito de stack. Se apoyó todo el argumento ahí, mapeando servicio por servicio (Cloud Run ≈ serverless gestionado, Cloud Armor ≈ WAF, Secret Manager ≈ gestión de secretos, Cloud Logging/Monitoring ≈ CloudWatch, Pulumi ≈ Terraform).
- **Inconsistencia detectada y corregida:** `pronto-paga/mensaje_reclutador.md` (postulación de la misma semana, mismo portal) declara *"on AWS I've used Lambda and S3, not a full serverless architecture"*. Escribir aquí "sin experiencia productiva en AWS" habría sido **más restrictivo que lo ya declarado** y una contradicción entre postulaciones. Se alineó la redacción de ambas: **"en AWS he usado Lambda y S3, no una arquitectura serverless completa"**. ⚠️ Si el usuario mantiene que ni Lambda ni S3 son reales, hay que corregir `pronto-paga/` también.
- El gap se declara en tres lugares distintos, no se esconde: bullet **"Equivalencias declaradas"** en Habilidades Técnicas (ambos CVs), párrafo **"Transparencia de stack"** en el resumen (versión Harvard), y `mensaje_reclutador.md` + respuesta (a).
- **No reclamado en ningún lado:** SQS, SNS, ECS, EC2, Aurora, DynamoDB, CloudWatch, Grafana, Kubernetes. No aparecen como experiencia propia en ninguna parte del CV.

## Ángulo diferenciador: IA agéntica

Alegra se declara **AI-First** y pide literalmente uso de "**agentes, MCPs o skills**". Es el punto donde el usuario está por encima del promedio del mercado y no por debajo, así que se le dio peso propio:

- Bullet dedicado en el rol actual, línea propia en Habilidades Técnicas, y una respuesta completa (b) en `respuestas_postulacion.md`.
- Redactado como hecho verificable (qué construyó: skills, comandos, workflows y MCPs sobre Claude Code plan Max; para qué: análisis, automatización de tareas manuales, desarrollo con puertas de calidad), conforme a la Tarea 4 y la Restricción n.º 3 — sin cifras de aceleración ni adjetivos sin evidencia.

## Reflejo léxico (mirroring) — Tarea 3 de AGENTS.md

**Corrección aplicada tras revisión del usuario (2026-08-28).** La primera versión espejaba keywords sueltas (serverless, IaC, IAM, Docker…) pero no las **frases exactas de la publicación**, que es lo que exige la Tarea 3: *"usar las PALABRAS EXACTAS DE LA PUBLICACIÓN ORIGINAL en el resumen y la experiencia laboral, reemplazando sinónimos del CV base por la terminología exacta de la oferta"*. Se reescribieron ambos CVs, el mensaje y las respuestas.

**Decisión estructural:** el rol actual se organizó bajo **los tres pilares con el nombre exacto del aviso** —"Arquitectura serverless y automatización", "Seguridad cloud y platform engineering", "Observabilidad, confiabilidad y costos"— más un bloque "IA en el día a día", igual que el aviso. Un revisor de Alegra lee el CV y encuentra su propia estructura.

**37 frases literales verificadas sobre ambos PDFs** (script de verificación sobre `pdftotext`, 37/37 presentes en ATS y en Harvard):

| Fuente en el aviso | Frase espejada en el CV |
|---|---|
| "responsable end-to-end de mejorar, optimizar y monitorear nuestra infraestructura" | idéntica, abre el resumen |
| "asegurando las plataformas internas que usan los equipos de desarrollo… para moverse rápido y sin fricción" | "asegurando además las plataformas internas que usa el equipo de desarrollo para moverse rápido y sin fricción" |
| "Diseñarás y evolucionarás arquitecturas serverless" | "Diseñé y evoluciono la arquitectura serverless" |
| "para ir reemplazando nuestro monolito" | "reemplazando progresivamente el monolito" |
| "Automatizarás ciclos de despliegue con IaC… para acelerar la entrega de software" | "Automaticé los ciclos de despliegue con IaC… para acelerar la entrega de software" |
| "templates reutilizables de IaC… sin depender de ti" | "código reutilizable… no dependa de mí" (ver limitación abajo) |
| "automatizaciones basadas en agentes de IA para optimizar procesos internos y eliminar tareas manuales" | idéntica |
| "Serás dueño/a de la seguridad de nuestra infraestructura: detección de tráfico anómalo, gestión de secretos, IAM y respuesta ante incidentes" | idéntica, en primera persona |
| "herramientas y plataformas internas para que los equipos de Dev se autogestionen" | "las plataformas internas que usa el equipo de desarrollo… para que desplieguen sin fricción" |
| "Implementarás y auditarás políticas de gobernanza… no solo en el papel" | "Implemento y audito las políticas de acceso y gobernanza como código… no solo en el papel" |
| "sistemas de monitoreo y alertas… con foco en detección proactiva, no reactiva" | idéntica |
| "causa raíz y prevención, no parches" | idéntica |
| "Monitorearás costos de forma continua. Actuarás como referente técnico… uso óptimo" | "monitoreo costos de forma continua actuando como referente técnico… en el uso óptimo de la nube" |
| "IA de forma integrada a tu flujo real de trabajo: agentes, MCPs o skills, especialmente en tareas de análisis, automatización y desarrollo" | "IA integrada a mi flujo real de trabajo: agentes, MCPs y skills… en tareas de análisis, automatización y desarrollo" |
| "diseño de APIs REST y arquitecturas de microservicios" | idéntica |
| "despliegues con Docker" | idéntica |
| "motores SQL y NoSQL" | idéntica, como título de la categoría de bases de datos |
| "lectura técnica, documentación y tutoriales" | idéntica, en Idiomas |
| "Curiosidad Activa / Ownership / Colaboración / Analítica" | bloque Competencias completo, cada una con su evidencia |
| "combinando la rigurosidad del cumplimiento de seguridad con la curiosidad de la Inteligencia Artificial" | espejada en Citibank ("rigurosidad de cumplimiento de seguridad") y cerrando la respuesta (b) |

**Frases del aviso deliberadamente NO espejadas, por falta de evidencia real:**

- **"CloudWatch, Graphana"** — no las ha operado. Se escribió "Cloud Logging/Monitoring, el equivalente de CloudWatch", que nombra la herramienta del aviso sin reclamarla.
- **"Lambda, API Gateway, SQS, SNS, ECS, EC2, Aurora"** — solo se mencionan Cloud Run y API Gateway de GCP marcados explícitamente como "equivalentes de Lambda y API Gateway"; SQS, SNS, ECS, EC2 y Aurora no aparecen en ninguna parte.
- **"cultura post-mortem"** — se espejó la sustancia ("causa raíz y prevención, no parches"), que sí practica, pero **no** la etiqueta "post-mortem", que implicaría un ritual documentado que no está respaldado en `cv.md`.
- **"templates reutilizables de IaC y pipelines para que cada equipo los adopte"** — trabaja con un equipo pequeño, no con múltiples equipos adoptando templates. Se espejó lo verificable ("código reutilizable… no dependa de mí") y se omitió "cada equipo".
- **"crear un repo o una API con el estándar ya aplicado, en un par de clics"** — no tiene un portal de autoservicio de ese tipo. Se espejó "estándares ya aplicados" en el contexto real (pipelines y entornos que usa su equipo).

## Cumplimiento de restricciones globales

| Restricción | Cómo se cumplió |
|---|---|
| n.º 1 — sin "CTO"/"Co-founder" | Se usó **Tech Lead** en ambos CVs y en las respuestas |
| n.º 2 — no inventar | Todo sale de `cv.md`, `profile/achievements.md` y el email de Del Mar; nada de AWS/Terraform/K8s inventado |
| n.º 3 — verificabilidad | Sin porcentajes de mejora ni adjetivos sueltos. Única cifra: 15M+ registros Sybase→Oracle (ya validada en CVs anteriores) |
| n.º 4 — PDF por `m2pdf` | Ambos PDFs con `/usr/local/bin/m2pdf` (primer intento falla por FreeSerif y el reintento produce el archivo — comportamiento esperado) |
| n.º 5 — ATS vs Harvard | **Preguntado al usuario**; eligió "Ambos". Se generaron las dos versiones |
| n.º 7 — orden de secciones | Habilidades Técnicas inmediatamente antes de Educación e Idiomas en ambos |
| n.º 8 — bloque Competencias | Cierra Educación e Idiomas, con evidencia entre paréntesis. **Espejado a la lista propia del aviso**: curiosidad activa, ownership, colaboración, analítica (+ capacidad de aprendizaje) en vez de la lista base genérica |

## Keywords espejadas (densidad verificada sobre el PDF ATS)

IaC 5 · respuesta ante incidentes 5 · arquitectura serverless 4 · skills 4 · ciclos de despliegue 3 · detección de tráfico anómalo 3 · gestión de secretos 3 · referente técnico 3 · análisis, automatización y desarrollo 3 · responsable end-to-end 2 · plataformas internas 2 · dueño de la seguridad de la infraestructura 2 · agentes MCPs 2 · gobernanza 2 · sistemas de monitoreo y alertas 2.

## Ajuste de extensión

Ambas versiones se llevaron a **2 páginas exactas** (verificado con `pdfinfo`; extracción lineal verificada con `pdftotext`). El primer borrador salía en 3. Recortes aplicados: fusión de viñetas de observabilidad y costos, condensación de Perficient y Citibank a una viñeta, eliminación del bullet de medios de pago (no aporta al rol cloud), encabezado de 3 a 2 líneas y compactación del bloque de Competencias. En la versión Harvard, además, ajuste de márgenes y `parskip` (capa de presentación, sin tocar contenido).

## Observaciones para el usuario

- **El aviso no publica salario.** Get on Board suele mostrarlo; este no. Conviene preguntar la banda temprano.
- **Nivel del cargo:** "Mid/Sr" con 4–5 años requeridos para un perfil de 15+. Riesgo de banda salarial por debajo del rango objetivo ($1.800.000–$3.000.000 líquidos), igual que ocurrió con ProntoPaga.
- **100% remoto con relación laboral estable** — calza con el filtro de modalidad (vive en Limache).
- **Inglés B1/B2 requerido solo para lectura técnica** — no es excluyente para el perfil.
- **Postulación enviada el 2026-08-28** y registrada en `../proceso` (Restricción n.º 6) con id `2026-08-28-alegra-cloud-engineer-mid-sr`, estado `postulado`. Seguimiento: `./track update "Alegra" --etapa respuesta --nota "..."` cuando conteste la empresa.
