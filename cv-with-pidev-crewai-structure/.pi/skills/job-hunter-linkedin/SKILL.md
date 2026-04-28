---
name: job-hunter-job
description: Buscador automatizado de empleos multi-portal con personalización de CV. Busca en LinkedIn, GetOnBoard, Computrabajo, Indeed, Chiletrabajos, Torre y Google Jobs. Úsalo cuando el usuario quiera encontrar empleo, buscar trabajo, crear CV personalizado para una vacante, o frases como "búscame empleo", "encuentra trabajos", "optimiza mi CV para este puesto", "aplica a empleos automáticamente", "genera CV para [puesto]".
allowed-tools: subagent, read, write, edit, web_search, fetch_content, navegar
required-files: cv.md (en el directorio del proyecto)
output-files: cv_job_links.md, cv_[nombre_empresa].md
---

# 🎯 Multi-Portal Job Hunter & ATS Optimizer

Sistema multi-agente que busca empleos en **múltiples portales** (LinkedIn, GetOnBoard, Computrabajo, Indeed, Chiletrabajos, Torre, Google Jobs), analiza vacantes y personaliza tu CV para cada aplicación.

## 🔧 Variables de Configuración

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `{job_title}` | Título del puesto a buscar | Senior Backend Developer |
| `{location}` | Ubicación geográfica | Santiago, Chile |
| `{experience_level}` | Nivel de experiencia | Senior / 5+ años |
| `{job_applicants}` | Máximo de candidatos en la vacante | 50 |
| `{skills}` | Habilidades clave del usuario | Java, Spring Boot, React |
| `{portals}` | Portales a buscar (opcional, default: todos) | getonbrd,linkedin |

## 🌐 Portales Soportados

Ver `.pi/skills/job-hunter-linkedin/PORTALS.md` para la lista completa con estrategias detalladas.

| Portal | Prioridad | Requiere Login | Salarios Visibles |
|--------|-----------|----------------|-------------------|
| GetOnBoard | 🥇 Alta | ❌ No | ✅ Sí |
| LinkedIn | 🥈 Media | ⚠️ Parcial | ❌ No |
| Google Jobs | 🥉 Alta | ❌ No | ⚠️ Variable |
| Computrabajo | Media | ❌ No | ⚠️ Variable |
| Indeed | Media | ❌ No | ❌ No |
| Chiletrabajos | Baja | ❌ No | ❌ No |
| Torre | Baja | ❌ No | ⚠️ Variable |

## 👥 Agentes del Pipeline

### Agente 1: `multi_portal_scraper`
**Rol:** Especialista en extracción de datos de múltiples portales de empleo
**Objetivo:** Buscar y extraer información detallada de empleos en TODOS los portales soportados

**Tareas:**
1. Buscar empleos con título `{job_title}` en `{location}` en **todos los portales** (ver tabla de portales arriba)
2. Estrategia de búsqueda paralela:
   - `web_search` con queries `site:{portal}` para cada portal
   - `fetch_content` directo a GetOnBoard (sin login requerido)
   - `fetch_content` de páginas públicas de LinkedIn (`/jobs/view/*`)
   - `web_search` general como Google Jobs fallback
3. Filtrar por `{experience_level}` (Senior/Jr/etc.)
4. Extraer: empresa, URL, **portal de origen**, requisitos, habilidades, salario, número de postulantes
5. **NO** incluir empleos que ya estén en `cv_job_links.md` (verificar por URL)
6. Priorizar empleos publicados hace menos de 30 días
7. Unificar resultados y deduplicar (mismo empleo en múltiples portales → preferir el portal con más info)

**Herramientas:** `web_search`, `fetch_content`, `navegar`

**Estrategia de búsqueda:**
```
Paso A: web_search en paralelo
  ├─ "site:getonbrd.com {job_title} Chile"
  ├─ "site:cl.linkedin.com/jobs {job_title} Chile"
  ├─ "site:cl.indeed.com {job_title} Chile"
  └─ "{job_title} Chile empleo trabajo {skills}" (Google Jobs fallback)

Paso B: fetch_content de URLs prometedoras
  ├─ getonbrd.com → contenido completo directo
  ├─ linkedin.com/jobs/view/* → páginas públicas
  └─ Otras URLs → intentar extraer descripción

Paso C: Unificar + deduplicar → Lista consolidada
```

