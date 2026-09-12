# Capítulo I: Introducción
## 1.1. Startup Profile
### 1.1.1. Descripción de la Startup

Somos VoltLab, un equipo de estudiantes apasionados por la innovación tecnológica y el desarrollo de soluciones digitales de la Universidad Peruana de Ciencias Aplicadas. Nuestra startup está enfocada en transformar la gestión y supervisión del consumo eléctrico tanto en hogares como en pequeños negocios mediante el aprovechamiento de la tecnología IoT y plataformas web distribuidas. A través de nuestra plataforma, conectamos dispositivos de medición inteligente con un sistema centralizado que permite monitorear el flujo energético en tiempo real, proyectar costos de facturación, identificar anomalías de consumo y automatizar alertas preventivas para evitar sobrecostos.

- **Misión:** Empoderar a los hogares y propietarios de pequeños negocios mediante herramientas tecnológicas accesibles e intuitivas que les permitan medir, entender y controlar su consumo eléctrico en tiempo real, fomentando hábitos de uso eficiente y garantizando un ahorro económico tangible y sostenible.

- **Visión:** Consolidarnos como una plataforma SaaS referente en la gestión energética inteligente a nivel regional, promoviendo una cultura de consumo responsable y optimización de recursos mediante la integración de hardware abierto y análisis de datos en la nube.

- **Valores:**
  - Sostenibilidad: Fomentamos el uso responsable de los recursos energéticos para mitigar el impacto ambiental y reducir costos innecesarios.
  - Transparencia: Proporcionamos datos claros, medibles y en tiempo real para que los usuarios comprendan con precisión su gasto energético.
  - Innovación: Integramos telemetría IoT y arquitecturas web modernas para resolver problemas reales de monitoreo y control.
  - Accesibilidad: Diseñamos soluciones intuitivas, inclusivas y adaptables a diversos tipos de usuarios y capacidades de infraestructura.
  - Confiabilidad: Garantizamos precisión en las lecturas de telemetría y consistencia en el procesamiento y entrega de información crítica.

### 1.1.2. Perfiles de integrantes del equipo

