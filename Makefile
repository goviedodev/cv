# Configuración
DOCKER_IMAGE = texlive/texlive
FILENAME = cv
CURRENT_DIR = $(shell pwd)
USER_ID = $(shell id -u)
GROUP_ID = $(shell id -g)
#
# Comando base de Docker
DOCKER_CMD = docker run --rm -v "$(CURRENT_DIR):/workdir" -u $(USER_ID):$(GROUP_ID) $(DOCKER_IMAGE)

all: pdf

# Compila el PDF
pdf:
	$(DOCKER_CMD) pdflatex $(FILENAME).tex

	# Limpia los archivos auxiliares que genera LaTeX (log, aux, out)
clean:
	rm -f $(FILENAME).aux $(FILENAME).log $(FILENAME).out $(FILENAME).pdf

# Compilación continua (útil si estás editando mucho)
watch:
	while true; do make pdf; sleep 5; done

	.PHONY: all pdf clean watch
