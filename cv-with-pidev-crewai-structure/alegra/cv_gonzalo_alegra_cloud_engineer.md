# Gonzalo Oviedo Lambert

**Cloud Engineer (Mid/Sr) — 100% remoto**
Limache, Región de Valparaíso, Chile · GMT-4 · +56 9 6372 3603 · goviedo.laboral@gmail.com
linkedin.com/in/gol · github.com/goviedodev · Español nativo · Inglés B2

## Resumen Profesional

Ingeniero con más de 15 años en software y, desde 2024, **responsable end-to-end de mejorar, optimizar y monitorear la infraestructura** de una plataforma en producción, asegurando además **las plataformas internas que usa el equipo de desarrollo para moverse rápido y sin fricción**. Escribo la infraestructura completa como código con **Pulumi (IaC) sobre Google Cloud** —Cloud Run, VMs, red, balanceo, IAM y secretos— y **automatizo los ciclos de despliegue para acelerar la entrega de software**. Antes, desde el desarrollo, trabajé **junto a los equipos de Infraestructura, Cloud, DevOps y Platform** de Salcobrand, Perficient y Caterpillar. Uso **IA integrada a mi flujo real de trabajo —agentes, MCPs y skills— en análisis, automatización y desarrollo**, con resultados en producción.

## Experiencia Profesional

### Tech Lead (Cloud & Platform) — Te Llevo, plataforma de movilidad (Chile) | 2024 – Presente

**Stack:** Google Cloud (Cloud Run, Compute Engine/VMs, API Gateway, Load Balancer, Cloud Armor WAF, IAM, Secret Manager, Logging/Monitoring, VPC, Google Maps Platform), **Pulumi (IaC)**, Docker, CI/CD, Java 21 (Spring Boot), Elixir/Phoenix, PostgreSQL, Linux, Cloudflare. En vivo: app.tellevoapp.cl

- **Infraestructura como código con Pulumi:** escribí y mantengo **toda la infraestructura en Pulumi** —servicios de **Cloud Run**, **VMs** de Compute Engine, VPC y firewall, Load Balancer con TLS, políticas de **Cloud Armor (WAF)**, cuentas de servicio con **IAM** de menor privilegio y secretos versionados fuera del repositorio—. Reconstruir un entorno es ejecutar el stack y revisar el plan de cambios, no seguir pasos manuales en la consola.
- Organicé ese código en **componentes reutilizables y stacks por entorno**, para que un servicio nuevo herede red, permisos, logging y estándares ya aplicados sin depender de mí, y **automaticé los ciclos de despliegue** encadenando build de imágenes **Docker** y `pulumi up` en el pipeline.
- **Arquitectura serverless:** diseñé y evoluciono la plataforma sobre servicios gestionados —**Cloud Run** y **API Gateway**, los equivalentes de Lambda y API Gateway—, **reemplazando progresivamente el monolito** por servicios con **APIs REST** propias y conservando **VMs** solo donde el workload lo justifica.
- **Costos:** integré y opero **Google Maps Platform** (rutas, geocodificación, mapas) como dependencia crítica: restricción y rotación de API keys, control de cuotas y **monitoreo continuo del costo por request**. **Monitoreo costos de forma continua** y soy **referente técnico** del equipo en el **uso óptimo de la nube** (dimensionamiento de Cloud Run, escalado a cero, facturación por servicio).
- **Seguridad y observabilidad:** soy **dueño de la seguridad de la infraestructura** —**detección de tráfico anómalo** con Cloud Armor y Cloudflare, **gestión de secretos**, **IAM** y **respuesta ante incidentes**—; mantengo **monitoreo y alertas** (Cloud Logging/Monitoring, el equivalente de CloudWatch) **con foco en detección proactiva, no reactiva**, busco **causa raíz y prevención, no parches**, y **audito las políticas de gobernanza como código**, **no solo en el papel**.
- **IA en el día a día:** construí mi harness sobre **Claude Code (plan Max)** con **skills, comandos, workflows y MCPs** propios y lo uso **en análisis, automatización y desarrollo**; con **openspec** (antes Firstmate) el trabajo pasa obligatoriamente por planificación antes de tocar código, y cierra con tests, linter y cobertura. Con el mismo enfoque puse en línea **farma.limachelocales.cl** (Elixir/Phoenix con **Jido.AI**, framework de agentes que deja el algoritmo determinista y reserva la IA para donde aporta), **datos-personales.limachelocales.cl** (**RAG** con **Java 21 y Spring AI** sobre base vectorial) y una solución para una zapatería local sobre **Cloudflare**.

### Desarrollador Java / Integraciones — Salcobrand (cadena de farmacias) | 2023 – 2024

- **Colaboración directa con los equipos de Infraestructura y DevOps** en APIs de alto tráfico: límites de recursos y health checks de los contenedores, credenciales y variables gestionadas por plataforma, y coordinación de ventanas de despliegue y rollback sobre producción.
- Implementé **Redis** como caché de las APIs de mayor tráfico e **IBM MQ** para comunicación asíncrona con entrega garantizada — infraestructura compartida cuya capacidad, colas y alertas se dimensionaron junto al equipo de operaciones. En los incidentes aportaba la vista de aplicación (logs, trazas, consultas lentas) a quienes operaban la infraestructura.

