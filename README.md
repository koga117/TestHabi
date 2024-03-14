# TestHabi

Lenguajes de programación:

  * Python 3 o superior

Librerías:

   * BaseHTTPRequestHandler: Librería estándar de Python para el manejo de peticiones HTTP.
   * mysqlclient: Librería para la interacción con bases de datos MySQL.
   * SQLAlchemy: Librería para la gestión de objetos-relacionales en Python.
   * json: Librería estándar de Python para la codificación y decodificación de JSON.
   * parse_qs: Librería de Python para obtener los parámetros de una cadena de consulta.

Herramientas:

  * Un editor de código como Visual Studio Code, PyCharm o Sublime Text.
  * Un intérprete de Python como CPython o PyPy.
  * Una base de datos MySQL.

Pasos de desarrollo: 

  1. Se importan las librerías necesarias, incluyendo mysqlclient para la conexión a MySQL.
  2. Se configura la conexión a la base de datos MySQL.
  3. Se definen los modelos Inmueble y StatusHistory con sus atributos y relaciones.
  4. Se crean las tablas en la base de datos (si no existen).
  5. Se define la clase InmueblesHandler que maneja las peticiones HTTP GET a la ruta /inmuebles.
  6. Se obtienen los parámetros de la consulta del front-end.
  7. Se realiza la conexión a la base de datos MySQL.
  8. Se ejecuta la consulta a la base de datos, obteniendo todos los inmuebles y su historial de estados.
