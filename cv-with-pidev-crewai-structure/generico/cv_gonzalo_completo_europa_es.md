---
lang: es
papersize: a4
colorlinks: true
urlcolor: black
linkcolor: black
---

# Gonzalo Oviedo Lambert

**Senior Software Engineer / Tech Lead — Java · Spring Boot · React · Cloud (GCP) · Ingeniería asistida por IA**\
Actual: Limache, Región de Valparaíso (Chile) · Reubicación: **disponible para incorporación inmediata en Madrid, España** (abierto a toda España y a trabajo remoto dentro de la UE)\
+56 9 6372 3603 · goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev\
Español nativo · Inglés B2 (uso diario en equipos de EE. UU., India y Ucrania) · Nacionalidad chilena

## Resumen Profesional

Ingeniero de software con **más de 15 años** construyendo sistemas transaccionales que hoy siguen en producción: **17 años atendiendo requerimientos bancarios para Santander/Isban** (Chile, Puerto Rico, Colombia, Uruguay y Venezuela), migraciones de datos financieros en **Citibank**, el e-commerce global de **Caterpillar** con Perficient, integraciones de alto tráfico para la cadena de farmacias **Salcobrand** y un Sistema de Gestión en Salud que diseñé, desarrollé y operé para un hospital. Desde 2024 soy **Tech Lead y arquitecto de una plataforma de movilidad en producción** (app.tellevoapp.cl) sobre **Java 21, Spring Boot, PostgreSQL y Google Cloud**, con toda la infraestructura escrita como código en **Pulumi**.

Trabajo el ciclo completo: backend **Java/Spring Boot** con arquitecturas por capas y microservicios, frontend **React/TypeScript** y **Flutter**, bases de datos **PostgreSQL y Oracle**, mensajería con **IBM MQ** y **Redis**, **CI/CD** (GitLab CI, Jenkins, GitHub Actions, Azure DevOps) y **Docker**. Desde 2024 desarrollo con **agentes de código (Claude Code)** bajo un proceso de ingeniería con planificación obligatoria y puertas de calidad automatizadas, y tengo **tres aplicaciones de IA en producción**, entre ellas un **RAG con Java 21 y Spring AI** sobre la Ley chilena de Protección de Datos Personales, inspirada en el **RGPD** europeo.

Busco integrarme a un equipo europeo donde el trabajo se comparta y se revise en conjunto: he trabajado tres años en equipos distribuidos **100% en inglés**, lideré técnicamente a 4 desarrolladores y hoy soy el referente de arquitectura, infraestructura y calidad de mi equipo.

## Por qué un equipo en Europa

- **Dominio bancario con un grupo español:** 17 años resolviendo requerimientos de Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito para Santander/Isban en cinco países, además de Citibank. Conozco los ritmos, la exigencia regulatoria y las ventanas de despliegue de un banco.
- **Equipos distribuidos y multiculturales:** tres años consecutivos (2021–2023) trabajando en inglés con EE. UU., Ucrania, India y Latinoamérica, 100% remoto, con stand-ups, code review y documentación en inglés.
- **Datos personales y regulación:** experiencia con historiales clínicos (hospital), datos financieros (banca) y un proyecto público de RAG sobre la Ley 21.719 de protección de datos personales, inspirada en el RGPD.
- **Ingeniería asistida por IA con proceso, no "vibe coding":** flujo spec → plan → ejecución → verificación con Claude Code, openspec y suites de tests como puerta de calidad, con resultados en producción.
- **Movilidad real:** disponible para reubicarme en Madrid con incorporación inmediata. Abierto a contratación local con patrocinio de Tarjeta Azul-UE (perfil TIC), a modalidad contractor B2B o a través de un empleador de registro (EOR).

## Experiencia Profesional

### Tech Lead y Arquitecto — Te Llevo, plataforma de movilidad (Chile) | 2024 – Presente

**Stack:** Java 21 (Spring Boot, Spring AI), Elixir/Phoenix (Ash, LiveView, Jido.AI), React Native, Flutter, PostgreSQL (pgvector), Google Cloud (Cloud Run, Compute Engine, API Gateway, Load Balancer, Cloud Armor WAF, IAM, Secret Manager, Logging/Monitoring, VPC, Google Maps Platform), Pulumi (IaC), Docker, Cloudflare, Transbank y Khipu (pagos), Claude Code (plan Max), MCP, openspec, Git. En producción: app.tellevoapp.cl y www.tellevoapp.cl

**Arquitectura y backend**

