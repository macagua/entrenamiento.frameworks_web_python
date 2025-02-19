"""Programa para la actualización de registro de la tabla"""

import logging
import pymysql
import os

logging.basicConfig(level=logging.INFO)

# Creando una lista de filas a actualizar
MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

UPDATE_SCRIPTS = """UPDATE clientes SET codigo_postal = %s WHERE id = %s;"""


def actualizar_registro():
    """Función para la actualización de registro de la tabla"""

    conexion = None
    credenciales = {
        "host": "localhost",  # Servidor MySQL (localhost si está en tu máquina)
        "user": "root",  # Usuario de MySQL
        "password": "root",  # Contraseña de MySQL
        "database": "sistema",  # Nombre de la base de datos
    }
    try:
        # Establecer la conexión con la base de datos
        conexion = pymysql.connect(
            host=credenciales["host"],
            user=credenciales["user"],
            password=credenciales["password"],
            database=credenciales["database"],
        )
        # Crear un objeto cursor para ejecutar las actualizaciones
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos '{credenciales['database']}'!\n")
        # Actualizar nuevos registros en la tabla
        cursor.executemany(UPDATE_SCRIPTS, MULTIPLE_COLUMNS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info(
            f"¡Fueron actualizado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except pymysql.err.Error as error:
        logging.info(f"¡Fallo la actualización de registro(s) en la tabla!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión MySQL a la base de datos '{credenciales['database']}' fue cerrada!\n"
            )


if __name__ == "__main__":
    actualizar_registro()
