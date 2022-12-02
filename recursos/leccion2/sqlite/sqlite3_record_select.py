""" Programa para realizar la consulta de registro(s) de la tabla """

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

NOMBRE_ARCHIVO = "sistema.db"
DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__)) + os.sep
ARCHIVO = DIR_ARCHIVO + NOMBRE_ARCHIVO
SQL_SCRIPTS = """SELECT * FROM clientes;"""


def consultar_registro():
    """
    Función para realizar la consulta de registro(s) de la tabla
    """

    try:
        conexion = sqlite3.connect(ARCHIVO)
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {NOMBRE_ARCHIVO}!\n")

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
            conexion.close()
            logging.info(
                "¡La conexión SQLite a la base de datos {} fue cerrada!\n".format(
                    NOMBRE_ARCHIVO
                )
            )


if __name__ == "__main__":
    consultar_registro()
