# Búsqueda: ofertas TI en SQM (Soquimich)

> Verificado el **2026-07-23** contra el portal oficial `www.trabajaensqm.com` (consulta directa a su
> API de búsqueda: 24 ofertas vivas en total) y contra LinkedIn (vista pública + API guest).
> Ambos links de oferta respondieron HTTP 200 ese día.

## ⚠️ Hallazgo clave sobre LinkedIn

**SQM NO publica sus vacantes TI en LinkedIn.** En LinkedIn solo aparecen 2 avisos de SQM
(Planificador/a de Mantención y Jefe/a de Proyecto — ninguno informático), y las propias
descripciones de SQM advierten textualmente:

> *"Por favor, realiza tu postulación únicamente a través de nuestro sitio oficial
> www.trabajaenSQM.com. Solo las postulaciones recibidas directamente por ese medio serán
> consideradas."*

Es decir: aunque una oferta apareciera en LinkedIn, **la postulación válida es solo por el portal
oficial**. Los links de abajo son los correctos para postular.

## 💻 Ofertas TI vivas (2 de 24)

| # | Cargo | Ubicación | Contrato | Cierre | Link para postular |
|---|---|---|---|---|---|
| 1 | **Data Engineer** ⏰ **CIERRA MAÑANA 24/07** | Santiago (presencial) | Plazo indefinido | 24/07/2026 | https://www.trabajaensqm.com/5200-Data-Engineer |
| 2 | **Ingeniero/a Sistemas CIO** (Centro Integrado de Operaciones) | Nueva Victoria, Pozo Almonte (Iquique) | Plazo indefinido | 15/08/2026 | https://www.trabajaensqm.com/5222-Ingeniero-a-Sistemas-CIO-Nueva-Victoria---SQM-Yodo-Nutrici-n-Vegetal |

### 1. Data Engineer — Santiago
- **Stack:** Databricks, Azure SQL, Azure Data Factory, Azure DevOps, Lakehouse en la nube, modelamiento de Data Warehouses, visualización de datos.
- **Requisitos:** Título Ing. Civil/Ejecución en Informática, Civil Industrial o afín. Desde 1 año de experiencia como Data Engineer / BI Specialist / BI Analyst. **Inglés intermedio (B1 sirve)**.
- **Condiciones:** presencial en Santiago, L–J 8:30–18:30 y V 8:30–14:00, contrato indefinido.
- **⏰ Publicada el 24/06, se desactiva el 24/07/2026** — postular HOY si interesa.

### 2. Ingeniero/a Sistemas CIO — Nueva Victoria (Iquique)
- **Rol:** administrar servidores y plataformas tecnológicas del Centro Integrado de Operaciones: disponibilidad, integridad y seguridad de sistemas de supervisión/control, gestión de vulnerabilidades e incidentes, bases de datos, continuidad operacional (perfil TI/OT industrial).
- **Condiciones:** faena en Nueva Victoria (Pozo Almonte, Iquique), contrato indefinido, publicación interna/externa.
- **Cierre: 15/08/2026.**

## Referencias LinkedIn (contexto, no para postular)

- Página de empresa: https://www.linkedin.com/company/sqm/jobs (requiere sesión)
- Únicos avisos SQM vivos en LinkedIn al 23/07 (no TI):
  - Planificador/a de Mantención — https://cl.linkedin.com/jobs/view/planificador-a-de-mantenci%C3%B3n-at-sqm-4439307458
  - Jefe/a Proyecto (SQM Comercial, CAPEX obras civiles) — https://cl.linkedin.com/jobs/view/jefe-a-proyecto-at-sqm-4444208024

## Notas de la revisión completa (24 ofertas)

Las otras 22 vacantes son de operaciones/minería/química/legal/RRHH (supervisores de puerto,
electromecánicos, geólogos, prácticas, abogado, etc.) — ninguna adicional con componente
informático. Roles como "Planificador de Operaciones" o "Analista IMA" solo piden SAP/Power BI
como herramienta de usuario, no son cargos TI.

**Cómo re-verificar en el futuro:** el portal expone su buscador en
`POST https://www.trabajaensqm.com/app/minisite/site/_search` (Elasticsearch);
con `{"size":50,"sort":[{"created_at":"desc"}]}` se obtienen todas las ofertas vivas de una vez.