- Diseñé y mantengo la arquitectura por capas del backend (REST, Service, DAO) sobre **Spring Boot**, con **PostgreSQL** como base relacional, consultas SQL vía JDBC y una suite de **pruebas unitarias automatizadas** como puerta de calidad antes de cada despliegue.
- Evoluciono la plataforma sobre servicios gestionados (**Cloud Run** y **API Gateway**), reemplazando progresivamente el monolito por servicios con **APIs REST** propias y conservando VMs solo donde el workload lo justifica.
- Integré las **APIs REST** de Google Maps Platform (Directions, Distance Matrix, Geocoding) para el cálculo de rutas y distancias entre pasajeros y conductores, con restricción y rotación de API keys, control de cuotas y monitoreo del costo por request.
- Implementé el sistema de pagos con **Transbank (Webpay)** y **Khipu**, cubriendo los flujos de checkout, confirmación y conciliación de transacciones, en Java y Flutter.
- Construí el sitio público (www.tellevoapp.cl) y el frontend web de la aplicación íntegramente en **Elixir/Phoenix con LiveView**, con la lógica de negocio sobre **Ash Framework**.

**Frontend y móvil**

- Construí la primera versión de la interfaz móvil en **React Native**, consumiendo las mismas APIs REST del backend, y más adelante migré el frontend a **Flutter** (dos aplicaciones móviles) manteniendo el backend sin cambios.

**Infraestructura, seguridad y operación**

- Escribí y mantengo **toda la infraestructura como código en Pulumi** sobre Google Cloud: servicios de Cloud Run, VMs, VPC y firewall, Load Balancer con TLS, políticas de **Cloud Armor (WAF)**, cuentas de servicio con **IAM de menor privilegio** y secretos versionados en Secret Manager. Reconstruir un entorno es ejecutar el stack y revisar el plan de cambios.
- Organicé ese código en componentes reutilizables y stacks por entorno, y automaticé los ciclos de despliegue encadenando builds de imágenes **Docker** y `pulumi up` en el pipeline de **CI/CD**.
- Soy responsable de la seguridad y la observabilidad de la plataforma: detección de tráfico anómalo con Cloud Armor y Cloudflare, gestión de secretos, IAM, monitoreo y alertas con Cloud Logging/Monitoring, y respuesta ante incidentes buscando causa raíz.

**Ingeniería asistida por IA**

- Definí e implanté el flujo de trabajo con agentes de código del equipo sobre **Claude Code**: skills y comandos versionados por tarea, servidores **MCP** propios, planificación obligatoria con **openspec** antes de tocar código, y cierre con tests, linter y cobertura. El resultado depende del proceso, no del prompt del día.
- Integré LLMs de bajo costo en tareas de soporte seleccionando el modelo por tarea y midiendo el costo por petición.
- Colaboro de forma continua con gerencia, área comercial y legal para diseñar arquitecturas de datos seguras y flujos de firma digital de contratos conformes a la regulación de tránsito.

### Desarrollador Java / Integraciones — Salcobrand, cadena de farmacias (Chile) | 2023 – 2024

**Stack:** Java, Spring Boot, APIs REST, Redis, IBM MQ, Docker, Git.

- Desarrollé integraciones para **APIs REST de alto tráfico** de la cadena de farmacias, implementando **Redis** como capa de caché de las APIs de mayor tráfico e **IBM MQ** para comunicación asíncrona con entrega garantizada.
- Trabajé en colaboración directa con los equipos de Infraestructura y DevOps: límites de recursos y health checks de los contenedores, credenciales y variables gestionadas por plataforma, y coordinación de ventanas de despliegue y rollback sobre producción.
- En los incidentes aportaba la vista de aplicación (logs, trazas, consultas lentas) a quienes operaban la infraestructura; el diagnóstico salía de esa conversación.

### Java Associate Developer — Perficient, cliente Caterpillar (100% remoto, en inglés) | 2022 – 2023

**Stack:** Java, Spring Boot, microservicios, APIs REST, SQL, Docker, GitHub, GitLab, Scrum.

- Desarrollé y mantuve las **APIs REST** del e-commerce global de Caterpillar en una **arquitectura de microservicios**, consumidas por varios frentes de la plataforma.
- Trabajé bajo **Scrum** en un equipo distribuido entre EE. UU., India y Latinoamérica: refinamiento de historias de usuario, code review y coordinación técnica diaria en inglés.
- Mis servicios se desplegaban a través de la plataforma interna del equipo de Cloud y Platform de Caterpillar, ajustándome a sus templates, reglas de configuración y controles de seguridad corporativos.

