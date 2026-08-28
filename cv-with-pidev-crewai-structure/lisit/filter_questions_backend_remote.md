# Filter questions — Lisit / Backend Developer (Remote)

## 1. Tell us about a large data migration you've done. How did you validate that nothing was lost?

At Citibank I migrated the reporting database from Sybase to Oracle — over 15 million financial records — with zero data loss, working with engineers in the US, Ukraine, India, and Chile under a strict regulatory release process.

The validation that mattered wasn't a single check, it was layered: row counts and aggregate totals (sums, min/max on financial fields) compared between source and target after each batch, not just at the end; a reconciliation pass against the source system before the old system was allowed to go dark, so any discrepancy had a place to be traced back to; and cutover windows tight enough that the two systems weren't diverging for long between the last sync and the switch. Regulatory sign-off on a bank forces that discipline — "it looks right" isn't an acceptable answer, the numbers have to match, provably, before anyone signs off.

Earlier in my career I did the same kind of work moving core banking batch processes from legacy AS/400 hosts to Java for Santander, Ripley, and Coopeuch: reverse-engineer the existing process first, model the target data, then reimplement — never migrate logic you don't yet understand.

## 2. How would you design an autocomplete that responds in under 0.4s under concurrency?

The rule I'd start from: never a heavy query per keystroke. That constraint drives the whole design.

- **Index the search path properly.** For prefix/substring search over PostgreSQL, a `pg_trgm` GIN index (or a dedicated prefix index if the match pattern is simple prefix-only) turns the query from a sequential scan into an index lookup — that's the difference between milliseconds and hundreds of milliseconds by itself.
- **Cache the hot queries.** Autocomplete traffic is heavily skewed toward a small set of popular prefixes. A cache layer (Redis is the standard tool here) in front of PostgreSQL for the most-requested terms takes repeat load off the database entirely, which matters most exactly under concurrency.
- **Limit and paginate aggressively.** Return the top N results (5–10), never the full match set — smaller result sets are cheaper to compute, cheaper to serialize, and cheaper to render.
- **Debounce on the client and cancel in-flight requests.** If the user is still typing, the previous request is stale — cancel it instead of letting it queue up and contend for connections.
- **Read replica if the base table is also under write load.** Autocomplete reads shouldn't compete with the writes that are updating the same data.

I haven't operated Redis in production myself — my caching and query-tuning experience is PostgreSQL-side (indexing, query plans) rather than a Redis deployment — but the design above is the standard shape for this problem, and it's the direction I'd take building it.

---

**Note:** these are also answered inline in the GetOnBoard application form. Kept here as the source text so wording stays consistent if asked to expand in an interview.
