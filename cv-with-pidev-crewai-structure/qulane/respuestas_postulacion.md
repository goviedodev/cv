# Respuestas preparadas — Qulane (.NET Web Forms + SQL Server, Part Time)

> Todo en **español** (el portal lo exige). Ninguna respuesta reclama experiencia en .NET que no existe.

---

## 1. "¿Cómo usas la IA para escribir código?" — la pregunta central de este proceso

La uso, y prefiero decirlo derecho antes de que me lo pregunten en una revisión de código.

La uso **como consulta**: para entender un concepto que no domino, contrastar dos enfoques posibles, recordar una sintaxis o desatascarme frente a un error que no reconozco. Es el mismo rol que tenían antes la documentación, Stack Overflow y un colega con más horas de vuelo en ese lenguaje.

No la uso **como autor**. El código que entrego lo escribo yo, y puedo explicar cada línea: qué hace, por qué está ahí en vez de otra alternativa, qué efectos tiene sobre el resto del sistema y cómo la probé antes de entregarla. No pego lo que devuelve una herramienta. Hay una razón práctica además de la profesional: en un sistema de facturación con cientos de usuarios activos y lógica de negocio acumulada durante años, el código pegado sin entender es exactamente cómo se rompe la producción — y quien tiene que explicar la caída soy yo, no la herramienta.

Después de quince años leyendo y depurando código ajeno, lo que aporto no es velocidad de tecleo: es el criterio de saber dónde se va a romper algo, qué efecto colateral tiene un cambio en una rutina que otros llaman, y cuándo la solución "rápida" deja una deuda que se paga en tres meses. Ese criterio no lo genera un asistente, y en una revisión de código se nota de inmediato quién lo tiene.

---

## 2. "¿Tienes experiencia con .NET Framework 4.x y Web Forms?"

No a nivel laboral, y no voy a decir que sí. Conozco .NET, C# y Web Forms de forma autodidacta y puntual, sin proyectos productivos.

Lo que sí tengo son quince años de desarrollo web **server-side** en Java —Struts, JSP, Spring Boot MVC—, que comparte el modelo mental de Web Forms: ciclo de vida de página, controles y estado manejados en el servidor, postback y renderizado del lado del servidor. Es otro lenguaje, no lo mismo, y la curva de C# y del framework existe. Mi apuesta es que sobre un sistema de facturación en mantención, con lógica de negocio compleja y SQL Server detrás, lo escaso no es la sintaxis de C# sino saber leer un sistema grande sin romperlo — y eso sí lo traigo.

Si para ustedes ese gap es descalificante, es una decisión razonable y la respeto.

---

## 3. "¿Qué tan avanzado es tu SQL Server?"

Sólido, con un matiz que prefiero declarar: mi mayor profundidad en procedimientos almacenados, planes de ejecución y tuning está en **Oracle PL/SQL y PostgreSQL**, no en T-SQL.

En SQL Server trabajé ocho años en Portal Inmobiliario (2008–2016): consultas de negocio, personalización de documentos y reportería con SQL Server Reporting Services sobre el modelo de datos de la empresa; y lo usé también en banca (Santander/Isban), donde además hice la migración de una base financiera de Sybase a Oracle.

Traducido a esta vacante: escribir y depurar stored procedures, leer un plan de ejecución, encontrar la consulta que está costando y corregirla es trabajo que hago hace años; lo que me tomará algunas semanas es la familiaridad fina con las herramientas y particularidades de T-SQL, no el concepto.

---

## 4. "¿Experiencia en sistemas de facturación o sector salud?" (deseables del aviso)

Ambos, y en el mismo cruce que hace Qulane:

- **Facturación:** tres años en Nubox Facturación Electrónica (2014–2017), plataforma con usuarios activos en Chile y Colombia, incluida su reportería contable; y facturación electrónica bancaria en Santander/Isban.
- **Salud:** diseñé, construí y mantuve el Sistema de Gestión en Salud del Hospital Cruz del Norte (Seven IT SpA, 2017–2020) para medicina, enfermería y kinesiología, con su **módulo de gestión de pagos** e informes administrativos en PDF. Antes de eso fui responsable de la Ficha Clínica del mismo hospital (2016–2017).
- **APIs de pago:** integré Transbank (Webpay) y Khipu en una plataforma en producción — checkout, confirmación y conciliación —, y antes trabajé Medios de Pago y Tarjetas de Crédito en banca.

---

## 5. "¿Por qué un perfil de 15+ años postula a un part-time?"

Porque me acomoda el formato, no porque no encuentre otra cosa. Veinte horas semanales con horario flexible me permiten comprometerme de verdad con este sistema en vez de repartirme mal. Y el tipo de trabajo —mantención y evolución de un sistema con años de lógica acumulada— es exactamente donde la experiencia rinde más: entender antes de tocar, corregir sin efectos colaterales, dejar el código más claro que como lo encontré.

Sobre la seniority: no vengo a rediseñar su arquitectura ni a proponerles migrar nada. Vengo a mantener y evolucionar lo que tienen, que es lo que pide el aviso.

---

## 6. Disponibilidad, horario y condiciones

- **Jornada:** 20 horas semanales, sin problema.
- **Horario EST/Pacific:** vivo en Chile (GMT-4). Estoy a **una hora de diferencia con EST**, así que la superposición para reuniones y comunicación es natural, no forzada.
- **Modalidad:** 100% remoto, con experiencia real de trabajo remoto autónomo desde 2016.
- **Renta:** USD $1.500/mes fijos por 20 horas es la condición publicada y la acepto como está.
- **Formato:** postulo como persona natural, no como agencia ni equipo.
- **Conectividad:** internet estable; equipo propio disponible además del que provee la empresa.
- **Idioma:** español nativo; inglés B2 si en algún momento se requiere para comunicación escrita con Canadá.

