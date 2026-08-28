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
{\large Desarrollador Backend Java}\\[6pt]
{\small Limache, Región de Valparaíso · disponible para modalidad híbrida en Santiago (GMT-4) · +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com · linkedin.com/in/gol · Español nativo · Inglés B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Desarrollador Backend con más de 15 años construyendo y manteniendo servicios backend corporativos en Java (8 en adelante): diseño, implementación y evolución de endpoints REST eficientes con Spring Boot (REST, MVC) en el Sistema de Gestión en Salud de Seven IT y en el e-commerce global de Caterpillar, y APIs de alto rendimiento sobre procesamiento transaccional bancario en Citibank y Santander/Isban — 17 años de tráfico masivo corporativo para Chile, Puerto Rico, Colombia, Uruguay y Venezuela. Java Core sólido (POJOs, concurrencia, serialización); trabajo con NoSQL (MongoDB) además de relacionales (PostgreSQL, Oracle), Docker y ecosistema cloud (Google Cloud, Azure DevOps), con foco en escalabilidad y resiliencia. Sin experiencia productiva en Undertow ni en Azure Storage (Blob Storage, Tables) — mi base de Java Core transfiere directo a arquitecturas ligeras de alta velocidad. Uso agentes de IA generativa (Claude Code) a diario en mi flujo de trabajo, alineado con el Desarrollo Asistido por IA y Spec-Driven Development (SDD) que describe FieldBeat.

# Experiencia Profesional

\rol{Tech Lead}{2024 – Presente}
\org{Startup de Movilidad — Chile}
\stack{Java 21 (Spring Boot), PostgreSQL, Google Cloud, Pulumi IaC, Docker, Git.}

- Diseño y mantengo el backend de APIs REST de la plataforma (Java 21, Spring Boot), en producción con usuarios reales desde 2024.
- Integré APIs REST de servicios externos (Google Maps: Directions, Distance Matrix, Geocoding).
- Implementé el sistema de pagos (Transbank Webpay, Khipu) como endpoints REST del backend: checkout, confirmación y conciliación.
- Despliegues automatizados sobre Google Cloud con infraestructura como código (Pulumi) y Docker.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}
\stack{Java, Oracle SQL, Spring Beans, Jenkins, Jira, Confluence, Git, Eclipse, Gradle, WebSphere.}

- Desarrollé y mantuve servicios backend corporativos para requerimientos mensuales del banco (framework interno Java Bean Spring), con manejo de excepciones y gestión de incidentes en Jira como parte del ciclo de calidad en producción.
- Migré la base de datos de Sybase a Oracle: más de 15 millones de registros financieros, sin pérdida de datos, en equipo multicultural (EE. UU., Ucrania, India, Chile).
- Construí y mantuve reportes para clientes internos sobre datos transaccionales de alto volumen.

\rol{Analista de Sistemas Bancarios}{2000 – 2017}
\org{Santander / Isban}
\stack{Java, AS/400, Struts, JSP, Hibernate, PHP, PostgreSQL, Oracle, SQL Server, Jenkins, Jira.}

- 17 años construyendo y manteniendo servicios backend corporativos para Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito.
- Atención a Chile, Puerto Rico, Colombia, Uruguay y Venezuela: migraciones bancarias de AS/400 a Java, facturación electrónica y gestión de incidentes en ambiente productivo de alto volumen.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), PostgreSQL 9.6, Linux, Google Cloud (VM), GitLab.}

- Diseñé y desarrollé el backend de APIs REST del Sistema de Gestión en Salud, en uso diario por personal clínico.
- Construí el módulo transaccional de pagos y la reportería administrativa en PDF, integrados vía APIs internas.
- Lideré técnicamente a 4 desarrolladores mediante revisión de código en GitLab.

\rol{Java Associate Developer en Perficient — Caterpillar (2022–2023) y otros roles previos}{2014 – 2017}
\org{Nubox Facturación Electrónica, Cencosud, Hospital Cruz del Norte (Director)}
\stack{Java, PostgreSQL, ExtJs, HTML/SASS/CSS, React, jQuery.}

- Desarrollo y mantenimiento de APIs REST del e-commerce global de Caterpillar bajo Scrum, con equipo distribuido EE. UU./India/Latinoamérica.
- Backend Java/PostgreSQL de un sistema de punto de venta (Hospital Cruz del Norte) y desarrollo web/reportería en Nubox y Cencosud.

# Habilidades Técnicas

- **Java Core:** Java (8 – 21), POJOs, concurrencia, serialización, SQL.
- **APIs RESTful:** diseño, estructuración y consumo de APIs REST eficientes, Spring Boot (REST, MVC), Spring Beans, arquitectura de microservicios.
- **Ecosistema Cloud:** Google Cloud (Pulumi IaC), Azure DevOps, Docker.
- **Persistencia y NoSQL:** PostgreSQL, Oracle PL/SQL, SQL Server (relacionales); MongoDB (NoSQL clave-valor/documentos).
- **Desarrollo Asistido por IA:** Claude Code (plan Max) como harness principal de desarrollo, afín a Spec-Driven Development (SDD); experiencia previa con Pi.dev y opencode.

# Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica.

Español nativo. Inglés B2, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania.

**Competencias:** comunicación asertiva y trabajo en equipo (colaboración constante con el equipo de la plataforma de movilidad); pensamiento analítico y resolución de problemas (aplicados a diario en esa arquitectura y en la migración Sybase → Oracle de Citibank); orientación a resultados, planificación y organización, y proactividad (dos proyectos de punta a punta: la plataforma de movilidad, co-fundada y construida desde cero, y el Sistema de Gestión en Salud de Seven IT); innovación y mejora continua (adopción de agentes de código en el flujo de desarrollo); capacidad de aprendizaje (de Java 8 a 21, y hacia arquitecturas cloud); orientación al cliente (reportería específica por requerimiento para clientes internos en Citibank) y capacidad para trabajar en ambientes dinámicos y de alta colaboración (equipos multiculturales en Perficient/Caterpillar y Citibank: EE. UU., India, Ucrania, Latinoamérica).
