---
name: job-hunter-getonboard
description: Automatiza la búsqueda y postulación a vacantes técnicas de Gonzalo Oviedo Lambert en GetOnBoard (getonbrd.com), completando el flujo de 3 pasos (Experience → Basic → Preview), seleccionando el CV correcto, declarando salario en USD bruto mensual y respondiendo el "Why are you interested" con valor y verificabilidad.
---

# 🛠️ GetOnBoard Job Hunter — Gonzalo Oviedo Lambert

Este módulo implementa el conocimiento y los flujos automatizados para navegar, buscar y postular a vacantes técnicas en **GetOnBoard** (`getonbrd.com`) con la cuenta de Gonzalo Oviedo Lambert, contestando los formularios de postulación con el mayor valor posible y sin inflar el perfil.

## 📌 Estado del Perfil del Candidato (Source of Truth)

- **Cuenta GetOnBoard:** `goviedo.sevenit@gmail.com`, registrada vía LinkedIn, y se opera desde el perfil de Chrome **`Default`**.

  🔴 **Trampa verificada 2026-08-17 (R4): hay DOS cuentas.** Abrir GetOnBoard desde el perfil de Chrome `Profile 17` autentica con el Google de ese perfil (`goviedo.laboral@gmail.com`) y **crea una cuenta nueva y vacía** (0 postulaciones, 0 CVs) en vez de entrar a la real. `goviedo.laboral@gmail.com` es **solo el correo que va escrito dentro de los CVs**, no la cuenta del portal. **Chequeo obligatorio antes de tocar nada:** si `/applications` dice *"You haven't applied to any job yet"*, estás en la cuenta equivocada — salir y entrar con `sevenit`.

  ⚠️ La extensión **Claude in Chrome se instala por perfil de Chrome** y solo está en `Default`. Para operar otro perfil hay que instalarla y autenticarla ahí, y luego elegir el navegador con `select_browser`.
- **Teléfono en perfil:** `+56963723603` (corregido en R4; estaba mal como `+5659723603`, 8 dígitos tras el 56 — imposible para un móvil chileno, los reclutadores no podían llamarlo) · **GitHub:** `goviedodev` (conectado y verificado) · **Ubicación:** Limache, Chile (GMT-4).
- **Titular del perfil** (`description_es` / `description_en`, máx. 255): estaban **cortados a media frase** hasta R4. Vigentes:
  - ES: `Ingeniero de Software Senior · Backend Java y Spring Boot · Desarrollo asistido por IA agéntica`
  - EN: `Senior Software Engineer · Java & Spring Boot Backend · AI-Augmented Development`
- **Seniority** (`webpro_seniority_ids`): **Senior + Expert**. Estaba vacío hasta R4, lo que dejaba el perfil fuera de los filtros por seniority de los reclutadores.
- **Año de titulación:** el `academic_background` del portal registra **2005–2009, Universidad del Bío Bío, Concepción**. `cv.md` no lo trae — usar este dato en vez de esquivar la pregunta.
- **Experiencias validadas** (mismas del CV maestro `cv.md`):
  1. *Te Llevo App* | **Architect, Lead Software Engineer** | Mar 2024 - May 2026 (Elixir/Ash, Java 21, Spring Boot, GCP, Flutter).
  2. *Perficient - Caterpillar* | **Java Associate Developer** | Ene 2022 - Dic 2023 (Java 21, Spring Boot, e-commerce global).
  3. *Citibank* | **Java Specialist** | Ene 2021 - Dic 2022 (Java, Oracle SQL, Spring Beans, WebSphere).
  4. *Seven IT SpA* | **Tech Lead & Lead Software Engineer** | Ene 2017 - Dic 2020 (Spring Boot, PostgreSQL, Google Cloud).
  5. *WebClass, Creasys, Coopeuch, Others* | **Java/Senior Developer** | Ene 2008 - Dic 2017 (Java, Struts, Hibernate, PostgreSQL, Oracle, AS/400).
- **Restricciones globales del proyecto:** prohibido "CTO"/"Co-founder" (usar "Tech Lead" / "Lead Software Engineer"); prohibido inventar experiencia o cifras no verificables (ver `AGENTS.md`).

### 📄 CVs ya cargados en GetOnBoard (`select#job_application_resume_id`)

Verificado en sesión real (2026-08-03). El CV por defecto preseleccionado es **"Spring Boot Java Developer and Agentic Coder" (value 973024)** — usarlo salvo que la oferta amerite otro:

| value | Nombre en el portal |
|---|---|
| 973024 | **Spring Boot Java Developer and Agentic Coder** (default recomendado) |
| 935668 | Spring Boot Java Developer and Fullstack React, Vue, and Angular |
| 971981 | Spring Boot Java Arquitect |
| 385644 | CV.pdf |
| 904230 / 904830 / 904929 / 935860 | CVs por empresa (BC Tecnología, 2BRAINS, Coderslab, Khipu) |

Si se genera un CV nuevo con el pipeline (Tareas 3–8 de `AGENTS.md`), se puede subir en el paso Basic con el enlace **"Upload a new resume"**.

---

## 🌐 Mapa del sitio (URLs verificadas)

| URL | Contenido |
|---|---|
| `https://www.getonbrd.com/myjobs` | "Jobs for you" — recomendaciones personalizadas con filtros (Programming, Seniority, ubicación, modalidad, rango salarial, tags) |
| `https://www.getonbrd.com/jobs/programming?q=<keyword>` | Búsqueda por keyword dentro de la categoría Programming (ej. `?q=java`). ⚠️ `/jobs-programming/java` da **404** |
| `https://www.getonbrd.com/jobs/programming/<slug>` | Detalle de la oferta |
| `https://www.getonbrd.com/jobs/<slug>/applications/new` | Inicio del formulario de postulación (paso 1) |
| `https://www.getonbrd.com/applications` | **Mis postulaciones — única fuente de verdad** del estado |
| `https://www.getonbrd.com/resumes` | Gestión de CVs subidos |
| `https://www.getonbrd.com/invitations` | Invitaciones de empresas |

**Ventajas del portal:** el salario (USD bruto mensual) es visible en la parrilla y el detalle; el número de postulantes aparece en el detalle como `"N applications"`; no hay killer questions estilo Computrabajo (el formulario es estándar de 3 pasos).

---

## ✅ Detección de "ya postulado" (verificado 2026-08-03)

1. **En el detalle de la oferta — detector confiable:** el botón `a#apply_bottom` cambia de texto:
   - `"Apply now"` → **no postulada** (href termina en `/applications/new`).
   - `"See your application"` → **ya postulada** (href apunta a `/applications/<hash>`).
   ```javascript
   (()=>{const b=document.getElementById('apply_bottom');
     return b ? b.innerText.trim() : 'SIN_BOTON';})()
   ```
2. **Baseline y cierre — fuente de verdad:** `https://www.getonbrd.com/applications`. Cada fila lista título, empresa, mensajes, **Status** (`ENVIADA`, `VISTA`, `RETIRADA`, `PROCESO FINALIZADO`, `BORRADOR`), ubicación y fecha. Tomar SIEMPRE un baseline de esta página **antes** del loop y releerla al cierre: solo el delta cuenta como postulado en la sesión.

   🔴 **Tres trampas al leerla (verificadas 2026-08-17, R4):**
   * **Se renderiza client-side**: `fetch` + `DOMParser` devuelve **cero filas**. Hay que leerla en la página viva.
   * **El estado está en mayúsculas solo por CSS** (`text-transform`): `innerText` da `ENVIADA` pero `textContent` da el original en minúsculas. Filtrar por `innerText` o con regex case-insensitive; si no, el filtro devuelve 0 y parece que no hay postulaciones.
   * **Paginación por `button.next_page`** ("Siguiente →") y su par "Anterior". Son `BUTTON`, no anchors: no hay `href` que seguir, hay que clicarlos. En R4 eran 2 páginas (60 + 29 = **89 filas**).
3. En la parrilla de búsqueda las tarjetas **no** marcan lo postulado de forma fiable: no decidir por la parrilla.

---

## 🧑‍💼 El perfil (`/webpros/edit`) — reglas verificadas 2026-08-17 (R4)

🔴 **El `professional_background` del PERFIL debe ser siempre NEUTRO.** El portal lo reinyecta tal cual en cada postulación futura. Hasta R4 contenía literalmente una carta dirigida a otra empresa — ES: *"Postulo con mucho interes al cargo de Back-End Developer (Java/Spring Boot) en **42Labs**… Atentamente, Gonzalo Oviedo Lambert"*; EN: *"…role at **TiMining**"* — y además sin tildes, secuela del workaround de apóstrofos del shell. Toda postulación posterior llegó con una carta dirigida a la empresa equivocada. **Sin nombre de empresa, sin nombre de cargo, sin despedida.** La personalización por oferta va en el paso 1 del formulario, que es una copia editable.

