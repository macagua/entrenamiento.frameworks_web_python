"""Programa para la consulta de registro(s) de la tabla"""

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

    conexion = None
    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = sqlite3.connect(DB)
        # Crear un cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Ejecutar SQL
        cursor.execute(SQL_SCRIPTS)
        # Recupera todas las filas de los resultados de una consulta
        registros = cursor.fetchall()
        # Mostrar registros
        print(f"Total de filas son: {len(registros)} \n")
        print("Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]}")
            print(f"\tApellido: {fila[2]}")
            print(f"\tCódigo postal: {fila[3]}\n")
        # Cerrar cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(f"¡Fallo la consulta de registro(s) en la tabla!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!\n"
            )


if __name__ == "__main__":
    consultar_registro()
