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
  \geometry{top=1.4cm,bottom=1.6cm,left=1.8cm,right=1.8cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.85em}{0.5em}
  \setlist[itemize]{leftmargin=1.1em,itemsep=1pt,topsep=2pt,parsep=0pt,label=\textbullet}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{0.35em}
  \linespread{1.0}
  \raggedbottom
  \newcommand{\rol}[2]{\textbf{#1}\hfill\textbf{#2}\par\vspace{-0.4em}}
  \newcommand{\org}[1]{\textit{#1}\par\vspace{-0.3em}}
  \newcommand{\stack}[1]{{\small\textit{Stack:} #1}\par\vspace{-0.2em}}
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad Página \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Fullstack Developer (Java + React)}\\[6pt]
{\small Limache, Región de Valparaíso (Chile) · Reubicación: Madrid, España · +56 9 6372 3603 · goviedo.laboral@gmail.com}\\[2pt]
{\small linkedin.com/in/gol · github.com/goviedodev · Español nativo · Inglés B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Fullstack Developer con más de 15 años de experiencia en **Java 11 y versiones superiores** (8 a 21) y **Spring Boot**, y con frameworks de frontend —**React** desde 2014, con proyectos recientes en React 18— en aplicaciones web con **interfaces REST** y **arquitecturas por capas (REST, Service, DAO)**. Trabajo a diario con **bases de datos relacionales** (PostgreSQL, Oracle) vía **JDBC y consultas SQL**, con **testing unitario** (JUnit, Jest) como puerta de calidad antes de cada despliegue, **Git** bajo **gitflow y pull requests**, entornos **CI/CD** (Jenkins, GitLab CI, Azure DevOps) y **metodologías Agile**. Experiencia con mensajería asíncrona (IBM MQ) en integraciones de alto tráfico. Inglés B2, por sobre el B1 requerido.

# Habilidades Técnicas

- **Backend:** Java (8 – 21, incluye Java 11 y superior), Spring Boot (REST, MVC), arquitecturas por capas (Controller/REST, Service, DAO), diseño de APIs REST, principios de código limpio, patrones de diseño.
- **Frontend:** React 18, TypeScript, JavaScript (ES6+), React Native, Vue.js/Nuxt, componentes reutilizables, HTML/CSS.
- **Bases de datos:** PostgreSQL, Oracle PL/SQL (JDBC, consultas SQL), MySQL, SQL Server (relacionales); MongoDB, Redis (NoSQL / caché).
- **Mensajería:** IBM MQ (mensajería asíncrona en integraciones de alto tráfico).
- **Testing y control de versiones:** JUnit, Jest, pruebas unitarias, Git (gitflow, pull requests), code review.
- **CI/CD y cloud:** Jenkins, GitLab CI/CD, GitHub Actions, Azure DevOps, Docker, Google Cloud Platform, Pulumi (IaC).
- **Metodologías:** Agile/Scrum, refinamiento de historias de usuario.
- **IA aplicada al desarrollo:** Claude Code (plan Max) como harness principal de desarrollo; experiencia previa con Pi.dev y opencode.

# Experiencia Profesional

\rol{Tech Lead y Arquitecto — Plataforma de movilidad}{2024 – Presente}
\org{Chile — en producción: app.tellevoapp.cl}
\stack{Java 21 (Spring Boot), React Native, Flutter, PostgreSQL, Google Cloud, Pulumi IaC, Docker, Git.}

- Diseño y mantengo la arquitectura por capas del backend (**REST, Service, DAO**) sobre **Spring Boot**, con **PostgreSQL** como base de datos relacional y consultas **SQL** vía JDBC.
- Construí la primera versión de la interfaz móvil en **React Native**, consumiendo las mismas **APIs REST** del backend, y más adelante migré el frontend a Flutter manteniendo el backend sin cambios.
- Integré **APIs REST** de servicios externos (Google Maps: Directions, Distance Matrix, Geocoding) para el cálculo de rutas entre pasajeros y conductores.
- Trabajo con **Git** (gitflow, pull requests) y definí el flujo de **CI/CD** del equipo: spec, plan, ejecución y verificación, con la suite de **pruebas unitarias automatizadas** como puerta de calidad antes de cada despliegue.

**Proyecto público — Next.js 14 + NestJS** ([github.com/goviedodev/niuro](https://github.com/goviedodev/niuro)): aplicación fullstack de reporte de turnos que reemplaza una planilla de operaciones industriales. Frontend en **React 18** con TypeScript y componentes reutilizables; backend **NestJS** con arquitectura por capas, `ValidationPipe` global y **pruebas unitarias en Jest**; autenticación con JWT; builds Docker y el mismo pipeline de **CI/CD** en GitHub Actions y Azure Pipelines.

\rol{Desarrollador Java / Integraciones}{2023 – 2024}
\org{Salcobrand (cadena de farmacias)}

- Integraciones para **APIs REST** de alto tráfico: caché con **Redis** y **mensajería asíncrona con IBM MQ**, coordinando ventanas de despliegue y rollback con los equipos de Infraestructura y DevOps.

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient (cliente: Caterpillar)}

- Desarrollo y mantenimiento de las **APIs REST** del e-commerce global de Caterpillar (**Java 21, Spring Boot**), bajo **metodologías Agile (Scrum)**, en equipo distribuido entre EE. UU., India y Latinoamérica, 100% remoto y en inglés.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA (Hospital Cruz del Norte, SQM)}
\stack{Spring Boot (REST, MVC), PostgreSQL 9.6, JavaScript, jQuery, Vuetify, Bootstrap, Git, GitLab.}

- Diseñé y desarrollé fullstack el Sistema de Gestión en Salud (medicina, enfermería, kinesiología): **arquitectura por capas** con backend de **APIs REST** en Spring Boot e interfaz web en JavaScript con componentes reutilizables.
- Construí el módulo transaccional de pagos y la reportería administrativa en PDF, integrados con el resto del sistema vía **APIs REST** internas.
- Lideré técnicamente a 4 desarrolladores (frontend y backend) mediante code review y definición de estándares y **principios de código limpio**.

\rol{Roles previos}{2000 – 2022}
\org{Citibank, Nubox, Cencosud, Portal Inmobiliario, Santander/Isban}

- **Java Specialist en Citibank** (2021 – 2022): soluciones sobre framework interno Java, **consultas SQL** en Oracle, Jenkins, y migración de bases financieras de Sybase a Oracle (más de 15 millones de registros, sin pérdida de datos) en equipo de EE. UU., Ucrania, India y Chile.
- **Full Stack Developer en Nubox** (2014 – 2017): desarrollo frontend con **React** y jQuery, definición de estilos e implementación de vistas para la nueva generación de aplicaciones Nubox.
- **Desarrollador en Cencosud S.A.** (2015 – 2016): software de **gestión de stock** para la cadena de supermercados, con cálculo de índices personalizados de inventario y cargas masivas — dominio cercano al de gestión logística.
- **Ingeniería de Software en Portal Inmobiliario** (2008 – 2016): desarrollo de aplicaciones web y reportería con SQL Server Reporting Services.
- **Analista de Sistemas Bancarios en Santander/Isban** (2000 – 2017): 17 años en el sector financiero (Préstamos, Medios de Pago, Cuentas Corrientes, Tarjetas de Crédito) para Chile, Puerto Rico, Colombia, Uruguay y Venezuela; migraciones bancarias de AS/400 a Java con **Struts** y **Hibernate**.

# Educación e Idiomas

\rol{Ingeniería en Ejecución en Computación e Informática}{Universidad del Bío-Bío, Concepción}
\org{Tesis: Extreme Programming (XP), teoría y práctica (2005 – 2009).}

**Idiomas:** Español nativo. **Inglés B2**, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania (Citibank 2021–2022, Perficient–Caterpillar 2022–2023) — por sobre el nivel B1 solicitado.

**Competencias:** **Comunicación asertiva y trabajo en equipo** (code review y definición de estándares liderando 4 desarrolladores en Seven IT). **Pensamiento analítico y resolución de problemas** (diseño de la arquitectura por capas de la plataforma de movilidad, en producción desde 2024). **Orientación a resultados, planificación y organización** (dos proyectos llevados de punta a punta: la plataforma de movilidad y el Sistema de Gestión en Salud de Seven IT). **Innovación y mejora continua** (adopción de agentes de código como Claude Code en el flujo de desarrollo diario). **Capacidad de aprendizaje** (progresión de Java 8 a 21, y de ahí a React, TypeScript y React Native). **Orientación al cliente** (refinamiento de historias de usuario antes de implementar, en Perficient–Caterpillar). **Capacidad para trabajar en ambientes dinámicos y de alta colaboración** (equipos multiculturales en Perficient/Caterpillar y Citibank: EE. UU., India, Ucrania, Latinoamérica).
