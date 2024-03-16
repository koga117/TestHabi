import unittest
from logica_negocio import filtrar_inmuebles, obtener_inmuebles_filtrados

class TestLogicaNegocio(unittest.TestCase):

    def test_filtrar_inmuebles(self):
        inmuebles = [{"id": 1, "estado": "pre_venta"}, {"id": 2, "estado": "en_venta"}]
        filtros = {"estado": "pre_venta"}
        inmuebles_filtrados = filtrar_inmuebles(inmuebles, filtros)
        self.assertEqual(len(inmuebles_filtrados), 1)
        self.assertEqual(inmuebles_filtrados[0]["id"], 1)

    def test_obtener_inmuebles_filtrados(self):
        inmuebles = obtener_inmuebles_filtrados({"estado": "pre_venta"})
        self.assertIsNotNone(inmuebles)
        self.assertTrue(len(inmuebles) > 0)

if __name__ == "__main__":
    unittest.main()
