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
  \geometry{top=1.4cm,bottom=1.6cm,left=1.7cm,right=1.7cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.7em}{0.5em}
  \setlist[itemize]{leftmargin=1.1em,itemsep=1pt,topsep=2pt,parsep=0pt,label=\textbullet}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{0.3em}
  \linespread{1.0}
  \raggedbottom
  \newcommand{\rol}[2]{\textbf{#1}\hfill\textbf{#2}\par\vspace{-0.4em}}
  \newcommand{\org}[1]{#1\par\vspace{-0.3em}}
  \newcommand{\stack}[1]{{\small\textbf{Stack:} #1}\par\vspace{-0.2em}}
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad Página \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Ingeniero de Software Senior · Soluciones de IA Generativa \& Automatización}\\[6pt]
{\small Limache, Valparaíso, Chile · +56 9 6372 3603 · goviedo.laboral@gmail.com}\\[2pt]
{\small linkedin.com/in/gol · Inglés B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Ingeniero de software con más de 15 años de trayectoria en backend Java/Spring Boot, actualmente enfocado en soluciones de IA generativa, agentes y automatización de procesos. Autor y mantenedor de un proyecto propio de RAG (Retrieval-Augmented Generation) en producción — ingesta y chunking de documentos, generación de embeddings, búsqueda por similitud sobre una base de datos vectorial (PostgreSQL + pgvector) y generación de respuestas con streaming — evidencia directa de trabajo con LLMs, embeddings y bases de datos vectoriales. Opero a diario harnesses de agentes de código (Claude Code, Pi.dev, opencode), diseñando el ciclo de vida de agentes (skills, comandos, workflows) como capa de ejecución e integrando LLMs de bajo costo sin sacrificar rendimiento. Nivel funcional en Python, en aprendizaje activo dado el uso extendido de ese lenguaje en el ecosistema de herramientas de IA generativa.

# Experiencia Profesional

\rol{Tech Lead \& Arquitecto Técnico}{2024 -- Presente}
\org{Startup de Movilidad --- Chile}
\stack{Elixir, Ash Framework, Flutter, Java 21 (Spring Boot), GraalVM, Google Cloud, Pulumi, Claude Code (plan Max), Pi.dev.}

- Arquitectura y desarrollo de la plataforma completa usando Claude Code (plan Max) como harness principal de desarrollo, complementado con Pi.dev, diseñando e implementando el ciclo de vida de agentes (skills, comandos, workflows) e integrando LLMs económicos para optimizar costos sin sacrificar rendimiento.
- Construcción del stack tecnológico completo y liderazgo del equipo técnico.
- Infraestructura en la nube automatizada con Pulumi (IaC).
- Integración de medios de pago (Transbank, Khipu) en Java y Flutter, incluyendo integraciones API con servicios externos.

\rol{Desarrollador Asociado Java}{2022 -- 2023}
\org{Perficient --- Caterpillar}
\stack{Java 21 (Spring Boot).}

- Desarrollo y mantenimiento de sistema de e-commerce global usando Java y metodologías ágiles.
- Colaboración en equipos multiculturales de EE. UU., India y Latinoamérica.

\rol{Especialista Java}{2021 -- 2022}
\org{Citibank}
\stack{Java, Oracle SQL, Spring Beans, Jenkins, Jira, Confluence, Git, Gradle, WebSphere.}

- Desarrollo de soluciones e integraciones para requerimientos mensuales usando framework interno (Java Bean Spring).
- Migración de base de datos de Sybase a Oracle en equipo multicultural (EE. UU., Ucrania, India, Chile).

\rol{Tech Lead}{2017 -- 2020}
\org{Seven IT SpA --- Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), PostgreSQL 9.6, Linux, Google Cloud (VM), Gitlab, jQuery, JavaScript, Bootstrap, Vuetify.}

- Diseño y desarrollo desde cero de Sistema de Gestión en Salud para control y registro de atención hospitalaria (medicina, enfermería, kinesiología), incluyendo APIs backend e integraciones internas.
- Módulo de gestión de pagos y generación automatizada de informes en PDF.
- Liderazgo funcional y técnico de equipo de 4 desarrolladores (front y backend).

\rol{Desarrollador Full-Stack}{2000 -- 2017}
\org{Santander/Isban, Nubox, Cencosud, Portal Inmobiliario}
\stack{Java, AS/400, Struts, JSP, Hibernate, PHP, PostgreSQL, Oracle, SQL Server, HTML, SASS/CSS, React, ExtJs.}

- 17 años en el sector financiero (Santander/Isban) atendiendo requerimientos de Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito para Chile, Puerto Rico, Colombia, Uruguay y Venezuela; facturación electrónica, migraciones bancarias (AS/400 a Java) y gestión de incidentes.
- Diseño de interfaz gráfica y desarrollo full-stack para Nubox Facturación Electrónica (nueva generación de aplicaciones y sitio para Colombia).
- Desarrollo de software de gestión de stock e integraciones para Cencosud S.A. y reportería para Portal Inmobiliario.

# Proyectos Destacados

**RAG sobre Ley 21.719 de Protección de Datos Personales (Chile)** — proyecto propio, en producción.
Repositorio: github.com/goviedodev/ley-datos-personales · Demo: datos-personales.limachelocales.cl

- Stack: Java 21, Spring Boot 4.1.1, Spring AI 2.0.1, PostgreSQL con extensión pgvector, Ollama (modelo qwen3.5:4b para generación, nomic-embed-text para embeddings de 768 dimensiones), 100% autoalojado (sin servicios externos).
- Implementa el patrón RAG completo: ingesta y limpieza de PDF, chunking (400 tokens, TokenTextSplitter), vectorización, búsqueda por similitud coseno (top-8) sobre pgvector, inyección de contexto en el prompt, respuesta con streaming token a token y memoria de conversación por sesión.
- Evidencia directa y verificable de trabajo con LLMs, embeddings, bases de datos vectoriales y arquitecturas de agentes/automatización aplicadas a un caso de uso real.

# Habilidades Técnicas

- **Lenguajes:** Java (1.8 -- 21), SQL. Python a nivel funcional, en aprendizaje activo.
- **Frameworks Backend:** Spring Boot, Spring AI, Struts, Hibernate.
- **IA Generativa \& Agentes:** Claude Code (plan Max, uso intensivo), Pi.dev, opencode -- orquestación de agentes, diseño de skills/hooks/workflows; integración de LLMs (Ollama), embeddings, RAG, prompt engineering.
- **Bases de Datos:** PostgreSQL (incluyendo pgvector para búsqueda vectorial), Oracle PL/SQL, MySQL, MongoDB.
- **Cloud \& Infraestructura:** Google Cloud (Pulumi IaC), Docker, Azure DevOps, AWS Lambda.
- **Frameworks Secundarios:** Flutter, Vue.js/Nuxt, React, Phoenix (Elixir Framework).

# Educación e Idiomas

\rol{Ingeniería en Ejecución en Computación e Informática}{2005 -- 2009}
\org{Universidad del Bío Bío, Concepción -- Tesis: Extreme Programming (XP), teoría y práctica.}

**Idiomas:** Español (nativo) · Inglés B2.

# Competencias

**Comunicación asertiva y trabajo en equipo** (colaboración constante con el equipo de la plataforma de movilidad). **Pensamiento analítico y resolución de problemas** (aplicados a diario en el diseño de esa arquitectura). **Orientación a resultados, planificación y organización, proactividad** (dos proyectos llevados de punta a punta: la plataforma de movilidad y el Sistema de Gestión en Salud de Seven IT). **Innovación y mejora continua** (adopción de agentes de código -- Claude Code -- y desarrollo de un proyecto propio de RAG en producción). **Capacidad de aprendizaje** (progresión de Java 8 a 21, y estudio activo de Python y herramientas de IA generativa). **Orientación al cliente** (refinamiento de historias de usuario antes de implementar). **Capacidad para trabajar en ambientes dinámicos y de alta colaboración** (equipos multiculturales en Perficient/Caterpillar y Citibank -- EE. UU., India, Ucrania, Latinoamérica).
