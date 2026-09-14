# Capítulo IV: Product Design

## 4.1. Style Guidelines

### 4.1.1. General Style Guidelines

#### Tipografía

En JouleTracker se utilizan dos tipografías que permiten establecer una jerarquía visual clara y mantener una experiencia de lectura cómoda.

**Inter** se utiliza en títulos y encabezados debido a su apariencia moderna, limpia y profesional. Su diseño permite destacar las secciones principales y facilitar la identificación de la información más importante.

Para los textos generales se utiliza **Roboto**, una tipografía ampliamente utilizada en interfaces digitales por su buena legibilidad en diferentes tamaños de pantalla. Se aplica principalmente en párrafos, descripciones, etiquetas y contenido informativo.

La combinación de ambas tipografías permite diferenciar los encabezados del contenido general, generando una estructura visual ordenada y consistente a lo largo de la plataforma.

**Figura 1:**  
Uso de la tipografía "Inter" en encabezados.

![Inter](../images/typography/inter.png)


**Fuente:** [Google Fonts - Inter](https://www.1001fonts.com/inter-font.html)

**Figura 2:**  
Uso de la tipografía "Roboto" en textos generales.

![Roboto](../images/typography/roboto.png)

**Fuente:** [Google Fonts - Roboto.](https://www.1001fonts.com/roboto-font.html)

#### Colores principales

La elección de colores en JouleTracker busca transmitir una identidad tecnológica, moderna y relacionada con la eficiencia energética.

![Colors](../images/colors/colors.png)

El color azul **#0066FF** se establece como color principal y se utiliza para acciones importantes, botones, enlaces y elementos seleccionados. Este color permite destacar las acciones principales y facilita la identificación de los elementos interactivos.

El color verde **#10B981** funciona como color secundario y se utiliza para representar estados positivos, eficiencia y resultados favorables dentro de la plataforma.

El color ámbar **#F59E0B** corresponde al color terciario y se utiliza principalmente para advertencias o situaciones que requieren atención.

Por último, el color **#0F172A** funciona como color neutral y se emplea principalmente en títulos, textos principales y otros elementos que requieren un alto nivel de contraste.

En conjunto, esta paleta permite establecer una jerarquía visual clara y utilizar los colores de manera semántica para comunicar diferentes estados de la aplicación.

#### Estilo visual

El estilo visual de JouleTracker busca mantener una interfaz limpia, moderna y enfocada en la información.

La combinación del azul principal **#0066FF** con el verde **#10B981** permite destacar acciones y estados positivos, mientras que el ámbar **#F59E0B** se reserva para situaciones de advertencia.

El color **#0F172A** proporciona contraste para títulos y textos importantes. Los fondos claros permiten que los contenidos sean fáciles de identificar y evitan una interfaz visualmente saturada.

Los componentes utilizan formas simples y bordes suavemente redondeados para mantener una apariencia moderna. Las tarjetas y bloques de información permiten agrupar contenidos relacionados y mejorar la organización visual.

#### Interactividad

Los elementos interactivos de JouleTracker proporcionan retroalimentación visual para indicar al usuario cuándo un elemento puede ser seleccionado, cuándo se encuentra activo o cuándo una acción ha sido realizada.

Los botones principales utilizan el color **#0066FF** y pueden presentar una variación de tono durante estados como `hover` o `active`.

Los elementos seleccionados mantienen una diferenciación visual respecto al resto de opciones para facilitar la orientación dentro de la interfaz.

Las tarjetas y componentes interactivos pueden utilizar cambios sutiles de elevación o sombra al pasar el cursor, proporcionando feedback inmediato sin generar distracciones.

Las transiciones son suaves y breves, buscando que las interacciones sean naturales y no interfieran con la comprensión de la información.

---

### 4.1.2. Web Style Guidelines

#### Responsividad

El diseño de JouleTracker está orientado a diferentes tamaños de pantalla, permitiendo adaptar la interfaz desde dispositivos móviles hasta computadoras de escritorio.

Los elementos se reorganizan de acuerdo con el espacio disponible, pasando de estructuras horizontales a verticales cuando es necesario. También se ajustan los tamaños, márgenes y espacios para mantener una correcta legibilidad.

La aplicación de principios responsive permite que las principales funcionalidades puedan utilizarse independientemente del dispositivo desde el cual se acceda a la plataforma.

#### Componentes

Los componentes mantienen un estilo visual consistente mediante el uso de la misma tipografía, colores y reglas de espaciado.

Los botones utilizan principalmente el color **#0066FF** para las acciones principales, mientras que las acciones secundarias pueden utilizar estilos neutros.

Las tarjetas permiten organizar información relacionada y presentar datos de manera diferenciada. Los indicadores pueden utilizar los colores semánticos definidos en la paleta para representar estados positivos o situaciones que requieren atención.

Esta consistencia facilita el reconocimiento de patrones y permite que el usuario comprenda rápidamente el propósito de cada elemento.

#### Accesibilidad

Se prioriza un contraste adecuado entre textos y fondos para facilitar la lectura.

El color **#0F172A** se utiliza principalmente para textos sobre fondos claros, mientras que los colores de los elementos interactivos deben mantener suficiente contraste para poder ser identificados fácilmente.

Además, los elementos interactivos deben ser accesibles mediante teclado y presentar estados de `focus` visibles.

Se utilizan etiquetas descriptivas y una estructura semántica adecuada para facilitar la interpretación de la interfaz mediante tecnologías de asistencia.

#### Animaciones suaves

Las interacciones utilizan transiciones sutiles para proporcionar retroalimentación sin sobrecargar visualmente la interfaz.

Entre los efectos considerados se encuentran:

- Cambio de color en botones.
- Modificación visual de los elementos seleccionados.
- Elevación ligera de tarjetas durante el estado `hover`.
- Transiciones suaves entre estados.

Estas animaciones tienen como objetivo mejorar la experiencia de usuario y proporcionar una respuesta visual clara ante las acciones realizadas.

---

## 4.2. Information Architecture

La arquitectura de información de JouleTracker organiza los contenidos y funcionalidades de la plataforma de manera que los usuarios puedan acceder fácilmente a la información relacionada con el consumo energético.

La estructura diferencia entre el contenido informativo de la Landing Page y las funcionalidades propias de la aplicación web.

La Landing Page presenta el propósito y las principales características de JouleTracker, mientras que la aplicación concentra las funciones relacionadas con la consulta y gestión de información energética.

Esta separación permite que cada espacio responda a diferentes necesidades: informar a nuevos usuarios en la Landing Page y facilitar la gestión de información a los usuarios de la aplicación.

### 4.2.1. Organization Systems

#### Jerárquico

La estructura de JouleTracker sigue un sistema jerárquico en el que la **Landing Page** funciona como punto principal de acceso a la plataforma. Desde esta página, el usuario puede conocer el propósito de JouleTracker, revisar sus principales funcionalidades y acceder a la aplicación web.

La información se presenta de manera progresiva, comenzando con una introducción general de la plataforma y continuando con las características y funcionalidades que ofrece. Finalmente, el usuario puede dirigirse hacia la aplicación para interactuar directamente con sus herramientas.

Dentro de la aplicación web, el **Dashboard** funciona como punto central desde el cual el usuario puede acceder a las diferentes funcionalidades relacionadas con el monitoreo y gestión del consumo energético.

Esta organización permite que la información fluya de lo general a lo particular, facilitando la comprensión y exploración de la plataforma.

#### Modular y Seccional

La información de JouleTracker se encuentra organizada en diferentes secciones y módulos, cada uno enfocado en una función o tipo de contenido específico.

En la Landing Page, las secciones presentan de manera ordenada la información principal de la plataforma, sus características y los beneficios que ofrece. En la aplicación web, los módulos permiten organizar las funcionalidades relacionadas con el consumo energético y la gestión de la información.

Esta organización modular permite mantener una interfaz limpia y enfocada, evitando presentar toda la información en un único espacio. Además, facilita la incorporación de nuevas funcionalidades y permite que cada módulo pueda evolucionar sin afectar la estructura general de la plataforma.

### 4.2.2. Labeling Systems

#### Menú principal

Las etiquetas utilizadas en la navegación de JouleTracker son directas y permiten identificar fácilmente las principales secciones de la plataforma.

En la Landing Page se utilizan etiquetas orientadas a presentar el proyecto y sus funcionalidades, mientras que dentro de la aplicación se emplean nombres relacionados con la gestión y monitoreo del consumo energético.

El uso de etiquetas claras permite que el usuario pueda comprender qué contenido o funcionalidad encontrará al seleccionar cada opción, reduciendo la confusión durante la navegación.

#### Botones de acción

Los botones utilizan etiquetas breves y orientadas a la acción, permitiendo que el usuario comprenda rápidamente qué ocurrirá al interactuar con ellos.

Se utilizan expresiones como **"Get Started"**, **"Learn More"**, **"Add Device"**, **"View Details"** y **"Save"**, dependiendo de la acción correspondiente.

El uso de verbos facilita la toma de decisiones y proporciona una relación clara entre el texto del botón y la acción que ejecutará el sistema.

#### Formularios

Los campos de los formularios utilizan etiquetas sencillas y descriptivas para indicar la información que debe ingresar el usuario.

Se consideran etiquetas como **"Name"**, **"Email"**, **"Password"**, **"Device Name"** y **"Device Type"**.

Esta nomenclatura permite que los usuarios comprendan fácilmente qué información deben proporcionar y reduce la posibilidad de errores durante el ingreso de datos.


### 4.2.3. SEO Tags and Meta Tags

JouleTracker debe incorporar metaetiquetas básicas que permitan identificar correctamente el contenido de la Landing Page, mejorar su presentación en los motores de búsqueda y garantizar una correcta visualización en diferentes dispositivos.

**Título:** La etiqueta `title` define el nombre de la página que aparece en la pestaña del navegador. También permite identificar de manera clara el contenido principal del sitio.

    <title>JouleTracker | Monitoreo del consumo energético</title>

**Descripción:** La meta descripción proporciona un resumen breve del propósito de JouleTracker. Esta información puede utilizarse para presentar una descripción del sitio en los resultados de búsqueda.

    <meta
      name="description"
      content="JouleTracker permite monitorear y analizar el consumo energético para mejorar el uso eficiente de la energía."
    >

**Palabras clave:** El contenido de la plataforma utiliza términos relacionados con su propósito, como **consumo energético**, **monitoreo energético**, **eficiencia energética**, **energy monitoring** y **energy tracking**. Estas palabras ayudan a mantener una relación temática clara entre el contenido del sitio y su objetivo.

**Viewport:** La etiqueta viewport permite adaptar correctamente el contenido de la página al tamaño de pantalla del dispositivo, siendo fundamental para el diseño responsive.

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

**Robots:** Para las páginas públicas se puede utilizar la directiva `index, follow`, permitiendo que los motores de búsqueda indexen el contenido y sigan los enlaces disponibles.

    <meta name="robots" content="index, follow">

### 4.2.4. Searching Systems

La Landing Page de JouleTracker no requiere un sistema de búsqueda global, debido a que la información se encuentra distribuida en secciones específicas y puede ser consultada mediante la navegación principal.

En la aplicación web, un sistema de búsqueda puede ser útil para localizar rápidamente información cuando aumente la cantidad de dispositivos, registros o datos relacionados con el consumo energético.

Esta funcionalidad podría implementarse mediante un campo de búsqueda acompañado de filtros que permitan reducir los resultados según criterios como dispositivo, fecha, periodo o estado.

Actualmente, si esta funcionalidad no se encuentra implementada, se puede considerar como una mejora para futuras versiones de JouleTracker, especialmente para facilitar la consulta de grandes cantidades de información.

### 4.2.5. Navigation Systems

#### Navegación superior

La navegación principal de JouleTracker se encuentra ubicada en la parte superior de la Landing Page, permitiendo acceder directamente a las diferentes secciones informativas.

Esta ubicación facilita el acceso a la información principal y permite que el usuario pueda desplazarse por la página de manera rápida y sencilla.

Dentro de la aplicación web, la navegación permite acceder al Dashboard y a las diferentes funcionalidades relacionadas con el monitoreo energético.

#### Flujo lógico

El recorrido del usuario sigue una estructura progresiva que comienza en la Landing Page y continúa hacia la aplicación web.

El usuario puede conocer primero el propósito de JouleTracker, revisar sus funcionalidades y posteriormente acceder a la plataforma para utilizar sus herramientas.

El flujo general parte de la presentación de la plataforma, continúa con la exploración de sus características y termina con el acceso al Dashboard, desde donde se pueden consultar las funcionalidades principales.

Esta organización permite mantener un recorrido intuitivo y evita pasos innecesarios durante la interacción.

#### Navegación dentro de la aplicación

El **Dashboard** funciona como uno de los principales puntos de navegación dentro de la aplicación web.

Desde este espacio, el usuario puede acceder a las funcionalidades relacionadas con los dispositivos, el consumo energético y la información disponible en la plataforma.

La sección actualmente seleccionada debe diferenciarse visualmente mediante el color principal **#0066FF**, permitiendo que el usuario reconozca fácilmente dónde se encuentra dentro de la aplicación.

#### Footer con navegación secundaria

El footer complementa la navegación principal proporcionando acceso a información adicional relacionada con JouleTracker.

Puede incluir enlaces hacia información del proyecto, contacto, políticas, términos y otros recursos relevantes.

De esta manera, el menú principal puede mantenerse enfocado en las funcionalidades y secciones más importantes, mientras que el footer concentra enlaces secundarios.

#### Estructura modular

La navegación mantiene una estructura modular que permite incorporar nuevas secciones y funcionalidades conforme evolucione JouleTracker.

Esta organización facilita la escalabilidad de la plataforma, ya que nuevos módulos pueden incorporarse siguiendo los mismos patrones de navegación sin afectar significativamente la estructura existente.

Además, mantener una estructura consistente permite que los usuarios puedan familiarizarse rápidamente con nuevas funcionalidades a medida que estas sean incorporadas.


## 4.3. Landing Page UI Design.

La interfaz del Landing Page de JouleTracker busca comunicar de forma directa el problema que resolvemos y cómo lo resolvemos, sin que el usuario tenga que pensar mucho para entenderlo. La idea principal es que cualquier persona que entre a la página, ya sea un jefe de hogar o el dueño de un pequeño negocio, entienda en los primeros segundos que puede monitorear su consumo eléctrico en tiempo real y evitar sorpresas en su recibo de luz.

Para lograr esto, ordenamos el contenido de forma progresiva: primero captamos la atención con el mensaje principal y el llamado a la acción, luego mostramos las funcionalidades clave, después explicamos paso a paso cómo funciona la plataforma, y finalmente reforzamos la confianza del usuario con la sección "Nosotros" y los testimonios, antes de invitarlo a registrarse o escribirnos. Con esta estructura evitamos que el usuario se pierda navegando o se sature de información antes de entender el valor real del producto.

A nivel visual, todavía estamos en la etapa de wireframe, por lo que la interfaz se trabajó en escala de grises para enfocarnos en la jerarquía de la información y el orden de lectura, dejando la definición de colores, tipografía y demás elementos de identidad para la siguiente etapa del diseño. Aun así, se buscó que la distribución en bloques y el espaciado entre secciones dieran una sensación clara y ordenada, tanto en escritorio como en versión móvil.

## 4.3.1. Landing Page Wireframe.

Los wireframes del Landing Page de JouleTracker representan la primera versión estructurada de la página, antes de pensar en colores o estilos. Nos sirvieron para definir qué bloques debía tener la página, en qué orden mostrarlos y qué tan visible debía quedar cada elemento importante, como el mensaje principal o los botones de acción. Esta etapa nos permitió validar que la información clave apareciera desde el primer momento y que el recorrido del usuario tuviera sentido antes de invertir tiempo en el diseño final.

**Desktop**

En la versión desktop, el wireframe prioriza una hero section amplia con el mensaje "Tu consumo eléctrico bajo control", acompañada del botón "Comenzar gratis" y una navegación superior fija con acceso directo a cada sección. A partir de la cabecera, el contenido se organiza en bloques horizontales que muestran las funcionalidades clave de la plataforma, el funcionamiento en 4 pasos, una vista previa del panel de control, la sección "Nosotros" y los testimonios de usuarios, cerrando con un bloque de contacto. Esta distribución aprovecha el ancho completo de la pantalla y permite que el usuario recorra la página de forma escaneable, sin perder de vista el mensaje principal.

<img src="../images/figma/JouleTrackerWireframe I (desktop).png" alt="Wireframe desktop del Landing Page" width="700" />

El primer contacto del usuario con la parte funcional de JouleTracker ocurre en el flujo de autenticación. Aquí buscamos que iniciar sesión o recuperar el acceso a la cuenta sea rápido y no genere fricción, ya que es el paso previo a que la persona pueda ver su consumo eléctrico. Por eso mantuvimos el mismo header del resto del sitio, y acompañamos el formulario con un mensaje que recuerda el beneficio principal de la plataforma ("Gestiona tu energía desde cualquier lugar"), para que el usuario no pierda de vista por qué está ahí.

<img src="../images/figma/JouleTrackerWirframe 1.1.png" alt="Wireframe de Iniciar sesión" width="700" />
<img src="../images/figma/JouleTrackerWireframe 1.2.png" alt="Recuperar contraseña" width="700" />

**Si el usuario no tiene cuenta** 
Se puede registrar de una forma rapida, sencilla y segura.
<img src="../images/figma/JouleTrackerWireframe 2.1.png" alt="Wireframe de registro" width="700" />

Una vez que el usuario decide crear una cuenta, lo acompañamos en tres pasos: completar sus datos, verificar su correo y confirmar que todo salió bien. Dividimos este proceso en pantallas separadas en lugar de un solo formulario largo, para que se sienta más liviano y el usuario sepa siempre en qué parte del proceso está. En el registro reforzamos por qué vale la pena unirse (fácil de usar, datos seguros, impacto real), y cerramos con una confirmación clara de que la cuenta ya está lista para usarse.

<img src="../images/figma/JouleTrackerWireframe 2.2.png" alt="Wireframe de verificación" width="700" />

<img src="../images/figma/JouleTrackerWireframe 2.3.png" alt="Wireframe de registro exitoso" width="700" />


**Mobile**

En la versión mobile, la estructura se reorganiza en una sola columna, priorizando el mensaje principal y el botón "Comenzar gratis" para que sean lo primero que vea el usuario. La navegación se compacta en un menú hamburguesa para no ocupar espacio innecesario en la pantalla, y las secciones (funcionalidades, cómo funciona, nosotros, testimonios y contacto) se apilan una debajo de otra en el mismo orden que en desktop. Así mantenemos la misma lógica de lectura, pero adaptada a una pantalla más pequeña y a una navegación táctil.
<img src="../images/figma/JouleTrackerWireframe(mobile) 1.2.png" alt="Wireframe de inicio" width="700" />

<img src="../images/figma/JouleTrackerWireframe(mobile) 1.1.png" alt="Wireframe de tu energía" width="700" /> 

<img src="../images/figma/JouleTrackerWireframe(mobile) 2.2.png" alt="Wireframe de funcionalidades" width="700" />

<img src="../images/figma/JouleTrackerWireframe(mobile) 2.1.png" alt="Wireframe de todo en un solo lugar" width="700" />

<img src="../images/figma/JouleTrackerWireframe(mobile) 3.2.png" alt="Wireframe de opción de como funciona" width="700" />

<img src="../images/figma/JouleTrackerWireframe(mobile) 3.1.png" alt="Wireframe de como funciona" width="700" />

En la versión mobile del flujo de autenticación, simplificamos cada pantalla a lo esencial: un solo formulario visible a la vez, sin distracciones, para que iniciar sesión o crear una cuenta desde el celular se sienta tan rápido como hacerlo desde una laptop. Mantuvimos las mismas opciones de acceso rápido (Google, Apple, Facebook, Instagram) y los mismos pasos del registro (crear cuenta, verificar correo, confirmación), pero apilados en una sola columna y con botones más grandes, pensados para el dedo y no para el cursor.

<img src="../images/figma/JouleTrackerWireframe(mobile) 6.1.png" alt="Wireframe mobile de Iniciar sesión" width="700" />

<img src="../images/figma/JouleTrackerWireframe(mobile) 6.2.png" alt="Wireframe mobile de Recuperar contraseña" width="700" />

<img src="../images/figma/JouleTrackerWireframe(mobile) 6.3.png" alt="Wireframe mobile de Recuperar contraseña" width="700" />

**Crear cuenta**

<img src="../images/figma/JouleTrackerWireframe(mobile) 7.1.png" alt="Wireframe mobile de Recuperar contraseña" width="700" />
<img src="../images/figma/JouleTrackerWireframe(mobile) 7.2.png" alt="Wireframe mobile de Recuperar contraseña" width="700" />
<img src="../images/figma/JouleTrackerWireframe(mobile) 7.3.png" alt="Wireframe mobile de Recuperar contraseña" width="700" />

## 4.3.2. Landing Page Mock-up.

Los mock-ups finales del Landing Page de JouleTracker representan la consolidación visual de todo lo planteado en los wireframes. En esta etapa incorporamos la paleta cromática de la marca, basada en tonos verdes junto con blanco y negro, para transmitir la idea de sostenibilidad, energía limpia y confianza que buscamos asociar con el producto. También se sumaron íconos, imágenes reales de dispositivos y espacios del hogar, y elementos decorativos como hojas, que refuerzan visualmente el concepto de eficiencia energética.

**Desktop**

En el mock-up desktop se evidencia una jerarquía visual clara, reforzada mediante el uso del verde institucional en botones, íconos y puntos de énfasis, combinado con fondos claros y bloques bien espaciados. La hero section destaca la propuesta de valor de JouleTracker acompañada de una imagen del dashboard en un laptop, dando una idea concreta del producto desde el primer momento. Las secciones posteriores mantienen la misma lógica del wireframe (funcionalidades, cómo funciona, vista previa de la plataforma, nosotros, testimonios y contacto), pero ahora con imágenes reales, íconos ilustrativos y una paleta consistente que facilita la comprensión rápida del producto.

<img src="../images/figma/JouleTrackerMockap(desktop).png" alt="Mock-up desktop del Landing Page" width="700" />

**Iniciar sesion**

<img src="../images/figma/JouleTrackerMockap(desktop) 1.1.png" alt="Mock-up desktop del Landing Page" width="700" />
<img src="../images/figma/JouleTrackerMockap(desktop) 1.2.png" alt="Mock-up desktop del Landing Page" width="700" />

**Registro**

<img src="../images/figma/JouleTrackerMockap(desktop) 2.1.png" alt="Mock-up desktop del Landing Page" width="700" />
<img src="../images/figma/JouleTrackerMockap(desktop) 2.2.png" alt="Mock-up desktop del Landing Page" width="700" />
<img src="../images/figma/JouleTrackerMockap(desktop) 2.3.png" alt="Mock-up desktop del Landing Page" width="700" />


**Mobile**

En la versión mobile del mock-up, la estructura se adapta a pantallas reducidas manteniendo la misma paleta de verdes, tipografía y jerarquía visual que en desktop. La navegación se compacta en un menú desplegable que aparece al tocar el ícono superior, dejando siempre visibles los accesos a Registrarte e Iniciar sesión. Las secciones se apilan en una sola columna: primero el mensaje principal con la imagen del dispositivo móvil, luego las funcionalidades en tarjetas de dos columnas, el paso a paso de "¿Cómo funciona?", la vista previa de la plataforma, la sección "Nosotros" con la misión, visión y equipo, y finalmente el bloque de contacto con los datos de la empresa. Esta adaptación busca que la propuesta de JouleTracker siga siendo clara y fácil de recorrer con el dedo, sin perder la identidad visual definida para desktop.

<img src="../images/figma/JouleTrackerMockap(mobile) 1.1.png" alt="Mock-up mobile del Landing Page" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.2.png" alt="Mock-up mobile de Inicio" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.3.png" alt="Mock-up mobile del menu" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.4.png" alt="Mock-up mobile de funcionalidades" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.5.png" alt="Mock-up mobile de menu" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.6.png" alt="Mock-up mobile de Cómo funciona" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.7.png" alt="Mock-up mobile de menu" width="350" />


<img src="../images/figma/JouleTrackerMockap(mobile) 1.8.png" alt="Mock-up mobile de nosotros" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 1.9.png" alt="Mock-up mobile de menu" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 2.1.png" alt="Mock-up mobile de contacto" width="350" />



**El usuario puede ingresar con su cuenta**

<img src="../images/figma/JouleTrackerMockap(mobile) 2.2.png" alt="Mock-up mobile verifica email." width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 2.3.png" alt="Mock-up mobile del Landing Page" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 2.4.png" alt="Mock-up mobile del Landing Page" width="350" />

**El usuario puede crear su propia cuenta**

<img src="../images/figma/JouleTrackerMockap(mobile) 2.5.png" alt="Mock-up mobile del Landing Page" width="350" />

<img src="../images/figma/JouleTrackerMockap(mobile) 2.6.png" alt="Mock-up mobile del Landing Page" width="350" />

## 4.4. Aplicación Web UX/UI Design.

La propuesta UX/UI del panel interno de JouleTracker está pensada para que el usuario, una vez registrado, entienda de un vistazo cómo va su consumo eléctrico y qué puede hacer al respecto. A partir de esa necesidad, la interfaz prioriza el acceso directo a los módulos más importantes (consumo, dispositivos, alertas, reportes y recomendaciones), la visualización rápida del estado actual mediante métricas clave, y la reducción de pasos para las acciones que el usuario repetirá con más frecuencia, como revisar su gasto del mes o atender una alerta.

### 4.4.1. Aplicación Web Wireframes.

Los wireframes de la aplicación definen la estructura base de las vistas más importantes del panel antes de aplicar el diseño visual final. En ellos se observa la distribución del sidebar de navegación, el header con los datos del usuario, las tarjetas de métricas, los gráficos de consumo y las tablas de detalle. Esta etapa permitió validar que la información más relevante para el usuario (cuánto está consumiendo, cuánto le está costando y qué puede optimizar) estuviera siempre visible, sin importar en qué módulo se encuentre.

**Desktop**

En escritorio, los wireframes muestran una estructura consistente en los siete módulos del panel: un sidebar fijo a la izquierda con acceso a Inicio, Consumo, Dispositivos, Alertas, Reportes, Recomendaciones y Configuración, y un área central que cambia según el módulo seleccionado. En **Inicio** y **Consumo** se prioriza un resumen visual del gasto eléctrico mediante tarjetas de métricas y gráficos de consumo. En **Dispositivos** y **Alertas** el foco pasa a tablas con el detalle de cada dispositivo o notificación. En **Reportes** se organiza la información histórica con filtros y comparativas, mientras que en **Recomendaciones** se muestran tarjetas de sugerencias personalizadas de ahorro. Finalmente, **Configuración** agrupa los datos de la cuenta, del hogar y las preferencias del usuario en bloques independientes. Esta consistencia entre módulos facilita que el usuario aprenda a usar el panel una sola vez y lo aplique en cualquier sección.

<img src="../images/figma/JouleTrackerDashboard(desktop) 1.1.png" alt="Wireframe del Dashboard - Inicio" width="700" />
<img src="../images/figma/JouleTrackerDashboard(desktop) 1.2.png" alt="Wireframe del Dashboard - Consumo" width="700" />
<img src="../images/figma/JouleTrackerDashboard(desktop) 1.3.png" alt="Wireframe del Dashboard - Dispositivos" width="700" />
<img src="../images/figma/JouleTrackerDashboard(desktop) 1.4.png" alt="Wireframe del Dashboard - Alertas" width="700" />
<img src="../images/figma/JouleTrackerDashboard(desktop) 1.5.png" alt="Wireframe del Dashboard - Reportes" width="700" />
<img src="../images/figma/JouleTrackerDashboard(desktop) 1.6.png" alt="Wireframe del Dashboard - Recomendaciones" width="700" />
<img src="../images/figma/JouleTrackerDashboard(desktop) 1.7.png" alt="Wireframe del Dashboard - Configuraciones" width="700" />

**Mobile**

En la versión mobile del Dashboard, la navegación lateral se reemplaza por una barra inferior fija con acceso directo a los módulos más usados (Inicio, Consumo, Dispositivos, Alertas) y un botón "Más" que despliega el resto de opciones (Reportes, Recomendaciones, Configuración, Contacto y Cerrar sesión) en un menú lateral. El contenido de cada módulo se reorganiza en una sola columna, apilando las tarjetas de métricas y los gráficos que en desktop iban en fila, para que toda la información siga siendo legible sin necesidad de hacer scroll horizontal. Las tablas de Dispositivos y Alertas se simplifican a listas verticales con la información esencial de cada fila, y en Configuración los bloques de información personal, hogar, preferencias y notificaciones se apilan uno debajo del otro, manteniendo el mismo criterio de agrupación que en la versión de escritorio.

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.1.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.2.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.3.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.4.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.5.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.6.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.7.png" alt="Wireframe del Dashboard - Inicio" width="700" />

<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.8.png" alt="Wireframe del Dashboard - Inicio" width="700" />


<img src="../images/figma/JouleTrackerDashboard(Mobile) 1.9.png" alt="Wireframe del Dashboard - Inicio" width="700" />








### 4.4.2. Web Applications Wireflow Diagrams

### 4.4.3. Web Applications Mock-ups

### 4.4.4. Web Applications User Flow Diagrams

## 4.5. Web Applications Prototyping

## 4.5. Aplicación Web Prototyping.

La fase de prototipado de JouleTracker nos permitió simular la navegación real de la plataforma antes de pensar en el desarrollo. Con esto validamos que la arquitectura de información, los componentes de interfaz y los flujos que definimos en los wireframes y wireflows realmente tuvieran sentido cuando alguien los recorre de principio a fin, tanto en escritorio como en mobile. Además del prototipo navegable en Figma, dejamos también evidencia en video del recorrido, para mostrar cómo se comporta la interfaz al interactuar con ella.

**Escritorio**

<img src="../images/figma/desktop-prototype.png" alt="desktop-prototype" width="700" />

<a href="https://www.figma.com/proto/I9Hbim3oES3bOynqQrzlHw/JouleTracker_Mockap-II--Desktop-?node-id=24-13&t=ywhOr6HZ8TOlJlUd-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=24%3A13" target="_blank">Ver prototipo en Figma</a>

**Mobile**
<img src="../images/figma/mobile-prototype.png" alt="mobileprototype" width="700" />

<a href="https://www.figma.com/proto/2cOm4G2UT14h4DdrItKjsA/JouleTracker_Mockap_mobile?node-id=2-66&t=e5ma48eTjakvBbnU-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1" target="_blank">Ver prototipo en Figma</a>

**Video prototype**
<a href="https://drive.google.com/file/d/1NVVftMkgkf8UINHr9ddtzFL6ZltgTxzm/view?usp=sharing" target="_blank">Video prototype</a>



## 4.6. Domain-Driven Software Architecture



### 4.6.1. Design-Level Event Storming

En esta sección se detalla el proceso de Design-Level EventStorming realizado por el equipo para perfeccionar el modelo del dominio de JoulTracker. Partiendo del Big Picture, profundizamos en el comportamiento interno del sistema para alcanzar el mayor nivel de detalle arquitectónico posible.

Primero, refinamos la línea de tiempo original, eliminando eventos redundantes o procesos manuales que quedaban fuera del alcance tecnológico de la plataforma. Sobre este flujo depurado, incorporamos los elementos tácticos del Domain-Driven Design: Actores y Comandos para representar las intenciones, Read Models para la interfaz gráfica, Políticas para las reglas automáticas y de negocio, Sistemas Externos, y Agregados (Aggregates) como responsables de procesar las operaciones y emitir los eventos de dominio. Este nivel de granularidad nos permitió consolidar y justificar las fronteras definitivas de nuestros Bounded Contexts.

Bounded Context 1: Identity & Access Management

Este contexto delimitado constituye el núcleo de seguridad y gestión de accesos para los usuarios residenciales y comerciales dentro de la plataforma JoulTracker. Se identificaron entidades clave como Usuario, Credenciales y Sesión, junto con conceptos del lenguaje ubicuo como token y autenticación. A partir de comandos como Register User y Log In, se generan eventos como User registered y User authenticated. Asimismo, se definieron políticas de seguridad automatizadas, como el envío de códigos de verificación tras el registro inicial y el bloqueo preventivo de cuentas tras detectar múltiples intentos fallidos de acceso.

![bounded context 1](../images/design-level-event-storming/bc1.png)


Bounded Context 2: Device & Telemetry Management

Este contexto delimitado centraliza la gestión del hardware IoT y la ingesta física de datos hacia la plataforma. Se identificaron entidades como SensorDevice y Telemetry, junto con conceptos del lenguaje ubicuo como payload y heartbeat. A partir de comandos como Register Sensor y Send Telemetry Data, se generan eventos como Sensor registered y Data received. Se establecieron políticas reactivas críticas para mantener la consistencia del estado del hardware, como la desconexión automática del sensor al detectar un timeout prolongado en la red y su posterior reconexión automática al recuperar la transmisión.

![bounded context 2](../images/design-level-event-storming/bc2.png)

Bounded Context 3: Dashboard & Energy Analytics

Este contexto conforma el núcleo analítico de JoulTracker, responsable de procesar la telemetría y calcular el gasto energético en tiempo real. Se manejan entidades como ConsumptionMetric y TariffPlan, utilizando términos como kilovatio-hora (kWh) y estimación monetaria. Mediante comandos como Calculate Energy Consumption y Calculate Estimated Cost, el sistema emite eventos como Energy consumption calculated y Estimated cost calculated. Las políticas de este contexto aseguran la actualización continua del dashboard cada vez que se ingesta nueva data y la conversión automática del consumo a moneda local según la tarifa vigente configurada.

![bounded context 3](../images/design-level-event-storming/bc3.png)

Bounded Context 4: Profiles & History Management

Este contexto delimitado gestiona la información personal de los usuarios y la consolidación estructurada de sus series temporales de consumo. Destacan entidades como UserProfile e HistoricalLog. A través de comandos como Update User Profile y Filter Consumption History, el sistema dispara eventos como Profile updated y History date range filtered. Una política clave en este módulo es la consolidación diaria automatizada (a través de disparadores de tiempo o cronjobs), que congela y empaqueta las lecturas cada 24 horas para garantizar consultas históricas eficientes sin sobrecargar la base de datos.

![bounded context 4](../images/design-level-event-storming/bc4.png)

Bounded Context 5: Alerting & Energy Optimization

Este contexto es el motor de prevención y optimización energética de la plataforma. Gira en torno a entidades como ConsumptionThreshold y AlertNotification, integrando conceptos como umbral de advertencia y patrón de consumo. A partir de comandos como Set Consumption Limit y Evaluate Consumption Thresholds, se originan eventos como Consumption limit set y Abnormal consumption detected. Sus políticas son altamente reactivas: evalúan cada nuevo registro contra las metas del usuario para despachar notificaciones inmediatas o generar recomendaciones de ahorro de forma automática si se detectan patrones anómalos.

![bounded context 5](../images/design-level-event-storming/bc5.png)

Bounded Context 6: Facility & Small Business Analytics

Este contexto delimitado provee las herramientas avanzadas de estructuración física para el segmento comercial (MYPE). Se identificaron entidades como BusinessArea y conceptos como mapeo de zonas y rendimiento de equipamiento. Comandos como Create Business Area y Compare Areas Consumption desencadenan eventos clave como Business area registered y Area consumption compared. Las políticas de este contexto automatizan la agregación de métricas por zona y alertan sobre consumos atípicos (fugas energéticas o maquinaria encendida por error) cuando los locales comerciales se encuentran fuera de su horario de atención.

![bounded context 6](../images/design-level-event-storming/bc6.png)

Se adjunta el enlance del table de miro con el proceso: [miro](https://miro.com/welcomeonboard/TnpJZmYyak5sRFNiYk9yemozbUJtUjBLZDZyYUpTek9McmxaMk9lM0VlTkFEZy81cU5OWWxrZ0U2Rkp0aUxVbWxMOXhrbDEvNkU5QTE3djZjbDNXb0tKa0EydzdPN20yN3dxUXNXSzdXb1J4ZDJITG5ndnJXN1piUnEyeEJpdEl3VHhHVHd5UWtSM1BidUtUYmxycDRnPT0hdjE=?share_link_id=815831854787)

### 4.6.2. Software Architecture Context Diagram


El Diagrama de Contexto (Nivel 1 del modelo C4) establece las fronteras de JouleTracker, ofreciendo una visión de alto nivel sobre cómo la plataforma se integra dentro de su entorno operativo. Este nivel abstrae los detalles internos de implementación y representa al sistema como una única entidad central, destacando exclusivamente las interacciones con los actores humanos y los sistemas de software o hardware externos.

Para este proyecto, el diagrama detalla la relación entre la plataforma y sus principales usuarios (el Jefe de Hogar y el Administrador de Negocio), evidenciando cómo consumen los servicios de monitoreo energético. Asimismo, ilustra la dependencia crítica con el ecosistema de hardware (Sensores IoT) para la ingesta continua de telemetría en tiempo real. Finalmente, establece los límites de responsabilidad del sistema al delegar procesos operativos clave a servicios de terceros, específicamente la gestión de cobros de suscripciones a la pasarela de pagos (Stripe) y la emisión de notificaciones transaccionales al proveedor de correos (Brevo).

El propósito de esta vista es proporcionar una comprensión clara y no técnica del alcance del sistema, el flujo principal de valor y sus dependencias tecnológicas externas.

![context](../images/Architecture-Diagrams/C4Context.png)

### 4.6.3. Software Architecture Container Diagrams


El Diagrama de Contenedores (Nivel 2 del modelo C4) realiza un acercamiento al sistema central de JouleTracker para revelar su arquitectura de software interna. En este nivel, el sistema se descompone en unidades técnicas de ejecución y despliegue separadas, conocidas como contenedores, mostrando sus responsabilidades específicas, la distribución del trabajo y las decisiones tecnológicas de alto nivel adoptadas por el equipo de desarrollo.

Para la plataforma JouleTracker, el diagrama ilustra una separación arquitectónica clara. Por un lado, se expone la interfaz de usuario a través de una aplicación web interactiva (Single-Page Application) y un sitio promocional (Landing Page), mediante los cuales interactúan los distintos tipos de clientes. Por otro lado, se detalla el núcleo operativo alojado en una Backend API estructurada con Spring Boot, la cual encapsula la lógica de los dominios, y finalmente, el motor de almacenamiento persistente representado por una base de datos relacional.

Adicionalmente, esta vista mapea el flujo de los datos especificando los protocolos de comunicación utilizados (como llamadas HTTPS/REST y conexiones a base de datos). También evidencia que es la Backend API la que asume la responsabilidad exclusiva de orquestar la ingesta directa desde los sensores IoT y la integración segura con los servicios de terceros (Stripe y Brevo) identificados en el nivel anterior.

![container](../images/Architecture-Diagrams/C4Container.png)


### 4.6.4. Software Architecture Components Diagrams


El Diagrama de Componentes (Nivel 3 del modelo C4) realiza un acercamiento exhaustivo y exclusivo al contenedor principal del sistema, la Backend API, para detallar sus bloques de construcción internos. En este nivel, se expone cómo el código de la aplicación se organiza lógicamente en componentes que encapsulan reglas de negocio, interfaces de entrada y adaptadores de salida, sirviendo como mapa directo para la implementación por parte del equipo de desarrollo.

Para la API de JouleTracker, el diagrama ilustra una arquitectura interna fuertemente influenciada por los principios de Domain-Driven Design (DDD). Primero, se identifican los componentes de entrada (REST Controllers y Listeners IoT) responsables de recibir las peticiones de las aplicaciones web y la telemetría de los sensores. Estos adaptadores delegan el procesamiento a los componentes de dominio centrales, los cuales materializan directamente en código los seis Bounded Contexts definidos en el diseño táctico.

Finalmente, la vista detalla los componentes de infraestructura de salida (Repositorios SQL y Clientes REST), que asumen la responsabilidad puramente técnica de persistir los agregados en la base de datos relacional y ejecutar las llamadas hacia los sistemas de terceros como Stripe y Brevo, manteniendo el núcleo del negocio aislado de los detalles de implementación externa.

![component](../images/Architecture-Diagrams/C4Component.png)


## 4.7. Software Object-Oriented Design

### 4.7.1. Class Diagrams

## 4.8. Database Design

### 4.8.1. Database Diagrams

En esta sección se presentan los diagramas de base de datos de cada Bounded Context, mostrando sus tablas, columnas, tipos de datos, claves primarias y foráneas, constraints y relaciones, con el fin de representar la estructura necesaria para la correcta persistencia de la información.

## 1. User Management Database Diagram

El **User Management Database Diagram** representa la estructura de persistencia responsable de gestionar la información de los usuarios del sistema. Este bounded context permite almacenar los datos básicos de identificación, autenticación, rol y estado de cada usuario, manteniendo la información necesaria para controlar su acceso y participación dentro de la plataforma.git pull --rebase

Las entidades pertenecientes a este contexto se encuentran enfocadas exclusivamente en la gestión de usuarios y sus datos de acceso, evitando almacenar información propia de otros bounded contexts.

![DB1](../images/db-diagrams/db1.png)


## 2. Monitoring Space Database Diagram

El **Monitoring Space Database Diagram** representa la estructura de persistencia utilizada para gestionar los espacios que serán monitoreados por la plataforma. Un espacio puede representar un hogar, negocio u otro establecimiento donde se realiza el seguimiento del consumo energético.

Este bounded context permite almacenar la información de los espacios monitoreados, sus características generales y la relación de los usuarios con dichos espacios. La información relacionada directamente con dispositivos o mediciones pertenece a sus respectivos bounded contexts.


![DB2](../images/db-diagrams/db2.png)

## 3. Device Management Database Diagram

El **Device Management Database Diagram** representa la estructura de persistencia encargada de administrar los dispositivos IoT y sensores utilizados por la plataforma. Este contexto mantiene la información relacionada con el registro, configuración, estado y seguimiento de los dispositivos.

Las entidades de este bounded context permiten identificar los dispositivos y sensores disponibles, almacenar sus configuraciones y mantener un historial de sus estados. Las mediciones generadas por estos dispositivos pertenecen al bounded context de Energy Monitoring.


![DB3](../images/db-diagrams/db3.png)

## 4. Energy Monitoring Database Diagram

El **Energy Monitoring Database Diagram** representa la estructura de persistencia responsable de almacenar las mediciones obtenidas desde los dispositivos IoT. Este bounded context permite registrar los datos de consumo y las variables eléctricas asociadas a cada medición.

También contempla la organización de las mediciones en lotes y el control de su calidad o validación. Las referencias hacia dispositivos y sensores pertenecen conceptualmente al contexto de Device Management, por lo que no se establecen dependencias de base de datos que rompan la autonomía entre bounded contexts.


![DB4](../images/db-diagrams/db4.png)

## 5. Consumption Analysis Database Diagram

El **Consumption Analysis Database Diagram** representa la estructura de persistencia utilizada para analizar la información de consumo previamente registrada. Este bounded context permite almacenar perfiles de consumo, análisis realizados sobre determinados periodos, patrones identificados y anomalías detectadas.

Su responsabilidad se centra en transformar las mediciones recopiladas en información útil para comprender el comportamiento del consumo. Las referencias hacia los espacios monitoreados se manejan como referencias externas al bounded context correspondiente.


![DB5](../images/db-diagrams/db5.png)

## 6. Recommendation Management Database Diagram

El **Recommendation Management Database Diagram** representa la estructura de persistencia responsable de gestionar las recomendaciones generadas a partir del análisis del consumo. Este bounded context permite registrar recomendaciones, su descripción, prioridad, ahorro estimado y estado de seguimiento.

Asimismo, permite almacenar las acciones asociadas a cada recomendación, facilitando el seguimiento de las medidas propuestas para mejorar el comportamiento del consumo. Las referencias hacia espacios monitoreados o resultados de análisis se mantienen como referencias externas, preservando la independencia del bounded context.


![DB6](../images/db-diagrams/db6.png)
>>>>>>> origin/feature/chapter4