---

### Agente 2: `job_analysis_reporter`
**Rol:** Asesor de carrera y analista de mercado laboral
**Objetivo:** Analizar y seleccionar el mejor empleo para el usuario

**Tareas:**
1. Analizar todas las vacantes encontradas por el Agente 1 (multi-portal)
2. Verificar que el número de candidatos no supere `{job_applicants}`
3. Calcular match entre habilidades del usuario (`{skills}`) y requisitos
4. Seleccionar **SOLO 1 EMPLEO** con mayor coincidencia
5. Generar informe con: resumen ejecutivo, análisis de requisitos, razones de selección, **portal de origen**

**Herramientas:** `read` (cv.md), `bash`

---

### Agente 3: `resume_skills_customizer`
**Rol:** Consultor de carrera y experto en optimización ATS
**Objetivo:** Crear CV personalizado para la vacante seleccionada

**Tareas:**
1. Leer `cv.md` original y el informe del Agente 2
2. Identificar habilidades del CV que coincidan con los requisitos del empleo
3. Reestructurar el CV priorizando:
   - Experiencia relevante al puesto
   - Habilidades técnicas mencionadas en la vacante
   - Palabras clave del empleo (para ATS)
4. **NO inventar información** - solo reorganizar la existente
5. Generar archivo: `cv_gonzalo_[nombre_empresa_sin_espacios].md`

**Herramientas:** `read`, `write`

---

### Agente 4: `cv_job_linkage_tracker`
**Rol:** Gestor de tracking y trazabilidad documental
**Objetivo:** Registrar la vinculación CV-Empleo en el historial

**Tareas:**
1. Leer `cv_job_links.md` existente
2. Agregar nueva fila con formato:

| Fecha | Empresa | Portal | Título del Puesto | URL | Archivo CV | Estado |
|-------|---------|--------|-------------------|-----|------------|--------|
| YYYY-MM-DD | [Empresa] | [Portal] | [Título] | [URL] | [Archivo] | Pendiente |

3. Si el empleo ya existe en el archivo (por URL), **no duplicar** - informar al usuario
4. Mantener el historial completo de todas las postulaciones

**Herramientas:** `read`, `write`, `edit`

---

## 📋 Pipeline de Ejecución

```
multi_portal_scraper → job_analysis_reporter → resume_skills_customizer → cv_job_linkage_tracker
```

### Paso 1: Extracción Multi-Portal
```
Agente: multi_portal_scraper
Acción: Buscar empleos con {job_title} en {location} en TODOS los portales
  ├─ GetOnBoard (prioridad alta para tech)
  ├─ LinkedIn (vía Google cache/páginas públicas)
  ├─ Google Jobs (fallback universal)
  ├─ Computrabajo, Indeed, Chiletrabajos, Torre
  └─ Unificar + deduplicar
Resultado: Lista consolidada de empleos únicos con portal de origen
```

### Paso 2: Análisis y Selección
```
Agente: job_analysis_reporter
Entrada: Resultados del Paso 1
Acción: Analizar y seleccionar 1 empleo que coincida con {skills}
Resultado: Informe con el empleo seleccionado y razones de selección
```

### Paso 3: Personalización del CV
```
Agente: resume_skills_customizer
Entrada: cv.md + Informe del Paso 2
Acción: Crear CV personalizado para el empleo seleccionado
Resultado: Archivo cv_gonzalo_[empresa].md
```

### Paso 4: Registro de Tracking
```
Agente: cv_job_linkage_tracker
Entrada: URL del empleo + Portal de origen + Nombre del archivo CV
Acción: Agregar nueva fila a cv_job_links.md
Resultado: Archivo cv_job_links.md actualizado
```