| Datos | Descripción | Foto                                                                                      |
|-------|-------------|-------------------------------------------------------------------------------------------|
| **Nombre:** Miguel Angel Jara Espinoza<br>**Carrera:** Ingeniería de Software<br>**Código:** U202512856 | Me llamo Miguel y soy un estudiante de la carrera de Ingeniería de Software actualmente cursando el quinto ciclo. Me considero una persona atenta y paciente. Cuento con conocimientos básicos en JavaScript, Python y C++, los cuales me permiten contribuir en el desarrollo y resolución de problemas dentro del proyecto. | <img src="../images/members/miguel.jpg" alt="Miguel Angel Jara Espinoza" width="500" />   |
| **Nombre:** Miguel Angel Vidal Castro<br>**Carrera:** Ingeniería de Software<br>**Código:** U202314186 | Me llamo Miguel Angel Vidal Castro y soy estudiante de la carrera de Ingeniería de Software. Cuento con conocimientos en gestión de proyectos y optimización de procesos, que me permiten contribuir en la planificación, organización y seguimiento de las actividades del equipo. Me interesa la mejora continua y la búsqueda de soluciones eficientes para optimizar recursos y procesos. Dentro del proyecto, aporto principalmente en la coordinación de tareas, gestión de recursos y organización del trabajo, buscando que las actividades se desarrollen de manera ordenada y eficiente. | <img width="500" alt="Miguel Angel Vidal Castro" src="../images/members/vidal.jpg" />     |
| **Nombre:** Alejandro Samir Choquehuanca Vasquez<br>**Carrera:** Ingeniería de Software<br>**Código:** U202420249 | Me llamo Alejandro Samir, pertenesco a la carrera de ingenieria de software, actualmente estoy en el 5to ciclo, estoy más enfocado en el desarrollo mobile y tratando de aprender y entender los diferentes lenguajes. Tengo conocimientos en Python, C++, Javascript, Html, Css, trabajo con diferentes herramientas como: visualStudio, Git Hub, Git. Me considero una persona trabajadora, responsable y con ganas de siguir aprendiendo | <img src="../images/members/alejandrosamir.jpeg" alt="Alejandro-logo" width="500" />      |
| **Nombre:** Mijail Alexander Matihues Quevedo<br>**Carrera:** Ingeniería de Software<br>**Código:** U202413533 | Me llamo Mijail soy un estudiante de la carrera de Ingeniería de Software. Actualmente estoy cursando el 5to ciclo. Tengo conocimientos de Python, C++, JavaScript, HTML, Css. Me considero una persona responsable y atenta con ganas de contribuir y ayudar en el desarrollo del proyecto. | Más tarde se agregará la foto.                                                            |
| **Nombre:** Rodrigo Velasquez Velasquez<br>**Carrera:** Ingeniería de Software<br>**Código:** U202222074 | Me llamo Rodrigo y soy estudiante de la carrera de Ingeniería de Software, actualmente cursando el quinto ciclo. Tengo conocimientos en Java, Python, C++, JavaScript, bases de datos, Git y GitHub. También he trabajado con herramientas como Docker y MongoDB. Me considero una persona responsable, comprometida y con disposición para seguir aprendiendo y aportar en el desarrollo del proyecto. | <img src="../images/members/rodrigo.png" alt="Rodrigo Velasquez Velasquez" width="500" /> |
## 1.2. Solution Profile
### 1.2.1.  Antecedentes y problemática
Los hogares y pequeños negocios enfrentan constantes dificultades en el control eficiente de su gasto energético debido a la falta de herramientas tecnológicas accesibles que integren telemetría y monitoreo de consumo en tiempo real. Esta situación genera pérdidas económicas imprevistas por facturación excesiva, decisiones de consumo a ciegas basadas en estimaciones tardías y una notable incapacidad para detectar fugas eléctricas, equipos defectuosos o picos anómalos de demanda a lo largo del mes. Por otro lado, la interacción con las empresas distribuidoras de energía suele ser unidireccional y reactiva, entregando únicamente un recibo consolidado al finalizar el ciclo de facturación, lo que impide a los usuarios corregir sus patrones de consumo de manera oportuna. Existe la necesidad de una solución de software distribuida que permita centralizar la captura de datos energéticos mediante sensores IoT, procesar métricas de consumo en tiempo real, proyectar costos y automatizar alertas preventivas, facilitando la toma de decisiones informadas y promoviendo una cultura de eficiencia y sostenibilidad económica.

<h4>5W + 2H</h4>

- **¿Qué ocurre? (WHAT):** Los usuarios residenciales y propietarios de pequeños negocios carecen de visibilidad inmediata sobre su consumo eléctrico diario. Esto se refleja en la incapacidad de rastrear qué artefactos o maquinarias demandan mayor carga, descontrol en el presupuesto mensual y fallas en la detección temprana de anomalías en la red eléctrica interna. Según Osinergmin (2023) [^1], las variaciones tarifarias y la falta de supervisión continua impactan directamente en el presupuesto familiar y comercial, requiriendo un uso más racional de la energía. Además, la integración de sistemas IoT para la gestión de energía aún presenta brechas de adopción por la complejidad y el alto costo de las soluciones industriales tradicionales (Al-Khatib et al., 2021) [^2].

- **¿Quiénes se ven afectados? (WHO):** El problema afecta principalmente a los jefes de hogar y administradores de pequeños negocios (bodegas, cafeterías, panaderías, talleres), quienes deben asumir costos fijos elevados con márgenes operativos ajustados. También impacta a las comunidades locales y al medio ambiente, dado que el consumo ineficiente sobrecarga las redes de distribución y acelera la huella de carbono asociada a la generación energética innecesaria (IEA, 2023) [^3].

- **¿Dónde ocurre? (WHERE):** Esta problemática se presenta en viviendas urbanas, comercios minoristas y establecimientos de servicios, especialmente en contextos donde la infraestructura eléctrica interna presenta desgaste o falta de mantenimiento. En el contexto nacional, esto resulta crítico debido al crecimiento del sector comercial y de servicios registrado por el INEI (2024) [^4], donde miles de micro y pequeñas empresas operan bajo presupuestos ajustados y una alta dependencia del suministro eléctrico continuo sin herramientas de medición interna.

