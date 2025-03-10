"""Programa para la consulta de registro(s) de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE

# Script SELECT SQL a usar al consultar datos
SELECT_SCRIPTS = """SELECT * FROM clientes;"""


def consultar_registro():
    """Función para la consulta de registro(s) de la tabla"""

    conexion = None
    try:
        # Establecer la conexión con la base de datos
        conexion = sqlite3.connect(DB)
        # Crear un objeto cursor para ejecutar las consultas
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Realizar consulta la tabla clientes
        cursor.execute(SELECT_SCRIPTS)
        # Recuperar los registros de la consulta
        registros = cursor.fetchall()
        # Mostrar los registros de la tabla
        print(f"📜 Total de filas son: {len(registros)} \n")
        print("📜 Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]} {fila[2]}")
            print(f"\tCódigo postal: {fila[3]}")
            print(f"\tTeléfono: {fila[4]}\n")
        # Cerrar el cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la consulta de registro(s) en la tabla!: {error}"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!"
            )


if __name__ == "__main__":
    consultar_registro()
