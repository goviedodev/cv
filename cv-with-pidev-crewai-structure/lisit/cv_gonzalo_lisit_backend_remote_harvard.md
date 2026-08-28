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
  \fancyfoot[C]{\small Gonzalo Oviedo Lambert\quad\textbar\quad Page \thepage}
  ```
---

\begin{center}
{\Huge\bfseries Gonzalo Oviedo Lambert}\\[4pt]
{\large Backend Developer --- Node.js/NestJS, PostgreSQL}\\[6pt]
{\small Current: Limache, Chile (GMT-4) \textbar\ Relocation: open to Santiago \textbar\ also fully remote worldwide \textbar\ +56 9 6372 3603}\\[2pt]
{\small goviedo.laboral@gmail.com \textbar\ linkedin.com/in/gol \textbar\ github.com/goviedodev \textbar\ English B2}
\end{center}
\vspace{0.4em}

# Professional Summary

Backend engineer with 15+ years shipping production systems on PostgreSQL, including two large-scale data migrations with zero data loss. I build backend services in Node.js/TypeScript (NestJS) and Java/Spring Boot, and currently own the backend architecture of a mobility platform live in production, where coordinate data and third-party geolocation APIs are daily work. I designed the agent-harness workflow (spec $\rightarrow$ plan $\rightarrow$ execute $\rightarrow$ verify, gated by automated tests) my team runs on with Claude Code.

# Technical Skills

- **Backend:** Node.js/TypeScript (NestJS, layered architecture), Java 8--21 (Spring Boot), REST APIs, JWT auth.
- **PostgreSQL:** schema design, indexing, query tuning, large-scale migrations. Also Oracle PL/SQL, MySQL, SQL Server, MongoDB.
- **Migration / ETL:** moving large volumes between engines, integrity validation, reconciliation.
- **Geospatial:** coordinate-based systems via Google Maps APIs in a production mobility platform --- no production PostGIS experience (see note below).
- **CI/CD \& DevOps:** Git, GitLab CI, GitHub Actions, Azure Pipelines, Docker, Google Cloud (Cloud Run), Pulumi IaC.
- **AI-assisted development:** Claude Code (daily driver), agent-harness design (Pi.dev, opencode).

**Honest notes on this role's stack:** PostGIS/spatial queries --- coordinates in the mobility platform are handled via Google Maps APIs, not native PostGIS geometries. Kong API Gateway --- no hands-on experience. Keycloak --- experimented outside production only (production auth experience is JWT/OAuth2, see NestJS project below). Containers --- Docker only, no Kubernetes/OpenShift.

# Selected Public Work

\rol{Shift-report web app --- Next.js 14 + NestJS}{github.com/goviedodev/niuro}
\stack{NestJS 10, TypeScript, JWT (HS256), Jest, Docker, GitHub Actions, Azure Pipelines.}

- Backend in NestJS 10 with layered architecture and a global \texttt{ValidationPipe}; unit tests in Jest.
- JWT-based auth with role-based access (operator, supervisor); record authorship taken from the token, never the form payload.
- Docker multi-stage builds; the same CI/CD pipeline implemented in both GitHub Actions and Azure Pipelines.

# Professional Experience

\rol{Tech Lead}{2024 -- Present}
\org{Mobility Startup --- app.tellevoapp.cl}
\stack{Elixir (Phoenix, Ash), Java 21 (Spring Boot), TypeScript, PostgreSQL, Google Cloud, Pulumi, Docker.}

- Own the end-to-end backend architecture of a carpooling platform live in production with real users since 2024.
- Backend logic centers on coordinate data --- pickup/drop-off points, route and distance calculation --- resolved through Google Maps APIs (Directions, Distance Matrix, Geocoding).
- Automated the Google Cloud infrastructure with Pulumi (IaC); workloads run on Cloud Run.
- Designed the team's AI-assisted development workflow: an agent harness (Claude Code) running spec $\rightarrow$ plan $\rightarrow$ execute $\rightarrow$ verify, with the automated test suite as the merge gate.

\rol{Java Developer}{2022 -- 2023}
\org{Perficient --- Caterpillar}
\stack{Java 21, Spring Boot, REST APIs, distributed Agile team.}

- Built and maintained backend services for Caterpillar's global e-commerce platform in a distributed Scrum team across the US, India, and Latin America.

\rol{Java Specialist}{2021 -- 2022}
\org{Citibank}
\stack{Java, Oracle PL/SQL, Spring Beans, Jenkins, Gradle, WebSphere, Git.}

- Migrated the reporting database from Sybase to Oracle --- 15M+ financial records, zero data loss --- with engineers in the US, Ukraine, India, and Chile under a strict regulatory release process.
- Built recurring reporting for internal bank clients on the bank's internal Spring-based framework: data modeling, query tuning, and reconciliation against source systems.

\rol{Tech Lead}{2017 -- 2020}
\org{Seven IT SpA --- Hospital Cruz del Norte (SQM)}
\stack{Spring Boot (REST, MVC), PostgreSQL, Google Cloud (VM), Linux, GitLab.}

- Designed, built, and operated a healthcare management system used daily by clinical staff, owning the PostgreSQL schema through three years of production evolution.
- Introduced GitLab CI/CD and Docker to the release process; led 4 developers through code review and design sessions.

\rol{Java / Senior Developer}{2008 -- 2017}
\org{WebClass, Creasys, Coopeuch and others}
\stack{Java, AS/400, Struts, Hibernate, PostgreSQL, Oracle PL/SQL, SQL Server.}

- Migrated core banking batch processes from legacy AS/400 hosts to Java for Santander, Ripley, and Coopeuch: reverse-engineered the existing process and reimplemented the business logic without stopping operations.
- Wrote queries and stored procedures in PL/SQL and T-SQL for banking and retail reporting.

# Education \& Languages

\rol{Computer Science and Informatics Engineering (B.Eng.)}{Universidad del Bío-Bío, Chile}
\org{Thesis: Extreme Programming (XP), theory and practice.}

**Languages:** Spanish (native) \textbar\ English B2 --- daily use since 2021 with teams in the US, Ukraine, and India.
