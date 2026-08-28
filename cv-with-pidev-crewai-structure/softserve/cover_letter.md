# Cover Letter — SoftServe, Senior Full Stack Software Engineer (Next.js, React, Python), req. 88952

Dear SoftServe Hiring Team,

I am applying for the Senior Full Stack Software Engineer position (Next.js, React, Python) supporting your Energy, Oil & Gas client. I have spent 15+ years building and operating business-critical systems end to end, and the combination in this role — a React/Next.js frontend over Python and Node backend services, deployed on AWS, feeding data processing that people actually make operational decisions from — is the work I do best.

**Frontend: React, Next.js, TypeScript.** The clearest sample is public: [github.com/goviedodev/niuro](https://github.com/goviedodev/niuro/tree/main/frontend/app/login). It is a Next.js 14 App Router application (React 18, TypeScript) I designed and built to replace an industrial shift-report spreadsheet with a validated, traceable web app that exports to a Databricks data lake. The login flow linked above shows how I structure client components, controlled forms, and error handling: a single typed `fetch` wrapper owns the bearer token, surfaces per-field server validation messages, and forces a logout on 401. The backend is NestJS + TypeScript with JWT (HS256) and operator/supervisor roles, where record authorship comes from the token rather than the payload. It ships with Jest tests, multi-stage Docker builds, and the same pipeline implemented in both GitHub Actions and Azure Pipelines.

**Python.** Python is my daily utility language: data cleanup and processing, log and report pipelines, deployment and integration scripts, and the internal tooling around the platform I currently run. I am not coming to Python cold on this role.

**Backend, APIs, auth, and databases.** I have designed and shipped REST APIs and backend services throughout my career — Spring Boot at Caterpillar's global e-commerce platform, NestJS more recently — with JWT authentication and role-based authorization in production. On the data side I have deep relational experience (PostgreSQL, Oracle PL/SQL, MySQL, SQL Server) including a Sybase-to-Oracle migration of 15M+ financial records at Citibank with zero data loss, plus MongoDB on the NoSQL side.

**One honest gap: GraphQL.** I have not shipped a GraphQL API in production. What I do have is a lot of experience with the problems GraphQL exists to solve — API contract design, over- and under-fetching, versioning, and typed client-server boundaries — and I work in a strongly typed TypeScript codebase every day. I would expect to be productive with Apollo or a similar stack quickly, and I would rather tell you this up front than have it come out in the technical interview.

**Cloud and delivery.** My primary cloud is Google Cloud (Cloud Run serverless, infrastructure fully automated with Pulumi), with AWS Lambda experience and Docker and CI/CD pipelines as a daily routine — GitHub Actions, Azure Pipelines, Jenkins, GitLab CI. The concepts transfer directly to AWS, and I am comfortable owning deployment and monitoring for what I build.

**AI-assisted development.** This is a real strength rather than a checkbox for me. I started with GitHub Copilot and now use Claude Code every day for implementation, debugging, and refactoring. I also designed the agent harness my team works in — defined skills and commands running a spec to plan to execute to verify cycle, with the automated test suite as the merge gate, and prompts and agent configs kept under version control like any other artifact.

**Team and time zone.** I have worked in English-speaking distributed teams since 2017 — at Citibank alongside engineers in the US, **Ukraine**, India and Chile, and at Perficient/Caterpillar across the US, India and Latin America. My English is upper-intermediate for daily written and spoken work. I am based in Chile at GMT-4, which gives me a full working-day overlap with US Eastern Time and a workable morning overlap with Ukraine.

I would welcome the chance to talk through the platform's architecture and where you need this role to have the most impact.

Best regards,

Gonzalo Oviedo Lambert
goviedo.laboral@gmail.com | +56 9 6372 3603
Limache, Valparaiso Region, Chile (GMT-4)
linkedin.com/in/gol | github.com/goviedodev
