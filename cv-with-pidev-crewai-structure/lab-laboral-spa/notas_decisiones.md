# Nota de decisiones — Laboratorio Laboral SPA (LabLab) / Full-Stack Developer

**Fecha:** 2026-08-26 · **Modo:** directo (URL de Get on Board provista por el usuario).

## Perfil elegido

**A — Chile local (CLP/USD publicado), español.** Empresa chilena, oficina en Santiago, modalidad híbrida, requiere postular en español según el portal.

## Keywords espejadas (ortografía del aviso)

`PHP` · `JavaScript / TypeScript` · `React` · `Node.js` · `APIs REST e integraciones` · `SQL y bases de datos relacionales` · `Git` · `producción` · `testing` · `documentación` · `incidencias en ambientes productivos` · `despliegues` · `herramientas de IA`. Cada keyword crítica aparece 2–3 veces (resumen, habilidades, un bullet de experiencia o el proyecto público).

## Decisiones que tomaste tú en esta ronda

| Punto | Decisión | Cómo quedó |
|---|---|---|
| **Symfony** (requisito duro del stack) | No declararlo | Gap explícito en `mensaje_reclutador.md`. En el CV solo se declara PHP (real, 2008–2017) sin framework específico, y frameworks MVC análogos (Spring Boot, Struts) como puente. |
| **PHP** | Sí, real | Aparece en Resumen, Habilidades y en los bullets de WebClass/Creasys/Coopeuch (2008–2017), que es donde efectivamente ocurrió. No se traslada a roles recientes. |
| **React / Node.js / TypeScript** | Sí, vía proyecto público | Declarados a través del proyecto `niuro` (Next.js 14 + React 18 + NestJS + JWT + Jest), no como experiencia laboral remunerada — es la evidencia real y verificable (repo público en GitHub). |
| **AWS** | Declarado de forma acotada | Solo AWS Lambda, sin inflar a "experiencia cloud AWS"; se apoya en Google Cloud (Cloud Run, Pulumi IaC) como el cloud fuerte del perfil, cubriendo "AWS u otros servicios cloud". |
| **Microservicios / SaaS** | Sí, acotado | La plataforma de movilidad se declara como "arquitectura completa" con integración de APIs de terceros; no se usa la palabra "SaaS" porque no es literalmente ese modelo de negocio. |
| **Formato** | ATS-safe (default del proyecto) | No se preguntó ni se aplicó estilo Harvard — restricción global n.º 5 de `AGENTS.md`: sin pedido explícito, el default es ATS. |
| **React Native** (dato aportado por Gonzalo el 2026-08-26, no estaba en `cv.md`) | Sí, en el resumen y en un bullet propio de TeLlevoApp | Gonzalo confirmó que la primera etapa de la interfaz móvil de la plataforma de movilidad se construyó en React Native, antes de migrar a Flutter (que sí estaba en `cv.md`). Se declaró como hecho puntual y acotado a esa etapa, no como stack activo hoy. |
| **Git** | Se subió de prioridad en el resumen, a pedido de Gonzalo | Antes aparecía solo en Habilidades y en las líneas de Stack; ahora el resumen abre con "Git como control de versiones en toda mi carrera" para que quede como hilo conductor de los 15 años, no solo como bullet de herramientas. |
| **PHP** | Se bajó de prioridad en el resumen, a pedido de Gonzalo | Sigue declarado (es real, 2008–2017), pero ahora se enmarca explícitamente como "proyectos de banca y ed-tech en empresas anteriores" en vez de abrir el resumen como si fuera el lenguaje principal actual. Se mantiene igual en Habilidades y en los bullets de WebClass/Creasys/Coopeuch. |

## Lo que sí se reclamó y por qué resiste una entrevista

- **Full-stack de punta a punta:** WebClass (PHP + Java, banca/ed-tech/retail, 2008–2017) y Seven IT (Sistema de Gestión en Salud, backend + frontend + PostgreSQL + despliegue + soporte, 2017–2020) son dos roles reales donde hizo el ciclo completo, que es exactamente lo que pide el aviso.
- **Diagnóstico de incidencias en producción:** declarado en Seven IT y WebClass (plataforma de 1.800 escuelas / 500k peticiones diarias), no como frase genérica sino ligado a un sistema y una escala reales.
- **IA aplicada al proceso de desarrollo, testing y documentación:** se usa casi la frase literal del aviso ("testing, documentación o resolución de problemas") porque coincide con lo que realmente hace con Claude Code en TeLlevoApp — no es keyword stuffing, es el mismo flujo spec → plan → ejecución → verificación de otras postulaciones.
- **Cifras conservadas** por verificables: 15M+ registros Sybase→Oracle (Citibank), 1.800 escuelas / 500k peticiones diarias (WebClass), equipo de 4 desarrolladores (Seven IT). Cero porcentajes de mejora autorreportados.

## Otras decisiones

- **Ubicación:** Limache + disponibilidad para modalidad híbrida en Santiago, en la primera línea del encabezado — el aviso es explícitamente híbrido en Santiago.
- **Sin "CTO"/"Co-founder"** (Restricción global n.º 1): la startup va como Tech Lead y se mantiene anónima.
- **Seniority:** el aviso pide "idealmente 4+ años"; hay 15. No se menciona el número del aviso, solo la trayectoria real.
- **Renta:** no se incluyó pretensión de renta en el CV (no es una sección estándar); el aviso ya publica USD 2.600–3.000/mes brutos, dentro de la banda que Gonzalo ha aceptado antes para roles locales.

## Riesgo abierto

El aviso lista Symfony como parte del "stack técnico esperado" (no explícitamente "excluyente", a diferencia de otros avisos revisados antes). Un filtro automático estricto por esa palabra podría descartar el CV. Es el costo de la decisión de no inventarla: PHP real sin Symfony es más defendible en una entrevista técnica que "Symfony" sin poder hablar de bundles, Doctrine ORM o el ciclo de vida de un controlador Symfony.

## Estado

**Preparada — NO enviada.** Falta que Gonzalo confirme y postule (el portal exige postular en español, ya cumplido).
