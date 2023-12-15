"""Programa para la actualización de registro de la tabla"""

import logging
import psycopg2
import os

logging.basicConfig(level=logging.INFO)

# Creando una lista de filas a actualizar
MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = ? WHERE id = ?;"""


def actualizar_registro():
    """Función para la actualización de registro de la tabla"""

    try:
        credenciales = {
            host:"localhost",
            database:"mercantil",
            user:"postgres",
            password:"postgres"
        }
        # Establecer la conexión con la base de datos
        conexion = psycopg2.connect(**credenciales)

        # Crear un objeto cursor para ejecutar las actualizaciones
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {credenciales['database']}!\n")

        cursor.executemany(SQL_SCRIPTS, MULTIPLE_COLUMNS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info(
            "¡Fueron actualizado(s) {} registro(s) correctamente en la tabla!\n".format(
                cursor.rowcount
            )
        )
        cursor.close()

    except psycopg2.errors.Error as error:
        print("¡Fallo la actualización de registro(s) en la tabla!", error)
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión PostgreSQL a la base de datos {credenciales['database']} fue cerrada!\n"
            )


if __name__ == "__main__":
    actualizar_registro()
