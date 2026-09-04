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
| Datos                                                                                                  | Descripción                                                                                                                                                                                                         | Foto                                                                    |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
|**Nombre:** Miguel Angel Jara Espinoza<br>**Carrera:** Ingeniería de Software<br>**Código:** U202512856 | Me llamo Miguel y soy un estudiante de la carrera de Ingeniería de Software actualmente cursando el quinto ciclo. Me considero una persona atenta y paciente. Con conocimientos básicos en javascript, python y c++.|<img src="../images/members/miguel.jpg" alt="Miguel-logo" width="500" /> |

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


#### 1.2.2.3 Lean UX Hypothesis Statements

#### 1.2.2.4 Lean UX Canvas

# Lean UX Canvas

## 1.3 Segmentos Objetivo

[^1]: Organismo Supervisor de la Inversión en Energía y Minería (Osinergmin). (2023). Guía de orientación sobre el uso eficiente y seguro de la energía eléctrica. https://www.gob.pe/osinergmin

[^2]: Al-Khatib, W., Al-Ghamdi, A. S., & Khan, M. A. (2021). IoT-based smart energy monitoring and management system for residential and small commercial buildings. Sustainable Energy Technologies and Assessments, 47, Article 101416. https://doi.org/10.1016/j.seta.2021.101416

[^3]: International Energy Agency (IEA). (2023). Energy Efficiency 2023: Analysis and key findings. https://www.iea.org/reports/energy-efficiency-2023

[^4]: Instituto Nacional de Estadística e Informática (INEI). (2024). Comportamiento de la economía peruana e índices de actividad comercial y de servicios. https://www.inei.gob.pe/prensa/noticias/
