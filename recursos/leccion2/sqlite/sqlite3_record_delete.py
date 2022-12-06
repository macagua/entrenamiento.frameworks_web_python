""" Programa para realizar la eliminación de registro de la tabla """

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE
SQL_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""


def eliminar_registro():
    """
    Función para realizar la eliminación de registro de la tabla
    """

    try:
        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {DB_FILE}!\n")

        # Eliminar un fila de registro simple
        cursor.execute(SQL_SCRIPTS)
        conexion.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        cursor.close()

    except sqlite3.Error as error:
        print("¡Fallo la eliminación de registro(s) en la tabla!", error)
    finally:
        if conexion:
            conexion.close()
            logging.info(
                "¡La conexión SQLite a la base de datos {} fue cerrada!\n".format(
                    DB_FILE
                )
            )


if __name__ == "__main__":
    eliminar_registro()
