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
{\large Full Stack Senior Developer}\\[6pt]
{\small Limache, Región de Valparaíso · trabajo 100\% remoto (GMT-4) · +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev · Español nativo · Inglés B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Full Stack Senior Developer con más de 15 años diseñando y desarrollando soluciones full stack que integran frontend, backend, APIs REST y servicios externos — el eje central de esta vacante. Trabajo React y TypeScript con componentes reutilizables (interfaz de una plataforma de movilidad en producción y, antes, la nueva generación de aplicaciones de Nubox Facturación Electrónica) y Node.js en el backend de un proyecto público (NestJS). Implementé el checkout con las pasarelas de pago Transbank (Webpay) y Khipu, cubriendo los flujos de pago, confirmación y conciliación de transacciones. Desarrollo bajo Scrum, con Git y CI/CD (incluido GitLab), pruebas unitarias y de integración, y code review.

# Experiencia Profesional

\rol{Tech Lead}{2024 – Presente}
\org{Startup de Movilidad — Chile}
\stack{Java 21 (Spring Boot), React Native, Flutter, PostgreSQL, Google Cloud, Pulumi IaC, Docker, Transbank y Khipu.}

- Diseñé y mantengo la arquitectura full stack completa (frontend, backend, base de datos e infraestructura), en producción con usuarios reales desde 2024.
- Implementé el sistema de pagos con Transbank (Webpay) y Khipu: checkout, confirmación y conciliación de transacciones.
- Construí la primera versión de la interfaz móvil en React Native con componentes reutilizables, y migré el frontend a Flutter sin tocar el backend.
- Diseñé e integré APIs REST de servicios externos (Google Maps: Directions, Distance Matrix, Geocoding).

\rol{UX/UI Designer \& Full Stack Developer}{2014 – 2017}
\org{Nubox Facturación Electrónica}
\stack{HTML, SASS/CSS, React, jQuery.}

- Establecí y supervisé las directrices de interfaz gráfica de la nueva generación de aplicaciones Nubox, implementando las vistas front-end con React y componentes reutilizables.
- Construí el nuevo sitio web para Colombia y su reportería contable, y compatibilicé el sitio a nivel país con Chrome.

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient — Caterpillar}
\stack{Java 21 (Spring Boot), APIs REST, SQL, Git, metodologías ágiles.}

- Desarrollé y mantuve APIs REST del sistema de e-commerce global de Caterpillar.
- Trabajé bajo Scrum en un equipo distribuido entre EE. UU., India y Latinoamérica: refinamiento de historias, code review y coordinación técnica en inglés.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), JavaScript, jQuery, Vuetify, Bootstrap, PostgreSQL 9.6, GitLab.}

- Diseñé y desarrollé full stack el Sistema de Gestión en Salud, con interfaz de componentes reutilizables (Vuetify, Bootstrap) y backend de APIs REST.
- Construí el módulo transaccional de pagos y la reportería administrativa en PDF.
- Lideré técnicamente a 4 desarrolladores mediante Merge Requests en GitLab y definición de estándares.

\rol{Java Specialist en Citibank (2021–2022) y otros roles previos}{2000 – 2017}
\org{Citibank, Hospital Cruz del Norte (Director), Cencosud, Portal Inmobiliario, Santander/Isban}
\stack{Java, AS/400, ExtJs, PHP, PostgreSQL, Oracle, SQL Server Reporting Services.}

- Migré bases de datos financieras de Sybase a Oracle en Citibank: más de 15 millones de registros, sin pérdida de datos.
- Desarrollé interfaces desktop-por-web con componentes reutilizables (ExtJs) para Cencosud y el Hospital Cruz del Norte, y reportería con SQL Server Reporting Services para Portal Inmobiliario.
- 17 años atendiendo requerimientos financieros (Préstamos, Medios de Pago, Cuentas Corrientes, Tarjetas de Crédito) para Santander/Isban en Chile, Puerto Rico, Colombia, Uruguay y Venezuela.

# Proyecto Público Destacado

**Aplicación de reporte de turnos — Next.js 14 + NestJS** — [github.com/goviedodev/niuro](https://github.com/goviedodev/niuro)

- Frontend en Next.js 14 (App Router) con React 18 y TypeScript: componentes reutilizables y wrapper `fetch` tipado que normaliza errores de validación por campo.
- Backend en NestJS 10 + TypeScript (Node.js) vía APIs REST, arquitectura por capas, `ValidationPipe` global y pruebas unitarias en Jest.
- Autenticación con JWT y dos roles; builds Docker multi-stage con CI/CD en GitHub Actions y Azure Pipelines.

# Habilidades Técnicas

- **Frontend:** React 18, TypeScript, JavaScript (ES6+), React Native, Vue.js/Nuxt, Vuetify, componentes reutilizables, HTML/SASS/CSS.
- **Backend y APIs:** Node.js (NestJS), Java (Spring Boot), diseño y desarrollo de APIs REST, integración de servicios externos, arquitectura de microservicios.
- **Checkout y medios de pago:** Transbank Webpay, Khipu, flujos transaccionales de pago, confirmación y conciliación.
- **Bases de datos:** PostgreSQL, Oracle PL/SQL, MySQL, SQL Server, MongoDB.
- **CI/CD y cloud:** Git, GitLab CI/CD, GitHub Actions, Azure Pipelines, Docker, Google Cloud Platform, Pulumi (IaC).
- **Testing y forma de trabajo:** Jest, JUnit, pruebas unitarias y de integración, code review, Merge Requests, Scrum.
- **IA aplicada al desarrollo:** Claude Code (plan Max) como harness principal de desarrollo; experiencia previa con Pi.dev y opencode.

# Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica.

Español nativo. Inglés B2, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania.

**Competencias:** comunicación asertiva y trabajo en equipo (colaboración constante con el equipo de la plataforma de movilidad); pensamiento analítico y resolución de problemas (aplicados a diario en el diseño de esa arquitectura); orientación a resultados, planificación y organización, y proactividad (dos proyectos llevados de punta a punta: la plataforma de movilidad, co-fundada y construida desde cero, y el Sistema de Gestión en Salud de Seven IT); innovación y mejora continua (adopción de agentes de código como parte del flujo de desarrollo) y capacidad de aprendizaje (de Java 8 a 21, y hacia React/TypeScript/Node.js); orientación al cliente (refinamiento de historias de usuario antes de implementar) y capacidad para trabajar en ambientes dinámicos y de alta colaboración (equipos multiculturales en Caterpillar y Citibank: EE. UU., India, Ucrania, Latinoamérica).
