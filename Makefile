# Configuración
DOCKER_IMAGE = texlive/texlive
CURRENT_DIR = $(shell pwd)
USER_ID = $(shell id -u)
GROUP_ID = $(shell id -g)

# Idioma: es (español) o en (inglés)
LANG ?= es

ifeq ($(LANG),en)
  FILENAME = cv-en
else
  FILENAME = cv
endif

DOCKER_CMD = docker run --rm -v "$(CURRENT_DIR):/workdir" -u $(USER_ID):$(GROUP_ID) $(DOCKER_IMAGE)

all: pdf

# Compila el PDF según el idioma
pdf:
	$(DOCKER_CMD) pdflatex $(FILENAME).tex

# Limpia archivos auxiliares
clean:
	rm -f $(FILENAME).aux $(FILENAME).log $(FILENAME).out $(FILENAME).pdf

.PHONY: all pdf clean
