# 🎯 Job Hunter LinkedIn - Skill Documentation

Skill multi-agente para buscar empleos en LinkedIn, analizar vacantes y personalizar tu CV automáticamente.

---

## 🚀 Instalación

El skill ya está incluido en tu proyecto en:

```
./.pi/skills/job-hunter-linkedin/SKILL.md
```

---

## 📖 Descripción

Este skill orquesta **4 agentes** que trabajan en secuencia para:

1. 🔍 **Buscar empleos** en LinkedIn según criterios específicos
2. 📊 **Analizar vacantes** y seleccionar la mejor opción
3. ✂️ **Personalizar tu CV** adaptándolo a los requisitos del empleo
4. 📋 **Registrar** la postulación en el historial de tracking

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

### Formato General

```bash
/skill:job-hunter-linkedin "<job_title>" "<location>" "<experience_level>" "<job_applicants>" "<skills>"
```

---

## 💡 Ejemplos de Invocación

### Ejemplo 1: Buscar empleo Backend Java Senior

```bash
/skill:job-hunter-linkedin "Senior Backend Java Developer" "Santiago, Chile" "Senior" "50" "Java Spring Boot Spring Cloud PostgreSQL"
```

**Resultado esperado:**
- Busca empleos de "Senior Backend Java Developer" en Santiago
- Filtra vacantes con máximo 50 candidatos
- Genera `cv_gonzalo_[empresa].md` personalizado
- Registra en `cv_job_links.md`

---

### Ejemplo 2: Buscar empleo Full Stack

```bash
/skill:job-hunter-linkedin "Full Stack Developer" "Chile" "Senior" "75" "Java React PostgreSQL Docker"
```

**Resultado esperado:**
- Busca empleos de "Full Stack Developer" en Chile
- Filtra vacantes con máximo 75 candidatos
- Personaliza el CV con habilidades en Java, React, PostgreSQL y Docker

---

### Ejemplo 3: Buscar empleo DevOps

```bash
/skill:job-hunter-linkedin "DevOps Engineer" "Latinoamérica" "Senior" "100" "Docker Kubernetes GCP AWS Azure"
```

**Resultado esperado:**
- Busca empleos de "DevOps Engineer" en Latinoamérica
- Filtra vacantes con máximo 100 candidatos
- Genera CV enfocando experiencia en contenedores y cloud

---

### Ejemplo 4: Buscar empleo Flutter Mobile

```bash
/skill:job-hunter-linkedin "Flutter Developer" "Chile" "Senior" "30" "Flutter Dart Firebase REST API"
```

**Resultado esperado:**
- Busca empleos de "Flutter Developer" en Chile
- Filtra vacantes con máximo 30 candidatos
- Personaliza CV resaltando experiencia en desarrollo móvil

---

### Ejemplo 5: Buscar empleo con filtro estricto (pocos candidatos)

```bash
/skill:job-hunter-linkedin "Backend Developer" "Santiago, Chile" "Senior" "25" "Java Spring Boot SQL Oracle"
```

**Resultado esperado:**
- Busca empleos con máximo 25 postulantes (vacantes más recientes/exclusivas)
- Enfoca en posiciones que paguen bien por tener menos competencia

---

## 🔄 Pipeline de Agentes

```
linkedin_job_scraper → job_analysis_reporter → resume_skills_customizer → cv_job_linkage_tracker
```

### Flujo Detallado

```
┌─────────────────────────────────────────────────────────────────┐
│ Agente 1: linkedin_job_scraper                                 │
│ ├─ Busca empleos en LinkedIn                                   │
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
│ ├─ Agrega nueva fila con: Fecha | Empresa | Título | URL | CV  │
│ └─ Guarda historial completo de postulaciones                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Archivos Generados

| Archivo | Descripción | Ubicación |
|---------|-------------|-----------|
| `cv_gonzalo_[empresa].md` | CV personalizado por empleo | Directorio del proyecto |
| `cv_job_links.md` | Historial de todas las postulaciones | Directorio del proyecto |

---

## 📊 Ejemplo de cv_job_links.md

```markdown
# 📋 Registro de CVs Personalizados vs Empleos

| Fecha | Empresa | Título del Puesto | URL LinkedIn | Archivo CV |
|-------|---------|-------------------|--------------|------------|
| 2026-04-27 | BC Tecnología | Backend Java Spring Boot | https://cl.linkedin.com/jobs/view/... | cv_gonzalo_bc_tecnologia.md |
| 2026-04-27 | GFT Technologies | Senior Full Stack Java React | https://cl.linkedin.com/jobs/view/... | cv_gonzalo_gft_technologies.md |
| 2026-04-27 | BancoConsorcio | Analista Desarrollador Fullstack Java | https://cl.linkedin.com/jobs/view/... | cv_gonzalo_consorcio.md |
```

---

## 🎯 Keywords para Activar

Usa cualquiera de estas frases para activar el skill:

- "búscame empleo en LinkedIn"
- "busca trabajos de [título]"
- "crea CV para [puesto]"
- "optimiza mi CV para este empleo"
- "aplica a este trabajo"
- "genera CV personalizado"
- "encuentra vacantes de [título]"
- "job hunter"
- "linkedin jobs"
- "buscar empleo automáticamente"
- "encontrar trabajo como [título]"
- "aplicar a [título] en [location]"

---

## ⚠️ Reglas de Comportamiento

1. **No duplica postulaciones:** Si el empleo ya existe en `cv_job_links.md`, no genera nuevo CV
2. **No inventa información:** Solo reorganiza datos existentes del CV original
3. **Selección única:** Solo genera 1 CV por ejecución (el mejor match)
4. **Prioridad:** Empleos con menor número de candidatos tienen mayor prioridad
5. **Fecha automática:** Usa YYYY-MM-DD para registrar la fecha actual

---

## 🔧 Requisitos

- Archivo `cv.md` debe existir en el directorio del proyecto
- Conexión a internet para buscar en LinkedIn
- Proyecto configurado con estructura Pi.dev

---

## 📞 Soporte

Para modificar o extender el skill, edita el archivo:

```
./.pi/skills/job-hunter-linkedin/SKILL.md
```

Allí encontrarás la configuración completa de cada agente, herramientas disponibles y flujos de trabajo.