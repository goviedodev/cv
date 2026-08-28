---
lang: es
colorlinks: true
urlcolor: black
linkcolor: black
header-includes: |
  ```{=latex}
  \usepackage{titlesec}
  \usepackage{enumitem}
  \usepackage{fancyhdr}
  \geometry{top=1.3cm,bottom=1.4cm,left=1.7cm,right=1.7cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.8em}{0.45em}
  \setlist[itemize]{leftmargin=1.1em,itemsep=1pt,topsep=2pt,parsep=0pt,label=\textbullet}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{0.28em}
  \linespread{1.0}
  \raggedbottom
  \newcommand{\rol}[2]{\textbf{#1}\hfill\textbf{#2}\par\vspace{-0.4em}}
  \newcommand{\org}[1]{\textit{#1}\par\vspace{-0.3em}}
  \newcommand{\stack}[1]{{\small\textit{Stack:} #1}\par\vspace{-0.2em}}
  \newcommand{\pilar}[1]{\vspace{0.25em}{\small\textbf{#1}}\par\vspace{-0.35em}}
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad Página \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Cloud Engineer (Mid/Sr)}\\[6pt]
{\small Limache, Región de Valparaíso · trabajo 100\% remoto (GMT-4) · +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev · Español nativo · Inglés B2}
\end{center}
\vspace{0.3em}

# Resumen Profesional

Ingeniero con más de 15 años en software y, desde 2024, **responsable end-to-end de mejorar, optimizar y monitorear la infraestructura** de una plataforma en producción, asegurando además las plataformas internas que usa el equipo de desarrollo **para moverse rápido y sin fricción**. Diseño y evoluciono **arquitecturas serverless** para ir **reemplazando el monolito**; **automatizo ciclos de despliegue con IaC** y pipelines **para acelerar la entrega de software**; soy **dueño de la seguridad de la infraestructura** —detección de tráfico anómalo, gestión de secretos, IAM y respuesta ante incidentes— y mantengo **monitoreo y alertas con foco en detección proactiva, no reactiva**, más el **monitoreo continuo de costos**. Uso **IA integrada a mi flujo real de trabajo —agentes, MCPs y skills— en análisis, automatización y desarrollo**.

**Transparencia de stack** (el aviso admite "o sus equivalentes"): mi nube productiva es Google Cloud, no AWS —en AWS he usado Lambda y S3, no una arquitectura serverless completa—; mi IaC es Pulumi, no Terraform; mi monitoreo es Cloud Logging/Monitoring, no CloudWatch ni Grafana.

# Experiencia Profesional

\rol{Tech Lead (Cloud \& Platform)}{2024 – Presente}
\org{Plataforma de Movilidad (startup) — Chile}
\stack{Google Cloud (Cloud Run, API Gateway, Load Balancer, Cloud Armor WAF, IAM, Secret Manager, Logging/Monitoring, VPC), Pulumi (IaC), Docker, GitLab CI/CD, Java 21 (Spring Boot), PostgreSQL, Linux, Claude Code con MCPs y skills.}

\pilar{Arquitectura serverless y automatización}

- Diseñé y evoluciono la **arquitectura serverless** de la plataforma sobre servicios gestionados (Cloud Run y API Gateway, equivalentes de Lambda y API Gateway), **reemplazando progresivamente el monolito** por microservicios con **APIs REST** que diseñé.
- **Automaticé los ciclos de despliegue con IaC** (Pulumi) y pipelines de CI/CD con **despliegues con Docker**, **para acelerar la entrega de software**: escribí la infraestructura completa —cómputo, red, balanceo, firewall, IAM y secretos— como **código reutilizable** versionado en Git, de modo que levantar un entorno nuevo no dependa de mí ni de configuración manual en consola.
- **Desplegué automatizaciones basadas en agentes de IA para optimizar procesos internos y eliminar tareas manuales** del ciclo de desarrollo y operación.

\pilar{Seguridad cloud y platform engineering}

- Soy **dueño de la seguridad de la infraestructura**: **detección de tráfico anómalo** con WAF (Cloud Armor), **gestión de secretos** (Secret Manager), **IAM** de menor privilegio y **respuesta ante incidentes**.
- Construí y mantengo **las plataformas internas que usa el equipo de desarrollo** —pipelines de CI/CD, entornos reproducibles y estándares ya aplicados— para que desplieguen **sin fricción**.
- **Implemento y audito las políticas** de acceso y **gobernanza como código**, versionadas y revisables, **no solo en el papel**.

\pilar{Observabilidad, confiabilidad y costos}

- Mantengo los **sistemas de monitoreo y alertas** (Cloud Logging/Monitoring, el equivalente de CloudWatch) **con foco en detección proactiva, no reactiva**: me entero de los problemas antes que los usuarios.
- Resuelvo incidentes buscando **causa raíz y prevención, no parches**, y **monitoreo costos de forma continua** actuando como **referente técnico** del equipo en el **uso óptimo** de la nube.

\pilar{IA en el día a día}

- Uso **IA integrada a mi flujo real de trabajo**: construí mi propio harness sobre Claude Code (plan Max) con **skills**, comandos y workflows propios, más **MCPs** para conectar herramientas externas, y lo aplico **en tareas de análisis, automatización y desarrollo**. Antes, el mismo enfoque con Pi.dev y opencode.

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient — cliente: Caterpillar}

- Desarrollé y mantuve las **APIs REST** del e-commerce global de Caterpillar dentro de una **arquitectura de microservicios** (Java 21, Spring Boot, Git, Scrum), con un equipo repartido entre EE. UU., India y Latinoamérica.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}

- **Automaticé ciclos de despliegue** con **Jenkins** (Java, Oracle SQL, Websphere, Gradle) en un entorno bancario con **rigurosidad de cumplimiento de seguridad**, atendiendo requerimientos productivos y **respuesta ante incidentes** bajo ventanas acotadas.
- Lideré técnicamente la migración de bases de datos financieras de Sybase a Oracle: más de 15 millones de registros, sin pérdida de datos, con equipos de EE. UU., Ucrania, India y Chile.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}

- Diseñé, desplegué y **operé en Google Cloud** el Sistema de Gestión en Salud usado a diario por personal clínico: servidores Linux, PostgreSQL, respaldos y disponibilidad del servicio.
- Punto de escalamiento ante incidentes de producción (**causa raíz y prevención**) y referente técnico de 4 desarrolladores, definiendo **los estándares** que aplicaban en cada Merge Request de GitLab.

\rol{Analista de Sistemas Bancarios y roles previos}{2000 – 2017}
\org{Santander/Isban, Cencosud, Portal Inmobiliario, Nubox Facturación Electrónica}

- 17 años en el sector financiero (Préstamos, Medios de Pago, Cuentas Corrientes, Tarjetas de Crédito) para Chile, Puerto Rico, Colombia, Uruguay y Venezuela, con **respuesta ante incidentes** sobre sistemas transaccionales en producción.

# Habilidades Técnicas

- **Arquitectura serverless y automatización:** servicios gestionados y contenedores (Cloud Run, API Gateway), **diseño de APIs REST y arquitecturas de microservicios**, migración de monolito a servicios, servicios event-driven, **IaC** (Pulumi) reutilizable, GitLab CI/CD, Jenkins, Azure DevOps, **despliegues con Docker**, y **GitHub Actions** con builds Docker multi-stage en mi proyecto público [github.com/goviedodev/niuro](https://github.com/goviedodev/niuro).
- **Seguridad cloud y platform engineering:** **detección de tráfico anómalo** (WAF), **gestión de secretos**, **IAM** y menor privilegio, **respuesta ante incidentes**, políticas de **gobernanza como código**, plataformas internas y estándares para equipos de desarrollo, TLS/Load Balancer, VPC/firewall.
- **Observabilidad, confiabilidad y costos:** **sistemas de monitoreo y alertas** con **detección proactiva, no reactiva**, logging centralizado, **causa raíz y prevención**, **monitoreo de costos de forma continua**.
- **Motores SQL y NoSQL y lenguajes:** PostgreSQL, Oracle, MySQL, SQL Server, MongoDB; Java (1.8 – 21, Spring Boot), SQL, JavaScript/TypeScript, Elixir.
- **IA integrada al flujo real de trabajo:** **agentes, MCPs y skills** propios sobre Claude Code (plan Max) **en tareas de análisis, automatización y desarrollo**; antes Pi.dev y opencode.

# Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica. Español nativo; **inglés B2 para lectura técnica, documentación y tutoriales**, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania.

**Competencias:** **curiosidad activa** (agentes de IA y Elixir/Ash adoptados por experimentación propia); **ownership** (responsable end-to-end de la infraestructura de la plataforma de movilidad); **colaboración** (referente técnico de 4 desarrolladores vía code review en equipos remotos); **analítica** (errores complejos con enfoque estructurado: 15 millones de registros migrados de Sybase a Oracle sin pérdida de datos).
