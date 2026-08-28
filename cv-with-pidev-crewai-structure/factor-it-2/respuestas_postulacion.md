# Respuestas — Postulación Factor IT (Full Stack Senior Developer)

## a) Cuéntanos sobre tu experiencia y perfil profesional

Soy desarrollador full stack con más de 15 años de trayectoria diseñando y construyendo soluciones que integran frontend, backend, APIs y servicios externos. Hoy soy Tech Lead de una plataforma de movilidad en producción sobre Google Cloud, donde implementé el sistema de pagos con Transbank (Webpay) y Khipu, integrando los flujos de checkout, confirmación y conciliación de transacciones. La interfaz la construí en React Native y luego migré a Flutter; las integraciones con servicios externos (Google Maps: Directions, Distance Matrix, Geocoding) las resolví vía APIs REST.

En React tengo respaldo desde antes: entre 2014 y 2017 implementé las vistas front-end de la nueva generación de aplicaciones de Nubox Facturación Electrónica. En TypeScript y Node.js mi proyecto más reciente es público (github.com/goviedodev/niuro): frontend en Next.js 14 con React 18 y TypeScript, backend en NestJS con pruebas en Jest. Antes desarrollé APIs REST para el e-commerce global de Caterpillar bajo Scrum con equipos de EE. UU., India y Latinoamérica, y como Tech Lead en Seven IT construí full stack un sistema de gestión en salud —incluido su módulo transaccional de pagos— liderando a 4 desarrolladores con Merge Requests en GitLab. No he trabajado microfrontends ni Modyo en producción, y lo declaro de entrada; sí Git, GitLab CI/CD, Docker y arquitectura de microservicios.

## b) Cuéntanos sobre tu formación académica y estudios

Soy Ingeniero en Ejecución en Computación e Informática, titulado en la Universidad del Bío-Bío (Concepción, 2005–2009). Mi tesis fue sobre Extreme Programming (XP), teoría y práctica — un tema poco convencional en la carrera en ese momento y que terminó marcando cómo trabajo hoy: iterativo, con pruebas automatizadas como puerta de calidad y entregas frecuentes.

Desde entonces mantengo formación continua por cuenta propia: de Java 8 a Java 21, TypeScript con React y NestJS en proyectos propios, arquitecturas cloud-native y, en el último tiempo, flujos de trabajo con agentes de IA (Claude Code) aplicados al desarrollo de software en producción.

## c) ¿Por qué estarías interesado en trabajar en Factor IT?

Dos razones, en orden de peso.

**Por el proyecto.** El aviso es sobre Checkout, medios de pago y pasarelas de pago, y es exactamente el dominio donde tengo más para aportar: implementé el checkout con Transbank (Webpay) y Khipu en la plataforma de movilidad que lidero técnicamente, cubriendo los flujos de pago, confirmación y conciliación de transacciones, y antes construí el módulo transaccional de pagos de un sistema de gestión en salud. No es un dominio nuevo para mí, es continuación directa de lo que ya construyo.

**Por el stack y el formato.** React, TypeScript y Node.js son las tecnologías con las que trabajo hoy en mis proyectos más recientes, sobre una base de 15 años en desarrollo backend con Java. El formato remoto y full time, con foco en un proyecto acotado, me permite dedicarme de lleno sin fricción de zona horaria con equipos de Latinoamérica — algo que ya hice en Perficient integrándome al equipo y los estándares de un cliente externo (Caterpillar), no los míos. Sobre la duración de ~4 meses: la tengo evaluada y me parece razonable para el alcance del proyecto que describe el aviso.

## d) Cuéntanos brevemente sobre una solución Full Stack que hayas desarrollado con React/TypeScript y Node.js. ¿Cómo diseñaste la integración entre frontend, backend y APIs, y qué decisiones tomaste para asegurar escalabilidad, seguridad y mantenibilidad?

Construí una aplicación para reemplazar una planilla Excel de novedades de turno en operaciones industriales por un sistema web trazable, con exportación a un Data Lake (proyecto público: github.com/goviedodev/niuro). Frontend en Next.js 14 (App Router) con React 18 y TypeScript; backend en NestJS 10 con TypeScript, expuesto como API REST.

**Integración frontend-backend-APIs:** todo el tráfico del frontend pasa por un único wrapper `fetch` tipado (`lib/api.ts`) que agrega la URL base, adjunta el token Bearer y traduce los errores de validación del backend (arreglos de mensajes por campo del `ValidationPipe`) a texto legible en la UI — un solo punto de contacto con la API, no llamadas sueltas repartidas por los componentes.

**Escalabilidad:** la persistencia queda detrás de un Repository (hoy un archivo JSON; documenté el punto exacto de reemplazo por TypeORM/Prisma + PostgreSQL sin tocar servicios ni controladores), y la autenticación es JWT sin estado, lo que permite escalar el backend horizontalmente sin sesión compartida. Los `Dockerfile` son multi-etapa (build con devDependencies, runtime con imagen mínima y usuario sin privilegios).

**Seguridad:** validación server-side con `class-validator` y `ValidationPipe` global (`whitelist` + `forbidNonWhitelisted`: descarta y rechaza cualquier campo no declarado), guards de autenticación y de rol (`@Roles` + `RolesGuard`) que se evalúan en el servidor —la UI solo oculta el botón de exportar, el backend igual devuelve 403 si se fuerza la llamada—, el autor de cada registro se toma del JWT y nunca del payload del formulario, y el mensaje de login es genérico para no permitir enumerar usuarios.

**Mantenibilidad:** estructura modular por dominio (auth, novedades, ingesta), pruebas unitarias en Jest sobre los dos servicios críticos, y el mismo pipeline de CI/CD corriendo en paralelo en GitHub Actions y Azure Pipelines (build + test de frontend y backend). Los límites del demo frente a un entorno productivo (login vs. Azure AD/Entra ID, persistencia en archivo vs. base de datos, secretos en `.env` vs. Key Vault) quedan documentados en el propio código, no ocultos.
