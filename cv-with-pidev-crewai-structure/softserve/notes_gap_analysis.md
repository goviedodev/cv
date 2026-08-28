# SoftServe req. 88952 — Fit analysis and interview prep

Application date: 2026-08-10 · Role: Senior Full Stack Software Engineer (Next.js, React, Python)

---

## Requirement coverage

| Requirement | Status | Evidence used |
|---|---|---|
| Strong full-stack experience | Covered | Seven IT (backend + browser UI + DB + deploy), TeLlevo, niuro demo |
| 5+ years in Agile teams | Covered | 15+ years; Scrum at Perficient/Caterpillar, Citibank |
| React, Next.js, modern JS, TypeScript | Covered, but thin in paid roles | niuro (Next.js 14 App Router, React 18, TS) is the anchor; Vue/Nuxt, React, Flutter as history |
| Python | Covered as utility/tooling, not as a service backend | Daily scripting, data processing, internal tooling |
| APIs and backend services | Strong | Spring Boot REST at Caterpillar, NestJS, 15 years of API work |
| Authentication / authorization | Covered | JWT HS256 + role-based access in niuro; Spring Security background |
| Relational and/or NoSQL DB design | Strong | PostgreSQL, Oracle PL/SQL, MySQL, SQL Server, MongoDB; 15M-record migration |
| **GraphQL** | **GAP — not in the CV, not shipped in production** | Disclosed openly in the cover letter; not claimed on the CV |
| OOP, automated testing, troubleshooting, perf | Strong | Java/OOP, TDD, Jest/JUnit/Mockito, production ownership |
| AWS cloud-native | Partial | Primary cloud is GCP (Cloud Run, Pulumi IaC); AWS Lambda experience only |
| Docker, CI/CD | Strong | Docker multi-stage, GitHub Actions, Azure Pipelines, Jenkins, GitLab CI |
| Business requirements to technical solutions | Strong | Seven IT requirement sessions with clinical staff; WebClass features that drove sales |
| GitHub Copilot / Claude Code | Strong differentiator | Copilot then Claude Code daily; built the team's agent harness |
| Upper-intermediate English, US timezone | Covered | Since 2017 in US/Ukraine/India teams; GMT-4 = full US Eastern overlap |

## The two real gaps and how they are handled

**1. GraphQL.** Not claimed anywhere on the CV. Disclosed directly in the cover letter along with the adjacent experience that makes it learnable (API contract design, typed TS boundaries). This is deliberate: a fabricated GraphQL claim dies in the first technical screen, and SoftServe screens hard.

*Before the interview, worth doing:* build a small Apollo Server + Next.js slice on top of the existing niuro backend (schema, resolvers, one query and one mutation, auth via the existing JWT). A weekend of work converts "honest gap" into "I did this last week, here is the branch."

**2. AWS depth.** The cloud experience is real but GCP-centric. Frame as: Cloud Run to ECS/Fargate/Lambda, Pulumi already supports AWS as a provider (same tool, different provider), Docker and CI/CD carry over unchanged.

## Angles worth leaning on in the interview

- **Ukraine team overlap.** The Citibank Sybase-to-Oracle migration was executed with engineers in Ukraine. This role's team is US + Ukraine. It is a genuine precedent, not a talking point.
- **Industrial/operational domain.** The niuro demo is literally an industrial operations use case (shift incidents, stoppages, safety observations, structured export to a data lake) and Seven IT served the SQM mining and chemical operation. Both map onto "optimize geophysical workflows" and "data processing components" better than a generic web CV would.
- **AI-assisted development is a listed plus, and it is the strongest single differentiator.** Most candidates will say "I use Copilot." Having designed an agent harness with a spec/plan/execute/verify cycle gated by a test suite is a different conversation.
- **Production ownership.** The role asks for ownership from design through deployment. Every recent role has that shape, including the on-call.

## Files in this folder

| File | Purpose |
|---|---|
| `cv_gonzalo_softserve_fullstack_nextjs.md` / `.pdf` | Tailored CV for this requisition |
| `cover_letter.md` | Application message, includes the GraphQL disclosure |
| `letter_to_recruiter.md` | Direct letter to Fernanda Pardo Muñoz (long + LinkedIn-short versions) |
| `job_description.md` | Archived posting |
| `notes_gap_analysis.md` | This file |

Note: `cv_gonzalo_softserve.md`, `comment.cv` and `cv_gonzalo_softserve.pdf` in this folder are from an earlier, unrelated SoftServe application (BS Junior Java Software Engineer, BEES platform, May 2025). They were left untouched.
