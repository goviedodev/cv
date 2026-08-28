---
name: job-hunter-computrabajo
description: Automatiza la búsqueda y postulación a vacantes técnicas de Gonzalo Oviedo Lambert en Computrabajo Chile usando Obscura y Playwright (CDP), completando formularios de selección (killer questions) de forma profesional y con alto valor.
---

# 🛠️ Computrabajo Job Hunter — Gonzalo Oviedo Lambert

Este módulo implementa el conocimiento y los flujos automatizados para navegar, buscar y postular a vacantes técnicas en **Computrabajo Chile** (candidato: Gonzalo Oviedo Lambert), respondiendo cuestionarios de selección (killer questions) de forma óptima y con el mayor valor posible.

## 📌 Estado del Perfil del Candidato (Source of Truth)
El perfil de Gonzalo está optimizado al **94%** de completitud y cuenta con las siguientes credenciales y datos duros validados:
- **Email:** `goviedo.laboral@gmail.com`
- **Teléfono:** `+56-963723603`
- **Ubicación:** Limache, Chile (GMT-4)
- **Título en resumen:** `Java Developer + IA`
- **Experiencias registradas:**
  1. *Te Llevo App* | **Architect, Lead Software Engineer** | Mar 2024 - May 2026 (Elixir/Ash, Java 21, Spring Boot, GCP, Flutter).
  2. *Perficient - Caterpillar* | **Java Associate Developer** | Ene 2022 - Dic 2023 (Java 21, Spring Boot, e-commerce global).
  3. *Citibank* | **Java Specialist** | Ene 2021 - Dic 2022 (Java, Oracle SQL, Spring Beans, WebSphere).
  4. *Seven IT SpA* | **Tech Lead & Lead Software Engineer** | Ene 2017 - Dic 2020 (Spring Boot, PostgreSQL, Google Cloud).
  5. *WebClass, Creasys, Coopeuch, Others* | **Java/Senior Developer** | Ene 2008 - Dic 2017 (Java, Struts, Hibernate, PostgreSQL, Oracle, AS/400).
- **Documento adjunto:** `cv.pdf` (cargado exitosamente en el portal).
- **Carta de presentación predefinida:** *"Senior Backend Developer - Java / Spring Boot / Elixir / IA"*.

---

## 💻 Comportamiento de la Interfaz de Computrabajo (Split-Pane)

La interfaz de resultados de búsqueda de Computrabajo funciona en dos columnas (**split-pane**):
1. **Columna Izquierda (Parrilla de Ofertas):** Contiene la lista de tarjetas de empleos.
2. **Columna Derecha (Detalle y Postulación):** Carga los requisitos del puesto, el botón `"Postularme"` y los cuestionarios.

*Para automatizar de forma más robusta, es preferible navegar directamente a la URL del aviso (`https://cl.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-...`) en lugar de interactuar con el split-pane.*

---

## 🧰 Herramientas de Ejecución (Node.js + Playwright CDP)

Para evadir las fuertes protecciones antibot de Computrabajo y poder reaccionar a flujos dinámicos, **NO utilizamos las herramientas nativas del browser harness**. En su lugar, el agente debe escribir y ejecutar scripts temporales en **Node.js usando Playwright**, conectándose a un navegador **Obscura** existente vía CDP.

### Flujo de Conexión:
1. El usuario debe tener el navegador Obscura ejecutándose en el puerto 9222. 
   - *Nota importante:* Si la sesión requiere login, el usuario debe lanzar Obscura **SIN la bandera `--stealth`** (ej: `./obscura serve --port 9222`), iniciar sesión manualmente de forma visual con Google, y avisar al agente.
2. El agente escribe un script `/tmp/script.js` con el siguiente andamiaje:
```javascript
const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  let browser;
  try {
    // Conexión al navegador existente de Obscura
    browser = await chromium.connectOverCDP('http://localhost:9222');
    const context = browser.contexts()[0];
    const page = context.pages().length > 0 ? context.pages()[0] : await context.newPage();
    
    // Navegar y esperar
    await page.goto('https://url-del-aviso');
    await page.waitForLoadState('networkidle');
    
    // ... Logica de extracción, validación y llenado usando page.evaluate() ...
    
    // Guardar resultados en disco para que el agente bash los lea
    fs.writeFileSync('/tmp/ct_result.json', JSON.stringify({ success: true }));
    
  } catch (err) {
    console.error('Error:', err);
  } finally {
    if (browser) await browser.close(); // Desconecta CDP sin cerrar el navegador del usuario
  }
})();
```
3. El agente ejecuta `node /tmp/script.js` usando la herramienta `bash`.

---

## 📋 Resolución Inteligente de Killer Questions

