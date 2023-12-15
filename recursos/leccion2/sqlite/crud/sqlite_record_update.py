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

SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = ? WHERE id = ?;"""


def actualizar_registro():
    """Función para la actualización de registro de la tabla"""

    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {DB_FILE}!\n")

        count = cursor.executemany(SQL_SCRIPTS, MULTIPLE_COLUMNS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info(
            "¡Fueron actualizado(s) {} registro(s) correctamente en la tabla!\n".format(
                cursor.rowcount
            )
        )
        cursor.close()

    except sqlite3.Error as error:
        print("¡Fallo la actualización de registro(s) en la tabla!", error)
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                "¡La conexión SQLite a la base de datos {} fue cerrada!\n".format(
                    DB_FILE
                )
            )


if __name__ == "__main__":
    actualizar_registro()
