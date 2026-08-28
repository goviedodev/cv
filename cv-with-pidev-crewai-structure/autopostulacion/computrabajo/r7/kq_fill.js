() => {
  if (!/candidate\/kq/.test(location.href)) return "ABORT:no-es-kq " + location.href;

  const norm = s => (s || "").replace(/\s+/g, " ").trim();
  const ctxOf = el => {
    let p = el;
    for (let i = 0; i < 5 && p; i++) { p = p.parentElement; if (p && norm(p.innerText).length > 25) break; }
    return norm(p ? p.innerText : "").toLowerCase();
  };

  const allQ = norm(document.body.innerText).toLowerCase();

  // --- aborto si el cuestionario revela un stack excluyente ---
  const EXCL = /\.net\b|asp\.net|c#|vb\.net|cobol|salesforce|murex|dynamics 365|servicenow|prestashop|\babap\b|genexus|flexcube|uipath|sap\s|powerbuilder|delphi/;
  if (EXCL.test(allQ)) return "ABORT:stack-excluyente";

  // --- renta segun seniority del aviso ---
  const title = norm(document.title + " " + allQ.slice(0, 200)).toLowerCase();
  let monto = "$2.400.000";
  if (/arquitect|tech lead|l[ií]der t[eé]cnico|jefe de desarrollo/.test(title)) monto = "$3.000.000";
  else if (/senior|staff|especialista/.test(title)) monto = "$2.700.000";
  else if (/semi ?senior/.test(title)) monto = "$2.000.000";

  const A = {
    renta: "Mi expectativa es de aproximadamente " + monto + " liquidos mensuales, dentro de un rango de $1.800.000 a $3.000.000 segun el nivel de responsabilidad, conversable segun beneficios y caracteristicas del proyecto. Disponibilidad inmediata para incorporarme y participar en el onboarding desde el primer dia.",
    disponibilidad: "Cuento con disponibilidad inmediata para incorporarme al proyecto y participar en los procesos de induccion y onboarding desde el primer dia.",
    java: "Mas de 15 anos desarrollando con Java y mas de 8 anos disenando microservicios y APIs REST con Spring Boot, desde Java 1.8 hasta Java 21 / Spring Boot 3. Entornos financieros de alta disponibilidad (Citibank, Coopeuch), e-commerce global (Caterpillar via Perficient) y plataformas cloud como Architect y Lead Software Engineer.",
    banca: "Si. En Citibank fui Java Specialist trabajando sobre Java, Oracle SQL, Spring y WebSphere, donde lidere la migracion de mas de 15 millones de registros financieros de Sybase a Oracle sin perdida de datos. Antes trabaje en Coopeuch. Conozco las exigencias de disponibilidad, trazabilidad y control de cambios del sector bancario.",
    sql: "Mas de 15 anos de experiencia. Diseno relacional, optimizacion de consultas y desarrollo complejo en PL/SQL (procedimientos, triggers, tuning). Lidere la migracion de mas de 15 millones de registros financieros de Sybase a Oracle en Citibank sin perdida de datos, y trabajo PostgreSQL de forma experta en plataformas de movilidad y salud.",
    cloud: "Nivel avanzado. Trabajo Docker a diario y construyo pipelines CI/CD (Jenkins, GitLab CI, Azure DevOps). Mi foco cloud es Google Cloud Platform con infraestructura como codigo en Pulumi, mas experiencia en AWS Lambda y almacenamiento. Aclaro con transparencia: no he operado Kubernetes en produccion (uso Docker + Cloud Run) ni Terraform; mi IaC es Pulumi.",
    micro: "Si. Mas de 8 anos disenando e implementando microservicios y APIs REST con Spring Boot, aplicando arquitectura hexagonal, orientada a eventos, DDD y principios SOLID. Experiencia en integraciones, brokers de mensajeria y estandares de diseno de APIs en entornos de alta disponibilidad.",
    front: "Si. Experiencia solida en frontend con Angular y React sobre TypeScript, aplicando Atomic Design para componentes modulares y mantenibles, con consumo eficiente de APIs REST.",
    mobile: "Si. Desarrollo mobile con Flutter en Te Llevo App, donde participe como Architect y Lead Software Engineer construyendo la aplicacion y su integracion con backend propio en Elixir/Ash y Java/Spring Boot sobre GCP.",
    vibe: "Es mi forma habitual de trabajar. Uso a diario herramientas de coding agentico (Claude Code y equivalentes) para orquestar agentes que exploran el codigo, proponen e implementan cambios y ejecutan pruebas, revisando siempre la salida con criterio de arquitectura, patrones de diseno y SOLID. Esto me permite entregar con alta velocidad sin ceder en calidad, apoyado en mas de 15 anos de backend Java/Spring y Elixir.",
    ia: "Integro Inteligencia Artificial agentica de forma nativa en mi flujo diario de desarrollo: orquesto agentes para resolver problemas y codificar con alta calidad y velocidad, manteniendo criterio de arquitectura y patrones. Integro LLMs a bajo nivel via API. Declaro con transparencia que no he trabajado MLOps ni entrenamiento de modelos.",
    ml: "Trabajo integracion de LLMs e IA agentica aplicada al desarrollo de software y a producto. Declaro con transparencia que no tengo experiencia en Machine Learning clasico, entrenamiento de modelos ni MLOps (SageMaker, Azure AI); mi aporte esta en disenar e integrar soluciones de IA sobre arquitecturas backend solidas.",
    python: "Uso Python de forma puntual para scripting, automatizacion e integracion de servicios de IA. Mi profundidad esta en Java/Spring Boot y Elixir, con mas de 15 anos de backend; me adapto rapido a Python apoyandome en esa base y en IA agentica.",
    ingles: "Poseo ingles intermedio B1 y dominio avanzado de ingles tecnico para lectura de documentacion y colaboracion en equipos distribuidos. He trabajado con equipos de EE.UU., India y Latinoamerica en Perficient/Caterpillar.",
    estudios: "Titulo profesional de Ingenieria en Ejecucion en Computacion e Informatica, Universidad del Bio Bio.",
    modalidad: "Resido en Limache, Region de Valparaiso. Estoy plenamente de acuerdo con modalidad remota o hibrida y cuento con oficina equipada y conectividad para trabajo remoto efectivo, con disponibilidad para asistir presencialmente cuando el equipo lo requiera.",
    exp: "Mas de 15 anos de experiencia en desarrollo de software, los ultimos anos como Architect y Lead Software Engineer. Stack principal Java 21 / Spring Boot 3, Elixir/Ash, PostgreSQL y Oracle, GCP con Docker, Pulumi IaC y CI/CD. Experiencia liderando equipos, definiendo estandares tecnicos, mentoria y code review.",
    def: "Cuento con mas de 15 anos de experiencia en desarrollo de software backend (Java/Spring Boot, Elixir), bases de datos relacionales y cloud GCP, liderando equipos como Architect y Lead Software Engineer. Detallo mi trayectoria completa en el CV adjunto y quedo disponible para profundizar en entrevista."
  };

  const pick = q => {
    if (/pretensi|renta|sueldo|salari|expectativa|aspiraci|liquid/.test(q)) return A.renta;
    if (/disponibilidad|cuando podr|incorporaci|iniciar|comenzar/.test(q)) return A.disponibilidad;
    if (/banc|financier|retail financ/.test(q)) return A.banca;
    if (/vibe coding|claude code|codex|copilot|cursor|coding agentic|agentes de c[oó]digo/.test(q)) return A.vibe;
    if (/machine learning|\bml\b|redes neuronales|modelos predictiv/.test(q)) return A.ml;
    if (/\bia\b|inteligencia artificial|\bllm\b|agente|copilot|genai/.test(q)) return A.ia;
    if (/flutter|mobile|android|\bios\b|aplicaciones m[oó]viles/.test(q)) return A.mobile;
    if (/python/.test(q)) return A.python;
    if (/java|spring/.test(q)) return A.java;
    if (/sql|oracle|postgres|base de datos|bases de datos|pl\/sql/.test(q)) return A.sql;
    if (/cloud|gcp|aws|azure|docker|kubernetes|devops|ci\/cd|pipeline|infraestructura/.test(q)) return A.cloud;
    if (/microservici|\bapi\b|rest|integracion|arquitectur/.test(q)) return A.micro;
    if (/angular|react|frontend|front-end|javascript|typescript/.test(q)) return A.front;
    if (/ingl[eé]s|idioma/.test(q)) return A.ingles;
    if (/titul|estudi|carrera|formaci[oó]n|universidad|egresad/.test(q)) return A.estudios;
    if (/presencial|h[ií]brid|remoto|modalidad|teletrabajo|residir|vive|comuna/.test(q)) return A.modalidad;
    if (/experiencia|anos|años|trayectoria|cuentas con|posee/.test(q)) return A.exp;
    return A.def;
  };

  // --- textareas ---
  const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
  const tas = Array.from(document.querySelectorAll("textarea"));
  tas.forEach(t => {
    let v = pick(ctxOf(t));
    if (v.length > 495) v = v.slice(0, 492) + "...";
    setter.call(t, v);
    t.dispatchEvent(new Event("input", { bubbles: true }));
    t.dispatchEvent(new Event("change", { bubbles: true }));
  });

  // --- radios: elegir la opcion mas veraz por grupo ---
  const groups = {};
  document.querySelectorAll("input[type=radio]").forEach(r => (groups[r.name] = groups[r.name] || []).push(r));
  Object.values(groups).forEach(rs => {
    const lab = r => norm((r.closest("label") || r.parentElement || {}).innerText || "").toLowerCase();
    const q = ctxOf(rs[0]);
    let chosen = null;
    // preguntas de anos -> el tramo mas alto (tiene 15+ anos)
    if (/anos|años|tiempo de experiencia|cuanto/.test(q)) {
      const nums = rs.map(r => { const m = lab(r).match(/(\d+)/); return { r, n: m ? +m[1] : -1 }; });
      const mas = nums.filter(x => /m[aá]s de/.test(lab(x.r)));
      chosen = (mas.length ? mas : nums).sort((a, b) => b.n - a.n)[0].r;
    }
    if (!chosen) chosen = rs.find(r => /^avanzado$/.test(lab(r)));
    if (!chosen) chosen = rs.find(r => /^s[ií]\b/.test(lab(r)));
    if (!chosen) chosen = rs.find(r => /^intermedio$/.test(lab(r)));
    if (!chosen) chosen = rs[0];
    chosen.click();
  });

  // --- validacion ---
  const vacios = tas.filter(t => !t.value.trim()).map(t => t.id);
  const largos = tas.filter(t => t.value.length > (t.maxLength > 0 ? t.maxLength : 500)).map(t => t.id + ":" + t.value.length);
  const sinMarcar = Object.keys(groups).filter(n => !groups[n].some(r => r.checked));
  if (vacios.length) return "ISSUE:vacios " + vacios.join(",");
  if (largos.length) return "ISSUE:overflow " + largos.join(",");
  if (sinMarcar.length) return "ISSUE:radios " + sinMarcar.join(",");
  return "READY ta=" + tas.length + " rd=" + Object.keys(groups).length;
}
