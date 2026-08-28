---
name: job-hunter-trabajando
description: Automatiza la búsqueda y postulación a vacantes técnicas de Gonzalo Oviedo Lambert en Trabajando.cl (Trabajando.com Chile), navegando el CV SPA con hash routing, los autocompletes Vue con debounce y el modal de búsqueda, aplicando sus filtros de modalidad, renta y afinidad técnica.
---

# 🛠️ Trabajando.cl Job Hunter — Gonzalo Oviedo Lambert

Módulo hermano de [[job-hunter-computrabajo]]. Cubre **Trabajando.cl** (`https://www.trabajando.cl`), portal con arquitectura muy distinta a Computrabajo: SPA en **Nuxt/Vue** con *hash routing*, catálogos **cerrados** en todos los campos y autocompletes con debounce.

**Cuenta:** `goviedo.laboral@gmail.com`

---

## 📌 Estado del perfil en el portal (cargado 2026-07-31)

| Sección | Ruta | Contenido |
|---|---|---|
| Datos personales | `#/informacion-personal` | RUN 14.355.380-9 · nac. 13/10/1979 · Chilena · Hombre · Chile / Limache, Valparaíso |
| Acerca de mí | `#/acerca-de-mi` | 802/900 caracteres, tercera persona, abre con profesión + UBB + 15 años |
| Experiencia | `#/experiencia-laboral` | CTO & Co-founder · "Startup de Movilidad" · Emprendedor · Gerencia/Dirección · Informática/Tecnología · ene 2024 – actualidad |
| Formación | `#/estudios` | Ing. en Computación e Informática · UBB · Presencial · **Titulado** · 2004–2009 + 5 cursos |
| Habilidades | `#/habilidades` | 27 ítems (23 con nivel + 4 competencias) |
| Idiomas | `#/idiomas` | Inglés medio · Español alto |
| Estado | `#/configura-tu-perfil` | ✅ "Estoy abierto a oportunidades" · ❌ "Dispuesto a cambiarme de ubicación" |

**Rutas completas del CV** (SPA bajo `https://www.trabajando.cl/mi-curriculum`):
`#/informacion-personal` · `#/acerca-de-mi` · `#/experiencia-laboral` · `#/estudios` · `#/habilidades` · `#/idiomas` · `#/expectativa-de-renta` · `#/licencia-conducir` · `#/informacion-adicional` · `#/configura-tu-perfil` · `#/ver-curriculum`

> ⚠️ **No existe sección de certificaciones.** Van en `#/estudios` con Nivel = `Otro` → Tipo = `Curso` → Institución = `Otra Institución`, y el emisor entre paréntesis dentro del nombre del curso.

### Diferencias con el CV maestro (`cv.md`) — no son errores, son límites del catálogo

* El título real es **"Ingeniería en EJECUCIÓN en Computación e Informática"**; ese nombre **no existe** en el catálogo, quedó como "Ingeniería en Computación e Informática".
* Figura como **Titulado** (corregido el 2026-08-01 tras confirmarlo Gonzalo; había quedado como Egresado).
* La startup se declara anónima ("Startup de Movilidad") por decisión suya del 2026-07-31.

---

## 🔎 Búsqueda de ofertas

**Vía UI:** el botón lupa del header es `a.open-search` (modal Bootstrap, `data-bs-target="#search-step1"`). El modal tiene dos inputs — *"¿Qué trabajo buscas?"* y *"Región / Comuna"* —, el botón **Buscar empleo** y un link **Búsqueda avanzada**.

**Vía URL (más rápido, evita el modal):**

```
https://www.trabajando.cl/trabajo-empleo/{QUERY}?ubicacion={region-minusculas}&region={ID}
```

| Región | ID |
|---|---|
| Metropolitana de Santiago | `1` |
| Valparaíso | `6` |

> El campo Región acepta **una sola ubicación** (reemplaza, no acumula). Para cubrir RM + Valparaíso hay que hacer **dos búsquedas**. Omitir `?ubicacion=&region=` busca en **todo Chile**, que es lo más eficiente.