🔴 **El submit por JavaScript NO guarda y NO avisa.** `document.querySelector('#commit').click()` envía el formulario como **GET** a `/webpros/<slug>` (responde 404) y **descarta todos los cambios en silencio**: parece que navegó bien y al volver a `/webpros/edit` está todo como antes. El form es `method=post` con `_method=patch`.
**Solución:** pulsar el botón *"Guardar todos los cambios"* con un **clic real de mouse** sobre sus coordenadas, tras `scrollIntoView({block:'center'})`. Con eso redirige a `/misempleos` con el mensaje de cambios guardados. **Verificar siempre releyendo `/webpros/edit`.**

Campos del perfil: `description_es`/`description_en` (titular, 255), `trix-professional_es`/`_en` → hidden `professional_background_es`/`_en`, `trix-academic_background_es`/`_en`, `webpro_phone`, `webpro_country`, `webpro_english_level`, `webpro_seniority_ids` (multi-select), `webpro_linkedin`, `webpro_gitlab`, `webpro_portfolio`. GitHub se conecta por OAuth, no por input.

## 📝 Flujo de postulación (3 pasos, verificado en sesión real)

Al abrir `/jobs/<slug>/applications/new`:

### Paso 1 — Experience (`job_application[step]=experience`)
- Dos editores **Trix** (rich text) cuyos valores viven en inputs hidden:
  - `trix-editor#trix-professional` → `input[name="job_application[professional_background]"]` — **300–2000 caracteres**. Viene **prellenado** con el texto guardado de Gonzalo (carta de valor: 15+ años Java/Spring Boot, GCP/DevOps, bases de datos, y el diferencial *AI-Augmented Coder* con harnesses de agentes Pi.dev/opencode). El portal lo guarda para futuras postulaciones.
  - `trix-editor#trix-academic_background` → `input[name="job_application[academic_background]"]` — prellenado con Universidad del Bío Bío 2005–2009.
- **Adaptar el primer párrafo del professional background al cargo de la oferta** (el texto guardado puede nombrar otro puesto — verificado: mencionaba "Senior Full-Stack Software Developer" al postular a "Java Developer"). Editar vía Trix, no el hidden directo:
  ```javascript
  (()=>{const t=document.getElementById('trix-professional');
    // t.editor.loadHTML('<div>...</div>') reemplaza todo el contenido
    return t.editor ? 'editor listo, chars: '+t.textContent.length : 'sin editor';})()
  ```
- Hay un hidden `input#question-answers[name=answers]`: si la empresa agregó preguntas propias aparecerán en esta pantalla — leerlas y responder con la verdad del perfil (misma política anti-inflado de siempre).
- Botón **`#submit-btn` ("Next")** → crea/actualiza un **borrador** y navega a `/applications/<hash>/edit?step=basic`.
- Validación del portal: "Please add more text." / "Please remove text." si el largo queda fuera de 300–2000.

### Paso 2 — Basic information (`step=basic`)
| Campo | Detalle |
|---|---|
| `select#job_application_resume_id` | CV a adjuntar (default 973024). Si se salta, la empresa ve el resume por defecto del perfil |
| `input#job_application_expected_salary` (number, required) | **Salario bruto mensual en USD** (ver tabla de anclaje abajo) |
| `textarea#reason-to-apply` (required) | "Why are you interested in working at X?" — **50–1000 caracteres** |
| `input#confirm_residency` (checkbox, required) | ⚠️ **Solo en ofertas localizadas.** "I certify that I have a legal work permit in Chile" — veraz para Gonzalo. Ver abajo |
- Botón **"Next: Review and send »"** (`#submit-btn`).

🔴 **Trampa verificada 2026-08-14 — `#confirm_residency`:** cuando la oferta es local (Chile), aparece un checkbox obligatorio. Mientras no esté marcado, **`#submit-btn` queda `disabled` y el clic no hace absolutamente nada, sin mensaje de error visible**. Diagnosticar siempre así antes de asumir que la navegación falló:
```javascript
(()=>{const f=document.querySelector('form');
  return JSON.stringify([...f.querySelectorAll('input,select,textarea')]
    .filter(e=>!e.checkValidity()).map(e=>(e.id||e.name)+': '+e.validationMessage));})()
```

### Paso intermedio — Questions (`step=questions`, **solo si la empresa agregó preguntas**)

