from main import obtener_inmuebles

@autodoc
def inmuebles_get(filtros):
  """
  Obtiene una lista de inmuebles.

  Esta ruta permite obtener una lista de inmuebles, filtrando por año de construcción, ciudad y estado.

  Args:
    filtros: Un objeto JSON con los filtros de búsqueda.

  Returns:
    Un objeto JSON con la lista de inmuebles.
  """

  return obtener_inmuebles(filtros)