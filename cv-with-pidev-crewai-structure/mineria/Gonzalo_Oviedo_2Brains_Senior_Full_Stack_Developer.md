Gonzalo Oviedo Lambert

Senior Full Stack Developer — React/Next.js/NestJS (Minería)

Limache, Región de Valparaíso, Chile — disponible para modalidad remota o híbrida en Santiago
goviedo.laboral@gmail.com | +56 9 6372 3603
linkedin.com/in/gol | github.com/goviedodev
Producto en producción: app.tellevoapp.cl
Español nativo | Inglés B2

## Resumen Profesional

Full-stack developer con 15+ años construyendo aplicaciones completas de punta a punta — backend, frontend, base de datos e infraestructura — en más de un stack (Java/Spring Boot, PHP, Elixir/Phoenix, Node.js/TypeScript). Hoy diseño y opero la arquitectura completa de una plataforma de movilidad en producción, y construí una aplicación de reporte operacional en Next.js 14 + NestJS. A esta altura de la carrera, la brecha técnica entre una tecnología u otra ya no es la variable que decide un proyecto: la resuelve haber construido de cero, más de una vez y en más de un lenguaje, sistemas completos que siguen en producción — incluido un sistema de gestión clínica para una operación minera y química (SQM).

## Habilidades Técnicas

- **Backend y lenguajes:** Node.js/TypeScript (NestJS), Java (Spring Boot, Struts), PHP, SQL.
- **Frontend:** Next.js (App Router), React 18, TypeScript, JavaScript (ES6+), Vue.js/Nuxt, Flutter.
- **Datos e integraciones:** PostgreSQL, Oracle PL/SQL, MySQL, SQL Server — modelado de esquemas, consultas y migraciones de gran volumen; exportación de datos a un data lake de Databricks vía Files API (Unity Catalog Volumes).
- **Autenticación y control de accesos:** JWT, autorización basada en roles, control de acceso por token (no por payload del formulario).
- **Cloud, Docker y CI/CD:** Google Cloud (Cloud Run), Docker (builds multi-stage), Pulumi (Infraestructura como Código), Git, GitHub Actions, Azure Pipelines (Azure DevOps), Jenkins, GitLab CI.
- **Testing e IA aplicada al desarrollo:** Jest, JUnit, Mockito, pruebas unitarias e integración; Claude Code (plan Max) como herramienta de IA principal en desarrollo, testing y documentación.

## Proyecto Público Destacado

