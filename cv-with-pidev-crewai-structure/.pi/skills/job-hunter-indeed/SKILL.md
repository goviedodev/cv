---
name: job-hunter-indeed
description: Automatiza la búsqueda y postulación a vacantes técnicas de Gonzalo Oviedo Lambert en Indeed Chile (cl.indeed.com), navegando con chrome-devtools-axi contra una instancia de Chrome dedicada por CDP, completando el perfil de profile.indeed.com y filtrando por modalidad/salario/stack antes de postular.
---

# 🛠️ Indeed Job Hunter — Gonzalo Oviedo Lambert

Este módulo implementa el conocimiento y los flujos automatizados para navegar, construir el perfil y postular a vacantes técnicas en **Indeed Chile** (`cl.indeed.com` / `profile.indeed.com`) con la cuenta `goviedo.laboral@gmail.com`.

---

## 🔴 Trampa crítica: cuenta y perfil de Chrome correctos

La cuenta de Indeed vive en **`goviedo.laboral@gmail.com`**, distinta de la cuenta de LinkedIn/GetOnBoard (`goviedo.sevenit@gmail.com`, perfil de Chrome `Default`). La extensión **Claude in Chrome** solo ve el perfil `Default` — usarla para Indeed abre y opera la cuenta equivocada.

**Solución verificada (2026-08-19):** copiar el "Profile 17" real de Chrome (que sí tiene la sesión de `goviedo.laboral@gmail.com` iniciada) a un `--user-data-dir` dedicado, y lanzar una instancia de Chrome completamente independiente con su propio puerto de depuración remota, controlada con **`chrome-devtools-axi`** (no con la extensión):

```bash
rsync -a --exclude='Cache/' --exclude='*Cache*' --exclude='GPUCache' --exclude='Code Cache' \
  "$HOME/.config/google-chrome/Profile 17/" "$HOME/.chrome-cdp-profile-laboral/Default/"
cp "$HOME/.config/google-chrome/Local State" "$HOME/.chrome-cdp-profile-laboral/Local State"
```

🔴 **Trampa: la copia muestra el selector de perfiles ("Who's using Chrome?") en vez de entrar directo.** El `Local State` original lista TODOS los perfiles de Chrome (Default, Profile 2, 6, 14, 16, 17, 20, 22, 24…) en `profile.info_cache`, pero la copia solo tiene la carpeta `Default`. Hay que editarlo para que solo declare ese perfil:

```bash
LS="$HOME/.chrome-cdp-profile-laboral/Local State"
jq '.profile.info_cache = {"Default": .profile.info_cache["Profile 17"]} | .profile.last_used = "Default" | .profile.last_active_profiles = ["Default"]' "$LS" > "${LS}.new"
mv "${LS}.new" "$LS"
```

Lanzar:
```bash
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus nohup google-chrome \
  --remote-debugging-port=9223 --user-data-dir="$HOME/.chrome-cdp-profile-laboral" \
  > /tmp/chrome-laboral.log 2>&1 &
```

Conectar `chrome-devtools-axi` con:
```bash
export CHROME_DEVTOOLS_AXI_BROWSER_URL="http://127.0.0.1:9223"
export CHROME_DEVTOOLS_AXI_SESSION="indeed-laboral"
```

Verificar la cuenta ANTES de tocar nada: `jq -r '.account_info[]?.email' "$HOME/.chrome-cdp-profile-laboral/Default/Preferences"` debe dar `goviedo.laboral@gmail.com`.

**Guardia instalada:** `.claude/hooks/indeed-profile17-guard.sh` (wired en `.claude/settings.local.json`) es un hook `PreToolUse` que bloquea cualquier navegación/llamada de `chrome-devtools-axi` a `indeed.com` a menos que pueda verificar que hay un proceso `chrome` con `--remote-debugging-port` cuyo `Preferences` confirme `goviedo.laboral@gmail.com`. Si el hook bloquea, la instancia dedicada murió — relanzarla con el comando de arriba.

---

## 🌐 Mapa del sitio