- **¿Cuándo ocurre? (WHEN):** El consumo ocurre de manera ininterrumpida, pero la problemática se agudiza en temporadas de altas temperaturas (por el uso intensivo de refrigeración y aire acondicionado), durante horas punta del sistema eléctrico y en periodos de alta demanda comercial (campañas estacionales, fines de semana y horarios nocturnos).

- **¿Por qué es importante resolverlo? (WHY):** Resolver este problema es fundamental para evitar el endeudamiento de los hogares y mejorar la rentabilidad de las microempresas mediante la reducción de costos operativos evitables. La incorporación de dispositivos IoT y plataformas web distribuidas permite monitorear variables de consumo en tiempo real, anticipar sobrecostos y reaccionar de forma inmediata ante consumos anómalos o fugas eléctricas (Al-Khatib et al., 2021) [^2].

- **¿Cómo se manifiesta? (HOW):** El problema se evidencia en recibos de luz con montos inesperados, reclamos frecuentes ante las empresas de suministro, desgaste prematuro de electrodomésticos y equipos por sobrecarga, y una conducta reactiva de los usuarios, quienes intentan ahorrar energía reduciendo actividades esenciales sin conocer el impacto real de cada aparato. Como señalan Al-Khatib et al. (2021) [^2], la falta de retroalimentación en tiempo real limita el aprendizaje de hábitos de consumo eficiente.

- **¿Cuánto impacta? (HOW MUCH):** El impacto es tangible tanto a nivel económico como operativo. Según la IEA (2023) [^3], la adopción de medidas de eficiencia energética y retroalimentación directa al consumidor puede generar reducciones en el consumo eléctrico de entre un 10% y un 20% anual. En el entorno local, el INEI (2024) [^4] reporta un dinamismo constante en el sector comercial, donde la energía eléctrica representa uno de los costos fijos más significativos. La falta de visibilidad y control preventivo genera sobrecostos constantes que debilitan la liquidez de los pequeños comercios y desestabilizan la economía doméstica.

## 1.2.2 Lean UX Process

#### 1.2.2.1 Lean UX Problem Statements

El estado actual de la gestión y monitoreo del consumo eléctrico se ha enfocado principalmente en hogares urbanos y pequeños negocios mediante un flujo de facturación mensual netamente reactivo, donde los usuarios enfrentan cobros inesperados, carecen de visibilidad sobre qué dispositivos o maquinarias generan picos de carga, y asumen pérdidas económicas por fugas eléctricas sin poder detectarlas a tiempo.

Lo que los productos y servicios existentes no logran abordar es la falta de información accesible en tiempo real y la desconexión tecnológica, dejando a los consumidores sin herramientas preventivas que desglosen su gasto antes del cierre del ciclo de facturación.

Nuestro producto, JouleTracker, abordará esta brecha mediante una plataforma SaaS que integra dispositivos de telemetría IoT para centralizar el monitoreo del flujo energético en tiempo real, proyectar los costos de facturación y automatizar alertas preventivas ante umbrales de sobre consumo o anomalías.

Nuestro enfoque inicial serán los jefes de hogar de zonas urbanas con consumos medio-altos y los propietarios o administradores de micro y pequeñas empresas (PYMEs) que buscan proteger sus márgenes operativos.

Sabremos que tenemos éxito cuando veamos que los usuarios interactúan frecuentemente con los dashboards y alertas, logrando una tasa de retención mensual superior al 65%, una conversión del 15% en la landing page, y que al menos el 8% de los pequeños negocios migren exitosamente a planes de suscripción de pago tras comprobar la optimización de sus costos.

#### 1.2.2.2 Lean UX Assumptions
**Business Assumptions**

- Creemos que existe un mercado creciente y desatendido de hogares urbanos y pequeños negocios dispuestos a adoptar soluciones digitales para optimizar su gasto en servicios básicos.
- Creemos que un modelo de negocio SaaS bajo esquema Freemium (con acceso básico gratuito para hogares y planes de suscripción mensual para pequeños negocios con soporte multidispositivo) es financieramente sostenible y escalable.
- Creemos que el costo de adquisición de hardware IoT y el desarrollo de software open-source permiten mantener márgenes operativos rentables para la comercialización de la plataforma.
- Creemos que VoltLab puede diferenciarse de las empresas tradicionales de suministro eléctrico al ofrecer una experiencia de usuario transparente, preventiva y centrada en la reducción del consumo, en lugar de actuar únicamente como un ente emisor de cobros.

