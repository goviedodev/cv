# Nota de decisiones — 3it / Developer Senior Java Banca (cliente Banco de Chile)

**Fecha:** 2026-08-24 · **Modo:** directo (oferta pegada por el usuario, sin URL del portal).

## Perfil elegido

**A — Chile local (CLP), español.** Consultora chilena, cliente Banco de Chile, oficina en Santiago, modalidad híbrida presencial 1 día/semana.

## Keywords espejadas (ortografía del aviso)

`Java 8 / 11 / 17 / 21` · `Spring Boot 3.x` · `ORM` (Hibernate/JPA) · `concurrencia` · `Git` · `Jenkins` · `REST y SOAP` · `Singleton, Builder y DTO` · `migración de sistemas legacy` · `Elasticsearch` · `banca`. Cada keyword crítica aparece 2–3 veces (resumen, habilidades, bullets).

## Decisiones que tomaste tú en esta ronda

| Punto | Decisión | Cómo quedó |
|---|---|---|
| **Kubernetes** (requisito duro) | No declararlo | Fuera del CV por completo. Se declara el gap de forma explícita en `mensaje_reclutador.md`. Contenedores se declaran como Docker + Pulumi IaC, que es lo real. |
| **SOAP** (requisito duro) | Sí, banca legacy | Aparece en Habilidades ("consumo e integración de servicios REST y SOAP") y en un bullet del bloque 2008–2017, que es donde efectivamente ocurrió. No se traslada a Citibank ni a roles recientes. |
| **Elasticsearch** (deseable) | Sí | Declarado en "Ciclo de desarrollo y operación" acotado a búsqueda y revisión de logs, junto con Kibana. Sin inflar a "stack de observabilidad". |
| **Dynatrace** (deseable) | No declarado | Gap explícito en el mensaje al reclutador. |
| **Formato** | Estilo Harvard | Preámbulo LaTeX de `.pi/skills/harvard-cv-format/`, macros `\rol`/`\org`/`\stack`. Verificado: 2 páginas exactas y `pdftotext` devuelve texto lineal, completo y en orden. |

## Lo que sí se reclamó y por qué resiste una entrevista

- **Concurrencia:** declarada como hilos, ejecución paralela de procesos batch y control de acceso a recursos compartidos — el terreno real de las migraciones de host y los procesos bancarios. No se declara "sistemas distribuidos de alta concurrencia".
- **Patrones de diseño:** Singleton, Builder, DTO y Repository, con la ortografía del aviso.
- **Spring Boot 3.x:** el trabajo actual es Java 21 + Spring Boot; la versión 3.x es coherente con ese stack.
- **Migración de legacy con mínima supervisión:** el aviso lo pide de forma literal. Se cubre con hechos (AS/400 → Java en Santander/Ripley/Coopeuch, Sybase → Oracle en Citibank) y con un bullet del rol actual sobre autonomía técnica, **sin usar la palabra "proactivo"** ni ningún otro adjetivo de la lista negra.

## Otras decisiones

- **Ubicación:** se declara Limache + disponibilidad para la modalidad híbrida en Santiago, en la primera línea del encabezado. El aviso marca la presencialidad como condición de postulación: conviene responderla antes de que la pregunten, y coincide con lo que dice tu perfil en los portales.
- **Sin "CTO"/"Co-founder"** (Restricción global n.º 1): la startup va como Tech Lead y se mantiene anónima.
- **Cifras conservadas** por verificables: 15M+ registros Sybase→Oracle, equipo de 4 desarrolladores, 1.800 escuelas / 500k peticiones diarias. Cero porcentajes de mejora autorreportados.
- **Seniority:** el aviso pide 6 años; hay 15. No se menciona el número del aviso, solo la trayectoria real.

## Riesgo abierto

El aviso pide Kubernetes como requisito duro y un filtro automático puede descartar el CV por esa palabra ausente. Es el costo de tu decisión de no declararlo, y es una decisión defendible: en una entrevista técnica de banca, "conozco los conceptos" frente a alguien que opera clústers a diario se nota. Si prefieres arriesgar el filtro a cambio de la entrevista, se puede reponer como "Kubernetes (conceptos: Pods, Deployments, ConfigMaps, Secrets)" en una segunda versión.

## Estado

**Preparada — NO enviada.** Falta que postules y que confirmes el portal de origen para completar la URL en `cv_job_links.md`.

## Respuesta a "¿Por qué te interesa trabajar en 3IT?"

Generada en `3it/respuesta_por_que_3it.md` (versión escrita ~240 palabras + versión hablada + notas de entrega). Ángulos: migración de legacy bancario como oficio propio, experiencia operando como externo dentro de la casa del cliente (Citibank, Perficient–Caterpillar) y la modalidad híbrida como condición que sí se cumple. Datos de empresa verificados en el sitio de 3IT (150+ especialistas, ISO 9001/27001, banca entre sus industrias); no se afirma nada del proyecto específico con Banco de Chile.