**Aplicación de reporte de turnos — Next.js 14 + NestJS** — [github.com/goviedodev/niuro](https://github.com/goviedodev/niuro)

Aplicación full-stack que diseñé y construí para reemplazar una planilla de operaciones industriales (incidentes de turno, detenciones, observaciones de seguridad) por una app web estructurada, trazable y con exportación a un data lake — el mismo tipo de problema que un visualizador de indicadores de condición y riesgo de activos, aplicado a otro dominio operacional.

- Frontend en Next.js 14 (App Router) con React 18 y TypeScript: sesión de usuario, formularios controlados y un wrapper `fetch` tipado que adjunta el token y normaliza los errores de validación por campo.
- Backend en NestJS 10 + TypeScript, arquitectura por capas, `ValidationPipe` global y pruebas unitarias en Jest.
- Autenticación y autorización con JWT (HS256) y dos roles (operador, supervisor); la autoría de cada registro se toma del token, nunca del formulario.
- Exportación de datos al lake en formato JSONL a través de la Databricks Files API (Unity Catalog Volumes).
- Builds Docker multi-stage y el mismo pipeline de CI/CD implementado en GitHub Actions y Azure Pipelines.

## Experiencia Profesional

**Tech Lead** | *Startup de Movilidad — Chile* | 2024 – Presente
Stack: Elixir (Phoenix, Ash), Java 21 (Spring Boot), TypeScript, Flutter, PostgreSQL, Google Cloud, Pulumi IaC, Docker, Git, Claude Code.

- Diseño y mantengo la arquitectura completa de la plataforma (backend, base de datos, infraestructura), en producción con usuarios reales desde 2024.
- Integré APIs de terceros (Google Maps: Directions, Distance Matrix, Geocoding) para resolver el cálculo de rutas y distancias entre pasajeros y conductores.
- Automaticé el despliegue de infraestructura en Google Cloud con Pulumi (IaC) sobre contenedores Docker, sin pasos manuales.
- Definí el flujo de trabajo del equipo con agentes de código (Claude Code): spec, plan, ejecución y verificación, con la suite de pruebas automatizadas como puerta de calidad antes de cada despliegue.

**Java Associate Developer** | *Perficient — Caterpillar* | 2022 – 2023
Stack: Java 21, Spring Boot, APIs REST, equipo ágil distribuido.

- Desarrollo y mantenimiento de servicios backend para la plataforma de e-commerce global de Caterpillar, en equipo Scrum distribuido entre EE. UU., India y Latinoamérica.

**Java Specialist** | *Citibank* | 2021 – 2022
Stack: Java, Oracle PL/SQL, Spring Beans, Jenkins, Gradle, WebSphere, Git.

- Migré la base de datos de reportería de Sybase a Oracle — más de 15 millones de registros financieros, sin pérdida de datos — junto a equipos de EE. UU., Ucrania, India y Chile bajo un proceso regulatorio estricto.
- Desarrollo y mantención de reportería recurrente para clientes internos del banco sobre el framework interno basado en Spring.

**Tech Lead** | *Seven IT SpA — Hospital Cruz del Norte (SQM)* | 2017 – 2020
Stack: Spring Boot (REST, MVC), PostgreSQL 9.6, JavaScript, jQuery, Vuetify, Google Cloud (VM), Linux, GitLab.

- Diseñé, construí y operé de punta a punta el Sistema de Gestión en Salud (medicina, enfermería, kinesiología) para una clínica que atiende a la operación minera y química de SQM: backend REST, interfaz web y esquema PostgreSQL.
- Construí el módulo de gestión de pagos y la reportería administrativa en PDF, integrados con el resto del sistema.
- Lideré técnicamente a un equipo de 4 desarrolladores (front y backend) mediante revisión de código y definición de estándares.

**Java / Senior Developer** | *WebClass, Creasys, Coopeuch y otros* | 2008 – 2017
Stack: Java, AS/400, Struts, JSP, Hibernate, PHP, PostgreSQL, Oracle, SQL Server, Jenkins, Jira.

- Desarrollo full-cycle: análisis de requerimientos, diseño, desarrollo y QA para banca, ed-tech y empresa.
- Migración de procesos bancarios de AS/400 a Java para Santander, Ripley y Coopeuch, sin detener la operación.
- Facturación electrónica e integraciones SOAP/REST entre aplicaciones Java/PHP y sistemas de terceros.

## Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica.

Español nativo. Inglés B2, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania.

## Notas honestas para esta vacante (léase antes de la entrevista)

- **Microsoft Entra ID (OAuth2/OIDC):** sin experiencia productiva específica con Entra ID. La experiencia real de autenticación/autorización es JWT + control de acceso basado en roles (proyecto niuro, plataforma de movilidad).
- **Azure Key Vault:** sin experiencia productiva. Sí uso Azure Pipelines (Azure DevOps) para CI/CD.
- **4+ años en el stack NestJS/Next.js específicamente:** el respaldo real de ese stack es el proyecto público niuro (NestJS 10 + Next.js 14), no un rol laboral remunerado de 4+ años en ese stack puntual. Los 15+ años de experiencia full-stack de punta a punta sí son reales y verificables en los roles listados arriba, en otros lenguajes.
- **Databricks:** experiencia real pero acotada al lado de escritura — exportación de datos al lake vía Files API (Unity Catalog Volumes) en niuro, no lectura/consulta de datos ya integrados en dashboards de Databricks.
