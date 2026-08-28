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
{\large Desarrollador Java · Spring Boot · Desarrollo asistido por IA}\\[6pt]
{\small Limache, Región de Valparaíso, Chile · +56 9 6372 3603 · goviedo.laboral@gmail.com}\\[2pt]
{\small linkedin.com/in/gol · Inglés B2 · Disponible para modalidad híbrida en Santiago}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Más de 15 años desarrollando sobre Java y Spring Boot en entornos donde la entrega no se puede postergar: banca (Citibank, Coopeuch, Santander), e-commerce global (Caterpillar) y sistemas de salud en producción. Especialista en APIs REST, capa de datos con JPA sobre Oracle y PostgreSQL, integración con sistemas legacy y migraciones de datos críticas. Trabajo con un flujo de desarrollo asistido por IA —especificación versionada, implementación con agentes de código, revisión humana y suite de tests como puerta de calidad— que acelera de forma medible el trabajo de endpoints, CRUD e integraciones, el núcleo de un proyecto Spring Boot de plazo acotado. Disponibilidad inmediata.

# Habilidades Técnicas

- **Lenguaje y framework:** Java 8–21, Spring Boot (REST, MVC, Data JPA, Beans), Maven, Gradle.
- **Bases de datos:** PostgreSQL, Oracle PL/SQL, SQL Server, MySQL, MongoDB.
- **Integración:** APIs REST entre sistemas legacy y plataformas modernas, migraciones de datos (Sybase a Oracle, AS/400 a Java), módulos de pago, facturación electrónica.
- **DevOps y despliegue:** Docker, Google Cloud (Cloud Run, Compute Engine), Pulumi (IaC), Jenkins, GitLab CI, Azure DevOps, WebSphere, Linux.
- **Desarrollo asistido por IA:** OpenSpec para especificación versionada; Claude Code (plan Max) sobre harness Firstmate; ciclo spec → plan → ejecución → verificación con revisión humana y tests automatizados antes de cada merge.
- **Frontend complementario:** Vue.js/Nuxt, React, Flutter, jQuery, Bootstrap.
- **Metodología:** Scrum, Jira, Confluence, Git, code review.

# Experiencia Profesional

\rol{Tech Lead \& Desarrollador Backend}{2024 – Presente}
\org{Te Llevo App — Startup de movilidad, Chile}
\stack{Java 21 (Spring Boot), PostgreSQL, Docker, Google Cloud, Pulumi, Elixir/Phoenix, Flutter.}

- **Plataforma en producción:** construí y mantengo una plataforma de movilidad con usuarios reales, con backend Java Spring Boot y APIs REST consumidas por aplicaciones móviles Flutter y por el frontend web. Verificable en [www.tellevoapp.cl](https://www.tellevoapp.cl) y [app.tellevoapp.cl](https://app.tellevoapp.cl).
- **Pagos e infraestructura:** implementé la integración del flujo de pagos de punta a punta y automaticé la infraestructura en Google Cloud como código con Pulumi.
- **Flujo de desarrollo con IA:** definí el ciclo de trabajo con agentes de código —especificación versionada en el repositorio con OpenSpec, implementación con Claude Code sobre Firstmate— con suite de tests automatizados y revisión humana como condición para integrar a la rama principal.

\rol{Java Developer}{2022 – 2023}
\org{Perficient — Caterpillar}
\stack{Java, Spring Boot, metodologías ágiles.}

- **E-commerce global:** desarrollo y mantenimiento de los servicios Java/Spring Boot del sistema de e-commerce mundial de Caterpillar.
- **Equipos distribuidos:** trabajo en células ágiles entre EE.UU., India y Latinoamérica, con entregas por sprint y code review cruzado.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}
\stack{Java, Spring, Oracle SQL, Jenkins, Jira, Confluence, Git, Gradle, WebSphere.}

- **Desarrollo bancario:** soluciones sobre el framework interno Java/Spring del banco, atendiendo requerimientos de negocio en ciclos mensuales de entrega.
- **Migración crítica de datos:** migración de Sybase a Oracle sobre volúmenes financieros de más de 15 millones de registros, en equipo distribuido entre EE.UU., Ucrania, India y Chile.
- **Reportería:** creación y mantenimiento de reportes para clientes internos, con documentación técnica en Confluence.

\rol{Tech Lead \& Desarrollador}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), PostgreSQL, Google Cloud, GitLab, Linux, JavaScript.}

- **Sistema de gestión hospitalaria:** diseñé, construí y operé sobre Spring Boot y PostgreSQL el registro de atenciones de medicina, enfermería y kinesiología, desplegado en Google Cloud.
- **Módulo de pagos e informes:** desarrollé la gestión de pagos y la generación de informes PDF para administración.
- **Liderazgo técnico:** dirigí un equipo de 4 desarrolladores (frontend y backend), desde el levantamiento de requerimientos con personal clínico hasta el despliegue en producción.

\rol{Desarrollador Java Senior}{2008 – 2017}
\org{WebClass, Creasys, Coopeuch y otros}
\stack{Java, Struts, JSP, Hibernate, AS/400, PostgreSQL, Oracle, SQL Server, Jenkins, Jira.}

- **Desarrollo full-cycle** (análisis, diseño, construcción y QA) para banca, retail y ed-tech: Santander, Ripley, Coopeuch.
- **Migraciones y facturación:** migraciones bancarias de AS/400 a Java, implementación de facturación electrónica y gestión de incidentes en producción.
- **Impacto de negocio:** nuevas funcionalidades sobre una plataforma educativa usada por 1.800 escuelas, que habilitaron ventas adicionales.

# Educación e Idiomas

\rol{Ingeniería de Ejecución en Computación e Informática}{2005 – 2009}
\org{Universidad del Bío-Bío, Concepción}

- Tesis: Extreme Programming (XP), teoría y práctica.
- Español nativo · Inglés B2, con colaboración técnica diaria en equipos de EE.UU., Ucrania e India.

# Disponibilidad

Disponibilidad inmediata para incorporarse a un proyecto de plazo acotado. Resido en Limache: puedo comprometer 1 a 2 días presenciales por semana en Santiago en días fijos, con presencialidad reforzada durante el kickoff, y el resto de la semana en remoto dentro del horario de oficina.
