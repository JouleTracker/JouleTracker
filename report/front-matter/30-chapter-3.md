# CAPÍTULO III: REQUIREMENTS SPECIFICATION
## 3.1. User Stories



<table border="1" cellspacing="0" cellpadding="7" style="border-collapse: collapse; width: 100%; border: 2px solid black;">
    <tr>
      <th align="center">Epic / Story ID</th>
      <th align="center">Título</th>
      <th align="center">Descripción</th>
      <th align="center">Criterios de Aceptación</th>
      <th align="center">Relacionado con (Epic ID)</th>
    </tr>
    <tr>
      <td valign="top"><b>US-01</b></td>
      <td valign="top">Registro de usuario</td>
      <td valign="top"><b>Como visitante</b>, quiero registrarme en JouleTracker proporcionando mis datos personales y credenciales, para poder acceder a las funcionalidades de monitoreo de consumo eléctrico.</td>
      <td valign="top"><b>Escenario 1: Registro exitoso</b><br><br><b>Dado</b> que el visitante no posee una cuenta registrada<br><b>Cuando</b> completa todos los campos obligatorios con información válida<br><b>Entonces</b> el sistema crea la cuenta correctamente<br><b>Y</b> permite al usuario continuar con el proceso de acceso a JouleTracker.<br><br><b>Escenario 2: Correo electrónico ya registrado</b><br><br><b>Dado</b> que existe una cuenta asociada al correo proporcionado<br><b>Cuando</b> el visitante intenta registrarse utilizando dicho correo<br><b>Entonces</b> el sistema rechaza el registro<br><b>Y</b> informa que el correo ya se encuentra registrado.<br><br><b>Escenario 3: Datos obligatorios incompletos</b><br><br><b>Dado</b> que el visitante se encuentra en el formulario de registro<br><b>Cuando</b> intenta registrarse sin completar todos los campos obligatorios<br><b>Entonces</b> el sistema no crea la cuenta<br><b>Y</b> indica qué información debe completar.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-02</b></td>
      <td valign="top">Inicio de sesión</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero iniciar sesión con mis credenciales, para acceder de forma segura a las funcionalidades de JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Inicio de sesión exitoso</b><br><br><b>Dado</b> que el usuario posee una cuenta activa<br><b>Cuando</b> ingresa un correo electrónico y una contraseña válidos<br><b>Entonces</b> el sistema autentica al usuario<br><b>Y</b> permite acceder al dashboard principal.<br><br><b>Escenario 2: Contraseña incorrecta</b><br><br><b>Dado</b> que el correo pertenece a una cuenta registrada<br><b>Cuando</b> el usuario proporciona una contraseña incorrecta<br><b>Entonces</b> el sistema rechaza el acceso<br><b>Y</b> informa que las credenciales son incorrectas.<br><br><b>Escenario 3: Cuenta inexistente</b><br><br><b>Dado</b> que el usuario se encuentra en la pantalla de inicio de sesión<br><b>Cuando</b> proporciona un correo no registrado<br><b>Entonces</b> el sistema no inicia sesión<br><b>Y</b> informa que no existe una cuenta asociada al correo.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-03</b></td>
      <td valign="top">Recuperación de contraseña</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero recuperar el acceso a mi cuenta cuando olvide mi contraseña, para poder continuar utilizando JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Solicitud válida</b><br><br><b>Dado</b> que el usuario posee una cuenta registrada<br><b>Cuando</b> solicita recuperar su contraseña utilizando su correo<br><b>Entonces</b> el sistema inicia el proceso de recuperación<br><b>Y</b> envía las instrucciones correspondientes.<br><br><b>Escenario 2: Correo no registrado</b><br><br><b>Dado</b> que el usuario se encuentra en la opción de recuperación de contraseña<br><b>Cuando</b> ingresa un correo no asociado a ninguna cuenta<br><b>Entonces</b> el sistema no inicia el proceso<br><b>Y</b> informa que el correo no está registrado.<br><br><b>Escenario 3: Nueva contraseña válida</b><br><br><b>Dado</b> que el usuario accedió correctamente al proceso de recuperación<br><b>Cuando</b> establece una nueva contraseña que cumple los requisitos<br><b>Entonces</b> el sistema actualiza sus credenciales<br><b>Y</b> permite iniciar sesión con la nueva contraseña.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-04</b></td>
      <td valign="top">Verificación de cuenta</td>
      <td valign="top"><b>Como usuario recién registrado</b>, quiero verificar mi cuenta, para confirmar mis datos y habilitar el acceso completo a JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Verificación exitosa</b><br><br><b>Dado</b> que el usuario posee una cuenta pendiente de verificación<br><b>Cuando</b> realiza correctamente el proceso de validación<br><b>Entonces</b> el sistema marca la cuenta como verificada<br><b>Y</b> habilita las funcionalidades correspondientes.<br><br><b>Escenario 2: Verificación inválida</b><br><br><b>Dado</b> que el usuario intenta validar su cuenta<br><b>Cuando</b> utiliza información o un código de verificación inválido<br><b>Entonces</b> el sistema rechaza la verificación<br><b>Y</b> solicita realizar nuevamente el proceso.<br><br><b>Escenario 3: Cuenta previamente verificada</b><br><br><b>Dado</b> que la cuenta ya fue verificada<br><b>Cuando</b> el usuario intenta repetir el proceso<br><b>Entonces</b> el sistema mantiene el estado de la cuenta<br><b>Y</b> informa que la verificación ya fue realizada.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-05</b></td>
      <td valign="top">Cierre de sesión</td>
      <td valign="top"><b>Como usuario autenticado</b>, quiero cerrar mi sesión, para evitar que otras personas accedan a mi información desde el mismo dispositivo.</td>
      <td valign="top"><b>Escenario 1: Cierre exitoso</b><br><br><b>Dado</b> que el usuario mantiene una sesión activa<br><b>Cuando</b> selecciona la opción de cerrar sesión<br><b>Entonces</b> el sistema finaliza la sesión<br><b>Y</b> redirige al usuario a la pantalla de acceso.<br><br><b>Escenario 2: Acceso posterior al cierre</b><br><br><b>Dado</b> que la sesión fue finalizada<br><b>Cuando</b> el usuario intenta acceder a una funcionalidad restringida<br><b>Entonces</b> el sistema bloquea el acceso<br><b>Y</b> solicita iniciar sesión nuevamente.<br><br><b>Escenario 3: Sesión expirada</b><br><br><b>Dado</b> que la sesión del usuario ha expirado<br><b>Cuando</b> intenta realizar una operación protegida<br><b>Entonces</b> el sistema impide continuar<br><b>Y</b> solicita nuevamente sus credenciales.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-06</b></td>
      <td valign="top">Visualización de Landing Page</td>
      <td valign="top"><b>Como visitante</b>, quiero acceder a la Landing Page de JouleTracker, para conocer rápidamente de qué trata la solución.</td>
      <td valign="top"><b>Escenario 1: Visualización exitosa</b><br><br><b>Dado</b> que el visitante accede al sitio web de JouleTracker<br><b>Cuando</b> la Landing Page termina de cargar<br><b>Entonces</b> el sistema muestra la propuesta de valor de la plataforma<br><b>Y</b> presenta sus principales funcionalidades.<br><br><b>Escenario 2: Visualización desde dispositivo móvil</b><br><br><b>Dado</b> que el visitante utiliza un dispositivo móvil<br><b>Cuando</b> accede a la Landing Page<br><b>Entonces</b> el contenido se adapta al tamaño de la pantalla<br><b>Y</b> mantiene disponibles los elementos principales.<br><br><b>Escenario 3: Error parcial de recursos</b><br><br><b>Dado</b> que un recurso visual no puede cargarse<br><b>Cuando</b> el visitante abre la página<br><b>Entonces</b> el contenido principal permanece disponible<br><b>Y</b> la navegación continúa funcionando.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-07</b></td>
      <td valign="top">Consulta de beneficios de JouleTracker</td>
      <td valign="top"><b>Como visitante</b>, quiero conocer los principales beneficios de JouleTracker, para evaluar si la solución puede ayudarme a controlar mi consumo eléctrico.</td>
      <td valign="top"><b>Escenario 1: Beneficios disponibles</b><br><br><b>Dado</b> que el visitante se encuentra en la Landing Page<br><b>Cuando</b> accede a la sección de beneficios<br><b>Entonces</b> el sistema muestra las ventajas principales de JouleTracker<br><b>Y</b> explica su relación con el monitoreo y ahorro energético.<br><br><b>Escenario 2: Navegación hacia beneficios</b><br><br><b>Dado</b> que la sección se encuentra disponible<br><b>Cuando</b> el visitante la selecciona desde el menú<br><b>Entonces</b> la página lo dirige al contenido correspondiente<br><b>Y</b> mantiene visible la navegación principal.<br><br><b>Escenario 3: Consulta sin autenticación</b><br><br><b>Dado</b> que el visitante no posee una sesión iniciada<br><b>Cuando</b> consulta la sección de beneficios<br><b>Entonces</b> puede visualizar el contenido<br><b>Y</b> no se le exige autenticarse.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-08</b></td>
      <td valign="top">Consulta del funcionamiento de JouleTracker</td>
      <td valign="top"><b>Como visitante</b>, quiero conocer cómo funciona JouleTracker y sus sensores IoT, para comprender cómo se obtiene y visualiza la información de consumo.</td>
      <td valign="top"><b>Escenario 1: Explicación disponible</b><br><br><b>Dado</b> que el visitante accede a la sección de funcionamiento<br><b>Cuando</b> consulta su contenido<br><b>Entonces</b> el sistema explica el proceso de medición, envío y visualización<br><b>Y</b> describe el rol de los sensores IoT.<br><br><b>Escenario 2: Información organizada</b><br><br><b>Dado</b> que el visitante revisa el funcionamiento<br><b>Cuando</b> visualiza el contenido<br><b>Entonces</b> la explicación se presenta en pasos comprensibles<br><b>Y</b> facilita entender el flujo general.<br><br><b>Escenario 3: Acceso desde el menú</b><br><br><b>Dado</b> que el visitante se encuentra en otra sección<br><b>Cuando</b> selecciona la opción de funcionamiento<br><b>Entonces</b> la página lo dirige a dicha sección<br><b>Y</b> muestra el contenido correspondiente.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-09</b></td>
      <td valign="top">Consulta de funcionalidades principales</td>
      <td valign="top"><b>Como visitante</b>, quiero conocer las funcionalidades principales de JouleTracker, para identificar qué herramientas ofrece la plataforma antes de registrarme.</td>
      <td valign="top"><b>Escenario 1: Funcionalidades mostradas</b><br><br><b>Dado</b> que el visitante se encuentra en la Landing Page<br><b>Cuando</b> accede a la sección de funcionalidades<br><b>Entonces</b> el sistema muestra las capacidades principales de JouleTracker<br><b>Y</b> incluye monitoreo, historial, alertas y estimaciones.<br><br><b>Escenario 2: Información comprensible</b><br><br><b>Dado</b> que el visitante desconoce la plataforma<br><b>Cuando</b> revisa las funcionalidades<br><b>Entonces</b> cada función posee una descripción clara<br><b>Y</b> puede comprender su utilidad.<br><br><b>Escenario 3: Sección disponible sin cuenta</b><br><br><b>Dado</b> que el visitante no está registrado<br><b>Cuando</b> consulta esta sección<br><b>Entonces</b> puede visualizar la información<br><b>Y</b> puede continuar navegando por la Landing Page.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-10</b></td>
      <td valign="top">Acceso a registro e inicio de sesión desde Landing Page</td>
      <td valign="top"><b>Como visitante</b>, quiero acceder al registro o inicio de sesión desde la Landing Page, para comenzar a utilizar JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Acceso al registro</b><br><br><b>Dado</b> que el visitante no posee una cuenta<br><b>Cuando</b> selecciona la opción de registro<br><b>Entonces</b> el sistema lo dirige al formulario correspondiente<br><b>Y</b> permite iniciar la creación de una cuenta.<br><br><b>Escenario 2: Acceso al inicio de sesión</b><br><br><b>Dado</b> que el visitante ya posee una cuenta<br><b>Cuando</b> selecciona iniciar sesión<br><b>Entonces</b> el sistema muestra la pantalla de autenticación<br><b>Y</b> permite ingresar sus credenciales.<br><br><b>Escenario 3: Opciones visibles</b><br><br><b>Dado</b> que la Landing Page cargó correctamente<br><b>Cuando</b> el visitante visualiza la sección principal<br><b>Entonces</b> las opciones de registro e inicio de sesión están disponibles<br><b>Y</b> pueden seleccionarse correctamente.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-11</b></td>
      <td valign="top">Registro de sensor IoT</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero registrar un sensor IoT en JouleTracker, para comenzar a monitorear el consumo eléctrico de mi hogar o negocio.</td>
      <td valign="top"><b>Escenario 1: Sensor registrado correctamente</b><br><br><b>Dado</b> que el usuario posee un sensor compatible<br><b>Cuando</b> proporciona un identificador válido del dispositivo<br><b>Entonces</b> el sistema registra el sensor<br><b>Y</b> lo asocia con la cuenta del usuario.<br><br><b>Escenario 2: Sensor ya registrado</b><br><br><b>Dado</b> que el sensor ya está asociado a una cuenta<br><b>Cuando</b> el usuario intenta registrarlo nuevamente<br><b>Entonces</b> el sistema rechaza la operación<br><b>Y</b> informa que el dispositivo ya se encuentra registrado.<br><br><b>Escenario 3: Identificador inválido</b><br><br><b>Dado</b> que el usuario está registrando un sensor<br><b>Cuando</b> proporciona un identificador incorrecto<br><b>Entonces</b> el sistema no registra el dispositivo<br><b>Y</b> solicita verificar la información.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-12</b></td>
      <td valign="top">Configuración de sensor</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero asignar un nombre y ubicación a mi sensor, para identificar fácilmente qué zona se encuentra monitoreando.</td>
      <td valign="top"><b>Escenario 1: Configuración exitosa</b><br><br><b>Dado</b> que existe un sensor registrado<br><b>Cuando</b> el usuario asigna un nombre y ubicación válidos<br><b>Entonces</b> el sistema guarda la configuración<br><b>Y</b> muestra la información junto al dispositivo.<br><br><b>Escenario 2: Nombre vacío</b><br><br><b>Dado</b> que el usuario está configurando un sensor<br><b>Cuando</b> intenta guardar un nombre vacío<br><b>Entonces</b> el sistema impide completar la operación<br><b>Y</b> solicita ingresar un nombre válido.<br><br><b>Escenario 3: Cambio de ubicación</b><br><br><b>Dado</b> que el sensor posee una ubicación registrada<br><b>Cuando</b> el usuario modifica dicha ubicación<br><b>Entonces</b> el sistema actualiza la información<br><b>Y</b> muestra la nueva zona asociada.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-13</b></td>
      <td valign="top">Consulta del estado del sensor</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero consultar el estado de conexión de mis sensores, para comprobar si están enviando información correctamente.</td>
      <td valign="top"><b>Escenario 1: Sensor conectado</b><br><br><b>Dado</b> que el sensor está enviando datos correctamente<br><b>Cuando</b> el usuario consulta sus dispositivos<br><b>Entonces</b> el sistema muestra el sensor como conectado<br><b>Y</b> presenta su última comunicación.<br><br><b>Escenario 2: Sensor desconectado</b><br><br><b>Dado</b> que el sensor dejó de enviar información<br><b>Cuando</b> el usuario consulta su estado<br><b>Entonces</b> el sistema lo muestra como desconectado<br><b>Y</b> señala la última comunicación registrada.<br><br><b>Escenario 3: Reconexión</b><br><br><b>Dado</b> que un sensor estaba desconectado<br><b>Cuando</b> vuelve a enviar información<br><b>Entonces</b> el sistema actualiza su estado<br><b>Y</b> lo muestra nuevamente como conectado.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-14</b></td>
      <td valign="top">Consulta de información del sensor</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero consultar la información de un sensor registrado, para verificar su nombre, ubicación, estado y última comunicación.</td>
      <td valign="top"><b>Escenario 1: Consulta exitosa</b><br><br><b>Dado</b> que el sensor pertenece a la cuenta del usuario<br><b>Cuando</b> selecciona dicho dispositivo<br><b>Entonces</b> el sistema muestra su información registrada<br><b>Y</b> presenta su estado actual.<br><br><b>Escenario 2: Sensor sin lecturas</b><br><br><b>Dado</b> que el sensor todavía no ha enviado información<br><b>Cuando</b> el usuario consulta su detalle<br><b>Entonces</b> el sistema muestra la configuración disponible<br><b>Y</b> indica que aún no existen lecturas.<br><br><b>Escenario 3: Sensor inexistente</b><br><br><b>Dado</b> que el identificador solicitado no existe<br><b>Cuando</b> el usuario intenta consultar el dispositivo<br><b>Entonces</b> el sistema informa que no puede encontrarse<br><b>Y</b> no muestra información de otro sensor.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-15</b></td>
      <td valign="top">Desvinculación de sensor</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero desvincular un sensor de mi cuenta, para dejar de monitorear un dispositivo que ya no utilizo.</td>
      <td valign="top"><b>Escenario 1: Desvinculación exitosa</b><br><br><b>Dado</b> que el sensor pertenece a la cuenta del usuario<br><b>Cuando</b> confirma la desvinculación<br><b>Entonces</b> el sistema elimina la asociación<br><b>Y</b> deja de mostrar el dispositivo entre sus sensores activos.<br><br><b>Escenario 2: Cancelación</b><br><br><b>Dado</b> que el sistema solicita confirmación<br><b>Cuando</b> el usuario cancela la operación<br><b>Entonces</b> el sensor permanece vinculado<br><b>Y</b> no se realizan cambios.<br><br><b>Escenario 3: Sensor inexistente</b><br><br><b>Dado</b> que el sensor ya no está asociado a la cuenta<br><b>Cuando</b> el usuario intenta desvincularlo nuevamente<br><b>Entonces</b> el sistema no realiza cambios<br><b>Y</b> informa que el dispositivo no está disponible.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-16</b></td>
      <td valign="top">Visualización del Dashboard</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero acceder a un dashboard con mis principales indicadores energéticos, para conocer rápidamente mi situación de consumo.</td>
      <td valign="top"><b>Escenario 1: Dashboard disponible</b><br><br><b>Dado</b> que el usuario inició sesión correctamente<br><b>Cuando</b> accede al dashboard<br><b>Entonces</b> el sistema muestra sus principales indicadores energéticos<br><b>Y</b> presenta la información disponible de sus sensores.<br><br><b>Escenario 2: Sin información</b><br><br><b>Dado</b> que todavía no existen lecturas registradas<br><b>Cuando</b> el usuario accede al dashboard<br><b>Entonces</b> el sistema informa que aún no existen datos suficientes<br><b>Y</b> mantiene disponibles las opciones de configuración.<br><br><b>Escenario 3: Sesión inválida</b><br><br><b>Dado</b> que la sesión dejó de ser válida<br><b>Cuando</b> el usuario intenta acceder al dashboard<br><b>Entonces</b> el sistema bloquea el acceso<br><b>Y</b> solicita iniciar sesión nuevamente.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-17</b></td>
      <td valign="top">Visualización del consumo actual</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero visualizar mi consumo eléctrico actual en el dashboard, para saber cuánta energía estoy utilizando en ese momento.</td>
      <td valign="top"><b>Escenario 1: Lectura disponible</b><br><br><b>Dado</b> que existe un sensor conectado y enviando información<br><b>Cuando</b> el usuario consulta el dashboard<br><b>Entonces</b> el sistema muestra el consumo eléctrico actual<br><b>Y</b> presenta la unidad de medida correspondiente.<br><br><b>Escenario 2: Sensor sin conexión</b><br><br><b>Dado</b> que el sensor no está enviando datos<br><b>Cuando</b> el usuario consulta el consumo actual<br><b>Entonces</b> el sistema informa que la lectura no está disponible<br><b>Y</b> muestra el estado del dispositivo.<br><br><b>Escenario 3: Nueva lectura</b><br><br><b>Dado</b> que el dashboard se encuentra abierto<br><b>Cuando</b> el sistema recibe una nueva lectura<br><b>Entonces</b> actualiza el valor mostrado<br><b>Y</b> mantiene la información reciente.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-18</b></td>
      <td valign="top">Visualización del consumo diario</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero visualizar mi consumo eléctrico acumulado durante el día, para conocer cuánta energía he utilizado.</td>
      <td valign="top"><b>Escenario 1: Consumo diario disponible</b><br><br><b>Dado</b> que existen lecturas registradas durante el día<br><b>Cuando</b> el usuario consulta el dashboard<br><b>Entonces</b> el sistema calcula el consumo acumulado<br><b>Y</b> muestra el resultado correspondiente.<br><br><b>Escenario 2: Sin lecturas del día</b><br><br><b>Dado</b> que todavía no existen registros para la fecha actual<br><b>Cuando</b> el usuario consulta el consumo diario<br><b>Entonces</b> el sistema muestra que no existen datos disponibles<br><b>Y</b> mantiene el indicador sin información.<br><br><b>Escenario 3: Nueva lectura registrada</b><br><br><b>Dado</b> que ya existe consumo acumulado<br><b>Cuando</b> se recibe una nueva lectura válida<br><b>Entonces</b> el sistema actualiza el total diario<br><b>Y</b> refleja el nuevo valor en el dashboard.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-19</b></td>
      <td valign="top">Consumo por sensor</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero consultar el consumo individual de cada sensor, para identificar qué zonas utilizan más energía.</td>
      <td valign="top"><b>Escenario 1: Consulta por sensor</b><br><br><b>Dado</b> que el usuario posee varios sensores registrados<br><b>Cuando</b> selecciona uno de ellos<br><b>Entonces</b> el sistema muestra únicamente el consumo asociado a ese dispositivo<br><b>Y</b> identifica el sensor seleccionado.<br><br><b>Escenario 2: Sensor sin registros</b><br><br><b>Dado</b> que el sensor seleccionado aún no posee lecturas<br><b>Cuando</b> el usuario consulta su consumo<br><b>Entonces</b> el sistema informa que no existen datos disponibles<br><b>Y</b> mantiene visible la información del dispositivo.<br><br><b>Escenario 3: Cambio de sensor</b><br><br><b>Dado</b> que el usuario está visualizando un sensor<br><b>Cuando</b> selecciona otro dispositivo<br><b>Entonces</b> el sistema actualiza la información mostrada<br><b>Y</b> presenta los datos del nuevo sensor.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-20</b></td>
      <td valign="top">Actualización automática del Dashboard</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero que el dashboard actualice automáticamente los datos de consumo, para consultar información reciente sin recargar manualmente la página.</td>
      <td valign="top"><b>Escenario 1: Actualización automática</b><br><br><b>Dado</b> que el usuario mantiene abierto el dashboard<br><b>Cuando</b> el sistema recibe nuevas lecturas<br><b>Entonces</b> actualiza los valores mostrados automáticamente<br><b>Y</b> mantiene visibles los indicadores actualizados.<br><br><b>Escenario 2: Sin nuevas lecturas</b><br><br><b>Dado</b> que no se reciben nuevos datos<br><b>Cuando</b> el dashboard permanece abierto<br><b>Entonces</b> el sistema conserva la última información válida<br><b>Y</b> no muestra valores inexistentes.<br><br><b>Escenario 3: Error de comunicación</b><br><br><b>Dado</b> que existe un problema al obtener nuevas lecturas<br><b>Cuando</b> el sistema intenta actualizar la información<br><b>Entonces</b> mantiene los últimos datos disponibles<br><b>Y</b> informa que existen dificultades de actualización.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-21</b></td>
      <td valign="top">Consulta de perfil</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero consultar la información de mi perfil, para verificar los datos asociados a mi cuenta.</td>
      <td valign="top"><b>Escenario 1: Consulta exitosa</b><br><br><b>Dado</b> que el usuario se encuentra autenticado<br><b>Cuando</b> accede a su perfil<br><b>Entonces</b> el sistema muestra la información registrada en su cuenta.<br><b>Y</b> presenta únicamente los datos correspondientes al usuario.<br><br><b>Escenario 2: Sesión inválida</b><br><br><b>Dado</b> que la sesión dejó de ser válida<br><b>Cuando</b> el usuario intenta acceder al perfil<br><b>Entonces</b> el sistema impide el acceso<br><b>Y</b> solicita iniciar sesión nuevamente.<br><br><b>Escenario 3: Información actualizada</b><br><br><b>Dado</b> que el usuario modificó previamente sus datos<br><b>Cuando</b> consulta nuevamente el perfil<br><b>Entonces</b> el sistema muestra la información actualizada.<br><b>Y</b> mantiene los cambios guardados.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-22</b></td>
      <td valign="top">Edición de perfil</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero modificar mis datos personales, para mantener actualizada la información de mi cuenta.</td>
      <td valign="top"><b>Escenario 1: Actualización exitosa</b><br><br><b>Dado</b> que el usuario accede a la edición de perfil<br><b>Cuando</b> modifica sus datos utilizando información válida<br><b>Entonces</b> el sistema guarda los cambios<br><b>Y</b> muestra la información actualizada.<br><br><b>Escenario 2: Información inválida</b><br><br><b>Dado</b> que el usuario está modificando sus datos<br><b>Cuando</b> proporciona información con un formato incorrecto<br><b>Entonces</b> el sistema rechaza los cambios<br><b>Y</b> indica qué datos deben corregirse.<br><br><b>Escenario 3: Campos obligatorios vacíos</b><br><br><b>Dado</b> que existen campos necesarios para mantener la cuenta<br><b>Cuando</b> el usuario intenta dejarlos vacíos<br><b>Entonces</b> el sistema impide guardar los cambios<br><b>Y</b> solicita completar la información requerida.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-23</b></td>
      <td valign="top">Consulta de historial de consumo</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero consultar mi historial de consumo eléctrico, para revisar el uso de energía realizado anteriormente.</td>
      <td valign="top"><b>Escenario 1: Historial disponible</b><br><br><b>Dado</b> que existen lecturas históricas registradas<br><b>Cuando</b> el usuario accede a su historial<br><b>Entonces</b> el sistema muestra los registros de consumo<br><b>Y</b> los organiza cronológicamente.<br><br><b>Escenario 2: Sin historial</b><br><br><b>Dado</b> que el usuario todavía no posee lecturas históricas<br><b>Cuando</b> consulta esta sección<br><b>Entonces</b> el sistema informa que no existen datos disponibles.<br><b>Y</b> mantiene la sección accesible.<br><br><b>Escenario 3: Nuevos registros</b><br><br><b>Dado</b> que existen nuevas lecturas almacenadas<br><b>Cuando</b> el usuario vuelve a consultar el historial<br><b>Entonces</b> el sistema incluye la información reciente.<br><b>Y</b> mantiene el orden de los registros.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-24</b></td>
      <td valign="top">Filtrado de historial por fechas</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero seleccionar un rango de fechas para mi historial, para analizar el consumo eléctrico durante un periodo específico.</td>
      <td valign="top"><b>Escenario 1: Rango válido</b><br><br><b>Dado</b> que existen datos dentro del periodo seleccionado<br><b>Cuando</b> el usuario establece una fecha inicial y final válidas<br><b>Entonces</b> el sistema muestra únicamente la información correspondiente<br><b>Y</b> aplica el filtro correctamente.<br><br><b>Escenario 2: Rango sin datos</b><br><br><b>Dado</b> que no existen registros en las fechas seleccionadas<br><b>Cuando</b> el usuario realiza la consulta<br><b>Entonces</b> el sistema informa que no existen datos para dicho periodo.<br><b>Y</b> mantiene el filtro aplicado.<br><br><b>Escenario 3: Fechas inválidas</b><br><br><b>Dado</b> que la fecha inicial es posterior a la fecha final<br><b>Cuando</b> el usuario intenta aplicar el filtro<br><b>Entonces</b> el sistema rechaza la consulta<br><b>Y</b> solicita corregir las fechas.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-25</b></td>
      <td valign="top">Cambio de contraseña</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero cambiar mi contraseña desde mi perfil, para mantener segura mi cuenta.</td>
      <td valign="top"><b>Escenario 1: Cambio exitoso</b><br><br><b>Dado</b> que el usuario conoce su contraseña actual<br><b>Cuando</b> proporciona la contraseña actual y una nueva contraseña válida<br><b>Entonces</b> el sistema actualiza sus credenciales<br><b>Y</b> confirma que el cambio fue realizado.<br><br><b>Escenario 2: Contraseña actual incorrecta</b><br><br><b>Dado</b> que el usuario intenta modificar sus credenciales<br><b>Cuando</b> proporciona una contraseña actual incorrecta<br><b>Entonces</b> el sistema rechaza el cambio<br><b>Y</b> mantiene la contraseña existente.<br><br><b>Escenario 3: Nueva contraseña inválida</b><br><br><b>Dado</b> que el usuario está realizando el cambio<br><b>Cuando</b> proporciona una nueva contraseña que no cumple los requisitos<br><b>Entonces</b> el sistema impide actualizarla<br><b>Y</b> informa los requisitos correspondientes.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-26</b></td>
      <td valign="top">Configuración de límite de consumo</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero establecer un límite de consumo eléctrico, para controlar la cantidad de energía que utilizo.</td>
      <td valign="top"><b>Escenario 1: Límite configurado</b><br><br><b>Dado</b> que el usuario se encuentra configurando sus alertas<br><b>Cuando</b> establece un límite válido<br><b>Entonces</b> el sistema guarda el valor<br><b>Y</b> comienza a utilizarlo como referencia.<br><br><b>Escenario 2: Límite inválido</b><br><br><b>Dado</b> que el usuario intenta establecer un valor negativo o inválido<br><b>Cuando</b> guarda la configuración<br><b>Entonces</b> el sistema rechaza la operación<br><b>Y</b> solicita ingresar un límite válido.<br><br><b>Escenario 3: Modificación de límite</b><br><br><b>Dado</b> que existe un límite previamente configurado<br><b>Cuando</b> el usuario establece un nuevo valor<br><b>Entonces</b> el sistema reemplaza la configuración anterior.<br><b>Y</b> utiliza el nuevo límite.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-27</b></td>
      <td valign="top">Alerta por exceso de consumo</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero recibir una alerta cuando mi consumo supere el límite establecido, para reducir oportunamente el uso de energía.</td>
      <td valign="top"><b>Escenario 1: Límite superado</b><br><br><b>Dado</b> que el usuario posee un límite configurado<br><b>Cuando</b> el consumo registrado supera dicho valor<br><b>Entonces</b> el sistema genera una alerta<br><b>Y</b> notifica al usuario.<br><br><b>Escenario 2: Consumo dentro del límite</b><br><br><b>Dado</b> que existe un límite configurado<br><b>Cuando</b> el consumo permanece por debajo del valor establecido<br><b>Entonces</b> el sistema no genera una alerta de exceso.<br><b>Y</b> mantiene el monitoreo activo.<br><br><b>Escenario 3: Nuevo exceso detectado</b><br><br><b>Dado</b> que el consumo vuelve a superar el límite posteriormente<br><b>Cuando</b> el sistema procesa la nueva lectura<br><b>Entonces</b> registra el nuevo evento<br><b>Y</b> genera la alerta correspondiente.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-28</b></td>
      <td valign="top">Meta mensual de consumo</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero establecer una meta mensual de consumo eléctrico, para administrar mejor la energía utilizada durante el mes.</td>
      <td valign="top"><b>Escenario 1: Meta creada</b><br><br><b>Dado</b> que el usuario no posee una meta configurada<br><b>Cuando</b> ingresa un valor mensual válido<br><b>Entonces</b> el sistema guarda la meta<br><b>Y</b> permite consultar su progreso.<br><br><b>Escenario 2: Meta inválida</b><br><br><b>Dado</b> que el usuario proporciona un valor no válido<br><b>Cuando</b> intenta guardar la meta<br><b>Entonces</b> el sistema rechaza la configuración<br><b>Y</b> solicita corregir el valor.<br><br><b>Escenario 3: Meta actualizada</b><br><br><b>Dado</b> que existe una meta activa<br><b>Cuando</b> el usuario modifica su valor<br><b>Entonces</b> el sistema actualiza el objetivo mensual.<br><b>Y</b> recalcula el progreso.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-29</b></td>
      <td valign="top">Estimación del costo eléctrico</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero visualizar una estimación económica de mi consumo eléctrico, para conocer aproximadamente cuánto representa la energía utilizada.</td>
      <td valign="top"><b>Escenario 1: Estimación disponible</b><br><br><b>Dado</b> que existen registros de consumo y una tarifa configurada<br><b>Cuando</b> el usuario consulta el costo estimado<br><b>Entonces</b> el sistema calcula el importe aproximado<br><b>Y</b> lo muestra al usuario.<br><br><b>Escenario 2: Sin tarifa configurada</b><br><br><b>Dado</b> que no existe información tarifaria disponible<br><b>Cuando</b> el usuario solicita la estimación<br><b>Entonces</b> el sistema informa que el cálculo no puede realizarse.<br><b>Y</b> solicita configurar una tarifa.<br><br><b>Escenario 3: Nueva lectura registrada</b><br><br><b>Dado</b> que existe un costo acumulado<br><b>Cuando</b> se agregan nuevos datos de consumo<br><b>Entonces</b> el sistema actualiza la estimación.<br><b>Y</b> muestra el nuevo importe.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-30</b></td>
      <td valign="top">Recomendaciones de ahorro energético</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero recibir recomendaciones relacionadas con mis patrones de consumo, para adoptar hábitos que me permitan utilizar menos energía.</td>
      <td valign="top"><b>Escenario 1: Recomendaciones disponibles</b><br><br><b>Dado</b> que existen suficientes registros de consumo<br><b>Cuando</b> el usuario accede a las recomendaciones<br><b>Entonces</b> el sistema presenta sugerencias relacionadas con sus patrones<br><b>Y</b> muestra acciones orientadas al ahorro.<br><br><b>Escenario 2: Información insuficiente</b><br><br><b>Dado</b> que el usuario posee pocos datos registrados<br><b>Cuando</b> consulta recomendaciones<br><b>Entonces</b> el sistema informa que necesita mayor información.<br><b>Y</b> no genera sugerencias sin respaldo.<br><br><b>Escenario 3: Cambio de comportamiento</b><br><br><b>Dado</b> que los patrones de consumo cambian<br><b>Cuando</b> el sistema vuelve a analizar los registros<br><b>Entonces</b> actualiza las recomendaciones mostradas.<br><b>Y</b> utiliza los datos recientes.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-31</b></td>
      <td valign="top">Registro de áreas del negocio</td>
      <td valign="top"><b>Como propietario de un pequeño negocio</b>, quiero registrar diferentes áreas de mi establecimiento, para organizar los sensores según la zona que monitorean.</td>
      <td valign="top"><b>Escenario 1: Área registrada</b><br><br><b>Dado</b> que el propietario desea organizar sus dispositivos<br><b>Cuando</b> proporciona un nombre válido para una nueva área<br><b>Entonces</b> el sistema registra la zona<br><b>Y</b> permite asociarle sensores.<br><br><b>Escenario 2: Nombre vacío</b><br><br><b>Dado</b> que el propietario crea una nueva área<br><b>Cuando</b> intenta guardarla sin proporcionar un nombre<br><b>Entonces</b> el sistema rechaza la operación<br><b>Y</b> solicita completar la información.<br><br><b>Escenario 3: Edición de área</b><br><br><b>Dado</b> que existe una zona registrada<br><b>Cuando</b> el propietario modifica su nombre<br><b>Entonces</b> el sistema actualiza la información.<br><b>Y</b> mantiene las asociaciones existentes.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-32</b></td>
      <td valign="top">Asociación de sensores a áreas</td>
      <td valign="top"><b>Como propietario de un pequeño negocio</b>, quiero asociar mis sensores a diferentes áreas del establecimiento, para conocer dónde se genera cada consumo.</td>
      <td valign="top"><b>Escenario 1: Asociación exitosa</b><br><br><b>Dado</b> que existe un sensor y un área registrados<br><b>Cuando</b> el propietario selecciona el área correspondiente<br><b>Entonces</b> el sistema relaciona el dispositivo con dicha zona<br><b>Y</b> guarda la asociación.<br><br><b>Escenario 2: Cambio de área</b><br><br><b>Dado</b> que el sensor se encuentra asociado a una zona<br><b>Cuando</b> el propietario lo asigna a otra área<br><b>Entonces</b> el sistema actualiza la asociación.<br><b>Y</b> muestra la nueva zona.<br><br><b>Escenario 3: Área inexistente</b><br><br><b>Dado</b> que la zona seleccionada fue eliminada<br><b>Cuando</b> se intenta asociar el sensor<br><b>Entonces</b> el sistema impide la operación<br><b>Y</b> solicita seleccionar un área válida.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-33</b></td>
      <td valign="top">Consumo eléctrico por área</td>
      <td valign="top"><b>Como propietario de un pequeño negocio</b>, quiero visualizar el consumo eléctrico de cada área, para identificar cuáles generan un mayor uso de energía.</td>
      <td valign="top"><b>Escenario 1: Datos por área disponibles</b><br><br><b>Dado</b> que existen sensores asociados a una zona<br><b>Cuando</b> el propietario consulta dicha área<br><b>Entonces</b> el sistema muestra su consumo eléctrico acumulado<br><b>Y</b> presenta los datos disponibles.<br><br><b>Escenario 2: Área sin sensores</b><br><br><b>Dado</b> que una zona no posee sensores asociados<br><b>Cuando</b> el propietario consulta su consumo<br><b>Entonces</b> el sistema informa que no existen datos disponibles.<br><b>Y</b> mantiene visible la información del área.<br><br><b>Escenario 3: Nueva lectura</b><br><br><b>Dado</b> que existe consumo registrado en un área<br><b>Cuando</b> alguno de sus sensores envía nuevos datos<br><b>Entonces</b> el sistema actualiza el consumo correspondiente.<br><b>Y</b> refleja la nueva lectura.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-34</b></td>
      <td valign="top">Comparación de consumo entre áreas</td>
      <td valign="top"><b>Como propietario de un pequeño negocio</b>, quiero comparar el consumo de las distintas áreas de mi establecimiento, para identificar dónde existe mayor gasto energético.</td>
      <td valign="top"><b>Escenario 1: Comparación disponible</b><br><br><b>Dado</b> que existen datos para varias áreas<br><b>Cuando</b> el propietario solicita una comparación<br><b>Entonces</b> el sistema muestra el consumo correspondiente a cada zona<br><b>Y</b> permite identificar diferencias.<br><br><b>Escenario 2: Área sin información</b><br><br><b>Dado</b> que una de las áreas no posee datos suficientes<br><b>Cuando</b> se realiza la comparación<br><b>Entonces</b> el sistema indica que no existen registros para dicha zona.<br><b>Y</b> muestra la información disponible de las demás áreas.<br><br><b>Escenario 3: Periodo específico</b><br><br><b>Dado</b> que el propietario selecciona un rango de fechas<br><b>Cuando</b> realiza la comparación<br><b>Entonces</b> el sistema utiliza únicamente los datos del periodo.<br><b>Y</b> actualiza los resultados.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-35</b></td>
      <td valign="top">Resumen energético del negocio</td>
      <td valign="top"><b>Como propietario de un pequeño negocio</b>, quiero consultar un resumen del consumo total de mi establecimiento, para supervisar rápidamente el uso general de energía.</td>
      <td valign="top"><b>Escenario 1: Resumen disponible</b><br><br><b>Dado</b> que existen datos de los sensores del establecimiento<br><b>Cuando</b> el propietario accede al dashboard del negocio<br><b>Entonces</b> el sistema muestra el consumo total registrado<br><b>Y</b> presenta los principales indicadores.<br><br><b>Escenario 2: Consumo por áreas</b><br><br><b>Dado</b> que existen varias zonas configuradas<br><b>Cuando</b> el propietario consulta el resumen<br><b>Entonces</b> el sistema incluye información de las principales áreas.<br><b>Y</b> permite comparar su participación en el consumo total.<br><br><b>Escenario 3: Sin datos registrados</b><br><br><b>Dado</b> que ningún sensor ha enviado información<br><b>Cuando</b> el propietario accede al resumen<br><b>Entonces</b> el sistema informa que todavía no existen datos de consumo.<br><b>Y</b> mantiene disponibles las opciones de configuración.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-36</b></td>
      <td valign="top">Consulta de última lectura</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero conocer la fecha y hora de la última lectura recibida, para comprobar qué tan actualizada está la información mostrada.</td>
      <td valign="top"><b>Escenario 1: Lectura disponible</b><br><br><b>Dado</b> que el sensor ha enviado información<br><b>Cuando</b> el usuario consulta sus datos<br><b>Entonces</b> el sistema muestra la fecha y hora de la última lectura.<br><b>Y</b> permite evaluar la actualidad de los datos.<br><br><b>Escenario 2: Sensor sin lecturas</b><br><br><b>Dado</b> que el dispositivo aún no ha enviado información<br><b>Cuando</b> el usuario consulta la última lectura<br><b>Entonces</b> el sistema informa que todavía no existen registros.<br><b>Y</b> no muestra una fecha incorrecta.<br><br><b>Escenario 3: Nueva lectura</b><br><br><b>Dado</b> que existe una fecha de última lectura registrada<br><b>Cuando</b> el sensor envía nuevos datos<br><b>Entonces</b> el sistema actualiza la fecha y hora mostradas.<br><b>Y</b> reemplaza el valor anterior.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-37</b></td>
      <td valign="top">Indicador de costo en Dashboard</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero visualizar el costo estimado de mi consumo desde el dashboard, para conocer rápidamente el impacto económico de la energía utilizada.</td>
      <td valign="top"><b>Escenario 1: Costo disponible</b><br><br><b>Dado</b> que existen consumo y tarifa configurados<br><b>Cuando</b> el usuario accede al dashboard<br><b>Entonces</b> el sistema muestra el costo estimado.<br><b>Y</b> utiliza la información disponible para el cálculo.<br><br><b>Escenario 2: Sin tarifa</b><br><br><b>Dado</b> que no existe una tarifa configurada<br><b>Cuando</b> el usuario consulta el indicador<br><b>Entonces</b> el sistema informa que el cálculo no está disponible.<br><b>Y</b> permite acceder a la configuración correspondiente.<br><br><b>Escenario 3: Consumo actualizado</b><br><br><b>Dado</b> que existe un costo estimado<br><b>Cuando</b> se reciben nuevas lecturas<br><b>Entonces</b> el sistema recalcula el importe.<br><b>Y</b> actualiza el indicador del dashboard.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-38</b></td>
      <td valign="top">Configuración de notificaciones</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero configurar qué notificaciones deseo recibir, para controlar los avisos enviados por JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Actualización exitosa</b><br><br><b>Dado</b> que el usuario accede a la configuración de notificaciones<br><b>Cuando</b> activa o desactiva una categoría disponible<br><b>Entonces</b> el sistema guarda la nueva preferencia<br><b>Y</b> la aplica a futuras notificaciones.<br><br><b>Escenario 2: Configuración sin cambios</b><br><br><b>Dado</b> que el usuario mantiene las preferencias actuales<br><b>Cuando</b> sale de la configuración sin modificar opciones<br><b>Entonces</b> el sistema conserva la configuración existente.<br><b>Y</b> no realiza cambios innecesarios.<br><br><b>Escenario 3: Alerta crítica</b><br><br><b>Dado</b> que ocurre un evento crítico definido por el sistema<br><b>Cuando</b> JouleTracker genera la notificación correspondiente<br><b>Entonces</b> el sistema informa al usuario sobre el evento.<br><b>Y</b> mantiene registrada la alerta.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-39</b></td>
      <td valign="top">Consulta de soluciones para hogares y pequeños negocios</td>
      <td valign="top"><b>Como visitante</b>, quiero conocer cómo JouleTracker puede utilizarse en hogares y pequeños negocios, para identificar qué opción se adapta mejor a mis necesidades.</td>
      <td valign="top"><b>Escenario 1: Información para hogares</b><br><br><b>Dado</b> que el visitante consulta las soluciones disponibles<br><b>Cuando</b> selecciona la opción orientada a hogares<br><b>Entonces</b> el sistema muestra los beneficios correspondientes.<br><b>Y</b> explica el monitoreo doméstico de consumo.<br><br><b>Escenario 2: Información para pequeños negocios</b><br><br><b>Dado</b> que el visitante consulta las soluciones disponibles<br><b>Cuando</b> selecciona la opción orientada a pequeños negocios<br><b>Entonces</b> el sistema muestra las funcionalidades relacionadas.<br><b>Y</b> explica la organización del consumo por áreas.<br><br><b>Escenario 3: Navegación entre segmentos</b><br><br><b>Dado</b> que el visitante está revisando uno de los segmentos<br><b>Cuando</b> selecciona el otro segmento<br><b>Entonces</b> el sistema actualiza la información mostrada.<br><b>Y</b> mantiene el acceso a las demás secciones de la Landing Page.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>US-40</b></td>
      <td valign="top">Desactivación de cuenta</td>
      <td valign="top"><b>Como usuario registrado</b>, quiero desactivar mi cuenta cuando ya no desee utilizar JouleTracker, para dejar de acceder a las funcionalidades de la plataforma.</td>
      <td valign="top"><b>Escenario 1: Desactivación exitosa</b><br><br><b>Dado</b> que el usuario confirma que desea desactivar su cuenta<br><b>Cuando</b> el sistema procesa la solicitud<br><b>Entonces</b> cambia la cuenta a estado inactivo<br><b>Y</b> finaliza las sesiones activas.<br><br><b>Escenario 2: Confirmación cancelada</b><br><br><b>Dado</b> que el usuario inició el proceso de desactivación<br><b>Cuando</b> cancela la confirmación<br><b>Entonces</b> el sistema mantiene la cuenta activa.<br><b>Y</b> no modifica sus datos.<br><br><b>Escenario 3: Acceso posterior</b><br><br><b>Dado</b> que la cuenta fue desactivada<br><b>Cuando</b> el usuario intenta iniciar sesión<br><b>Entonces</b> el sistema impide el acceso.<br><b>Y</b> informa que la cuenta se encuentra inactiva.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-01</b></td>
      <td valign="top">Register User</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar el endpoint de registro de usuario, para permitir la creación de cuentas en JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Registro exitoso</b><br><br><b>Dado</b> que un cliente envía una petición con correo válido, contraseña y datos obligatorios<br><b>Cuando</b> el endpoint <code>POST /api/auth/register</code> procesa la solicitud<br><b>Entonces</b> el sistema crea el usuario con estado activo<br><b>Y</b> retorna <code>201 Created</code> con el identificador y correo del usuario.<br><br><b>Escenario 2: Correo duplicado</b><br><br><b>Dado</b> que un cliente envía una petición con un correo ya registrado<br><b>Cuando</b> el endpoint <code>POST /api/auth/register</code> procesa la solicitud<br><b>Entonces</b> el sistema retorna <code>409 Conflict</code><br><b>Y</b> no crea un nuevo registro.<br><br><b>Escenario 3: Datos inválidos</b><br><br><b>Dado</b> que la solicitud contiene campos obligatorios vacíos o con formato inválido<br><b>Cuando</b> el endpoint valida el cuerpo de la petición<br><b>Entonces</b> el sistema retorna <code>400 Bad Request</code><br><b>Y</b> informa los campos que deben corregirse.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-02</b></td>
      <td valign="top">Login User</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar el endpoint de inicio de sesión, para autenticar usuarios y permitir el acceso seguro a las funciones privadas.</td>
      <td valign="top"><b>Escenario 1: Autenticación exitosa</b><br><br><b>Dado</b> que el cliente envía un correo registrado y una contraseña válida<br><b>Cuando</b> el endpoint <code>POST /api/auth/login</code> procesa las credenciales<br><b>Entonces</b> el sistema autentica al usuario y genera un token de acceso<br><b>Y</b> retorna <code>200 OK</code> con la información necesaria para la sesión.<br><br><b>Escenario 2: Credenciales incorrectas</b><br><br><b>Dado</b> que el correo existe pero la contraseña no coincide<br><b>Cuando</b> el endpoint procesa la solicitud<br><b>Entonces</b> el sistema rechaza la autenticación<br><b>Y</b> retorna <code>401 Unauthorized</code>.<br><br><b>Escenario 3: Usuario inexistente</b><br><br><b>Dado</b> que el cliente envía un correo no registrado<br><b>Cuando</b> el endpoint intenta autenticar la cuenta<br><b>Entonces</b> el sistema rechaza el acceso<br><b>Y</b> retorna <code>401 Unauthorized</code> sin exponer información sensible.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-03</b></td>
      <td valign="top">Recover Password</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar el proceso de recuperación de contraseña, para que un usuario pueda restablecer sus credenciales de forma segura.</td>
      <td valign="top"><b>Escenario 1: Solicitud válida</b><br><br><b>Dado</b> que el cliente envía un correo asociado a una cuenta<br><b>Cuando</b> el endpoint <code>POST /api/auth/password/recovery</code> procesa la solicitud<br><b>Entonces</b> el sistema genera un token temporal de recuperación<br><b>Y</b> retorna <code>200 OK</code> e inicia el flujo de restablecimiento.<br><br><b>Escenario 2: Token inválido</b><br><br><b>Dado</b> que el usuario intenta cambiar la contraseña con un token inexistente o alterado<br><b>Cuando</b> el endpoint de restablecimiento valida el token<br><b>Entonces</b> el sistema rechaza la operación<br><b>Y</b> retorna <code>400 Bad Request</code>.<br><br><b>Escenario 3: Token expirado</b><br><br><b>Dado</b> que el token superó su tiempo de vigencia<br><b>Cuando</b> el usuario intenta utilizarlo<br><b>Entonces</b> el sistema impide modificar la contraseña<br><b>Y</b> retorna una respuesta indicando que debe solicitar un nuevo token.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-04</b></td>
      <td valign="top">Verify Account</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la verificación de cuenta, para habilitar únicamente usuarios que hayan completado correctamente el proceso de validación.</td>
      <td valign="top"><b>Escenario 1: Verificación exitosa</b><br><br><b>Dado</b> que existe una cuenta pendiente y el cliente posee un código válido<br><b>Cuando</b> el endpoint <code>POST /api/auth/verify</code> procesa la solicitud<br><b>Entonces</b> el sistema actualiza la cuenta como verificada<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Código inválido</b><br><br><b>Dado</b> que el código proporcionado no corresponde a la cuenta<br><b>Cuando</b> el endpoint valida la solicitud<br><b>Entonces</b> el sistema no modifica el estado del usuario<br><b>Y</b> retorna <code>400 Bad Request</code>.<br><br><b>Escenario 3: Cuenta ya verificada</b><br><br><b>Dado</b> que la cuenta ya se encuentra verificada<br><b>Cuando</b> el cliente intenta repetir el proceso<br><b>Entonces</b> el sistema conserva el estado actual<br><b>Y</b> retorna una respuesta informativa sin duplicar la operación.</td>
      <td valign="top"><b>EP-01</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-05</b></td>
      <td valign="top">Get Landing Content</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta del contenido público de la Landing Page, para mostrar información actualizada sobre JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Contenido disponible</b><br><br><b>Dado</b> que el cliente solicita la información pública<br><b>Cuando</b> el endpoint <code>GET /api/public/landing</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve la información principal de JouleTracker<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Contenido parcial</b><br><br><b>Dado</b> que una sección pública no posee información configurada<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema devuelve las secciones disponibles<br><b>Y</b> retorna <code>200 OK</code> sin generar un error general.<br><br><b>Escenario 3: Error interno</b><br><br><b>Dado</b> que ocurre un problema al recuperar la información pública<br><b>Cuando</b> el endpoint intenta procesar la consulta<br><b>Entonces</b> el sistema controla el error<br><b>Y</b> retorna una respuesta de error sin exponer información sensible.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-06</b></td>
      <td valign="top">Get JouleTracker Features</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta de funcionalidades públicas, para mostrar en la Landing Page las capacidades principales de JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Funcionalidades disponibles</b><br><br><b>Dado</b> que existen funcionalidades configuradas<br><b>Cuando</b> el endpoint <code>GET /api/public/features</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve la lista de funcionalidades<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Lista vacía</b><br><br><b>Dado</b> que temporalmente no existen funcionalidades publicadas<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema devuelve una lista vacía<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 3: Contenido ordenado</b><br><br><b>Dado</b> que existen varias funcionalidades configuradas<br><b>Cuando</b> el cliente solicita la información<br><b>Entonces</b> el sistema las devuelve en el orden establecido<br><b>Y</b> mantiene sus títulos y descripciones.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-07</b></td>
      <td valign="top">Get Audience Solutions</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta de soluciones para hogares y pequeños negocios, para mostrar contenido diferenciado en la Landing Page.</td>
      <td valign="top"><b>Escenario 1: Soluciones para hogares</b><br><br><b>Dado</b> que el cliente solicita el segmento de hogares<br><b>Cuando</b> el endpoint <code>GET /api/public/solutions?segment=home</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve la información correspondiente<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Soluciones para negocios</b><br><br><b>Dado</b> que el cliente solicita el segmento de pequeños negocios<br><b>Cuando</b> el endpoint <code>GET /api/public/solutions?segment=business</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve la información correspondiente<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 3: Segmento inválido</b><br><br><b>Dado</b> que el cliente envía un segmento no reconocido<br><b>Cuando</b> el endpoint valida el parámetro<br><b>Entonces</b> el sistema rechaza la consulta<br><b>Y</b> retorna <code>400 Bad Request</code>.</td>
      <td valign="top"><b>EP-02</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-08</b></td>
      <td valign="top">Register Sensor</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar el endpoint para registrar sensores IoT, para asociar dispositivos de medición con una cuenta autenticada.</td>
      <td valign="top"><b>Escenario 1: Sensor registrado</b><br><br><b>Dado</b> que el usuario autenticado envía un identificador válido<br><b>Cuando</b> el endpoint <code>POST /api/sensors</code> procesa la solicitud<br><b>Entonces</b> el sistema registra y asocia el sensor<br><b>Y</b> retorna <code>201 Created</code> con su identificador.<br><br><b>Escenario 2: Sensor duplicado</b><br><br><b>Dado</b> que el dispositivo ya se encuentra registrado<br><b>Cuando</b> el cliente intenta registrarlo nuevamente<br><b>Entonces</b> el sistema rechaza la operación<br><b>Y</b> retorna <code>409 Conflict</code>.<br><br><b>Escenario 3: Identificador inválido</b><br><br><b>Dado</b> que el identificador del sensor no cumple el formato requerido<br><b>Cuando</b> el endpoint valida la solicitud<br><b>Entonces</b> el sistema rechaza el registro<br><b>Y</b> retorna <code>400 Bad Request</code>.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-09</b></td>
      <td valign="top">Configure Sensor</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la actualización de la configuración de un sensor, para modificar su nombre y ubicación dentro de JouleTracker.</td>
      <td valign="top"><b>Escenario 1: Configuración actualizada</b><br><br><b>Dado</b> que el sensor pertenece al usuario autenticado<br><b>Cuando</b> el endpoint <code>PUT /api/sensors/{sensorId}</code> recibe datos válidos<br><b>Entonces</b> el sistema actualiza la configuración<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Sensor inexistente</b><br><br><b>Dado</b> que no existe un sensor con el identificador recibido<br><b>Cuando</b> el endpoint procesa la solicitud<br><b>Entonces</b> el sistema no encuentra el recurso<br><b>Y</b> retorna <code>404 Not Found</code>.<br><br><b>Escenario 3: Sensor ajeno</b><br><br><b>Dado</b> que el sensor pertenece a otra cuenta<br><b>Cuando</b> el usuario intenta modificarlo<br><b>Entonces</b> el sistema rechaza el acceso<br><b>Y</b> retorna <code>403 Forbidden</code>.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-10</b></td>
      <td valign="top">Receive Energy Reading</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar el endpoint de recepción de lecturas eléctricas, para almacenar las mediciones enviadas por los sensores IoT.</td>
      <td valign="top"><b>Escenario 1: Lectura válida</b><br><br><b>Dado</b> que un sensor registrado envía una medición válida<br><b>Cuando</b> el endpoint <code>POST /api/readings</code> procesa la lectura<br><b>Entonces</b> el sistema almacena la medición asociada al sensor<br><b>Y</b> retorna <code>201 Created</code>.<br><br><b>Escenario 2: Sensor desconocido</b><br><br><b>Dado</b> que el sensor no se encuentra registrado<br><b>Cuando</b> intenta enviar una lectura<br><b>Entonces</b> el sistema rechaza la operación<br><b>Y</b> retorna <code>404 Not Found</code>.<br><br><b>Escenario 3: Lectura inválida</b><br><br><b>Dado</b> que la medición contiene valores incorrectos o incompletos<br><b>Cuando</b> el endpoint valida la solicitud<br><b>Entonces</b> el sistema no almacena los datos<br><b>Y</b> retorna <code>400 Bad Request</code>.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-11</b></td>
      <td valign="top">Get Sensor Status</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta del estado de sensores, para indicar si un dispositivo está conectado y cuándo transmitió por última vez.</td>
      <td valign="top"><b>Escenario 1: Sensor conectado</b><br><br><b>Dado</b> que el sensor envió datos recientemente<br><b>Cuando</b> el endpoint <code>GET /api/sensors/{sensorId}/status</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve el estado conectado<br><b>Y</b> retorna <code>200 OK</code> con la última comunicación.<br><br><b>Escenario 2: Sensor desconectado</b><br><br><b>Dado</b> que no existen lecturas recientes<br><b>Cuando</b> se consulta el estado<br><b>Entonces</b> el sistema devuelve el estado desconectado<br><b>Y</b> conserva la fecha de última comunicación.<br><br><b>Escenario 3: Sensor inexistente</b><br><br><b>Dado</b> que el identificador no existe<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema no encuentra el recurso<br><b>Y</b> retorna <code>404 Not Found</code>.</td>
      <td valign="top"><b>EP-03</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-12</b></td>
      <td valign="top">Get Dashboard Summary</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta principal del dashboard, para entregar los indicadores energéticos de la cuenta autenticada.</td>
      <td valign="top"><b>Escenario 1: Indicadores disponibles</b><br><br><b>Dado</b> que existen lecturas registradas para el usuario<br><b>Cuando</b> el endpoint <code>GET /api/dashboard/summary</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve los principales indicadores energéticos<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Usuario sin datos</b><br><br><b>Dado</b> que la cuenta no posee lecturas registradas<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema devuelve una respuesta válida sin datos<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 3: Usuario no autenticado</b><br><br><b>Dado</b> que la solicitud no contiene credenciales válidas<br><b>Cuando</b> el cliente intenta consultar el dashboard<br><b>Entonces</b> el sistema bloquea el acceso<br><b>Y</b> retorna <code>401 Unauthorized</code>.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-13</b></td>
      <td valign="top">Get Latest Reading</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta de la última lectura, para mostrar el consumo reciente y la fecha de actualización de cada sensor.</td>
      <td valign="top"><b>Escenario 1: Lectura disponible</b><br><br><b>Dado</b> que el sensor posee registros<br><b>Cuando</b> el endpoint <code>GET /api/readings/latest?sensorId={sensorId}</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve la lectura más reciente<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Sin lecturas</b><br><br><b>Dado</b> que el sensor todavía no posee registros<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema indica que no existen lecturas<br><b>Y</b> retorna una respuesta vacía definida por la API.<br><br><b>Escenario 3: Sensor inexistente</b><br><br><b>Dado</b> que el identificador del sensor no existe<br><b>Cuando</b> se procesa la consulta<br><b>Entonces</b> el sistema no encuentra el recurso<br><b>Y</b> retorna <code>404 Not Found</code>.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-14</b></td>
      <td valign="top">Update Dashboard Data</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la actualización de los datos del dashboard, para reflejar nuevas lecturas sin recargar manualmente la página.</td>
      <td valign="top"><b>Escenario 1: Nueva lectura</b><br><br><b>Dado</b> que el dashboard se encuentra activo<br><b>Cuando</b> el backend recibe una nueva medición<br><b>Entonces</b> el sistema actualiza los datos disponibles para el cliente<br><b>Y</b> permite mostrar el nuevo valor.<br><br><b>Escenario 2: Sin nuevas lecturas</b><br><br><b>Dado</b> que no existen datos nuevos<br><b>Cuando</b> el dashboard permanece abierto<br><b>Entonces</b> el sistema conserva la última información válida<br><b>Y</b> no genera valores ficticios.<br><br><b>Escenario 3: Error de conexión</b><br><br><b>Dado</b> que se interrumpe temporalmente la comunicación<br><b>Cuando</b> el cliente intenta actualizar los datos<br><b>Entonces</b> el sistema mantiene la información previa<br><b>Y</b> permite reintentar la actualización.</td>
      <td valign="top"><b>EP-04</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-15</b></td>
      <td valign="top">Get User Profile</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta y actualización del perfil, para permitir que cada usuario gestione sus datos personales.</td>
      <td valign="top"><b>Escenario 1: Perfil obtenido</b><br><br><b>Dado</b> que el usuario se encuentra autenticado<br><b>Cuando</b> el endpoint <code>GET /api/users/me</code> procesa la consulta<br><b>Entonces</b> el sistema recupera únicamente la información del usuario autenticado<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Perfil actualizado</b><br><br><b>Dado</b> que el usuario envía datos válidos<br><b>Cuando</b> el endpoint <code>PUT /api/users/me</code> procesa la solicitud<br><b>Entonces</b> el sistema actualiza la información permitida<br><b>Y</b> retorna <code>200 OK</code> con los datos actualizados.<br><br><b>Escenario 3: Datos inválidos</b><br><br><b>Dado</b> que la solicitud contiene información con formato incorrecto<br><b>Cuando</b> el endpoint valida los campos<br><b>Entonces</b> el sistema rechaza la actualización<br><b>Y</b> retorna <code>400 Bad Request</code>.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-16</b></td>
      <td valign="top">Get Consumption History</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la consulta del historial de consumo, para mostrar únicamente las lecturas pertenecientes al usuario autenticado.</td>
      <td valign="top"><b>Escenario 1: Historial disponible</b><br><br><b>Dado</b> que el usuario posee lecturas almacenadas<br><b>Cuando</b> el endpoint <code>GET /api/consumption/history</code> procesa la consulta<br><b>Entonces</b> el sistema recupera sus registros de consumo<br><b>Y</b> retorna <code>200 OK</code> con la lista correspondiente.<br><br><b>Escenario 2: Historial vacío</b><br><br><b>Dado</b> que el usuario aún no posee lecturas registradas<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema devuelve una colección vacía<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 3: Rango de fechas</b><br><br><b>Dado</b> que el usuario especifica fechas válidas<br><b>Cuando</b> el endpoint procesa los parámetros<br><b>Entonces</b> el sistema devuelve únicamente los registros del periodo solicitado<br><b>Y</b> retorna <code>200 OK</code>.</td>
      <td valign="top"><b>EP-05</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-17</b></td>
      <td valign="top">Generate Consumption Alert</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la evaluación automática del consumo, para generar alertas preventivas o de exceso según los límites configurados.</td>
      <td valign="top"><b>Escenario 1: Exceso detectado</b><br><br><b>Dado</b> que existe un límite configurado<br><b>Cuando</b> una nueva lectura supera dicho valor<br><b>Entonces</b> el sistema registra una alerta de exceso<br><b>Y</b> la asocia con el usuario correspondiente.<br><br><b>Escenario 2: Proximidad detectada</b><br><br><b>Dado</b> que existe un umbral preventivo<br><b>Cuando</b> el consumo alcanza dicho porcentaje<br><b>Entonces</b> el sistema genera una advertencia preventiva<br><b>Y</b> la deja disponible para notificación.<br><br><b>Escenario 3: Consumo normal</b><br><br><b>Dado</b> que el consumo se mantiene por debajo de los umbrales<br><b>Cuando</b> el sistema procesa una nueva lectura<br><b>Entonces</b> no genera una alerta de exceso<br><b>Y</b> mantiene el monitoreo activo.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-18</b></td>
      <td valign="top">Calculate Estimated Cost</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar el cálculo del costo estimado, para convertir el consumo registrado en un importe aproximado según la tarifa configurada.</td>
      <td valign="top"><b>Escenario 1: Cálculo disponible</b><br><br><b>Dado</b> que existen consumo y tarifa configurados<br><b>Cuando</b> el endpoint <code>GET /api/costs/estimate</code> procesa la consulta<br><b>Entonces</b> el sistema calcula el importe aproximado<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Sin tarifa</b><br><br><b>Dado</b> que no existe una tarifa configurada<br><b>Cuando</b> el usuario solicita el cálculo<br><b>Entonces</b> el sistema informa que falta la configuración requerida<br><b>Y</b> no devuelve un importe incorrecto.<br><br><b>Escenario 3: Nuevas lecturas</b><br><br><b>Dado</b> que existen nuevas mediciones de consumo<br><b>Cuando</b> el cálculo vuelve a ejecutarse<br><b>Entonces</b> el sistema utiliza el consumo actualizado<br><b>Y</b> devuelve una nueva estimación.</td>
      <td valign="top"><b>EP-06</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-19</b></td>
      <td valign="top">Manage Business Areas</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar la gestión de áreas de pequeños negocios, para organizar sensores y consumo eléctrico por zonas.</td>
      <td valign="top"><b>Escenario 1: Área creada</b><br><br><b>Dado</b> que el propietario envía un nombre válido<br><b>Cuando</b> el endpoint <code>POST /api/business/areas</code> procesa la solicitud<br><b>Entonces</b> el sistema crea el área<br><b>Y</b> retorna <code>201 Created</code>.<br><br><b>Escenario 2: Sensor asociado</b><br><br><b>Dado</b> que existen un área y un sensor válidos<br><b>Cuando</b> el endpoint de asociación procesa la solicitud<br><b>Entonces</b> el sistema relaciona el sensor con el área<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 3: Área inexistente</b><br><br><b>Dado</b> que el identificador del área no existe<br><b>Cuando</b> se intenta asociar un sensor<br><b>Entonces</b> el sistema no encuentra el recurso<br><b>Y</b> retorna <code>404 Not Found</code>.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
    <tr>
      <td valign="top"><b>TS-20</b></td>
      <td valign="top">Get Business Dashboard Metrics</td>
      <td valign="top"><b>Como desarrollador</b>, quiero implementar las consultas del dashboard para pequeños negocios, para obtener consumo total y métricas por área.</td>
      <td valign="top"><b>Escenario 1: Métricas disponibles</b><br><br><b>Dado</b> que existen áreas con lecturas registradas<br><b>Cuando</b> el endpoint <code>GET /api/business/dashboard</code> procesa la consulta<br><b>Entonces</b> el sistema devuelve el consumo total y métricas por área<br><b>Y</b> retorna <code>200 OK</code>.<br><br><b>Escenario 2: Área sin datos</b><br><br><b>Dado</b> que una zona no posee lecturas<br><b>Cuando</b> se genera el resumen<br><b>Entonces</b> el sistema indica que no existen datos para dicha área<br><b>Y</b> mantiene la información de las demás zonas.<br><br><b>Escenario 3: Periodo filtrado</b><br><br><b>Dado</b> que el propietario especifica un rango de fechas válido<br><b>Cuando</b> el endpoint procesa la consulta<br><b>Entonces</b> el sistema calcula las métricas utilizando únicamente ese periodo<br><b>Y</b> retorna <code>200 OK</code>.</td>
      <td valign="top"><b>EP-07</b></td>
    </tr>
