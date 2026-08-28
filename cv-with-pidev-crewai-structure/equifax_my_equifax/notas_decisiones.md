# Nota de decisiones — Equifax / Senior Developer (My Equifax, D2C)

**Fecha:** 2026-08-24

## Idioma: inglés (confirmado por Gonzalo)

El aviso dice "entorno de trabajo 100% en inglés" y pide "excelentes skills de comunicación en inglés". Un CV en español sería la primera contradicción del proceso. Además, las dos postulaciones previas a Equifax en este repo (`23people_equifax/`, `23people_equifax_interconnect/`) también fueron en inglés.

> Nota sobre la skill `cv-tailor`: clasificaría esto como perfil A (Chile local, CLP → español). El aviso manda sobre la regla; queda registrado para no tratarlo como error.

## Encaje: no hay gaps duros

Es la mejor coincidencia de las postulaciones recientes. Todos los requisitos técnicos están cubiertos con experiencia real:

| Requisito | Cobertura |
|---|---|
| 4+ años Java | 15+ años (1.8 → 21) |
| 4+ años Spring Boot | Desde 2017 (Seven IT) hasta hoy |
| 4+ años PostgreSQL | Seven IT 2017–2020 + Creasys/WebClass + plataforma actual |
| 4+ años cloud AWS/GCP | GCP desde 2017; Pulumi IaC desde 2024; AWS Lambda y S3 |
| Inglés B2 | Citibank y Perficient, equipos english-only 2021–2023 |
| Título en Informática/Sistemas | Ing. en Ejecución en Computación e Informática, UBB, titulado |

**Matiz honesto sobre cloud:** la fortaleza es **GCP**, no AWS. El aviso pide "AWS/GCP" con barra, así que GCP satisface el requisito literal; en AWS se declara solo Lambda y S3, sin inflar. Si en la entrevista el equipo resulta ser AWS-first, ese es el punto a conversar.

## Resumen profesional — agente `ai_expert_redactor_for_recruters`

Aplicado igual que en `michael-page/`: 40–50 palabras, 3–4 líneas, escaneable en 7 segundos. Sin "CTO"/"Co-founder" (Restricción global n.º 1, que prevalece sobre el ejemplo de la propia plantilla del agente).

### Opción A — Dominio e impacto ✅ **APLICADA** (43 palabras)
> Senior backend developer, 15+ years in Java and Spring Boot. Built transactional systems for banking (Citibank), global e-commerce (Caterpillar) and healthcare on PostgreSQL, deployed on GCP and AWS. Six years working daily in English with distributed teams across the US, India and Ukraine.

Los tres nombres reconocibles (Citibank, Caterpillar, PostgreSQL) más la prueba de inglés en la misma línea.

### Opción B — Espejo del requisito (43 palabras)
> Java and Spring Boot backend developer with 15+ years, well past the 4+ this role asks for. PostgreSQL since 2017 — schema design, queries, stored procedures — and cloud since then too: GCP with Pulumi IaC, plus AWS Lambda and S3. Daily stand-ups in English.

Responde el checklist uno a uno. Mejor si el primer filtro es un ATS con scoring por keywords.

### Opción C — Autogestión (46 palabras)
> Senior backend developer, 15+ years in Java and Spring Boot. I own services end to end — schema on PostgreSQL, REST layer, deployment to GCP and AWS — and have done it inside regulated banking and global e-commerce teams, working in English with people in three time zones.

Ataca directo la "capacidad de autogestión" del bloque de skills personales.

## Qué se corrigió respecto del CV de InterConnect (julio)

`23people_equifax_interconnect/cv_gonzalo_equifax_interconnect.md` contiene "aceleración de hasta **300%**" y "picos sobre **2000%**", hoy prohibidos por la Restricción global n.º 3 (lista negra de verificabilidad). Ese CV **no se reutilizó**: se rehízo desde `cv.md`. También se sacó "cutting provisioning from days to minutes" por la misma razón.

Cifras conservadas por verificables: 15M+ registros Sybase→Oracle, equipo de 4 desarrolladores, 1.800 escuelas / 500k peticiones diarias.

## Otras decisiones

- **Formato ATS.** El bloque "Role Fit" se escribió como lista, no como tabla — las tablas se parsean mal en ATS.
- **Harness de IA:** Claude Code (plan Max) como principal, Pi.dev y opencode como experiencia previa (según tu criterio actual).
- **Ubicación:** "Chile (GMT-4) — available for remote or Santiago hybrid". El aviso no declara modalidad; conviene confirmarla antes de avanzar, porque vives en Limache y un híbrido presencial en Santiago no te sirve.
- **Renta:** no declarada en el aviso. Referencia útil: el aviso de 23People/Indeed del 2026-08-19 para cliente Equifax publicaba **$2.900.000–$3.200.000 líquidos**.

## Faltantes

- **No tengo la URL del aviso** — la descripción llegó pegada. Hace falta para el registro en `cv_job_links.md` y para saber si va por 23people, por el portal de Equifax o por otro intermediario.
- **Posible duplicado:** ya enviaste una postulación a un rol Java/Spring Boot de cliente Equifax el 2026-08-19 vía Indeed. Si es el mismo proceso con otro título, conviene no duplicar.

## Estado

**Preparada — NO enviada.**
