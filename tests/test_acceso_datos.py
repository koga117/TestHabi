import unittest
from acceso_datos import obtener_conexion, obtener_inmuebles

class TestAccesoDatos(unittest.TestCase):

    def test_obtener_conexion(self):
        conexion = obtener_conexion()
        self.assertIsNotNone(conexion)
        conexion.close()

    def test_obtener_inmuebles(self):
        filtros = {
            "year": 2018,
            "city": "bogota",
            "estado": "en_venta"
        }
        inmuebles = obtener_inmuebles(filtros)
        self.assertIsNotNone(inmuebles)
        self.assertTrue(len(inmuebles) > 0)

if __name__ == "__main__":
    unittest.main()
