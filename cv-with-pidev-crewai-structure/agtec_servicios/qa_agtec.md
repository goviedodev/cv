# 📋 Preguntas y Respuestas — AGtec Servicios Informáticos

> **Puesto:** Desarrollador/a Backend Senior  
> **Portal:** Computrabajo  
> **Fecha:** 2026-04-28

---

## 1. Java y Spring Boot

**P: ¿Cuántos años de experiencia tienes desarrollando backend con Java y Spring Boot? Indica versiones utilizadas y tipo de sistemas (APIs, microservicios, monolitos).**

15+ años con Java (desde 2008), 8+ con Spring Boot. Versiones: Java 1.8 a 21, Spring Boot/MVC/REST. APIs RESTful (Seven IT, Perficient, Citibank), microservicios con Java 21/Spring Boot (Perficient/Caterpillar y plataforma cloud actual como CTO), y monolitos con Spring MVC en etapas iniciales (Seven IT, WebClass), migrados luego a arquitectura de servicios. Sectores: finanzas, e-commerce, salud y banca.

---

## 2. Python

**P: ¿Cuántos años has trabajado con Python en desarrollo backend? Frameworks usados y para qué casos (APIs, scripts, Lambda, ETL, otros).**

Mi experiencia con Python se centra en **IA Harness con software agéntico** (Pi.dev, OpenCode), utilizándolo diariamente para crear **aplicaciones utilitarias**: scripts de automatización, agentes de IA, integración de LLMs, y herramientas de productividad. No lo he usado en producción backend como lenguaje principal — mi stack core es Java/Spring Boot (15+ años) — pero lo manejo con fluidez en contextos de automatización y desarrollo asistido por IA.

---

## 3. Microservicios vs Monolitos

**P: ¿Cuántos años de experiencia tienes trabajando con arquitecturas de microservicios? ¿Y con arquitecturas monolíticas? Describe brevemente en qué contextos.**

**Microservicios (~5 años):** En Perficient/Caterpillar desarrollé microservicios con Java 21/Spring Boot para el e-commerce global. En mi rol actual como CTO diseño una plataforma de movilidad cloud basada en microservicios con Java 21, GraalVM y GCP.

**Monolíticos (~10 años):** Sistemas monolíticos con Java/Spring MVC en Seven IT (gestión hospitalaria), WebClass (plataforma ed-tech para 1.800 escuelas), y sector bancario (Coopeuch, Santander). Varios migraron gradualmente a arquitectura de servicios.

---

## 4. APIs RESTful

**P: ¿Cuántos años diseñando y manteniendo APIs RESTful en producción? Indica volumen aproximado de tráfico o criticidad del sistema.**

**8+ años** diseñando y manteniendo APIs RESTful en producción (desde ~2017 con Spring Boot).

**Contextos y criticidad:**
- **Citibank:** APIs para sistemas financieros de alta criticidad con alto volumen de transacciones y seguridad estricta.
- **Perficient/Caterpillar:** APIs RESTful para e-commerce global con equipos multiculturales distribuidos.
- **Seven IT/Hospital Cruz del Norte:** APIs para sistema de gestión hospitalaria en producción controlando registros médicos, pagos y atención.
- **CTO (actual):** APIs de microservicios para plataforma de movilidad cloud con Java 21 y GCP.

---

## 5. PostgreSQL

**P: ¿Cuántos años de experiencia con PostgreSQL? Nivel de uso: consultas complejas, índices, optimización de rendimiento, transacciones.**

**15+ años con PostgreSQL** (desde 2008). Nivel avanzado: consultas complejas, optimización de rendimiento y transacciones en Seven IT (gestión hospitalaria con PostgreSQL 9.6), sector bancario (Coopeuch), ed-tech (WebClass), y migración de bases de datos en Citibank (Sybase → Oracle).

---

## 6. MongoDB / NoSQL

**P: ¿Cuántos años trabajando con MongoDB u otras bases NoSQL? Describe tipos de modelos de datos y escenarios de uso.**

MongoDB figura en mi perfil como **base de datos secundaria**. No tengo un número concreto de años dedicado exclusivamente, pero lo he utilizado como complemento a stacks Java/Spring Boot para **modelado de datos NoSQL** orientado a documentos flexibles (formularios, catálogos, datos semi-estructurados) donde la escalabilidad horizontal y la flexibilidad del esquema superaban la rigidez relacional. Mi experiencia fuerte en bases de datos se centra en PostgreSQL y Oracle PL/SQL (15+ años).

---

## 7. Redis / Caché / Mensajería

**P: ¿Cuántos años utilizando Redis u otros sistemas de caché/mensajería? ¿En qué casos lo implementaste y con qué impacto?**