**Business Outcomes Assumptions**

- Creemos que VoltLab aumentará el valor de vida del cliente si los pequeños negocios perciben un retorno de inversión claro frente al costo de su plan de suscripción.
- Creemos que alcanzaremos una tasa de conversión del 15% en la landing page si la propuesta de valor comunica claramente el ahorro potencial de energía.
- Creemos que mantendremos una tasa de retención mensual superior al 65% si los usuarios configuran al menos dos alertas de umbral de consumo durante su primera semana.
- Creemos que lograremos que el 8% de los usuarios de pequeños negocios migren a un plan de pago si acceden a reportes analíticos avanzados de predicción de gasto.
- Creemos que reduciremos la tasa de cancelación por debajo del 5% trimestral ofreciendo integración continua y confiable con los sensores IoT de medición eléctrica.



**Users Assumptions**

- Creemos que nuestros usuarios principales son jefes de hogar de zonas urbanas que gestionan el presupuesto familiar y buscan herramientas digitales para optimizar el gasto de servicios básicos.
- Creemos que los administradores y dueños de micro y pequeñas empresas (bodegas, cafeterías, talleres) necesitan supervisar el consumo eléctrico continuo de sus maquinarias para proteger sus márgenes de ganancia.
- Creemos que ambos segmentos de usuarios interactúan frecuentemente con navegadores web desde computadoras de escritorio o dispositivos móviles, pero carecen de conocimientos técnicos sobre telemetría o magnitudes eléctricas complejas.
- Creemos que los propietarios de pequeños negocios tienen mayor disposición a delegar o compartir la visualización de métricas de consumo con socios o encargados de turno.
- Creemos que los jefes de hogar priorizan la rapidez de configuración y la simplicidad visual por encima de reportes analíticos densos.



**Users Outcomes and Benefit Assumptions**

- Creemos que los jefes de hogar lograrán tranquilidad económica al conocer la proyección estimada de su recibo de luz en tiempo real antes del cierre de facturación.
- Creemos que los dueños de pequeños negocios protegerán sus márgenes operativos al identificar oportunamente consumos pasivos y maquinarias que funcionan de forma ineficiente fuera del horario comercial.
- Creemos que los usuarios transicionarán de un comportamiento reactivo a una gestión energética preventiva al recibir alertas instantáneas cuando se detecten patrones anómalos o fugas eléctricas.
- Creemos que los usuarios residenciales y comerciales adoptarán hábitos de uso responsable si cuentan con comparativas históricas comprensibles que no dependan de terminología técnica compleja.
- Creemos que ambos segmentos evitarán sobrecostos mensuales imprevistos al poder configurar y respetar umbrales presupuestales personalizados dentro de la plataforma.


**Feature Assumptions**

- Creemos que la integración automatizada de sensores IoT permitirá a los usuarios recopilar datos energéticos continuos sin necesidad de realizar registros manuales.
- Creemos que un dashboard interactivo en tiempo real permitirá a los usuarios comprender inmediatamente la carga energética activa en su inmueble.
- Creemos que una herramienta de proyección de facturación mensual en moneda local eliminará la incertidumbre de los usuarios frente al cobro final de su empresa eléctrica.
- Creemos que un módulo de analítica histórica y tendencias de consumo permitirá a los usuarios identificar hábitos ineficientes a lo largo del tiempo.
- Creemos que un sistema de alertas preventivas configurables facilitará la detección rápida de fugas eléctricas o equipos encendidos por accidente.
- Creemos que permitir agrupar sensores por áreas específicas (ej. cocina, refrigeración) ayudará a los pequeños negocios a identificar sus mayores fuentes de gasto.

### 1.2.2.3 Lean UX Hypothesis Statements

Hypothesis Statement 01

**Creemos** que integrar sensores IoT automatizados para la ingesta de datos logrará que los usuarios confíen en la precisión y continuidad de la plataforma.

**Sabremos** que hemos tenido éxisto

**Cuando** al menos el 90% de los sensores vinculados mantenga una transmisión continua sin caídas reportadas por más de 7 días durante los primeros meses de uso.

Hypothesis Statement 02

