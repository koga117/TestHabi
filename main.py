import json
import pymysql
from http.server import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import Column, Integer, String, BigInteger, Text, DateTime, ForeignKey
from datetime import datetime

# URL base de la API
API_BASE_URL = "http://localhost:5000/"

# URL para obtener la lista de inmuebles
INMUEBLES_URL = f"{API_BASE_URL}/inmuebles"

# Manejador de peticiones HTTP
class inmuebles(BaseHTTPRequestHandler):
     def do_GET(self):
         """
         Procesa una petición GET a la API.
         Esta función se encarga de obtener los inmuebles de la base de datos y de enviarlos al cliente.
         """
         # Obtención del cuerpo de la solicitud
         content_length = int(self.headers.get('Content-Length'))
         body = self.rfile.read(content_length)

         # Parseo del cuerpo como JSON
         filtros = json.loads(body.decode())

         # Obtención de la lista de inmuebles
         inmuebles = obtener_inmuebles(filtros)

         # Conversión a JSON y envío de la respuesta
         json_data = json.dumps(inmuebles)
         self.send_response(200)
         self.send_header("Content-Type", "application/json")
         self.end_headers()
         self.wfile.write(json_data.encode())

# Función para obtener los inmuebles de la base de datos
def obtener_inmuebles(filtros):
  """
  Realiza la consulta a la base de datos y devuelve una lista de inmuebles.
  """

  # Conexión a la base de datos
  connection = pymysql.connect(
    host="3.138.156.32",
    user="pruebas",
    password="VGbt3Day5R",
    database="habi_db",
    port=3309,
  )

  # Consulta a la base de datos
  try:
    cursor = connection.cursor()
    cursor.execute("""
      SELECT p.id, p.address, p.city, sh.status_id, s.name AS estado, p.price, p.description, p.year
      FROM habi_db.property p
      INNER JOIN habi_db.status_history sh ON p.id = sh.property_id
      INNER JOIN habi_db.status s ON sh.status_id = s.id
      ORDER BY sh.update_date DESC
    """)
    inmuebles = cursor.fetchall()
    print(inmuebles)
  except pymysql.Error as e:
    # Manejo del error de conexión a la base de datos
    print(f"Error al conectar a la base de datos: {e}")
    return []
  finally:
    cursor.close()
    connection.close()

  # Conversión a JSON y envío de la respuesta
  Column = ["id", "address", "city","status_id","estado", "price","description", "year"]
  lista_diccionarios = [
    dict(zip(Column, tupla)) for tupla in inmuebles
  ]

  # Aplicación de filtros
  lista_filtrada = []
  for inmueble in lista_diccionarios:
    estado_actual = inmueble['estado']
    if estado_actual in ("pre_venta", "en_venta", "vendido"):
      cumple_condiciones = True
      for clave, valor in filtros.items():
        if inmueble[clave] != valor:
          print(inmueble['id'],inmueble[clave],valor)
          cumple_condiciones = False
      if cumple_condiciones:
        lista_filtrada.append({
          "id": inmueble['id'],
          "address": inmueble['address'],
          "city": inmueble['city'],
          "estado": estado_actual,
          "price": inmueble['price'],
          "description": inmueble['description'],
        })

  return lista_filtrada

#Inicio del servidor HTTP
server = HTTPServer(('', 5000), inmuebles)
server.serve_forever()
