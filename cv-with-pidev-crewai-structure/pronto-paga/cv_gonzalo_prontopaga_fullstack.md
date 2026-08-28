---
lang: en
colorlinks: true
urlcolor: black
linkcolor: black
header-includes: |
  ```{=latex}
  \usepackage{enumitem}
  \geometry{top=1.2cm,bottom=1.3cm,left=1.5cm,right=1.5cm}
  \setlist[itemize]{leftmargin=1.1em,itemsep=1pt,topsep=2pt,parsep=0pt}
  \setlength{\parskip}{0.25em}
  \linespread{0.98}
  ```
---

**Gonzalo Oviedo Lambert**
*Full-Stack Engineer — React · TypeScript · REST APIs · Cloud & CI/CD*
Valparaíso Region / Santiago Metropolitan Region, Chile (GMT-4)
[goviedo.laboral@gmail.com](mailto:goviedo.laboral@gmail.com) · +56 9 6372 3603
[linkedin.com/in/gol](https://www.linkedin.com/in/gol) · [github.com/goviedodev](https://github.com/goviedodev) · Native Spanish · English B2

## Professional Summary

Full-stack engineer with over 15 years building and running software end to end: React and TypeScript interfaces with reusable, scalable components, decoupled backend services and REST APIs, automated testing, code review and CI/CD. Most of my career has been in payments and financial systems — 17 years at Santander/Isban on loans, payment methods, current accounts and credit cards, then Citibank, and more recently the Transbank (Webpay) and Khipu payment-gateway integration of a mobility platform in production — so collection, dispersion and transaction reconciliation are familiar ground, as are the secure-development standards a fintech requires (JWT authentication and authorisation, secrets kept out of source, least privilege, server-side validation). I use Claude Code daily as my primary development harness, under a spec → plan → execute → verify flow where I read, review and own every line that ships — never unsupervised generation.

## Professional Experience

**Tech Lead** | *Mobility Startup — Chile* | 2024 – Present
Stack: React Native, TypeScript, Java 21 (Spring Boot), Flutter, PostgreSQL, Google Cloud, Pulumi (IaC), Docker, Transbank & Khipu payment gateways, Git, Claude Code.

- Designed and maintain the full-stack architecture (frontend, backend services, database and infrastructure) of a platform in production with real users since 2024.
- Built the payments flow with the Transbank (Webpay) and Khipu gateways: checkout, payment confirmation and transaction reconciliation, including the asynchronous callbacks each gateway returns.
- Built the first version of the mobile interface in React Native with reusable components shared across screens, then migrated the frontend to Flutter without changing the backend contract.
- Designed and integrated REST APIs of external services (Google Maps: Directions, Distance Matrix, Geocoding) for route and distance calculation.
- Automated cloud infrastructure as code with Pulumi on Google Cloud, and run deployments through an automated pipeline.
- Use Claude Code (Max plan) as the primary development harness — writing the spec, reviewing the plan, executing and verifying — and integrate cost-effective LLMs to keep the pipeline affordable. Earlier experience with the Pi.dev and opencode agent harnesses.

**Java Associate Developer** | *Perficient — Caterpillar* | 2022 – 2023
Stack: Java 21 (Spring Boot), REST APIs, SQL, Git, agile methodologies.

- Developed and maintained REST APIs of Caterpillar's global e-commerce system, consumed by several front ends of the platform.
- Worked under Scrum in a team distributed across the USA, India and Latin America: user-story refinement, code reviews and daily technical coordination in English.

**Java Specialist** | *Citibank* | 2021 – 2022
Stack: Java, Spring, Oracle SQL, Jenkins, Git, Gradle, WebSphere, Jira, Confluence.

- Delivered monthly change requests on the bank's internal Java/Spring framework, and built and maintained reports for internal clients.
- Migrated a financial database from Sybase to Oracle (over 15 million records, no data loss) with a multicultural team across the USA, Ukraine, India and Chile.

**Tech Lead** | *Seven IT SpA — Hospital Cruz del Norte, SQM* | 2017 – 2020
Stack: Spring Boot (REST, MVC), JavaScript, jQuery, Vuetify, Bootstrap, PostgreSQL 9.6, Google Cloud (VM), GitLab CI.

- Designed and built the Healthcare Management System full stack (medicine, nursing, physiotherapy): web interface with reusable components and a REST API backend, used daily by clinical staff.
- Built the transactional payments module and the administrative PDF reporting integrated with the rest of the system through internal APIs.
- Led 4 developers (frontend and backend) technically: code review through GitLab merge requests, branching strategy and development standards — the hands-on technical leadership this role asks for.

**UX/UI Designer & Full Stack Developer** | *Nubox Electronic Invoicing* | 2014 – 2017
Stack: React, HTML, SASS/CSS, jQuery.

- Set and supervised the UI guidelines for the new generation of Nubox applications, implementing the front-end views in React with reusable components.
- Built the new website for Colombia and its accounting reporting: business reports per requirement and site interaction.
- Made the site compatible country-wide with Chrome, widening access to the electronic invoicing platform.

**Systems Analyst, Banking** | *Santander / Isban* | 2000 – 2017 · **Analyst & Developer** | *Cencosud S.A.* | 2015 – 2016 · **Software Engineering** | *Portal Inmobiliario* | 2008 – 2016

- 17 years in the financial sector on loans, **payment methods**, current accounts and credit cards, serving Chile, Puerto Rico, Colombia, Uruguay and Venezuela: electronic invoicing, banking migrations (AS/400 to Java) and incident resolution on transactional systems.
- Stock-management web software for the Cencosud supermarket chain and reporting with SQL Server Reporting Services at Portal Inmobiliario.

## Featured Public Project

**Shift-report application — Next.js 14 + NestJS (TypeScript end to end)** — [github.com/goviedodev/niuro](https://github.com/goviedodev/niuro)

Full-stack application I designed and built to replace an industrial operations spreadsheet with a structured, traceable web app.

- Frontend in Next.js 14 (App Router) with React 18 and TypeScript: user session, controlled forms built from reusable components, and a typed `fetch` wrapper that normalises per-field validation errors.
- Decoupled backend in NestJS 10 + TypeScript (Node.js) consumed through REST APIs, layered architecture, global `ValidationPipe` and unit tests in Jest.
- Authentication and authorisation with JWT and two roles; record authorship is taken from the token, never from the form payload.
- Asynchronous export process to a data lake (JSONL + Databricks Files API).
- Multi-stage Docker builds and the same CI/CD pipeline implemented on both GitHub Actions and Azure Pipelines.

## Technical Skills

- **Frontend:** React 18, TypeScript, JavaScript (ES6+), React Native, Next.js, component architecture, reusable and scalable components, state management (Context API), Vue.js/Nuxt, Vuetify, HTML/SASS/CSS, performance and optimisation.
- **Backend & APIs:** Node.js (NestJS), TypeScript, Java 21 (Spring Boot), REST API design and development, decoupled business logic, event handling and asynchronous processes, external service integration, microservices.
- **Cloud & serverless:** Google Cloud Platform (production cloud: Compute, automated deployments), AWS Lambda and S3, Pulumi (infrastructure as code), Docker (multi-stage builds).
- **DevOps & CI/CD:** Git and branching strategies, GitLab CI/CD, GitHub Actions, Azure Pipelines, Jenkins, deployment automation and release management.
- **Testing & quality:** Jest, JUnit, unit and integration tests, code review / merge requests, continuous improvement, incident resolution, application logging and monitoring.
- **Security:** JWT and OAuth2 authentication and authorisation, server-side validation, secrets management outside source control, least privilege, secure development practices for transactional financial systems.
- **Databases:** PostgreSQL, Oracle PL/SQL, MySQL, SQL Server (relational); MongoDB (NoSQL); data modelling.
- **Payments & fintech domain:** payment gateway integration (Transbank Webpay, Khipu), checkout, payment confirmation and transaction reconciliation, electronic invoicing, core banking (loans, payment methods, current accounts, credit cards).
- **AI-assisted development:** Claude Code (Max plan) as primary development harness — spec → plan → execute → verify, with full technical understanding and review of every generated solution before it merges; previous experience with the Pi.dev and opencode agent harnesses.

## Education & Languages

**Engineering in Computer Science and Informatics** — Universidad del Bío-Bío, Concepción (2005 – 2009). Thesis: Extreme Programming (XP), theory and practice.

Native Spanish. English B2, in continuous professional use since 2021 with teams in the USA, India and Ukraine.

**Core competencies:** assertive communication and teamwork (constant collaboration with the mobility platform team and daily coordination in English with distributed teams at Caterpillar and Citibank); analytical thinking and problem solving (applied daily to the design of that architecture and to incident resolution on banking transactional systems); results orientation, planning and organisation, and initiative (two projects carried end to end: the mobility platform, built from scratch, and Seven IT's Healthcare Management System); innovation and continuous improvement (adoption of coding agents as part of the development flow); ability to learn (from Java 8 to 21, and onward to React, TypeScript and Node.js); customer orientation (user-story refinement before implementing); and the ability to work in dynamic, highly collaborative environments (multicultural teams at Perficient/Caterpillar and Citibank across the USA, India, Ukraine and Latin America).
