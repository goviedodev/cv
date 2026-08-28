---
lang: en
colorlinks: true
urlcolor: black
linkcolor: black
header-includes: |
  ```{=latex}
  \usepackage{titlesec}
  \usepackage{enumitem}
  \usepackage{fancyhdr}
  \geometry{top=1.0cm,bottom=1.1cm,left=1.4cm,right=1.4cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.55em}{0.3em}
  \setlist[itemize]{leftmargin=1.0em,itemsep=0pt,topsep=1pt,parsep=0pt,label=\textbullet}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{0.22em}
  \linespread{0.97}
  \raggedbottom
  \newcommand{\rol}[2]{\textbf{#1}\hfill\textbf{#2}\par\vspace{-0.4em}}
  \newcommand{\org}[1]{\textit{#1}\par\vspace{-0.3em}}
  \newcommand{\stack}[1]{{\small\textit{Stack:} #1}\par\vspace{-0.2em}}
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad Page \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Full-Stack Engineer — React \textperiodcentered\ TypeScript \textperiodcentered\ REST APIs \textperiodcentered\ Cloud \& CI/CD}\\[6pt]
{\small Valparaíso Region / Santiago Metropolitan Region, Chile (GMT-4) \textperiodcentered\ +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com \textperiodcentered\ linkedin.com/in/gol \textperiodcentered\ github.com/goviedodev \textperiodcentered\ Native Spanish \textperiodcentered\ English B2}
\end{center}
\vspace{0.4em}

# Professional Summary

Full-stack engineer with over 15 years building and running software end to end: React and TypeScript interfaces with reusable, scalable components, decoupled backend services and REST APIs, automated testing, code review and CI/CD. Most of my career has been in payments and financial systems — 17 years at Santander/Isban on loans, payment methods, current accounts and credit cards, then Citibank, and more recently the Transbank (Webpay) and Khipu payment-gateway integration of a mobility platform in production — so collection, dispersion and transaction reconciliation are familiar ground, as are the secure-development standards a fintech requires (JWT authentication and authorisation, secrets kept out of source, least privilege, server-side validation). I use Claude Code daily as my primary development harness, under a spec → plan → execute → verify flow where I read, review and own every line that ships — never unsupervised generation.

# Professional Experience

\rol{Tech Lead}{2024 – Present}
\org{Mobility Startup — Chile}
\stack{React Native, TypeScript, Java 21 (Spring Boot), Flutter, PostgreSQL, Google Cloud, Pulumi (IaC), Docker, Transbank \& Khipu, Git, Claude Code.}

- Designed and maintain the full-stack architecture (frontend, backend services, database and infrastructure) of a platform in production with real users since 2024.
- Built the payments flow with the Transbank (Webpay) and Khipu gateways: checkout, payment confirmation and transaction reconciliation, including the asynchronous callbacks each gateway returns.
- Built the first mobile interface in React Native with reusable components shared across screens, then migrated the frontend to Flutter without changing the backend contract.
- Designed and integrated REST APIs of external services (Google Maps: Directions, Distance Matrix, Geocoding) for route and distance calculation.
- Automated cloud infrastructure as code with Pulumi on Google Cloud, with deployments through an automated pipeline.
- Use Claude Code (Max plan) as primary development harness — spec, plan review, execution and verification — and integrate cost-effective LLMs to keep the pipeline affordable. Earlier experience with the Pi.dev and opencode agent harnesses.

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient — Caterpillar}
\stack{Java 21 (Spring Boot), REST APIs, SQL, Git, agile methodologies.}

- Developed and maintained REST APIs of Caterpillar's global e-commerce system, consumed by several front ends of the platform.
- Worked under Scrum in a team distributed across the USA, India and Latin America: user-story refinement, code reviews and daily technical coordination in English.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}
\stack{Java, Spring, Oracle SQL, Jenkins, Git, Gradle, WebSphere, Jira, Confluence.}

- Delivered monthly change requests on the bank's internal Java/Spring framework, and built and maintained reports for internal clients.
- Migrated a financial database from Sybase to Oracle (over 15 million records, no data loss) with a multicultural team across the USA, Ukraine, India and Chile.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), JavaScript, jQuery, Vuetify, Bootstrap, PostgreSQL 9.6, Google Cloud, GitLab CI.}

- Designed and built the Healthcare Management System full stack: web interface with reusable components and a REST API backend, used daily by clinical staff.
- Built the transactional payments module and the administrative PDF reporting, integrated through internal APIs.
- Led 4 developers (frontend and backend) technically: code review through GitLab merge requests, branching strategy and development standards.

\rol{UX/UI Designer \& Full Stack Developer}{2014 – 2017}
\org{Nubox Electronic Invoicing}
\stack{React, HTML, SASS/CSS, jQuery.}

- Set and supervised the UI guidelines for the new generation of Nubox applications, implementing the front-end views in React with reusable components.
- Built the new website for Colombia and its accounting reporting, and made the site compatible country-wide with Chrome.

\rol{Systems Analyst (Banking) \textperiodcentered\ Analyst \& Developer \textperiodcentered\ Software Engineering}{2000 – 2016}
\org{Santander / Isban \textperiodcentered\ Cencosud S.A. \textperiodcentered\ Portal Inmobiliario}

- 17 years in the financial sector on loans, payment methods, current accounts and credit cards for Chile, Puerto Rico, Colombia, Uruguay and Venezuela: electronic invoicing, banking migrations (AS/400 to Java) and incident resolution on transactional systems.
- Stock-management web software for the Cencosud supermarket chain, and reporting with SQL Server Reporting Services at Portal Inmobiliario.

# Featured Public Project

**Shift-report application — Next.js 14 + NestJS (TypeScript end to end)** — github.com/goviedodev/niuro

- Frontend in Next.js 14 (App Router) with React 18 and TypeScript: user session, controlled forms from reusable components, and a typed `fetch` wrapper that normalises per-field validation errors.
- Decoupled NestJS 10 + TypeScript (Node.js) backend consumed through REST APIs, layered architecture, global `ValidationPipe` and unit tests in Jest.
- JWT authentication and authorisation with two roles; record authorship taken from the token, never from the form payload. Asynchronous export process to a data lake.
- Multi-stage Docker builds and the same CI/CD pipeline on both GitHub Actions and Azure Pipelines.

# Technical Skills

- **Frontend:** React 18, TypeScript, JavaScript (ES6+), React Native, Next.js, component architecture, reusable and scalable components, state management (Context API), Vue.js/Nuxt, Vuetify, HTML/SASS/CSS, performance and optimisation.
- **Backend & APIs:** Node.js (NestJS), TypeScript, Java 21 (Spring Boot), REST API design, decoupled business logic, event handling and asynchronous processes, external service integration, microservices.
- **Cloud & serverless:** Google Cloud Platform (production cloud), AWS Lambda and S3, Pulumi (infrastructure as code), Docker (multi-stage builds).
- **DevOps & CI/CD:** Git and branching strategies, GitLab CI/CD, GitHub Actions, Azure Pipelines, Jenkins, deployment automation and release management.
- **Testing & quality:** Jest, JUnit, unit and integration tests, code review / merge requests, incident resolution, application logging and monitoring.
- **Security:** JWT and OAuth2 authentication and authorisation, server-side validation, secrets management outside source control, least privilege, secure development for transactional financial systems.
- **Databases:** PostgreSQL, Oracle PL/SQL, MySQL, SQL Server (relational); MongoDB (NoSQL); data modelling.
- **Payments & fintech domain:** payment gateway integration (Transbank Webpay, Khipu), checkout, payment confirmation and transaction reconciliation, electronic invoicing, core banking.
- **AI-assisted development:** Claude Code (Max plan) as primary development harness — spec → plan → execute → verify, with full technical understanding and review of every generated solution before it merges; previous experience with Pi.dev and opencode.

# Education & Languages

**Engineering in Computer Science and Informatics** — Universidad del Bío-Bío, Concepción (2005 – 2009). Thesis: Extreme Programming (XP), theory and practice.

Native Spanish. English B2, in continuous professional use since 2021 with teams in the USA, India and Ukraine.

**Core competencies:** assertive communication and teamwork (constant collaboration with the mobility platform team and daily coordination in English with distributed teams at Caterpillar and Citibank); analytical thinking and problem solving (applied daily to that architecture and to incident resolution on banking transactional systems); results orientation, planning and organisation, and initiative (two projects carried end to end: the mobility platform, built from scratch, and Seven IT's Healthcare Management System); innovation and continuous improvement (adoption of coding agents as part of the development flow); ability to learn (from Java 8 to 21, and onward to React, TypeScript and Node.js); customer orientation (user-story refinement before implementing); and the ability to work in dynamic, highly collaborative environments (multicultural teams at Perficient/Caterpillar and Citibank across the USA, India, Ukraine and Latin America).
