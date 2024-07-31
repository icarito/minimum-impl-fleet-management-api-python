# Fleet Management Software API Flask Sample Implementation

## Introducción

Este proyecto es una implementación de
[Fleet Management Software API](https://github.com/Laboratoria/curriculum/tree/main/projects/05-fleet-management-api)
en Python con la librería Flask, orientada a implementar los proyectos de **DevOps**.
Actualmente, solo se ha implementado el endpoint
[GET /taxis](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/taxis/getTaxi)
sin autenticación.

## ¿Cómo ejecutar este proyecto?

1. **Configurar la base de datos**:
   - Necesitas una base de datos PostgreSQL en Vercel con al menos la tabla `taxis`. 
   - Puedes crear esta base de datos siguiendo los
   [pasos 2, 3 y 4](https://github.com/Laboratoria/curriculum/tree/main/projects/05-fleet-management-api#8-pistas-tips-y-lecturas-complementarias)
   de la sección "8. Pistas, tips y lecturas complementarias"
   del README de Fleet Management Software API.

2. **Configurar variables de entorno**:
   - Renombra el archivo `.env.sample` a `.env`.
   - Modifica el valor de la variable de entorno `DATABASE_URL` con la información proporcionada por Vercel.

3. **Crear el Python virtual environment y activarlo**:
   - Ejecuta el comando `python3 -m venv venv` en una terminal para crear una Python virtual environment.
   - Ejecuta el comando `source venv/bin/activate` en una terminal para activarlo.

3. **Instalar dependencias**:
   - Ejecuta el comando `pip install -r requirements.txt` en una terminal para instalar las dependencias necesarias.

4. **Iniciar la aplicación**:
   - Ejecuta el comando `flask --app fleet_api/app.py run --host=0.0.0.0 --port=PORT` en una terminal para iniciar la aplicación. Puedes cambiar `PORT` para especificar el puerto en el que la API escuchará peticiones HTTP. Esto es importante al desplegar la API en la nube en proyectos de **DevOps**.

   Puedes probar la aplicación haciendo una petición GET a `http://localhost:PORT/taxis`,
   reemplazando `PORT` por el valor del parámetro `--port` del comando de ejecución.
   Si la aplicación se está ejecutando correctamente, deberías obtener como respuesta un array
   JSON con 10 registros de la tabla `taxis` de la base de datos configurada en Vercel.
