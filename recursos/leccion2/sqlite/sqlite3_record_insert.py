"""Programa para realizar la inserción de registro(s) de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE

# Creando una lista de filas a ingresar
MULTIPLE_COLUMNS = [
    (1, "Leonardo", "Caballero", "5001", "+58-412-4734567"),
    (2, "Ana", "Poleo", "6302", "+58-426-5831297"),
    (3, "Pedro", "Lopez", "4001", "+58-414-2360943"),
]

SQL_SCRIPTS = """INSERT INTO clientes VALUES (?, ?, ?, ?, ?);"""


def insertar_registro():
    """Función para la inserción de registro de la tabla"""

    try:
        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {DB_FILE}!\n")

        count = cursor.executemany(SQL_SCRIPTS, MULTIPLE_COLUMNS)
        conexion.commit()
        logging.info(
            "¡Fueron insertado(s) {} registro(s) correctamente en la tabla!\n".format(
                cursor.rowcount
            )
        )
        cursor.close()

    except sqlite3.Error as error:
        print("¡Fallo la inserción de registro(s) en la tabla!", error)
    finally:
        if conexion:
            conexion.close()
            logging.info(
                "¡La conexión SQLite a la base de datos {} fue cerrada!\n".format(
                    DB_FILE
                )
            )


if __name__ == "__main__":
    insertar_registro()
