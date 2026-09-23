# AI Engineer IA Generativa — BCTecnología

**Portal:** Computrabajo Chile
**URL:** https://cl.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-ai-engineer-ia-generativa-en-santiago-las-condes-E7D9F254911F55C361373E686DCF3405
**Ubicación:** Santiago - Las Condes, R.Metropolitana (100% remoto según header; el cuerpo del aviso menciona "modalidad híbrida" para el proyecto bancario del cliente)
**Renta:** $3.100.000 CLP mensual, contrato a plazo fijo, 44 hrs/semana

## Descripción

Diseñar, desarrollar e integrar soluciones de IA Generativa, LLMs y Machine Learning (asistentes virtuales, NLP, análisis predictivo) para cliente bancario. Requiere: IA Generativa/LLMs, arquitecturas RAG y sistemas de agentes, Python, LangChain/LlamaIndex/Hugging Face, bases de datos vectoriales (Pinecone/ChromaDB/Milvus/PGVector/Azure AI Search), Azure OpenAI/AWS Bedrock/Vertex AI, APIs con FastAPI/Flask, Docker, LLMOps/MLOps, prompt engineering. 2-3 años de experiencia.

## Por qué encaja (con proyecto propio como evidencia)

Proyecto personal público de RAG en producción, evidencia directa del stack pedido salvo el lenguaje:

- **Repo:** https://github.com/goviedodev/ley-datos-personales
- **Demo en vivo:** https://datos-personales.limachelocales.cl/
- Stack real: Java 21 + Spring Boot 4.1.1 + **Spring AI 2.0.1** (el equivalente a LangChain en el ecosistema Java, no LangChain4j) + PostgreSQL con **pgvector** + Ollama (qwen3.5:4b para generación, nomic-embed-text para embeddings de 768 dimensiones).
- Cubre el ciclo RAG completo pedido en el aviso: ingesta y limpieza de PDF, chunking (400 tokens vía TokenTextSplitter), vectorización, búsqueda por similitud coseno (top-8), inyección de contexto en el prompt, respuesta con streaming token a token, memoria de conversación por sesión.
- Corre 100% local (Ollama + Docker), sin dependencias de servicios externos — dominio real de la arquitectura, no solo consumo de APIs administradas.
- Python: nivel funcional/commodity, en aprendizaje constante — el patrón RAG y las decisiones de arquitectura (chunking, embeddings, retrieval, prompt injection) son las mismas independientemente del lenguaje; el proyecto demuestra el razonamiento, no una traducción literal de sintaxis.
- Generación de código asistida por IA: uso principal de Claude Code como herramienta de generación, apoyado en harnesses propios (axi — https://github.com/kunchenguid/axi —, openspec, estructura de carpetas al estilo Jake Van Cliff) aplicando ingeniería real en los procesos para asegurar calidad.

**Estado:** Postulación directa (un clic en "Postularme", sin killer questions).