### Filtro por jornada: `?jornadas={ID}`

| ID | Jornada | Total (2026-08-01) | De TI |
|---|---|---|---|
| 1 | Jornada Completa | 8.850 | — |
| 3 | **Part Time** | 658 | **0** en los primeros 135 |
| 4 | Comisionista | 2 | — |
| 5 | Reemplazo | 12 | — |
| 6 | Práctica | 255 | — |
| 7 | Por Turnos | 760 | — |
| 8 | **Free Lance** | 16 | **0** (docentes, prevencionistas, relatores de gasfitería) |
| 9 | **Teletrabajo** | 73 | **9** |
| 10 | En terreno | 915 | — |
| — | Mixta (Teletrabajo + Presencial) | 1.156 | el grueso del pool TI |

> 🚨 **Trabajando.cl no tiene mercado contractor/freelance de TI.** Filtrar por Free Lance o Part Time devuelve cero avisos técnicos. Para una estrategia contractor, el volumen sale de **relajar seniority y stack** sobre los avisos Mixta/Teletrabajo, no del filtro de modalidad.

**Volumen medido el 2026-07-31 con query `Java`:** 29 resultados en RM · 1 en Valparaíso.

El motor hace *match* laxo y cuela ruido severo (aparecieron Bobinador, Ingeniero Eléctrico y Vendedor Técnico de Transformadores bajo la query "Java"). **Filtrar siempre leyendo el aviso, nunca confiar en el conteo.**

---

## ⚙️ Automatización con `chrome-devtools-axi` — 12 lecciones verificadas

Todas comprobadas en sesión real el 2026-07-31. Este portal rompe varios supuestos que sí funcionan en Computrabajo.

### 1. Los `uid=` del snapshot se invalidan tras cada snapshot
Un `press Backspace` dirigido a un uid obsoleto **truncó el campo Empresa** ("Startup de Movilidad" → "Startup de Movilid") sin ningún error. **Preferir `eval` con selectores CSS sobre los uid.**

### 2. `fill` y `fillform` NO funcionan en los `<select>` de Vue
Algunos tienen objetos como `option.value` (devuelven `[object Object]`). Solución:

```javascript
const pick = (s, txt) => {
  const n = [...s.options].findIndex(o => o.textContent.trim() === txt);
  if (n < 0) return false;
  s.selectedIndex = n;
  s.dispatchEvent(new Event('change', { bubbles: true }));
  s.dispatchEvent(new Event('input',  { bubbles: true }));
  return true;
};
```

### 3. Escribir en un `<input>` de Vue exige el setter nativo
Asignar `input.value = x` **no actualiza el modelo**:

```javascript
const setv = (i, v) => {
  i.focus();
  Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(i, v);
  i.dispatchEvent(new Event('input', { bubbles: true }));
};
```

### 4. Los autocompletes tienen debounce de ~1400 ms
Componentes con clase `.autocomplete`, resultados en `li.autocomplete-result`. **Leer antes de 1400 ms devuelve los resultados de la consulta ANTERIOR** — produce un desfase de uno que parece un catálogo incoherente. Esperar ≥1400 ms (1600 ms para ir sobrado).

### 5. Seleccionar una sugerencia exige despachar tres MouseEvent
`element.click()` y `chrome-devtools-axi click @uid` **no la seleccionan**:

```javascript
['mousedown','mouseup','click'].forEach(t =>
  li.dispatchEvent(new MouseEvent(t, { bubbles: true, cancelable: true, view: window })));
```

### 6. En `#/habilidades` las competencias NO piden nivel
Tras elegir una habilidad **técnica** aparece un `<select>` de Nivel (Bajo/Medio/Alto) y **el tag solo se agrega al elegir nivel**. Pero las **competencias** (`Desarrollo De Software`, `Programación orientada a Objetos`, `Metodologías Ágiles`, `Inteligencia Artificial`) se agregan directo y el select **nunca aparece**: esperarlo es un falso error. Si un tag queda sin nivel, se ve como `"Nombre"` en vez de `"Nombre - Nivel Alto"`.