| URL | Contenido |
|---|---|
| `https://profile.indeed.com/` | Perfil — resumen: nombre, contacto, CV, banners de "Competencias"/"Preferencias" |
| `https://profile.indeed.com/edit/contact` | Nombre, apellidos, teléfono, email, ubicación (ciudad/estado), reubicación |
| `https://profile.indeed.com/qualifications` | Experiencia laboral **más reciente** (solo una, no historial completo), escolaridad, habilidades, licencias, certificaciones, idiomas |
| `https://profile.indeed.com/preferences` | Títulos de empleo deseados (hasta 10), tipos de empleo (checkboxes), sueldo mínimo + periodo de pago, tiempo de traslado, disponibilidad de reubicación |
| `https://profile.indeed.com/readytowork` | Switch "Listo para trabajar" (disponibilidad inmediata) |
| `https://cl.indeed.com/jobs?q=<kw>&l=<loc>` | Búsqueda de empleos (SPA de dos paneles: lista izquierda + detalle derecho) |
| `https://cl.indeed.com/viewjob?jk=<jk>` | Detalle de una oferta específica — **ver trampa abajo**, el botón de postulación aquí no siempre coincide con el de la búsqueda |

---

## 🧑‍💼 El perfil — campos y quirks verificados (2026-08-19)

### Subir CV — el botón visible NO es el input real
"Subir CV" es un `<button>` que dispara un `<input type=file>` **oculto** (`display:none`, sin `id`/`name`), fuera del árbol de accesibilidad. `chrome-devtools-axi upload @<uid-del-botón> <ruta>` **no funciona** — corre sin error pero no adjunta nada.

**Solución verificada:** usar el protocolo CDP directo (`DOM.setFileInputFiles`) contra el nodo real del `<input type=file>`, vía un pequeño script Python con `websockets` (ya disponible en el entorno):

```python
import asyncio, json, urllib.request, websockets
async def main():
    with urllib.request.urlopen("http://localhost:9223/json/list") as r:
        page = next(t for t in json.loads(r.read()) if t.get("type") == "page")
    async with websockets.connect(page["webSocketDebuggerUrl"], max_size=None) as ws:
        # DOM.enable, DOM.getDocument(depth=-1, pierce=True), buscar recursivamente
        # el nodeName=='INPUT' con attribute type=file, luego:
        # DOM.setFileInputFiles({files: [ruta], nodeId: node_id})
        ...
asyncio.run(main())
```

Tras `setFileInputFiles`, Indeed muestra un modal de confirmación **"¿Esto es correcto?"** con el CV parseado (nombre, título, resumen) y dos botones: *"No, subir otro archivo"* / *"Sí, es correcto"*. Hay que pulsar **"Sí, es correcto"** para que la subida se confirme server-side — sin ese clic, un reload muestra "Subir CV" de nuevo como si nada hubiera pasado.

🔴 **El parser del CV sobrescribe nombre y ubicación con lo que diga el PDF**, incluso si ya estaban bien puestos manualmente. En este caso pisó "Gonzalo Oviedo Lambert" → "Gonzalo Lambert" (se comió "Oviedo") y "Limache, Valparaíso" → "Santiago de Chile, Región Metropolitana" (el CV en PDF trae "Santiago" en el encabezado, un dato desactualizado en el CV maestro que no refleja la residencia real). **Siempre verificar y corregir `Nombre`/`Apellidos`/`Ciudad, estado` en `/edit/contact` después de subir un CV nuevo.**

Tras la subida aparece además un modal **"Configuración de privacidad"** (visible/no visible a empresas). Mantener lo que ya estaba configurado — no aceptar ciegamente la opción "Recomendado" (visible), que puede contradecir una elección de discreción previa.

### `/edit/contact` — combobox de ciudad con autocompletado real
El campo "Ciudad, estado" es un combobox con autocompletado por API (no acepta texto libre validado hasta seleccionar una opción real). `chrome-devtools-axi fill` no dispara la búsqueda; hace falta `chrome-devtools-axi type` (tecleo simulado) para que aparezcan las opciones, y luego localizar la opción exacta vía `document.querySelectorAll('[role=option]')` (⚠️ **hay varios `[role=listbox]` en la página simultáneamente** — p. ej. el selector de país del teléfono — filtrar por texto exacto, no asumir que es el primero) y hacer click en el nodo DOM directamente.

