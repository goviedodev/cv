# 🎯 Job Hunter Multi-Portal - Skill Documentation

Skill multi-agente para buscar empleos en **múltiples portales** (LinkedIn, GetOnBoard, Computrabajo, Indeed, Chiletrabajos, Torre, Google Jobs), analizar vacantes y personalizar tu CV automáticamente.

---

## 🚀 Instalación

El skill ya está incluido en tu proyecto en:

```
./.pi/skills/job-hunter-linkedin/SKILL.md
```

Documentación de portales soportados:

```
./.pi/skills/job-hunter-linkedin/PORTALS.md
```

---

## 📖 Descripción

Este skill orquesta **4 agentes** que trabajan en secuencia para:

1. 🔍 **Buscar empleos** en 7 portales simultáneamente según criterios específicos
2. 📊 **Analizar vacantes** y seleccionar la mejor opción
3. ✂️ **Personalizar tu CV** adaptándolo a los requisitos del empleo
4. 📋 **Registrar** la postulación en el historial de tracking (con portal de origen)

### Portales Soportados

| Portal | Prioridad | Requiere Login | Salarios Visibles |
|--------|-----------|----------------|-------------------|
| GetOnBoard | 🥇 Alta | ❌ No | ✅ Sí |
| LinkedIn | 🥈 Media | ⚠️ Parcial | ❌ No |
| Google Jobs | 🥉 Alta | ❌ No | ⚠️ Variable |
| Computrabajo | Media | ❌ No | ⚠️ Variable |
| Indeed | Media | ❌ No | ❌ No |
| Chiletrabajos | Baja | ❌ No | ❌ No |
| Torre | Baja | ❌ No | ⚠️ Variable |

---

## ⚙️ Variables de Configuración

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `job_title` | Título del puesto a buscar | `Senior Backend Java Developer` |
| `location` | Ubicación geográfica | `Santiago, Chile` |
| `experience_level` | Nivel de experiencia requerido | `Senior` |
| `job_applicants` | Máximo de candidatos permitidos en la vacante | `50` |
| `skills` | Habilidades clave del usuario (separadas por espacios) | `Java Spring Boot React SQL` |

---

## 📝 Sintaxis de Invocación

```
/skill:job-hunter-linkedin "<job_title>" "<location>" "<experience_level>" "<job_applicants>" "<skills>"
```

---

## 💡 Ejemplos de Invocación

### Ejemplo 1: Buscar empleo Backend Java Senior (todos los portales)

```bash
/skill:job-hunter-linkedin "Senior Backend Java Developer" "Santiago, Chile" "Senior" "50" "Java Spring Boot Spring Cloud PostgreSQL"
```

**Resultado esperado:**
- Busca empleos en GetOnBoard, LinkedIn, Google Jobs, Computrabajo, Indeed, Chiletrabajos, Torre
- Filtra vacantes con máximo 50 candidatos
- Genera `cv_gonzalo_[empresa].md` personalizado
- Registra en `cv_job_links.md` con portal de origen

### Ejemplo 2: Buscar empleo Full Stack

```bash
/skill:job-hunter-linkedin "Full Stack Developer" "Chile" "Senior" "75" "Java React PostgreSQL Docker"
```

### Ejemplo 3: Buscar empleo DevOps

```bash
/skill:job-hunter-linkedin "DevOps Engineer" "Latinoamérica" "Senior" "100" "Docker Kubernetes GCP AWS Azure"
```

### Ejemplo 4: Buscar empleo Flutter Mobile

```bash
/skill:job-hunter-linkedin "Flutter Developer" "Chile" "Senior" "30" "Flutter Dart Firebase REST API"
```

### Ejemplo 5: Buscar con filtro estricto (pocos candidatos)

```bash
/skill:job-hunter-linkedin "Backend Developer" "Santiago, Chile" "Senior" "25" "Java Spring Boot SQL Oracle"
```

---

## 🔄 Pipeline de Agentes

```
multi_portal_scraper → job_analysis_reporter → resume_skills_customizer → cv_job_linkage_tracker
```

### Flujo Detallado

