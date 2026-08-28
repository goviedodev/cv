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
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad P\'agina \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Senior Full Stack Developer --- React/Next.js/NestJS (Miner\'ia)}\\[6pt]
{\small Limache, Regi\'on de Valpara\'iso, Chile \textbar\ disponible remoto o h\'ibrido en Santiago \textbar\ +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com \textbar\ linkedin.com/in/gol \textbar\ github.com/goviedodev \textbar\ Ingl\'es B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Full-stack developer con 15+ años construyendo aplicaciones completas de punta a punta --- backend, frontend, base de datos e infraestructura --- en más de un stack (Java/Spring Boot, PHP, Elixir/Phoenix, Node.js/TypeScript). Hoy diseño y opero la arquitectura completa de una plataforma de movilidad en producción, y construí una aplicación de reporte operacional en Next.js 14 + NestJS. A esta altura de la carrera, la brecha técnica entre una tecnología u otra ya no es la variable que decide un proyecto: la resuelve haber construido de cero, más de una vez y en más de un lenguaje, sistemas completos que siguen en producción --- incluido un sistema de gestión clínica para una operación minera y química (SQM).

# Habilidades Técnicas

- **Backend y lenguajes:** Node.js/TypeScript (NestJS), Java (Spring Boot, Struts), PHP, SQL.
- **Frontend:** Next.js (App Router), React 18, TypeScript, JavaScript (ES6+), Vue.js/Nuxt, Flutter.
- **Datos e integraciones:** PostgreSQL, Oracle PL/SQL, MySQL, SQL Server; exportación de datos a un data lake de Databricks vía Files API (Unity Catalog Volumes).
- **Autenticación y accesos:** JWT, autorización basada en roles, control de acceso por token.
- **Cloud, Docker y CI/CD:** Google Cloud (Cloud Run), Docker (multi-stage), Pulumi IaC, Git, GitHub Actions, Azure Pipelines (Azure DevOps), Jenkins, GitLab CI.
- **Testing e IA aplicada:** Jest, JUnit, Mockito; Claude Code (plan Max) como herramienta principal en desarrollo, testing y documentación.

**Notas honestas para esta vacante:** sin experiencia productiva con Microsoft Entra ID ni Azure Key Vault (autenticación real vía JWT + roles). El respaldo de NestJS/Next.js es el proyecto público niuro, no 4+ años facturados en ese stack puntual. Databricks: experiencia real acotada al lado de escritura (exportación vía Files API), no lectura/consulta de dashboards ya integrados.

# Proyecto Público Destacado

\rol{Aplicación de reporte de turnos --- Next.js 14 + NestJS}{github.com/goviedodev/niuro}
\stack{Next.js 14, React 18, TypeScript, NestJS 10, JWT (HS256), Jest, Docker, GitHub Actions, Azure Pipelines.}

- Diseñé y construí esta app para reemplazar una planilla de operaciones industriales por una app web estructurada, trazable y con exportación a un data lake --- el mismo tipo de problema que un visualizador de indicadores de condición y riesgo de activos, en otro dominio operacional.
- Frontend en Next.js 14 (App Router) con React 18 y TypeScript: sesión de usuario, formularios controlados y un wrapper \texttt{fetch} tipado que adjunta el token y normaliza errores de validación por campo.
- Backend en NestJS 10 + TypeScript, arquitectura por capas, \texttt{ValidationPipe} global y pruebas unitarias en Jest; autenticación JWT (HS256) con dos roles (operador, supervisor).
- Exportación de datos al lake en formato JSONL vía Databricks Files API (Unity Catalog Volumes); builds Docker multi-stage con el mismo pipeline en GitHub Actions y Azure Pipelines.

# Experiencia Profesional

\rol{Tech Lead}{2024 -- Presente}
\org{Startup de Movilidad --- Chile}
\stack{Elixir (Phoenix, Ash), Java 21 (Spring Boot), TypeScript, Flutter, PostgreSQL, Google Cloud, Pulumi IaC, Docker, Claude Code.}

- Diseño y mantengo la arquitectura completa de la plataforma (backend, base de datos, infraestructura), en producción con usuarios reales desde 2024.
- Integré APIs de terceros (Google Maps: Directions, Distance Matrix, Geocoding) para el cálculo de rutas y distancias entre pasajeros y conductores.
- Automaticé el despliegue de infraestructura en Google Cloud con Pulumi (IaC) sobre contenedores Docker.
- Definí el flujo de trabajo del equipo con agentes de código (Claude Code): spec, plan, ejecución y verificación, con la suite de pruebas automatizadas como puerta de calidad.

\rol{Java Associate Developer}{2022 -- 2023}
\org{Perficient --- Caterpillar}
\stack{Java 21, Spring Boot, APIs REST, equipo ágil distribuido.}

- Desarrollo y mantenimiento de servicios backend para la plataforma de e-commerce global de Caterpillar, en equipo Scrum distribuido entre EE.\ UU., India y Latinoamérica.

\rol{Java Specialist}{2021 -- 2022}
\org{Citibank}
\stack{Java, Oracle PL/SQL, Spring Beans, Jenkins, Gradle, WebSphere, Git.}

- Migré la base de datos de reportería de Sybase a Oracle --- más de 15 millones de registros financieros, sin pérdida de datos --- junto a equipos de EE.\ UU., Ucrania, India y Chile bajo un proceso regulatorio estricto.
- Desarrollo y mantención de reportería recurrente para clientes internos del banco sobre el framework interno basado en Spring.

\rol{Tech Lead}{2017 -- 2020}
\org{Seven IT SpA --- Hospital Cruz del Norte (SQM)}
\stack{Spring Boot (REST, MVC), PostgreSQL 9.6, JavaScript, jQuery, Vuetify, Google Cloud (VM), Linux, GitLab.}

- Diseñé, construí y operé de punta a punta el Sistema de Gestión en Salud (medicina, enfermería, kinesiología) para una clínica que atiende a la operación minera y química de SQM: backend REST, interfaz web y esquema PostgreSQL.
- Construí el módulo de gestión de pagos y la reportería administrativa en PDF, integrados con el resto del sistema.
- Lideré técnicamente a un equipo de 4 desarrolladores (front y backend) mediante revisión de código y definición de estándares.

\rol{Java / Senior Developer}{2008 -- 2017}
\org{WebClass, Creasys, Coopeuch y otros}
\stack{Java, AS/400, Struts, JSP, Hibernate, PHP, PostgreSQL, Oracle, SQL Server, Jenkins, Jira.}

- Desarrollo full-cycle: análisis de requerimientos, diseño, desarrollo y QA para banca, ed-tech y empresa.
- Migración de procesos bancarios de AS/400 a Java para Santander, Ripley y Coopeuch, sin detener la operación.
- Facturación electrónica e integraciones SOAP/REST entre aplicaciones Java/PHP y sistemas de terceros.

# Educación e Idiomas

\rol{Ingeniería en Ejecución en Computación e Informática}{Universidad del Bío-Bío, 2005 -- 2009}
\org{Tesis: Extreme Programming (XP), teoría y práctica.}

**Idiomas:** Español nativo \textbar\ Inglés B2 --- uso continuo desde 2021 con equipos de EE.\ UU., India y Ucrania.
