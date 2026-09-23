# Carta de Motivación — Cloud Engineer (Mid/Sr), 100% remoto

**Gonzalo Oviedo Lambert**
Limache, Región de Valparaíso, Chile · GMT-4 · +56 9 6372 3603
goviedo.laboral@gmail.com · linkedin.com/in/gol · github.com/goviedodev

**Para:** Equipo de Talento y Tecnología, Alegra
**Asunto:** Postulación a Cloud Engineer (Mid/Sr) — trabajo 100% remoto

---

Estimado equipo de Alegra:

Postulo a **Cloud Engineer (Mid/Sr)** porque el rol describe lo que ya hago todos los días: ser **responsable end-to-end de mejorar, optimizar y monitorear la infraestructura**, y sostener las **plataformas internas que usa el equipo de desarrollo para moverse rápido y sin fricción**. Llevo más de 15 años en software y los últimos años los he pasado del lado de la infraestructura, no como observador.

## He estado en los dos lados del mostrador

Buena parte de mi carrera la pasé escribiendo servicios **junto a los equipos de Infraestructura, Cloud, DevOps y Platform**, no aislado de ellos.

En **Salcobrand** trabajé sobre APIs de alto tráfico de una cadena de farmacias coordinando con Infraestructura y DevOps los límites de recursos de los contenedores, las credenciales y variables gestionadas por plataforma, las colas de **IBM MQ** y la capacidad de la caché **Redis**, además de las ventanas de despliegue y los planes de rollback. Cuando había un incidente, yo aportaba la vista de aplicación y ellos la de infraestructura; el diagnóstico salía de esa conversación, no de un ticket.

En **Perficient**, para el e-commerce global de **Caterpillar**, fui el "equipo de desarrollo" al que una plataforma interna tiene que habilitar. El equipo de Cloud y Platform de Caterpillar era dueño de los pipelines, los ambientes y los estándares corporativos; mis servicios se desplegaban por ahí, con sus templates, sus reglas de configuración y sus controles de seguridad, coordinando cada promoción de ambiente. Sé perfectamente cuándo una plataforma interna acelera al equipo y cuándo se convierte en el cuello de botella — y eso es lo que quiero evitar construyendo la de Alegra.

## Hoy: infraestructura como código con Pulumi sobre GCP

Desde 2024 soy responsable de la infraestructura de **Te Llevo** (app.tellevoapp.cl), una plataforma de movilidad en producción. **Toda su infraestructura está escrita en Pulumi**: servicios de **Cloud Run**, **VMs** de Compute Engine, VPC y reglas de firewall, Load Balancer con TLS, políticas de **Cloud Armor (WAF)**, cuentas de servicio con **IAM de menor privilegio** y secretos en **Secret Manager**, todo versionado en Git. Reconstruir un entorno es ejecutar el stack y revisar el plan de cambios, no seguir una lista de pasos en la consola. Organicé ese código en componentes reutilizables y stacks por entorno para que un servicio nuevo herede red, permisos, logging y estándares sin depender de mí.

También integro y opero **Google Maps Platform** —rutas, geocodificación y mapas— como dependencia crítica del producto: restricción y rotación de API keys, control de cuotas y **monitoreo continuo del costo por request**, que es la partida más sensible de la cuenta. El **monitoreo de costos de forma continua** que piden en el aviso no es teoría para mí: es lo que revisa todos los meses quien paga la factura.

Sobre observabilidad y seguridad: mantengo **monitoreo y alertas con foco en detección proactiva, no reactiva** (Cloud Logging/Monitoring), resuelvo incidentes buscando **causa raíz y prevención, no parches**, y soy dueño de la **detección de tráfico anómalo**, la **gestión de secretos**, el **IAM** y la **respuesta ante incidentes**.

## IA en el flujo real de trabajo, no como discurso

Me llamó la atención que Alegra declare que usar IA no es opcional, sino la norma. Es la forma en que ya trabajo.

Como flujo personal me pareció muy interesante explorar tecnologías emergentes de IA como **Jido.AI con Elixir y Phoenix**. Jido es un framework de agentes, y eso es justamente lo que lo hace especial para el desarrollo de algoritmos: deja la parte determinista donde debe estar (100% determinista) y reserva la IA para donde realmente aporta. El resultado está desplegado y en línea en **https://farma.limachelocales.cl**.

Desde diciembre del año pasado empecé a aplicar IA en el desarrollo de la startup, construyendo un **harness sobre Claude Code** para un flujo de desarrollo guiado y completo — el resultado está en producción en **https://app.tellevoapp.cl**. Los resultados son confiables porque el flujo no depende del prompt: primero con **Firstmate** y ahora con **openspec**, el trabajo pasa obligatoriamente por una etapa de planificación antes de tocar código, y después me aseguro de que existan los tests suficientes, además de linter y cobertura. Esa es la diferencia entre usar IA y confiar en ella.

También desarrollé una aplicación con **Spring AI** para aplicar **RAG** sobre la Ley de Protección de Datos Personales, en línea en **https://datos-personales.limachelocales.cl/**, y actualmente estoy ayudando a una zapatería de la zona con una solución construida 100% con IA sobre **Cloudflare**.

En el día a día eso se traduce en lo que ustedes describen: **agentes, MCPs y skills** propios aplicados a **análisis, automatización y desarrollo**, y **automatizaciones basadas en agentes de IA para eliminar tareas manuales**.

## Transparencia sobre el stack

Prefiero decirlo de frente: mi nube productiva es **Google Cloud, no AWS** (en AWS he usado Lambda y S3, no una arquitectura serverless completa), mi IaC es **Pulumi, no Terraform**, y mi monitoreo es Cloud Logging/Monitoring, no CloudWatch ni Grafana. El aviso admite "o sus equivalentes" y creo que es honesto por ambas partes: los conceptos son los mismos —serverless gestionado, WAF, gestión de secretos, IAM de menor privilegio, alertas, IaC declarativa con plan y estado versionado— y la curva entre Pulumi y Terraform, o entre Cloud Run y Lambda, se recorre leyendo documentación, que es exactamente el uso que le doy a mi inglés B2. Lo que no se aprende en una semana es haber sido responsable de que una plataforma no se caiga, y eso sí lo traigo.

## Condiciones

- **Modalidad:** 100% remoto, disponibilidad inmediata para coordinar en GMT-4 y para los coworkings mensuales.
- **Pretensión salarial:** **USD 2.200 mensuales**.

Me interesa Alegra porque la infraestructura ahí no es un área de soporte: es el producto que usan los equipos de desarrollo. Me gustaría conversar sobre cómo se ve hoy el camino de salida del monolito y qué falta para que cada equipo se autogestione.

Quedo atento.

**Gonzalo Oviedo Lambert**
goviedo.laboral@gmail.com · +56 9 6372 3603 · linkedin.com/in/gol