```
┌─────────────────────────────────────────────────────────────────┐
│ Agente 1: multi_portal_scraper                                 │
│ ├─ Busca empleos en 7 portales simultáneamente                  │
│ │  ├─ GetOnBoard (prioridad alta para tech)                    │
│ │  ├─ LinkedIn (vía Google cache/páginas públicas)              │
│ │  ├─ Google Jobs (fallback universal)                         │
│ │  └─ Computrabajo, Indeed, Chiletrabajos, Torre               │
│ ├─ Unifica + deduplica resultados                              │
│ ├─ Filtra por location y experience_level                      │
│ ├─ Verifica que candidatos < job_applicants                    │
│ └─ Excluye empleos ya en cv_job_links.md                       │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Agente 2: job_analysis_reporter                                 │
│ ├─ Analiza requisitos de cada vacante                          │
│ ├─ Calcula match con skills del usuario                        │
│ ├─ Selecciona el MEJOR empleo (mayor coincidencia)             │
│ └─ Genera informe con razones de selección                      │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Agente 3: resume_skills_customizer                             │
│ ├─ Lee cv.md original                                          │
│ ├─ Reestructura priorizando skills del empleo                 │
│ ├─ Agrega palabras clave para ATS                             │
│ └─ Genera: cv_gonzalo_[empresa_sin_espacios].md                 │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Agente 4: cv_job_linkage_tracker                               │
│ ├─ Lee cv_job_links.md existente                              │
│ ├─ Verifica que el empleo no esté duplicado                   │
│ ├─ Agrega nueva fila con: Fecha | Empresa | Portal | Título   │
│ │   | URL | CV | Estado                                       │
│ └─ Guarda historial completo de postulaciones                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Archivos Generados

| Archivo | Descripción | Ubicación |
|---------|-------------|-----------|
| `cv_gonzalo_[empresa].md` | CV personalizado por empleo | Directorio del proyecto |
| `cv_job_links.md` | Historial de todas las postulaciones (con portal) | Directorio del proyecto |

---

## 📊 Ejemplo de cv_job_links.md

```markdown
# 📋 Registro de CVs Personalizados vs Empleos

| Fecha | Empresa | Portal | Título del Puesto | URL | Archivo CV | Estado |
|-------|---------|--------|-------------------|-----|------------|--------|
| 2026-04-27 | BC Tecnología | GetOnBoard | Desarrollador Back-end Java Spring Boot | https://www.getonbrd.com/... | cv_gonzalo_bc_tecnologia.md | Enviado |
| 2026-04-27 | GFT Technologies | Portal GFT | Senior Full Stack Java React | https://jobs.gft.com/... | cv_gonzalo_gft_technologies.md | Enviado |
| 2026-04-28 | 2BRAINS | GetOnBoard | Software Engineer Back-end Senior | https://www.getonbrd.com/... | cv_gonzalo_2brains.md | Pendiente |
```

---

## 🎯 Keywords para Activar

Usa cualquiera de estas frases para activar el skill:

- "búscame empleo"
- "busca trabajos de [título]"
- "crea CV para [puesto]"
- "optimiza mi CV para este empleo"
- "aplica a este trabajo"
- "genera CV personalizado"
- "encuentra vacantes de [título]"
- "job hunter"
- "buscar empleo automáticamente"
- "encontrar trabajo como [título]"
- "aplicar a [título] en [location]"
- "búscame trabajo en [portal]"
- "buscar empleo multi-portal"

---

## 🌐 Portales Detallados

Consulta `.pi/skills/job-hunter-linkedin/PORTALS.md` para:
- URLs de búsqueda específicas por portal
- Estrategias de scraping por portal
- Ventajas y limitaciones de cada portal
- Flujo de ejecución optimizado
- Deduplicación inteligente

---

## ⚠️ Reglas de Comportamiento

1. **No duplica postulaciones:** Si el empleo ya existe en `cv_job_links.md`, no genera nuevo CV
2. **No inventa información:** Solo reorganiza datos existentes del CV original
3. **Selección única:** Solo genera 1 CV por ejecución (el mejor match)
4. **Prioridad:** Empleos con menor número de candidatos tienen mayor prioridad
5. **Fecha automática:** Usa YYYY-MM-DD para registrar la fecha actual
6. **Portal de origen:** Siempre registra en qué portal se encontró el empleo
7. **Deduplicación:** Si el mismo empleo aparece en múltiples portales, prefiere el que tenga más info
8. **GetOnBoard prioridad:** Para puestos tech, es la fuente principal

---

## 🔧 Requisitos

- Archivo `cv.md` debe existir en el directorio del proyecto
- Conexión a internet para buscar en múltiples portales
- Proyecto configurado con estructura Pi.dev

---

## 📞 Soporte

Para modificar o extender el skill, edita los archivos:

```
./.pi/skills/job-hunter-linkedin/SKILL.md    ← Configuración principal
./.pi/skills/job-hunter-linkedin/PORTALS.md  ← Portales soportados
```
