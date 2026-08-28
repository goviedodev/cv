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
{\large Desarrollador Full Stack Senior — SQL Server · JavaScript/jQuery · Facturación y Salud}\\[6pt]
{\small Limache, Región de Valparaíso · 100\% remoto (GMT-4, una hora de diferencia con EST) · +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev · Español nativo · Inglés B2}
\end{center}
\vspace{0.4em}

# Resumen Profesional

Desarrollador con **más de 15 años** escribiendo, leyendo, depurando y manteniendo código ajeno en sistemas con lógica de negocio compleja, bases de datos grandes y usuarios reales en producción: 17 años en banca (Santander/Isban), facturación electrónica (Nubox), un sistema de gestión hospitalaria y reportería sobre SQL Server. A esta altura el código es un lenguaje que leo directo: entiendo qué hace una rutina, por qué está escrita así y qué se rompe si la toco. Esa es la expertise que traigo — **código que se entiende, con estándares, nombres y responsabilidades claras**, probado antes de entregarlo.

**Sobre el uso de IA, respondiendo a lo que pide el aviso:** la uso, y no lo escondo — pero como herramienta de consulta, no de autoría. La consulto para entender un concepto o desatascar una duda puntual; **el código lo escribo yo y puedo explicar cada línea de lo que entrego**: qué hace, por qué está ahí, qué efectos tiene y cómo lo probé. No pego lo que devuelve una herramienta. El criterio técnico —arquitectura, estándares, manejo de errores— viene de quince años de oficio, y en un sistema de facturación en producción es ese criterio el que evita el daño.

**Declaración honesta de alcance:** mi experiencia productiva no es en .NET Framework, sino en Java/Spring Boot y stacks web server-side equivalentes; .NET lo conozco a nivel autodidacta, no laboral. Lo comprobable es el resto del aviso: SQL Server, JavaScript/jQuery/HTML/CSS, mantención de sistemas de facturación, sector salud e integraciones con medios de pago.

# Experiencia Profesional

\rol{UX/UI Designer \& Full Stack Developer}{2014 – 2017}
\org{Nubox Facturación Electrónica}
\stack{JavaScript, jQuery, HTML, SASS/CSS, React.}

- Desarrollo y mantención de una plataforma de **facturación electrónica** con base de usuarios activa en Chile y Colombia.
- Construí el sitio de Colombia y su **reportería contable**: reportes de negocio por requerimiento sobre datos transaccionales de facturación.
- Implementé las vistas front-end con JavaScript y jQuery, definí las directrices gráficas de la nueva generación de aplicaciones y compatibilicé el sitio con Chrome a nivel país, corrigiendo el comportamiento que bloqueaba el ingreso de nuevos usuarios.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), JavaScript, jQuery, Bootstrap, Vuetify, PostgreSQL 9.6, Linux, Google Cloud, GitLab.}

- Diseñé, desarrollé y mantuve el **Sistema de Gestión en Salud** (medicina, enfermería, kinesiología), en uso diario por personal clínico.
- Construí el **módulo de gestión de pagos** y los informes administrativos en PDF: el cruce exacto entre facturación y sector salud de esta vacante.
- Desarrollé la capa de interfaz con JavaScript y jQuery, y las consultas y procedimientos de base de datos que la alimentan; lideré técnicamente a 4 desarrolladores vía Merge Requests en GitLab, con estándares revisados antes de cada entrega.

\rol{Ingeniería de Software}{2008 – 2016}
\org{Portal Inmobiliario}
\stack{SQL Server, SQL Server Reporting Services (SSRS), desarrollo web.}

- Aplicaciones web y **reportería sobre SQL Server con SSRS**: consultas de negocio, personalización de documentos y generación de reportes.
- Construí *Seguidor Web*, herramienta de gestión para corredores de propiedades, con mantención evolutiva continua: entender el modelo de datos antes de tocarlo y ajustar consultas sin romper lo que ya funcionaba.

\rol{Analista de Sistemas Bancarios}{2000 – 2017}
\org{Santander / Isban}
\stack{Java, AS/400, Struts, JSP, Hibernate, PHP, SQL Server, Oracle, PostgreSQL, Jenkins, Jira.}