### 7. Los tags de habilidad son `span.badge-habilidades`
Se eliminan haciendo click (con los tres MouseEvent) en el `svg` que contienen.

### 8. El editor de Responsabilidades es `contenteditable`, no `textarea`
Está en `#/experiencia-laboral`. **Autolinkea dominios**: escribir "Pi.dev" lo convirtió en hipervínculo dentro del CV. Evitar dominios en el texto. Para vaciarlo: `Range` + `selectNodeContents` + `Backspace`.

### 9. El backend normaliza a sentence-case los nombres de curso
"Claude Code 101" quedó guardado como "Claude code 101". **Verificado que no es CSS** (`text-transform: none`) — es el dato almacenado. Irreversible desde el formulario.

### 10. El catálogo de **instituciones** no tiene proveedores de cursos online
No existen Anthropic, Educative, CertiProf, Kibernum ni Udemy. Usar **"Otra Institución"** y poner el emisor entre paréntesis en el nombre del curso. No hay campo para el ID de credencial.

### 11. El catálogo de **habilidades** es cerrado y tiene huecos importantes

| ❌ No existen | ✅ Sí existen |
|---|---|
| Flutter · Elixir · Kafka · Solidity · Gradle · Mockito · Kubernetes · Terraform · Google Cloud · **Spring Boot** | Java · Spring Framework · Backend · Microservicios · Arquitectura · Oracle Pl/Sql · Postgresql · Mysql · Mongodb · Docker · Cloud Computing · Aws · Azure · Devops · Jenkins · Gitlab · Linux · Maven · Hibernate · Javascript · Angular · Vuejs · React · Scrum · Blockchain · Machine Learning · Desarrollo De Software · Metodologías Ágiles · Programación orientada a Objetos · Inteligencia Artificial |

Flutter y Elixir se compensan nombrándolos en la experiencia laboral y en "Acerca de mí", que sí son texto libre.

### 12. El navegador es compartido con Gonzalo
Las pestañas **cambian de contexto sin aviso** (a mitad de sesión una saltó de trabajando.cl a `qa-app.tellevoapp.cl`). **Verificar `location.href` antes de cada operación** y abrir pestaña propia con `chrome-devtools-axi newpage <url>` si hace falta.

---

## 🎯 Filtros obligatorios (confirmados por Gonzalo el 2026-07-31)

Idénticos a los de Computrabajo:

1. **Modalidad: solo híbrido o remoto.** Reside en Limache, Región de Valparaíso. Descartar 100% presencial aunque el tag del portal diga otra cosa — **leer el cuerpo del aviso**, ahí está el dato real.
2. **Renta: 1.800.000 CLP – 3.000.000 CLP líquidos**, ajustable por cargo:

   | Cargo del aviso | Cifra a declarar |
   |---|---|
   | Arquitecto / Tech Lead / Jefe de Desarrollo | 3.000.000 CLP |
   | Senior / Staff / Especialista | 2.700.000 CLP |
   | Desarrollador (sin seniority) / Full Stack | 2.400.000 CLP |
   | Semi Senior | 2.000.000 CLP |

   Descartar avisos con renta publicada **bajo 1.800.000 CLP**.
3. **Afinidad técnica.** Descartar stacks excluyentes que no domina: .NET/C#, PHP, Cobol, Salesforce, Murex, Dynamics 365, Prestashop, Golang, Python/Django, QA, BI, ETL, prácticas y soporte técnico.

**Gaps reales — declararlos con honestidad, nunca inflar:** Kubernetes en producción (usa Docker + Cloud Run), Terraform/Ansible (usa Pulumi), AWS CDK/CloudFormation (su IaC es GCP), Machine Learning / MLOps, LangChain / LlamaIndex (integra LLMs a bajo nivel), .NET/C#, Redshift.

