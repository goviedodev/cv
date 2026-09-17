# Comandos del Gem — Referencia rápida

Modos de operación del Gem **Sparring Técnico FullStack** (Google Gemini).
Configuración completa en [gem-gemini.md](gem-gemini.md) · Material de estudio en [guia-entrevista.md](guia-entrevista.md)

---

## Tabla resumen

| Comando | Para qué sirve | Cuándo usarlo |
|---|---|---|
| `/diagnostico` | 8 preguntas rápidas de distintos temas + plan de estudio priorizado | Al empezar, o cada 3–4 días para medir avance |
| `/simulacro [tema] [nivel]` | Entrevista simulada, una pregunta a la vez, con nota y feedback | Cuando ya repasaste y quieres presión real |
| `/repasar <tema>` | Explicación de estudio completa con código y preguntas típicas | Tema que no manejas o que viste hace tiempo |
| `/profundizar <tema>` | Nivel senior: trade-offs, casos borde, qué falla en producción | Tema que ya entiendes y quieres defender a fondo |
| `/ampliar-guia <tema>` | Nueva sección en Markdown para pegar en `guia-entrevista.md` | Cuando detectas un hueco en el documento |
| `/flashcards <tema> [n]` | Tarjetas pregunta/respuesta de 3 líneas | Repaso rápido, metro, día previo |
| `/codigo <ejercicio>` | Ejercicio de live coding con solución comparada | Preparar la ronda de código |
| `/design <problema>` | System design guiado: requisitos → arquitectura → cuellos de botella | Entrevistas de arquitectura o cargos senior |
| `/star <situación>` | Convierte una experiencia tuya en respuesta STAR con números | Preparar las preguntas de comportamiento |
| `/sueldo <situación>` | Guion textual de negociación, listo para decir | Antes de RRHH o al recibir una oferta |

Sin comando, el Gem interpreta la intención y elige el modo solo.

---

## Detalle por comando

### `/diagnostico`
Te hace 8 preguntas cortas de temas distintos y devuelve dónde estás débil, ordenado por prioridad.

> `/diagnostico`

**Devuelve:** preguntas una a una → informe final con fortalezas, 3 huecos concretos y qué estudiar primero.

---

### `/simulacro [tema] [nivel]`
Entrevista simulada. **Una pregunta a la vez**, espera tu respuesta, y recién ahí evalúa.
Niveles: `junior`, `semi`, `senior` (por defecto `senior`).

> `/simulacro seguridad senior`
> `/simulacro kubernetes`
> `/simulacro` ← mezcla todos los temas

**Devuelve por cada respuesta:** nota /10 · qué estuvo bien · qué faltó · la respuesta ideal en 4–6 líneas. Y repregunta como un entrevistador real.
**Al cerrar:** informe con fortalezas, huecos y plan.

---

### `/repasar <tema>`
Repaso de estudio con el formato de la guía.

> `/repasar OAuth2 y PKCE`
> `/repasar virtual threads`
> `/repasar change detection en Angular`

**Devuelve:** Qué es → Cómo lo explico en entrevista (respuesta hablada entre comillas) → Código comentado → Errores comunes → Preguntas típicas. Con 🎯 en lo más preguntado.

---

### `/profundizar <tema>`
Un nivel más arriba de `/repasar`: para cuando el entrevistador te repregunta.

> `/profundizar idempotencia en Pub/Sub`
> `/profundizar por qué falla @Transactional en llamadas internas`

**Devuelve:** trade-offs, casos borde, qué se rompe en producción, cómo se ve en un code review.

---

### `/ampliar-guia <tema>`
Genera una sección nueva en el formato exacto del documento, lista para pegar.

> `/ampliar-guia arquitectura hexagonal`
> `/ampliar-guia WebSockets en Spring y Angular`
> `/ampliar-guia estructuras de datos para live coding`

**Devuelve:** Markdown puro con títulos numerados, tablas, código comentado, 🎯 y "Preguntas típicas", más la indicación de en qué número insertarlo.
**Después:** pega en `guia-entrevista.md` y corre `node build-html.js` para regenerar la página.

---

### `/flashcards <tema> [cantidad]`
Tarjetas de repaso. Respuestas de máximo 3 líneas. Por defecto 15.

> `/flashcards spring security 20`
> `/flashcards kafka`

---

### `/codigo <ejercicio>`
Ejercicio de live coding. Te da el enunciado, te deja resolver, y después compara su solución con la tuya.

> `/codigo agrupar pedidos por cliente con streams`
> `/codigo implementar un rate limiter`
> `/codigo buscador con debounce en Angular`

---

### `/design <problema>`
System design guiado.

> `/design un acortador de URLs`
> `/design un sistema de notificaciones con Pub/Sub`
> `/design el checkout de un e-commerce`

**Devuelve:** primero preguntas de requisitos, luego arquitectura, trade-offs y cuellos de botella.

---

### `/star <situación>`
Convierte una experiencia real tuya en respuesta estructurada.

> `/star cuando bajé la latencia del endpoint de pedidos`
> `/star un conflicto con un compañero por el diseño de la API`

**Devuelve:** Situación → Tarea → Acción → Resultado, con resultados cuantificados y lista para decir en voz alta.

---

### `/sueldo <situación>`
Coaching de negociación con guion textual. Rango de referencia: 2,0–2,3 líquidos, ancla en 2,3–2,5.

> `/sueldo me preguntaron la expectativa en el primer filtro`
> `/sueldo me ofrecieron 1,9 bruto`
> `/sueldo quieren saber mi sueldo actual`

**Devuelve:** la frase exacta entre comillas, lista para decir, aclarando líquido vs bruto.

---

## Rutinas sugeridas

**Sesión de 30 minutos**
1. `/flashcards <tema del día> 10` — calentamiento
2. `/repasar <lo que fallaste>` — cierra el hueco
3. `/simulacro <ese tema>` — 5 preguntas con presión

**Día previo a la entrevista**
1. `/diagnostico` — confirma que no queda nada crítico abierto
2. `/flashcards seguridad 20` — el tema excluyente
3. `/sueldo` — ensaya el guion en voz alta
4. `/simulacro` — 10 preguntas mezcladas, cronometrado

**Cuando encuentras un hueco en el documento**
`/ampliar-guia <tema>` → pegar en `guia-entrevista.md` → `node build-html.js`
