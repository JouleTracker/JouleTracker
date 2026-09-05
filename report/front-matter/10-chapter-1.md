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

| Datos | Descripción | Foto |
|-------|-------------|------|
| **Nombre:** Miguel Angel Jara Espinoza<br>**Carrera:** Ingeniería de Software<br>**Código:** U202512856 | Me llamo Miguel y soy un estudiante de la carrera de Ingeniería de Software actualmente cursando el quinto ciclo. Me considero una persona atenta y paciente. Cuento con conocimientos básicos en JavaScript, Python y C++, los cuales me permiten contribuir en el desarrollo y resolución de problemas dentro del proyecto. | <img src="../images/members/miguel.jpg" alt="Miguel Angel Jara Espinoza" width="500" /> |
| **Nombre:** Miguel Angel Vidal Castro<br>**Carrera:** Ingeniería de Software<br>**Código:** U202314186 | Me llamo Miguel Angel Vidal Castro y soy estudiante de la carrera de Ingeniería de Software. Cuento con conocimientos en gestión de proyectos y optimización de procesos, que me permiten contribuir en la planificación, organización y seguimiento de las actividades del equipo. Me interesa la mejora continua y la búsqueda de soluciones eficientes para optimizar recursos y procesos. Dentro del proyecto, aporto principalmente en la coordinación de tareas, gestión de recursos y organización del trabajo, buscando que las actividades se desarrollen de manera ordenada y eficiente. | <img width="500" alt="Miguel Angel Vidal Castro" src="../images/members/vidal.jpg" /> |
|**Nombre:** Alejandro Samir Choquehuanca Vasquez<br>**Carrera:** Ingeniería de Software<br>**Código:** U202420249 | Me llamo Alejandro Samir, pertenesco a la carrera de ingenieria de software, actualmente estoy en el 5to ciclo, estoy más enfocado en el desarrollo mobile y tratando de aprender y entender los diferentes lenguajes. Tengo conocimientos en Python, C++, Javascript, Html, Css, trabajo con diferentes herramientas como: visualStudio, Git Hub, Git. Me considero una persona trabajadora, responsable y con ganas de siguir aprendiendo | <img src="../images/members/alejandrosamir.jpeg" alt="Alejandro-logo" width="500" /> |
|**Nombre:** Mijail Alexander Matihues Quevedo<br>**Carrera:** Ingeniería de Software<br>**Código:** U202413533 | Me llamo Mijail soy un estudiante de la carrera de Ingeniería de Software. Actualmente estoy cursando el 5to ciclo. Tengo conocimientos de Python, C++, JavaScript, HTML, Css. Me considero una persona responsable y atenta con ganas de contribuir y ayudar en el desarrollo del proyecto. | mas tarde pongo pongo mi foto  |

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

### 1.2.2 Lean UX Process

#### 1.2.2.1 Lean UX Problem Statements


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

- Creemos que un dashboard interactivo con actualización en tiempo real permitirá a los usuarios comprender inmediatamente la carga energética activa generada por los sensores IoT en su inmueble.
- Creemos que una herramienta de proyección de facturación mensual en moneda local eliminará la incertidumbre de los usuarios frente al cobro final de su recibo eléctrico.
- Creemos que un sistema de alertas preventivas configurables ante umbrales y consumos anómalos facilitará la detección rápida de fugas eléctricas o equipos encendidos fuera de horario.
- Creemos que un módulo de analítica histórica y tendencias de consumo permitirá a los usuarios identificar electrodomésticos y maquinarias ineficientes para adoptar medidas correctivas de ahorro.

#### 1.2.2.3 Lean UX Hypothesis Statements

Hypothesis Statement 01

**Creemos** que permitir a los usuarios monitoreen su consumo eléctrico en tiempo real, podrán tomar decisiones sobre el uso de la energía en el momento oportuno y evitar consumos innecesarios.

**Sabremos** que hemos tenido éxisto

**Cuando** al menos el 80% de los usuarios activos consulte el monitoreo de consumo eléctronico en tiempo real al menos una vez por semana durante los primeros 3 meses de uso.

Hypothesis Statement 02

**Creemos** que proporcionar a los usuarios una proyección del costo de su facturación eléctrica les permitirá anticipar sus gastos y tomar medidas para evitar sobrecostos.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 75% de los usuarios consulte la proyección de su facturación durante cada ciclo de consumo durante los primeros 3 meses de uso.

Hypothesis Statement 03

**Creemos** que implementar un sistema de detección de anomalías permitirá a los usuarios identificar oportunamente picos inusuales de consumo, posibles fugas eléctricas o comportamientos anormales de sus equipos.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 70% de las anomalías detectadas por VoltLab sean revisadas por los usuarios durante los primeros 6 meses de uso.

Hypothesis Statement 04

**Creemos** que implementar alertas preventivas sobre consumos elevados y anomalías permitirá a los usuarios actuar oportunamente y reducir el riesgo de sobrecostos en su facturación eléctrica.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 70% de las alertas preventivas generadas por VoltLab sean visualizadas por los usuarios durante los primeros 3 meses de uso.

