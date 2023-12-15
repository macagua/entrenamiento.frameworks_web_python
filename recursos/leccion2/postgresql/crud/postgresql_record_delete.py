"""Programa para la eliminación de registro de la tabla"""

import logging
import psycopg2
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE
SQL_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""


def eliminar_registro():
    """Función para la eliminación de registro de la tabla"""

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

        # Eliminar un fila de registro simple
        cursor.execute(SQL_SCRIPTS)

        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        cursor.close()

    except psycopg2.Error as error:
        print("¡Fallo la eliminación de registro(s) en la tabla!", error)
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión PostgreSQL a la base de datos {credenciales['database']} fue cerrada!\n"
            )


if __name__ == "__main__":
    eliminar_registro()
