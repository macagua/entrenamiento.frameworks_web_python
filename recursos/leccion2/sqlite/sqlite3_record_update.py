""" Programa para realizar la actualización de registro de la tabla """

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

NOMBRE_ARCHIVO = "sistema.db"
DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__)) + os.sep
ARCHIVO = DIR_ARCHIVO + NOMBRE_ARCHIVO

# Creando una lista de filas a actualizar
MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = ? WHERE id = ?;"""


def actualizar_registro():
    """
    Función para realizar la actualización de registro de la tabla
    """

    try:
        conexion = sqlite3.connect(ARCHIVO)
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {NOMBRE_ARCHIVO}!\n")

        count = cursor.executemany(SQL_SCRIPTS, MULTIPLE_COLUMNS)
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
            conexion.close()
            logging.info(
                "¡La conexión SQLite a la base de datos {} fue cerrada!\n".format(
                    NOMBRE_ARCHIVO
                )
            )


if __name__ == "__main__":
    actualizar_registro()
