# Graph Report - .  (2026-08-10)

## Corpus Check
- 361 files · ~282,834 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 962 nodes · 1149 edges · 69 communities (53 shown, 16 thin omitted)
- Extraction: 61% EXTRACTED · 38% INFERRED · 2% AMBIGUOUS · INFERRED: 433 edges (avg confidence: 0.89)
- Token cost: 2,463,215 input · 0 output

## Community Hubs (Navigation)
- Auditoría Anti-IA del CV
- Postulación Equifax InterConnect
- Postulación AGtec Backend
- CV Base Manual
- Postulación Stord Elixir
- Posicionamiento IA Agéntica
- Postulación Prima Madrid
- Informes de Análisis de Vacantes
- Automatización Computrabajo
- CVs Backend Multi-Empresa
- Postulación Coderslab Java
- CVs Java Full Stack
- Postulaciones J2EE y Codelco
- Postulación Remote Leverage
- Postulación 2Brains
- Analista Programador Computrabajo
- CVs Telnyx y Tecnología y Personas
- Postulaciones BCTecnología
- Postulación X-Team Platform
- Scraping de Ofertas Computrabajo
- Postulaciones Kibernum y Knowmad
- Vacantes Elixir Remotas
- Agentes de CV y Verificabilidad
- Postulación GFT Technologies
- Informes de Búsqueda Java
- Configuración de Modelos en pi
- Portales y Reglas de Método
- Script filter.js
- Pipeline de Agentes Legacy
- Exportación PDF y Pandoc
- Vías Legales para Trabajar en España
- Postulación FullStack Kotlin/React
- Búsqueda Java en Alemania
- Selección de Vacantes IA + Frontend
- Postulación GetData PL/SQL
- Estrategia Nicho Elixir España
- Postulación ITPS Arquitectura Hexagonal
- Script parse_job.js
- Baseline y Falsos Negativos
- Script apply_start.sh
- Script check_applied.sh
- Script cover.sh
- Script fill.sh
- Script kq_dump.sh
- Script kq_submit.sh
- Script read_all.sh
- Script read_offer.sh
- Script scrape_baseline.sh
- Script scrape_offers.sh
- Inglés B1 y Marketplaces
- CV Maestro en Inglés
- Script extract_job.js
- Documentación del Framework
- Script get_puppeteer.js
- Script get_pw.js
- Inglés B1 en X-Team
- Parsewave Freelance Elixir
- Tech Lead Seven IT

