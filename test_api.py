import unittest

from main import obtener_inmuebles

class TestInmueblesAPI(unittest.TestCase):

  def test_get_inmuebles_sin_filtros(self):
    """
    Prueba la función `obtener_inmuebles` sin filtros.

    Esta prueba verifica que la función devuelve una lista de inmuebles.
    """

    # Obtención de la lista de inmuebles sin filtros
    inmuebles = obtener_inmuebles({})

    # Verificación de la respuesta
    self.assertEqual(type(inmuebles), list)
    self.assertGreater(len(inmuebles), 0)

  def test_get_inmuebles_con_filtros(self):
    """
    Prueba la función `obtener_inmuebles` con filtros.

    Esta prueba verifica que la función devuelve una lista de inmuebles que cumplen con los filtros.
    """

    # Definición de los filtros
    filtros = {
      "estado": "en_venta",
      "city": "Bogotá",
    }

    # Obtención de la lista de inmuebles con filtros
    inmuebles = obtener_inmuebles(filtros)

    # Verificación de la respuesta
    self.assertEqual(type(inmuebles), list)
    self.assertGreater(len(inmuebles), 0)
    for inmueble in inmuebles:
      self.assertEqual(inmueble['estado'], "en_venta")
      self.assertEqual(inmueble['city'], "Bogotá")

if __name__ == "__main__":
  unittest.main()
