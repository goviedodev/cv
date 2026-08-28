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
{\large Developer Senior Backend Java · Banca}\\[6pt]
{\small Limache, Región de Valparaíso · disponible para modalidad híbrida en Santiago · +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com · linkedin.com/in/gol · Español nativo · Inglés B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Developer Java con 15 años de trabajo en banca. Migré bases financieras de Sybase a Oracle en Citibank y llevé procesos batch de host AS/400 a Java en Santander, Ripley y Coopeuch. Java 8 a 21 y Spring Boot son la herramienta diaria; hoy respondo por la arquitectura backend de una plataforma en producción.

# Habilidades Técnicas

- **Java y Spring Boot:** Java 8 / 11 / 17 / 21, Spring Boot 3.x, Spring MVC, Spring Beans, Spring Data JPA, Struts, WebSphere, Gradle, GraalVM. Concurrencia: hilos, ejecución paralela de procesos batch y control de acceso a recursos compartidos.
- **ORM y bases de datos:** Hibernate / JPA, Oracle PL/SQL (queries y stored procedures), SQL Server, Sybase, PostgreSQL, MySQL, MongoDB. Modelado de esquemas y migraciones de gran volumen.
- **Integración de servicios:** consumo e integración de servicios REST y SOAP, APIs internas de banca, reportería para áreas usuarias. Patrones de diseño aplicados a diario: Singleton, Builder, DTO, Repository.
- **Sistemas legacy y host bancario:** AS/400, análisis funcional y técnico de procesos batch existentes y su reimplementación en Java (Santander, Ripley, Coopeuch).
- **Ciclo de desarrollo y operación:** Git, GitLab, Jenkins, CI/CD, Docker, Pulumi (IaC), Google Cloud, AWS (Lambda, S3), Linux, Elasticsearch y Kibana para búsqueda y revisión de logs, Jira, Confluence, metodologías ágiles.
- **IA aplicada al desarrollo:** Claude Code (plan Max) como harness principal de trabajo; experiencia previa con Pi.dev y opencode.

# Experiencia Profesional

\rol{Tech Lead}{2024 – Presente}
\org{Startup de Movilidad — Chile}
\stack{Java 21 (Spring Boot), GraalVM, Elixir, Google Cloud, Pulumi IaC, Docker, Git, Claude Code (plan Max).}

- Diseñé la arquitectura backend completa de la plataforma, en producción con usuarios reales desde 2024.
- Automaticé la infraestructura cloud con Pulumi (IaC) sobre contenedores Docker: los despliegues no tienen pasos manuales.
- Definí el flujo de trabajo con agentes de código del equipo —spec, plan, ejecución y verificación— con la suite de pruebas automatizadas como puerta de calidad.
- Trabajo con mínima supervisión externa: la investigación técnica, la decisión de arquitectura y la implementación son mías.

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient — Caterpillar}
\stack{Java, Spring Boot, APIs REST, Git, metodologías ágiles.}

- Desarrollo y mantenimiento del sistema de e-commerce global de Caterpillar, sobre servicios REST consumidos por varios frentes.
- Coordinación técnica diaria en inglés con equipos de EE.UU., India y Latinoamérica.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}
\stack{Java, Spring Beans, Oracle PL/SQL, Sybase, Jenkins, Gradle, WebSphere, Git, Jira, Confluence.}

- Ejecuté la migración de bases de datos financieras de Sybase a Oracle: más de 15 millones de registros, sin pérdida de datos, con ventanas de corte acotadas y exigencias regulatorias de por medio.
- Desarrollé los requerimientos mensuales del banco sobre el framework interno (Java Bean / Spring), respetando la metodología y los estándares de la corporación.
- Construí y mantuve la reportería para clientes internos dentro de los SLA acordados con las áreas usuarias.
- Integración con servicios internos del banco y coordinación técnica con equipos de EE.UU., Ucrania, India y Chile.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), PostgreSQL 9.6, Google Cloud (VM), Linux, GitLab, JavaScript.}

- Lideré el diseño y desarrollo del Sistema de Gestión en Salud (medicina, enfermería, kinesiología), usado a diario por personal clínico.
- Construí el módulo transaccional de pagos, con reportería administrativa en PDF.
- Conduje un equipo de 4 desarrolladores (front y backend) con code reviews y revisiones de diseño.

\rol{Java / Senior Developer}{2008 – 2017}
\org{WebClass, Creasys, Coopeuch y otros — banca, retail y ed-tech}
\stack{Java, AS/400, Struts, JSP, Hibernate, SQL Server, Oracle, PostgreSQL, servicios SOAP, Jenkins, Jira.}

- Participé en migraciones bancarias de host AS/400 a Java para Santander, Ripley y Coopeuch: levantamiento del proceso existente, diseño del modelo de datos y reimplementación de la lógica en Java.
- Integré servicios SOAP y REST entre aplicaciones Java y sistemas de terceros (facturación electrónica, servicios internos de banca y retail).
- Escribí queries y stored procedures sobre SQL Server y Oracle para procesos de negocio y reportería.
- Sumé funcionalidades a la plataforma educativa que sirve a 1.800 escuelas y 500 mil peticiones diarias, y atendí incidentes en producción.

# Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Titulado. Tesis: Extreme Programming (XP), teoría y práctica.

Español nativo. Inglés B2, en uso continuo desde 2021 con equipos de EE.UU., India y Ucrania.
