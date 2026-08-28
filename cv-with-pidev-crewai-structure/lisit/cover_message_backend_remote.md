# Cover message — Lisit / Backend Developer (Remote)

**Suggested channel:** GetOnBoard application form or recruiter LinkedIn message.
**Length:** ~115 words.

---

Hi, I'm Gonzalo Oviedo, a backend engineer with 15+ years on PostgreSQL, including a large-scale migration with zero data loss.

At Citibank I migrated a reporting database from Sybase to Oracle — 15M+ financial records, zero data loss — and earlier I moved core banking batch processes from AS/400 hosts to Java for Santander, Ripley, and Coopeuch: exactly the kind of legacy-to-new-master migration this role describes. I build backend services in NestJS/TypeScript (see github.com/goviedodev/niuro) and Java/Spring Boot, and I currently own the backend of a mobility platform where coordinate data is daily work — though resolved via Google Maps APIs, not PostGIS.

Two gaps to flag upfront: no production experience with Kong API Gateway or PostGIS spatial queries. Everything else in the listing I can speak to directly.

Available fully remote, any time zone overlap you need.

---

## Gaps declared (do not hide in interview)

| Requirement in the posting | Real situation |
|---|---|
| PostGIS / geospatial queries — desirable | No production use. Coordinate/route/distance logic in the mobility platform runs through Google Maps APIs, not native PostGIS geometries. |
| Kong API Gateway — desirable | No hands-on experience. |
| Keycloak — desirable (paired with OAuth2/JWT) | Experimented with it outside production only. Production auth experience is JWT/OAuth2 (NestJS project). |
| Kubernetes / OpenShift — desirable (paired with Docker) | Docker only, no Kubernetes/OpenShift. |
| Redis cache — part of the "high-concurrency REST APIs" hard requirement | No production use of Redis specifically. Pagination and PostgreSQL query optimization are real; the Redis layer itself is not something I've shipped. |
