# Desarrollador Back-end — Lisit (Remote)

**Empresa:** Lisit
**Portal:** GetOnBoard
**URL:** https://www.getonbrd.com/jobs/programming/desarrollador-backend-lisit-remote
**Modalidad:** 100% remoto — candidatos de cualquier parte del mundo
**Seniority:** Senior · Full time · Programming
**Fecha de captura:** 2026-08-26
**GETONBRD Job ID:** 63250

> Nota: existe otra postulación previa a Lisit en este mismo repo (`lisit/cv_gonzalo_lisit.md`, fila `cv_job_links.md` 2026-05-25) para una vacante distinta — "Backend Developer Java + Spring Boot", híbrida en Santiago. Esta es una vacante nueva y diferente, 100% remota, centrada en migración de datos a PostgreSQL/PostGIS. Los archivos de esta postulación llevan el sufijo `_backend_remote` para no pisar los anteriores.

## Descripción

En Lisit creamos, desarrollamos e implementamos servicios de software enfocados en automatización y optimización. Este rol se enfoca en una iniciativa clave de evolución del sistema: el traspaso de datos del sistema actual hacia un nuevo Maestro basado en PostgreSQL y PostGIS, incorporando una API de normalización para alta concurrencia y la carga masiva de datos geográficos, cuidando desempeño, integridad y confiabilidad durante la migración.

## Funciones

- Trabajar junto al Backend titular para construir el traspaso de datos del sistema actual al nuevo Maestro (PostgreSQL/PostGIS).
- Diseñar e implementar la API de normalización orientada a alta concurrencia.
- Liderar la carga masiva de datos geográficos con enfoque en rendimiento y escalabilidad.
- Migración / ETL de datos: mover volúmenes grandes entre motores, validación de integridad y conciliación.
- Implementar caché (Redis), paginación y procesos batch asíncronos.
- Tests y disciplina de trabajo con CI/CD en GitLab.
- Optimizar modelamiento, índices y consultas en PostgreSQL.
- Colaborar en Git y cobertura exigida (SonarQube ≥ 80%), commits diarios.

## Excluyente (requisitos duros)

- Node.js con NestJS (o experiencia sólida en TypeScript backend con arquitectura por capas / hexagonal).
- PostgreSQL avanzado: modelamiento, índices, optimización de consultas, uso eficiente de recursos.
- Experiencia en Migración / ETL: mover volúmenes grandes entre motores, validar integridad y conciliar resultados.
- APIs REST de alta concurrencia: caché (Redis), paginación, procesos batch asíncronos.
- Git + CI/CD (GitLab): disciplina de commits diarios y cobertura de tests (SonarQube ≥ 80%).

## Deseable (suma puntos)

- PostGIS o experiencia con datos geoespaciales (consultas espaciales, geometrías).
- Lectura de PL/SQL para comprender reglas de negocio del sistema de origen.
- Kong API Gateway y Keycloak / OAuth2 / JWT.
- Docker y Kubernetes / OpenShift.

## Preguntas filtro

1. ¿Cuéntanos una migración de datos grande que hayas hecho? ¿Cómo validaste que no se perdió nada?
2. ¿Cómo diseñarías un autocompletar que responda en menos de 0,4s bajo concurrencia? (esperado: índices + caché, nunca consulta pesada por tecla)

## Beneficios

100% remoto.

## Instrucciones del usuario para esta postulación (2026-08-26)

- Destacar el uso de PostGIS del proyecto Mobilidad (startup de movilidad, app.tellevoapp.cl): trabajo centrado en coordenadas.
- Ser honesto: las consultas espaciales y geometrías del proyecto Mobilidad se resolvieron con funciones de Google Maps, no con PostGIS nativo.
- Kong API Gateway: no lo ha usado.
- Keycloak: solo un experimento, no en producción.
- Contenedores: solo Docker (sin Kubernetes/OpenShift).
- CV y mensajes de esta postulación: en inglés. Generar tanto versión ATS-safe como estilo Harvard.
