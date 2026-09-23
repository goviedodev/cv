# Notas de decisiones — miReserva.tech (Co-Fundador)

**Fecha:** 2026-08-31 · **Portal:** LinkedIn (postulación manual) · **Job ID:** 4458854958

## Clasificación de la oferta

Perfil **A (Chile local)**, con una torsión importante: **no es un rol técnico de ejecución**, es un rol de **socio fundador** (estrategia, modelo de ingresos, comercial, producto, alianzas, financiación). El CV base (`cv.md`) está construido como perfil de arquitecto backend; para esta vacante hubo que **reordenar la narrativa completa** poniendo la experiencia emprendedora y comercial arriba y la técnica como diferenciador, no como eje.

## Excepción documentada a la Restricción global n.º 1 de `AGENTS.md`

`AGENTS.md` prohíbe usar "CTO" y "Co-founder" en todo CV generado. **El usuario autorizó explícitamente la excepción para esta postulación** (pregunta formulada y respondida el 2026-08-31: "Usar CTO y Co-fundador").

Justificación: la vacante **es** de Co-Fundador. Ocultar los títulos fundadores y sustituirlos por "Tech Lead" destruiría exactamente la evidencia que el aviso pide ("ganas de participar en entornos de startups, emprendimiento o creación de nuevos proyectos digitales"). La excepción **aplica solo a esta carpeta**; el resto del pipeline mantiene la restricción vigente.

Títulos usados:
- **Co-Fundador y CTO — Te Llevo App** (startup de movilidad, 2024 – Presente). En el CV base figura como "CTO & Co-founder | Startup de Movilidad"; aquí se nombra la empresa por indicación del usuario.
- **Dueño, Director y CTO — Seven IT SpA** (2016 – 2020). Consolida en una sola entrada las dos filas del CV base ("CTO | Seven IT SpA 2017–2020" y "Director y Desarrollador de Ficha Clínica | Hospital Cruz del Norte 2016–2017"), que corresponden al mismo emprendimiento y al mismo cliente.

## Mirroring aplicado (keywords exactas del aviso)

reservar y gestionar servicios · fáciles de usar, seguros y escalables · diseño centrado en la persona usuaria · estrategia del negocio · modelo de ingresos · posicionamiento en el mercado · diseño y validación del producto · priorización de funcionalidades · planificación de lanzamientos · captación de clientes · alianzas · objetivos medibles · transparencia, responsabilidad y colaboración · riesgos calculados · decisiones ágiles · propuesta de valor · negociar acuerdos · relaciones con clientes y partners · productos SaaS · arquitectura web · herramientas no-code

Densidad objetivo 2–3 apariciones por término clave, repartidas entre Resumen, Experiencia y Habilidades.

## Ángulos de encaje construidos (todos verificables)

| Requisito del aviso | Evidencia real usada |
|---|---|
| Entornos de startups / emprendimiento / creación de proyectos digitales | Dos empresas propias: Seven IT SpA (constituida, con personal contratado) y Te Llevo App (co-fundada) |
| Riesgos calculados y decisiones ágiles | Operación financiada con capital propio y facturación, sin rondas externas; adopción temprana de Elixir/Ash y agentes de IA |
| Habilidades comerciales, presentar propuesta de valor, negociar acuerdos | Venta y negociación directa del Sistema de Gestión en Salud con el Hospital Cruz del Norte (SQM), cliente corporativo, sostenida desde la venta hasta el soporte |
| Relaciones con clientes y partners | Relación con SQM durante todo el ciclo; áreas de negocio en banca (Santander/Isban, Citibank) y retail (Cencosud) |
| Modelo de ingresos | Integración de Transbank y Khipu en el flujo de reserva y checkout de Te Llevo App |
| Diseño y validación de producto, priorización, lanzamientos | Refinamiento de historias de usuario y priorización en Te Llevo App; lanzamiento del sitio de Nubox para Colombia |
| Diseño centrado en la persona usuaria | Directrices de UX/UI de la nueva generación de aplicaciones Nubox |
| Coordinar equipo, objetivos medibles, cultura de transparencia | Jefatura de 4 desarrolladores en Seven IT; estándares aplicados en Merge Requests y decisiones documentadas en Git en Te Llevo App |
| Valorable: SaaS, arquitectura web, no-code | Tres productos SaaS construidos (salud, facturación electrónica, movilidad); arquitectura web y de microservicios; harness propio de agentes de IA |
| Híbrido en Región Metropolitana | Declarada disponibilidad para modalidad híbrida en la RM, sin falsear domicilio (reside en Limache) |