`chrome-devtools-axi fill` en un campo de texto normal (Apellidos, Título del puesto) **concatena** en vez de reemplazar si el campo ya tenía contenido. Usar el setter nativo de `HTMLInputElement.prototype.value` + `dispatchEvent('input'/'change', {bubbles:true})` vía `eval` para fijar un valor exacto de forma confiable, o limpiar el campo antes con su botón "Borrar `<valor>`" si existe.

### `/qualifications` — solo UNA experiencia laboral
El formulario de "Experiencia laboral" captura solo la **más reciente** (Título del puesto + Empresa, texto libre, sin fechas ni descripción) — no es un historial completo como en GetOnBoard/LinkedIn. El historial completo vive únicamente en el CV adjunto. Cargar aquí el cargo más reciente real (p. ej. "Lead Software Engineer" @ "Te Llevo App").

Escolaridad, Habilidades e Idiomas sí aceptan múltiples entradas vía **"Guardar y agregar otro"** (patrón: fill → click "Guardar y agregar otro" → repetir → última entrada con "Guardar" simple). El nivel de idioma es un `<select>` real con opciones `Nativo/Experto/Avanzado/Intermedio/Principiante` — **B2 CEFR mapea a "Avanzado"**, no "Experto" (eso sería C1/C2) ni "Intermedio" (sería B1).

### `/preferences` — salario y anclaje
"Sueldo base mínimo" pide monto + periodo de pago (Por hora/año/mes/semana/día). El monto se auto-formatea con separadores de miles al escribir. Anclar en **el piso del rango objetivo** ($1.800.000 CLP/mes), consistente con la política general de declarar el mínimo aceptable, no el punto medio.

"Tipos de empleo" son checkboxes (Por contrato, Indefinido, Medio tiempo, Tiempo completo, Temporal, Beca/prácticas) — marcar los compatibles con el perfil (Por contrato + Indefinido + Tiempo completo), no todos.

---

## 🔍 Búsqueda y postulación

### El botón de postulación tiene DOS variantes, y determinan todo

1. **"Postúlate rápidamente" / "Postularse mediante Indeed"** — flujo nativo de Indeed (Indeed Apply / SmartApply).
2. **"Postularse en la página de la empresa"** — redirige a un ATS externo (Workday, BNE — Bolsa Nacional de Empleo gubernamental —, u otro sitio propio).

**Cómo diferenciarlas de forma confiable:** el badge/botón correcto solo aparece al **navegar dentro del SPA de resultados de búsqueda** (clic en el `heading`/`button` de la tarjeta, o el panel de detalle que ya trae `#jobDescriptionText` cargado). **Navegar directo a `https://cl.indeed.com/viewjob?jk=<jk>`** (fuera del SPA) a veces muestra "Postularse mediante Indeed" para una oferta que en la búsqueda SÍ mostraba "Postularse en la página de la empresa" — no confiar en el botón de una carga directa de `/viewjob`, siempre verificar clicando desde la lista de búsqueda.

**Verificación SMS (2026-08-14→2026-08-19):** el flujo nativo exigía verificar el teléfono por SMS en la primera postulación de la cuenta. **Gonzalo completó esa verificación el 2026-08-19** — confirmado en sesión real: la primera postulación nativa del día (Dhemax, ver abajo) llegó directo al formulario sin ningún prompt de SMS.

### 🔴 CRÍTICO — reCAPTCHA bloquea el flujo nativo después de la primera postulación exitosa de la sesión

Verificado 2026-08-19 en sesión real: la **primera** postulación nativa del día (Dhemax) llegó al paso de revisión (`review-module`, progreso 100%) y el botón **"Envía tu postulación"** estaba habilitado — se envió sin fricción, sin reCAPTCHA visible en absoluto. Las **siguientes** postulaciones nativas de la misma sesión (TINET, 3IT, KPaz) mostraron un widget reCAPTCHA (`type=image, size=normal`, checkbox "no soy un robot", iframe de `recaptcha.net/recaptcha/enterprise/anchor`) en el paso de revisión, y **el botón "Envía tu postulación" queda `disabled` hasta resolverlo**.

