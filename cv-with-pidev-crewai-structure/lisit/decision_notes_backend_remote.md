# Decision notes — Lisit / Backend Developer (Remote)

**Date:** 2026-08-26 · **Mode:** direct (URL provided by the user, fetched and parsed).

## Profile chosen

**B — International remote, English.** Fully remote posting ("candidates can reside anywhere in the world"), and the user explicitly asked for English and for both formats (ATS + Harvard). Title mirrors the posting's own title ("Desarrollador Back-end" → "Backend Developer"), per the keyword-mirroring rule, rather than the generic Profile B title suggestion.

## Why this posting is a real fit despite being a Java-heavy master CV

The posting's hard requirement is "Node.js con NestJS (o experiencia sólida en TypeScript backend con arquitectura por capas / hexagonal)." That's not invented for this application — it's real, existing experience already documented in `softserve/cv_gonzalo_softserve_fullstack_nextjs.md` (the public `niuro` project: NestJS 10 + TypeScript, JWT auth, Jest, Docker, dual CI). This CV pulls that project forward as the lead technical proof point instead of leaving it as a secondary skill.

## Mirrored keywords (posting's exact spelling)

`Node.js`/`NestJS` · `TypeScript backend` · `layered architecture` · `PostgreSQL` (modeling, indexing, query tuning) · `Migration / ETL` · `high-concurrency REST APIs` · `pagination` · `GitLab CI` · `JWT` · `PostGIS` · `PL/SQL` · `Docker`. Each critical keyword appears 2–3 times (summary, skills, a project or experience bullet).

## Decisions the user made for this round

| Point | Decision | How it landed |
|---|---|---|
| **PostGIS / geospatial** (desirable) | Highlight the coordinate/mapping work from the Mobility Startup project, but be explicit that spatial queries and geometries were resolved via Google Maps APIs, not native PostGIS | Skills section names it directly as a caveat; a dedicated "Honest Notes" block repeats it so it can't be missed; also declared in the cover message and expandable in the filter-question answers if asked |
| **Kong API Gateway** (desirable) | Not used — declare as a plain gap | Listed in Honest Notes and in the cover message's gap table; not claimed anywhere in the CV |
| **Keycloak** (desirable, paired with OAuth2/JWT) | Only an experiment, not production | Declared as experimental-only; production auth experience is scoped to JWT/OAuth2 via the NestJS project, which is real |
| **Containers** (desirable, paired with Kubernetes/OpenShift) | Docker only | Declared as Docker-only, no Kubernetes/OpenShift claim anywhere |
| **Format** | Both ATS-safe and Harvard style, per explicit user instruction | Two Markdown files generated; Harvard uses the same LaTeX preamble/macros as `3it/` and `generico/cv_gonzalo_oviedo.md` |
| **Language** | English, per explicit user instruction | Both CV files, cover message, and filter-question answers are in English; `job_description_backend_remote.md` stays in the original Spanish as the source record |

## Gap not flagged by the user but caught while building this

**Redis** (part of the excluyente "high-concurrency REST APIs: cache (Redis), pagination, async batch processes" line) — no production Redis use exists anywhere in the CV history for this candidate (checked `cv.md`, `softserve/`, `3it/`; the only file mentioning Redis is an older, non-compliant draft that also carries unverifiable inflated metrics and was not used as a source). Declared as a gap in the cover message, and answered honestly in the filter-question response about autocomplete design (Redis proposed as the right tool, without claiming hands-on production use).

## What was kept because it's verifiable

- Sybase → Oracle migration: 15M+ financial records, zero data loss (Citibank) — matches question 1 directly.
- AS/400 → Java batch migrations for Santander, Ripley, Coopeuch — same migration muscle, older evidence.
- NestJS/TypeScript production code, publicly checkable at github.com/goviedodev/niuro.
- No "CTO"/"Co-founder" anywhere (global restriction #1) — the mobility startup is titled "Tech Lead" throughout.
- Zero self-reported percentage improvements; the only numbers kept are the ones that survive "tell me more about that" (15M+ records, 4 developers led, three years running a PostgreSQL schema in production).

## Pre-existing Lisit application in this repo

`lisit/cv_gonzalo_lisit.md` (2026-05-25) targeted a different, now-presumably-filled posting — "Backend Developer Java + Spring Boot," hybrid in Santiago, coupon platform. That file was left untouched; this round's files carry the `_backend_remote` suffix so nothing gets overwritten or conflated. Worth noting: that older file used the email `gonzalo.oviedo.dev@gmail.com`, which doesn't match the canonical `goviedo.laboral@gmail.com` used everywhere else in this repo — flagging it here in case it's worth a look, out of scope for this round.

## Open risk

The "Node.js con NestJS" requirement is framed as excluyente but with an explicit alternative ("o experiencia sólida en TypeScript backend con arquitectura por capas / hexagonal") — the CV satisfies either reading. The bigger open risk is Redis: it's inside the same excluyente bullet as pagination and async batch processing, and an ATS keyword match on "Redis" will fail. That's a real, disclosed gap, not a formatting problem.

## Status

**Prepared — NOT submitted.** Both CV formats (ATS + Harvard) generated as Markdown and PDF. Submit through the GetOnBoard form, then update `cv_job_links.md` status from "Generado" to "Enviado."
