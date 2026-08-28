Gonzalo Oviedo Lambert
Backend Developer — Node.js/NestJS, PostgreSQL

Current: Limache, Valparaíso Region, Chile (GMT-4) | Relocation: open to relocating to Santiago, Metropolitan Region — also available for fully remote work worldwide
goviedo.laboral@gmail.com | +56 9 6372 3603
linkedin.com/in/gol | github.com/goviedodev
Live product: app.tellevoapp.cl
English: upper-intermediate (B2), 6+ years working daily in English-speaking distributed teams (US, Ukraine, India)

## Professional Summary

Backend engineer with 15+ years shipping production systems on PostgreSQL, including two large-scale data migrations with zero data loss. I build backend services in Node.js/TypeScript (NestJS) and Java/Spring Boot, and I currently own the backend architecture of a mobility platform live in production, where coordinate data, PostgreSQL, and third-party geolocation APIs are daily work. AI-assisted development is part of how I write code every day — I designed the agent-harness workflow (spec → plan → execute → verify, gated by automated tests) my team runs on with Claude Code.

## Technical Skills

- **Backend & Languages:** Node.js/TypeScript (NestJS, layered architecture), Java 8–21 (Spring Boot), JavaScript (ES6+), SQL, REST APIs, JWT authentication
- **PostgreSQL:** schema design and modeling, indexing, query tuning, large-scale data migrations; also Oracle PL/SQL (reading and writing), MySQL, SQL Server, MongoDB
- **Data migration / ETL:** moving large volumes between database engines, integrity validation, reconciliation against source systems
- **Geospatial:** coordinate-based systems (pickup/drop-off points, route and distance calculation) resolved through Google Maps APIs in a production mobility platform — no direct production experience with PostGIS spatial queries/geometries (see Honest Notes below)
- **CI/CD & DevOps:** Git, GitLab CI, GitHub Actions, Azure Pipelines, Jenkins, Docker (multi-stage builds), Google Cloud (Cloud Run), Pulumi (IaC)
- **Testing:** Jest, JUnit, Mockito, unit and integration testing, test-driven development
- **AI-assisted development:** Claude Code (daily driver), agent-harness design (Pi.dev, opencode) — skills, commands, and a spec-to-verify cycle gated by automated tests

## Honest Notes on This Role's Stack (read before the interview)

- **PostGIS / geospatial queries:** in the mobility platform, coordinate handling, geocoding, and route/distance calculation are resolved through **Google Maps APIs**, not native PostGIS spatial queries or geometry columns. I have not used PostGIS in production.
- **Kong API Gateway:** no hands-on experience.
- **Keycloak:** experimented with it outside of a production project; no production experience. I do have production JWT/OAuth2 authentication experience (see NestJS project below).
- **Containers:** Docker only — no Kubernetes/OpenShift experience.

## Selected Public Work

**Shift-report web application — Next.js 14 + NestJS** — github.com/goviedodev/niuro

Full-stack application designed and built to replace an industrial operations spreadsheet (shift incidents, stoppages, safety observations) with a structured, validated, traceable web app.

- Backend in **NestJS 10 + TypeScript**, layered architecture, global `ValidationPipe` for request validation, unit tests in **Jest**.
- Authentication and authorization with **JWT (HS256)** and role-based access (operator, supervisor); record authorship is taken from the token, never from the form payload.
- **Docker** multi-stage builds; the same CI/CD pipeline implemented twice, in **GitHub Actions** and **Azure Pipelines**.

## Professional Experience

**Tech Lead** | Mobility Startup — app.tellevoapp.cl | 2024 – Present
*Elixir (Phoenix, Ash), Java 21 (Spring Boot), TypeScript, Flutter, PostgreSQL, Google Cloud, Pulumi, Docker*

- Own the end-to-end backend architecture of a carpooling platform live in production with real users since 2024.
- Backend logic is built around coordinate data — pickup/drop-off points, route and distance calculation between riders and drivers — resolved through Google Maps APIs (Directions/Distance Matrix/Geocoding).
- Automated the Google Cloud infrastructure with Pulumi (IaC) and run workloads on Cloud Run.
- Designed the team's AI-assisted development workflow: an agent harness (Claude Code) running a spec → plan → execute → verify cycle, with the automated test suite as the merge gate.

**Java Developer** | Perficient — Caterpillar | 2022 – 2023
*Java 21, Spring Boot, REST APIs, distributed Agile team*

- Built and maintained backend services for Caterpillar's global e-commerce platform inside a distributed Scrum team across the US, India, and Latin America.

**Java Specialist** | Citibank | 2021 – 2022
*Java, Oracle PL/SQL, Spring Beans, Jenkins, Gradle, WebSphere, Git*

- Migrated the reporting database from Sybase to Oracle — 15M+ financial records, zero data loss — working alongside engineers in the US, Ukraine, India, and Chile under a strict regulatory release process.
- Built and maintained recurring reporting for internal bank clients on the bank's internal Spring-based framework, which meant living in SQL: data modeling, query tuning, and reconciliation against source systems.

**Tech Lead** | Seven IT SpA — Hospital Cruz del Norte (SQM) | 2017 – 2020
*Spring Boot (REST, MVC), PostgreSQL, Google Cloud (VM), Linux, GitLab*

- Designed, built, and operated a healthcare management system used daily by clinical staff, including the PostgreSQL schema and its evolution over three years in production.
- Introduced GitLab CI/CD and Docker to the team's release process; led 4 developers through code review and design sessions.

**Java / Senior Developer** | WebClass, Creasys, Coopeuch and others | 2008 – 2017
*Java, AS/400, Struts, Hibernate, PostgreSQL, Oracle PL/SQL, SQL Server*

- Migrated core banking batch processes from legacy AS/400 hosts to Java for Santander, Ripley, and Coopeuch: reverse-engineered the existing process, designed the target data model, and reimplemented the business logic in Java without stopping operations.
- Wrote queries and stored procedures in PL/SQL and T-SQL for banking and retail reporting.

## Education & Languages

- **Computer Science and Informatics Engineering (B.Eng.)** — Universidad del Bío-Bío, Chile (2005–2009). Thesis: Extreme Programming (XP), theory and practice.
- **Spanish:** native. **English:** upper-intermediate (B2) — daily written and spoken use since 2021 with teams in the US, Ukraine, and India.