</table>

### Epics


<table border="1" cellspacing="0" cellpadding="7" style="border-collapse: collapse; width: 100%; border: 2px solid black;">
  <tr>
    <th align="center">Epic ID</th>
    <th align="center">Título</th>
    <th align="center">Descripción</th>
    <th align="center">Historias relacionadas</th>
  </tr>
  <tr>
    <td valign="top"><b>EP-01</b></td>
    <td valign="top">Gestión de cuentas y autenticación</td>
    <td valign="top">Agrupa las funcionalidades relacionadas con el registro, inicio de sesión, verificación, recuperación de contraseña y seguridad de acceso de los usuarios en JouleTracker.</td>
    <td valign="top">US-01 a US-05, TS-01 a TS-04</td>
  </tr>
  <tr>
    <td valign="top"><b>EP-02</b></td>
    <td valign="top">Landing Page y presentación de JouleTracker</td>
    <td valign="top">Incluye las funcionalidades públicas que permiten presentar JouleTracker, explicar sus beneficios, mostrar cómo funciona la solución y facilitar el acceso de los visitantes a la plataforma.</td>
    <td valign="top">US-06 a US-10, US-39, TS-05 a TS-07</td>
  </tr>
  <tr>
    <td valign="top"><b>EP-03</b></td>
    <td valign="top">Gestión de sensores IoT</td>
    <td valign="top">Reúne las funcionalidades necesarias para registrar, configurar, consultar y desvincular sensores IoT, así como recibir las lecturas eléctricas enviadas por los dispositivos.</td>
    <td valign="top">US-11 a US-15, TS-08 a TS-11</td>
  </tr>
  <tr>
    <td valign="top"><b>EP-04</b></td>
    <td valign="top">Dashboard y monitoreo de consumo</td>
    <td valign="top">Comprende la visualización del consumo eléctrico actual, consumo diario, información por sensor, última lectura, costo estimado y actualización automática del dashboard.</td>
    <td valign="top">US-16 a US-20, US-36, US-37, TS-12 a TS-14</td>
  </tr>
  <tr>
    <td valign="top"><b>EP-05</b></td>
    <td valign="top">Perfil, historial y gestión personal</td>
    <td valign="top">Agrupa las funcionalidades que permiten al usuario consultar y actualizar su perfil, revisar su historial de consumo, filtrar registros, cambiar su contraseña y desactivar su cuenta.</td>
    <td valign="top">US-21 a US-25, US-40, TS-15 y TS-16</td>
  </tr>
  <tr>
    <td valign="top"><b>EP-06</b></td>
    <td valign="top">Alertas, metas y optimización energética</td>
    <td valign="top">Incluye la configuración de límites y metas, alertas por exceso de consumo, estimaciones económicas, recomendaciones de ahorro y preferencias de notificación.</td>
    <td valign="top">US-26 a US-30, US-38, TS-17 y TS-18</td>
  </tr>
  <tr>
    <td valign="top"><b>EP-07</b></td>
    <td valign="top">Gestión energética para pequeños negocios</td>
    <td valign="top">Reúne las funcionalidades orientadas a organizar áreas de un establecimiento, asociar sensores, comparar consumos y consultar métricas energéticas para apoyar la gestión del negocio.</td>
    <td valign="top">US-31 a US-35, TS-19 y TS-20</td>
  </tr>
