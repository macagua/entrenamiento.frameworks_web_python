"""Programa para la actualización de registro de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE

# Creando una lista de filas a actualizar
MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

# Script UPDATE SQL a usar al actualizar datos
UPDATE_SCRIPTS = """UPDATE clientes SET codigo_postal = ? WHERE id = ?;"""


def actualizar_registro():
    """Función para la actualización de registro de la tabla"""

    conexion = None
    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = sqlite3.connect(DB)
        # Crear un cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Ejecutar SQL
        cursor.executemany(UPDATE_SCRIPTS, MULTIPLE_COLUMNS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info(
            f"¡Fueron actualizado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(f"¡Fallo la actualización de registro(s) en la tabla!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!\n"
            )


if __name__ == "__main__":
    actualizar_registro()
