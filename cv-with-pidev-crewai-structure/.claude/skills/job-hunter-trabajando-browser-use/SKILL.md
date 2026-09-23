---
name: job-hunter-trabajando-browser-use
description: Automatiza la postulación en Trabajando.cl usando browser-use/browser-harness (https://github.com/browser-use/browser-use) conectado por CDP al Chrome real de Gonzalo (Profile 17), como alternativa a chrome-devtools-axi. Úsalo cuando el usuario pida explícitamente "browser-use" para Trabajando.cl.
---

# 🐴 Trabajando.cl Job Hunter — vía browser-use

Módulo hermano de [[job-hunter-trabajando]] (que usa `chrome-devtools-axi` sobre un Chrome aislado). Este skill cubre el **mismo portal y los mismos criterios de filtrado/respuestas**, pero con **browser-use** (paquete `browser-use`, que instala el CLI `browser-use` — en realidad un wrapper de `browser_harness`) conectado por CDP al **Chrome real del usuario**, no a una instancia aislada.

**Cuándo usar este skill en vez de `job-hunter-trabajando`:** solo cuando el usuario pide explícitamente "browser-use" / "https://github.com/browser-use/browser-use" y prohíbe `chrome-devtools-axi` o Claude-in-Chrome. Verificado funcional end-to-end el 2026-08-29 (postulación real enviada a WOM S.A.).

**Comparte con `job-hunter-trabajando`:** criterios de filtrado (modalidad híbrida/remota, renta $1.800.000–$3.000.000, afinidad técnica), banco de respuestas estándar, y todas las lecciones de DOM de Trabajando.cl que siguen aplicando (formulario duplicado, botón de envío real). Léelo primero para el contexto de negocio; este documento es solo la capa de herramienta.

---

## ⚠️ Cuenta correcta: Chrome Profile 17, NO `~/.chrome-profiles/jobhunt`

`goviedo.laboral@gmail.com` vive en el **Chrome principal y real del usuario** (`~/.config/google-chrome`), bajo **`Profile 17`**. Ver [[chrome-profile-17-goviedo-laboral]] y [[indeed-cuenta-y-bloqueo-sms]].

**NO uses** el perfil aislado `~/.chrome-profiles/jobhunt` — está logueado en una cuenta Google **distinta** (`gonzalo.oviedo.dev@gmail.com`). Lanzar una instancia nueva de Chrome con ese `--user-data-dir` no da acceso a la identidad correcta. Verificado el 2026-08-29: llevó a pedir confirmación al usuario dos veces antes de encontrar el perfil correcto.

**Cómo conectar al perfil correcto:**

1. El Chrome principal del usuario ya corre con CDP alcanzable sin flags extra (mismo mecanismo que usa `chrome-devtools-axi`/Claude-in-Chrome).
2. Si Profile 17 no tiene ya una ventana abierta, ábrela dentro de la instancia que ya corre (no lanza un proceso nuevo, solo abre una ventana del perfil pedido vía IPC):
   ```bash
   google-chrome-stable --profile-directory="Profile 17" "https://www.trabajando.cl/" &
   disown
   ```
3. Conecta browser-use al **daemon por defecto** (sin `BU_CDP_URL`, que apuntaría a una instancia aislada distinta):
   ```bash
   source <ruta-venv>/bin/activate
   unset BU_CDP_URL
   ```
4. **CDP no distingue perfiles** — el daemon ve TODAS las pestañas de TODOS los perfiles abiertos en esa instancia de Chrome (trabajo, familia, finanzas, etc., mezclados). Nunca operes sobre "la pestaña actual" a ciegas: guarda el `target_id` exacto de la pestaña que tú abriste y pásalo explícitamente a cada llamada (`switch_tab(target_id)` antes de cada bloque de trabajo, `target_id=...` en `js(...)` cuando haga falta).
5. **Verifica la identidad antes de cualquier acción irreversible**: lee `document.body.innerText` en `/mi-curriculum` y confirma el teléfono `+56963723603` y el email `goviedo.laboral@gmail.com` antes de postular.

---

## 🔧 Setup del entorno browser-use

Python 3.11+ requerido (el `pip3` del sistema puede apuntar a un Python más viejo — usar `python3 -m venv`, nunca asumir que `pip3` resuelve al intérprete correcto).

```bash
python3 -m venv <proyecto>/.venv-browser-use
source <proyecto>/.venv-browser-use/bin/activate
pip install --upgrade pip -q
pip install browser-use -q
```

Esto instala `browser-use` (el paquete "make websites accessible for AI agents") que a su vez trae `browser-harness` — el motor real de control CDP con un CLI de scripting tipo REPL. **No hace falta Playwright ni `playwright install`**: browser-harness controla Chrome directo por CDP, sin lanzar navegadores propios cuando ya hay uno corriendo.

Diagnóstico:
```bash
browser-use --doctor
```

---

## 📜 Patrón de invocación

Cada comando es un heredoc de Python con helpers pre-importados (`new_tab`, `goto_url`, `switch_tab`, `js`, `click_at_xy`, `page_info`, `capture_screenshot`, `cdp`, `list_tabs`, `close_tab`, etc.):

```bash
source <venv>/bin/activate
unset BU_CDP_URL
timeout 60 browser-use <<'PY'
switch_tab("<target_id>")
print(page_info())
PY
```

**Gotchas verificados 2026-08-29:**

- **`js(...)` mantiene contexto de página entre llamadas** — declarar `const x = ...` en un script y volver a declarar `const x` en el siguiente lanza `Identifier 'x' has already been declared`. Envolver siempre en `(function(){ ... })()`.
- **Cada invocación de `browser-use` es un proceso nuevo** que se conecta al daemon — si un comando se queda sin salida ("Bash completed with no output"), normalmente fue timeout silencioso del wrapper `timeout Ns`; subir el timeout (60-90s) y reintentar, no asumir que falló.
- **`Emulation` puede quedar con un override de dispositivo móvil pegado** de una sesión anterior del daemon, rompiendo el layout desktop del sitio (columna de detalle de oferta con `width:0`). Si `window.innerWidth` da un valor angosto (ej. 732) pese a la ventana real ser ancha, limpiar y fijar tamaño explícito antes de navegar:
  ```javascript
  cdp("Emulation.clearDeviceMetricsOverride")
  cdp("Emulation.setDeviceMetricsOverride", width=1400, height=900, deviceScaleFactor=0, mobile=False)
  ```

---

## 🔁 Flujo de postulación (mecánica DOM verificada)

Coincide en gran parte con lo documentado en [[job-hunter-trabajando]] (formulario duplicado, botón de envío real), con los siguientes matices vistos con browser-use el 2026-08-29:

1. Navegar a `https://www.trabajando.cl/trabajo-empleo/ia/trabajo/<id>-<slug>` (o la búsqueda que corresponda). Leer el detalle con:
   ```javascript
   document.querySelector('.detalleOfertaContainer').innerText
   ```
2. **El botón visible real** ("Postular" o "Postula fácil", según la oferta) es uno entre varios duplicados ocultos en el DOM — filtrar siempre por `offsetParent !== null`:
   ```javascript
   [...document.querySelectorAll('button, a')]
     .filter(b => /postul/i.test(b.textContent.trim()) && b.offsetParent !== null)
   ```
3. Click en sus coordenadas centrales (`getBoundingClientRect()` + `click_at_xy`). Esto abre uno de estos modales (`.modal` con `display:block`), según el estado del CV de la cuenta:
   - **`.modalCompletarCvTrabajando`** — la oferta exige el CV **estructurado nativo** de Trabajando.com (no un archivo subido). Si la cuenta solo tiene un CV tipo archivo, esta oferta **no se puede completar** sin antes construir el CV estructurado (`/mi-curriculum#/informacion-personal`, etc. — ver [[job-hunter-trabajando]] para los 12 gotchas de ese formulario Vue). No forzar; guardar la oferta y pasar a la siguiente, o avisar al usuario si vale la pena construir el CV estructurado.
   - **`.modalPostularConArchivo`** — confirma "Vas a postular con tu archivo `<nombre>.pdf`" y tiene su propio botón "Postular". Click ahí primero.
4. Tras confirmar el archivo (o si la oferta no lo pedía), aparece el modal de preguntas: "Responde las preguntas del reclutador…" con botones **"Comenzar"** / "Guardar empleo y postular más adelante". Click en **"Comenzar"** (de nuevo, filtrando `offsetParent !== null` — hay un duplicado oculto).
5. Se renderiza `.formularioPreguntasOferta` en la misma página. Recolectar TODOS los tipos de campo dentro de ese contenedor (puede haber `<textarea>`, `<input>` numérico y `<select>` de escala 1-5 — un `<select>` sin responder falla el envío en silencio):
   ```javascript
   [...document.querySelector('.formularioPreguntasOferta').querySelectorAll('textarea,input,select')]
     .filter(e => e.offsetParent !== null)
   ```
6. Llenar cada campo con el setter nativo (Vue no detecta `element.value = x` directo):
   ```javascript
   const setv = (el, v) => {
     el.focus();
     Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, "value").set.call(el, v); // o HTMLInputElement.prototype para <input>
     el.dispatchEvent(new Event("input", { bubbles: true }));
     el.dispatchEvent(new Event("change", { bubbles: true }));
   };
   ```
7. Verificar que los contadores "(ingresados: N)" reflejan el texto antes de enviar.
8. **El botón real de envío final tiene clase `w-100`** (no confundir con "Responder", que vive oculto en un offcanvas móvil deshabilitado — ver [[job-hunter-trabajando]] lección específica):
   ```javascript
   [...document.querySelectorAll("button")]
     .filter(x => /^Postular$/i.test(x.textContent.trim()) && x.offsetParent !== null && x.className.includes("w-100"))
   ```
9. **Confirmar SIEMPRE en `/mis-postulaciones`** — buscar la etapa "Enviado" con la fecha de hoy. La URL nunca cambia durante todo el flujo, así que no sirve como señal de éxito.

---

## ✅ Confirmar con el usuario antes de enviar

Postular es irreversible hacia un tercero. Antes del click final de envío, mostrar las respuestas completas de las killer questions y pedir confirmación explícita — no asumir aprobación aunque el usuario haya pedido "postular" en general.

---

## 🚨 El CV-archivo de la cuenta está bloqueado — no se puede subir uno nuevo por postulación

Verificado el 2026-08-29 en `/mi-curriculum#/archivo-cv`: la página dice literalmente **"Tu archivo no es editable y no se puede cambiar"**, y no existe ningún control de reemplazo/subida (`input[type=file]`, botón "Reemplazar archivo", etc.) en toda la página — se confirmó enumerando todos los `button`/`a` visibles. La única acción disponible para cambiar de representación de CV es **"Crear mi currículum"**, que abandona el archivo por completo y migra a la ficha estructurada nativa del portal (el formulario Vue de 12 gotchas documentado en [[job-hunter-trabajando]]) — no es "adjuntar un PDF distinto".

**Consecuencia práctica:** si el usuario pide generar un CV a medida (ej. estilo Harvard, adaptado a una vacante específica vía `AGENTS.md`) para postular en Trabajando.cl, **ese PDF no se puede adjuntar a la postulación** — el portal siempre usa el único archivo ya subido a la cuenta (`cv_gonzalo_generic_es.pdf`, subido el 10/08/2026 en esta sesión). El CV generado queda como documentación/respaldo en la carpeta de la oferta, pero la postulación real sale con el archivo genérico de la cuenta. Confirmar esto con el usuario ANTES de generar el CV a medida (evita trabajo desperdiciado) o, si ya se generó, avisarle del bloqueo antes de enviar y dejar que decida cómo seguir (enviar con el archivo genérico igual / migrar a CV estructurado / no postular por este medio).

## 🚨 Muchas ofertas de esta ronda exigen el CV estructurado nativo, no solo Deloitte

Verificado el 2026-08-29: el modal `modalCompletarCvTrabajando` ("Este empleo solicita un CV Trabajando.com") no es exclusivo de una empresa — apareció en AI Engineer (Deloitte), Ingeniero/a de Soluciones de IA (Empresa Confidencial) y Product Builder Full Stack & IA (Mando Medio), de 6 ofertas probadas en la ronda. **Verificar el tipo de modal ANTES de invertir tiempo redactando respuestas** — un click de prueba en "Postular"/"Postula fácil" revela en segundos si sale `modalCompletarCvTrabajando` (bloqueada) o `modalPostularConArchivo` (sigue adelante), sin comprometer nada (cerrar el modal no registra la postulación).

## 📊 Bitácora

### 2026-08-29 — Primera ejecución con browser-use (prueba + ronda con CV a medida)

Baseline real verificado: **0 postulaciones** en la cuenta (contradice la bitácora de [[job-hunter-trabajando]] que registraba 20 — ver [[trabajando-cl-cuenta-real-vs-bitacora]], probablemente por sesiones efímeras previas que no persistieron en esta cuenta/perfil).

Búsqueda: `https://www.trabajando.cl/trabajo-empleo/ia` (15 ofertas visibles de 232 totales).

| Oferta | Empresa | Resultado |
|---|---|---|
| AI Engineer | Deloitte | ❌ Bloqueada — exige CV estructurado nativo |
| Analista Desarrollador IA Backend Engineer (Python & Azure) | WORLDLAN LTDA. | ⏭️ Descartada — stack Python/Azure/FastAPI/Celery muy alejado del perfil (Java/GCP) |
| **Arquitecto/a Empresarial de Soluciones e IA** | **WOM S.A.** | ✅ **Enviada** — fuerte match (Spring Boot, GCP, microservicios, 7-10 años). 6 preguntas, gap declarado con honestidad en BSS/OSS telecom y Azure. Ver `trabajando/wom-arquitecto-empresarial-soluciones-ia/`. |
| Ingeniero/a de Software IA | Empresas SB (Salcobrand) | ⏸️ Formulario completo (renta $2.700.000, sin ajustes) pero **NO enviada** — el usuario pidió no postular a Salcobrand |
| Ingeniero/a de Soluciones de IA | Empresa Confidencial | ❌ Bloqueada — exige CV estructurado nativo. CV a medida en formato Harvard generado igual (`trabajando/confidencial-ingeniero-soluciones-ia/`) siguiendo el pipeline de `AGENTS.md` en Modo Directo, pero no se pudo adjuntar (ver hallazgo de arriba) |
| Product Builder (Full Stack & IA) | Mando Medio | ❌ Bloqueada — exige CV estructurado nativo. Match muy fuerte (nombra "Claude Code Max" explícitamente) pero inalcanzable sin migrar el CV |
| **INGENIERO AUTOMATIZACION E IA** | **Fundación Arturo López Pérez** | ✅ **Enviada** — 5 preguntas, gaps declarados con honestidad (sin certificaciones RPA ni IA/Cloud formales, compensado con el proyecto RAG propio). Ver `trabajando/falp-ingeniero-automatizacion-ia/`. |

**Total enviadas en esta primera mitad: 2** (WOM, FALP). **Tasa de bloqueo por CV estructurado nativo: 3 de 6 ofertas revisadas (50%)** — mucho más alto de lo esperado.

### Migración al CV estructurado nativo (misma sesión, misma noche)

El usuario autorizó explícitamente migrar la cuenta al CV estructurado nativo ("no me preguntes nada más, toma tú las decisiones"). Pasos y hallazgos:

1. **`Crear mi currículum`** en `/mi-curriculum` dispara una propuesta generada por IA de Trabajando ("Nuestra IA ha generado una propuesta de CV en base a tu archivo") — parsea el PDF existente y prellena Acerca de mí, Experiencia Laboral (solo 3 roles) y Formación Académica. **Revisar con cuidado antes de aceptar**: la propuesta de este caso traía un adjetivo de la lista negra de `AGENTS.md` ("Experto"), una fecha de término incorrecta en el rol vigente, y "Egresado" en vez de "Titulado". Aceptarla como scaffold y corregir después es más rápido que tipear todo desde cero.
2. **`Actividad de la empresa` (Experiencia Laboral) es un campo autocomplete obligatorio** que el parseo de IA deja vacío — sin él, la sección entera queda marcada "Faltan datos" aunque el resto esté completo. Patrón de tres pasos: `el.focus()` vía JS → `type_text(...)` (teclado real, no el setter nativo — con el setter nativo el dropdown no se abre) → esperar ~1.8s → click con el patrón de 3 `MouseEvent` sobre `li.autocomplete-result`.
3. **🚨 El botón "Guardar" puede fallar en silencio sin ningún indicio visible** (sin error, sin excepción JS, cero requests de red disparados) si el formulario tiene un campo requerido que no dispara la validación de forma obvia. Causa raíz encontrada en `#/informacion-adicional`: el radio **"RUN" / "Pasaporte"** nunca queda marcado si solo se rellena el campo de texto del número de documento — sin el radio marcado, el submit no hace nada (0 requests de red, confirmado con `cdp("Network.enable")` + `drain_events()`). **Lección general: after clicking "Guardar", SIEMPRE verificar persistencia navegando a otra ruta y volviendo** — un in-memory value seguirá "presente" en el DOM aunque el guardado haya fallado. La señal de éxito no es consistente entre formularios: `#/acerca-de-mi` e `#/idiomas` redirigen a `#/` tras guardar con éxito; `#/informacion-adicional` y `#/experiencia-laboral` no redirigen incluso cuando SÍ guardaron — no asumir el redirect como señal universal, solo la re-verificación por navegación es confiable.
4. **Los idiomas (`#/idiomas`) no tienen edición in-place** — solo alta/baja. Para cambiar el nivel de un idioma ya agregado: click en la `x` (SVG `fa-xmark`) dentro de su `span.badge` para eliminarlo, luego volver a `#/idiomas` (formulario en blanco) y agregarlo de nuevo con el nivel correcto.
5. **`#/expectativa-de-renta`**: el input real de monto es el **tercer** `input` visible en la página (los dos primeros son el buscador de empleos del header) — indexar por posición, no por placeholder (no tiene).

**Resultado de la migración:** CV estructurado 100% completo, cero "Faltan datos" en el dashboard (`/mi-curriculum`). Esto desbloqueó automáticamente las tres ofertas que antes exigían `modalCompletarCvTrabajando`/`modalCompletarCV`.

### Segunda mitad de la ronda — tras la migración

| Oferta | Empresa | Resultado |
|---|---|---|
| **Product Builder (Full Stack & IA)** | **Mando Medio** | ✅ **Enviada** — desbloqueada. Nombra "Claude Code Max" explícitamente en el aviso. 6 preguntas, gap declarado en Python (nivel funcional). |
| **AI Engineer** | **Deloitte** | ✅ **Enviada** — desbloqueada. 3 preguntas (2 textarea + 1 input renta). Gap declarado: sin título "AI Engineer" formal ni TensorFlow/PyTorch/Scikit-learn; compensado con el proyecto RAG propio. |
| **Ingeniero/a de Soluciones de IA** | **Empresa Confidencial** | ✅ **Enviada** — desbloqueada. 4 preguntas (3 textarea + 1 input renta). El PDF Harvard generado antes de la migración (`trabajando/confidencial-ingeniero-soluciones-ia/`) quedó como respaldo/documentación — la postulación real usa el CV estructurado nativo, ya que el portal no permite adjuntar un archivo distinto por postulación (ver hallazgo de arriba, sigue vigente incluso con CV estructurado). |

**Total tras la migración: 5 postulaciones enviadas** (WOM, FALP, Mando Medio, Deloitte, Empresa Confidencial) sobre un baseline real de 0. Único caso no enviado por decisión explícita del usuario: Empresas SB (Salcobrand) — formulario completo, descartado.

### Tercera ronda — misma noche, instrucción del usuario de ampliar cobertura

El usuario pidió explícitamente ampliar la búsqueda a toda oferta relacionada con "IA, Inteligencia artificial u otras similares para cargos de conocimiento informático". Se probaron ambas queries (`/trabajo-empleo/ia` y `/trabajo-empleo/inteligencia-artificial` — devuelven prácticamente el mismo dataset, ~215-232 resultados) y se paginó con `?pagina=2`.

**Criterios de descarte aplicados en esta ronda** (más allá de los ya documentados):
- **Ausencia del tag "Mixta (Teletrabajo + Presencial)"** se trató como señal fiable de modalidad presencial — el portal es consistente en marcar así toda oferta híbrida/remota; su ausencia (solo "Jornada Completa") descartó varias ofertas aunque no dijeran "Presencial" explícitamente.
- **Requisito de residencia en una región específica** (ej. Consultor IA Senior/Semi-Senior/Trainee/Práctica de ChainLabs, todos exigiendo residencia en Iquique/Tarapacá) descarta de plano, sin importar cuán bueno sea el resto del match.
- **Rol de negocio/liderazgo sin componente técnico hands-on** (ej. "Líder de Transformación Digital e IA" en Seguros SURA, "Ingeniero de Planificación Comercial - Gerencia de IA y Datos" en Consorcio) no cuenta como "cargo de conocimiento informático" pese a mencionar IA — se descartan aunque cumplan modalidad.
- **Stack de Data Science puro** (Databricks, PySpark, MLflow, Scikit-learn/Pandas avanzado, álgebra lineal/estadística — ej. "Especialista Data Analytics" de Líder Bci, "Analista de datos e inteligencia artificial" de Randstad) se trata como mismatch de dominio, no solo de tecnología puntual: el perfil es de ingeniería de software backend, no de ciencia de datos.

**Hallazgo destacado: Coopeuch tenía 4 ofertas de IA abiertas simultáneamente** (Desarrollador de Agentes IA, Ingeniero de IA, Especialista de Operaciones IA, Arquitecto de Soluciones IA) — un mismo empleador puede tener un equipo de IA contratando en varios niveles a la vez; vale la pena revisar TODAS las ofertas de una empresa que aparece una vez en los resultados, no asumir que es la única vacante.

**Nuevas ofertas enviadas esta ronda:**

| Oferta | Empresa | Resultado |
|---|---|---|
| Desarrollador de Agentes IA | Coopeuch | ✅ Enviada — AWS Bedrock/Copilot Studio como gap, compensado con Claude Code y proyecto RAG propio |
| Ingeniero de IA | Coopeuch | ✅ Enviada — match casi literal con su trabajo diario de diseño de prompts/agentes |
| Especialista de Operaciones IA | Coopeuch | ✅ Enviada — gap más honesto de la ronda (no es rol de Ops/SRE en su trayectoria) |
| Arquitecto/a de Soluciones IA | Coopeuch | ✅ Enviada — fuerte match de nivel arquitecto senior |
| Ingeniero de Transformación Digital e IA | Avla Seguros | ✅ Enviada — match muy fuerte, casi idéntico a su proyecto RAG propio |

**Total acumulado de la sesión: 10 postulaciones enviadas** (WOM, FALP, Mando Medio, Deloitte, Empresa Confidencial, Coopeuch ×4, Avla) sobre un baseline real de 0, más 1 formulario completo no enviado por decisión del usuario (Empresas SB/Salcobrand).

### Cuarta ronda — misma noche, instrucción del usuario de postular a 40 ofertas de "java"

**Hallazgo clave: el pool real de Trabajando.cl para "java"/backend en Chile es mucho más chico de lo que sugiere el conteo bruto.** La query `java` reporta 43 resultados, pero la mayoría es ruido por match laxo (bobinador, vendedor técnico de transformadores, técnico en electricidad, ayudante de bodega, técnico enfermería, asistente de activos fijos, etc. — el motor de búsqueda no filtra por relevancia real). Se probaron además `desarrollador-java` (31), `backend-java` (40, ~mismo dataset que `java`), `fullstack` (31), `tech-lead` (15), `microservicios` (15), `software-engineer` (227, pero dominado por ofertas .NET/C#), `programador-java` (9), `spring-boot` (1), `arquitecto-de-software` (12) — todas con solapamiento alto entre sí (son básicamente el mismo universo de ~40-50 ofertas técnicas reales en el portal en un momento dado, no 40 ofertas nuevas por cada query).

**Después de triage exhaustivo, el pool de ofertas Java/backend genuinamente afines (híbrido/remoto + sin exclusión dura de stack) fue de 7, no 40.** Se aplicó igual el mismo rigor de filtrado de siempre:

- **3 ofertas de Michael Page ("Banca (proyecto)")** descartadas de plano — ya estaban marcadas como "Descartadas" en `cv_job_links.md` desde 2026-08-19 por exigir JCL/Mainframe avanzado (exclusión declarada del usuario). No se reabre una exclusión ya resuelta solo porque la bitácora previa resultó tener otros datos stale — la exclusión de JCL en sí seguía vigente y verificada.
- **Descubrimiento nuevo: el tag de modalidad del listado no siempre es confiable.** El caso de ACHS Tech Lead mostraba "Jornada Completa" en el listado pero el cuerpo del aviso decía explícitamente "Modalidad Híbrida". Lección: cuando una oferta por lo demás encaja muy bien pero el tag dice presencial, vale la pena leer el cuerpo completo antes de descartar — el tag no siempre refleja la realidad.
- **"Empresas SB" reapareció** (Líder Técnico en Integraciones) — se confirmó que es Salcobrand, la empresa que el usuario pidió explícitamente evitar en la ronda de IA; se descartó de nuevo sin dudar, sin importar cuán bueno fuera el resto del match.
- **Reposts casi idénticos del mismo empleador** (Perceptual Consultores con 4-5 IDs distintos para el mismo cargo, ENEX S.A. con Tech Lead + Desarrollador Backend + Desarrollador Fullstack todos "Jornada Completa" sin híbrido) — se postuló una sola vez por cargo genuinamente distinto, nunca a duplicados exactos del mismo puesto.
- **Exclusiones duras de stack siguieron aplicando estrictamente**: .NET/C#/VB.NET (varias ofertas), Go/Golang, Python/Django cuando es obligatorio y específico de framework (no solo "Python" genérico), residencia obligatoria fuera de la Región Metropolitana/Valparaíso.

**Ofertas Java/backend enviadas esta ronda (7):** Analista de integraciones y automatización, Ingeniero Desarrollador FullStack (Perceptual Consultores), Ingeniero/a de Software (Caja Los Andes), Tech Lead (ACHS), Desarrollador Full Stack (RYC Consultores), Desarrollador FullStack (Help Seguros), Desarrollador Full-Stack industria automotriz (Empresa Confidencial).

**Total final de la sesión: 17 postulaciones enviadas** sobre un baseline real de 0, más 1 formulario completo no enviado por decisión del usuario (Empresas SB/Salcobrand). **No se llegó a 40** porque el pool real y afín se agotó tras un triage honesto — igual que documentado para otros portales (ver [[job-hunter-computrabajo]] y [[job-hunter-trabajando]]: "el techo realista por ronda es de 3 a 6" en mercados de nicho), Trabajando.cl para Java/backend híbrido en Chile tiene un techo real bajo, no artificial.
