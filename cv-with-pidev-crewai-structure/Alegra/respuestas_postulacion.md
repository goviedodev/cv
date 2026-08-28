# Respuestas — Postulación Alegra (Cloud Engineer Mid/Sr)

> Get on Board suele pedir estas respuestas al postular. Redactadas con reflejo léxico del aviso (Tarea 3 de AGENTS.md). Listas para pegar.

## a) Cuéntanos sobre tu experiencia y perfil profesional

Llevo más de 15 años construyendo software y, desde 2024, soy responsable end-to-end de mejorar, optimizar y monitorear la infraestructura de una plataforma de movilidad en producción. No es un rol de "mantener la nube funcionando": la diseñé, la desplegué, la aseguro, la monitoreo y controlo su costo, y además mantengo las plataformas internas que usa el equipo de desarrollo para moverse rápido y sin fricción.

Arquitectura serverless y automatización. Diseñé y evoluciono la arquitectura sobre servicios gestionados —Cloud Run y API Gateway, los equivalentes de Lambda y API Gateway— reemplazando progresivamente el monolito por microservicios con APIs REST. Automaticé los ciclos de despliegue con IaC (Pulumi) y pipelines de CI/CD con despliegues con Docker, para acelerar la entrega de software: la infraestructura completa —cómputo, red, balanceo, firewall, IAM y secretos— está escrita como código reutilizable versionado en Git, de modo que levantar un entorno nuevo no depende de mí ni de configuración manual en consola. Y desplegué automatizaciones basadas en agentes de IA para optimizar procesos internos y eliminar tareas manuales.

Seguridad cloud y platform engineering. Soy dueño de la seguridad de la infraestructura: detección de tráfico anómalo con WAF, gestión de secretos, IAM de menor privilegio y respuesta ante incidentes. Las políticas de acceso y gobernanza están implementadas y auditadas como código, versionadas y revisables — no solo en el papel.

Observabilidad, confiabilidad y costos. Mantengo los sistemas de monitoreo y alertas con foco en detección proactiva, no reactiva: me entero de los problemas antes que los usuarios. Los incidentes los trabajo buscando causa raíz y prevención, no parches — la disciplina viene de 17 años en Santander/Isban y Citibank atendiendo sistemas transaccionales que no se pueden caer. Y monitoreo costos de forma continua: elegir servicios gestionados por sobre máquinas siempre encendidas fue, antes que nada, una decisión de costo.

Un punto de transparencia, porque prefiero decirlo yo antes que se descubra en la entrevista técnica: mi nube productiva es Google Cloud, no AWS. En AWS he usado Lambda y S3, no una arquitectura serverless completa, y mi IaC es Pulumi, no Terraform; mi monitoreo es Cloud Logging/Monitoring, no CloudWatch ni Grafana. El aviso dice explícitamente "o sus equivalentes" y creo que aplica: VPC, IAM, balanceo, colas, secretos, observabilidad y control de costos son los mismos conceptos, y Pulumi y Terraform resuelven el mismo problema con distinta sintaxis. El traslado es cuestión de semanas de trabajo real, no de meses.

## b) ¿Cómo usarías IA en el día a día?

Ya la uso de forma integrada a mi flujo real de trabajo, con agentes, MCPs y skills, y no como asistente ocasional: construí mi propio harness sobre Claude Code (plan Max) con skills, comandos y workflows propios, más MCPs para conectar herramientas externas al flujo.

Lo aplico en tareas de análisis, automatización y desarrollo, que son las tres que menciona el aviso: analizar problemas de arquitectura contrastando alternativas antes de decidir, automatizar procesos internos y eliminar tareas manuales que antes hacía a mano, y desarrollar con puertas de calidad definidas por mí — no acepto salida de agente que no pase revisión y pruebas.

Antes de Claude Code trabajé el mismo enfoque con Pi.dev y opencode, así que el diseño del ciclo de vida de un agente (qué skill, qué contexto, qué límite, qué verificación) es algo que ya iteré varias veces. Es también la forma en que cierro brechas técnicas rápido: investigar patrones, mejores prácticas y trampas conocidas de una herramienta nueva con agentes es mucho más veloz que leer documentación de punta a punta. Es, exactamente, combinar la rigurosidad del cumplimiento de seguridad con la curiosidad de la Inteligencia Artificial.

## c) ¿Por qué te interesa Alegra?

Tres razones, en orden de peso.

Porque el rol es el trabajo que ya hago, con más escala. Los tres pilares del aviso —arquitectura serverless y automatización, seguridad cloud y platform engineering, observabilidad, confiabilidad y costos— describen casi punto por punto lo que hago hoy, incluido el reemplazo progresivo del monolito. La diferencia es el tamaño: pasar de una plataforma propia a una que usan millones de Pymes en 8 países es exactamente el salto que busco.

Porque la cultura AI-First no es marketing en mi caso. Que la IA "no sea un proyecto paralelo sino la forma en que operan" es raro de encontrar. Yo ya construí mi harness de agentes y lo opero a diario; un equipo donde eso es la norma —con hackathons y espacios de experimentación— me deja empujar más lejos algo que hoy hago solo.

Porque el 100% remoto con relación laboral estable calza con cómo trabajo. Vivo en Limache (GMT-4) y llevo años en equipos distribuidos: EE. UU., India, Ucrania y Latinoamérica en Caterpillar y Citibank. La coordinación asíncrona y la documentación escrita no son un ajuste para mí, son el modo por defecto.