Hypothesis Statement 05

**Creemos** que integrar sensores IoT con la plataforma VoltLab permitirá automatizar la recopilación de datos energéticos y proporcionar información continua sobre el consumo eléctrico.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 90% de las mediciones generadas por los dispositivos IoT sean registradas correctamente en VoltLab durante los primeros 3 meses de funcionamiento.

Hypothesis Statement 06

**Creemos** que proporcionar un historial del consumo eléctrico permitirá a los usuarios comparar sus patrones de consumo e identificar cambios que puedan generar mayores costos.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 70% de los usuarios consulte su historial de consumo y realice al menos una comparación entre diferentes periodos durante los primeros 3 meses de uso.

Hypothesis Statement 07

**Creemos** que proporcionar una visualización centralizada de las métricas energéticas permitirá a los usuarios comprender con mayor facilidad su comportamiento de consumo y tomar decisiones informadas.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 80% de los usuarios utilice las visualizaciones de consumo de VoltLab durante los primeros 3 meses de uso.

Hypothesis Statement 08

**Creemos** que centralizar el monitoreo, las proyecciones de costos, las anomalías y las alertas en una sola plataforma permitirá a los usuarios gestionar su consumo eléctrico de manera más eficiente y reducir gastos innecesarios.

**Sabremos** que hemos tenido éxito

**Cuando** al menos el 75% de los usuarios utilice dos o más funcionalidades de VoltLab de manera recurrente durante los primeros 3 meses de uso.

#### 1.2.2.4 Lean UX Canvas

#### 1.2.2.4. Lean UX Canvas.

| 1. Businesses Problem | 5. Solutions | 2. Businesses Outcomes |
|-----------------------|--------------|-------------------------|
| Actualmente, los hogares y pequeños negocios tienen dificultades para controlar eficientemente su consumo eléctrico debido a la falta de herramientas tecnológicas accesibles que permitan visualizar el consumo en tiempo real. Los usuarios dependen principalmente del recibo de electricidad al finalizar el periodo de facturación, lo que dificulta detectar oportunamente consumos excesivos, fugas eléctricas, equipos defectuosos o picos anómalos de demanda. Esta falta de visibilidad genera sobrecostos, decisiones de consumo basadas en estimaciones tardías y una gestión energética reactiva. | VoltLab es una plataforma web que integra dispositivos IoT de medición inteligente para monitorear el consumo eléctrico en tiempo real. La solución centraliza los datos energéticos y los presenta mediante indicadores y gráficos fáciles de interpretar, permitiendo a los usuarios conocer su consumo, proyectar costos de facturación y detectar comportamientos anómalos. Además, la plataforma genera alertas preventivas ante consumos elevados o situaciones inusuales, ayudando a los usuarios a tomar decisiones oportunas para reducir gastos y mejorar la eficiencia energética. <br><br>Características clave:<br>- Monitoreo del consumo eléctrico en tiempo real mediante sensores IoT<br>- Visualización de métricas de consumo mediante gráficos e indicadores<br>- Proyección del costo de la facturación eléctrica<br>- Detección de consumos anómalos y picos de demanda<br>- Alertas preventivas ante comportamientos inusuales<br>- Historial de consumo para analizar tendencias<br>- Identificación de patrones de consumo para promover hábitos eficientes<br>- Plataforma web accesible desde diferentes dispositivos<br>- Arquitectura distribuida y procesamiento de datos en la nube | Sabremos que estamos resolviendo el problema cuando los hogares y pequeños negocios utilicen VoltLab de manera constante para monitorear y gestionar su consumo eléctrico. Buscamos que los usuarios obtengan mayor visibilidad sobre sus gastos energéticos, puedan identificar oportunamente consumos anómalos y reduzcan sus costos mediante decisiones informadas. Como resultados esperados, se plantea alcanzar una reducción del consumo eléctrico de entre 10% y 20% en los usuarios que adopten medidas de eficiencia, disminuir los sobrecostos ocasionados por consumos inesperados y mejorar la capacidad de los usuarios para anticipar el monto de su facturación mensual. |

| 3. Users |
|----------|
| Nos enfocaremos inicialmente en dos segmentos principales: (1) jefes de hogar que desean controlar y reducir el gasto mensual de electricidad, identificar qué artefactos generan mayor consumo y detectar anomalías en su instalación eléctrica; y (2) propietarios o administradores de pequeños negocios, como bodegas, cafeterías, panaderías y talleres, que necesitan controlar sus costos operativos y garantizar la continuidad de sus actividades. Estos usuarios requieren una solución accesible e intuitiva que les permita comprender sus patrones de consumo sin necesidad de conocimientos técnicos especializados. |

