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
  \geometry{top=1.3cm,bottom=1.5cm,left=1.6cm,right=1.6cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.6em}{0.4em}
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
{\large Ingeniero de Automatización de Procesos con IA}\\[6pt]
{\small Actual: Limache, Región de Valparaíso (Chile) · Reubicación: disponible para modalidad híbrida en Santiago}\\[2pt]
{\small +56 9 6372 3603 · goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev}\\[2pt]
{\small Español nativo · Inglés técnico intermedio-avanzado (B2)}
\end{center}
\vspace{0.3em}

# Resumen Profesional

Ingeniero de software con más de 15 años en desarrollo, automatización e implementación de soluciones tecnológicas (Java/Spring Boot, banca, salud, retail) y, desde 2024, dedicado a diseñar soluciones basadas en **Inteligencia Artificial Generativa** que están en producción. Trabajo a diario con el ecosistema **Claude/Anthropic**: construí mi flujo de desarrollo sobre **Claude Code (plan Max)** con **skills, comandos, workflows y servidores MCP** propios, y diseño y orquesto **flujos de trabajo que integran modelos y servicios de IA** (agentes con Jido.AI en Elixir, RAG con Spring AI y pgvector, automatizaciones sobre Cloudflare Workers). He analizado procesos **As-Is** de hospitales, farmacias y comercios para convertirlos en software, y sé explicar una solución de IA tanto a un equipo de desarrollo como a un cliente sin formación técnica.

# Experiencia Profesional

\rol{Tech Lead y Arquitecto}{2024 -- Presente}
\org{Te Llevo, plataforma de movilidad --- Chile · En producción: app.tellevoapp.cl}
\stack{Claude Code (plan Max), MCP, openspec, Elixir/Phoenix (Ash, Jido.AI), Java 21 (Spring Boot, Spring AI), Flutter, PostgreSQL + pgvector, Ollama, Google Cloud, Pulumi, Cloudflare Workers.}

- Diseñé y orquesto el **flujo de trabajo con agentes de IA** del equipo sobre **Claude Code**: skills y comandos (diseño de prompts versionados por tarea), workflows con planificación obligatoria vía **openspec** antes de tocar código, y puertas de calidad con tests, linter y cobertura. El resultado no depende del prompt del día: depende del proceso.
- Integré **LLMs de bajo costo** en tareas de soporte para optimizar costos sin sacrificar rendimiento, seleccionando modelo por tarea y midiendo el costo por petición.
- **RAG sobre la Ley 21.719 de Protección de Datos Personales** (datos-personales.limachelocales.cl, github.com/goviedodev/ley-datos-personales): **Java 21 + Spring AI**, **integración de la API del modelo** vía Ollama (qwen3.5 para generación, nomic-embed-text para embeddings), PostgreSQL con **pgvector**, ingesta y chunking de PDF, búsqueda por similitud coseno, **diseño de prompts** con inyección de contexto, respuesta con streaming y memoria de conversación por sesión.
- **Automatización para una farmacia local** (farma.limachelocales.cl): Elixir/Phoenix con **Jido.AI**, framework de **agentes de IA** que deja determinista lo que debe serlo y reserva el **LLM** para donde aporta. Levanté el proceso **As-Is** con el dueño del negocio y definí con él qué automatizar.
- **Solución para una zapatería local** construida íntegramente con IA sobre **Cloudflare Workers (JavaScript/TypeScript)**, con un cliente sin formación técnica: relevamiento del proceso, propuesta en lenguaje simple y entrega iterativa.
- Infraestructura completa como código con **Pulumi sobre Google Cloud** e integración de medios de pago (Transbank, Khipu) en Java y Flutter.

\rol{Desarrollador Java / Integraciones}{2023 -- 2024}
\org{Salcobrand --- cadena de farmacias}

- Integraciones para APIs de alto tráfico: caché con **Redis** y mensajería asíncrona con **IBM MQ**, coordinando ventanas de despliegue y rollback con los equipos de Infraestructura y DevOps.

\rol{Java Associate Developer}{2022 -- 2023}
\org{Perficient --- cliente: Caterpillar}

- Desarrollo y mantenimiento de las **APIs REST** del e-commerce global de Caterpillar (Java 21, Spring Boot, Scrum), en un equipo distribuido entre EE. UU., India y Latinoamérica, 100% remoto y en inglés.

\rol{Java Specialist}{2021 -- 2022}
\org{Citibank}