**Redis y caché:** Implementé Redis en **Salcobrand** como capa de caché para APIs de alto tráfico, reduciendo latencia en consultas recurrentes y descargando la base de datos principal.

**Mensajería:** Usé **IBM MQ** en Salcobrand para comunicación asíncrona entre sistemas, garantizando entrega confiable de mensajes en procesos de negocio críticos.

Mi experiencia es práctica pero no es mi stack principal — mi fortaleza está en Java/Spring Boot y bases de datos relacionales (15+ años).

---

## 8. AWS / Cloud Deployment

**P: ¿Cuántos años de experiencia desplegando aplicaciones en AWS? Servicios usados (EC2, S3, RDS, Lambda) y nivel de responsabilidad técnica.**

Mi experiencia de despliegue en cloud se centra en **Google Cloud Platform**, no en AWS. He usado **GCP con Pulumi (IaC)** para desplegar servicios en **Google Cloud Run** con infraestructura automatizada desde código.

Para cómputo serverless, mi experiencia es con **Cloudflare Workers**, no con AWS Lambda.

No tengo experiencia de producción con servicios AWS como EC2, S3, RDS o Lambda, aunque los conceptos de infraestructura cloud son transferibles entre proveedores.

---

## 9. Arquitectura Cloud

**P: ¿Cuántos años participando en diseño de arquitecturas cloud? ¿Tomaste decisiones de escalabilidad, disponibilidad o costos?**

**8+ años** participando en diseño de arquitecturas cloud como **CTO** en dos roles:

**Seven IT (2017–2020):** Diseñé la infraestructura cloud para un sistema de gestión hospitalaria en **Google Cloud (VM)**, tomando decisiones de disponibilidad y escalabilidad para un sistema en producción con múltiples servicios.

**Startup de Movilidad (2024–presente):** Diseño la arquitectura cloud completa con **GCP y Pulumi (IaC)**, incluyendo decisiones de **costos** (uso de LLMs económicos sin sacrificar rendimiento), **escalabilidad** (microservicios en Cloud Run) y **disponibilidad** (infraestructura automatizada y desplegable desde código).

---

## 10. Testing

**P: ¿Cuántos años aplicando tests unitarios e integración en backend? Herramientas usadas y nivel de cobertura esperado en tus proyectos.**

**15+ años aplicando testing en backend** como parte del ciclo QA full-cycle.

**Testing unitario:** Experiencia con pruebas unitarias integradas en el desarrollo Java (JUnit en ecosistemas Spring/Java). En mi rol actual como CTO, mantengo pruebas unitarias e integración para microservicios.

**Testing de integración:** Implementado en proyectos de Perficient/Caterpillar, Citibank y Seven IT, incluyendo pruebas de integración con bases de datos PostgreSQL/Oracle y servicios externos.

**Herramientas:** JUnit, Jenkins (CI), pipelines de CI/CD.

**Cobertura esperada:** Apunto a **80%+** en unitarias para lógica de negocio crítica, con integración que cubra los flujos end-to-end principales.

---

## 11. CI/CD

**P: ¿Cuántos años utilizando pipelines de CI/CD? Herramientas concretas (GitLab, Jenkins, GitHub Actions) y tu rol en su configuración.**

**10+ años** con pipelines de CI/CD.

**Jenkins:** Configuré pipelines de CI/CD en **Citibank** (2019–2022) y en etapas anteriores (WebClass/Creasys), automatizando builds, pruebas unitarias y despliegues en entornos regulados.

**GitLab CI:** Implementé pipelines en **Seven IT** (2017–2020) con GitLab, integrando build, test y despliegue continuo para el sistema hospitalario.

**Azure DevOps:** Lo he utilizado como herramienta de gestión y CI/CD en proyectos empresariales, configurando pipelines de integración.

**Mi rol:** He sido responsable de **configurar, mantener y optimizar** estos pipelines, asegurando que incluyan builds automatizados, pruebas, análisis de calidad y despliegues continuos.

---

## 12. Docker y Git

**P: ¿Cuántos años trabajando con Docker en desarrollo y despliegue? Nivel de uso de Git (branching, PRs, code review, flujos de equipo).**

**Docker (~4 años):** Lo utilizo en mi rol actual como CTO para contenerización de microservicios Java 21/Spring Boot, empaquetando aplicaciones para despliegue en Google Cloud Run. También en entornos de desarrollo local para consistencia entre ambientes.

**Git (15+ años):** Dominio avanzado. Flujos con GitLab y GitHub: branching (GitFlow/feature branches), PRs con code review, merge strategies y resolución de conflictos. En Citibank, Perficient y Seven IT trabajé con equipos distribuidos donde Git era central para colaboración, revisiones de código y control de versiones en pipelines CI/CD.
