---
name: harvard-cv-format
description: >-
  Aplica el estilo tipográfico Harvard (encabezado centrado, secciones en versalitas con regla horizontal, cargo a la izquierda + fechas alineadas a la derecha, viñetas compactas) al Markdown final de un CV de este proyecto, justo antes de exportarlo con m2pdf. Capa OPT-IN que requiere confirmación explícita del usuario en cada uso: el formato ATS-safe es el default del proyecto y gana ante silencio, ambigüedad o instrucción explícita de respetar la regla ATS. Úsala solo tras confirmación, cuando el usuario pida "estilo Harvard", "formato clásico/académico" o "mejora la maquetación del PDF".
allowed-tools: read, write, edit, bash
required-files: El Markdown del CV ya pulido por la Tarea 6 (`markdown_format_polisher`). Debe estar limpio y completo — esta skill maqueta, no redacta.
output-files: El mismo archivo Markdown con preámbulo LaTeX y estructura Harvard + el PDF generado con `/usr/local/bin/m2pdf`
---

# 🎓 Formato Harvard para CV

**Rol:** Editor tipográfico. Tomas un Markdown de CV ya redactado y auditado, y le aplicas la maqueta del template de CV de Harvard OCS sin tocar una sola palabra del contenido.

**Objetivo:** Un PDF de máximo 2 páginas, jerarquía visual clara y texto 100% extraíble por un ATS.

**Límite duro:** esta skill **no redacta, no resume, no inventa y no borra contenido**. Si para que quepa en 2 páginas hay que recortar texto, se detiene y le pregunta al usuario qué sacar. Solo puede ajustar márgenes, interlineado y espaciado.

## Cuándo entra en el pipeline

Después de la **Tarea 6** (`markdown_format_polisher`) y antes de la **Tarea 8** (`pdf_exporter`).

El orden importa: la Tarea 6 elimina artefactos LaTeX/pandoc del Markdown, y esta skill los reintroduce **a propósito y de forma controlada**. Si se ejecuta al revés, el pulidor borra el preámbulo. **Esta skill es siempre la última que toca el Markdown antes de `m2pdf`.**

## Paso 0 — Gate de confirmación (obligatorio, no se salta nunca)

**ATS manda. Esta skill no se auto-invoca jamás.** Antes de tocar un solo carácter del Markdown, resuelve en este orden:

| Situación | Acción |
|---|---|
| El usuario pidió explícitamente respetar la regla ATS | **Aborta.** No apliques el estilo y **no preguntes**. Informa que se exporta en formato ATS-safe. Solo se reactiva si el usuario pide después el estilo Harvard de forma explícita. |
| El usuario pidió explícitamente estilo Harvard | Continúa al Paso 1 sin volver a preguntar. |
| Cualquier otro caso (no dijo nada del formato, o el PDF se desbordó de 2 páginas) | **Pregunta y espera respuesta.** |

Formulación de la pregunta:

> ¿Genero el PDF en **formato ATS-safe** (default, máxima compatibilidad con parsers de portales) o con **estilo Harvard** (mejor legibilidad para un revisor humano; para envío directo por correo o entrega en mano)?

**Sin un "sí" explícito → ATS.** El silencio, una respuesta ambigua o tu propio criterio estético no autorizan el estilo Harvard. Que el CV se vea mejor **no** es razón suficiente: el usuario es quien sabe si el documento va a un portal con parser o a la bandeja de un reclutador.

Criterio para recomendar (si el usuario pide tu opinión): portal de empleo con formulario de carga → ATS; correo directo a un reclutador, referido interno o entrega en mano → Harvard.

## Relación con la regla ATS

`.pi/skills/ats-cv-optimizer/` exige Markdown lineal sin artefactos LaTeX, y esa regla tiene **precedencia** sobre esta skill (Restricción global n.º 5 de `AGENTS.md`). Cuando el usuario autoriza el estilo Harvard en el Paso 0, el preámbulo LaTeX y las tres macros se permiten **solo bajo estas dos condiciones**:

1. No se usan tablas, columnas ni text boxes como layout — el flujo del texto sigue siendo lineal y en orden de lectura.
2. Se verifica con `pdftotext` (Paso 5) que el texto sale extraíble y en el orden correcto.

Si la verificación del Paso 5 falla, se revierte el estilo y se exporta con el formato por defecto.

## Paso 1 — Verifica precondiciones

- **El Paso 0 se resolvió con autorización explícita del usuario.** Si no, no sigas.
- El Markdown existe, está pulido (Tarea 6) y contiene todo el contenido final.
- Haz copia de respaldo del PDF anterior si existe (el estilo se puede revertir, el PDF no).
- Si el archivo aún tiene `:::center`, `.unnumbered` u otros artefactos, **primero corre la Tarea 6**.

## Paso 2 — Inserta el preámbulo YAML

Al inicio del archivo, antes de cualquier contenido:

````markdown
---
lang: es
colorlinks: true
urlcolor: black
linkcolor: black
header-includes: |
  ```{=latex}
  \usepackage{titlesec}
  \usepackage{enumitem}
  \usepackage{fancyhdr}
  \geometry{top=1.4cm,bottom=1.6cm,left=1.8cm,right=1.8cm}
  \titleformat{\section}{\normalfont\large\scshape}{}{0em}{}[\vspace{-0.8em}\rule{\textwidth}{0.9pt}]
  \titlespacing*{\section}{0pt}{0.85em}{0.5em}
  \setlist[itemize]{leftmargin=1.1em,itemsep=1pt,topsep=2pt,parsep=0pt,label=\textbullet}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{0.35em}
  \linespread{1.0}
  \raggedbottom
  \newcommand{\rol}[2]{\textbf{#1}\hfill\textbf{#2}\par\vspace{-0.4em}}
  \newcommand{\org}[1]{\textit{#1}\par\vspace{-0.3em}}
  \newcommand{\stack}[1]{{\small\textit{Stack:} #1}\par\vspace{-0.2em}}
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\small NOMBRE COMPLETO\quad\textbar\quad Página \thepage}
  ```
---
````

**Obligatorio:** el bloque `header-includes` va envuelto en una valla ` ```{=latex} `. Sin ella, pandoc interpreta el LaTeX como Markdown y se come los corchetes de `\titleformat{...}[...]` (el `\rule` desaparece y el documento falla con `Missing \begin{document}`).

Para CV en inglés, cambia `lang: es` por `lang: en`.

## Paso 3 — Reestructura el encabezado y las entradas

**Encabezado** (reemplaza el `# Nombre` + lista de contacto con viñetas):

```markdown
\begin{center}
{\Huge\bfseries Nombre Apellido}\\[4pt]
{\large Título Profesional · Segundo Título}\\[6pt]
{\small Ciudad, País · +56 9 XXXX XXXX · correo@dominio.com}\\[2pt]
{\small linkedin.com/in/usuario · Inglés Intermedio B1}
\end{center}
\vspace{0.4em}
```

**Secciones:** un solo nivel, `#` (→ `\section`, versalitas + regla). No usar `##` para secciones principales.

**Entradas de experiencia:** tres líneas de macros + línea en blanco + viñetas.

```markdown
\rol{Cargo del Puesto}{2024 – Presente}
\org{Empresa — Ubicación}
\stack{Java 21 (Spring Boot), PostgreSQL, Docker, GCP.}

- **Logro con etiqueta en negrita:** descripción del impacto.
- **Segundo logro:** descripción del impacto.
```

Reglas de las macros:
- `&` dentro de `\rol{}`, `\org{}` o `\stack{}` se escribe `\&`.
- Los links Markdown `[texto](url)` **no funcionan dentro** de las macros. Van solo en las viñetas.
- La línea en blanco antes de la primera viñeta es obligatoria: sin ella pandoc fusiona la lista con el párrafo anterior y el PDF sale como un muro de texto con guiones.
- Educación e Idiomas se pueden fusionar en una sección para ganar espacio.

## Paso 4 — Genera el PDF

```bash
/usr/local/bin/m2pdf <archivo.md>
```

Único conversor autorizado (Restricción global n.º 4 de `AGENTS.md`).

**Comportamiento esperado, no es un error:** el primer intento de `m2pdf` siempre falla con `The font "FreeSerif" cannot be found` porque esa fuente no está en la imagen `pandoc/extra`. El script reintenta automáticamente en "configuración de emergencia" y ese segundo intento es el que produce el PDF (tipografía Computer Modern, que es justamente la del look académico). Solo hay que preocuparse si **también** falla el reintento.

Limpia `missfont.log` y `texput.log` si quedaron en el directorio.

## Paso 5 — Verificación obligatoria

```bash
pdfinfo <archivo>.pdf | grep Pages          # debe ser ≤ 2
pdftotext <archivo>.pdf - | head -40        # texto lineal y en orden
```

Checklist antes de entregar:

- [ ] Máximo 2 páginas, sin una página final casi vacía.
- [ ] `pdftotext` devuelve el texto completo, en orden de lectura, sin caracteres perdidos.
- [ ] Fechas alineadas a la derecha en la misma línea del cargo.
- [ ] Ninguna viñeta quedó convertida en párrafo con guiones.
- [ ] Ningún contenido desapareció respecto del Markdown de entrada.

**Si sobra media página o menos**, ajusta en este orden hasta que quepa: `\parskip` (0.35em → 0.3em) → `titlespacing` before (0.85em → 0.7em) → `geometry` márgenes laterales (1.8cm → 1.7cm). **Nunca** bajes el tamaño de fuente base ni recortes contenido por tu cuenta.

## Implementación de referencia

`generico/cv_gonzalo_oviedo.md` — CV en español, 2 páginas, con este estilo aplicado de punta a punta.
