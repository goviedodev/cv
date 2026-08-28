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
{\large Agentic Software Engineer · GitHub Copilot · AI-First Development Workflows · Full-Stack (Java, Elixir, React, Node)}\\[6pt]
{\small Villa Baviera S/N, Parcela 77, Bulnes, Región del Biobío, Chile (GMT-4) · Available for 100\% remote work, Latin America}\\[2pt]
{\small goviedo.laboral@gmail.com · +56 9 6372 3603 · linkedin.com/in/gol}\\[2pt]
{\small Chilean citizen, authorized to work full-time in Chile — no visa sponsorship required · English: professional working proficiency}
\end{center}
\vspace{0.4em}

# Professional Summary

Software engineer with 15 years of experience building production systems for banking, healthcare and high-traffic education platforms, working AI-first since 2024. In the systems I ship today, most of the implementation code is written by coding agents under my architectural direction: I use GitHub Copilot, Claude Code, Pi.dev and opencode as my primary development environment, and I run every feature through a specification, plan, execute and verify loop with an automated test suite as the merge gate.

I designed the agent lifecycle my team uses — skills, commands and workflows defined as files inside the repository — and I write the specifications, repository structure and context documents that make agent output reliable across large, multi-file codebases. I review every AI-generated diff before merge and apply heavier validation on the flows where a defect costs money or data. I work end to end: frontend, backend, and infrastructure as code.

# Technical Skills

- **Agentic AI engineering:** GitHub Copilot, Claude Code, Pi.dev, opencode, Windsurf. Context engineering: repository and codebase structuring for agent consumption, machine-executable specifications, agent instruction files (skills, commands, workflows), documentation written for context-efficient AI output.
- **AI-first delivery practices:** specification-to-deployment workflows, human-in-the-loop code review, risk-adjusted validation of high-impact flows, structured iteration and feedback loops over agent output, automated test suites as quality gates.
- **Backend:** Java (1.8 to 21), Spring Boot, Elixir, Phoenix, Ash Framework, Node.js, RESTful Application Programming Interfaces (APIs), microservices, Object-Oriented Programming (OOP).
- **Frontend:** React, Vue.js, Nuxt, JavaScript (ES6+), TypeScript, Phoenix LiveView, Flutter.
- **Databases:** PostgreSQL, Oracle PL/SQL, MySQL, MongoDB.
- **Cloud and infrastructure:** Google Cloud Platform (Cloud Run, Compute Engine), Pulumi (Infrastructure as Code), Docker, GitLab CI/CD, Jenkins, Azure DevOps, Amazon Web Services (AWS) Lambda.
- **Methodologies:** Agile/Scrum, Lean, Test-Driven Development (TDD), code review, asynchronous work in distributed teams.

# Professional Experience

\rol{Tech Lead and Agentic Software Engineer}{2024 – Present}
\org{TeLlevoApp (mobility startup) — Remote}
\stack{GitHub Copilot, Claude Code, Pi.dev, opencode, Elixir, Phoenix LiveView, Ash Framework, Java 21 (Spring Boot), Flutter, PostgreSQL, Google Cloud, Pulumi, Docker.}

- **Architectural oversight over AI-generated code:** deliver production software in which coding agents generate the majority of the implementation code, while I define the module boundaries, the domain model and the acceptance criteria before any agent writes a line.
- **AI-first workflow from specification through deployment:** each feature passes a specification, plan, execute and verify cycle, and no agent-written branch merges without a green automated test suite and my review of the diff.
- **Context engineering as a daily task:** repository structure, `AGENTS.md`-style instruction files, per-task skill and command definitions, and specifications written so an agent can execute them across a multi-file codebase without losing the thread.
- **Structured feedback loops:** when a generated implementation misses, I correct the specification and the context files rather than only the code, so the same class of error stops recurring.
- **Risk-adjusted review:** payment, authentication and trip-state flows get manual walkthroughs and extra test cases; low-risk presentation code is validated by the suite alone.
- **Frontend, backend and infrastructure:** Phoenix LiveView and Flutter on the frontend, Elixir and Java services on the backend, Google Cloud automated with Pulumi — and a second product shipped end to end with the same agent workflow, a pharmaceutical price comparator in Phoenix LiveView that searches Chile's main pharmacy chains.

\rol{Java Associate Developer}{2022 – 2023}
\org{Perficient — Caterpillar}
\stack{Java 21, Spring Boot, Agile/Scrum.}

- Developed and maintained modules of Caterpillar's global e-commerce system, working the full cycle from refinement to production support.
- Worked in English inside a distributed Agile team spread across the United States, India and Latin America, taking part in daily ceremonies and asynchronous handovers across time zones.

\rol{Java Specialist}{2021 – 2022}
\org{Citibank}
\stack{Java, Spring, Oracle SQL, Sybase, Jenkins, Gradle, WebSphere, Jira, Git.}

- Executed the migration of financial databases from Sybase to Oracle with no data loss, under banking regulatory controls and on large transactional systems.
- Built and maintained reports and monthly-cycle solutions on an internal Java/Spring framework for internal business clients.
- Coordinated technically in English with engineers in the United States, Ukraine, India and Chile.

\rol{Tech Lead}{2017 – 2020}
\org{Seven IT SpA — Hospital Cruz del Norte, SQM}
\stack{Spring Boot (REST, MVC), PostgreSQL 9.6, Linux, Google Cloud, GitLab, JavaScript, jQuery, Bootstrap, Vuetify.}

- Led the design and delivery of a healthcare management system used daily by clinical staff, covering the medicine, nursing and physiotherapy record modules.
- Built the payment management module and the custom PDF reporting used by hospital administration.
- Ran requirement sessions directly with clinical staff and translated them into technical specifications for the team.
- Led a team of four frontend and backend developers through code reviews and design sessions.

\rol{Java and Senior Developer}{2008 – 2017}
\org{WebClass, Creasys, Coopeuch and others}
\stack{Java, Struts, Hibernate, JSP, AS/400, PostgreSQL, Oracle, SQL Server, PHP, Jenkins, Jira.}

- Full-cycle development for banking, ed-tech and enterprise clients (Santander, Ripley, Coopeuch): requirements analysis, design, development and quality assurance.
- Extended an education platform serving 1,800 schools with features that opened additional sales for the company.
- Led legacy migrations from AS/400 to Java and handled electronic invoicing and incident management.

# Education and Languages

- **Computer Science and Informatics Engineering**, Universidad del Bío-Bío, Chile (four-year university degree). Thesis: Extreme Programming (XP), theory and practice.
- **Languages:** Spanish (native), English (professional working proficiency, used daily in distributed teams since 2017).