- 17 años de **mantención y evolución de sistemas legacy con lógica de negocio compleja**: Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito, para Chile, Puerto Rico, Colombia, Uruguay y Venezuela.
- **Facturación electrónica** bancaria, migraciones de plataforma (AS/400 a Java) y gestión de incidentes en producción: diagnóstico sobre código ajeno, corrección y verificación antes de liberar.
- Desarrollo web server-side sobre Struts/JSP —ciclo de vida de página, controles y estado del lado del servidor—, el mismo modelo mental que sostiene ASP.NET Web Forms, en otro lenguaje.

\rol{Tech Lead}{2024 – Presente}
\org{Startup de Movilidad — Chile}
\stack{Java 21 (Spring Boot), Elixir, Flutter, PostgreSQL, Google Cloud, Pulumi IaC, Docker, Transbank y Khipu.}

- Integré **APIs de pago** (Transbank Webpay y Khipu): checkout, confirmación y conciliación de transacciones.
- Diseño y mantención de la arquitectura completa de la plataforma, en producción con usuarios reales desde 2024, usando agentes de código dentro de un flujo con puertas de calidad y revisión humana línea por línea, sin delegar la autoría del código entregado.

**Java Specialist en Citibank** (2021 – 2022): framework interno propietario y creación y mantención de reportes en Oracle SQL; migración de base de datos financiera de Sybase a Oracle. **Java Associate Developer en Perficient — Caterpillar** (2022 – 2023): e-commerce global bajo Scrum con equipo distribuido entre EE. UU., India y Latinoamérica. **Director y Desarrollador de Ficha Clínica en Hospital Cruz del Norte, SQM** (2016 – 2017) y **Analista y Desarrollador en Cencosud S.A.** (2015 – 2016): interfaces desktop-por-web con ExtJs, índices de stock y cargas masivas.

# Habilidades Técnicas

- **Bases de datos:** SQL Server (consultas de negocio y reportería con SSRS), Oracle PL/SQL (procedimientos almacenados, optimización de consultas, debugging), PostgreSQL, MySQL; MongoDB.
- **Frontend:** JavaScript (ES6+), jQuery, HTML, SASS/CSS, Bootstrap, Vuetify, ExtJs, React, TypeScript, Vue.js/Nuxt.
- **Backend y web server-side:** Java (Spring Boot, Struts, JSP, Hibernate), Elixir/Phoenix, Node.js, APIs REST e integración de servicios externos.
- **Dominio funcional:** facturación electrónica (Nubox, Santander), sector salud (Hospital Cruz del Norte, Seven IT), medios de pago y pasarelas (Transbank Webpay, Khipu, banca).
- **Control de versiones y entrega:** Git, GitLab (Merge Requests y CI/CD), GitHub Actions, Jenkins, Docker; pruebas unitarias y de integración (JUnit, Jest) y prueba del propio código antes de entregar.
- **Stack .NET — declarado sin experiencia productiva:** .NET Framework, C\# y ASP.NET Web Forms a nivel autodidacta y puntual, no laboral. Lo declaro en vez de inflarlo; la base transferible es el desarrollo web server-side con ciclo de vida de página (Struts/JSP) y SQL Server.
- **IA aplicada al desarrollo:** Claude Code (plan Max) como asistente de consulta y verificación con revisión humana obligatoria; el código entregado es de autoría propia y explicable línea por línea.

# Educación e Idiomas

**Ingeniería en Ejecución en Computación e Informática** — Universidad del Bío-Bío, Concepción (2005 – 2009). Tesis: Extreme Programming (XP), teoría y práctica.

Español nativo. Inglés B2, en uso continuo desde 2021 con equipos de EE. UU., India y Ucrania.

**Competencias:** comunicación asertiva y trabajo en equipo (reporte diario de avances y bloqueos con equipos distribuidos en Caterpillar y Citibank); responsabilidad, compromiso con los plazos y atención al detalle (17 años atendiendo requerimientos bancarios con fecha fija de liberación y sin margen de error en producción); pensamiento analítico y resolución de problemas (diagnóstico y corrección de incidentes sobre código ajeno en banca y salud); planificación y organización (dos proyectos llevados de punta a punta: la plataforma de movilidad y el Sistema de Gestión en Salud de Seven IT); innovación y mejora continua (adopción de agentes de código con puertas de calidad y revisión humana, no como reemplazo del criterio técnico); capacidad de aprendizaje (de Java 8 a 21, y hacia React/TypeScript/Node.js y Elixir); orientación al cliente (refinamiento de requerimientos con el usuario antes de implementar); capacidad para trabajar en ambientes dinámicos y de alta colaboración (equipos multiculturales y trabajo remoto autónomo, sin supervisión).