🔴 **Localizar cada textarea por `previousElementSibling`** (2026-08-14): el enunciado de la pregunta es el hermano previo del `textarea`. Buscar subiendo por los ancestros con `innerText.indexOf(pregunta)` hace que **varias preguntas resuelvan al mismo elemento** y las respuestas se pisan entre sí. `maxlength` real: **1500**.
```javascript
const byQuestion = n => [...document.querySelectorAll('textarea')]
  .find(t => t.previousElementSibling && t.previousElementSibling.innerText.indexOf(n) >= 0);
```
El flujo **no siempre es de 3 pasos**: cuando la empresa añade preguntas propias son 4 (`1 Experience → 2 Basic information → 3 Questions → 4 Preview`). Verificado el 2026-08-10 en *Sr React Developer (Smith)*, que preguntaba *"¿Tienes experiencia trabajando en inglés?"* con checkboxes `Sí / No / No, pero puedo mantener conversaciones sin problemas`. Responder con la verdad del perfil y avanzar con `Next: Review and send »`.

### Paso 3 — Preview (⚠️ **es un MODAL, no una página** — corregido 2026-08-10)
- Tras `Next: Review and send` el portal redirige a `/applications?job_application_preview=true#<hash>` y abre un **modal**. **La postulación queda en `DRAFT` hasta pulsar `Send application now` dentro de ese modal.** Verificado: al no pulsarlo, la postulación a LemonTech quedó en DRAFT y no se envió nada.
- 🔴 **Ese botón NO se encuentra con `querySelector` desde `eval`** (devuelve lista vacía), pero **sí aparece en el snapshot de accesibilidad**. Localizarlo y pulsarlo con un clic real:
  ```bash
  chrome-devtools-axi snapshot --full | grep "Send application now"   # → uid
  chrome-devtools-axi click @<uid>
  ```
- ⚠️ La URL `.../edit?step=preview` **no** lleva al preview: rebota al paso 1. Para retomar un borrador usar `.../edit?step=basic` y avanzar con `#submit-btn`.
- **Cierre**: releer `/applications`, contar las filas con la fecha del día y comprobar que **no queda ninguna fila en `DRAFT`**.
- Muestra el resumen completo. Recién el botón final de esta pantalla **envía** la postulación y notifica a la empresa.
- ⚠️ **La postulación es una acción irreversible hacia un tercero: confirmar con Gonzalo antes del envío final de cada oferta.** Los borradores de los pasos 1–2 son inocuos (no notifican a la empresa) y quedan retomables en la misma URL `/edit`.

---

## 💰 Pretensión salarial (USD bruto mensual)

GetOnBoard pide el salario como **bruto mensual en USD**. Rango de referencia de Gonzalo: **$1.800.000 – $3.000.000 CLP líquidos** (≈ segun conversión y carga tributaria, **2.200 – 3.500 USD brutos** aprox. a ~950 CLP/USD).

**Regla n.º 1:** si la oferta publica rango salarial (GetOnBoard casi siempre lo muestra), **anclar dentro del rango publicado**, apuntando al tercio superior si el cargo es Senior/Lead.

Si no hay rango publicado, anclar por cargo:

| Cargo del aviso | USD bruto mensual a declarar |
|---|---|
| Arquitecto / Tech Lead / Jefe de Desarrollo | 3500 |
| Senior / Staff / Especialista | 3000 |
| Desarrollador (sin seniority) / Full Stack | 2600 |
| Semi Senior | 2200 |

Descartar ofertas cuyo techo publicado quede bajo **~1900 USD/mes** (equivalente al piso de $1.800.000 CLP líquidos).

## 💬 "Why are you interested…" (50–1000 chars) — plantilla

Personalizar SIEMPRE con 1–2 datos concretos de la oferta (stack, dominio, empresa). Base:

> Me interesa porque el desafío calza con mi trayectoria: más de 15 años construyendo backend Java/Spring Boot (hasta Java 21 / Spring Boot 3) en banca, e-commerce global y startups, con GCP, Docker y CI/CD. Además integro IA agéntica (harnesses como Pi.dev) en mi flujo diario de desarrollo, manteniendo criterio de arquitectura y calidad. Puedo aportar desde el día uno en [tecnología/dominio específico de la oferta].

Validar longitud antes de enviar (el contador del portal es visible junto al textarea).

---

## 🌐 REGLA DE IDIOMA (obligatoria, verificada 2026-08-03)