- Soluciones e integraciones sobre framework interno (Java, Oracle SQL, Jenkins, WebSphere) y migración de bases financieras de Sybase a Oracle: más de 15 millones de registros sin pérdida de datos, con equipos de EE. UU., Ucrania, India y Chile.

\rol{Tech Lead}{2017 -- 2020}
\org{Seven IT SpA --- Hospital Cruz del Norte, SQM}

- Dueño, gestor y desarrollador del Sistema de Gestión en Salud: **analicé los procesos As-Is** de medicina, enfermería y kinesiología junto al personal clínico y administrativo, identifiqué qué automatizar y lo convertí en módulos en producción, incluido el de pagos e informes en PDF para la administración.
- **Presentaciones y reuniones con el cliente y sus stakeholders** (dirección del hospital, jefaturas clínicas) para definir alcance y prioridades; liderazgo técnico de 4 desarrolladores.

\rol{Roles previos}{2000 -- 2017}
\org{Hospital Cruz del Norte, Nubox, Cencosud, Portal Inmobiliario, Santander/Isban}

- 17 años en el sector financiero (Santander/Isban) atendiendo requerimientos de Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito para Chile, Puerto Rico, Colombia, Uruguay y Venezuela: levantamiento de requerimientos con áreas de negocio, migraciones (AS/400 a Java) y gestión de incidentes.
- Directrices de interfaz y desarrollo full-stack en Nubox (JavaScript, React); software de gestión de stock para Cencosud; reportería para Portal Inmobiliario.

# Habilidades Técnicas

- **Claude/Anthropic:** Claude Code (plan Max, uso diario desde 2024) con skills, comandos, workflows y servidores **MCP** propios; **Function Calling / tool use**; planificación con openspec; harnesses previos Pi.dev y opencode.
- **Inteligencia Artificial Generativa y LLM:** **integración de APIs de modelos de IA** (Spring AI, Ollama, Jido.AI), **diseño de prompts**, RAG (embeddings, pgvector, chunking, inyección de contexto), streaming, memoria de conversación, selección de modelo por costo.
- **Orquestación de flujos y agentes de IA:** agentes con Jido.AI (Elixir), workflows de agentes de código, automatizaciones sobre Cloudflare Workers, integración de modelos y servicios de IA en procesos existentes.
- **Lenguajes:** Java (1.8 -- 21), SQL, JavaScript/TypeScript (React, Vue.js, Node.js en Cloudflare Workers), Elixir; **Python** a nivel funcional, en estudio activo por su uso en el ecosistema de IA.
- **Backend y datos:** Spring Boot, Spring AI, APIs REST, microservicios, PostgreSQL (pgvector), Oracle, MySQL, MongoDB, Redis, IBM MQ.
- **Cloud e infraestructura:** Google Cloud (Cloud Run, IAM, Secret Manager, Logging), Pulumi (IaC), Docker, CI/CD (GitLab CI, Jenkins, GitHub Actions), Cloudflare.

# Educación e Idiomas

\rol{Ingeniería en Ejecución en Computación e Informática}{2005 -- 2009}
\org{Universidad del Bío-Bío, Concepción --- Tesis: Extreme Programming (XP), teoría y práctica.}

**Idiomas:** Español nativo. **Inglés técnico intermedio-avanzado (B2)**: documentación, reuniones y trabajo diario en inglés con equipos de EE. UU., India y Ucrania (Citibank 2021--2022, Perficient--Caterpillar 2022--2023).

# Competencias

**Comunicación con clientes y stakeholders** (definición de alcance con la dirección y jefaturas clínicas del Hospital Cruz del Norte; relevamiento directo con dueños de una farmacia y una zapatería). **Capacidad de explicar conceptos técnicos de IA a audiencias no técnicas** (propuestas de automatización con IA presentadas en lenguaje simple a comercios locales, hoy en producción). **Pensamiento analítico y resolución de problemas** (análisis As-Is de procesos hospitalarios convertidos en módulos de software). **Orientación a resultados, planificación y organización** (dos proyectos llevados de punta a punta: la plataforma de movilidad y el Sistema de Gestión en Salud). **Innovación y mejora continua / actualización permanente** (adopción de Claude Code, MCP, Spring AI y Jido.AI por experimentación propia, con resultados en línea). **Trabajo en equipo en ambientes dinámicos** (equipos multiculturales en Perficient/Caterpillar y Citibank). **Capacidad de aprendizaje** (de Java 8 a 21, y de ahí a Elixir, Spring AI y Python).
