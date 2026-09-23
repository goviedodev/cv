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
  \geometry{top=1.05cm,bottom=1.15cm,left=1.45cm,right=1.45cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.55em}{0.30em}
  \setlist[itemize]{leftmargin=1.0em,itemsep=0pt,topsep=1pt,parsep=0pt,label=\textbullet}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{0.16em}
  \linespread{0.97}
  \raggedbottom
  \newcommand{\rol}[2]{\vspace{0.15em}\textbf{#1}\hfill\textbf{#2}\par\vspace{-0.45em}}
  \newcommand{\org}[1]{{#1}\par\vspace{-0.3em}}
  \newcommand{\stack}[1]{{\small\textbf{Stack:} #1}\par\vspace{-0.2em}}
  \newcommand{\producto}[1]{{\small\textbf{Producto:} #1}\par\vspace{-0.2em}}
  \newcommand{\pilar}[1]{\vspace{0.15em}{\small\textbf{#1}}\par\vspace{-0.4em}}
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad Página \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Co-Fundador · CTO — Estrategia, Producto y Tecnología}\\[6pt]
{\small Limache, Región de Valparaíso · disponibilidad para modalidad híbrida en la Región Metropolitana de Santiago · +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev · Español nativo · Inglés B2}
\end{center}
\vspace{0.1em}

# Resumen Profesional

Emprendedor y tecnólogo con más de 15 años en software y **dos empresas propias fundadas y operadas**: hoy **Co-Fundador y CTO de Te Llevo App**, una plataforma donde las personas **reservan y gestionan servicios** de movilidad, y antes **dueño y CTO de Seven IT SpA**, la empresa que creé para construir y vender el Sistema de Gestión en Salud del Hospital Cruz del Norte (SQM). He participado en la **definición de la estrategia del negocio**, el **modelo de ingresos** y el **posicionamiento en el mercado**; en el **diseño y validación del producto**, la **priorización de funcionalidades** y la **planificación de lanzamientos**; y en la **captación de clientes** y la negociación directa con un cliente corporativo. Conozco el lado técnico en profundidad —**productos SaaS**, **arquitectura web**, cloud y **herramientas no-code / IA**— y eso me permite **tomar decisiones ágiles** y **asumir riesgos calculados** sabiendo lo que cuesta construirlos.

# Experiencia Emprendedora y de Liderazgo

\rol{Co-Fundador y CTO}{2024 – Presente}
\org{Te Llevo App — startup de movilidad, Chile}
\producto{plataforma web y móvil donde las personas reservan, pagan y gestionan viajes.}
\stack{Java 21 (Spring Boot), Elixir/Ash Framework, Flutter, Google Cloud, Pulumi (IaC), Docker, PostgreSQL, Claude Code (plan Max) con agentes, MCPs y skills propios.}

\pilar{Estrategia, modelo de ingresos y posicionamiento}

- Co-fundé la empresa desde cero y participo en la **definición de la estrategia del negocio** y del **posicionamiento del producto** en el mercado chileno de movilidad, con actores globales ya instalados.
- Habilité el **modelo de ingresos** integrando los **medios de pago** locales (Transbank, Khipu) en el flujo de reserva y checkout: sin cobro no hay negocio, y ese fue el primer hito que exigí antes de escalar funcionalidades.
- Financiamos la operación con **capital propio y facturación**, no con rondas externas; eso obliga a **asumir riesgos calculados** con presupuesto real y a monitorear costos de infraestructura de forma continua.

\pilar{Diseño y validación del producto}

- Participo en el **diseño y validación del producto**, la **priorización de funcionalidades** y la **planificación de lanzamientos**, refinando historias de usuario con el equipo antes de comprometer desarrollo.
- Definí un producto **fácil de usar, seguro y escalable**: aplicación Flutter para la persona usuaria, backend sobre servicios gestionados de Google Cloud e infraestructura como código reutilizable (Pulumi), de modo que crecer no dependa de configuración manual.

\pilar{Equipo, objetivos y cultura}

- **Coordino tareas con el resto del equipo** y marco **objetivos medibles** por entrega; construí el stack tecnológico completo y lidero al equipo técnico.
- Trabajo con **transparencia y responsabilidad**: decisiones de arquitectura documentadas y revisables en Git, y estándares aplicados en cada Merge Request en lugar de acuerdos verbales.
- Adopté por experimentación propia Elixir/Ash y **agentes de IA** en el ciclo de desarrollo: harness propio sobre Claude Code (plan Max) con skills, comandos, workflows y MCPs, aplicado a diario en análisis, automatización y desarrollo.

\rol{Dueño, Director y CTO}{2016 – 2020}
\org{Seven IT SpA — Sistema de Gestión en Salud (Hospital Cruz del Norte, SQM)}
\producto{software de gestión clínica (medicina, enfermería, kinesiología) más módulo de pagos e informes de administración.}
\stack{Spring Boot (REST, MVC), ExtJS, PostgreSQL, Linux, Google Cloud, GitLab, JavaScript, Bootstrap, Vuetify.}

- **Creé la empresa** y asumí un rol integral —gerencia, jefatura de personal, liderazgo funcional y técnico, análisis, desarrollo e infraestructura— desde la constitución hasta la **puesta en marcha** del sistema en operación hospitalaria real.
- **Presenté la propuesta de valor y negocié el acuerdo** directamente con el Hospital Cruz del Norte (SQM), un cliente corporativo, y sostuve la **relación con el cliente** desde la venta hasta el soporte en producción.
- **Contraté y coordiné un equipo de 4 desarrolladores** (front y backend), definiendo estándares técnicos y prioridades de cada entrega.
- Construí el **módulo de gestión de pagos** e informes en PDF para administración, y un POS de caja por web con cálculo de índices de stock y cargas masivas.
- Diseñé, desplegué y **operé el sistema en Google Cloud**: servidores Linux, PostgreSQL, respaldos y disponibilidad para personal clínico que lo usaba a diario.

# Experiencia en Producto SaaS y Mercado

\rol{UX/UI Designer y Full Stack Developer}{2014 – 2017}
\org{Nubox — Facturación Electrónica (producto SaaS)}

- Definí y supervisé las directrices de interfaz de la nueva generación de aplicaciones Nubox —estilos, mockups e iconografía— aplicando **diseño centrado en la persona usuaria** sobre un producto SaaS con clientes de pago.
- **Lancé el sitio web de Nubox para Colombia** y su reportería contable: **posicionamiento del producto en un nuevo mercado**, con reportes de negocio construidos por requerimiento del cliente.
- Compatibilicé el sitio con Chrome a nivel país, **ampliando la entrada de nuevos usuarios** a la plataforma.

\rol{Analista y Desarrollador}{2008 – 2016}
\org{Portal Inmobiliario}

- Construí **Seguidor Web**, herramienta de gestión y administración para corredores de propiedades: producto interno de un marketplace, con reportería propia para el usuario profesional.

# Experiencia Corporativa y Trabajo con Stakeholders

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient — cliente: Caterpillar}

- Desarrollé y mantuve el e-commerce global de Caterpillar (Java 21, Spring Boot, Scrum) coordinando con equipos de EE. UU., India y Latinoamérica.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}

- Lideré técnicamente la migración de bases de datos financieras de Sybase a Oracle con equipos de EE. UU., Ucrania, India y Chile, en un entorno de alta exigencia de cumplimiento.

\rol{Analista de Sistemas Bancarios}{2000 – 2017}
\org{Santander / Isban}

- 17 años en el sector financiero (Préstamos, Medios de Pago, Cuentas Corrientes, Tarjetas de Crédito) para Chile, Puerto Rico, Colombia, Uruguay y Venezuela: **negociar alcances y plazos** con áreas de negocio fue parte del trabajo diario.

\rol{Analista y Desarrollador}{2015 – 2016}
\org{Cencosud S.A.}

- Desarrollé el software web de gestión de stock de la cadena de supermercados, con cálculo de índices personalizados y cargas masivas.

# Habilidades

- **Estrategia y negocio:** definición de **estrategia del negocio**, **modelo de ingresos** (medios de pago: Transbank, Khipu), **posicionamiento en el mercado**, creación y administración de empresa propia (Seven IT SpA), presupuesto y control de costos, **riesgos calculados** con capital propio.
- **Comercial y comunicación:** presentación de la **propuesta de valor**, **negociación de acuerdos** con cliente corporativo (SQM), **relaciones con clientes y partners** sostenidas en el tiempo, comunicación con áreas de negocio no técnicas (banca, retail, salud), equipos multiculturales (EE. UU., India, Ucrania, Latinoamérica).
- **Producto:** **diseño y validación del producto**, **priorización de funcionalidades**, **planificación de lanzamientos**, refinamiento de historias de usuario, **diseño centrado en la persona usuaria** (UX/UI en Nubox), reportería y analítica de negocio, **objetivos medibles** por entrega.
- **Tecnología:** **productos SaaS** (salud, facturación electrónica, movilidad), **arquitectura web** y de microservicios, APIs REST, Java 21 / Spring Boot, Elixir/Ash, Flutter, JavaScript/TypeScript, PostgreSQL y Oracle, Google Cloud, Pulumi (IaC), Docker, CI/CD (GitLab, Jenkins).
- **IA y herramientas de baja fricción:** harness propio sobre Claude Code (plan Max) con agentes, skills y MCPs aplicado a análisis, automatización y desarrollo; prototipado rápido para **validar producto antes de invertir desarrollo**.

# Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica. Español nativo; **inglés B2** para lectura técnica, documentación y trabajo continuo desde 2021 con equipos de EE. UU., India y Ucrania.

**Competencias:** **Emprendimiento y riesgos calculados** (dos empresas propias: Seven IT SpA, constituida y operada con cliente corporativo, y Te Llevo App, co-fundada y financiada con capital propio). **Habilidades comerciales y de negociación** (propuesta de valor presentada y acuerdo cerrado con el Hospital Cruz del Norte / SQM). **Comunicación asertiva y trabajo en equipo** (coordinación diaria con el equipo de Te Llevo App y jefatura de 4 desarrolladores en Seven IT). **Pensamiento analítico y resolución de problemas** (arquitectura de ambas plataformas y migración Sybase a Oracle en Citibank). **Planificación y organización** (dos productos llevados de punta a punta, desde la constitución de la empresa hasta la operación en producción). **Innovación y mejora continua** (adopción de Elixir/Ash y de agentes de IA en el flujo de desarrollo). **Capacidad de aprendizaje** (progresión de Java 8 a 21 y hacia Elixir, Flutter y agentes de IA). **Orientación a la persona usuaria** (directrices de UX/UI en Nubox y refinamiento de historias de usuario antes de implementar). **Ambientes dinámicos y de alta colaboración** (equipos multiculturales en Perficient/Caterpillar y Citibank).
