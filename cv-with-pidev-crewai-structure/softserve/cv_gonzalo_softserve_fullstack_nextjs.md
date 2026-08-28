# Gonzalo Oviedo Lambert

**Senior Full Stack Software Engineer — React, Next.js, TypeScript, Python**

- Limache, Valparaiso Region, Chile (GMT-4) — full overlap with US Eastern Time
- goviedo.laboral@gmail.com | +56 9 6372 3603
- [linkedin.com/in/gol](https://www.linkedin.com/in/gol) | [github.com/goviedodev](https://github.com/goviedodev)
- Live product: [app.tellevoapp.cl](https://app.tellevoapp.cl)
- English: upper-intermediate, written and spoken — 6+ years working daily in English-speaking distributed teams (US, Ukraine, India)

---

## Professional Summary

Full stack engineer with 15+ years shipping production systems end to end: requirements, design, implementation, deployment, and the on-call afterwards. I work across the whole stack — React and Next.js (App Router, TypeScript) on the front, Node/TypeScript, Python, and Java on the back, over PostgreSQL, Oracle, and MongoDB.

Most of my career has been spent on business-critical software where downtime is expensive: banking reporting at Citibank, a global e-commerce platform at Caterpillar, hospital records at a mining-sector clinic (SQM). I am comfortable being the person who owns a feature from the design discussion to the production incident.

AI-assisted development is part of how I write code every day — I started with GitHub Copilot and now work primarily in Claude Code, and I built the agent harness my team runs on. I treat generated code the way I treat any other code: it goes through the test suite before it goes anywhere.

---

## Technical Skills

- **Frontend:** React 18, Next.js 14 (App Router, Server/Client Components), TypeScript, modern JavaScript (ES6+), Vue.js/Nuxt, Flutter, HTML/CSS
- **Backend:** Node.js/TypeScript (NestJS), Python (automation, data processing, internal tooling — daily use), Java 8–21 (Spring Boot), Elixir (Phoenix, Ash Framework)
- **APIs & security:** REST API design, JSON Web Token (JWT) authentication, role-based authorization, server-side validation, third-party integrations (payments, electronic invoicing)
- **Databases:** PostgreSQL, Oracle PL/SQL, MySQL, SQL Server, MongoDB — schema design, query tuning, large-scale migrations
- **Cloud & DevOps:** Google Cloud Platform (Cloud Run, serverless), AWS Lambda, Docker (multi-stage builds, docker-compose), Pulumi (Infrastructure as Code), Azure DevOps
- **CI/CD:** GitHub Actions, Azure Pipelines, Jenkins, GitLab CI, Gradle, Git
- **Testing:** Jest, JUnit, Mockito, test-driven development, integration and regression testing
- **AI-assisted development:** Claude Code (daily driver), GitHub Copilot, agent harness design (Pi.dev, opencode) — skills, commands, and a spec to plan to execute to verify cycle, gated by automated tests
- **Practices:** Agile/Scrum, object-oriented design, SOLID, code review, performance troubleshooting

---

## Selected Public Work

**Shift-report web application — Next.js 14 + NestJS** · [github.com/goviedodev/niuro](https://github.com/goviedodev/niuro/tree/main/frontend/app/login)

Full-stack application I designed and built to replace an industrial operations spreadsheet (shift incidents, stoppages, safety observations) with a structured, validated, traceable web app feeding a Databricks data lake.

- Frontend in **Next.js 14 App Router with React 18 and TypeScript**: login and session handling, client components with controlled forms, `useRouter` navigation, and a single typed `fetch` wrapper that attaches the bearer token and normalizes API errors — including per-field validation messages coming back from the server.
- Authentication and authorization with **JWT (HS256)** and two roles (operator, supervisor). Record authorship is taken from the token, never from the form payload, so no one can file a report under someone else's name.
- Backend in **NestJS 10 + TypeScript** with global `ValidationPipe`, unit tests in **Jest**, **Docker** multi-stage builds, and the same pipeline logic implemented twice — **GitHub Actions and Azure Pipelines**.
- Data export to the lake as JSONL through the Databricks Files API (Unity Catalog Volumes).

---

## Professional Experience

### Tech Lead | Mobility Startup — app.tellevoapp.cl | 2024 – Present

*Elixir (Phoenix, Ash), Java 21 (Spring Boot), Flutter, TypeScript, Python, Google Cloud, Pulumi, Docker, Claude Code, Pi.dev*

- Own the end-to-end architecture of a carpooling platform live in production with real users since 2024 — frontend, backend, infrastructure, and releases.
- Designed and built the team's AI-assisted development workflow: an agent harness with defined skills and commands running a spec to plan to execute to verify cycle, with the automated test suite as the merge gate. Prompts and agent configs are versioned like any other source artifact.
- Automated the full Google Cloud infrastructure with Pulumi and moved workloads onto Cloud Run serverless containers to keep operating cost predictable as traffic grew.
- Write Python daily for the surrounding tooling: data cleanup, log and report processing, deployment and scraping utilities, and glue between services.
- Route LLM traffic through a proxy to select cheaper models where evaluation showed no quality regression, and set the engineering standards the team follows (SOLID, code review, clean code).

### Java Developer | Perficient — Caterpillar | 2022 – 2023

*Java 21, Spring Boot, REST APIs, microservices, Agile/Scrum*

- Built and maintained backend services for Caterpillar's global e-commerce platform, working the full feature lifecycle inside a distributed Scrum team across the US, India, and Latin America.
- Worked entirely in English: sprint ceremonies, code reviews, pairing, and written design discussion with stakeholders in other time zones.
- Participated in code review, test automation, and regression testing as part of the definition of done.

### Java Specialist | Citibank | 2021 – 2022

*Java, Oracle SQL, Spring, Jenkins, Gradle, WebSphere*

- Migrated the reporting database from Sybase to Oracle — over 15 million financial records, zero data loss — alongside engineers in the US, **Ukraine**, India, and Chile.
- Built and maintained recurring reporting for internal bank clients, which meant living in SQL: data modeling, query tuning, and reconciliation against source systems.
- Delivered monthly backend features on the bank's internal Spring framework under a strict release, audit, and regulatory process.

### Tech Lead | Seven IT SpA — Hospital Cruz del Norte (SQM) | 2017 – 2020

*Spring Boot (REST, MVC), PostgreSQL, JavaScript, jQuery, Vuetify, Google Cloud, Linux, GitLab*

- Designed, built, deployed, and operated a healthcare management system used daily by clinical staff (medical, nursing, and physiotherapy records) for a clinic serving the SQM mining and chemical operation.
- Full-stack ownership: REST backend, browser UI, PostgreSQL schema, cloud deployment, and production support — plus the payments module and automated PDF reporting for administration.
- Ran requirements sessions directly with clinical and administrative staff and turned them into a working system; mentored a team of 4 developers through code review and design sessions.

### Java / Senior Developer | WebClass, Creasys, Coopeuch and others | 2008 – 2017

*Java, Struts, Hibernate, AS/400, PHP, PostgreSQL, Oracle, SQL Server, Jenkins*

- Full-cycle delivery for banking and ed-tech clients (Santander, Ripley, Coopeuch): requirements analysis, design, implementation, and QA.
- Migrated core banking processes from AS/400 to Java and built electronic invoicing integrations.
- Shipped features on an education platform serving 1,800+ schools and 500k+ daily requests, where new functionality drove additional sales for the product.

---

## Education & Languages

- **Computer Science and Informatics Engineering (B.Eng.)** — Universidad del Bío-Bío, Chile. Thesis: Extreme Programming (XP), theory and practice.
- **Spanish:** native. **English:** upper-intermediate — daily written and spoken use since 2017 in distributed teams across the US, Ukraine, and India.
- **Time zone:** GMT-4, full working-day overlap with US Eastern Time and partial overlap with Ukraine.
