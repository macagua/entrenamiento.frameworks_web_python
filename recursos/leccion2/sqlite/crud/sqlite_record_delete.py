"""Programa para la eliminación de registro de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE
SQL_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""


def eliminar_registro():
    """Función para la eliminación de registro de la tabla"""

    conexion = None
    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = sqlite3.connect(DB)
        # Crear un cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Ejecutar SQL
        cursor.execute(SQL_SCRIPTS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        # Cerrar cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(f"¡Fallo la eliminación de registro(s) en la tabla!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!\n"
            )


if __name__ == "__main__":
    eliminar_registro()