> **CAUTION AND RULE:** "Cuando las preguntas son en inglés, o dice *sent in english*: **ENVÍA LAS RESPUESTAS EN INGLÉS**. Ahora si las preguntas están en español, **ENVÍA LAS RESPUESTAS EN ESPAÑOL**."

Cómo aplicarla en cada postulación, ANTES de enviar:

1. **Detectar el idioma de la oferta**: el campo `lang` de la API (`lang: en` → inglés) o el idioma dominante de la descripción. Ojo: el título puede estar en español y la oferta ser en inglés (caso Checkr).
2. **Detectar instrucciones explícitas**: si la descripción dice "CV en inglés", "apply in English", "sent in English" o similar → TODO en inglés (cover letter PROF_EN, reason, respuestas).
3. **Detectar el idioma de cada pregunta** de la empresa: preguntas en inglés → responder en inglés; preguntas en español → responder en español. Nunca mezclar (no enviar cover letter en español con respuestas en inglés a una oferta `lang: en`).
4. Si un draft quedó en el idioma equivocado, **rehacerlo antes de enviar** (reabrir con el hash `/jobs/<slug>/applications/<hash>/edit?step=experience` y reemplazar cover letter + reason + respuestas).

Casos reales: Checkr (`lang: en`, pide CV en inglés) e Improving `java-developer-ssr` (`lang: en`, inglés B2/C1 excluyente) requieren postulación 100% en inglés aunque el aviso mezcle español.

---

## 🏠 Modalidad: filtro obligatorio

Gonzalo reside en **Limache, Región de Valparaíso**. GetOnBoard etiqueta cada oferta como `Remote`, `(Hybrid)` o `(In-office)`:
- ✅ **Remote** (cualquier alcance que incluya Chile: "Any location", "South America", "Chile") — prioridad.
- ✅ **Hybrid (Santiago)** — aceptable.
- ❌ **In-office** — descartar.

Verificar además la sección **"Remote work policy"** del detalle: algunas ofertas "Remote" restringen el país (ej. "Remote (Brazil)", "Remote (Mexico)") — descartar si Chile no califica.

## 🚫 Filtro de afinidad: no postular por llenar cupo

Descartar avisos cuyo stack excluyente Gonzalo no domina, aunque el título suene afín: **.NET / C#**, **PHP**, **Cobol**, **Salesforce**, **Murex**, **Dynamics 365**, **Golang**, **Python/Django/Vue como core**, **Ruby on Rails como core**, QA, BI, ETL, SAP, Odoo, IBM Openpages, soporte técnico.

Cuando el aviso pide algo que Gonzalo no tiene pero el resto encaja, **declarar el gap con honestidad** en el professional background o en las preguntas: gaps reales confirmados — **Kubernetes en producción** (usa Docker + Cloud Run), **Terraform/Ansible** (usa Pulumi), **AWS CDK/CloudFormation** (su IaC es GCP), **ML/MLOps/SageMaker**, **LangChain/LlamaIndex** (integra LLMs a bajo nivel), **Vue.js**, **.NET/C#**, **Redshift**.

---

## 🔌 Conectar el navegador (Chrome 150 — verificado 2026-08-14)

`--remote-debugging-port` **ya no funciona sobre el perfil por defecto** (`DevTools remote debugging requires a non-default data directory`). Copiar el perfil tampoco es viable (contiene cookies y credenciales). La vía soportada:

1. Lanzar Chrome con el perfil del candidato **pasando el bus de sesión**, o el llavero falla y se pierde la sesión iniciada:
   ```bash
   DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
     google-chrome --profile-directory="Profile 17" https://www.getonbrd.com/applications
   ```
   `Profile 17` = `goviedo.laboral@gmail.com` (verificable en `~/.config/google-chrome/Profile 17/Preferences` → `account_info[0].email`).
2. **Pedir a Gonzalo** que active `chrome://inspect/#remote-debugging` en esa ventana (requiere su consentimiento manual; no es automatizable).
3. Operar con `CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1` en **cada** invocación:
   ```bash
   CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1 chrome-devtools-axi eval '...'
   ```
   `curl http://localhost:<puerto>/json/version` devuelve **404** en este modo: es lo esperado, la conexión va por WebSocket. No es señal de fallo.

⚠️ La salida de `chrome-devtools-axi eval` está **capada en ~8060 caracteres y se trunca en silencio**. Para inventariar el catálogo, paginar la API con `per_page=20` devolviendo TSV compacto, no JSON.
⚠️ `UID` es variable de solo lectura del shell: usar `SENDUID` u otro nombre al capturar el uid del botón Send.