---

## 🔁 Flujo de postulación

**Estado de verificación: ✅ VERIFICADO end-to-end el 2026-08-01** con 3 postulaciones reales (ronda 1).

### 🚨 La trampa que costó dos envíos fallidos silenciosos

El formulario de preguntas existe **duplicado** en el DOM, en dos contenedores:

| Contenedor | Rol | Estado |
|---|---|---|
| `.formularioPreguntasOferta` | Layout desktop | ✅ **El activo** |
| `.offcanvas.offCanvasPreguntasMobil` | Layout móvil | ❌ `visibility: hidden`, `offsetParent === null` |

El offcanvas oculto **conserva dimensiones** (`getBoundingClientRect().width > 0`), así que **filtrar por ancho selecciona el formulario equivocado**. Sus campos se llenan sin error y su botón de envío no hace nada: la postulación falla **sin ningún mensaje** y `/mis-postulaciones` sigue vacío.

> **Regla:** filtrar SIEMPRE por `offsetParent !== null`, **nunca** por `getBoundingClientRect().width > 0`. Y acotar el llenado a `document.querySelector(".formularioPreguntasOferta")`.

### 🚨 El botón de envío se llama "Postular", no "Responder"

Hay un botón visible llamado **`Responder`**, pero vive dentro del offcanvas oculto y está deshabilitado. **El submit real es un segundo botón `Postular`**, identificable por la clase `w-100`:

```javascript
const submit = [...document.querySelectorAll("button")]
  .filter(x => /^Postular$/i.test(x.textContent.trim())
            && x.offsetParent !== null
            && x.className.includes("w-100"))[0];
["mousedown","mouseup","click"].forEach(t =>
  submit.dispatchEvent(new MouseEvent(t, {bubbles:true, cancelable:true, view:window})));
```

Su clase incluye `boton-deshabilitado`, pero **es decorativa**: `disabled === false`, `pointerEvents: auto`, `opacity: 1`. No interpretarla como bloqueo.

### Secuencia completa verificada

```
abrir detalle de la oferta → esperar ≥6 s
  ↓
click "Postular" (acotado al contenedor del detalle, offsetParent !== null)
  ↓
├─ NO aparece modal  → postulación DIRECTA, ya quedó registrada. Fin.
└─ aparece modal "Responde las preguntas del reclutador para tu postulación al cargo X"
      botones: "Comenzar" | "Guardar empleo y postular más adelante"
   ↓ click "Comenzar" (offsetParent !== null) → esperar ≥3,5 s
   ↓ se renderiza .formularioPreguntasOferta en la MISMA página (la URL nunca cambia)
   ↓ leer las preguntas, redactar con la verdad del perfil, llenar SOLO ese contenedor
   ↓ click botón "Postular" con clase w-100
   ↓ verificar en /mis-postulaciones
```

> ⚠️ **La URL nunca cambia durante todo el flujo** — no sirve como señal de éxito. La única confirmación válida es `/mis-postulaciones`.

### Tipos de pregunta — son TRES, no dos

* **`<textarea>`** — máx. 3.000 caracteres (mucho más holgado que los 500 de Computrabajo). El contador "(ingresados: N)" se actualiza y sirve para verificar que el valor entró en el modelo Vue.
* **`<input type=text>` numérico** — algunas preguntas redactadas como Sí/No en realidad **solo aceptan números** (típicamente años de experiencia o monto de renta). El aviso *"Esta pregunta solo acepta números / Solo puedes agregar hasta 11 caracteres"* aparece **recién después** de escribir texto.
* **`<select>` de escala 1–5** — opciones `Selecciona / 1 / 2 / 3 / 4 / 5`, usado para "indica tu nivel de manejo de X" y a veces para preguntas que no son de escala.

