Acceso a Aplicacion de Inmuebles
===========================

# Aplicación Inmuebles

## Descripción

Esta aplicación web es una API RESTful que permite a los usuarios buscar inmuebles por diferentes criterios. La API expone un endpoint para filtrar inmuebles y devuelve los resultados en formato JSON.

## Arquitectura

La aplicación está implementada con Python utilizando el módulo `http.server` para crear un servidor HTTP simple.

## Funcionalidades

* **Búsqueda de inmuebles:** Los usuarios pueden enviar solicitudes GET a la API para buscar inmuebles utilizando filtros.

## Endpoint

* **GET /inmuebles**: Este endpoint recibe un cuerpo de petición con un diccionario JSON que contiene los criterios de filtro para los inmuebles. La API devuelve una lista de inmuebles en formato JSON que cumplen con los criterios especificados.

## Parámetros de la petición

  * **filtros (JSON)**: Diccionario con los criterios de filtro para los inmuebles. Las claves del diccionario deben coincidir con los nombres de las propiedades de los inmuebles.

## Valor de retorno

* **Lista de inmuebles (JSON)**: Una lista de objetos JSON, donde cada objeto representa un inmueble con sus respectivas propiedades.

## Ejemplo de uso

**Solicitud GET:**

curl -X GET http://localhost:5000/inmuebles -H "Content-Type: application/json" -d '{"ciudad": "Bogotá", "precio_minimo": 100000}'

**Respuesta de la API (formato JSON):**

```json
[
  {
    "id": 123,
    "address": "Calle 123",
    "city": "Bogotá",
    "price": 200000,
    "description": "Apartamento en el centro de la ciudad"
  },
  {
    "id": 456,
    "address": "Avenida Principal",
    "city": "Bogotá",
    "price": 300000,
    "description": "Casa con jardín"
  }
]