### Java Specialist — Citibank (equipo de EE. UU., Ucrania, India y Chile) | 2021 – 2022

**Stack:** Java, Spring Beans, Oracle SQL y PL/SQL, Jenkins, Gradle, WebSphere, Git, Jira, Confluence, Eclipse.

- Desarrollé soluciones para requerimientos mensuales sobre el framework interno del banco (Java Bean Spring), con **consultas SQL** en Oracle y despliegues automatizados con **Jenkins** en un entorno de rigurosidad de cumplimiento y ventanas acotadas.
- Participé en la migración de bases de datos financieras de **Sybase a Oracle**: más de **15 millones de registros** transferidos sin pérdida de datos, coordinando con equipos de EE. UU., Ucrania, India y Chile.
- Creé y mantuve reportes SQL para clientes internos del banco.

### Tech Lead — Seven IT SpA, Hospital Cruz del Norte (SQM) | 2017 – 2020

**Stack:** Spring Boot (REST, MVC), PostgreSQL 9.6, JavaScript, jQuery, Vuetify, Bootstrap, Linux, Google Cloud (VM), GitLab.

- Dueño, gestor y desarrollador del **Sistema de Gestión en Salud** (medicina, enfermería, kinesiología): analicé los procesos As-Is junto al personal clínico y administrativo y los convertí en módulos en producción, con backend de APIs REST en Spring Boot e interfaz web con componentes reutilizables.
- Construí el módulo transaccional de pagos y la reportería administrativa en PDF, integrados con el resto del sistema vía APIs internas.
- Desplegué y operé el sistema sobre Google Cloud: VMs Linux, PostgreSQL, respaldos, disponibilidad y escalamiento de incidentes.
- Lideré técnicamente a **4 desarrolladores** (frontend y backend) mediante revisión de código en Merge Requests, definición de estándares y principios de código limpio.
- Presentaciones y reuniones con la dirección del hospital y las jefaturas clínicas para definir alcance y prioridades.

### Director y Desarrollador de Ficha Clínica — Hospital Cruz del Norte (SQM) | 2016 – 2017

**Stack:** ExtJs, Java, PostgreSQL.

- Rol integral: jefatura, liderazgo funcional y técnico, análisis, desarrollo, diseño e infraestructura, desde la gerencia hasta la puesta en marcha. Creación de la empresa y jefatura de personal.
- Construí el POS (caja) como interfaz desktop por web con ExtJs, con cálculo de índices personalizados de stock y cargas masivas.

### UX/UI Designer y Full Stack Developer — Nubox Facturación Electrónica | 2014 – 2017

**Stack:** HTML, SASS/CSS, React, jQuery.

- Establecí y supervisé las directrices de interfaz gráfica de la nueva generación de aplicaciones Nubox: estilos, mockups e iconografía, e implementación de las vistas front-end con **React** y componentes reutilizables.
- Desarrollé el nuevo sitio web para Colombia y su reportería contable: reportes de negocio por requerimiento, interacción del sitio y estilo visual.
- Compatibilicé el sitio a nivel país con el navegador Chrome, ampliando la entrada de nuevos usuarios a la plataforma de Facturación Electrónica.

### Analista y Desarrollador — Cencosud S.A., cadena de supermercados | 2015 – 2016

**Stack:** ExtJs, Java, SQL.

- Desarrollé el software web de **gestión de stock** de la cadena: interfaz desktop por web con ExtJs, cálculo de índices personalizados de inventario y cargas masivas.

### Ingeniería de Software — Portal Inmobiliario | 2008 – 2016

**Stack:** Aplicaciones web, SQL Server Reporting Services.

- Desarrollo de aplicaciones web, personalización de documentos y generación de reportes con SQL Server Reporting Services.
- Construí el Seguidor Web, herramienta de gestión y administración para corredores de propiedades.

### Analista de Sistemas Bancarios — Santander / Isban | 2000 – 2017

**Stack:** Java, Struts, JSP, Hibernate, AS/400, PHP, PostgreSQL, Oracle, SQL Server, Jenkins, Jira.

- **17 años en el sector financiero** atendiendo requerimientos de Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito para Chile, Puerto Rico, Colombia, Uruguay y Venezuela.
- Migraciones bancarias de **AS/400 a Java** (Struts, Hibernate), facturación electrónica y gestión de incidentes sobre sistemas transaccionales en producción.
- Levantamiento de requerimientos directamente con las áreas de negocio del banco.

