# TestHabi
    Este proyecto implementa una API RESTful para consultar inmuebles disponibles para la venta. La API permite filtrar los inmuebles por año de construcción, ciudad y estado.

Lenguajes de programación:

  * Python 3 o superior

Librerías:

   * Sphinx: Libreria para la generacion de documentacion
   * Sphinx_rtd_theme: Es un tema de Sphinx diseñado para proporcionar una excelente experiencia de lectura para los usuarios de documentación   
   * Pytest: Libreria para la generacion de pruebas unitarias 
   * BaseHTTPRequestHandler: Librería estándar de Python para el manejo de peticiones HTTP.
   * Pymysql: Librería para la interacción con bases de datos MySQL.
   * SQLAlchemy: Librería para la gestión de objetos-relacionales en Python.
   * json: Librería estándar de Python para la codificación y decodificación de JSON.
   * parse_qs: Librería de Python para obtener los parámetros de una cadena de consulta.

Herramientas:

  * Un editor de código como Visual Studio Code, PyCharm o Sublime Text.
  * Un intérprete de Python como CPython o PyPy.
  * Una base de datos MySQL.

Pasos de desarrollo: 

  1. Se importan las librerías necesarias, incluyendo pymysql para la conexión a MySQL.
  2. Se configura la conexión a la base de datos MySQL.
  3. Se define la clase Inmuebles que maneja las peticiones HTTP GET a la ruta /inmuebles.
  4. Se obtienen los parámetros de la consulta del front-end.
  5. Se realiza la conexión a la base de datos MySQL.
  6. Se ejecuta la consulta a la base de datos, obteniendo todos los inmuebles y su historial de estados.

