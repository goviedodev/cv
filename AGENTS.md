# AGENTS.md - CV LaTeX Project

This repository contains my personal Curriculum Vitae built with LaTeX.

## Build Commands

### Prerequisites
- Docker must be installed and running
- TeXLive image is used for compilation

### Main Commands
```bash
# Compile PDF from cv.tex
make pdf

# Clean auxiliary files (log, aux, out)
make clean

# Watch mode - continuously compile every 5 seconds
make watch

# Manual Docker compilation
docker run --rm -v "$(pwd):/workdir" -u $(id -u):$(id -g) texlive/texlive pdflatex cv.tex
```

### Output
- Main PDF: `cv.pdf`
- Additional CVs in subdirectories:
  - `getonboard/bc-tecnologia/cv.pdf`
  - `linkedin/postulacion-tekton/cv-linkedin-tekton.pdf`
  - `linkedin/postulacion-kibernum/cv-linkedin-kibernum-java-aws.pdf`

## Code Style Guidelines

### LaTeX Formatting

**File Structure**
- Single main file (`cv.tex`) that can include other `.tex` files via `\input{}`
- Keep sections logically organized with clear comments using `%`

**Formatting Conventions**
- Use 2 spaces for indentation in code blocks
- Wrap lines at ~80 characters for readability
- Use `\vspace{...}` for vertical spacing (e.g., `\vspace{8pt}`)
- Use `\begin{itemize}[noitemsep, topsep=0pt]` for compact lists

**Packages and Imports**
- Standard packages: `inputenc`, `fontenc`, `geometry`, `hyperref`, `enumitem`, `microtype`
- Use `helvet` package with `\familydefault{\sfdefault}` for sans-serif font
- Disable ligatures with `\DisableLigatures{encoding = *, family = * }` for ATS compatibility

**Section Conventions**
```latex
\section*{Section Title}
\hrule
\vspace{5pt}
\noindent
Content here...
```

**List Environments**
```latex
\begin{itemize}[noitemsep, topsep=0pt]
    \item Item content
\end{itemize}
```

**Links and Contact Info**
- Use `\href{URL}{display text}` for hyperlinks
- Use `\hrefmailto{goviedo.sevenit@gmail.com}{email}` format

### Naming Conventions
- Filenames: lowercase with hyphens (e.g., `cv.tex`, `carta-presentacion.pdf`)
- Variable names in LaTeX: descriptive but concise

### Error Handling
- Check `.log` file for compilation errors
- Common issues: missing packages, character encoding problems, undefined references
- Use `make clean` to remove stale auxiliary files before recompiling

### Best Practices

1. **ATS-Friendly PDF**: Keep formatting simple, avoid complex tables, use standard fonts
2. **Encoding**: Always use UTF-8 with `\usepackage[utf8]{inputenc}`
3. **Page Layout**: Use `geometry` package with consistent margins (1.5cm default)
4. **Hyperlinks**: Use `hyperref` package with `hidelinks` option if needed
5. **Version Control**: Commit changes to `.tex` files, not compiled PDFs

### Directory Structure
```
/home/goviedo/proyectos/cv/
├── cv.tex                 # Main CV
├── cv.pdf                 # Compiled PDF
├── Makefile               # Build automation
├── README.md              # Project info
├── getonboard/            # Job application CVs
│   └── bc-tecnologia/
├── linkedin/              # LinkedIn application CVs
│   ├── postulacion-tekton/
│   └── postulacion-kibernum/
└── cartas-presentacion/   # Cover letters
```

### Common Tasks

**Adding New Section**
```latex
\section*{New Section Title}
\hrule
\vspace{5pt}
\noindent
Your content here...
```

**Updating Contact Info**
- Edit lines in the header section (around lines 18-26)
- Update both email and phone

**Adding New Job Entry**
```latex
\textbf{Job Title} | \textit{Company} \hfill Date Range \\
\begin{itemize}[noitemsep, topsep=0pt]
    \item Achievement or responsibility
\end{itemize}
```

### Notes for AI Agents
- This is a simple LaTeX project, not a software codebase
- No tests exist - verify output by opening the PDF
- Always run `make clean` before `make pdf` to avoid stale cache issues
- When editing, prefer making small incremental changes and compiling to verify