## Proyectos Propios en Producción

### RAG sobre la Ley 21.719 de Protección de Datos Personales — Java 21 + Spring AI

datos-personales.limachelocales.cl · github.com/goviedodev/ley-datos-personales

- Asistente de consulta sobre la ley chilena de protección de datos personales, inspirada en el **RGPD** europeo: ingesta y limpieza de PDF, chunking con TokenTextSplitter (400 tokens), embeddings de 768 dimensiones (nomic-embed-text), búsqueda por similitud coseno (top-8) sobre **PostgreSQL con pgvector**, inyección de contexto en el prompt, generación con qwen3.5 vía **Ollama**, respuesta con streaming token a token y memoria de conversación por sesión.
- Stack: **Java 21, Spring Boot, Spring AI**, PostgreSQL + pgvector, Ollama, Docker. Corre 100% en local, sin enviar datos a servicios externos.

### Automatización para una farmacia local — Elixir/Phoenix + Jido.AI

farma.limachelocales.cl

- Levanté el proceso As-Is con el dueño del negocio y definí con él qué automatizar. Construido con **Jido.AI**, framework de agentes que deja determinista lo que debe serlo y reserva el LLM para donde aporta.

### Aplicación de reporte de turnos — Next.js 14 + NestJS

github.com/goviedodev/niuro

- Aplicación full stack que reemplaza una planilla de operaciones industriales por una app web trazable. Frontend en **Next.js 14 (App Router) con React 18 y TypeScript**: sesión de usuario, formularios controlados con componentes reutilizables y un wrapper fetch tipado que normaliza los errores de validación por campo.
- Backend en **NestJS 10 (Node.js, TypeScript)** con arquitectura por capas, ValidationPipe global y **pruebas unitarias en Jest**; autenticación con **JWT** y dos roles, con la autoría de cada registro tomada del token y nunca del formulario.
- Builds **Docker multi-stage** y el mismo pipeline de **CI/CD** implementado en **GitHub Actions** y **Azure Pipelines**.

### Solución para una zapatería local — Cloudflare Workers

- Construida íntegramente con IA sobre **Cloudflare Workers (JavaScript/TypeScript)** para un cliente sin formación técnica: relevamiento del proceso, propuesta en lenguaje simple y entrega iterativa.

## Cómo Trabajo

- **Ciclo completo de desarrollo:** refinamiento de historias de usuario, diseño, implementación, pruebas unitarias y de integración, code review en Pull/Merge Requests, despliegue y operación.
- **Metodologías ágiles:** Scrum en Perficient–Caterpillar; Extreme Programming (XP) desde la tesis universitaria; Git con gitflow y pull requests; Jira y Confluence.
- **Calidad como proceso:** suite de tests automatizados como puerta de calidad antes de cada despliegue, linter y cobertura en el pipeline; principios de código limpio y patrones de diseño aplicados en code review.
- **IA como herramienta de ingeniería:** generación de código mayoritariamente con Claude Code, apoyado en harnesses propios (axi, openspec y una estructura de carpetas al estilo Jake Van Cliff) para mantener trazabilidad y calidad de ingeniería en cada cambio. Experiencia previa con Pi.dev y opencode.
- **Comunicación con negocio:** definición de alcance con la dirección de un hospital y sus jefaturas clínicas, con gerencia, área comercial y legal de una startup, y con dueños de comercios locales sin formación técnica.

## Habilidades Técnicas