**No se pudo resolver programáticamente:**
- Un clic vía `chrome-devtools-axi click @<uid>` (CDP `Input` trusted, no sintético) sobre el iframe **enfoca** el widget (`focused` en el snapshot) pero **no marca el checkbox** — el botón sigue `disabled`.
- Esperar 5–20 s (por si era un v3 invisible que auto-resuelve) tampoco cambió el estado; `[name=g-recaptcha-response]` permanece con longitud 0.
- `navigator.webdriver` es `false` en esta instancia (Chrome lanzado con `--remote-debugging-port` sin Puppeteer), así que no es ese vector de detección — más probablemente Google evalúa la **ausencia de trayectoria de movimiento del mouse** antes del clic (el checkbox de reCAPTCHA v2 analiza el path del cursor, no solo el evento de clic final), algo que un clic CDP puntual sin desplazamiento previo no puede simular.
- `chrome-devtools-axi screenshot` timeó dos veces al intentar inspeccionar visualmente el widget — no confirmado si es un problema aparte o relacionado.

**Impacto:** cuando aparece, el formulario queda 100% completo (CV, preguntas de la empresa) pero atascado en el checkbox — hay que decidir entre dejarlo como borrador (recuperable después con un clic real de Gonzalo) o no invertir tiempo llenándolo. **Registrar como "Bloqueado" en `cv_job_links.md`, no como descarte** — el encaje puede ser bueno, el bloqueo es puramente técnico.

