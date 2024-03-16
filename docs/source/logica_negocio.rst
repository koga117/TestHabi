Acceso a Logica Inmuebles
===========================

# Módulo logica_negocio

Este módulo contiene la lógica de negocio para la aplicación, como la búsqueda y el filtrado de inmuebles.

## Dependencias

Este módulo depende del módulo `acceso_datos` para obtener información sobre los inmuebles.

## Funciones

### filtrar_inmuebles(inmuebles, filtros)

Filtra una lista de inmuebles según los criterios especificados en un diccionario.

**Parámetros:**

* **inmuebles**: Lista de diccionarios, donde cada diccionario representa un inmueble.
* **filtros**: Diccionario con los criterios de filtro. Las claves del diccionario deben coincidir con los nombres de las propiedades de los inmuebles.

**Valor de retorno:**

* Una lista de inmuebles que cumplen con los criterios de filtro.

### obtener_inmuebles_filtrados(filtros)

Obtiene una lista de inmuebles filtrados por los criterios especificados.

**Parámetros:**

* **filtros**: Diccionario con los criterios de filtro. Las claves del diccionario deben coincidir con los nombres de las propiedades de los inmuebles.

**Valor de retorno:**

* Una lista de diccionarios, donde cada diccionario representa un inmueble que cumple con los criterios de filtro.