- **Lenguajes:** Java (8 – 21), SQL, JavaScript (ES6+), TypeScript, Elixir, Dart, Bash, PHP; Python a nivel funcional (scripts y automatización).
- **Backend Java:** Spring Boot (REST, MVC, Data JPA, Beans), Spring AI, Hibernate, Struts, arquitecturas por capas (Controller/REST, Service, DAO), microservicios, diseño de APIs REST, JDBC y consultas SQL, GraalVM, principios SOLID y código limpio, patrones de diseño.
- **Backend Elixir y Node.js:** Phoenix, Phoenix LiveView, Ash Framework, Jido.AI, OTP; NestJS (Node.js, TypeScript), Cloudflare Workers.
- **Frontend y móvil:** React 18, Next.js 14, TypeScript, React Native, Flutter, Vue.js/Nuxt, Vuetify, Bootstrap, jQuery, ExtJs, HTML5, SASS/CSS3, componentes reutilizables, PWA.
- **Bases de datos:** PostgreSQL (incluido pgvector), Oracle (PL/SQL), MySQL, SQL Server (Reporting Services), Sybase, MongoDB, Redis; modelado, optimización de consultas y migraciones de gran escala.
- **Mensajería y caché:** IBM MQ (mensajería asíncrona con entrega garantizada), Redis (caché de APIs de alto tráfico).
- **Cloud e infraestructura:** Google Cloud Platform (Cloud Run, Compute Engine, API Gateway, Load Balancer y TLS, Cloud Armor WAF, IAM, Secret Manager, Cloud Logging/Monitoring, VPC, Google Maps Platform), Pulumi (IaC con componentes reutilizables y stacks por entorno), Docker (builds multi-stage), Cloudflare (WAF, DNS, Workers), Linux; AWS (Lambda, S3) y Azure DevOps en uso puntual.
- **CI/CD y control de versiones:** GitLab CI/CD, Jenkins, GitHub Actions, Azure Pipelines, Git (gitflow, pull requests, code review).
- **Testing y calidad:** JUnit, Mockito, Jest, ExUnit, pruebas unitarias y de integración, Playwright MCP, Swagger/OpenAPI, TDD, Spec Driven Development.
- **Seguridad:** JWT y gestión de sesiones, buenas prácticas OWASP, IAM de menor privilegio, gestión de secretos, WAF (Cloud Armor, Cloudflare), detección de tráfico anómalo, respuesta ante incidentes.
- **IA aplicada al desarrollo y a producto:** Claude Code (plan Max, uso diario desde 2024) con skills, comandos, workflows y servidores MCP propios; openspec y axi; RAG (embeddings, pgvector, chunking, inyección de contexto, streaming, memoria de conversación); Spring AI, Ollama, Jido.AI; diseño de prompts; selección de modelo por costo; experiencia previa con Pi.dev y opencode.
- **Pagos e integraciones:** Transbank (Webpay), Khipu, Google Maps Platform, facturación electrónica.
- **Metodologías y gestión:** Scrum, Kanban, Extreme Programming (XP), refinamiento de historias de usuario, Jira, Confluence, liderazgo técnico y mentoría.
- **Exploración tecnológica:** Blockchain (Solidity, Internet Computer / ICP), sistemas de alta concurrencia sobre la BEAM (Elixir).

## Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción, Chile (titulación universitaria completa, 2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica.

**Formación continua (autodidacta, con resultados en producción):** progresión de Java 8 a Java 21; Elixir/Phoenix, Ash Framework y Jido.AI; Spring AI y bases de datos vectoriales (pgvector); Pulumi (IaC) y Google Cloud; React 18, Next.js 14 y NestJS; Flutter; Cloudflare Workers; Claude Code, MCP y openspec.

**Idiomas:** Español nativo. **Inglés B2**, en uso continuo desde 2021: stand-ups, code review, documentación técnica y reuniones con equipos de EE. UU., Ucrania e India (Citibank 2021–2022, Perficient–Caterpillar 2022–2023).

**Movilidad y contratación:** disponible para reubicación inmediata en Madrid (o cualquier ciudad de España) y para trabajo remoto dentro de la UE. Abierto a contrato local con patrocinio de Tarjeta Azul-UE (perfil TIC), a contractor B2B con facturación de exportación de servicios o a contratación vía empleador de registro (EOR).

**Competencias:** **Comunicación asertiva y trabajo en equipo** (code review y definición de estándares liderando 4 desarrolladores en Seven IT; colaboración constante con el equipo de la plataforma de movilidad). **Pensamiento analítico y resolución de problemas** (diseño de la arquitectura por capas de la plataforma de movilidad, en producción desde 2024; migración de 15 millones de registros de Sybase a Oracle sin pérdida de datos). **Orientación a resultados, planificación y organización** (dos proyectos llevados de punta a punta: la plataforma de movilidad y el Sistema de Gestión en Salud de Seven IT). **Innovación y mejora continua** (adopción de Claude Code, MCP, Spring AI y Jido.AI por experimentación propia, con tres aplicaciones de IA en línea). **Capacidad de aprendizaje** (de Java 8 a 21, y de ahí a React/TypeScript, Elixir/Phoenix e infraestructura como código). **Orientación al cliente** (refinamiento de historias de usuario antes de implementar en Perficient–Caterpillar; relevamiento directo con la dirección de un hospital y con dueños de comercios locales). **Capacidad para trabajar en ambientes dinámicos y de alta colaboración** (equipos multiculturales en Perficient/Caterpillar y Citibank: EE. UU., India, Ucrania y Latinoamérica).
