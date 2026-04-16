# DouglasProyecto-Final-1400
Este proyecto es una aplicacion en Python que simula un customer service virtual (bot) tipo WhatsAPP en la terminal para un Centro de Recepcion ST de dispositivos Electronicos. Permite revisar, reparar, actualizar o donar dichos equipos. Para su implentacion en la vida sostenible para el alarge del uso de estos equipos real tendria que contar con algunas otras herramientas que se conecta a este sistema que presentamos hoy. Este sistema de atención es para un servicio recepcion técnico de dispositivos electrónicos que permite al cliente interactuar mediante un menú en la terminal para revisar, actualiza,reparar o donar equipos. 

#Funcionalidades
Registro del nombre del cliente
Menú interactivo con opciones:
Revisar dispositivo
Actualizar/Reparar dispositivo
Donar dispositivo
Validación de datos con try/except
Generación de informes automáticos
Cálculo de costos por hora
Opciones de traslado (cliente lleva, recogida, urgente)
Generación de número de ticket
Confirmación del cliente antes de continuar
Registro de fecha de entrega o recogida
Persistencia de datos en archivo JSON
Control de flujo con opción de continuar o salir

#Seudocodigo
Explica la logica que se ejecuta desde el main.py

INICIO

Mostrar mensaje de bienvenida
Solicitar nombre del cliente

MIENTRAS el cliente desee continuar:

    Mostrar menú de opciones:
        1. Actualizae/Revisar
        2. Reparar
        3. Donar

    Leer opción del cliente

    SI opción es Actualizar/Revisar:
        Solicitar datos del dispositivo
        Validar entradas
        Generar informe de revisión

        Mostrar recomendación de reparación
        Informar que el costo puede variar

        Preguntar si desea continuar a reparación

        SI responde sí:
            Ir al proceso de reparación
        SI no:
            Informar que puede retirar el equipo

    SI opción es Reparar:
        Mostrar tipos de reparación
        Validar selección

        Mostrar opciones de traslado:
            Cliente lleva equipo
            Recogida a domicilio
            Servicio urgente

        Calcular costo estimado
        Mostrar informe

        Informar que el costo puede variar
        Preguntar si desea continuar

        SI no:
            Cancelar operación

        SI sí:
            SI cliente lleva el equipo:
                Solicitar fecha de entrega
                Generar número de ticket
                Guardar datos
                Preguntar si es todo
                SI sí:
                    Terminar programa

            SI recogida o urgente:
                Solicitar fecha de recogida
                Guardar datos

    SI opción es Donar:
        Solicitar datos del equipo
        Guardar información
        Mostrar informe

    Preguntar si desea algo más

    SI no:
        Mostrar mensaje de despedida
        Terminar programa

FIN

Ejemplo de uso
[CentrodeRecepcionST]: Ingrese su nombre: Ana

=== CentrodeRecepcionST ===
[CentrodeRecepcionST]: Bienvenido Ana
1️⃣ Actulizar/Revisar
2️⃣ Reparar
3️⃣ Donar
Tecnologías utilizadas
Python 3
JSON
Conceptos aplicados
Programación Orientada a Objetos
Manejo de errores
Condicionales
Bucles
Persistencia de datos
Autor


#Estructura del Proyecto
/proyecto
│── main.py
│── servicio.py
│── datos.json
Cómo ejecutar
Abrir la terminal en la carpeta del proyecto
Ejecutar:
python main.py
Ejemplo de uso
[Servicio Técnico]: Ingrese su nombre: Ana

=== Servicio Técnico Pro ===
[CentrodeRecepcionST]: Bienvenido Ana
[CentrodeRecepcionST: Ana, seleccione una opción
1️⃣ Actualizar/Revisar
2️⃣ Reparar
3️⃣ Donar
Tecnologías utilizadas
Python 3
JSON para almacenamiento de datos

Conceptos aplicados:
Programación Orientada a Objetos (POO)
Manejo de errores (try/except)
Condicionales y bucles
Entrada y salida de datos
Persistencia de información
 
#Desarrollos futuros:
Para llevar este proyecto a la realidad necesitariamos incluir estos tres desarrollos:

1. WhatsApp (Twilio)
Recibe mensajes
2. Backend (Python)
Procesa lógica (TU código)
3. Webhook (Flask/FastAPI)
Conecta ambo
Servicio Técnico Pro

 