> 🚨 **Un `<select>` sin responder hace fallar el submit EN SILENCIO.** Costó dos intentos fallidos en la oferta 6106892: el selector `textarea,input` capturaba 4 controles y el formulario en realidad tenía **6 preguntas** — las dos últimas eran selects invisibles para ese selector. Recolectar SIEMPRE los tres tipos:
> ```javascript
> const campos  = [...f.querySelectorAll("textarea,input")].filter(e => e.offsetParent !== null);
> const escalas = [...f.querySelectorAll("select")].filter(s => s.offsetParent !== null);
> ```
> Y contar las preguntas del texto (`/Pregunta\s*\d+/g`) para verificar que el total de controles cuadra antes de enviar.

* Los tres exigen el setter nativo (lección 3) o `selectedIndex` + `change` según el tipo.

### 💡 Las killer questions revelan el stack real del aviso

Dos veces el cuerpo del aviso ocultó el stack excluyente y **solo apareció al abrir las preguntas**:

| Aviso | Lo que decía | Lo que reveló la pregunta |
|---|---|---|
| "Analista Programador — rubro seguros" | modalidad Mixta, mencionaba Java | Pregunta 3 pedía **Salesforce Service Cloud / Administration** |
| "Analista Programador" (Zurich Chile) | descripción funcional genérica, sin stack | Pregunta 1 pedía **C#, .NET, .NET Core, Angular, DB2** |

> **Práctica recomendada:** abrir el formulario de preguntas y **leerlas antes de decidir postular**. Abandonar sin enviar no registra nada — es un descarte gratuito y más informado que el que se hace solo con el cuerpo del aviso.

### ⚠️ No encadenar el submit con la navegación siguiente

Ejecutar el `eval` de envío y, en el mismo comando de shell, navegar a la oferta siguiente **corta el envío a medio camino** y la postulación no se registra. Enviar, **verificar en `/mis-postulaciones`**, y recién entonces pasar a la próxima.

### Botones del listado y del detalle

| Botón | Clase | Qué hace |
|---|---|---|
| `Postular` | `btn primary-btn blue` | Inicia la postulación (hay uno por tarjeta del listado **y** uno en el detalle) |
| `Postular` | `w-100 btn primary-btn blue boton-deshabilitado` | **Envía** el formulario de preguntas |
| `Responder` | dentro de `.offcanvas` | ❌ Señuelo: oculto y deshabilitado |
| `Guardar empleo y postular más adelante` | `btn btn-link text-wrap` | Guarda en favoritos, **no** postula |

> ⚠️ Hay **múltiples botones "Postular" simultáneos** (uno por tarjeta del listado). **Acotar siempre al contenedor del detalle** antes de hacer click, o se postula a una oferta no revisada.

**Fuente de verdad:** `https://www.trabajando.cl/mis-postulaciones`. Tomar **baseline antes** del loop y comparar el delta al cierre. La tabla trae `Etapa | A qué postulaste | Fechas | Portal`. Etapas observadas: **"En proceso"** y **"Enviado"**. La indexación fue **inmediata** (sin el retraso de 1–2 min de Computrabajo).

```
[0] BASELINE: leer /mis-postulaciones y guardar la lista previa
    ↓
buscar por URL directa (RM y Valparaíso por separado)
    ↓
por cada oferta: abrir detalle → filtrar por aviso → postular (secuencia de arriba)
    ↓
[N] CIERRE: releer /mis-postulaciones y comparar contra el baseline
```

> ⚠️ La postulación es irreversible hacia un tercero: **confirmar con Gonzalo antes del submit final** de cada oferta.

---

## 📊 Bitácora de rondas

### Ronda 1 — 2026-08-01 (baseline: 0 postulaciones)

**Embudo:** ~134 avisos escaneados → 17 candidatos por título → 4 sobrevivieron al filtro leyendo el aviso → **3 postuladas** (1 descartada por Gonzalo).

