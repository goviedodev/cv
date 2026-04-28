# 📘 Manual de Uso — Multi-Portal Job Hunter

Sistema automatizado de búsqueda de empleo en 7 portales con personalización de CV por aplicación.

---

## 📋 Tabla de Contenidos

1. [¿Qué hace este sistema?](#1-qué-hace-este-sistema)
2. [Requisitos](#2-requisitos)
3. [Estructura del Proyecto](#3-estructura-del-proyecto)
4. [Configuración Inicial](#4-configuración-inicial)
5. [Cómo Buscar Empleo](#5-cómo-buscar-empleo)
6. [Ejemplos Prácticos](#6-ejemplos-prácticos)
7. [Portales de Búsqueda](#7-portales-de-búsqueda)
8. [Archivos Generados](#8-archivos-generados)
9. [Tracking de Postulaciones](#9-tracking-de-postulaciones)
10. [Pipeline de Agentes](#10-pipeline-de-agentes)
11. [Tips para Mejores Resultados](#11-tips-para-mejores-resultados)
12. [Solución de Problemas](#12-solución-de-problemas)
13. [Extender el Sistema](#13-extender-el-sistema)

---

## 1. ¿Qué hace este sistema?

Este sistema **automatiza tu búsqueda de empleo** en múltiples portales de trabajo simultáneamente:

```
Tú dices: "Búscame empleo como Senior Backend Developer en Chile"
            ↓
El sistema:
  1️⃣ Busca en 7 portales a la vez
  2️⃣ Analiza cuál empleo te conviene más
  3️⃣ Genera un CV personalizado para ese empleo
  4️⃣ Registra la postulación en un historial
            ↓
Tú recibes: CV listo para enviar + registro de la aplicación
```

**No es un scraper masivo** — selecciona el **mejor empleo** de cada búsqueda y genera **1 CV personalizado** por ejecución.

---

## 2. Requisitos

| Requisito | Detalle |
|-----------|---------|
| **Pi.dev** | Agente Pi instalado y configurado |
| **cv.md** | Tu CV original en formato Markdown (en el directorio del proyecto) |
| **Conexión a internet** | Para buscar en los portales de empleo |
| **Skills instalados** | El skill `job-hunter-linkedin` ya viene incluido en el proyecto |

### Tu CV (`cv.md`)

Debe estar en el directorio raíz del proyecto con esta estructura mínima:

```markdown
# Tu Nombre
## Título Profesional

### Experiencia
- [Trabajo 1]
- [Trabajo 2]

### Habilidades Técnicas
- Lenguaje, Framework, Herramienta

### Educación
- Título, Institución
```

> ⚠️ El sistema **NO inventa información**. Solo reorganiza lo que ya está en tu `cv.md`.

---

## 3. Estructura del Proyecto

```
cv-with-pidev-crewai-structure/
│
├── cv.md                              ← Tu CV original (REQUERIDO)
├── cv_job_links.md                    ← Historial de postulaciones (AUTO)
├── cv_gonzalo_[empresa].md            ← CVs generados por empleo (AUTO)
├── AGENTS.md                          ← Configuración del orquestador
├── MANUAL.md                          ← Este manual
│
├── .pi/skills/job-hunter-linkedin/
│   ├── SKILL.md                       ← Configuración del skill
│   ├── README.md                      ← Documentación del skill
│   └── PORTALS.md                     ← Detalle de portales soportados
│
└── [carpetas por empresa]/            ← Material adicional por aplicación
    ├── cv_gonzalo_[empresa].md
    └── carta_presentacion.md (opcional)
```

---

## 4. Configuración Inicial

### Paso 1: Verifica que tu CV existe

```bash
cat cv.md
```

Si no existe, créalo con tu información profesional en formato Markdown.

### Paso 2: Verifica el skill

```bash
cat .pi/skills/job-hunter-linkedin/SKILL.md
```

Debes ver la configuración del `multi_portal_scraper` y los 4 agentes.

### Paso 3: Verifica el tracking

```bash
cat cv_job_links.md
```

Si es tu primera vez, el archivo estará vacío o no existirá. Se crea automáticamente.

---

## 5. Cómo Buscar Empleo

### Comando Principal

Simplemente dile al agente lo que necesitas en lenguaje natural:

```
"Búscame empleo como Senior Backend Developer en Santiago, Chile"
```

O usa la sintaxis completa para mayor control:

```
/skill:job-hunter-linkedin "{job_title}" "{location}" "{experience_level}" "{job_applicants}" "{skills}"
```

### Parámetros

| Parámetro | Qué es | Ejemplo |
|-----------|--------|---------|
| `job_title` | Título del puesto | `Senior Backend Developer` |
| `location` | Ubicación | `Santiago, Chile` |
| `experience_level` | Nivel requerido | `Senior` |
| `job_applicants` | Máx. postulantes aceptable | `50` |
| `skills` | Tus habilidades clave | `Java Spring Boot PostgreSQL Docker` |

### Frases que activan el sistema

Cualquiera de estas funciona:

- `"Búscame empleo"`
- `"Busca trabajos de Java en Chile"`
- `"Genera CV para Senior Backend Developer"`
- `"Encuentra vacantes de DevOps"`
- `"Job hunter"`
- `"Búscame trabajo en GetOnBoard"`
- `"Buscar empleo automáticamente"`

---

## 6. Ejemplos Prácticos

### Ejemplo 1: Búsqueda estándar

```
"Búscame empleo como Senior Backend Java Developer en Santiago, Chile, nivel Senior, máximo 50 postulantes, mis skills son Java Spring Boot React SQL PostgreSQL Docker"
```

**Resultado:**
- Busca en 7 portales simultáneamente
- Encuentra 10-20 empleos relevantes
- Selecciona el que mejor match tiene con tus skills
- Genera `cv_gonzalo_empresa.md` personalizado
- Registra en `cv_job_links.md`

### Ejemplo 2: Solo posiciones remotas

```
"Búscame empleo como Full Stack Developer remoto en Latinoamérica, nivel Senior, máximo 100 postulantes, mis skills son Java React TypeScript PostgreSQL"
```

### Ejemplo 3: Filtro estricto (poca competencia)

```
"Búscame empleo como DevOps Engineer en Chile, nivel Senior, máximo 25 postulantes, mis skills son Docker Kubernetes GCP AWS Terraform"
```

> 💡 **Menos postulantes = menos competencia.** Un empleo con 25 postulantes es más accesible que uno con 200+.

### Ejemplo 4: Búsqueda por tecnología específica

```
"Búscame empleo como Flutter Developer en Chile, nivel Mid-Senior, máximo 75 postulantes, mis skills son Flutter Dart Firebase REST API CI/CD"
```

### Ejemplo 5: Buscar en un portal específico

```
"Búscame empleo en GetOnBoard como Backend Developer en Chile"
```

El sistema priorizará ese portal pero también buscará en los demás.

---

## 7. Portales de Búsqueda

### Los 7 Portales

| Portal | ¿Para qué es bueno? | ¿Requiere login? |
|--------|---------------------|------------------|
| **GetOnBoard** 🥇 | Tech/programación, salarios visibles | ❌ No |
| **Google Jobs** 🥈 | Agregador universal, captura todo | ❌ No |
| **LinkedIn** 🥉 | Red profesional, gran volumen | ⚠️ Parcial |
| **Computrabajo** | Alto volumen en Chile | ❌ No |
| **Indeed** | Agregador global | ❌ No |
| **Chiletrabajos** | Empleo local, pymes | ❌ No |
| **Torre** | Remoto LATAM, matching con IA | ❌ No |

### Estrategia de Búsqueda

```
1. web_search en paralelo (4 queries simultáneas):
   ├─ "site:getonbrd.com {puesto} Chile"
   ├─ "site:cl.linkedin.com/jobs {puesto} Chile"
   ├─ "site:cl.indeed.com {puesto} Chile"
   └─ "{puesto} Chile empleo trabajo {skills}"  ← Google Jobs

2. fetch_content de URLs prometedoras:
   ├─ GetOnBoard → contenido completo (sin login)
   ├─ LinkedIn → páginas públicas individuales
   └─ Otras → extraer descripción disponible

3. Unificar + deduplicar resultados
4. Pasar lista consolidada al analizador
```

### Deduplicación

Si el mismo empleo aparece en múltiples portales:
1. Se detecta por **URL** (si ya está en `cv_job_links.md`, se salta)
2. Se detecta por **Empresa + Título** (misma empresa + título similar = duplicado)
3. Se prefiere el portal con **más información** (salario visible, descripción completa)

---

## 8. Archivos Generados

### CV Personalizado

**Nombre:** `cv_gonzalo_[nombre_empresa_sin_espacios].md`

**Ejemplo:** `cv_gonzalo_2brains.md`

**Contenido:**
- Tu experiencia reorganizada para destacar lo que pide esa vacante
- Habilidades técnicas alineadas con los requisitos del empleo
- Palabras clave del puesto integradas (para pasar filtros ATS)
- **No se inventa ninguna información**

### Historial de Postulaciones

**Nombre:** `cv_job_links.md`

**Formato:**

| Fecha | Empresa | Portal | Título del Puesto | URL | Archivo CV | Estado |
|-------|---------|--------|-------------------|-----|------------|--------|
| 2026-04-28 | 2BRAINS | GetOnBoard | Software Engineer Back-end Senior | https://... | cv_gonzalo_2brains.md | Pendiente |

---

## 9. Tracking de Postulaciones

El archivo `cv_job_links.md` mantiene un historial completo de todas tus aplicaciones.

### Estados

| Estado | Significado |
|--------|-------------|
| `Pendiente` | CV generado pero no enviado |
| `Enviado` | Postulación realizada |
| `Rechazado` | No fue seleccionado |
| `Entrevista` | Te contactaron para entrevista |
| `Oferta` | Recibiste oferta laboral |

### Cómo actualizar el estado

```
"Cambia el estado de la postulación a 2BRAINS a 'Enviado'"
"Marca la postulación a GFT como 'Entrevista'"
```

### Ver tu historial

```
"Muéstrame mi historial de postulaciones"
```

---

## 10. Pipeline de Agentes

El sistema usa 4 agentes que trabajan en secuencia:

```
┌─────────────────────────────────────────────────────────┐
│ 1. multi_portal_scraper                                 │
│    • Busca en 7 portales simultáneamente                │
│    • Extrae: empresa, URL, portal, requisitos, salario  │
│    • Unifica y deduplica resultados                     │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 2. job_analysis_reporter                                │
│    • Analiza cada vacante                               │
│    • Calcula match con tus skills                       │
│    • Selecciona el MEJOR empleo (1 solo)                │
│    • Genera informe con razones de selección            │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 3. resume_skills_customizer                             │
│    • Lee tu cv.md original                              │
│    • Reestructura para destacar lo que pide la vacante  │
│    • Agrega palabras clave para ATS                     │
│    • Genera cv_gonzalo_[empresa].md                     │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 4. cv_job_linkage_tracker                               │
│    • Lee cv_job_links.md existente                      │
│    • Agrega nueva fila con la postulación               │
│    • Incluye: fecha, empresa, portal, URL, CV, estado   │
└─────────────────────────────────────────────────────────┘
```

> ⏱️ **Tiempo estimado:** 2-5 minutos por búsqueda (dependiendo de la cantidad de resultados).

---

## 11. Tips para Mejores Resultados

### 🎯 Skills específicos > Skills genéricos

```
✅ "Java Spring Boot SQL Docker Kubernetes GCP"
❌ "Programación, liderazgo, trabajo en equipo"
```

### 📍 Ubicación flexible = más resultados

```
✅ "Chile" o "Latinoamérica" o "Remoto"
❌ "Limache, Chile" (demasiado específico)
```

### 🔢 Postulantes bajos = menos competencia

```
✅ job_applicants: 25-50 (empleos recientes, menos competencia)
⚠️ job_applicants: 100+ (más competencia, pero más opciones)
```

### 🔄 Ejecuta múltiples búsquedas

Cada búsqueda genera **1 CV personalizado**. Ejecuta varias para tener varios CVs:

```
Búsqueda 1: "Backend Java" → cv_gonzalo_empresa_a.md
Búsqueda 2: "Full Stack"   → cv_gonzalo_empresa_b.md
Búsqueda 3: "DevOps"       → cv_gonzalo_empresa_c.md
```

### 📅 Frecuencia recomendada

| Frecuencia | Recomendación |
|------------|---------------|
| **Diaria** | Ideal si estás buscando activamente |
| **Semanal** | Bueno si tienes empleo y buscas opciones |
| **Quincenal** | Mínimo para no perder oportunidades |

### 📝 Actualiza tu cv.md regularmente

El sistema lee tu `cv.md` para generar CVs personalizados. Si aprendiste una tecnología nueva o cambiaste de trabajo, actualízalo primero.

---

## 12. Solución de Problemas

### No encuentra empleos

| Causa | Solución |
|-------|----------|
| Título muy específico | Usa un título más genérico (ej: "Developer" en lugar de "Senior Cloud-Native Microservices Developer") |
| Ubicación muy restringida | Amplía a todo el país o "Latinoamérica" |
| Skills no coinciden | Incluye las tecnologías más demandadas en tu área |

### CV generado no parece relevante

| Causa | Solución |
|-------|----------|
| cv.md desactualizado | Actualiza tu cv.md con experiencia reciente |
| Skills mal definidos | Sé más específico con las tecnologías |
| Puesto no coincide con tu perfil | Ajusta el job_title a tu experiencia real |

### El mismo empleo aparece en múltiples búsquedas

Esto es **normal**. El sistema tiene deduplicación automática:
- Si el empleo ya está en `cv_job_links.md`, no genera un CV duplicado
- Te informa que ya postulaste a ese empleo

### LinkedIn no devuelve resultados

LinkedIn requiere login. El sistema usa:
- Páginas públicas de LinkedIn (`/jobs/view/*`) accesibles sin login
- Google cache para resultados de LinkedIn
- Otros portales como fuentes principales

> ✅ **GetOnBoard es la fuente principal para tech** — no requiere login y muestra salarios.

---

## 13. Extender el Sistema

### Agregar un nuevo portal

Edita `.pi/skills/job-hunter-linkedin/PORTALS.md` y agrega:

```markdown
| [Nombre] | [URL Base] | [Fortaleza] | [Estrategia] |
```

Y describe la estrategia de búsqueda en la sección "Estrategia por Portal".

### Modificar los agentes

Edita `.pi/skills/job-hunter-linkedin/SKILL.md` para:
- Cambiar el comportamiento de cualquier agente
- Agregar reglas de filtrado adicionales
- Modificar el formato de salida

### Agregar campos al tracking

Edita la tabla en `cv_job_links.md` y en `SKILL.md` (sección del Agente 4) para agregar columnas como:
- `Salario` — Rango salarial del empleo
- `Modalidad` — Remoto/Híbrido/Presencial
- `Respuesta` — Fecha de respuesta de la empresa

### Crear cartas de presentación

Puedes pedir al agente:

```
"Genera una carta de presentación para la vacante de 2BRAINS"
```

Esto crea un archivo `[empresa]_carta_presentacion.md` personalizado.

---

## 📞 Resumen Rápido

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUJO DE 1 MINUTO                        │
│                                                             │
│ 1. Actualiza cv.md si hay cambios                           │
│ 2. Di: "Búscame empleo como [título] en [ubicación]"        │
│ 3. Espera 2-5 minutos                                       │
│ 4. Revisa el CV generado: cv_gonzalo_[empresa].md           │
│ 5. Revisa cv_job_links.md para confirmar el registro        │
│ 6. ¡Postula con el CV personalizado!                        │
│ 7. Actualiza el estado a "Enviado"                          │
└─────────────────────────────────────────────────────────────┘
```

---

*Manual generado el 2026-04-28 — Versión 2.0 (Multi-Portal)*
