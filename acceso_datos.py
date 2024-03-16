import pymysql

def obtener_conexion():
    return pymysql.connect(
        host="3.138.156.32",
        user="pruebas",
        password="VGbt3Day5R",
        database="habi_db",
        port=3309,
    )

def obtener_inmuebles(filtros):
    connection = obtener_conexion()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT p.id, p.address, p.city, sh.status_id, s.name AS estado, p.price, p.description, p.year
            FROM habi_db.property p
            INNER JOIN habi_db.status_history sh ON p.id = sh.property_id
            INNER JOIN habi_db.status s ON sh.status_id = s.id
            ORDER BY sh.update_date DESC
        """)
        inmuebles = cursor.fetchall()
        return [dict(zip(["id", "address", "city", "status_id", "estado", "price", "description", "year"], tupla)) for tupla in inmuebles]
    except pymysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return []
    finally:
        cursor.close()
        connection.close()
