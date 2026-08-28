# Application answers — ProntoPaga (Full-Stack Engineer, Semi Senior)

> The posting states **"Requires applying in English"**, so every text below is written in English and ready to paste into the Get on Board form.

---

## Cover letter (main field of the application)

I'm applying to the Full-Stack Engineer role at ProntoPaga because the position sits exactly where my two strongest lines of work meet: full-stack development in React and TypeScript, and payments.

Payments is not a new domain for me. I spent 17 years at Santander/Isban working on loans, payment methods, current accounts and credit cards across Chile, Puerto Rico, Colombia, Uruguay and Venezuela, followed by Citibank. More recently, in the mobility platform I lead technically, I built the payments flow against the Transbank (Webpay) and Khipu gateways end to end — checkout, payment confirmation and transaction reconciliation, including the asynchronous callbacks each gateway sends back. Collection and dispersion of payments, idempotency of a confirmation that arrives twice, and reconciling what the gateway says against what your own system recorded are problems I have already had to solve in production.

On the frontend, React and TypeScript are what I work with. I implemented the front-end views of the new generation of Nubox's electronic invoicing applications in React, built the first mobile interface of the mobility platform in React Native with reusable components shared across screens, and my most recent TypeScript project is public: github.com/goviedodev/niuro, a Next.js 14 + React 18 frontend against a decoupled NestJS backend, with JWT authentication, server-side validation, Jest tests, multi-stage Docker builds and the same CI/CD pipeline running on both GitHub Actions and Azure Pipelines.

I also want to be straightforward about where I don't match the posting, because you will find out in the first technical interview anyway. My production cloud is Google Cloud, automated as code with Pulumi. On AWS I have worked with Lambda and S3, but I have not designed and operated a full serverless architecture on AWS in production, and I have no experience modelling data in DynamoDB — my NoSQL background is MongoDB, and my depth in data modelling is relational (PostgreSQL, Oracle). Those are the two gaps. Everything else the posting asks for — REST API design, event handling and asynchronous processes, CI/CD, infrastructure as code, Git branching strategies, containers, OWASP Top 10, secrets management, least privilege, JWT/OAuth2 — is work I do today. I've moved between stacks repeatedly across my career (AS/400 to Java, Java 8 to 21, Spring Boot to NestJS), and the concepts behind serverless — decoupled business logic, event orchestration, statelessness, observability — are the same ones I already apply.

One last point, since the posting raises it explicitly: I use generative AI as part of my development flow — Claude Code (Max plan) is my primary harness, in a spec → plan → execute → verify loop. I write the specification, review the plan before any code is generated, and read and own every line that merges. I don't ship code I can't explain. That is precisely the distinction your posting draws, and it's why I'm comfortable applying to a role that names it.

Gonzalo Oviedo Lambert
goviedo.laboral@gmail.com · +56 9 6372 3603 · linkedin.com/in/gol

---

## Answers to likely screening questions

### 1. Tell us about your professional experience and profile

I'm a full-stack engineer with over 15 years of experience, currently Tech Lead of a mobility platform in production on Google Cloud, where I designed the whole architecture: React Native frontend (later migrated to Flutter), Java 21 / Spring Boot backend services, PostgreSQL, and infrastructure as code with Pulumi. Within that platform I built the payments module against the Transbank (Webpay) and Khipu gateways.

Before that: REST APIs for Caterpillar's global e-commerce at Perficient, under Scrum with teams in the USA, India and Latin America; Java Specialist at Citibank, where I migrated a financial database from Sybase to Oracle (over 15 million records, no data loss); and Tech Lead at Seven IT, where I built a healthcare management system full stack — including its transactional payments module — leading 4 developers through code review in GitLab. My React background goes back to 2014–2017 at Nubox, and my current TypeScript/Node work is public in github.com/goviedodev/niuro.

### 2. Tell us about your academic background

I hold a degree in Engineering in Computer Science and Informatics from Universidad del Bío-Bío (Concepción, 2005–2009). My thesis was on Extreme Programming — theory and practice, which was an unusual topic for the programme at the time and ended up shaping how I work: iterative, with automated tests as the quality gate and frequent delivery.

Since then I've kept learning on my own: Java 8 through 21, TypeScript with React and NestJS in my own projects, cloud-native architecture, and more recently AI agent workflows applied to production software development.

