# 🌐 Portales de Búsqueda Soportados

## Portales Principales

| Portal | URL Base | Fortaleza | Estrategia de Búsqueda |
|--------|----------|-----------|----------------------|
| **LinkedIn** | cl.linkedin.com/jobs | Red profesional, gran volumen | `web_search` con `site:cl.linkedin.com/jobs` + `fetch_content` (páginas públicas) |
| **GetOnBoard** | getonbrd.com | Tech/programación LATAM, salarios visibles | `fetch_content` directo a `/empleos/programacion` y tags |
| **Computrabajo** | computrabajo.cl | Alto volumen Chile | `web_search` + `navegar` |
| **Indeed** | cl.indeed.com | Agregador global | `web_search` con `site:cl.indeed.com` |
| **Chiletrabajos** | chiletrabajos.cl | Empleo local Chile | `web_search` + `navegar` |
| **Torre** | torre.co | Remoto LATAM, matching inteligente | `web_search` + `navegar` |
| **Google Jobs** | google.com/search | Agregador universal (captura todo) | `web_search` como fallback universal |

---

## Estrategia por Portal

### 🥇 GetOnBoard (Prioridad ALTA para tech)
- **URLs de búsqueda:**
  - `https://www.getonbrd.com/empleos/programacion/{keyword}`
  - `https://www.getonbrd.com/jobs/tag/{tech-tag}`
- **Ventajas:**
  - Salarios publicados en USD
  - Filtros por remoto/senior
  - Tags de tecnología específicos
  - **No requiere login**
- **Herramienta recomendada:** `fetch_content` directo
- **Keywords de ejemplo:** `java`, `spring-boot`, `backend`, `full-stack`

### 🥈 LinkedIn (Complementaria)
- **Limitación:** Requiere autenticación para ver listados
- **Estrategia workaround:**
  - `web_search` con query `site:cl.linkedin.com/jobs "{job_title}" Chile`
  - `fetch_content` de URLs individuales públicas (`/jobs/view/...`)
  - Páginas públicas siempre accesibles sin login
- **Ventajas:** Mayor volumen, datos de empresa, networking

### 🥉 Computrabajo
- **URLs:** `https://www.computrabajo.cl/trabajo-de-{keyword}-en-{location}`
- **Ventajas:** Gran volumen de empleos locales
- **Herramientas:** `web_search` + `navegar` para detalles

### Indeed Chile
- **URLs:** `https://cl.indeed.com/q-{keyword}-l-Chile-empleos.html`
- **Ventajas:** Agregador que indexa de múltiples fuentes
- **Herramientas:** `web_search` con `site:cl.indeed.com`

### Chiletrabajos
- **URLs:** `https://www.chiletrabajos.cl/trabajo/{keyword}-{location}`
- **Ventajas:** Empleo local chileno, incluye pymes
- **Herramientas:** `web_search` + `navegar`

### Torre
- **URLs:** `https://www.torre.co/jobs?q={keyword}&location=Chile`
- **Ventajas:** Remoto LATAM, matching con IA
- **Herramientas:** `web_search` + `navegar`

---

## Google Jobs — Red de Seguridad Universal

Google Jobs **agrega resultados de todos los portales** + sitios de empresas directos.

**Query óptima:**
```
web_search("{job_title} Chile empleo trabajo remoto {skills}")
```

**Ventajas:**
- Captura empleos publicados solo en sitios corporativos
- Incluye portales que otros scrapers pueden perder
- Resultados de `glassdoor.com`, `occ.com.mx`, `ziprecruiter.com`
- Siempre accesible sin login

---

## Deduplicación Inteligente

Un mismo empleo puede aparecer en múltiples portales. Se deduplica por:

1. **URL exacta** → si ya existe en `cv_job_links.md`, se salta
2. **Empresa + Título similar** → si misma empresa y título coincidente >80%, se considera duplicado
3. **Portal diferente** → si el mismo empleo aparece en 2 portales, se prefiere el portal con más info (salario, descripción completa)

---

## Flujo de Ejecución Optimizado

```
Paso 1: web_search con múltiples queries en paralelo
  ├─ "site:getonbrd.com {job_title} Chile"
  ├─ "site:cl.linkedin.com/jobs {job_title} Chile"  
  ├─ "site:cl.indeed.com {job_title} Chile"
  └─ "{job_title} Chile empleo {skills}"

Paso 2: fetch_content de las URLs más prometedoras
  ├─ getonbrd.com → contenido completo directo
  ├─ linkedin.com/jobs/view/* → páginas públicas
  └─ Otras URLs → intentar extraer descripción

Paso 3: Unificar resultados + deduplicar
  └─ Lista consolidada de empleos únicos

Paso 4: Agente 2 analiza y selecciona el mejor match
```