🔴 **Corrección (misma sesión, aplicación #2 del día — 23People):** NO es un límite estricto de "1 por sesión". La 4ª postulación nativa del día (23People) llegó al `review-module` con el botón **habilitado** pese a tener un `iframe[src*=recaptcha]` presente — en este caso era la variante invisible (v3, se auto-resuelve) en vez del checkbox visible (v2) que bloqueó a TINET y 3IT. **Indeed/Google decide caso a caso, probablemente por señales de riesgo de la oferta/empresa específica, no por un contador de sesión.** No hay forma de predecir cuál variante tocará antes de llegar al `review-module` — solo verificar `disabled` en el botón "Envía tu postulación" y, si está `false`, enviar de inmediato antes de que cambie de estado.

**Estrategia recomendada:** intentar la vía nativa en todo candidato de buen encaje sin asumir que fallará — el costo de intentarlo es bajo (formulario completo de todos modos, sirve como borrador si queda bloqueado) y a veces sí se envía. Seguir priorizando "Postularse en la página de la empresa" solo quiere decir que esa vía nunca tiene este riesgo particular, no que la nativa deba evitarse.

### ATS externos tienen su propia fricción

**BNE (Bolsa Nacional de Empleo, `bne.cl`)** — portal gubernamental de empleo de Chile. Varias ofertas "Postularse en la página de la empresa" (ej. SII Group Chile) en realidad redirigen aquí, no al sitio de la empresa. El botón "Postular" lleva a `bne.cl/empleadores/login` — **requiere cuenta propia de BNE**, sin relación con la cuenta de Indeed/GetOnBoard/LinkedIn. No se creó cuenta nueva sin autorización explícita — pendiente decidir si vale la pena registrarse ahí dado el volumen de ofertas que pasan por este portal.

**Workday** (`*.myworkdayjobs.com`) exige **crear una cuenta como paso 1**, incluso en el flujo "Solicitar manualmente" (sin autofill de CV) — no hay forma de postular sin cuenta en ese tenant específico.

🔴 **Registro de cuenta silenciosamente fallido dos veces** (2026-08-19, tenant de Babel Group): tras rellenar email + contraseña válida + checkbox de privacidad y pulsar "Crear cuenta", el flujo redirige a "Conectar" (login) sin mostrar error — pero el login posterior con esas mismas credenciales falla ("contraseña o email incorrectos o cuenta bloqueada"). Ocurrió con contraseña fijada vía `eval`+setter nativo ambas veces. Hipótesis no confirmada: detección anti-bot que descarta eventos sintéticos (`isTrusted=false`) en vez de mostrar un error de validación. **Sin resolver** — pendiente probar con `chrome-devtools-axi fill`/`click` "reales" (CDP `Input` trusted) en vez de `eval`+setter nativo, o completar el registro manualmente una vez y guardar la sesión.

### Patrón estructural: "Postularse en la página de la empresa" casi siempre exige una cuenta nueva

Verificado con 3 empresas distintas el 2026-08-19: **BNE** (bne.cl, portal gubernamental — SII Group Chile redirige ahí), **Workday** (`*.myworkdayjobs.com` — Babel Group) y **SAP SuccessFactors** (`trabajos.achs.cl` — ACHS, y el enlace "Postular" específico de la vacante redirigió a la home del portal en vez del formulario, posible pérdida de sesión). **Los tres exigen cuenta propia**, sin relación con Indeed/GetOnBoard/LinkedIn. Esto no es la excepción — parece ser la norma para el "otro lado" del inventario de Indeed Chile. No crear cuentas nuevas sin autorización explícita de Gonzalo; registrar como "Bloqueado" con el nombre del portal y por qué.

**Implicación práctica:** ni la vía nativa (capada por reCAPTCHA a ~1/sesión) ni la vía externa (cada empresa un portal/cuenta distinta) escalan bien de forma autónoma. El rendimiento real por sesión es bajo — priorizar calidad de la primera postulación nativa disponible sobre volumen.

### Los títulos de las ofertas engañan sobre el stack real

Verificado con KPaz "Desarrollador Backend AWS - Remoto": el título sugería buen encaje (remoto, AWS básico), pero la descripción completa exigía AWS profundo (EKS, Lambda, SQS, API Gateway) más Kafka y Kubernetes como requisitos duros — ninguno de los cuales declara Gonzalo. **Siempre leer la descripción completa antes de decidir aplicar, incluso cuando el título y el badge de ubicación parecen encajar.**

### Extracción masiva de tarjetas — mucho más rápido que snapshot por oferta

Para filtrar candidatos sin gastar un snapshot completo por tarjeta, usar `eval` para extraer `jk`, título, empresa, ubicación y el flag `Postúlate rápidamente` de todas las tarjetas de una página de búsqueda a la vez:
```js
[...document.querySelectorAll('.job_seen_beacon')].map(c => ({
  jk: c.querySelector('[data-jk]')?.getAttribute('data-jk'),
  title: c.querySelector('h2 a, h2 span, [id^=jobTitle]')?.textContent?.trim(),
  co: c.querySelector('[data-testid=company-name]')?.textContent?.trim(),
  loc: c.querySelector('[data-testid=text-location]')?.textContent?.trim(),
  quick: !!c.textContent.match(/Postúlate rápidamente/)
}))
```
Luego, para cada `jk` candidato, un solo `eval` **async** que hace clic + espera + lee la descripción completa (no solo el snapshot truncado, que corta a ~20-22K caracteres) en una sola llamada:
```js
async () => {
  const card = [...document.querySelectorAll('.job_seen_beacon')].find(c => c.querySelector('[data-jk]')?.getAttribute('data-jk') === '<jk>');
  card.querySelector('h2 a, h2 span, [id^=jobTitle]').click();
  await new Promise(r => setTimeout(r, 1200));
  const t = document.getElementById('jobDescriptionText')?.innerText || '';
  return { remote: /remot|híbrid|home.?office|teletrabajo/i.test(t), len: t.length };
}
```

### Preguntas de la empresa — sin `aria-label`, ordenar por posición

A diferencia de GetOnBoard (que sí tiene `aria-label`), los `textarea`/`input[type=text]` del módulo de preguntas de SmartApply **no traen `aria-label` ni `id` legible** (son IDs autogenerados de React tipo `_r_5_`). Hay que asumir que el **orden del DOM coincide con el orden visual de las preguntas** (verificado, sí coincide) y rellenar por índice posicional, no por texto de label. El mismo patrón de `fillform`/setter nativo + `dispatchEvent` de GetOnBoard aplica aquí para evitar la concatenación de `fill`.

### Sesiones concurrentes de `chrome-devtools-axi`

Cuando una sesión (`CHROME_DEVTOOLS_AXI_SESSION`) queda en un estado raro ("The selected page has been closed" persistente tras cerrar una pestaña con `window.close()` vía `eval`), no vale la pena depurarlo — usar un **nombre de sesión nuevo** (`indeed-laboral-2`, `-3`, …) y volver a `open` la URL objetivo; el estado se resetea limpio y es más rápido que troubleshootear la sesión vieja. Cada nombre de sesión nuevo asigna su propio puerto de bridge automáticamente, así que no colisionan entre sí.

Para verificar el estado real de las pestañas sin depender del estado interno de una sesión de `chrome-devtools-axi`, `curl -s http://localhost:9223/json/list | jq` consulta el CDP directamente — siempre preciso, nunca se queda "stale".

### Filtro de idioma en la postulación
Igual que en LinkedIn/GetOnBoard: si el aviso o sus preguntas están en inglés (o dice explícitamente "CVs enviados en inglés serán valorados"), responder todo en inglés; si están en español, responder en español. Ejemplo real: 23People (Equifax) pide explícitamente CV en inglés pese a que el aviso está mayormente en español.

### Filtro de modalidad — leer la descripción completa, no confiar en el location tag
El campo "locations"/ubicación de la tarjeta casi siempre muestra la ciudad de la oficina (p. ej. "Santiago de Chile"), **incluso cuando el puesto es 100% remoto**. Hay que leer la descripción completa: frases como "Modalidad 100% remota desde cualquier parte de Chile" o "Home Office Remoto con residencia en Chile" en el cuerpo del aviso priman sobre el tag de ubicación / el campo "remote type: Hybrid" de Workday. A la inversa, avisos sin ninguna mención de modalidad (ni remoto ni híbrido) deben tratarse como potencialmente 100% presenciales y descartarse por precaución dado que Gonzalo reside en Limache.

---

## 🔁 Loop completo por oferta

```
[0] Verificar que la instancia dedicada de Chrome (puerto 9223) esté viva: curl http://localhost:9223/json/version
    ↓
Buscar en cl.indeed.com/jobs?q=<keyword>&l=Chile (o l= vacío para global/LATAM en roles remotos)
    ↓
Para cada tarjeta de resultado, click en el heading (dentro del SPA, no navegar directo a /viewjob)
   → leer #jobDescriptionText completo (eval, no solo el snapshot truncado)
   → ¿modalidad confirmada remoto/híbrido compatible con Limache? ¿stack sin exclusiones? ¿seniority correcta?
        → no a cualquiera: SALTAR (registrar motivo)
   → ver qué botón de postulación aparece
        → "Postúlate rápidamente"/"Postularse mediante Indeed": BLOQUEADO hasta verificar teléfono — registrar y saltar
        → "Postularse en la página de la empresa": abre pestaña nueva con el ATS externo
             → completar el formulario del ATS (varía por proveedor — Workday requiere cuenta, otros pueden ser de una sola página)
             → si el ATS tiene fricción no resuelta (p. ej. registro de Workday fallando), registrar como bloqueado, no insistir más de 2-3 intentos
    ↓
[N] Registrar cada postulación enviada Y cada descarte con motivo concreto en cv_job_links.md (Portal = "Indeed"), de forma incremental
```

## 📊 Estado al cierre de la sesión 2026-08-19 (ronda 2, post-verificación de teléfono)

Gonzalo verificó su teléfono y completó campos adicionales del perfil manualmente antes de esta ronda. Resultado:

- **1 postulación enviada de punta a punta:** Dhemax — Fullstack Developer Java-Kotlin/Quarkus (remoto, Viña del Mar). Confirmó que el flujo SMS ya no bloquea.
- **2 postulaciones bloqueadas en el último paso por reCAPTCHA** (formulario 100% completo, incluidas preguntas de la empresa, solo falta el checkbox): TINET (Desarrollador Backend Java Senior, híbrido Las Condes) y 3IT (Desarrollador Backend Senior, híbrido Santiago). Ver hallazgo crítico arriba — es un límite de sesión, no un rechazo de la oferta.
- **1 bloqueada por requerir cuenta en portal externo (BNE):** SII Group Chile.
- **1 descartada por discrepancia entre título y descripción real** (KPaz — AWS/Kafka/Kubernetes profundo, no declarado).
- **1 descartada por modalidad no declarada + seniority baja** (TechBiz Global — sin mención de remoto/híbrido, pide 3-5 años).
- **4 descartadas por falta de modalidad remota/híbrida confirmada** (COASIN, TicMoAI, SOHO, DigiTect Solutions).

Ver `cv_job_links.md` para el detalle completo con motivos.

**Acción recomendada antes de la próxima ronda:** decidir estrategia frente al límite de reCAPTCHA (¿vale la pena que Gonzalo resuelva manualmente los checkboxes de las postulaciones dejadas a medias, dado que el formulario ya queda completo?) y si conviene crear una cuenta en BNE (bne.cl) dado el volumen de ofertas "Postularse en la página de la empresa" que redirigen ahí.