</table>



## 3.3. Product Backlog

<table border="1" cellspacing="0" cellpadding="7" style="border-collapse: collapse; width: 100%; border: 2px solid black;">
  <tr>
    <th align="center"># Orden</th>
    <th align="center">User Story Id</th>
    <th align="center">Título</th>
    <th align="center">Descripción</th>
    <th align="center">Story Points<br>(1 / 2 / 3 / 5 / 8)</th>
  </tr>
  <tr>
    <td valign="top" align="center"><b>1</b></td>
    <td valign="top" align="center"><b>US-06</b></td>
    <td valign="top">Visualización de Landing Page</td>
    <td valign="top">Como visitante , quiero acceder a la Landing Page de JouleTracker, para conocer rápidamente de qué trata la solución.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>2</b></td>
    <td valign="top" align="center"><b>US-07</b></td>
    <td valign="top">Consulta de beneficios de JouleTracker</td>
    <td valign="top">Como visitante , quiero conocer los principales beneficios de JouleTracker, para evaluar si la solución puede ayudarme a controlar mi consumo eléctrico.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>3</b></td>
    <td valign="top" align="center"><b>US-08</b></td>
    <td valign="top">Consulta del funcionamiento de JouleTracker</td>
    <td valign="top">Como visitante , quiero conocer cómo funciona JouleTracker y sus sensores IoT, para comprender cómo se obtiene y visualiza la información de consumo.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>4</b></td>
    <td valign="top" align="center"><b>US-09</b></td>
    <td valign="top">Consulta de funcionalidades principales</td>
    <td valign="top">Como visitante , quiero conocer las funcionalidades principales de JouleTracker, para identificar qué herramientas ofrece la plataforma antes de registrarme.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>5</b></td>
    <td valign="top" align="center"><b>US-10</b></td>
    <td valign="top">Acceso a registro e inicio de sesión desde Landing Page</td>
    <td valign="top">Como visitante , quiero acceder al registro o inicio de sesión desde la Landing Page, para comenzar a utilizar JouleTracker.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>6</b></td>
    <td valign="top" align="center"><b>US-01</b></td>
    <td valign="top">Registro de usuario</td>
    <td valign="top">Como visitante , quiero registrarme en JouleTracker proporcionando mis datos personales y credenciales, para poder acceder a las funcionalidades de monitoreo de consumo eléctrico.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>7</b></td>
    <td valign="top" align="center"><b>US-02</b></td>
    <td valign="top">Inicio de sesión</td>
    <td valign="top">Como usuario registrado , quiero iniciar sesión con mis credenciales, para acceder de forma segura a las funcionalidades de JouleTracker.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>8</b></td>
    <td valign="top" align="center"><b>US-11</b></td>
    <td valign="top">Registro de sensor IoT</td>
    <td valign="top">Como usuario registrado , quiero registrar un sensor IoT en JouleTracker, para comenzar a monitorear el consumo eléctrico de mi hogar o negocio.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>9</b></td>
    <td valign="top" align="center"><b>US-12</b></td>
    <td valign="top">Configuración de sensor</td>
    <td valign="top">Como usuario registrado , quiero asignar un nombre y ubicación a mi sensor, para identificar fácilmente qué zona se encuentra monitoreando.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>10</b></td>
    <td valign="top" align="center"><b>US-16</b></td>
    <td valign="top">Visualización del Dashboard</td>
    <td valign="top">Como usuario registrado , quiero acceder a un dashboard con mis principales indicadores energéticos, para conocer rápidamente mi situación de consumo.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>11</b></td>
    <td valign="top" align="center"><b>US-17</b></td>
    <td valign="top">Visualización del consumo actual</td>
    <td valign="top">Como usuario registrado , quiero visualizar mi consumo eléctrico actual en el dashboard, para saber cuánta energía estoy utilizando en ese momento.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>12</b></td>
    <td valign="top" align="center"><b>US-18</b></td>
    <td valign="top">Visualización del consumo diario</td>
    <td valign="top">Como usuario registrado , quiero visualizar mi consumo eléctrico acumulado durante el día, para conocer cuánta energía he utilizado.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>13</b></td>
    <td valign="top" align="center"><b>US-19</b></td>
    <td valign="top">Consumo por sensor</td>
    <td valign="top">Como usuario registrado , quiero consultar el consumo individual de cada sensor, para identificar qué zonas utilizan más energía.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>14</b></td>
    <td valign="top" align="center"><b>US-20</b></td>
    <td valign="top">Actualización automática del Dashboard</td>
    <td valign="top">Como usuario registrado , quiero que el dashboard actualice automáticamente los datos de consumo, para consultar información reciente sin recargar manualmente la página.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>15</b></td>
    <td valign="top" align="center"><b>US-36</b></td>
    <td valign="top">Consulta de última lectura</td>
    <td valign="top">Como usuario registrado , quiero conocer la fecha y hora de la última lectura recibida, para comprobar qué tan actualizada está la información mostrada.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>16</b></td>
    <td valign="top" align="center"><b>US-37</b></td>
    <td valign="top">Indicador de costo en Dashboard</td>
    <td valign="top">Como usuario registrado , quiero visualizar el costo estimado de mi consumo desde el dashboard, para conocer rápidamente el impacto económico de la energía utilizada.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>17</b></td>
    <td valign="top" align="center"><b>US-23</b></td>
    <td valign="top">Consulta de historial de consumo</td>
    <td valign="top">Como usuario registrado , quiero consultar mi historial de consumo eléctrico, para revisar el uso de energía realizado anteriormente.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>18</b></td>
    <td valign="top" align="center"><b>US-24</b></td>
    <td valign="top">Filtrado de historial por fechas</td>
    <td valign="top">Como usuario registrado , quiero seleccionar un rango de fechas para mi historial, para analizar el consumo eléctrico durante un periodo específico.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>19</b></td>
    <td valign="top" align="center"><b>US-26</b></td>
    <td valign="top">Configuración de límite de consumo</td>
    <td valign="top">Como usuario registrado , quiero establecer un límite de consumo eléctrico, para controlar la cantidad de energía que utilizo.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>20</b></td>
    <td valign="top" align="center"><b>US-27</b></td>
    <td valign="top">Alerta por exceso de consumo</td>
    <td valign="top">Como usuario registrado , quiero recibir una alerta cuando mi consumo supere el límite establecido, para reducir oportunamente el uso de energía.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>21</b></td>
    <td valign="top" align="center"><b>US-28</b></td>
    <td valign="top">Meta mensual de consumo</td>
    <td valign="top">Como usuario registrado , quiero establecer una meta mensual de consumo eléctrico, para administrar mejor la energía utilizada durante el mes.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>22</b></td>
    <td valign="top" align="center"><b>US-29</b></td>
    <td valign="top">Estimación del costo eléctrico</td>
    <td valign="top">Como usuario registrado , quiero visualizar una estimación económica de mi consumo eléctrico, para conocer aproximadamente cuánto representa la energía utilizada.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>23</b></td>
    <td valign="top" align="center"><b>US-30</b></td>
    <td valign="top">Recomendaciones de ahorro energético</td>
    <td valign="top">Como usuario registrado , quiero recibir recomendaciones relacionadas con mis patrones de consumo, para adoptar hábitos que me permitan utilizar menos energía.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>24</b></td>
    <td valign="top" align="center"><b>US-38</b></td>
    <td valign="top">Configuración de notificaciones</td>
    <td valign="top">Como usuario registrado , quiero configurar qué notificaciones deseo recibir, para controlar los avisos enviados por JouleTracker.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>25</b></td>
    <td valign="top" align="center"><b>US-31</b></td>
    <td valign="top">Registro de áreas del negocio</td>
    <td valign="top">Como propietario de un pequeño negocio , quiero registrar diferentes áreas de mi establecimiento, para organizar los sensores según la zona que monitorean.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>26</b></td>
    <td valign="top" align="center"><b>US-32</b></td>
    <td valign="top">Asociación de sensores a áreas</td>
    <td valign="top">Como propietario de un pequeño negocio , quiero asociar mis sensores a diferentes áreas del establecimiento, para conocer dónde se genera cada consumo.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>27</b></td>
    <td valign="top" align="center"><b>US-33</b></td>
    <td valign="top">Consumo eléctrico por área</td>
    <td valign="top">Como propietario de un pequeño negocio , quiero visualizar el consumo eléctrico de cada área, para identificar cuáles generan un mayor uso de energía.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>28</b></td>
    <td valign="top" align="center"><b>US-34</b></td>
    <td valign="top">Comparación de consumo entre áreas</td>
    <td valign="top">Como propietario de un pequeño negocio , quiero comparar el consumo de las distintas áreas de mi establecimiento, para identificar dónde existe mayor gasto energético.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>29</b></td>
    <td valign="top" align="center"><b>US-35</b></td>
    <td valign="top">Resumen energético del negocio</td>
    <td valign="top">Como propietario de un pequeño negocio , quiero consultar un resumen del consumo total de mi establecimiento, para supervisar rápidamente el uso general de energía.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>30</b></td>
    <td valign="top" align="center"><b>US-21</b></td>
    <td valign="top">Consulta de perfil</td>
    <td valign="top">Como usuario registrado , quiero consultar la información de mi perfil, para verificar los datos asociados a mi cuenta.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>31</b></td>
    <td valign="top" align="center"><b>US-22</b></td>
    <td valign="top">Edición de perfil</td>
    <td valign="top">Como usuario registrado , quiero modificar mis datos personales, para mantener actualizada la información de mi cuenta.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>32</b></td>
    <td valign="top" align="center"><b>US-25</b></td>
    <td valign="top">Cambio de contraseña</td>
    <td valign="top">Como usuario registrado , quiero cambiar mi contraseña desde mi perfil, para mantener segura mi cuenta.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>33</b></td>
    <td valign="top" align="center"><b>US-03</b></td>
    <td valign="top">Recuperación de contraseña</td>
    <td valign="top">Como usuario registrado , quiero recuperar el acceso a mi cuenta cuando olvide mi contraseña, para poder continuar utilizando JouleTracker.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>34</b></td>
    <td valign="top" align="center"><b>US-04</b></td>
    <td valign="top">Verificación de cuenta</td>
    <td valign="top">Como usuario recién registrado , quiero verificar mi cuenta, para confirmar mis datos y habilitar el acceso completo a JouleTracker.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>35</b></td>
    <td valign="top" align="center"><b>US-05</b></td>
    <td valign="top">Cierre de sesión</td>
    <td valign="top">Como usuario autenticado , quiero cerrar mi sesión, para evitar que otras personas accedan a mi información desde el mismo dispositivo.</td>
    <td valign="top" align="center"><b>1</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>36</b></td>
    <td valign="top" align="center"><b>US-13</b></td>
    <td valign="top">Consulta del estado del sensor</td>
    <td valign="top">Como usuario registrado , quiero consultar el estado de conexión de mis sensores, para comprobar si están enviando información correctamente.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>37</b></td>
    <td valign="top" align="center"><b>US-14</b></td>
    <td valign="top">Consulta de información del sensor</td>
    <td valign="top">Como usuario registrado , quiero consultar la información de un sensor registrado, para verificar su nombre, ubicación, estado y última comunicación.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>38</b></td>
    <td valign="top" align="center"><b>US-15</b></td>
    <td valign="top">Desvinculación de sensor</td>
    <td valign="top">Como usuario registrado , quiero desvincular un sensor de mi cuenta, para dejar de monitorear un dispositivo que ya no utilizo.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>39</b></td>
    <td valign="top" align="center"><b>US-39</b></td>
    <td valign="top">Consulta de soluciones para hogares y pequeños negocios</td>
    <td valign="top">Como visitante , quiero conocer cómo JouleTracker puede utilizarse en hogares y pequeños negocios, para identificar qué opción se adapta mejor a mis necesidades.</td>
    <td valign="top" align="center"><b>2</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>40</b></td>
    <td valign="top" align="center"><b>US-40</b></td>
    <td valign="top">Desactivación de cuenta</td>
    <td valign="top">Como usuario registrado , quiero desactivar mi cuenta cuando ya no desee utilizar JouleTracker, para dejar de acceder a las funcionalidades de la plataforma.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>41</b></td>
    <td valign="top" align="center"><b>TS-05</b></td>
    <td valign="top">Get Landing Content</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta del contenido público de la Landing Page, para mostrar información actualizada sobre JouleTracker.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>42</b></td>
    <td valign="top" align="center"><b>TS-06</b></td>
    <td valign="top">Get JouleTracker Features</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta de funcionalidades públicas, para mostrar en la Landing Page las capacidades principales de JouleTracker.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>43</b></td>
    <td valign="top" align="center"><b>TS-07</b></td>
    <td valign="top">Get Audience Solutions</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta de soluciones para hogares y pequeños negocios, para mostrar contenido diferenciado en la Landing Page.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>44</b></td>
    <td valign="top" align="center"><b>TS-01</b></td>
    <td valign="top">Register User</td>
    <td valign="top">Como desarrollador , quiero implementar el endpoint de registro de usuario, para permitir la creación de cuentas en JouleTracker.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>45</b></td>
    <td valign="top" align="center"><b>TS-02</b></td>
    <td valign="top">Login User</td>
    <td valign="top">Como desarrollador , quiero implementar el endpoint de inicio de sesión, para autenticar usuarios y permitir el acceso seguro a las funciones privadas.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>46</b></td>
    <td valign="top" align="center"><b>TS-03</b></td>
    <td valign="top">Recover Password</td>
    <td valign="top">Como desarrollador , quiero implementar el proceso de recuperación de contraseña, para que un usuario pueda restablecer sus credenciales de forma segura.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>47</b></td>
    <td valign="top" align="center"><b>TS-04</b></td>
    <td valign="top">Verify Account</td>
    <td valign="top">Como desarrollador , quiero implementar la verificación de cuenta, para habilitar únicamente usuarios que hayan completado correctamente el proceso de validación.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>48</b></td>
    <td valign="top" align="center"><b>TS-08</b></td>
    <td valign="top">Register Sensor</td>
    <td valign="top">Como desarrollador , quiero implementar el endpoint para registrar sensores IoT, para asociar dispositivos de medición con una cuenta autenticada.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>49</b></td>
    <td valign="top" align="center"><b>TS-09</b></td>
    <td valign="top">Configure Sensor</td>
    <td valign="top">Como desarrollador , quiero implementar la actualización de la configuración de un sensor, para modificar su nombre y ubicación dentro de JouleTracker.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>50</b></td>
    <td valign="top" align="center"><b>TS-10</b></td>
    <td valign="top">Receive Energy Reading</td>
    <td valign="top">Como desarrollador , quiero implementar el endpoint de recepción de lecturas eléctricas, para almacenar las mediciones enviadas por los sensores IoT.</td>
    <td valign="top" align="center"><b>8</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>51</b></td>
    <td valign="top" align="center"><b>TS-11</b></td>
    <td valign="top">Get Sensor Status</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta del estado de sensores, para indicar si un dispositivo está conectado y cuándo transmitió por última vez.</td>
    <td valign="top" align="center"><b>3</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>52</b></td>
    <td valign="top" align="center"><b>TS-12</b></td>
    <td valign="top">Get Dashboard Summary</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta principal del dashboard, para entregar los indicadores energéticos de la cuenta autenticada.</td>
    <td valign="top" align="center"><b>8</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>53</b></td>
    <td valign="top" align="center"><b>TS-13</b></td>
    <td valign="top">Get Latest Reading</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta de la última lectura, para mostrar el consumo reciente y la fecha de actualización de cada sensor.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>54</b></td>
    <td valign="top" align="center"><b>TS-14</b></td>
    <td valign="top">Update Dashboard Data</td>
    <td valign="top">Como desarrollador , quiero implementar la actualización de los datos del dashboard, para reflejar nuevas lecturas sin recargar manualmente la página.</td>
    <td valign="top" align="center"><b>8</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>55</b></td>
    <td valign="top" align="center"><b>TS-15</b></td>
    <td valign="top">Get User Profile</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta y actualización del perfil, para permitir que cada usuario gestione sus datos personales.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>56</b></td>
    <td valign="top" align="center"><b>TS-16</b></td>
    <td valign="top">Get Consumption History</td>
    <td valign="top">Como desarrollador , quiero implementar la consulta del historial de consumo, para mostrar únicamente las lecturas pertenecientes al usuario autenticado.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>57</b></td>
    <td valign="top" align="center"><b>TS-17</b></td>
    <td valign="top">Generate Consumption Alert</td>
    <td valign="top">Como desarrollador , quiero implementar la evaluación automática del consumo, para generar alertas preventivas o de exceso según los límites configurados.</td>
    <td valign="top" align="center"><b>8</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>58</b></td>
    <td valign="top" align="center"><b>TS-18</b></td>
    <td valign="top">Calculate Estimated Cost</td>
    <td valign="top">Como desarrollador , quiero implementar el cálculo del costo estimado, para convertir el consumo registrado en un importe aproximado según la tarifa configurada.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>59</b></td>
    <td valign="top" align="center"><b>TS-19</b></td>
    <td valign="top">Manage Business Areas</td>
    <td valign="top">Como desarrollador , quiero implementar la gestión de áreas de pequeños negocios, para organizar sensores y consumo eléctrico por zonas.</td>
    <td valign="top" align="center"><b>5</b></td>
  </tr>
  <tr>
    <td valign="top" align="center"><b>60</b></td>
    <td valign="top" align="center"><b>TS-20</b></td>
    <td valign="top">Get Business Dashboard Metrics</td>
    <td valign="top">Como desarrollador , quiero implementar las consultas del dashboard para pequeños negocios, para obtener consumo total y métricas por área.</td>
    <td valign="top" align="center"><b>8</b></td>
  </tr>
</table>