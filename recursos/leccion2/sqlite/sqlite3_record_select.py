"""Programa para realizar la consulta de registro(s) de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE
SQL_SCRIPTS = """SELECT * FROM clientes;"""


def consultar_registro():
    """Función para la consulta de registro(s) de la tabla"""

    try:
        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {DB_FILE}!\n")

        cursor.execute(SQL_SCRIPTS)
        registros = cursor.fetchall()

        print(f"Total de filas son: {len(registros)} \n")
        print("Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]}")
            print(f"\tCódigo postal: {fila[2]}")
            print(f"\tTeléfono: {fila[3]}\n")

        cursor.close()

    except sqlite3.Error as error:
        print("¡Fallo la consulta de registro(s) en la tabla!", error)
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
    consultar_registro()