Cuando se abre el formulario de selección (`/candidate/kq`), escanea los campos `textarea` y `radio` mediante `page.evaluate()`:

### 1. 📂 Preguntas Cerradas (Radios)
- **Java / Microservicios / Modalidad híbrida-remota:** Buscar label y marcar **Sí**.
- **Años con Spring Boot:** Marcar **más de 5 años**.
- **Base de datos Oracle / SQL:** Marcar **Avanzado** o **Intermedio**.

### 2. 📝 Preguntas Abiertas (Textareas)
Escribe respuestas altamente profesionales justificando el valor, sin exceder el límite de 500 caracteres (importantísimo para que el botón funcione).

#### 💰 Pretensiones de Renta
- Rango: **$1.800.000 – $3.000.000 CLP líquidos mensuales**.
- Anclaje sugerido: Arquitecto/Tech Lead ($3.0M), Senior/Staff ($2.7M), Full Stack ($2.4M), Semi Senior ($2.0M).
- Respuesta: *"Mis pretensiones líquidas son de aproximadamente $X CLP mensuales, rango conversable según beneficios adicionales y responsabilidades."*

#### ☕ Java y Spring Boot
- *"Más de 15 años de sólida trayectoria con Java y 8+ años diseñando APIs REST/Microservicios robustos con Spring Boot en entornos de alta disponibilidad (banca, e-commerce)."*

#### ☁️ Cloud y DevOps
- *"Nivel avanzado. Construyo pipelines CI/CD y automatizo infraestructura como código (Pulumi). Foco actual en arquitectura nativa cloud sobre GCP, complementado con experiencia en microservicios AWS Lambda y orquestación Docker."*

#### 💾 Bases de Datos
- *"Experiencia avanzada (+15 años). Diseño relacional, optimización de consultas complejas (PL/SQL). Lideré migraciones críticas (ej. Sybase a Oracle en Citibank, 15M+ registros sin pérdida) y domino PostgreSQL."*

#### 📱 Frontend y Arquitectura
- *"Sí, sólida experiencia frontend (Angular, React). Aplico metodología de Diseño Atómico para estructurar componentes modulares y mantenibles, integrados eficientemente vía TypeScript."*

#### 🌎 Inglés / Disponibilidad
- *"Poseo inglés intermedio B1 y dominio técnico avanzado para colaboración en equipos internacionales."* / *"Disponibilidad inmediata para inducción y onboarding."*

---

## 🔎 Detección del Estado de Postulación y Deduplicación

No te fíes de etiquetas como "Postulado" inyectadas dinámicamente en el DOM de las ofertas, suelen dar falsos positivos/negativos.

✅ **Única fuente de verdad: El Baseline de "Mis postulaciones" (`/candidate/match`).**
1. Antes del loop de postulaciones, el agente debe navegar con el script a `https://candidato.cl.computrabajo.com/candidate/match`
2. Extraer todos los títulos de las postulaciones activas:
```javascript
const cards = await page.$$eval('div.box.dFlex.hover', els => 
    els.map(el => el.querySelector('h1,h2,h3') ? el.querySelector('h1,h2,h3').textContent.trim() : '')
);
```
3. Cruzar ese JSON de baseline contra el aviso que se va a postular.

**Filtros Previos (Jornada y Stack):**
- Descartar ofertas `100% presencial` (solo híbridas/remotas).
- Descartar ofertas de otros perfiles (C#, .NET, Cobol, Salesforce, Murex, Dynamics, SAP).
- Validar leyendo el CUERPO del aviso, no solo los tags.

## 🔁 Loop Completo por Oferta (Flujo Lógico Playwright)

1. **Visitar aviso directo:** `page.goto(URL)`
2. **Validar requisitos:** Leer descripción, rechazar si el stack es incompatible (ej. pide .NET excluyente) o es presencial puro.
3. **Pulsar "Postularme":**
   ```javascript
   const postularBtn = Array.from(document.querySelectorAll('a, button, span')).find(b => b.textContent.trim() === 'Postularme');
   if(postularBtn) postularBtn.click();
   ```
4. **Evaluar nueva URL:**
   - Si redirige a `/match/?oi=...`, ya estaba postulado. Saltar.
   - Si redirige a `/candidate/kq?oi=...`, es el **formulario Killer Questions**.
5. **Completar KQ:**
   - Hacer un mapeo inteligente. Validar explícitamente que los textarea `length <= 500`.
   - Pulsar `Enviar mi CV`.
6. **Carta de presentación:**
   - Si redirige a `/candidate/postapply?oi=...`, la postulación entró.
   - Presionar `Actualizar` para enviar la carta de presentación obligatoria.
7. **Verificar Cierre:** El sistema debe notificar `"Hemos adjuntado cv.pdf a tu postulación y tu Carta de presentación"`.