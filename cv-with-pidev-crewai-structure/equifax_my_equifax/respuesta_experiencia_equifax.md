# "Tell us about your experience in Equifax..."

**Role:** Senior Developer — My Equifax (D2C) · **Date:** 2026-08-24

> ⚠️ **The question as pasted is ambiguous and ends in "...".** Read literally, it asks about experience *at* Equifax — and Gonzalo has never worked there. Two readings are covered below. If the form's wording continues past what was pasted (e.g. "...'s technologies", "...'s industry"), send the full text and this answer gets retargeted.

---

## Reading 1 — "Have you worked at Equifax before?" (recommended default)

The honest answer is no, and it opens the door to the answer that actually helps.

### Written version (form / email) — 205 words

I have not worked at Equifax. What I have done for most of my career is build the systems on the other side of the transaction.

At Citibank I worked on backend services for a bank whose flows depend on credit and risk assessments before anything else happens — approve, decline, price, escalate. I also ran the migration of financial databases from Sybase to Oracle there: over 15 million records, no data loss, inside an environment where an error is auditable and expensive. Before that, at Coopeuch, Santander and Ripley, I spent years on banking backends, including migrating legacy AS/400 modules to Java.

My Equifax sits at the consumer end of that same chain — the person whose file all of that describes, looking at it directly. The engineering constraints I know well: correctness that has to hold under audit, availability that is not negotiable, and a data model that outlives whatever framework is on top of it.

On the stack, the fit is direct: Java and Spring Boot for fifteen years, PostgreSQL as my main database since 2017, and cloud since then too — GCP with Pulumi for infrastructure as code, plus AWS Lambda and S3.

What I do not bring is credit-risk modelling. That is a discipline I would be learning, not teaching.

### Verbal version (~40 seconds)

> "I have not worked at Equifax. But I have spent fifteen years on banking backends — Citibank, Coopeuch, Santander — and those systems all revolve at some point around a credit decision: request it, then act on it. At Citibank I also ran a Sybase-to-Oracle migration of over fifteen million records with no data loss.
>
> My Equifax is the consumer end of that same chain. The stack is what I already work in every day — Java, Spring Boot, PostgreSQL, cloud — and the constraint I know from banking is the one that matters here: being wrong is expensive.
>
> What I would be learning is credit-risk modelling itself. That part I would not claim."

---

## Reading 2 — "Have you had any previous process with Equifax?"

Only if the form is asking about prior contact. Short and factual:

> No employment history with Equifax. I have applied twice before through 23people — a Senior Developer Java/Spring Boot role for the InterConnect platform in July 2026, and a Java/Spring Boot position in August 2026. This is the third role of yours I have applied to, which should say something about how much I want to work there.

---

## Delivery notes

- **Say "no" first.** A recruiter asking about experience at Equifax and getting three paragraphs of adjacent banking work before the answer reads as evasion. The "no" costs one sentence and buys the rest.
- **Do not claim credit-bureau domain expertise.** The defensible claim is *adjacent*: consuming credit decisions from the bank side, not building the scoring models. Saying so out loud lands better than bluffing — and it is the one thing an interviewer in this industry can catch instantly.
- **Verify before sending:** the claim "banking flows that depend on credit and risk assessments" has to be literally true of what you touched at Citibank/Coopeuch/Santander. If your work there was reporting and migrations without touching that path, cut the clause and lead with the migration instead.
- **Figures used are the verifiable ones only:** 15M+ records Sybase→Oracle. No percentages, no self-reported acceleration.
- **Reuse:** `23people_equifax_interconnect/why_equifax_answer.md` covers the *why Equifax* question (motivation) — a different question from this one. Keep both answers consistent if they get asked in the same form.