| 4. User Outcomes & Benefits |
|-----------------------------|
| Los usuarios buscan VoltLab para obtener visibilidad y control sobre su consumo eléctrico, evitando depender únicamente del recibo mensual para conocer sus gastos. Los jefes de hogar podrán identificar qué equipos consumen mayor cantidad de energía, recibir alertas ante comportamientos anómalos y tomar decisiones para reducir su factura. Los propietarios de pequeños negocios podrán controlar uno de sus principales costos operativos, proyectar sus gastos energéticos y detectar oportunamente posibles fallas o consumos excesivos. Como cambio de comportamiento, esperamos que los usuarios pasen de una gestión energética reactiva a una gestión preventiva, revisando periódicamente sus indicadores, modificando hábitos de consumo y actuando ante las alertas generadas por la plataforma. |

| 6. Hypotheses |
|----------------|
| - Creemos que los hogares y pequeños negocios utilizarán regularmente VoltLab si pueden visualizar su consumo eléctrico en tiempo real mediante una interfaz web sencilla e intuitiva.<br>- Creemos que los usuarios podrán reducir su consumo eléctrico entre 10% y 20% si reciben información clara sobre sus patrones de consumo y alertas ante comportamientos anómalos.<br>- Creemos que la proyección del costo de facturación permitirá a los usuarios anticipar sus gastos mensuales y tomar decisiones oportunas para evitar sobrecostos.<br>- Creemos que las alertas preventivas ayudarán a los usuarios a detectar oportunamente picos de consumo, posibles fugas eléctricas o equipos con comportamientos inusuales.<br>- Creemos que los propietarios de pequeños negocios adoptarán la solución si pueden utilizarla sin requerir conocimientos técnicos especializados y si el ahorro potencial justifica el costo de implementación de los dispositivos IoT.<br>- Creemos que la integración de sensores IoT con una plataforma web permitirá generar información más útil para la toma de decisiones que el uso exclusivo del recibo mensual de electricidad. |

| 7. What's the most important thing we need to learn first? | 8. What's the least amount of work we need to do to learn the next most important thing? |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ¿Realmente los hogares y pequeños negocios utilizarán una plataforma que les muestre su consumo eléctrico en tiempo real y tomarán decisiones a partir de esta información? También necesitamos validar si consideran suficientemente valiosas las funciones de monitoreo, proyección de costos y alertas preventivas como para adoptar la solución. | Validar el interés y comportamiento de los usuarios sin construir inicialmente toda la infraestructura IoT y la plataforma completa:<br><br>- Prototipo interactivo: Crear un mockup navegable de VoltLab que simule el dashboard, gráficos de consumo, proyección de costos y alertas.<br>- Simulación de datos IoT: Utilizar datos de consumo simulados para mostrar cómo funcionaría el monitoreo en tiempo real.<br>- Prueba con usuarios: Presentar el prototipo a jefes de hogar y propietarios de pequeños negocios y observar si comprenden los indicadores y qué acciones tomarían ante diferentes escenarios de consumo.<br>- Encuesta y entrevistas: Recopilar información sobre sus principales dificultades con el consumo eléctrico, disposición a utilizar sensores IoT y valor percibido de las funciones propuestas.<br>- Landing page: Crear una página informativa que explique la propuesta de VoltLab y permita medir el interés de potenciales usuarios mediante un registro o formulario. | 


## 1.3 Segmentos Objetivo

VoltLab está dirigido a dos segmentos principales de usuarios que comparten la necesidad de monitorear y controlar su consumo eléctrico de manera más eficiente:

- **Hogares urbanos con consumo eléctrico medio-alto:** Familias y propietarios de vivienda interesados en reducir su gasto en electricidad, que buscan herramientas accesibles para entender en qué momentos y con qué dispositivos consumen más energía, y así tomar decisiones informadas sobre su uso.

- **Pequeños negocios (PYMEs):** Emprendedores y administradores de pequeños comercios (bodegas, restaurantes, talleres, oficinas pequeñas) que necesitan controlar sus costos operativos y evitar sobrecostos por consumo eléctrico ineficiente, así como detectar anomalías (picos de consumo, fugas energéticas) que puedan indicar fallas en equipos.

Ambos segmentos comparten un perfil común: buscan una solución tecnológica intuitiva, de bajo costo de implementación, que no requiera conocimientos técnicos avanzados, y que les brinde visibilidad en tiempo real sobre su consumo energético para tomar decisiones que impacten directamente en su ahorro económico.

[^1]: Organismo Supervisor de la Inversión en Energía y Minería (Osinergmin). (2023). Guía de orientación sobre el uso eficiente y seguro de la energía eléctrica. https://www.gob.pe/osinergmin

[^2]: Al-Khatib, W., Al-Ghamdi, A. S., & Khan, M. A. (2021). IoT-based smart energy monitoring and management system for residential and small commercial buildings. Sustainable Energy Technologies and Assessments, 47, Article 101416. https://doi.org/10.1016/j.seta.2021.101416

[^3]: International Energy Agency (IEA). (2023). Energy Efficiency 2023: Analysis and key findings. https://www.iea.org/reports/energy-efficiency-2023

[^4]: Instituto Nacional de Estadística e Informática (INEI). (2024). Comportamiento de la economía peruana e índices de actividad comercial y de servicios. https://www.inei.gob.pe/prensa/noticias/