---

## 7. "Cuéntanos sobre tu experiencia y perfil profesional" (máx. 2.000 caracteres)

> **1988 caracteres con espacios.** Pegar tal cual; respeta el límite del campo.

Llevo más de 15 años desarrollando y, sobre todo, manteniendo sistemas con lógica de negocio acumulada y usuarios reales en producción: 17 años en banca (Santander/Isban) atendiendo Préstamos, Medios de Pago, Cuentas Corrientes y Tarjetas de Crédito, con facturación electrónica y la migración de plataforma de AS/400 a Java.

Su negocio —facturación para el sector salud— es donde más cruce tengo. En Nubox Facturación Electrónica (2014–2017) trabajé la plataforma y su reportería contable para Chile y Colombia, con las vistas escritas en JavaScript y jQuery. En Seven IT SpA (2017–2020) diseñé, construí y mantuve el Sistema de Gestión en Salud del Hospital Cruz del Norte, incluido su módulo de gestión de pagos e informes administrativos, liderando a 4 desarrolladores. En Portal Inmobiliario (2008–2016) pasé ocho años sobre SQL Server y SSRS: consultas de negocio, documentos y reportería. También integré pasarelas de pago (Transbank Webpay, Khipu) de punta a punta.

Prefiero declarar lo que no tengo: mi experiencia productiva no es en .NET Framework, lo conozco a nivel autodidacta, no laboral. Mis quince años de web server-side son en Java (Struts/JSP, Spring Boot): mismo modelo mental de ciclo de vida de página y estado en el servidor, otro lenguaje. Y en bases de datos mi profundidad en stored procedures y tuning es mayor en Oracle PL/SQL y PostgreSQL que en T-SQL. Si eso me deja fuera, lo entiendo.

Sobre la IA, porque su aviso lo pide explícito: la uso y no lo escondo, pero como consulta, no como autor. La consulto para entender un concepto o desatascar una duda; el código lo escribo yo y puedo explicar cada línea —qué hace, por qué está ahí, qué efectos tiene y cómo la probé—. No pego lo que devuelve una herramienta: en un sistema de facturación con cientos de usuarios activos, eso es exactamente cómo se rompe la producción. Lo que aporto tras quince años leyendo código ajeno no es velocidad de tecleo, es saber dónde se va a romper algo antes de tocarlo.

---

## 8. "¿Por qué te interesa trabajar en Qulane?"

### Versión completa (1642 caracteres)

Por el negocio, antes que por el cargo. Qulane hace software médico y de facturación para el sector salud, y ese cruce es donde pasé buena parte de mi carrera: tres años en Nubox Facturación Electrónica y tres más construyendo y manteniendo el Sistema de Gestión en Salud del Hospital Cruz del Norte, con su módulo de pagos y su reportería administrativa. No tendría que aprender el negocio desde cero: sé lo que es una prestación mal cargada, un cobro que no cuadra, un informe que el área administrativa necesita cerrado el día 1.

Segundo, por el tipo de trabajo. El aviso habla de mantener y evolucionar un sistema con cientos de usuarios activos, bases grandes y lógica de negocio acumulada. Eso no es lo que más se ofrece —casi todo es empezar algo nuevo—, y es justamente donde quince años rinden más: entender antes de tocar, corregir sin efectos colaterales y dejar el código más claro de como lo encontré.

Tercero, y no es un detalle menor: por cómo escribieron el aviso. Dejar por escrito que el código lo escribe la persona y que hay que poder explicar cada línea dice algo del estándar interno del equipo. Es exactamente cómo trabajo, y prefiero un equipo que se tome esa discusión en serio antes que uno que mida entregas por velocidad. Que además sea remoto, con horario flexible y sin micromanagement, encaja con cómo trabajo desde 2016; y desde Chile estoy a una hora de EST, así que la coordinación con Canadá es cómoda.

Por último, el formato part-time con posibilidad de crecer según desempeño me parece la manera correcta de partir: que la decisión de darme más horas la tomen viendo código entregado, no leyendo un CV.

### Versión corta, si el campo es acotado (816 caracteres)

Qulane hace facturación y software para el sector salud, que es donde pasé buena parte de mi carrera: Nubox Facturación Electrónica y el Sistema de Gestión en Salud del Hospital Cruz del Norte, con su módulo de pagos. No tendría que aprender el negocio desde cero.

Me interesa además el tipo de trabajo: mantener y evolucionar un sistema vivo, con usuarios y lógica acumulada, es donde quince años de oficio rinden más —entender antes de tocar y corregir sin romper nada alrededor.

Y me interesa cómo escribieron el aviso: dejar por escrito que el código lo escribe la persona y que hay que poder explicar cada línea dice algo del estándar del equipo. Es exactamente cómo trabajo. El part-time con crecimiento según desempeño me parece la forma correcta de partir: que la decisión la tomen viendo código entregado.

> **Nota:** todo lo anterior es verificable y específico de Qulane. Evitar el relleno genérico ("empresa innovadora", "me encantaría crecer con ustedes"): con un empleador que redactó ese aviso, el elogio vacío resta.

---

## 9. Frases a NO usar en este proceso

- "Experiencia sólida en .NET Framework" o cualquier variante que sugiera experiencia laboral en .NET → **falso**.
- "SQL Server avanzado" sin el matiz de Oracle/PostgreSQL → **medio verdadero, se declara completo**.
- "No uso IA" → **falso, y además contraproducente**: el aviso no prohíbe la IA, prohíbe delegarle la autoría. Negarla suena a respuesta ensayada.
- "Entity Framework" → sin experiencia; el equivalente real es Hibernate/JPA.
