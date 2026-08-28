# Notas de decisiones — Qulane (Desarrollador .NET Web Forms + SQL Server, Part Time)

**Fecha:** 2026-08-28 · **Portal:** Get on Board (Job ID 63358) · **Perfil aplicado:** B (remoto internacional en USD), con postulación en español porque el aviso lo exige.

---

## 1. Instrucción explícita del usuario que gobierna esta postulación

Gonzalo pidió que el **resumen** enfatice:

1. Que tiene **más de 15 años** de experiencia y que a estas alturas **entiende el código como un lenguaje**.
2. Que esa experiencia es la que da la expertise para entregar **código de calidad, que se entienda, con estándares y conceptos claros**.
3. Que **va a usar IA y no lo va a negar**, pero de forma **responsable**, entendiendo lo que el cargo pide.

Los tres puntos están en el primer y segundo párrafo del Resumen Profesional de ambas versiones del CV, y se repiten en el mensaje al reclutador y en la respuesta 1 de `respuestas_postulacion.md`.

**Lectura de la regla del aviso (importante):** el aviso **no prohíbe la IA**. Textual: *"puedes consultarla para entender un concepto o resolver una duda, pero el código lo escribes tú y debes poder explicar cada línea de lo que entregas"*. El filtro de descarte es *"dependes de herramientas de IA para escribir código"*. Por eso la estrategia no es negar el uso de IA (habría sido falso y además suena a respuesta ensayada), sino **encuadrarlo exactamente dentro del marco que el propio aviso autoriza**: consulta sí, autoría no, explicación línea por línea siempre. Negarla habría sido el error táctico.

Consecuencia menor: en este CV la IA **no** se presenta como diferenciador (a diferencia de las otras postulaciones del repo, donde el harness de agentes es un punto fuerte). Aquí se presenta como una **práctica bajo control**, subordinada al criterio técnico. La mención a Claude Code se mantiene, pero redactada como flujo con puertas de calidad y revisión humana, nunca como delegación.

---

## 2. Gap duro: .NET Framework 4.x y Web Forms

Consultado al usuario antes de escribir nada. Respuesta: **"Solo autodidacta / puntual"** — sin experiencia laboral. `cv.md` lo confirma: cero menciones a .NET, C#, ASP.NET o Web Forms en todo el repositorio.

El aviso lo pone como filtro de descarte explícito: *"NO APLIQUES SI no tienes experiencia real y reciente con .NET Framework 4.x y Web Forms"*.

**Decisión: postular igual, declarando el gap en el primer párrafo del mensaje y en un bloque propio del CV.** Fundamento:

- Restricción global n.º 2 del proyecto: prohibido inventar experiencia. No hay forma de "adaptar" el CV para cubrir esto.
- Declararlo primero, y no dejar que lo descubran, es la única jugada que no quema la relación con el empleador.
- El resto del aviso sí está cubierto y es fuerte (ver punto 3), y la empresa hace justamente facturación para el sector salud — el dominio funcional exacto del usuario.

**Riesgo asumido y comunicado:** es probable el descarte automático por este filtro. La postulación se justifica por el encaje de dominio y por el ángulo de IA, no por el stack.

**Base transferible que sí se reclama (sin equipararla a .NET):** desarrollo web server-side con ciclo de vida de página, controles y estado en el servidor (Struts/JSP en Santander/Isban, ExtJs en Cencosud y Hospital Cruz del Norte). Redactado siempre como *"el mismo modelo mental… en otro lenguaje"*, nunca como equivalencia.

---

## 3. Qué sí se reclama, y con qué respaldo de `cv.md`

| Requisito / deseable del aviso | Respaldo real | Fuerza |
|---|---|---|
| SQL Server | Portal Inmobiliario 2008–2016 (SQL Server + SSRS); Santander/Isban (SQL Server, Oracle) | Media-alta, matizada |
| SPs complejos, optimización, debugging | Oracle PL/SQL y PostgreSQL (profundidad real); SQL Server a nivel de consultas y reportería | **Matizado explícitamente** |
| JavaScript, jQuery, HTML, CSS | Nubox 2014–2017; Seven IT 2017–2020 (jQuery, Bootstrap, Vuetify) | Alta |
| Mantención de sistemas con lógica de negocio compleja | 17 años Santander/Isban; Citibank; Portal Inmobiliario | Alta |
| Sistemas de facturación (deseable) | Nubox Facturación Electrónica; facturación electrónica bancaria | **Alta** |
| Sector salud (deseable) | Hospital Cruz del Norte (Ficha Clínica) y Seven IT (Sistema de Gestión en Salud + módulo de pagos) | **Alta** |
| Integraciones con APIs de pago (deseable) | Transbank Webpay y Khipu; Medios de Pago y Tarjetas en banca | Alta |
| Git / control de versiones (deseable) | Git, GitLab con Merge Requests | Alta |
| Pruebas de código antes de entrega | JUnit, Jest; revisión de Merge Requests en Seven IT | Media-alta |
| Entity Framework (deseable) | **No se reclama.** Equivalente: Hibernate/JPA, Ecto | — |
| Comunicación en español | Nativo | Alta |
| Disponibilidad horaria EST/Pacific | Chile GMT-4 = EST+1h | Alta |