**Creemos** que proporcionar un dashboard de monitoreo en tiempo real logrará que los usuarios identifiquen picos inusuales de energía de manera inmediata.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 80% de los usuarios activos consulte su dashboard al menos dos veces por semana.

Hypothesis Statement 03

**Creemos** que mostrar una proyección estimada del costo mensual logrará que los usuarios planifiquen mejor su presupuesto familiar o comercial.

**Sabremos** que hemos tenido éxito

**Cuando** el 75% de los usuarios revise su proyección económica antes de los últimos 5 días del cierre de su ciclo de facturación.

Hypothesis Statement 04

**Creemos** proporcionar gráficos de analítica histórica logrará que los usuarios reconozcan y corrijan patrones de consumo ineficientes.

**Sabremos** que hemos tenido éxito

**Cuando** más del 70% de los usuarios utilice los filtros de fechas para comparar su consumo respecto al mes anterior.

Hypothesis Statement 05

**Creemos** que implementar alertas preventivas sobre umbrales de consumo logrará que los usuarios reaccionen a tiempo y reduzcan sobrecostos operativos.

**Sabremos** que hemos tenido éxito

**Cuando** el 60% de los usuarios configure al menos un límite de consumo mensual y el 70% visualice las notificaciones generadas.

Hypothesis Statement 06

**Creemos** que segmentar el monitoreo por áreas de negocio logrará que los dueños de PYMEs identifiquen maquinarias específicas que consumen demasiada energía.

**Sabremos** que hemos tenido éxito

**Cuando** el 80% de los usuarios del segmento comercial asigne sus sensores a más de un área estructurada dentro de la plataforma.

### 1.2.2.4. Lean UX Canvas


| 1. Business Problem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 5. Solution Ideas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2. Business Outcomes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| El estado actual de la gestión del consumo eléctrico se enfoca en un flujo de facturación mensual reactivo, donde los usuarios enfrentan cobros inesperados y asumen pérdidas por fugas sin poder detectarlas a tiempo. Los servicios existentes no logran abordar la falta de información en tiempo real, dejando a los consumidores sin herramientas preventivas. Nuestro producto, JouleTracker, abordará esta brecha mediante una plataforma SaaS que integra telemetría IoT para centralizar el monitoreo continuo, proyectar costos y automatizar alertas preventivas, enfocándose inicialmente en jefes de hogar y administradores de PYMEs.                                                                                                                                                                          | 1. Integración de Hardware IoT: Automatización de la ingesta de datos energéticos mediante sensores inteligentes para garantizar lecturas continuas.<br> 2. Dashboard en Tiempo Real: Interfaz visual para comprender inmediatamente la carga energética activa en el inmueble. <br> 3. Proyector de Costo Mensual: Herramienta de estimación económica en moneda local para anticipar la facturación. <br> 4. Analítica e Historial Comparativo: Gráficos con filtros de fechas para comparar consumos pasados e identificar hábitos ineficientes. <br> 5. Alertas Preventivas y Límites: Sistema de notificaciones automáticas frente a sobreconsumos o picos anómalos. <br> 6. Segmentación Comercial (MYPEs): Funcionalidad para agrupar sensores por áreas específicas de un negocio (ej. cocina, refrigeración) e identificar fuentes de gasto.  <br> | • Alcanzar una tasa de retención mensual superior al 65%.<br><br>• Obtener una tasa de conversión del 15% mediante la Landing Page.<br><br>• Lograr que al menos el 8% de los pequeños negocios migren de un plan Freemium a un plan de pago.<br><br>• Mantener una tasa de cancelación trimestral inferior al 5%.<br><br>• Incrementar progresivamente la adopción y uso recurrente de JouleTracker.                                                                                                                                                       |
| **3. Users**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **7. Most Important Learning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **4. User Outcomes & Benefits**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Jefes de hogar</b><br>Personas responsables de administrar el presupuesto familiar y pagar los servicios eléctricos de viviendas urbanas. Buscan reducir gastos y comprender mejor su consumo de energía.<br><br><b>Propietarios y administradores de pequeños negocios</b><br>Responsables de bodegas, cafeterías, panaderías, talleres y otros pequeños establecimientos que necesitan controlar sus costos eléctricos y detectar consumos anormales.                                                                                                                                                                                                                                                                                                                                                                      | ¿Los hogares y pequeños negocios utilizarán realmente una plataforma que les permita visualizar su consumo eléctrico en tiempo real y tomar decisiones basándose en esta información?<br><br>También necesitamos validar si consideran suficientemente valiosas las funciones de monitoreo, proyección de costos y alertas preventivas como para adoptar JouleTracker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Previsibilidad del gasto</b><br>Conocer anticipadamente el costo aproximado del recibo eléctrico.<br><br><b>Ahorro económico</b><br>Identificar consumos innecesarios y equipos que utilizan energía de manera ineficiente.<br><br><b>Detección temprana</b><br>Identificar fugas, picos de consumo o equipos funcionando fuera de horarios habituales.<br><br><b>Gestión preventiva</b><br>Tomar acciones antes de que llegue el recibo mensual.<br><br><b>Mayor control</b><br>Comprender los patrones de consumo mediante información clara y accesible. |
| **6. Hypotheses**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **8. Least Effort to Learn**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - Creemos que la integración de sensores IoT logrará que los usuarios confíen en la precisión y continuidad de la plataforma.<br> - Creemos que el dashboard en tiempo real logrará que los usuarios identifiquen picos inusuales de energía de manera inmediata.<br> - Creemos que mostrar una proyección de costos logrará que los usuarios planifiquen mejor su presupuesto familiar o comercial.<br> - Creemos que proporcionar gráficos históricos logrará que los usuarios reconozcan y corrijan patrones de consumo ineficientes.<br> - Creemos que las alertas preventivas sobre umbrales lograrán que los usuarios reaccionen a tiempo y reduzcan sobrecostos operativos.<br> - Creemos que segmentar el monitoreo por áreas de negocio logrará que las PYMEs identifiquen maquinarias específicas de alto consumo. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | • Crear un prototipo interactivo del dashboard.<br><br>• Utilizar datos simulados de consumo eléctrico en tiempo real.<br><br>• Presentar el prototipo a jefes de hogar y propietarios de pequeños negocios.<br><br>• Realizar pruebas de usabilidad, entrevistas y encuestas.<br><br>• Evaluar si los usuarios comprenden los indicadores y toman decisiones utilizando la información presentada.<br><br>• Crear una Landing Page para medir el interés de potenciales usuarios.                                                                          |



