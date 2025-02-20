"""Programa para la eliminación de registro de la tabla"""

import logging
import pymysql
import os

logging.basicConfig(level=logging.INFO)

DELETE_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""


def eliminar_registro():
    """Función para la eliminación de registro de la tabla"""

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
        # Crear un objeto cursor para ejecutar las eliminaciones
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos '{credenciales['database']}'!\n")
        # Eliminar un fila de registro simple
        cursor.execute(DELETE_SCRIPTS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        # Cerrar el cursor
        cursor.close()
    except pymysql.err.Error as error:
        logging.info(f"¡Fallo la eliminación de registro(s) en la tabla!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión MySQL a la base de datos '{credenciales['database']}' fue cerrada!\n"
            )


if __name__ == "__main__":
    eliminar_registro()
