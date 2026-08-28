# Decision notes — Equifax / Senior Developer (My Equifax, D2C)

**Date:** 2026-08-24 · English rendering of `notas_decisiones.md`.

## Language: English (confirmed by Gonzalo)

The posting says "100% English-speaking working environment" and asks for excellent English communication. A Spanish CV would be the first contradiction in the process. Both earlier Equifax applications in this repo (`23people_equifax/`, `23people_equifax_interconnect/`) were also in English.

> Note on the `cv-tailor` skill: it would classify this as profile A (local Chile, CLP → Spanish). The posting overrides the rule; recorded here so it is not read as a mistake.

## Fit: no hard gaps

The strongest match of the recent applications. Every technical requirement is backed by real experience:

| Requirement | Coverage |
|---|---|
| 4+ years Java | 15+ years (1.8 → 21) |
| 4+ years Spring Boot | Since 2017 (Seven IT) through today |
| 4+ years PostgreSQL | Seven IT 2017–2020 + Creasys/WebClass + current platform |
| 4+ years cloud AWS/GCP | GCP since 2017; Pulumi IaC since 2024; AWS Lambda and S3 |
| English B2 | Citibank and Perficient, English-only teams 2021–2023 |
| Degree in Informatics/Systems | Computer Science and Informatics Engineering, Universidad del Bío-Bío, graduated |

**Honest qualifier on cloud:** the strength is **GCP**, not AWS. The posting says "AWS/GCP" with a slash, so GCP satisfies the literal requirement; on AWS only Lambda and S3 are claimed, with no inflation. If the team turns out to be AWS-first, that is the point to raise in the interview.

## Professional summary — `ai_expert_redactor_for_recruters` agent

Applied the same way as in `michael-page/`: 40–50 words, 3–4 lines, scannable in 7 seconds. No "CTO"/"Co-founder" (Global Constraint #1, which overrides the agent's own template example).

### Option A — Domain and impact ✅ **APPLIED** (43 words)
> Senior backend developer, 15+ years in Java and Spring Boot. Built transactional systems for banking (Citibank), global e-commerce (Caterpillar) and healthcare on PostgreSQL, deployed on GCP and AWS. Six years working daily in English with distributed teams across the US, India and Ukraine.

Three recognisable names (Citibank, Caterpillar, PostgreSQL) plus the English evidence in the same line.

### Option B — Requirement mirror (43 words)
> Java and Spring Boot backend developer with 15+ years, well past the 4+ this role asks for. PostgreSQL since 2017 — schema design, queries, stored procedures — and cloud since then too: GCP with Pulumi IaC, plus AWS Lambda and S3. Daily stand-ups in English.

Answers the checklist item by item. Better if the first filter is an ATS scoring on keywords.

### Option C — Self-management (46 words)
> Senior backend developer, 15+ years in Java and Spring Boot. I own services end to end — schema on PostgreSQL, REST layer, deployment to GCP and AWS — and have done it inside regulated banking and global e-commerce teams, working in English with people in three time zones.

Goes straight at the "self-management" item in the personal-skills block.

## What was corrected relative to the InterConnect CV (July)

`23people_equifax_interconnect/cv_gonzalo_equifax_interconnect.md` contains "acceleration of up to **300%**" and "peaks above **2000%**", now banned by Global Constraint #3 (verifiability blacklist). That CV was **not reused**: this one was rebuilt from `cv.md`. "Cutting provisioning from days to minutes" was dropped for the same reason.

Figures kept because they are verifiable: 15M+ records in the Sybase→Oracle migration, a team of 4 developers led, 1,800 schools / 500k daily requests.

## Other decisions

- **ATS format.** The "Role Fit" block is a list, not a table — tables parse badly in ATS.
- **AI harness:** Claude Code (Max plan) as the primary one, Pi.dev and opencode as prior experience.
- **Location:** "Chile (GMT-4) — available for remote or Santiago hybrid". The posting does not state the work model; worth confirming before going further, since Gonzalo lives in Limache and an on-site hybrid in Santiago does not work.
- **Salary:** not stated in the posting. Useful reference: the 23People/Indeed posting of 2026-08-19 for client Equifax published **CLP 2,900,000–3,200,000 net**.

## Open items

- **No posting URL** — the description arrived pasted. It is needed for the `cv_job_links.md` record and to know whether this runs through 23people, Equifax's own portal or another intermediary.
- **Possible duplicate:** an application for a Java/Spring Boot role with client Equifax was already sent on 2026-08-19 via Indeed. If it is the same process under a different title, it should not be duplicated.

## Status

**Prepared — NOT sent.**