| Oferta | Empresa | Modalidad | Killer questions |
|---|---|---|---|
| Ingeniero/a de Software | Caja de Compensación Los Andes, Providencia | Mixta | 5 (4 textarea + 1 numérica) |
| Analista de integraciones y automatización | Empresa Confidencial, Santiago | Mixta | 2 (ambas numéricas) |
| Desarrollador Full Stack | Administradora de Turismo Rosa Agustina, Olmué | Art. 22 | **Ninguna** (postulación directa) |

**Descartada por decisión de Gonzalo:** Full Stack .NET/Java/React (Agibiz, Las Condes) — .NET como co-requisito central.

**Gaps declarados con honestidad:** sin experiencia en **Oracle Flexcube** (core bancario) y experiencia **acotada en productos de crédito**, ambos en la postulación de Caja los Andes.

**Aprendizaje sobre el tamaño del mercado:** las queries genéricas son inservibles — `Desarrollador` devuelve 165 resultados dominados por "desarrollador de negocios", y `Backend` reporta 952 pero el motor ignora la query. Solo `Java` da señal decente (29 en RM, 1 en Valparaíso). **Filtrar los slugs con regex técnico dentro del scraper** en vez de revisar a mano.

### Ronda 2 — 2026-08-01 (baseline: 3)

Barrido nacional (sin filtro de región, para capturar remotos) sobre las queries `Java`, `Analista Programador`, `Full Stack`, `Ingeniero de Software`, `Arquitecto de Software`, `Backend`.

**Embudo:** ~250 avisos únicos → 18 candidatos por título → 5 pasaron el filtro del aviso → **3 postuladas**, 2 abortadas al leer las preguntas.

| Oferta | Empresa | Modalidad | Resultado |
|---|---|---|---|
| Arquitecto/a de Sistemas | Caja de Compensación Los Andes | Mixta | ✅ Postulada (renta declarada 3.000.000) |
| Analista de Sistemas Senior — Mantenimiento Correctivo | **Banco de Chile** | Mixta | ✅ Postulada (renta 2.700.000) |
| Desarrollador/a Full Stack | Providencia | Mixta | ✅ Postulada (renta 2.500.000) |
| Analista Programador — rubro seguros | Las Condes | Mixta | ❌ Abortada: Salesforce |
| Analista Programador | Zurich Chile | Mixta | ❌ Abortada: C#/.NET/DB2 |

**Total acumulado: 6 postulaciones.**

### Ronda 3 — 2026-08-01 · **Estrategia contractor** (baseline: 6 → cierre: 20)

Excepción puntual autorizada por Gonzalo: bajar el piso de seniority, soltar el filtro de stack, y posicionarse como **contractor por horas**. El filtro de modalidad híbrida/remota **se mantuvo**.

**Parámetros de la ronda:** $12.000 CLP/hora bruto (≈ $2.100.000 mensuales a jornada completa) · 20–30 h/semana · honorarios o contrato por proyecto · perfil público del portal **sin modificar** (el ángulo va solo en las killer questions).

**14 postulaciones nuevas:** Banco de Chile · Zurich Seguros de Vida · Penta Vida (×3: Backend .NET, Líder Técnico Arquitectura, Ingeniero de Software) · Robert Half · RedSalud · Perceptual Consultores · Agibiz · Ingevec · Táctica Consultores · Despapeliza · Help SPA · 2 Empresa Confidencial.

**Abandonadas al leer las preguntas (3):** Backend PHP Laravel (renta publicada **$1.300.000**, muy bajo la tarifa) · Fullstack Las Condes (**100% presencial**) · Fullstack TS/React (100% presencial).

#### 🗣️ Banco de respuestas contractor (reutilizable)

**Tarifa** — numérico: `12000` (hora) o `2100000` (mensual). Texto:
> Trabajo por hora en modalidad de honorarios: $12.000 CLP/hora bruto, con disponibilidad de 20 a 30 horas semanales. En jornada completa equivale a aproximadamente $2.100.000 mensuales, bajo el promedio de mercado para un perfil con mi experiencia. Ofrezco esta tarifa porque mi flujo de trabajo me permite entregar en menos horas y el ahorro lo traspaso al cliente. Si prefieren jornada completa con contrato, también es conversable.

