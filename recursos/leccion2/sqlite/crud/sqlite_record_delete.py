"""Programa para la eliminación de registro de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE

# Script DELETE SQL a usar al eliminar datos
DELETE_SQL_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""


def eliminar_registro(delete_sql):
    """Función para la eliminación de registro de la tabla"""

    conexion = None
    try:
        # Establecer la conexión con la base de datos
        conexion = sqlite3.connect(DB)
        # Crear un objeto cursor para ejecutar las eliminaciones
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Eliminar un fila de registro simple
        cursor.execute(delete_sql)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info("✅ ¡Registro eliminado correctamente!\n")
        # Cerrar el cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la eliminación de registro(s) en la tabla!: {error}"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!"
            )


if __name__ == "__main__":
    eliminar_registro(DELETE_SQL_SCRIPTS)
