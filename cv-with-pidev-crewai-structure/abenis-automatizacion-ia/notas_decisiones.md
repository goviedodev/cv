# Notas de decisión — Abenis, Ingeniero/a de Automatización de Procesos con IA

**Fecha:** 2026-09-10 · **Carpeta:** `abenis-automatizacion-ia/` (el nombre pedido `abenis/` ya estaba tomado por la postulación de mayo 2026 a Analista Programador, y `abenis-consultores/` por la de Backend Cloud de agosto 2026).

## Clasificación

**Perfil A — Chile local (CLP), empresa chilena, híbrido Santiago Centro, contrato indefinido directo con cliente.** Excepción al perfil A: aquí la IA generativa es el titular del CV, no el último bullet, porque el aviso es explícitamente de IA y pide "Experiencia con Claude/Anthropic".

## Formato

- Dos versiones: ATS-safe (`cv_gonzalo_abenis_automatizacion_ia.md`, default) y Harvard (`cv_gonzalo_abenis_automatizacion_ia_harvard.md`, pedida explícitamente por Gonzalo el 2026-09-10). Ambas de 2 páginas, mismo contenido. Usar ATS en portales con parser; Harvard para correo directo o entrega en mano.
- Sin itálicas. Sin override de fuente: el contenedor `pandoc/extra` no tiene Tahoma, Calibri ni Times New Roman (verificado con fc-list), igual que en todos los CV previos del repo.
- Dirección: "Actual: Limache · Reubicación: disponible para modalidad híbrida en Santiago" (memoria `direccion-cv-limache-vs-santiago`).

## Keywords espejadas (ortografía exacta del aviso)

Ingeniero de Automatización de Procesos con IA · Inteligencia Artificial Generativa · LLM · Claude/Anthropic · integración de APIs de modelos de IA · diseño de prompts · orquestación de flujos · agentes de IA · Function Calling · MCP · As-Is · oportunidades de automatización · clientes y stakeholders · audiencias técnicas y no técnicas · Inglés técnico intermedio-avanzado · Python · JavaScript/Node.js · soluciones tecnológicas.

## Requisito → evidencia usada

| Requisito | Evidencia (fuente verificada) |
|---|---|
| 2+ años desarrollo/automatización | 15+ años (cv.md) |
| Experiencia con Claude/Anthropic | Claude Code plan Max diario desde 2024, skills/comandos/workflows/MCP propios (cv.md, alegra/) |
| IA Generativa y LLM práctica | RAG Spring AI + pgvector + Ollama en producción (memoria `proyecto-rag-ley-datos-personales`); Jido.AI en farma.limachelocales.cl (alegra/carta) |
| Integración APIs de modelos + prompts | Spring AI/Ollama, Jido.AI; prompts con inyección de contexto; skills versionadas |
| Orquestación de flujos/agentes | Workflows Claude Code + openspec; agentes Jido.AI |
| Python o JavaScript/Node.js | JavaScript/TypeScript real (React, Vue, Cloudflare Workers); Python funcional en estudio (memoria `python-como-commodity-adaptable`) |
| Comunicación con clientes / no técnicos | Seven IT (dirección hospital, personal clínico), farmacia y zapatería locales, Santander 5 países |
| Inglés técnico intermedio-avanzado | B2, uso diario 2021–2023 (memoria `datos-para-formularios-postulacion`) |
| Function Calling y MCP | Servidores MCP propios en Claude Code = tool use. No se afirma uso de la Messages API de Anthropic en producto de cliente (no verificable) — declarado abiertamente en la carta |

## Gaps declarados (no ocultados)

- Sin integración directa de la API de Anthropic en un producto de cliente; el trabajo con Anthropic es vía Claude Code/MCP.
- Python a nivel funcional, no avanzado.
- Node.js: experiencia vía Cloudflare Workers, no servidores Node tradicionales.

## Verificación (cv-tailor Paso 4)

- [x] Cero cifras de la lista negra (sin "300%", sin "99.98%"; se conserva 15M registros Citibank, permitido).
- [x] Sin "CTO"/"Co-founder": se usa "Tech Lead y Arquitecto".
- [x] Título del CV = título del aviso.
- [x] Keywords críticas ≥ 2 veces: Claude/Anthropic, IA Generativa, LLM, MCP, Function Calling, As-Is, agentes de IA, diseño de prompts.
- [x] Ninguna tecnología no usada. Salcobrand 2023–2024 respaldado por respuestas del usuario en `gft_technologies/respuestas_whatsapp.md` y `agtec_servicios/qa_agtec.md`.
- [x] Habilidades Técnicas antes de Educación e Idiomas; bloque Competencias con evidencia entre paréntesis.

## Condiciones declaradas en la carta

Híbrido Santiago Centro OK · disponibilidad inmediata · pretensión $2.500.000 líquidos (memoria `datos-para-formularios-postulacion`).

## Envío

**Enviada el 2026-09-10** (confirmado por Gonzalo). Registrada en `../proceso/track` con id `2026-09-10-abenis-ingeniero-de-automatizacion-de-procesos-con-ia`. Contexto original: el aviso llegó sin URL ni canal. Opciones: (1) responder en la publicación de LinkedIn de Abenis donde apareció el texto, (2) correo a fescalona@abenis.cl, contacto usado en agosto 2026 (`abenis-consultores/EMAIL_A_ENVIAR.txt`). Borradores en `mensaje_reclutador.md`. `cv_job_links.md` ya en estado Enviada.