Ejecucion api --Windows:
  1. Ejecutar comando para creacion de entorno virtual (py -m venv .venv) 
  2. Ejecutar comando para activar entorno virtual (.venv\Scripts\activate)
  3. Ejecutar comando para la instalacion de librerias (pip install -r .\requeriments.txt)
  4. Ejecutar el comando para subir el api (python .\app.py)
  5. Ejecutar pruebas usando postman tipo de peticion GET URL (http://localhost:5000/inmuebles)
  6. Json para la ejecucion de la prueba:

Archivo JSON con los datos esperados del front para los filtros:

    Json:
    {
        "year": 2018,
        "city": "bogota",
        "estado": "en_venta"
    }
   
Ejecucion pruebas unitarias --Windows:
  1. Ejecutar el comando para ejecutar la prueba unitaria de conexion a BD (python -m unittest tests.test_acceso_datos)
  2. Ejecutar el comando para ejecutar la prueba unitaria de logica de negocio (python -m unittest tests.test_logica_negocio)
  3. Ejecutar el comando para ejecutar la prueba unitaria de api (python -m unittest tests.test_app)


# Segundo requerimiento
    Diagrama Entidad-Relacion:

    Usuario ----(Le da Me gusta a)---- Inmueble
    |                                 |
    |                                 |
    |                                 |
    `-- Me gusta --'

    Explicacion:
        **Usuario:**
            * id (int): Identificador único del usuario.
            * nombre (varchar): Nombre del usuario.
            * correo (varchar): Correo electrónico del usuario.
        **Inmueble:**
            * id (int): Identificador único del inmueble.
            * direccion (varchar): Dirección del inmueble.
            * ciudad (varchar): Ciudad donde se encuentra el inmueble.
            * precio (bigint): Precio del inmueble.
            * descripcion (text): Descripción del inmueble.
            * año (int): Año de construcción del inmueble.
        **Me gusta:**
            * id (int): Identificador único del "Me gusta".
            * usuario_id (int): Identificador del usuario que le dio "Me gusta" al inmueble.
            * inmueble_id (int): Identificador del inmueble que recibió el "Me gusta".
            * fecha (datetime): Fecha en la que se dio el "Me gusta".

    Codigo SQL:

    CREATE TABLE `me_gusta` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `usuario_id` int(11) NOT NULL,
    `inmueble_id` int(11) NOT NULL,
    `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `me_gusta_usuario_id_fk` (`usuario_id`),
    KEY `me_gusta_inmueble_id_fk` (`inmueble_id`),
    CONSTRAINT `me_gusta_usuario_id_fk` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`),
    CONSTRAINT `me_gusta_inmueble_id_fk` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

# Puntos extra: 
    **Modelo de base de datos:**
        **Diagrama**
            Usuario ----(Tiene)---- Inmueble
            |                                 |
            |                                 |
            |                                 |
            `-- Historial de estados --'
        **Explicacion:**
            **Usuario:**
                * id (int): Identificador único del usuario.
                * nombre (varchar): Nombre del usuario.
                * correo (varchar): Correo electrónico del usuario.
            **Inmueble:**
                * id (int): Identificador único del inmueble.
                * direccion (varchar): Dirección del inmueble.
                * ciudad (varchar): Ciudad donde se encuentra el inmueble.
                * precio (bigint): Precio del inmueble.
                * descripcion (text): Descripción del inmueble.
                * año (int): Año de construcción del inmueble.
            **Historial de estados:**
                * id (int): Identificador único del estado del inmueble.
                * inmueble_id (int): Identificador del inmueble.
                * estado_id (int): Identificador del estado.
                * fecha (datetime): Fecha en la que se actualizó el estado.
            **Estado:**
                * id (int): Identificador único del estado.
                * nombre (varchar): Nombre del estado.
                * descripcion (text): Descripción del estado.
            **Relaciones:**

                * **Usuario tiene Inmueble:** Esta relación de uno a muchos indica que un usuario puede tener varios inmuebles.
                * **Inmueble tiene Historial de estados:** Esta relación de uno a muchos indica que un inmueble puede tener varios estados a lo largo del tiempo.
                * **Historial de estados tiene Estado:** Esta relación de uno a muchos indica que un estado del historial de estados está asociado a un estado específico.
            **Explicación del modelo:**

                Se ha modificado el modelo original de la siguiente manera:

                * Se ha dividido la tabla `status_history` en dos tablas: `historial_de_estados` y `estado`. Esto se ha hecho para mejorar la normalización de la base de datos y evitar la redundancia de datos.
                * Se ha creado una nueva relación `Inmueble tiene Historial de estados` para registrar el historial de estados de un inmueble.
                * Se ha creado una nueva tabla `Estado` para almacenar los diferentes estados posibles de un inmueble.

                Estas modificaciones tienen como objetivo mejorar la velocidad de las consultas de la siguiente manera:

            * **Reducir el tamaño de las tablas:** La tabla `property` ya no necesita almacenar el historial de estados, lo que reduce su tamaño.
            * **Evitar las búsquedas en tablas grandes:** Las consultas que buscan inmuebles por estado ahora solo necesitan consultar la tabla `historial_de_estados`, que es mucho más pequeña que la tabla `property`.
            * **Utilizar índices:** Se pueden crear índices en las columnas `estado_id` y `fecha` de la tabla `historial_de_estados` para mejorar aún más el rendimiento de las consultas.

            **Beneficios adicionales:**

            * El nuevo modelo es más flexible y extensible. Se pueden agregar nuevos estados sin necesidad de modificar la estructura de la tabla `property`.
            * El nuevo modelo es más fácil de entender y mantener.

            **Limitaciones:**

            * El nuevo modelo requiere un poco más de trabajo de desarrollo para implementarlo.
            * El nuevo modelo puede ser un poco más complejo de entender para los usuarios no técnicos.

            **Conclusiones:**

            La propuesta de mejora del modelo de base de datos tiene como objetivo mejorar la velocidad de las consultas, la flexibilidad y la extensibilidad del modelo. Se espera que estas mejoras beneficien a los usuarios de la aplicación al proporcionar una experiencia más rápida y eficiente.

            **Nota:**
                Diagrama dentro de la carpeta Diagram
# Segundo ejercicio 

    **Dentro del archivo algoritmo_bloques.py**