# Documentación del Proyecto CV LaTeX

## Uso del Makefile

### Compilar PDF

```bash
# Español (por defecto)
make pdf

# Inglés
make pdf LANG=en
```

### Limpiar archivos auxiliares

```bash
# Limpiar archivos del CV en español
make clean

# Limpiar archivos del CV en inglés
make clean LANG=en
```

## Archivos

- `cv.tex` - CV en español
- `cv-en.tex` - CV en inglés
- `cv.pdf` - PDF compilado en español
- `cv-en.pdf` - PDF compilado en inglés

## Notas

- Docker debe estar instalado y ejecutándose
- Se usa la imagen TeXLive para compilación