## Gaps declarados (no se maquillaron)

1. **Búsqueda de inversión y financiación:** el aviso lo pide ("cuando sea necesario"). Gonzalo **no ha levantado rondas externas**. En vez de inventarlo, el CV afirma el hecho verificable —financiamiento con capital propio y facturación— y el mensaje al reclutador lo declara de frente. Es una postura defendible en entrevista: sabe operar con presupuesto real y sin dilución.
2. **Representar a la empresa en eventos:** no hay evidencia de charlas o presencia en eventos en `cv.md`. No se afirmó. Lo más cercano y real que sí se usó es la comunicación con áreas de negocio no técnicas y con equipos multiculturales.
3. **Ubicación:** vive en Limache (Región de Valparaíso), no en Santiago. Se declara disponibilidad híbrida en la RM en lugar de fingir domicilio en Santiago (decisión ya establecida para este repositorio).
4. **Naturaleza del rol:** una vacante de "Co-Fundador" publicada como oferta laboral normalmente implica equity y poca o nula renta fija inicial. **Conviene aclarar compensación y participación societaria antes de invertir tiempo**, especialmente frente a la expectativa de renta habitual del usuario.

## Verificabilidad (Restricción global n.º 3)

Sin cifras de la lista negra. Las únicas cifras usadas son verificables y ya establecidas en el repositorio: más de 15 años de experiencia, 4 desarrolladores a cargo, 17 años en el sector financiero, y la migración Sybase → Oracle en Citibank. No se usaron porcentajes de mejora ni adjetivos sin evidencia; el bloque **Competencias** lleva cada término con su evidencia entre paréntesis (Restricción n.º 8).

## Formato (Restricción global n.º 5)

Usuario consultado el 2026-08-31; respuesta: **ambas versiones**.

- `cv_gonzalo_mireserva_cofundador.md` / `.pdf` — **ATS-safe**, Markdown lineal, sin LaTeX. **3 páginas**: `m2pdf` fuerza `geometry:margin=2cm` por línea de comandos, así que no se puede compactar sin LaTeX (prohibido en la versión ATS) ni sin recortar keywords. Para un parser la extensión es indiferente; es la versión para portales.
- `cv_gonzalo_mireserva_cofundador_harvard.md` / `.pdf` — **estilo Harvard**, **2 páginas**, para envío directo por correo o LinkedIn a un fundador. Se ajustó solo la capa de presentación (márgenes, interlineado, espaciado de secciones y viñetas) sin tocar el contenido redactado.
- Restricción n.º 9 (sin itálicas): las macros `\org` y `\stack` se redefinieron **sin `\textit`** respecto de la plantilla usada en `Alegra/` y `factor-it-2/`. La macro de producto se llama `\producto` y no `\prod` porque `\prod` ya existe en LaTeX.
- Restricción n.º 7 (orden de secciones): Habilidades va inmediatamente antes de Educación e Idiomas, y el bloque Competencias cierra esa última sección.

## Pendiente

Postulación **manual**: el CV queda generado, no enviado. Al enviarlo, actualizar el estado en `cv_job_links.md` a "Enviado" y registrar en `$HOME/proyectos/cv/proceso` con `./track add` (Restricción global n.º 6).