### Java Associate Developer — Perficient (cliente: Caterpillar) | 2022 – 2023

- Desarrollé y mantuve las **APIs REST** del e-commerce global de Caterpillar en una **arquitectura de microservicios** (Java 21, Spring Boot, Scrum), con un equipo distribuido entre EE. UU., India y Latinoamérica, 100% remoto y asíncrono.
- **Trabajé contra el equipo de Cloud y Platform de Caterpillar**, dueño de los pipelines, ambientes y estándares corporativos: mis servicios se desplegaban por su plataforma interna, ajustándome a sus templates y controles de seguridad. Fui el "equipo de desarrollo" al que una plataforma interna debe permitirle **moverse rápido y sin fricción**, y sé cuándo esa plataforma ayuda y cuándo estorba.

### Java Specialist — Citibank | 2021 – 2022

- **Automaticé ciclos de despliegue** con **Jenkins** (Java, Oracle SQL, Websphere, Gradle) en un entorno bancario con **rigurosidad de cumplimiento de seguridad** y **respuesta ante incidentes** en ventanas acotadas. Lideré la migración de bases financieras de Sybase a Oracle: más de 15 millones de registros, sin pérdida de datos, con equipos de EE. UU., Ucrania, India y Chile.

### Tech Lead — Seven IT SpA (Hospital Cruz del Norte, SQM) | 2017 – 2020

- Diseñé, desplegué y **operé sobre Google Cloud** el Sistema de Gestión en Salud usado a diario por personal clínico: **VMs** Linux, PostgreSQL, respaldos, disponibilidad y escalamiento de incidentes. Referente técnico de 4 desarrolladores y de los estándares aplicados en cada Merge Request.

### Analista de Sistemas Bancarios y roles previos — Santander/Isban, Cencosud, Portal Inmobiliario, Nubox | 2000 – 2017

- 17 años en el sector financiero (Préstamos, Medios de Pago, Cuentas Corrientes, Tarjetas de Crédito) para Chile, Puerto Rico, Colombia, Uruguay y Venezuela, con **respuesta ante incidentes** sobre sistemas transaccionales y migraciones de plataforma (AS/400 a Java).

## Habilidades Técnicas

- **IaC y automatización:** **Pulumi** (componentes reutilizables, stacks por entorno, estado versionado), **despliegues con Docker**, CI/CD (GitLab CI, Jenkins, Azure DevOps) y **GitHub Actions** con builds multi-stage (github.com/goviedodev/niuro).
- **Cloud (GCP como nube productiva):** Cloud Run, Compute Engine (VMs), API Gateway, Load Balancer y TLS, VPC y firewall, IAM, Secret Manager, Cloud Logging/Monitoring, Cloud Armor (WAF), Google Maps Platform; Cloudflare (WAF, DNS, Workers). **Diseño de APIs REST y arquitecturas de microservicios**, migración de monolito a servicios gestionados.
- **Seguridad, observabilidad y costos:** **detección de tráfico anómalo**, **gestión de secretos**, **IAM** de menor privilegio, **respuesta ante incidentes**, **gobernanza como código**, **sistemas de monitoreo y alertas** con **detección proactiva, no reactiva**, **causa raíz y prevención**, **monitoreo de costos de forma continua**.
- **Motores SQL y NoSQL y lenguajes:** PostgreSQL, Oracle, MySQL, SQL Server, MongoDB, Redis, IBM MQ; Java (1.8 – 21, Spring Boot, Spring AI), SQL, JavaScript/TypeScript, Elixir (Phoenix, Ash, Jido.AI), Flutter.
- **IA integrada al flujo real de trabajo:** **agentes, MCPs y skills** propios sobre Claude Code (plan Max), planificación obligatoria con openspec y puertas de calidad con tests, linter y cobertura; antes Pi.dev y opencode.
- **Equivalencias declaradas:** mi nube productiva es **GCP**, no AWS (en AWS he usado Lambda y S3, no una arquitectura serverless completa); mi IaC es **Pulumi**, no Terraform; mi monitoreo es Cloud Logging/Monitoring, no CloudWatch ni Grafana. Los conceptos son los mismos.

## Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica. Español nativo; **inglés B2 para lectura técnica, documentación y tutoriales**, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania.

**Competencias:** **curiosidad activa** (Jido.AI con Elixir/Phoenix y Spring AI adoptados por experimentación propia, ambos en línea); **ownership** (responsable end-to-end de la infraestructura de Te Llevo, escrita íntegramente en Pulumi); **colaboración** (trabajo con los equipos de Infraestructura, Cloud, DevOps y Platform de Salcobrand, Perficient y Caterpillar, remotos y multiculturales); **analítica** (15 millones de registros migrados de Sybase a Oracle sin pérdida de datos); **capacidad de aprendizaje** (de Java 8 a 21, y de ahí a Elixir/Phoenix e IaC en Pulumi).
