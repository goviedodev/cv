---
name: job-hunter-linkedin
description: Buscador automatizado de empleos en LinkedIn con personalización de CV. Úsalo cuando el usuario quiera encontrar empleo, buscar trabajo en LinkedIn, crear CV personalizado para una vacante, o frases como "búscame empleo", "encuentra trabajos en LinkedIn", "optimiza mi CV para este puesto", "aplica a empleos automáticamente", "genera CV para [puesto]".
allowed-tools: subagent, read, write, edit, web_search, fetch_content, navegar
required-files: cv.md (en el directorio del proyecto)
output-files: cv_job_links.md, cv_[nombre_empresa].md
---

# 🎯 LinkedIn Job Hunter & ATS Optimizer

Sistema multi-agente que busca empleos en LinkedIn, analiza vacantes y personaliza tu CV para cada aplicación.

## 🔧 Variables de Configuración

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `{job_title}` | Título del puesto a buscar | Senior Backend Developer |
| `{location}` | Ubicación geográfica | Santiago, Chile |
| `{experience_level}` | Nivel de experiencia | Senior / 5+ años |
| `{job_applicants}` | Máximo de candidatos en la vacante | 50 |
| `{skills}` | Habilidades clave del usuario | Java, Spring Boot, React |

## 👥 Agentes del Pipeline

### Agente 1: `linkedin_job_scraper`
**Rol:** Especialista en extracción de datos de LinkedIn
**Objetivo:** Buscar y extraer información detallada de empleos en LinkedIn

**Tareas:**
1. Buscar empleos con título `{job_title}` en `{location}`
2. Filtrar por `{experience_level}` (Senior/Jr/etc.)
3. Extraer: empresa, URL, requisitos, habilidades, salario, número de postulantes
4. **NO** incluir empleos que ya estén en `cv_job_links.md`
5. Priorizar empleos publicados hace menos de 7 días

**Herramientas:** web_search, fetch_content, navegar

---

### Agente 2: `job_analysis_reporter`
**Rol:** Asesor de carrera y analista de mercado laboral
**Objetivo:** Analizar y seleccionar el mejor empleo para el usuario

**Tareas:**
1. Analizar todas las vacantes encontradas por el Agente 1
2. Verificar que el número de candidatos no supere `{job_applicants}`
3. Calcular match entre habilidades del usuario (`{skills}`) y requisitos
4. Seleccionar **SOLO 1 EMPLEO** con mayor coincidencia
5. Generar informe con: resumen ejecutivo, análisis de requisitos, razones de selección

**Herramientas:** read (cv.md), bash

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

**Herramientas:** read, write

---

### Agente 4: `cv_job_linkage_tracker`
**Rol:** Gestor de tracking y trazabilidad documental
**Objetivo:** Registrar la vinculación CV-Empleo en el historial

**Tareas:**
1. Leer `cv_job_links.md` existente
2. Agregar nueva fila con formato:

| Fecha | Empresa | Título del Puesto | URL LinkedIn | Archivo CV |
|-------|---------|-------------------|--------------|------------|
| YYYY-MM-DD | [Empresa] | [Título] | [URL] | [Archivo] |

3. Si el empleo ya existe en el archivo, **no duplicar** - informar al usuario
4. Mantener el historial completo de todas las postulaciones

**Herramientas:** read, write, edit

---

## 📋 Pipeline de Ejecución

```
linkedin_job_scraper → job_analysis_reporter → resume_skills_customizer → cv_job_linkage_tracker
```

### Paso 1: Extracción de Datos
```
Agente: linkedin_job_scraper
Acción: Buscar empleos con {job_title} en {location}
Resultado: Lista de empleos con URLs, requisitos y número de postulantes
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
Entrada: URL del empleo + Nombre del archivo CV
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

---

## 🔍 Ejemplos de Uso

### Ejemplo 1: Buscar empleo específico
```
/skill:job-hunter-linkedin "Senior Backend Java Developer" "Santiago, Chile" "Senior" "50" "Java Spring Boot React SQL"
```

### Ejemplo 2: Buscar con parámetros mínimos
```
/skill:job-hunter-linkedin "Full Stack Developer" "Chile" "Senior" "100" "Java React PostgreSQL"
```

### Ejemplo 3: Usando pipeline completo
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

---

## 📝 Formato del Archivo de Tracking

```markdown
# 📋 Registro de CVs Personalizados vs Empleos

| Fecha | Empresa | Título del Puesto | URL LinkedIn | Archivo CV |
|-------|---------|-------------------|--------------|------------|
| 2026-04-27 | BC Tecnología | Backend Java Spring Boot | https://cl.linkedin.com/jobs/view/... | cv_gonzalo_bc_tecnologia.md |
| 2026-04-27 | GFT Technologies | Senior Full Stack Java React | https://cl.linkedin.com/jobs/view/... | cv_gonzalo_gft_technologies.md |
```

---

## 🔄 Flujo de Variables

```
Usuario proporciona: job_title, location, experience_level, job_applicants, skills
                    ↓
Agente 1 (scraper): Busca empleos, filtra por candidatos
                    ↓
Agente 2 (reporter): Selecciona mejor match
                    ↓
Agente 3 (customizer): Crea CV personalizado
                    ↓
Agente 4 (tracker): Registra en cv_job_links.md
                    ↓
Usuario recibe: CV listo + registro actualizado
```

---

## 🎯 Keywords para Activar este Skill

- "búscame empleo en LinkedIn"
- "busca trabajos"
- "crea CV para [puesto]"
- "optimiza mi CV para este empleo"
- "aplica a este trabajo"
- "genera CV personalizado"
- "encuentra vacantes de [título]"
- "job hunter"
- "linkedin jobs"
- "buscar empleo automáticamente"