import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from logica_negocio import obtener_inmuebles_filtrados

API_BASE_URL = "http://localhost:5000/"

class Inmuebles(BaseHTTPRequestHandler):
    def do_GET(self):
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length)
        filtros = json.loads(body.decode())
        inmuebles = obtener_inmuebles_filtrados(filtros)
        json_data = json.dumps(inmuebles)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json_data.encode())

server = HTTPServer(('', 5000), Inmuebles)
server.serve_forever()