---

## 4. Orden de la experiencia: reordenado por relevancia, no por fecha

Se rompió el orden cronológico inverso del CV maestro y se ordenó por cercanía a la vacante:

1. **Nubox** (facturación + JS/jQuery) — el deseable más fuerte.
2. **Seven IT / Hospital Cruz del Norte** (salud + módulo de pagos + jQuery).
3. **Portal Inmobiliario** (SQL Server + SSRS) — el único respaldo real de SQL Server.
4. **Santander/Isban** (legacy complejo, facturación, web server-side).
5. **Startup de Movilidad** (APIs de pago + uso responsable de IA) — al final a propósito: aquí el rol actual no es el argumento.

Los roles menos relevantes (Citibank, Perficient/Caterpillar, Cencosud, Ficha Clínica) van agrupados en un párrafo de cierre.

---

## 5. Restricciones globales aplicadas

- **n.º 1** — "CTO & Co-founder" del `cv.md` maestro → **Tech Lead** en ambas versiones.
- **n.º 2** — Cero experiencia inventada; el gap de .NET se declara en vez de rellenarse.
- **n.º 3** — Purgado el "incrementando la velocidad de codificación hasta 300%" del resumen maestro (cifra de lista negra). Ninguna cifra nueva sin respaldo: las que quedan son años, cantidad de desarrolladores liderados y países atendidos, todas verificables.
- **n.º 4** — PDFs generados exclusivamente con `/usr/local/bin/m2pdf` (primer intento falla por `FreeSerif`, el reintento de emergencia produce el PDF; comportamiento esperado).
- **n.º 5** — Formato preguntado al usuario: eligió **ambos** (ATS y Harvard).
- **n.º 7** — Habilidades Técnicas inmediatamente antes de Educación e Idiomas en ambas versiones.
- **n.º 8** — Bloque de Competencias al cierre, cada una con evidencia entre paréntesis. Se priorizaron las que el aviso nombra: *responsabilidad, compromiso con los plazos y atención al detalle* (mirroring del requisito "Responsable, comprometido con los plazos y con atención al detalle") y *comunicación* (mirroring de "Buena comunicación en español").

---

## 6. Verificación de salida

| Archivo | Páginas | Extracción ATS |
|---|---|---|
| `cv_gonzalo_qulane_dotnet_webforms.pdf` (ATS) | 2 | Verificada con `pdftotext`: texto lineal, completo y en orden de lectura |
| `cv_gonzalo_qulane_dotnet_webforms_harvard.pdf` (Harvard) | 2 | Verificada con `pdftotext`: texto lineal, completo y en orden de lectura |

Ambos partieron en 3 páginas; se recortó fusionando viñetas y comprimiendo el bloque de Competencias, **sin tocar el Resumen Profesional** (los tres párrafos que el usuario pidió enfatizar quedaron intactos en la versión ATS; en la Harvard están levemente comprimidos por espacio, conservando las tres ideas).

---

## 7. Riesgos y advertencias para Gonzalo

1. **Filtro de descarte explícito.** El aviso dice "NO APLIQUES SI no tienes experiencia real y reciente con .NET Framework 4.x y Web Forms". Es probable el descarte. La postulación es una apuesta consciente al encaje de dominio (facturación + salud) y a la política de IA.
2. **Nivel del cargo: Junior, con 130 postulaciones** al momento de leer el aviso. Perfil de 15+ años compitiendo en una vacante junior: puede leerse como sobrecalificación. La respuesta 5 de `respuestas_postulacion.md` la aborda de frente.
3. **Renta:** USD $1.500/mes por 20 h/semana. En jornada completa equivaldría a ~USD $3.000, dentro de su banda; como part-time es un **complemento**, no un reemplazo de ingreso principal. Compatible con seguir buscando o mantener otro proyecto.
4. **Empresa canadiense, pago en USD, sin subcontrato.** Verificar la forma de pago y la situación tributaria antes de firmar.
5. **Postulación en español obligatoria** según el portal — todo el material está en español.
6. **No enviada.** Todo el material queda generado y pendiente de revisión y envío por Gonzalo.