## 📡 Inventario por API (mucho más barato que la parrilla HTML)

`GET /api/v0/categories/programming/jobs?per_page=20&page=N` (mismo origen, con sesión) entrega por oferta: `title`, `remote_modality`, `remote_zone`, `countries`, `lang`, `min_salary`, `max_salary`, `published_at`, `applications_count`, `seniority` y `tags`. 324 ofertas vigentes en 20 páginas (2026-08-14). Permite filtrar modalidad, techo salarial y afinidad **antes** de abrir un solo detalle; luego confirmar el estado real con `#apply_bottom`.

## 🧰 Herramientas del Harness (browser_*)

> 🔴 **Corregido el 2026-08-10:** en este harness el navegador se controla con **`chrome-devtools-axi`**, no con `browser_*`. Equivalencias: `open <url>`, `snapshot [--full]`, `eval '<js>'`, `click @<uid>`, `fill @<uid> <texto>`, `upload @<uid> <path>`. Para los Trix sigue aplicando `t.editor.loadHTML(...)` vía `eval`. **Cuidado con los apóstrofos**: un `'` dentro del JS (p. ej. `Caterpillar's`) rompe el comando con `parse error` al pasarlo entre comillas simples desde el shell — redactar sin apóstrofos.

La tabla original (harness con `browser_*`) se conserva como referencia:

| Acción | Herramienta |
|---|---|
| Abrir URL | `browser_navigate` (⚠️ ver quirk abajo) |
| Ver estructura / refs | `browser_snapshot` |
| Ejecutar JS (lectura o navegación) | `browser_execute_js` — envolver sentencias en IIFE `(()=>{...})()`; un `return` suelto de varias líneas falla |
| Llenar campos | `browser_fill` por `ref`; para los **Trix editors usar `t.editor.loadHTML(...)`** vía JS, no el hidden input |
| Clic | `browser_click` por `ref`, o `document.getElementById('submit-btn').click()` vía JS |
| Subir CV nuevo | `browser_upload_file` sobre el input de "Upload a new resume" |

**⚠️ Quirk verificado (2026-08-03):** en getonbrd.com `browser_navigate` suele devolver `cdp_error ... reading 'scrollWidth'`, **pero la navegación SÍ se ejecuta**. Confirmar con `browser_page_info` en vez de reintentar. Alternativa estable: `(()=>{window.location.href='<url>'; return 'nav';})()` con `browser_execute_js` + `browser_wait` de 3 s.

## 🔁 Loop completo por oferta

```
[0] BASELINE: leer https://www.getonbrd.com/applications y guardar la lista previa
    ↓
buscar en /jobs/programming?q=<keyword> (y /myjobs) → recolectar slugs con salario y fecha
    ↓
abrir detalle /jobs/programming/<slug> → esperar ≥3 s
   → #apply_bottom dice "See your application"? → YA POSTULADA: saltar
   → leer el aviso: ¿In-office? ¿Remote que excluye Chile? ¿stack excluyente? ¿techo < 1900 USD?
        → sí a cualquiera: SALTAR (registrar motivo del descarte)
   → clic "Apply now" (#apply_bottom)
   → PASO 1: adaptar párrafo inicial del professional background al cargo,
             responder preguntas de la empresa si las hay, verificar 300–2000 chars → Next
   → PASO 2: seleccionar CV (default 973024), salario USD según tabla/rango publicado,
             "Why are you interested" personalizado 50–1000 chars → Next: Review and send
   → PASO 3: revisar preview → CONFIRMAR CON GONZALO → enviar
    ↓
[N] CIERRE: releer /applications y comparar contra el baseline.
    Solo el delta (nuevas filas SENT) cuenta como postulado en esta sesión.
```

## 📊 Bitácora de estadísticas (obligatorio actualizar al cierre de cada ronda)

`autopostulacion/getonboard/estadisticas.txt` — archivo vivo con el embudo, el histórico por ronda, los descartes con su motivo y los gaps declarados. Al terminar cada ronda registrar como mínimo:
1. Baseline → cierre de `/applications` con el delta exacto (título + empresa + fecha).
2. Las ofertas descartadas con el motivo concreto (modalidad, país, stack, renta).
3. Cualquier gap nuevo declarado en el formulario.
4. Actualizar también `cv_job_links.md` (Tarea 7 de `AGENTS.md`) con Portal = **GetOnBoard** para cada postulación enviada.