---

## 📁 Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `cv.md` | CV original del usuario (requerido) |
| `cv_job_links.md` | Historial de postulaciones generadas |
| `cv_gonzalo_[empresa].md` | CV personalizado por empleo |
| `.pi/skills/job-hunter-linkedin/PORTALS.md` | Documentación de portales soportados |

---

## 🔍 Ejemplos de Uso

### Ejemplo 1: Buscar empleo específico (todos los portales)
```
/skill:job-hunter-linkedin "Senior Backend Java Developer" "Santiago, Chile" "Senior" "50" "Java Spring Boot React SQL"
```

### Ejemplo 2: Buscar solo en GetOnBoard
```
/skill:job-hunter-linkedin "Full Stack Developer" "Chile" "Senior" "100" "Java React PostgreSQL"
```

### Ejemplo 3: Buscar DevOps en Latinoamérica
```
/skill:job-hunter-linkedin "DevOps Engineer" "Latinoamérica" "Senior" "75" "Docker Kubernetes GCP AWS"
```

---

## ⚠️ Reglas de Comportamiento

1. **Verificar duplicados:** Si el empleo ya está en `cv_job_links.md`, no generar nuevo CV
2. **No inventar datos:** Solo reorganizar información existente del CV
3. **Prioridad:** Empleos con menor número de candidatos tienen prioridad
4. **Fecha actual:** Usar YYYY-MM-DD para la fecha en el tracking
5. **Selección única:** Solo generar 1 CV por ejecución (el mejor match)
6. **Limpiar URLs:** Eliminar parámetros de tracking innecesarios en las URLs
7. **Portal de origen:** Siempre registrar en qué portal se encontró el empleo
8. **Deduplicación inteligente:** Si el mismo empleo aparece en 2+ portales, preferir el portal con más información (salario visible, descripción completa)
9. **GetOnBoard prioridad:** Para puestos tech, GetOnBoard es la fuente principal (salarios visibles, sin login)

---

## 📝 Formato del Archivo de Tracking

```markdown
# 📋 Registro de CVs Personalizados vs Empleos

| Fecha | Empresa | Portal | Título del Puesto | URL | Archivo CV | Estado |
|-------|---------|--------|-------------------|-----|------------|--------|
| 2026-04-27 | BC Tecnología | GetOnBoard | Desarrollador Back-end Java Spring Boot | https://www.getonbrd.com/... | cv_gonzalo_bc_tecnologia.md | Enviado |
| 2026-04-27 | GFT Technologies | Portal GFT | Senior Full Stack Java React | https://jobs.gft.com/... | cv_gonzalo_gft_technologies.md | Enviado |
| 2026-04-28 | 2BRAINS | GetOnBoard | Software Engineer Back-end Senior | https://www.getonbrd.com/... | cv_gonzalo_2brains.md | Pendiente |
```

---

## 🔄 Flujo de Variables

```
Usuario proporciona: job_title, location, experience_level, job_applicants, skills
                    ↓
Agente 1 (multi_portal): Busca en 7 portales simultáneamente
  ├─ GetOnBoard (prioridad tech)
  ├─ LinkedIn (Google cache)
  ├─ Google Jobs (universal)
  └─ Computrabajo, Indeed, Chiletrabajos, Torre
  └─ Unificar + deduplicar
                    ↓
Agente 2 (reporter): Selecciona mejor match
                    ↓
Agente 3 (customizer): Crea CV personalizado
                    ↓
Agente 4 (tracker): Registra en cv_job_links.md (con portal)
                    ↓
Usuario recibe: CV listo + registro actualizado
```

---

## 🎯 Keywords para Activar este Skill

- "búscame empleo"
- "busca trabajos"
- "crea CV para [puesto]"
- "optimiza mi CV para este empleo"
- "aplica a este trabajo"
- "genera CV personalizado"
- "encuentra vacantes de [título]"
- "job hunter"
- "buscar empleo automáticamente"
- "búscame trabajo en [portal]"
- "buscar empleo multi-portal"
