# 🚀 cv-with-pidev-crewai-structure

**La Base Definitiva para la Búsqueda de Empleo Automatizada con Inteligencia Artificial**

Este repositorio no es simplemente una colección de currículums y cartas de presentación. **`cv-with-pidev-crewai-structure`** ha sido diseñado como la **base definitiva y el *framework* central de búsqueda de trabajo**, operando bajo una arquitectura de agentes autónomos orquestados mediante **Pi.dev** e inspirados en la estructura de **CrewAI**.

Aquí, la búsqueda de empleo deja de ser un proceso manual y repetitivo para convertirse en un **pipeline de ingeniería de software automatizado**.

---

## 🎯 ¿Por qué es la Base Definitiva?

El enfoque tradicional de postular a empleos es ineficiente. Este repositorio transforma esa dinámica mediante la implementación de un flujo de trabajo "Agentic AI":

1. **Búsqueda Multi-Portal Concurrente:** Rastreos automatizados en plataformas como LinkedIn, GetOnBoard, Computrabajo, Indeed, entre otros, buscando oportunidades de alto valor (remoto, en dólares, perfiles senior).
2. **Análisis y Matching Inteligente:** Los agentes evalúan las vacantes, descartan las que no sirven y seleccionan aquellas que hacen un "perfect match" con el stack tecnológico (Java, Spring Boot, Google Cloud, Agentic AI).
3. **Personalización Estratégica (Sin Alucinaciones):** A partir del archivo maestro `cv.md` (el *Source of Truth*), el sistema genera dinámicamente un nuevo CV adaptado a las palabras clave exactas de la vacante, resaltando la experiencia relevante sin inventar datos.
4. **Trazabilidad Absoluta:** Cada postulación queda registrada de forma automática en una base de datos Markdown (`cv_job_links.md`).

---

## 👥 Arquitectura de Agentes (El Pipeline)

El flujo se divide en 4 roles o "agentes" principales:

* 🕵️‍♂️ **`multi_portal_scraper`:** Extrae listados de empleos en tiempo real, esquivando muros de login y consolidando datos de múltiples fuentes.
* 📊 **`job_analysis_reporter`:** Analiza las descripciones de cargo (JDs) y genera reportes ejecutivos evaluando por qué una vacante es ideal.
* ✍️ **`resume_skills_customizer`:** Toma el CV original y lo reescribe arquitectónicamente para pasar los filtros ATS de la empresa destino.
* 🗂️ **`cv_job_linkage_tracker`:** Mantiene el log central de postulaciones para evitar duplicados y llevar un registro de estados.

---

## 📁 Estructura del Repositorio

El entorno se organiza dinámicamente a medida que se ejecutan las búsquedas:

```text
📦 cv-with-pidev-crewai-structure
 ┣ 📜 cv.md                   # Source of Truth: El currículum maestro original.
 ┣ 📜 cv_job_links.md         # Registro automatizado de todas las postulaciones.
 ┣ 📜 AGENTS.md               # Definición de la arquitectura de agentes (CrewAI style).
 ┣ 📜 PORTALS.md              # Estrategias de scraping por portal.
 ┣ 📜 README.md               # Este archivo.
 ┣ 📂 .pi/                    # Skills, configuraciones y herramientas de Pi.dev.
 ┣ 📂 khipu/                  # Ejemplo de vacante generada: Contiene CV (.md y .pdf) + Cover Letter
 ┣ 📂 2brains/                # Ejemplo de vacante generada
 ┗ 📂 tecla_peru/             # Ejemplo de vacante generada
```

---

## 🛠️ Stack Tecnológico Integrado

* **Pi.dev (Agentic AI Harness):** Motor principal de ejecución y orquestación de LLMs.
* **CrewAI Concepts:** División del trabajo en roles, objetivos y herramientas específicas.
* **Python / Playwright / BeautifulSoup:** Scraping avanzado y extracción de datos en la web.
* **Bash & Node.js (`md-to-pdf`):** Para operaciones rápidas de sistema y compilación automatizada de los CVs a formato PDF listos para enviar.
* **Markdown:** Como formato universal, ligero y versionable.

---

*« Deja que tus agentes busquen, analicen y adapten tu perfil mientras tú te preparas para brillar en la entrevista técnica. »*