**Diferencial / por qué la tarifa es menor:**
> Mi diferencial está en el flujo de trabajo: uso harnesses de agentes de código (Claude Code, Pi.dev, opencode) en mi día a día, no delegando sino diseñando el flujo — especificación, plan, ejecución y verificación — con una suite de tests automatizados como puerta de calidad. En la práctica esto acelera hasta 3x la exploración y codificación sobre código que no escribí yo, que es justamente la fase más lenta al integrarse a un proyecto en curso.

**Tecnología que no domina** (plantilla usada en .NET, TypeScript/Node, Salesforce, DB2, QA automation):
> Prefiero declararlo con transparencia: no cuento con experiencia en [X] en producción. Mi especialidad son más de 15 años en Java y Spring Boot […]. Mi flujo con agentes de código acorta de forma importante la curva en ecosistemas nuevos. Si el cargo requiere autonomía inmediata en [X], conviene considerarlo en la evaluación.

> ⚠️ El **"3x"** es una excepción consciente a la regla de verificabilidad de `AGENTS.md`. Está acotado a lo defendible (onboarding en código ajeno) y **nunca** debe escalarse a "300%" ni a "la IA resuelve la mayoría de los problemas".

> ⚠️ La tarifa de $12.000/h queda **bajo** los $2.500.000 del perfil público del portal. Si un reclutador lo nota, la explicación es la modalidad por horas.

### 📉 Tamaño real del mercado afín en Trabajando.cl (medido el 2026-08-01)

Tras dos rondas y ~380 avisos escaneados, **el portal quedó agotado para este perfil**. El inventario TI está dominado por stacks que Gonzalo no domina:

| Stack dominante en el pool | Volumen aproximado |
|---|---|
| .NET / C# / ASP.NET / Blazor | el bloque más grande |
| Node.js / TypeScript / NestJS / Next.js | segundo bloque (muchos avisos duplicados de la misma empresa) |
| PHP / Laravel | recurrente |
| Python / Django | recurrente |
| Salesforce · Odoo · ERP Oracle Fusion | nicho |
| **Java / Spring Boot** | **marginal — apenas un puñado de avisos** |

> **Implicancia operativa:** en Trabajando.cl **no es alcanzable una ronda de 20 postulaciones** con el filtro de afinidad puesto. El techo realista por ronda es de **3 a 6**. Antes de pedir más, confirmar con Gonzalo si prefiere esperar avisos nuevos, ampliar a otros portales (ver [[job-portals-knowledge-base]]) o relajar explícitamente algún filtro — por ejemplo aceptar stacks JS/TS, donde sí hay volumen.

---

## 📝 Respuestas estándar (compartidas con [[job-hunter-computrabajo]])

Reutilizar el banco de respuestas de esa skill para renta, Java/Spring Boot, Cloud/DevOps, bases de datos, frontend, inglés/formación y disponibilidad. Están redactadas sobre la verdad verificable del perfil y no necesitan variante propia para este portal.

**Ajuste al redactar aquí:** los consejos de Trabajando.cl piden explícitamente **tercera persona** en "Acerca de mí" y en experiencia (funciones en infinitivo, logros como resultado). El resto del portal no impone estilo.

---

## 📋 Pendientes abiertos

- [x] ~~Confirmar Titulado vs Egresado~~ — Gonzalo confirmó **Titulado** el 2026-08-01; ya corregido en `#/estudios?i=5`.
- [x] ~~Llenar `#/expectativa-de-renta`~~ — ya tiene **$2.500.000 en Pesos Chilenos** (verificado 2026-08-01). Mantener las respuestas de renta en las killer questions coherentes con esta cifra.
- [x] ~~Ejecutar la primera ronda~~ — hecha el 2026-08-01, ver bitácora.
- [ ] Decidir si activar "Estoy dispuesto a cambiarme de ubicación" (hoy desmarcado; puede excluirlo de búsquedas de Santiago).
