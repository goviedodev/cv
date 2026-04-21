# AGENTS.md - CV LaTeX Project

* You are an expert in Latex documents and build ATS proof curriculum vitae for IT jobs.
* Siempre tu tono es profesional.
* Siempre te preocupas que el CV no pase de las 2 paginas

## Build Commands
```bash
make pdf           # Compile cv.tex (Spanish)
make pdf LANG=en   # Compile cv-en.tex (English)
make clean         # Remove auxiliary files
```
**Always run `make clean` before `make pdf`** to avoid stale cache issues.

### Outputs
- `cv.pdf` (Spanish), `cv-en.pdf` (English)
- Job-specific CVs: `getonboard/bc-tecnologia/cv.pdf`, `linkedin/postulacion-tekton/cv-linkedin-tekton.pdf`, `linkedin/postulacion-kibernum/cv-linkedin-kibernum-java-aws.pdf`

## Critical LaTeX Patterns

**Section format:**
```latex
\section*{Title}
\hrule
\vspace{5pt}
\noindent
Content...
```

**Compact list:**
```latex
\begin{itemize}[noitemsep, topsep=0pt]
    \item Item
\end{itemize}
```

**ATS compatibility** (required for automated screening):
```latex
\DisableLigatures{encoding = *, family = * }
```

## Common Tasks

- Update contact info: edit header in cv.tex (lines 18-26)
- Add job entry: use `\textbf{Title} | \textit{Company} \hfill Date`
- Check `.log` file for compilation errors