### 3. Why do you want to work at ProntoPaga?

Because it's a payments company, and payments is the domain I know best. Fast collection and dispersion for merchants is a problem with real constraints — latency, idempotency, reconciliation, local payment methods that each behave differently — and I've worked those constraints from the bank side (Santander/Isban, Citibank), from the merchant side (Transbank and Khipu integration), and from the invoicing side (Nubox). I'd rather work on a product where the technical difficulty is genuine and the correctness of a transaction actually matters than on a generic CRUD platform.

The stack is the second reason. React and TypeScript are what I build with today, and AWS serverless is the one part I'd be learning on the job — which I'd rather say out loud than discover in the interview.

### 4. Describe a full-stack solution you built with React/TypeScript and Node.js. How did you design the frontend–backend–API integration, and what decisions ensured scalability, security and maintainability?

I built an application to replace an industrial shift-report spreadsheet with a traceable web system that exports to a data lake (public: github.com/goviedodev/niuro). Frontend in Next.js 14 (App Router) with React 18 and TypeScript; backend in NestJS 10 with TypeScript, exposed as a REST API.

**Frontend–backend integration.** All frontend traffic goes through a single typed `fetch` wrapper (`lib/api.ts`) that adds the base URL, attaches the Bearer token, and translates backend validation errors (the per-field message arrays from the global `ValidationPipe`) into readable UI text. One contact point with the API instead of scattered calls across components.

**Scalability.** Persistence sits behind a Repository interface, with the exact swap point for TypeORM/Prisma + PostgreSQL documented so services and controllers don't change. Authentication is stateless JWT, which lets the backend scale horizontally without shared session state. Docker builds are multi-stage: dev dependencies in the build layer, a minimal runtime image with a non-privileged user.

**Security.** Server-side validation with `class-validator` and a global `ValidationPipe` (`whitelist` + `forbidNonWhitelisted`, so any undeclared field is stripped and rejected); authentication and role guards evaluated on the server — the UI merely hides the export button, but the backend still returns 403 if the call is forced; the author of each record is taken from the JWT, never from the form payload; and the login error message is generic so users can't be enumerated. Secrets live in environment variables, outside version control.

**Maintainability.** Modular structure by domain (auth, records, ingestion), Jest unit tests on the two critical services, and the same CI/CD pipeline running in parallel on GitHub Actions and Azure Pipelines (build + test of frontend and backend). The demo's limits versus a production environment — file persistence instead of a database, `.env` instead of a secrets manager — are documented in the code itself rather than hidden.

### 5. What is your experience with AWS serverless and DynamoDB?

This is my main gap and I'd rather state it plainly. My production cloud is Google Cloud, automated with Pulumi as infrastructure as code, with Docker containers and automated deployment pipelines. On AWS I have used Lambda and S3, but I haven't designed and operated a complete serverless architecture — API Gateway, Lambda, DynamoDB, event orchestration — in production. I have no DynamoDB experience; my NoSQL work is MongoDB, and my data modelling depth is relational (PostgreSQL, Oracle PL/SQL, SQL Server).

What I do bring is everything around it: decoupled business logic, REST API design, asynchronous and event-driven processing (the payment-gateway callbacks I handle today are exactly that), infrastructure as code, CI/CD, and logging and monitoring in production. Single-table design in DynamoDB is a real shift from relational modelling and I'd treat it as something to study deliberately rather than assume it transfers.

### 6. How do you use AI in your development work?

Claude Code (Max plan) is my primary development harness, and I use it under a fixed loop: I write the specification, review the generated plan before any code exists, execute, then verify against tests and my own reading of the diff. I've also designed agent lifecycles — skills, commands, workflows — on the Pi.dev and opencode harnesses, and integrated cheaper LLMs where the task doesn't need a frontier model, to keep the cost of the pipeline sustainable.

The part that matters for your posting: I don't merge code I can't explain. AI accelerates the typing and the exploration; the architecture decisions, the security review and the responsibility for what reaches production stay with me. When something breaks at 2 a.m., there is no harness to delegate to — you either understand the system or you don't.

### 7. Salary expectations

The posting's published range is USD $2,000 – $3,000 gross per month. I'm aligned with that range.