## God Nodes (most connected - your core abstractions)
1. `cv_job_links.md — registro de trazabilidad CV ↔ vacante (93 postulaciones)` - 12 edges
2. `CV — Gonzalo Oviedo Lambert, Equifax InterConnect (Java / Spring Boot)` - 11 edges
3. `Gonzalo Oviedo Lambert (Manual Base CV)` - 11 edges
4. `CV — Avos Tech (Senior Fullstack Engineer variant)` - 10 edges
5. `CV Gonzalo Oviedo — SoftServe Full Stack (React, Next.js, TypeScript, Python)` - 10 edges
6. `Computrabajo Job Hunter Skill` - 9 edges
7. `Preguntas y Respuestas — killer questions AGtec (Computrabajo)` - 9 edges
8. `CV tailored for FullStack — Agentic Elixir Engineer` - 9 edges
9. `CV Gonzalo Oviedo — Remote Leverage (English)` - 9 edges
10. `multi_portal_scraper (Agente 1)` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Agentic AI Skill/Command/Workflow Authoring with Pi.dev` --semantically_similar_to--> `AI-Native Development Differentiator (Pi.dev, Opencode, Hermes)`  [INFERRED] [semantically similar]
  companies/cv_gonzalo_2brains_fullstack_ia.pdf → coderslab/porque-interesado.md
- `Gonzalo Oviedo — Baseline Generic CV PDF` --semantically_similar_to--> `Arquitecto Full-Stack Senior Positioning (Generic ES)`  [AMBIGUOUS] [semantically similar]
  generico/cv_gonzalo_oviedo.pdf → generico/cv_gonzalo_generic_es.md
- `Rasgo dominante "Orientación a resultados" (personalidad laboral)` --conceptually_related_to--> `Regla de verificabilidad (Restricción global n.º 3)`  [INFERRED]
  Talentview3D.pdf → AGENTS.md
- `cv-en.md — CV maestro en inglés` --semantically_similar_to--> `cv.md — CV maestro en español (Source of Truth)`  [INFERRED] [semantically similar]
  cv-en.md → cv.md
- `Computrabajo Job Hunter Skill (pi copy)` --semantically_similar_to--> `Computrabajo Job Hunter Skill`  [INFERRED] [semantically similar]
  .pi/skills/job-hunter-computrabajo/SKILL.md → .claude/skills/job-hunter-computrabajo/SKILL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pipeline secuencial de 8 tareas del Multi-Portal Job Hunter** — agents_multi_portal_scraper, agents_job_analysis_reporter, agents_resume_skills_customizer, agents_ai_profile_enhancer, agents_anti_ai_cv_auditor, agents_markdown_format_polisher, agents_cv_job_linkage_tracker, agents_pdf_exporter [EXTRACTED 1.00]
- **Vías legales para trabajar con una empresa española desde Chile** — job_portals_contractor_b2b, job_portals_eor, job_portals_tarjeta_azul_ue, busqueda_espana_barrera_autorizacion_ue [EXTRACTED 1.00]
- **Ofertas Elixir abiertas a LATAM sin barrera de inglés declarada** — busqueda_global_elixir_x_team, busqueda_global_elixir_stord, busqueda_global_elixir_ryz_labs, busqueda_global_elixir_patient_reach_360, busqueda_global_elixir_subvisual, busqueda_global_elixir_parsewave [EXTRACTED 1.00]
- **Portal-Agnostic 'Applications List Is the Only Source of Truth' Pattern** — _claude_skills_job_hunter_computrabajo_skill_mis_postulaciones_source_of_truth, _claude_skills_job_hunter_trabajando_skill_mis_postulaciones_source_of_truth, _pi_skills_job_hunter_getonboard_skill_applications_source_of_truth, _pi_skills_job_hunter_getonboard_skill_apply_bottom_detector [INFERRED 0.85]
- **CV Quality Pipeline (tailor → ATS → anti-AI → m2pdf)** — _pi_skills_cv_tailor_skill_cv_tailor, _pi_skills_ats_cv_optimizer_skill_ats_cv_optimizer, _pi_skills_anti_ai_cv_auditor_skill_anti_ai_cv_auditor, _pi_skills_ats_cv_optimizer_skill_m2pdf_exclusive_converter, _pi_skills_job_hunter_linkedin_skill_resume_skills_customizer [EXTRACTED 1.00]
- **Routes to Use the Anthropic Subscription from pi** — _pi_plans_plan_como_anthropic_native_provider_plan, _pi_plans_plan_tengo_omniroute_claude_plan, _pi_plans_plan_tengo_ruta_a_openai_format, _pi_plans_plan_tengo_ruta_b_anthropic_messages, _pi_plans_plan_como_oauth_subscription_auth [EXTRACTED 1.00]
- **Equifax InterConnect Application Package (23people)** — 23people_equifax_interconnect_cover_letter_equifax_interconnect_cover_letter, 23people_equifax_interconnect_cv_gonzalo_equifax_interconnect_cv, 23people_equifax_interconnect_why_equifax_answer_answer, 23people_equifax_why_equifax_motivation, 23people_equifax_profile_980_senior_engineer_profile [INFERRED 0.85]
- **2Brains Full-Stack (Java + Angular + IA) Application Package** — 2brains_cover_letter_en_cover_letter, 2brains_cover_letter_es_carta_presentacion, 2brains_cv_gonzalo_2brains_cv, 2brains_cv_gonzalo_2brains_fullstack_ia_cv, 2brains_porque_interesado_motivacion [INFERRED 0.85]
- **AI Agent Harness Differentiator Narrative (across applications)** — 23people_equifax_profile_980_ai_agent_orchestration, 23people_equifax_interconnect_cover_letter_equifax_interconnect_ai_harness_3x_delivery, 23people_equifax_interconnect_cv_gonzalo_equifax_interconnect_ai_assisted_engineering_differentiator, 2brains_cover_letter_en_agentic_ai_pidev, 2brains_cv_gonzalo_2brains_fullstack_ia_skills_prompts_workflows [INFERRED 0.85]
- **Job Analysis Report Pattern (portal → requirement matrix → CV tailoring recommendation)** — 2brains_backend_senior_cf68_job_analysis_report_analysis, accessowl_job_analysis_report_analysis, acercarse_job_analysis_report_analysis [INFERRED 0.85]
- **Abenis Consultores Application Package (notes, letter, email, CV, PDF)** — abenis_consultores_abenis_decision_notes_decision_notes, abenis_consultores_carta_presentacion_letter, abenis_consultores_email_a_enviar_email, abenis_consultores_cv_gonzalo_abenis_consultores_cv, abenis_consultores_cv_gonzalo_abenis_consultores_pdf [EXTRACTED 1.00]
- **Seniority Title De-escalation Across Applications (CTO → Tech Lead)** — accessowl_job_analysis_report_avoid_cto_title, acercarse_job_analysis_report_title_downgrade_strategy, accessowl_cv_gonzalo_accessowl_cv, acercarse_cv_gonzalo_acercarse_cv [EXTRACTED 1.00]
- **Pipeline de autopostulación: scrape → filtro → dossier → lista final** — autopostulacion_computrabajo_tmp_all_uniq_ofertas_unicas, autopostulacion_computrabajo_tmp_cand2_candidatas, autopostulacion_computrabajo_tmp_dossier2_cuerpos_aviso, autopostulacion_computrabajo_tmp_apply_list_lista_postulacion, autopostulacion_computrabajo_tmp_apply_final_lista_postulacion [INFERRED 0.85]
- **Política de honestidad: declarar gaps y explicar lo transferible** — autopostulacion_computrabajo_estadisticas_gaps_declarados, autopostulacion_computrabajo_estadisticas_criterio_no_postular_stack_ajeno, autopostulacion_computrabajo_tmp_answers_gap_cloud_devops, agtec_servicios_qa_agtec_gap_aws, agtec_servicios_qa_agtec_gap_python, agtec_servicios_qa_agtec_gap_mongodb [INFERRED 0.85]
- **Paquete de postulación AGtec: CV + carta + killer questions + enlace de seguimiento** — agtec_servicios_cv_gonzalo_agtec_cv, agtec_servicios_cover_letter_agtec_cover_letter, agtec_servicios_qa_agtec_killer_questions, agtec_servicios_links_computrabajo_match_url, agtec_servicios_cv_gonzalo_agtec_pdf_render, agtec_servicios_cover_letter_agtec_pdf_render [EXTRACTED 1.00]
- **Computrabajo scrape → dedup → shortlist pipeline** — autopostulacion_computrabajo_tmp_offers_r6_round6_scrape, autopostulacion_computrabajo_tmp_offers_r6b_round6b_scrape, autopostulacion_computrabajo_tmp_offers_r6_uniq_round6_unique, autopostulacion_computrabajo_tmp_offers_dedup_offer_index, autopostulacion_computrabajo_tmp_queue_application_queue [INFERRED 0.85]
- **Avos Tech application packet (CV, letter, Q&A)** — avos_tech_cv_gonzalo_avos_tech_cv, avos_tech_cv_gonzalo_avos_tech_cv_pdf, avos_tech_cover_letter_avos_tech_carta_presentacion, avos_tech_respuesta_fullstack_corta_respuesta_corta, avos_tech_respuestas_preguntas_respuestas_postulacion [INFERRED 0.95]
- **Per-company tailored CV variants of one career history** — avos_tech_cv_gonzalo_avos_tech_cv, babel_cv_gonzalo_babel_health_cv, bc_tecnologia_cv_gonzalo_bc_tecnologia_cv [INFERRED 0.85]
- **Paquete de postulación BCTecnología Semi Senior (CV + carta + killer questions)** — bc_tecnologia_3_cv_gonzalo_bc_fullstack_semisenior_cv, bc_tecnologia_3_carta_presentacion_bc_fullstack_semisenior_cover_letter, bc_tecnologia_3_preguntas_formulario_killer_questions [INFERRED 0.95]
- **IA agéntica como valor diferencial transversal a todas las postulaciones** — bc_tecnologia_2_cv_gonzalo_bc_fullstack_cloud_pidev_agentic_ai, bc_tecnologia_3_cv_gonzalo_bc_fullstack_semisenior_ia_agentica_adaptacion, binexo_cv_gonzalo_binexo_orquestacion_agentes_harnesses, binexo_cv_gonzalo_binexo_ai_augmented_engineer [INFERRED 0.85]
- **Estrategia de declaración honesta de brechas con mitigación por IA** — bc_tecnologia_3_preguntas_formulario_gap_typescript_nestjs, bc_tecnologia_4_cover_letter_bc_tecnologia_4_declaracion_brechas, bc_tecnologia_3_cv_gonzalo_bc_fullstack_semisenior_ia_agentica_adaptacion [INFERRED 0.85]
- **Coderslab.io Application Package (vacancy analysis → tailored CV → motivation letters)** — coderslab_job_analysis_report_vacancy, coderslab_cv_gonzalo_coderslab_cv, coderslab_porque_interesado_motivation, coderslab_resumen_interes_summary, coderlabs_interes_trabajo_coderslab_letter [INFERRED 0.85]
- **Java/Spring Boot Cover Letter Template Family (shared structure: stack → evidence → why-company → English level)** — companies_cover_letter_bairesdev_letter, companies_cover_letter_miratech_letter, companies_cover_letter_technorex_letter, companies_cover_letter_whiteam_letter [INFERRED 0.85]
- **Fiserv Staff-Level CV Multi-Format Bundle (Markdown, plain-text ATS, PDF)** — companies_gonzalo_oviedo_fiserv_staff_java_software_engineer_cv, companies_gonzalo_oviedo_fiserv_staff_java_software_engineer_txt_variant, companies_gonzalo_oviedo_cv_pdf_render [INFERRED 0.95]
- **Shared career backbone reused verbatim across all CV variants (Citibank Sybase-to-Oracle migration, Perficient/Caterpillar e-commerce, Seven IT healthcare system, WebClass 1800 schools, UBB XP thesis)** — companies_cv_gonzalo_consorcio_cv, companies_cv_gonzalo_fortia_cv, companies_cv_gonzalo_gft_technologies_cv, companies_cv_gonzalo_miratech_cv, companies_cv_gonzalo_open_talent_fintech_cv, companies_cv_gonzalo_plaintech_solutions_cv, companies_cv_gonzalo_sii_germany_cv, companies_cv_gonzalo_technorex_cv, companies_cv_gonzalo_turtle_trax_cv, companies_cv_gonzalo_whiteam_cv [EXTRACTED 1.00]
- **Agentic AI positioning cluster: CV variants that lead with agent harnesses and LLM orchestration instead of plain Java backend** — companies_cv_gonzalo_fortia_cv, companies_cv_gonzalo_plaintech_solutions_cv, companies_cv_gonzalo_turtle_trax_cv, companies_cv_gonzalo_fortia_agent_execution_harness, companies_cv_gonzalo_plaintech_solutions_agentic_augmented_development, companies_cv_gonzalo_turtle_trax_agentic_workflow_quality_gate [INFERRED 0.85]
- **Production agent platform subsystems described in the Fortia CV (harness, MCP tooling, vector memory, anonymization, on-prem LLM infra)** — companies_cv_gonzalo_fortia_agent_execution_harness, companies_cv_gonzalo_fortia_mcp_custom_tooling, companies_cv_gonzalo_fortia_contextual_memory_vector_store, companies_cv_gonzalo_fortia_bidirectional_anonymization_layer, companies_cv_gonzalo_fortia_on_premise_llm_infrastructure [EXTRACTED 1.00]
- **Paquete de posicionamiento contractor (CV + carta + extracto)** — contractor_cv_gonzalo_contractor_es_cv, contractor_carta_contractor_es_carta, contractor_extracto_computrabajo_extracto, contractor_carta_contractor_es_sin_curva_de_onboarding, contractor_cv_gonzalo_contractor_es_disponibilidad_3_6_meses [EXTRACTED 1.00]
- **Diferenciador de IA agéntica reutilizado en todas las postulaciones** — computrabajo_analista_programador_cv_gonzalo_analista_programador_codificador_potenciado_por_ia, connect_antigravity_cv_gonzalo_connect_antigravity_ai_first_engineering_approach, connect_antigravity_cv_gonzalo_connect_antigravity_agent_harnesses, contractor_cv_gonzalo_contractor_es_claude_code_harness_principal [INFERRED 0.85]
- **Pipeline análisis de vacante → CV personalizado → PDF** — computrabajo_analista_programador_job_analysis_report_report, computrabajo_analista_programador_job_analysis_report_estrategia_personalizacion_cv, computrabajo_analista_programador_cv_gonzalo_analista_programador_cv, computrabajo_analista_programador_cv_gonzalo_analista_programador_pdf, connect_antigravity_informe_analisis_connect_antigravity_report, connect_antigravity_cv_gonzalo_connect_antigravity_cv, connect_antigravity_cv_gonzalo_connect_antigravity_pdf [INFERRED 0.85]
- **Agentic AI harness (Pi.dev / opencode / Claude Code) positioning reused across every CV variant** — cv_versions_cv2_en_agentic_ai_harness_practice, fistrek_cv_gonzalo_fistrek_ai_harness_differentiator, fullstack_cv_gonzalo_fullstack_ai_coder_judgment, fullstack_agentic_elixir_cv_gonzalo_fullstack_spec_plan_execute_verify_loop, fullstack_linkedin_post1_cv_gonzalo_fullstack_node_react_agentic_velocity_claim, fullstack_linkedin_post1_job_analysis_report_key_differentiator [INFERRED 0.85]
- **FullStack Agentic Elixir application bundle (job analysis → tailored CV → PDF → recruiter message → decision note)** — fullstack_agentic_elixir_job_analysis_report_role, fullstack_agentic_elixir_cv_gonzalo_fullstack_cv, fullstack_agentic_elixir_cv_gonzalo_fullstack_rendered_pdf, fullstack_agentic_elixir_linkedin_message_outreach, fullstack_agentic_elixir_linkedin_message_profile_c_decision, fullstack_agentic_elixir_job_analysis_report_declared_gaps [EXTRACTED 1.00]
- **Elixir/BEAM profile C evidence set (production systems backing every Elixir-targeted application)** — fcm_digital_cv_gonzalo_fcm_digital_elixir_otp_beam_specialization, fcm_digital_cv_gonzalo_fcm_digital_tellevoapp_production_systems, fullstack_agentic_elixir_cv_gonzalo_fullstack_ash_otp_domain_model, fullstack_agentic_elixir_cv_gonzalo_fullstack_farma_limachelocales [INFERRED 0.85]
- **Agentic AI harness positioning shared across all CV variants** — fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_agentic_ai_harnessing, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_es_ia_agentica, generico_cv_gonzalo_generic_en_agent_workflow_spec_plan_execute_verify, generico_cv_gonzalo_generic_es_agentic_ai_lead_developer, generico_cv_gonzalo_generico_ia_es_ai_assisted_engineering_differentiator [INFERRED 0.85]
- **Job-tailoring pipeline: analysis → reframing → EN/ES CV output** — fullstack_linkedin_post2_java_job_analysis_report_senior_java_fullstack_vacancy, fullstack_linkedin_post2_java_job_analysis_report_fit_analysis, fullstack_linkedin_post2_java_job_analysis_report_strategic_reframing, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_senior_java_fullstack_profile, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_es_senior_java_fullstack_profile [INFERRED 0.85]
- **Common career spine reused by every CV variant (Citibank, Caterpillar, Seven IT, WebClass, mobility startup)** — fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_mobility_startup_role, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_perficient_caterpillar_role, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_citibank_role, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_seven_it_role, fullstack_linkedin_post2_java_cv_gonzalo_fullstack_java_early_career_role [EXTRACTED 1.00]
- **Variantes del CV base reescritas por vacante objetivo** — historial_cv_cv, getdata_cv_gonzalo_getdata_java_springboot_cv, gft_technologies_cv_gonzalo_gft_technologies_cv, itps_cv_gonzalo_itps_cv [INFERRED 0.85]
- **Pipeline completo de postulación a GFT Technologies LATAM (CV, carta, portal, screening)** — gft_technologies_cv_gonzalo_gft_technologies_cv, gft_technologies_gft_carta_presentacion_carta, gft_technologies_portal_jobs_gft_com, gft_technologies_respuestas_whatsapp_respuestas [EXTRACTED 1.00]
- **Serie de informes de análisis de vacantes con scoring de compatibilidad y exclusión incremental** — job_analysis_reports_job_analysis_report_informe, job_analysis_reports_job_analysis_report_2_informe, job_analysis_reports_job_analysis_report_3_informe, job_analysis_reports_job_analysis_report_4_informe, job_analysis_reports_job_analysis_report_5_informe, job_analysis_reports_job_analysis_report_espana_informe, job_analysis_reports_informe_analisis_fullstack_informe [EXTRACTED 1.00]
- **Paquete de postulación a Khipu (informe + CV + cartas)** — job_analysis_reports_job_analysis_report_khipu_report, job_analysis_reports_job_analysis_report_khipu_khipu, khipu_cv_gonzalo_khipu_cv, khipu_cover_letter_es_letter, khipu_cover_letter_short_letter [EXTRACTED 1.00]
- **Paquete de postulación a Kibernum (CV + carta + FAQ de killer questions)** — kibernum_java_angular_qa_faq_kibernum_vacancy, kibernum_java_angular_cv_gonzalo_kibernum_cv, kibernum_java_angular_cover_letter_kibernum_letter, kibernum_java_angular_qa_faq_faq [EXTRACTED 1.00]
- **Pipeline de vacantes Java/Spring Boot senior remotas evaluadas por los informes** — job_analysis_reports_job_analysis_report_espana_2_metrica, job_analysis_reports_job_analysis_report_java_chile_recent_plaintech_solutions, job_analysis_reports_job_analysis_report_java_chile_recent_equifax_23people, job_analysis_reports_job_analysis_report_java_remoto_global_2026_07_27_turtle_trax, job_analysis_reports_job_analysis_report_khipu_khipu, job_analysis_reports_job_analysis_report_peru_usd_tecla [INFERRED 0.85]
- **Paquete de postulación Kibernum (análisis → CV → carta → PDF)** — kibernum_java_angular_2_job_analysis_report_vacancy, kibernum_java_angular_2_job_analysis_report_ats_strategy, kibernum_java_angular_2_cv_gonzalo_kibernum_cv, kibernum_java_angular_2_cover_letter_kibernum_cover_letter, kibernum_java_angular_2_cv_gonzalo_kibernum_pdf [EXTRACTED 1.00]
- **Paquete de postulación Lisit (vacante GetOnBoard → CV → carta → PDF)** — lisit_job_analysis_report_vacancy, lisit_job_analysis_report_match_score, lisit_cv_gonzalo_lisit_cv, lisit_cover_letter_lisit_cover_letter, lisit_cv_gonzalo_lisit_pdf [EXTRACTED 1.00]
- **Posicionamiento transversal como orquestador de harnesses de agentes (Pi.dev/opencode)** — lisit_cv_gonzalo_lisit_ai_coder_harness, knowmad_mood_cv_gonzalo_knowmad_mood_agent_lifecycle_design, knowmad_mood_cv_gonzalo_knowmad_mood_llm_cost_optimization, latam_chumi_cv_gonzalo_latam_chumi_active_orchestration, kibernum_java_angular_2_cv_gonzalo_kibernum_cv [INFERRED 0.85]
- **Hexagonal Architecture Narrative Across Michael Page Application Package** — michael_page_cv_gonzalo_michael_page_cv_michael_page, michael_page_cover_letter_michael_page_carta_seguros, michael_page_respuestas_preguntas_respuestas_postulacion, michael_page_respuestas_preguntas_arquitectura_hexagonal, michael_page_respuestas_preguntas_regla_de_dependencia [EXTRACTED 1.00]
- **AI-Augmented Coding as Cross-Application Differentiator (300% Speed Claim)** — manual_cv_agentic_ai_pidev, micro1_cv_gonzalo_micro1_ai_first_engineering_section, micro1_job_analysis_report_key_differentiator_ai_native, metrica_programador_cv_gonzalo_metrica_programador_cv_programador, michael_page_cv_gonzalo_michael_page_cv_michael_page [INFERRED 0.85]
- **Shared Career History Reused Across All Tailored CV Variants** — manual_cv_gonzalo_oviedo_lambert, metrica_espana_cv_gonzalo_metrica_cv_metrica, metrica_programador_cv_gonzalo_metrica_programador_cv_programador, michael_page_cv_gonzalo_michael_page_cv_michael_page, micro1_cv_gonzalo_micro1_cv_micro1 [INFERRED 0.95]
- **Seniority Title De-escalation Pattern (CTO/Co-founder → Tech Lead) across applications** — pasalc_spa_job_analysis_report_title_de_escalation, paperstreet_paperstreet_decision_notes_title_de_escalation, pasalc_spa_cv_gonzalo_pasalc_spa_cv, paperstreet_cv_gonzalo_paperstreet_cv, niuro_codelco_cv_gonzalo_niuro_codelco_cv [INFERRED 0.85]
- **Agentic AI Harness (Pi.dev / opencode / Claude Code) as cross-application differentiator** — multinacional_servicios_ti_cv_gonzalo_multinacional_ti_cv, niuro_codelco_cv_gonzalo_niuro_codelco_cv, paperstreet_cv_gonzalo_paperstreet_cv, pasalc_spa_cv_gonzalo_pasalc_spa_cv, patient_reach_360_elixir_cv_gonzalo_patient_reach_360_cv, pasalc_spa_job_analysis_report_agentic_ai_differentiator, patient_reach_360_elixir_cv_gonzalo_patient_reach_360_spec_plan_execute_verify [INFERRED 0.85]
- **Codelco ODS 65 application flow — job description, stack gaps, prototype, recruiter note, CV** — niuro_codelco_descripcion_laboral_niuro_senior_job_description, niuro_codelco_descripcion_laboral_niuro_senior_dve_estrategia_datos_fuente_unica, niuro_codelco_descripcion_laboral_niuro_senior_corporate_stack_requirement, niuro_codelco_nota_reclutadora_recruiter_note, niuro_codelco_nota_reclutadora_gap_closing_prototype, niuro_codelco_nota_reclutadora_honest_gap_disclosure, niuro_codelco_cv_gonzalo_niuro_codelco_cv [EXTRACTED 1.00]
- **Remote (Elixir) Application Package: analysis → CV → written responses** — remote_job_analysis_report_remote_elixir_role, remote_job_analysis_report_cv_customization_strategy, remote_cv_gonzalo_remote_en_cv_remote_en, remote_application_responses_application_responses [EXTRACTED 1.00]
- **Agentic AI Harness Narrative Reused Across Applications** — profile_achievements_agentic_ai_production, remote_cv_gonzalo_remote_en_agentic_harness_operator, remote_cv_gonzalo_remote_en_spec_plan_execute_verify, ps_grupo_automatizacion_ms_cover_letter_ps_grupo_automatizacion_ms_ai_augmentation, prima_cv_gonzalo_prima_cv_prima [INFERRED 0.85]
- **Canonical Profile Sources Feeding Tailored CVs** — profile_biography_biography_master, profile_achievements_achievements_master, prima_cv_gonzalo_prima_cv_prima, ps_grupo_automatizacion_ms_cv_gonzalo_ps_grupo_automatizacion_ms_cv_ps_grupo, remote_cv_gonzalo_remote_en_cv_remote_en [INFERRED 0.85]
- **SoftServe req. 88952 Application Package** — softserve_job_description_posting, softserve_cv_gonzalo_softserve_fullstack_nextjs_cv, softserve_cover_letter_cover_letter, softserve_letter_to_recruiter_letter, softserve_notes_gap_analysis_analysis [EXTRACTED 1.00]
- **Honest Gap Disclosure and Reframing Strategy Across Applications** — softserve_notes_gap_analysis_graphql_gap, softserve_notes_gap_analysis_aws_depth_gap, ryz_labs_elixir_job_analysis_report_tool_gap_not_concept_gap, remote_leverage_job_analysis_report_typescript_nextjs_gap [INFERRED 0.85]
- **Senior Elixir Positioning Across Ryz Labs and Shinkansen** — ryz_labs_elixir_cv_gonzalo_ryz_labs_cv, shinkansen_cv_gonzalo_shinkansen_cv, ryz_labs_elixir_cv_gonzalo_ryz_labs_elixir_otp_beam, ryz_labs_elixir_cv_gonzalo_ryz_labs_tellevoapp [INFERRED 0.85]
- **Elixir-targeted application track (Stord + Subvisual)** — stord_elixir_latam_cv_gonzalo_stord_document, stord_elixir_latam_job_analysis_report_senior_software_engineer_elixir_jr101607, subvisual_elixir_cv_gonzalo_subvisual_document, subvisual_elixir_job_analysis_report_elixir_developer_role, subvisual_elixir_job_analysis_report_priority_ranking [INFERRED 0.85]
- **TCIT application package: analysis → tailored CV → cover letter** — tcit_job_analysis_report_java_springboot_aws_role, tcit_job_analysis_report_ai_augmented_coder_differentiator, tcit_cv_gonzalo_tcit_document, tcit_cover_letter_tcit_document [EXTRACTED 1.00]
- **Agentic AI harness positioning reused across all CV variants** — stord_elixir_latam_cv_gonzalo_stord_agentic_harness_discipline, subvisual_elixir_cv_gonzalo_subvisual_judgment_over_blind_delegation, tcit_cv_gonzalo_tcit_ai_software_engineering_approach, technorex_wellfound_cv_gonzalo_technorex_agent_lifecycle_harness [INFERRED 0.85]
- **Pipeline de CV a medida por empresa: informe de análisis → CV markdown → PDF** — wall_partners_job_analysis_report_wall_partners_analysis, wall_partners_cv_gonzalo_wall_partners_cv, wall_partners_cv_gonzalo_wall_partners_pdf_render, telnyx_job_analysis_report_telnyx_analysis, telnyx_cv_gonzalo_telnyx_cv, telnyx_cv_gonzalo_telnyx_pdf_render [INFERRED 0.85]
- **Posicionamiento transversal de IA agéntica (Pi.dev/opencode) en todas las variantes de CV** — tecnologia_personas_cv_gonzalo_tecnologia_personas_ai_assistant_integration, telnyx_cv_gonzalo_telnyx_ai_harness_productivity, termgrid_cv_gonzalo_termgrid_agent_lifecycle_design, traackr_gonzalo_oviedo_traackr_software_engineer_agent_harness_spec_plan_execute_verify, wall_partners_cv_gonzalo_wall_partners_human_judgment_over_agents [INFERRED 0.85]
- **Paquete de evidencia Elixir/BEAM para la postulación a Telnyx** — telnyx_cv_gonzalo_telnyx_tellevoapp_elixir_production, telnyx_cv_gonzalo_telnyx_otp_beam_concurrency, telnyx_experiencia_programacion_funcional_immutability_pattern_matching, telnyx_job_analysis_report_match_analysis [EXTRACTED 1.00]
- **Agentic platform differentiator matching CV evidence to X-Team requirements** — xteam_platform_elixir_ai_cv_gonzalo_xteam_claude_md_instruction_files, xteam_platform_elixir_ai_cv_gonzalo_xteam_agentic_harness_toolchain, xteam_platform_elixir_ai_cv_gonzalo_xteam_agent_ready_engineering_platform, xteam_platform_elixir_ai_job_analysis_report_golden_path_creation, xteam_platform_elixir_ai_job_analysis_report_priority_rationale [INFERRED 0.85]
- **X-Team application targeting decision (apply to 2921, avoid 2906, fallback LATAM roles)** — xteam_platform_elixir_ai_job_analysis_report_senior_platform_engineer_vacancy, xteam_platform_elixir_ai_job_analysis_report_c1_english_exclusion, xteam_platform_elixir_ai_job_analysis_report_other_latam_roles, xteam_platform_elixir_ai_cv_gonzalo_xteam_english_b1_disclosure [INFERRED 0.85]
- **Career progression roles backing the X-Team CV narrative** — xteam_platform_elixir_ai_cv_gonzalo_xteam_mobility_startup_role, xteam_platform_elixir_ai_cv_gonzalo_xteam_perficient_caterpillar_role, xteam_platform_elixir_ai_cv_gonzalo_xteam_citibank_role, xteam_platform_elixir_ai_cv_gonzalo_xteam_seven_it_role, xteam_platform_elixir_ai_cv_gonzalo_xteam_early_career_role [EXTRACTED 1.00]

## Communities (69 total, 16 thin omitted)

### Community 0 - "Auditoría Anti-IA del CV"
Cohesion: 0.05
Nodes (49): Equifax Application — Academic Background, Claude Architect Certification (in progress), Equifax Cover Letter (EN), Equifax Tailored CV (EN), Equifax Tailored CV (PDF export), Markdown Layout Tables in Equifax CV, Unverifiable Metrics in Equifax CV (400%, 99.9%), Anti-AI CV Auditor (README) (+41 more)

### Community 1 - "Postulación Equifax InterConnect"
Cohesion: 0.06
Nodes (45): AI Agent Harness Leverage — ~3x Delivery Speed, Cover Letter — Senior Developer Java / Spring Boot (Equifax InterConnect), Decision Logic Close to the Data (PL/SQL, PostgreSQL in-database rules), Availability — 09:00–18:00 Schedule and Hybrid 2x3 Model, Equifax InterConnect Decisioning Platform, Cover Letter Equifax InterConnect (PDF render), Equifax Santiago Development Center (SDC), Differentiator — AI-Assisted Engineering (Pi.dev, Claude Code, OpenCode) (+37 more)

### Community 2 - "Postulación AGtec Backend"
Cohesion: 0.05
Nodes (44): Carta de Presentación AGtec — Desarrollador Backend Senior, Carta de Presentación AGtec (PDF renderizado), Por qué AGtec — encaje cultural y motivación, Python en contexto de software agéntico (Pi.dev, OpenCode), Redis como capa de caché en Salcobrand, Declaración de AWS Lambda en el CV AGtec, Java Specialist @ Citibank (2019-2022) — migración Sybase a Oracle, CTO & Co-founder — Startup de Movilidad (Java 21, GraalVM, GCP, Pulumi) (+36 more)

### Community 3 - "CV Base Manual"
Cohesion: 0.06
Nodes (43): Agentic AI Harness (Pi.dev, Opencode, Hermes), Java Specialist — Citibank (2021–2022), CTO & Co-founder — Startup de Movilidad (2024–Presente), Gonzalo Oviedo Lambert (Manual Base CV), Manual Base CV (PDF Render), Java Associative Developer — Perficient / Caterpillar (2022–2023), Senior Backend Architect / AI-Driven Development Positioning, Seven IT SpA — Hospital Cruz del Norte / SQM (2017–2020) (+35 more)

### Community 4 - "Postulación Stord Elixir"
Cohesion: 0.06
Nodes (43): Agentic AI harness discipline: spec → plan → execute → verify, Citibank Sybase→Oracle migration (15M+ records, 0% loss), CV Gonzalo Oviedo — Stord (Senior Software Engineer, Elixir), E-commerce payment & fulfillment domain experience (Caterpillar), Elixir/Phoenix/OTP on the BEAM (production expertise), Stord CV — PDF rendering, TeLlevoApp — two Elixir/Phoenix systems in production, Non-obvious domain advantage: high-volume commerce experience (+35 more)

### Community 5 - "Posicionamiento IA Agéntica"
Cohesion: 0.05
Nodes (42): CV Gonzalo Oviedo — Consorcio (Analista Desarrollador FullStack Java), Pandoc markup leak in rendered PDF (':::' and header attributes visible), Positioning: FullStack Java / Spring Boot / SQL / GCP (Spanish, Chile-local), Habilidades Primarias vs Secundarias skill-tiering device, Consorcio CV — rendered PDF (pandoc output), Agent Execution Harness (Pi.dev): skills, commands, workflows as DSL, Positioning: AI Agentic Engineer / LLM Systems Architect (role re-framing of same career), Bidirectional anonymization layer for cloud LLM calls (+34 more)

### Community 6 - "Postulación Prima Madrid"
Cohesion: 0.07
Nodes (42): CV Gonzalo Oviedo — Prima (Elixir, Madrid), Elixir / Phoenix / Ash Framework Stack, CV Prima — PDF Rendition, Immediate Relocation Availability to Madrid, TeLlevoApp Phoenix LiveView Production Projects, Microservices + Event-Driven + DDD Requirement, Prima Match Analysis (gaps: Event-Driven, English fluency, on-site), Prima — Elixir Software Engineer (Madrid) Vacancy (+34 more)

### Community 7 - "Informes de Análisis de Vacantes"
Cohesion: 0.07
Nodes (39): Metrica España — Backend Senior Java / Spring Boot 100% Remoto, Estrategia de énfasis: microservicios, Docker y testing JUnit/Mockito, Job Analysis Report — España Remoto (vacante adicional), Agentic AI harness experience as CV differentiator, FortIA — Ingeniero/a Senior de IA Agéntica (GetOnBoard, USD 3.5k–5.5k), Heurística de selección: menor número de postulantes gana, Job Analysis Report — IA Agéntica Remoto (FortIA), Rozeta Labs — Applied AI Engineer, Agentic Systems (runner-up) (+31 more)

### Community 8 - "Automatización Computrabajo"
Cohesion: 0.06
Nodes (36): actualizarCartaPresentacion, Technical Affinity Filter (no quota-filling applications), Post-Apply Cover Letter Attachment Step, Honest Technology Gap Declaration, Computrabajo Job Hunter Skill, 500-Character Killer Question Overflow Trap, Killer Questions Answer Bank (Computrabajo), Computrabajo Affine Market Exhaustion (+28 more)

### Community 9 - "CVs Backend Multi-Empresa"
Cohesion: 0.07
Nodes (36): Agentic AI harness practice (Pi.dev, opencode) as CV differentiator, AS/400 legacy banking modules migrated to Java architecture, CV v2 (English) — FullStack Developer Analyst (Java/Flutter/JS/SQL/GCP), Healthcare Management System (Seven IT SpA / Hospital Cruz del Norte), Pulumi Infrastructure-as-Code on Google Cloud, Zero-downtime Sybase → Oracle 500GB migration (Citibank), CV tailored for FCM Digital — Senior Backend Engineer (Elixir/OTP/Phoenix), Elixir/OTP/BEAM high-concurrency, fault-tolerant specialization (+28 more)

### Community 10 - "Postulación Coderslab Java"
Cohesion: 0.07
Nodes (35): ATS Keyword Block (Java 21, GCP, Fintech), CV Coderslab (Back-end Senior Java, ES) — coderlabs variant, CV Coderslab PDF Render (coderlabs), Primary vs Secondary Skill Table Split, High-Quality Code Culture as Motivator (PR reviews, automated testing), Carta de Interés Coderslab.io (ES), Observability Upskilling Motive (Prometheus, Grafana, ELK, Datadog), CV Coderslab (Back-end Engineer Java 21 + Node.js) (+27 more)

### Community 11 - "CVs Java Full Stack"
Cohesion: 0.07
Nodes (34): Agentic AI Harnessing (Pi.dev / OpenCode), Senior Java Developer — Citibank (2021-2022), Senior Java Full Stack Developer — WebClass/Creasys/Coopeuch (2008-2017), IA Agéntica — Orquestación de Agentes de Software (ES), CV Java Full Stack (ES) — PDF Renderizado, Senior Java Full Stack Developer Positioning (ES), Lead Software Engineer — Mobility Startup (2024-Present), Java Full Stack CV (EN) — Rendered PDF (+26 more)

### Community 12 - "Postulaciones J2EE y Codelco"
Cohesion: 0.08
Nodes (34): Cover Letter — Desarrollador Java J2EE / Spring Boot / POO (Multinacional TI), ATS Keyword Targeting for J2EE/POO Vacancy, CV Gonzalo Oviedo — Java J2EE / Spring Boot Senior (Multinacional TI), Hybrid Availability Constraint (Limache → 1 monthly Santiago meeting), CV Multinacional TI (PDF render), CV Gonzalo Oviedo — Full Stack Senior (Niuro / Codelco ODS 65), CV Niuro/Codelco (PDF render), Codelco Corporate Stack Requirement (NestJS, Next.js, Azure DevOps, Databricks) (+26 more)

### Community 13 - "Postulación Remote Leverage"
Cohesion: 0.10
Nodes (34): Cover Letter — Remote Leverage Full-Stack Engineer (Internal Tools), CV Gonzalo Oviedo — Remote Leverage (Spanish), Agent Harnesses (Pi.dev, opencode), AI-Enhanced Coder Positioning, CV Gonzalo Oviedo — Remote Leverage (English), Full-Cycle Feature Ownership (stakeholder request to deployment), CV Remote Leverage EN — PDF Render, Job Analysis — Remote Leverage Full-Stack Engineer (Internal Tools) (+26 more)

### Community 14 - "Postulación 2Brains"
Cohesion: 0.08
Nodes (33): AI Agent Harness Orchestration with Full Technical Ownership, 2BRAINS Experience Cover Statement, Completed-Startup / Immediate-Availability Narrative, Consultancy Variety Prevents Stagnation, 2BRAINS Interest / Motivation Letter, AI Coder Positioning (Pi.dev / opencode), CV Gonzalo Oviedo — 2BRAINS Senior Backend (Java/Spring/SQL), Job Analysis — Software Engineer Back-end Senior @ 2BRAINS (GetOnBoard cf68) (+25 more)

### Community 15 - "Analista Programador Computrabajo"
Cohesion: 0.08
Nodes (32): Codificador Potenciado por IA (diferenciador tecnológico), CV Gonzalo Oviedo — Analista Programador Senior (Computrabajo), Core Java / Spring Boot / SQL (Oracle, PostgreSQL), CV Analista Programador (PDF renderizado), Perfil Full-cycle (requerimientos a IaC en GCP), Estrategia de Personalización de CV (backend sólido + IA como valor agregado), Informe de Análisis de Empleo — Analista Programador, Vacante Analista Programador (Las Condes, confidencial) (+24 more)

### Community 16 - "CVs Telnyx y Tecnología y Personas"
Cohesion: 0.08
Nodes (31): Integración de asistentes de programación con IA como valor diferencial, CV Gonzalo Oviedo — Tecnología y Personas (Senior Backend Java / Spring Boot / AI), PDF render — CV Tecnología y Personas, AI Agent Harnesses (Pi.dev, Opencode, Hermes) como multiplicador de productividad, CV Gonzalo Oviedo — Telnyx (Senior Software Engineer, Elixir/OTP), Concurrencia y tolerancia a fallos con OTP/BEAM (GenServers, Supervisors), PDF render — CV Telnyx, TeLlevoApp — dos proyectos Elixir/Phoenix en producción (+23 more)

### Community 17 - "Postulaciones BCTecnología"
Cohesion: 0.10
Nodes (29): Cover Letter — BCTecnología Desarrollador FullStack Java (Microservicios Cloud), Transferibilidad GCP/AWS hacia OCI, CV — Desarrollador FullStack Java Senior, Microservicios Cloud (BCTecnología), Microservicios cloud-native (GCP, Docker, Pulumi IaC), PDF export — CV BCTecnología FullStack Cloud, Valor diferencial: orquestación de agentes con Pi.dev, Carta de Presentación — BCTecnología Full Stack Semi Senior (Remoto), CV — Desarrollador Full Stack Semi Senior (BCTecnología, Node/Angular) (+21 more)

### Community 18 - "Postulación X-Team Platform"
Cohesion: 0.08
Nodes (29): Agent-Ready Engineering Platform / Golden Path for SDLC Agents, Agentic Harness Toolchain (Claude Code, Pi.dev, opencode), AI-First Workflow as Daily Practice (spec -> plan -> execute -> verify), Senior Java Specialist — Citibank (2021-2022), CLAUDE.md Agent Instruction Files and Repo Guardrails, Developer Experience Evidence (standardized Docker envs, 85% JUnit coverage), Senior Software Engineer — WebClass, Creasys, Coopeuch (2008-2017), Elixir / Phoenix / LiveView / Ash / OTP Expertise (+21 more)

### Community 19 - "Scraping de Ofertas Computrabajo"
Cohesion: 0.11
Nodes (27): Avos Tech (Computrabajo employer listing), BCTecnología (Computrabajo employer listing), Computrabajo Deduplicated Offer Index, ListOffers Score Bucket Ranking, Computrabajo Round 6 Raw Offer Scrape, Computrabajo Round 6 Unique Offers, Computrabajo Round 6b Offer Scrape, Computrabajo Application Shortlist Queue (+19 more)

### Community 20 - "Postulaciones Kibernum y Knowmad"
Cohesion: 0.11
Nodes (25): Carta de Presentación — Kibernum Full Stack Java/Angular, Transferibilidad hacia Angular 14+ desde frameworks reactivos, CV Gonzalo Oviedo — Kibernum (Java/Angular, GCP, Agentic AI), CV Kibernum (render PDF), Estrategia de personalización ATS para Kibernum, Computrabajo (portal de origen de la vacante), Vacante Kibernum S.A. — Desarrollador/a Full Stack Java/Angular, Diseño del ciclo de vida de agentes (skills, comandos, workflows) (+17 more)

### Community 21 - "Vacantes Elixir Remotas"
Cohesion: 0.18
Nodes (13): cv_job_linkage_tracker (Agente 7), IA agéntica (Claude Code, Pi.dev) como discriminador poco común, Patient Reach 360 — Full Stack Elixir Developer (Phoenix/LiveView), Ryz Labs — Senior Software Engineer (Elixir), Stord — Senior Software Engineer (Elixir), Remote Latin America, Subvisual — Elixir Developer (work from anywhere), X-Team — Senior Platform Engineer Elixir/TypeScript & AI (LATAM, rol 2921), cv_job_links.md — registro de trazabilidad CV ↔ vacante (93 postulaciones) (+5 more)

### Community 22 - "Agentes de CV y Verificabilidad"
Cohesion: 0.29
Nodes (10): ai_profile_enhancer (Agente 4), anti_ai_cv_auditor (Agente 5), cv_tailor (Agente 9, sastre por oferta), Regla de verificabilidad (Restricción global n.º 3), Afirmación "incrementando la velocidad de codificación hasta 300%", cv.md — CV maestro en español (Source of Truth), cv.md como Source of Truth (personalización sin alucinaciones), Talentview 3D — informe de evaluación psicolaboral de Gonzalo Oviedo (15-jun-2026) (+2 more)

### Community 23 - "Postulación GFT Technologies"
Cohesion: 0.22
Nodes (10): CV Gonzalo Oviedo — GFT Technologies (Full Stack Java / React / SQL), Enfoque en banca regulada, compliance y OWASP (perfil GFT), CV GFT Technologies (PDF renderizado), Carta de Presentación — GFT Technologies LATAM, Nota de verificabilidad de logros declarados, Carta de Presentación GFT (PDF renderizado), Filosofía de trabajo en tres pilares (valor al negocio, adaptabilidad, visión full-cycle), Portal de postulación GFT (jobs.gft.com) con credencial parcial (+2 more)

### Community 24 - "Informes de Búsqueda Java"
Cohesion: 0.22
Nodes (10): Exclusión de vacantes ya postuladas para evitar duplicados, Informe de Búsqueda de Empleo #2 — alternativa a BC Tecnología, Vacante: Analista Desarrollador Fullstack Java — Consorcio (banca, presencial, 90%), Búsqueda multi-portal con conteo por portal y descarte de ofertas cerradas, Informe de Análisis #3 — Coderslab.io (búsqueda en 7 portales), Vacante: Back-end Senior Java — Coderslab.io (100% remoto, USD 2.400-3.000, 92%), Criterios de filtrado de vacantes (título, ubicación, nivel, <50 postulantes), Informe de Búsqueda de Empleo #1 — Java/Spring Boot Semi Senior Chile (+2 more)

### Community 25 - "Configuración de Modelos en pi"
Cohesion: 0.29
Nodes (8): Plan: Native Anthropic Provider in pi, Global defaultProvider/defaultModel Override, Anthropic OAuth Subscription Auth (auth.json), Explicit claude/* Model References, Plan: Claude Models via OmniRoute Gateway, Route A: omniroute provider in OpenAI format, Route B: omniroute-claude provider (anthropic-messages), upstream_empty_response on Low max_tokens

### Community 26 - "Portales y Reglas de Método"
Cohesion: 0.25
Nodes (8): Prohibición de los títulos CTO y Co-founder, Advertencia de método: postular siempre por el ATS original, nunca por el agregador, SQM — Data Engineer (Santiago, Databricks/Azure), SQM — Ingeniero/a Sistemas CIO (Nueva Victoria, TI/OT industrial), SQM: solo el portal oficial trabajaensqm.com cuenta como postulación válida, CTO & Co-founder — Startup de Movilidad (Elixir/Ash, Pi.dev, 2024-Presente), JOB-PORTALS.md — base de conocimiento canónica de portales de empleo, Portales descartados (cerrados o absorbidos): Stack Overflow Jobs, Hired.com, AngelList Talent…

### Community 27 - "Script filter.js"
Cohesion: 0.25
Nodes (6): base, baseKeys, fresh, fs, offers, out

### Community 28 - "Pipeline de Agentes Legacy"
Cohesion: 0.38
Nodes (7): job_analysis_reporter (Agente 2), Modo directo (oferta provista por el usuario), multi_portal_scraper (Agente 1), resume_skills_customizer (Agente 3), Método de re-verificación: endpoint Elasticsearch _search de trabajaensqm.com, Marca 🤖: portales que bloquean scrapers (Cloudflare) y exigen consulta manual, Pipeline de 4 agentes (versión legacy del manual)

### Community 29 - "Exportación PDF y Pandoc"
Cohesion: 0.29
Nodes (7): markdown_format_polisher (Agente 6), pdf_exporter (Agente 8), Pipeline Multi-Portal Job Hunter & ATS Optimizer (Tareas 1-8), Regla m2pdf: único conversor autorizado a PDF, Artefactos Pandoc residuales (.unnumbered, #anclas) en el CV maestro, Lote 2026-08-03: 14 postulaciones Computrabajo con cv.pdf de perfil, sin CV personalizado, Stack tecnológico integrado (Pi.dev, CrewAI, Playwright, md-to-pdf)

### Community 30 - "Vías Legales para Trabajar en España"
Cohesion: 0.29
Nodes (7): Autorización de trabajo UE como obstáculo real (no el idioma), getManfred (publica salario obligatoriamente), InfoJobs (contrato español, exige residencia), Vía Contractor B2B (factura de exportación de servicios, SII), Vía EOR (Deel, Remote — empleador legal en Chile), Vía Tarjeta Azul-UE (RD 1155/2024, umbral €39.269,92), Tres vías legales para trabajar con una empresa española desde Chile

### Community 31 - "Postulación FullStack Kotlin/React"
Cohesion: 0.29
Nodes (7): Atribución discrepante: Equifax como empleador del e-commerce Caterpillar (2022-2023), Agentic AI con Pi.dev — ciclo de vida de agentes (skills, comandos, workflow) como harness, CV histórico — FullStack Java / Flutter / JavaScript / SQL / GCP, Exploración de tecnologías emergentes (Elixir/Ash, Blockchain ICP/Solidity), Uso de herramientas de IA (Cursor, Claude Code, Copilot) como requisito explícito del mercado, Informe de Análisis — Full Stack Engineer (FullStack, LinkedIn), Vacante: Full Stack Engineer (Java + Kotlin + React) — FullStack, 100% remoto LatAm

### Community 32 - "Búsqueda Java en Alemania"
Cohesion: 0.29
Nodes (7): Expectativa salarial $2.5M–$3.5M CLP y salario actual declarado, Declaración de nivel de inglés B1 intermedio, Benchmark salarial Java/Spring Boot en Alemania por nivel, Brecha de idioma B1 vs C1 exigido como principal riesgo de la postulación, Informe de Búsqueda #4 — Spring Boot Java Developer en Alemania, Presentar GCP/Pulumi como experiencia cloud-native transferible a AWS, Vacante: Senior Software Developer Java/Spring Boot — SII Group Germany (híbrido, 88%)

### Community 33 - "Selección de Vacantes IA + Frontend"
Cohesion: 0.29
Nodes (7): Disponibilidad para reubicación / modalidad híbrida en España, Criterio de selección: priorizar vacantes que capitalicen la habilidad diferencial en Agentic AI, Informe de Análisis #5 — 2Brains (Java + Angular + IA), Vacante: Desarrollador Full-Stack (Java + Angular + IA) — 2Brains (remoto), Encaje estratégico: vacantes que valoran IA + frontend maximizan la propuesta de valor, Informe de Análisis — España Remoto (Senior Spring Boot Java), Vacante: Desarrollador/a Backend Java (Spring Boot) — Tecnología y Personas (España, remoto)

### Community 34 - "Postulación GetData PL/SQL"
Cohesion: 0.33
Nodes (6): Claim de productividad 300% sostenido / picos 2000%, CV Gonzalo Oviedo — GetData (Java / Spring Boot / PL-SQL), CV GetData (PDF renderizado), Posicionamiento PL/SQL como habilidad primaria (perfil GetData), Valor Diferencial — AI Engineering (agentes Pi.dev / Claude Code), Métricas verificables como recurso de redacción (15M registros, 1.800 escuelas, 500K peticiones/día)

### Community 35 - "Estrategia Nicho Elixir España"
Cohesion: 0.40
Nodes (5): Elixir como diferenciador para España, no Java, Prima (insurtech, Madrid, Elixir/Rust, full-remote), Posicionamiento como arquitecto backend políglota (Java/Spring + Elixir), Realidad del mercado Elixir: 3-6 vacantes vivas abiertas a Chile, Nicho Elixir/BEAM y conteo real por board

### Community 36 - "Postulación ITPS Arquitectura Hexagonal"
Cohesion: 0.40
Nodes (5): Salcobrand (2023-2024) declarado como último cliente formal, Respuestas de screening por WhatsApp — GFT Technologies, Arquitectura hexagonal y principios SOLID como eje del perfil, CV Gonzalo Oviedo — ITPS (Developer Java SR / Lead Software Engineer), CV ITPS (PDF renderizado)

### Community 37 - "Script parse_job.js"
Cohesion: 0.40
Nodes (4): fs, html, ldjsonMatches, titleMatch

### Community 38 - "Baseline y Falsos Negativos"
Cohesion: 0.50
Nodes (4): Tomar baseline antes de cada ronda y medir por delta del contador, Falsos negativos: la página de detalle no revela si ya se postuló, Lista de URLs candidatas (primer filtro grueso), Dossier 1 — cuerpos completos de aviso con APPLIEDFLAG

### Community 49 - "Inglés B1 y Marketplaces"
Cohesion: 0.67
Nodes (3): Inglés B1 como restricción vinculante, Gun.io — marketplace sin screening de inglés dedicado, Clasificación de marketplaces por exigencia de inglés (B1 viable vs B2/C1)

### Community 50 - "CV Maestro en Inglés"
Cohesion: 1.00
Nodes (3): cv-en.md — CV maestro en inglés, cv-en.pdf — exportación PDF del CV en inglés, cv-goviedo.pdf — PDF cuyo contenido es el CV en inglés, pese al nombre

### Community 52 - "Documentación del Framework"
Cohesion: 0.67
Nodes (3): MANUAL.md — Manual de uso del Multi-Portal Job Hunter, Skill job-hunter-linkedin (.pi/skills/job-hunter-linkedin/), README.md — framework de búsqueda de empleo automatizada

## Ambiguous Edges - Review These
- `cv_job_linkage_tracker (Agente 7)` → `Estados de postulación (Pendiente / Enviado / Rechazado / Entrevista / Oferta)`  [AMBIGUOUS]
  MANUAL.md · relation: conceptually_related_to
- `Regla m2pdf: único conversor autorizado a PDF` → `Stack tecnológico integrado (Pi.dev, CrewAI, Playwright, md-to-pdf)`  [AMBIGUOUS]
  README.md · relation: conceptually_related_to
- `SQM — Data Engineer (Santiago, Databricks/Azure)` → `CTO & Co-founder — Startup de Movilidad (Elixir/Ash, Pi.dev, 2024-Presente)`  [AMBIGUOUS]
  BUSQUEDA-SQM.md · relation: conceptually_related_to
- `Declaración de AWS Lambda en el CV AGtec` → `Gap declarado: sin experiencia de producción en AWS (cloud es GCP)`  [AMBIGUOUS]
  agtec_servicios/qa_agtec.md · relation: conceptually_related_to
- `CV — BC Tecnología (Java Spring Boot Semi Senior variant)` → `GetOnBrd Application Portal Entry Point`  [AMBIGUOUS]
  bc-tecnologia/portal.txt · relation: conceptually_related_to
- `Fiserv Staff Java Software Engineer CV (EN, Markdown)` → `Seniority Downshift Framing (15+ years presented as Semi Senior)`  [AMBIGUOUS]
  companies/cv_gonzalo_bc_tecnologia.md · relation: conceptually_related_to
- `CV Gonzalo Oviedo — GFT Technologies (Full Stack Java / React / SQL)` → `Employer attribution discrepancy: Caterpillar e-commerce credited to Equifax, and Banco de Chile listed for 2008-2017`  [AMBIGUOUS]
  companies/cv_gonzalo_gft_technologies.md · relation: references
- `Employer attribution discrepancy: Caterpillar e-commerce credited to Equifax, and Banco de Chile listed for 2008-2017` → `CV Gonzalo Oviedo — Miratech (Software Engineer, Java/Spring/Cloud, English)`  [AMBIGUOUS]
  companies/cv_gonzalo_gft_technologies.md · relation: conceptually_related_to
- `CV Gonzalo Oviedo — Miratech (Software Engineer, Java/Spring/Cloud, English)` → `English level reframed from 'Intermedio B1' to 'Inglés técnico profesional, 6+ años'`  [AMBIGUOUS]
  companies/cv_gonzalo_turtle_trax.md · relation: conceptually_related_to
- `CV Gonzalo Oviedo — Analista Desarrollador FullStack (Consorcio)` → `Regla del proyecto: sin "CTO" ni "Co-founder"`  [AMBIGUOUS]
  contractor/extracto_computrabajo.md · relation: conceptually_related_to
- `Arquitecto Full-Stack Senior Positioning (Generic ES)` → `Gonzalo Oviedo — Baseline Generic CV PDF`  [AMBIGUOUS]
  generico/cv_gonzalo_oviedo.pdf · relation: semantically_similar_to
- `Atribución discrepante: Equifax como empleador del e-commerce Caterpillar (2022-2023)` → `CV histórico — FullStack Java / Flutter / JavaScript / SQL / GCP`  [AMBIGUOUS]
  gft-technologies/cv_gonzalo_gft_technologies.md · relation: conceptually_related_to
- `Salcobrand (2023-2024) declarado como último cliente formal` → `CV Gonzalo Oviedo — ITPS (Developer Java SR / Lead Software Engineer)`  [AMBIGUOUS]
  gft_technologies/respuestas_whatsapp.md · relation: conceptually_related_to
- `Universidad del Bío Bío — Extreme Programming (XP) Thesis` → `Patrones de Diseño GoF (Creacionales, Estructurales, Comportamiento)`  [AMBIGUOUS]
  manual/cv.md · relation: conceptually_related_to
- `TeLlevoApp Phoenix LiveView Production Projects` → `End-to-End Carpooling Ecosystem (app.tellevoapp.cl) Achievement`  [AMBIGUOUS]
  remote/application_responses.md · relation: conceptually_related_to
- `CV Gonzalo Oviedo — Remote (English, Senior Backend Elixir)` → `Mixed Spanish/English Summary Section in an English CV`  [AMBIGUOUS]
  remote/cv_gonzalo_remote_en.md · relation: rationale_for
- `No certified English level required (only strong communication)` → `English claimed as Professional Working Proficiency`  [AMBIGUOUS]
  tecla_peru/cv_gonzalo_tecla_peru.md · relation: conceptually_related_to
- `Wellfound applications portal note (Technorex)` → `CV Gonzalo Oviedo — Technorex (FullStack Java / Spring Boot / GCP)`  [AMBIGUOUS]
  technorex/job-post.txt · relation: references

## Knowledge Gaps
- **222 isolated node(s):** `apply_start.sh script`, `CHROME_DEVTOOLS_AXI_AUTO_CONNECT`, `check_applied.sh script`, `CHROME_DEVTOOLS_AXI_AUTO_CONNECT`, `cover.sh script` (+217 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `cv_job_linkage_tracker (Agente 7)` and `Estados de postulación (Pendiente / Enviado / Rechazado / Entrevista / Oferta)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Regla m2pdf: único conversor autorizado a PDF` and `Stack tecnológico integrado (Pi.dev, CrewAI, Playwright, md-to-pdf)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `SQM — Data Engineer (Santiago, Databricks/Azure)` and `CTO & Co-founder — Startup de Movilidad (Elixir/Ash, Pi.dev, 2024-Presente)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Declaración de AWS Lambda en el CV AGtec` and `Gap declarado: sin experiencia de producción en AWS (cloud es GCP)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `CV — BC Tecnología (Java Spring Boot Semi Senior variant)` and `GetOnBrd Application Portal Entry Point`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Fiserv Staff Java Software Engineer CV (EN, Markdown)` and `Seniority Downshift Framing (15+ years presented as Semi Senior)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `CV Gonzalo Oviedo — GFT Technologies (Full Stack Java / React / SQL)` and `Employer attribution discrepancy: Caterpillar e-commerce credited to Equifax, and Banco de Chile listed for 2008-2017`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._