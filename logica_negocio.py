from acceso_datos import obtener_inmuebles

def filtrar_inmuebles(inmuebles, filtros):
    for clave, valor in filtros.items():
        inmuebles = [inmueble for inmueble in inmuebles if inmueble[clave] == valor]
    return inmuebles

def obtener_inmuebles_filtrados(filtros):
    inmuebles = obtener_inmuebles(filtros)
    if filtros:
        inmuebles = filtrar_inmuebles(inmuebles, filtros)
    return inmuebles
