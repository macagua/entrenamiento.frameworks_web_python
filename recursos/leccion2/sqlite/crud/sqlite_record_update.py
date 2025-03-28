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
UPDATE_SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = ? WHERE id = ?;"""


def actualizar_registro(update_sql, update_values):
    """Función para la actualización de registro de la tabla"""

    conexion = None
    try:
        # Establecer la conexión con la base de datos
        conexion = sqlite3.connect(DB)
        # Crear un cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Actualizar nuevos registros en la tabla
        cursor.executemany(update_sql, update_values)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info(
            f"✅ ¡Fueron actualizado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la actualización de registro(s) en la tabla!: {error}"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!"
            )


if __name__ == "__main__":
    actualizar_registro(UPDATE_SQL_SCRIPTS, MULTIPLE_COLUMNS)