## 1.3 Segmentos Objetivo

VoltLab está dirigido a dos segmentos principales de usuarios que comparten la necesidad de monitorear y controlar su consumo eléctrico de manera más eficiente:

- **Hogares urbanos con consumo eléctrico medio-alto:** Familias y propietarios de vivienda interesados en reducir su gasto en electricidad, que buscan herramientas accesibles para entender en qué momentos y con qué dispositivos consumen más energía, y así tomar decisiones informadas sobre su uso.

- **Pequeños negocios (PYMEs):** Emprendedores y administradores de pequeños comercios (bodegas, restaurantes, talleres, oficinas pequeñas) que necesitan controlar sus costos operativos y evitar sobrecostos por consumo eléctrico ineficiente, así como detectar anomalías (picos de consumo, fugas energéticas) que puedan indicar fallas en equipos.

Ambos segmentos comparten un perfil común: buscan una solución tecnológica intuitiva, de bajo costo de implementación, que no requiera conocimientos técnicos avanzados, y que les brinde visibilidad en tiempo real sobre su consumo energético para tomar decisiones que impacten directamente en su ahorro económico.

[^1]: Organismo Supervisor de la Inversión en Energía y Minería (Osinergmin). (2023). Guía de orientación sobre el uso eficiente y seguro de la energía eléctrica. https://www.gob.pe/osinergmin

[^2]: Al-Khatib, W., Al-Ghamdi, A. S., & Khan, M. A. (2021). IoT-based smart energy monitoring and management system for residential and small commercial buildings. Sustainable Energy Technologies and Assessments, 47, Article 101416. https://doi.org/10.1016/j.seta.2021.101416

[^3]: International Energy Agency (IEA). (2023). Energy Efficiency 2023: Analysis and key findings. https://www.iea.org/reports/energy-efficiency-2023

[^4]: Instituto Nacional de Estadística e Informática (INEI). (2024). Comportamiento de la economía peruana e índices de actividad comercial y de servicios. https://www.inei.gob.pe/prensa/noticias/
