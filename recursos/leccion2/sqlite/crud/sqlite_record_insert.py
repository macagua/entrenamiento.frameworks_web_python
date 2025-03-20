"""Programa para la inserción de registro(s) de la tabla"""

import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = "sistema.db"
DB = DB_PATH + DB_FILE

# Script CREATE TABLE SQL para crear tabla clientes
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER UNIQUE NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    codigo_postal INTEGER NOT NULL,
    telefono TEXT NOT NULL,
    PRIMARY KEY(id)
);"""

# Creando una lista de filas a ingresar
MULTIPLE_COLUMNS = [
    (1, "Leonardo", "Caballero", "5001", "+58-412-4734567"),
    (2, "Ana", "Poleo", "6302", "+58-426-5831297"),
    (3, "Manuel", "Matos", "4001", "+58-414-2360943"),
]

# Script INSERT SQL a usar al ingresar datos
INSERT_SQL_SCRIPTS = """INSERT INTO clientes VALUES (?, ?, ?, ?, ?);"""


def insertar_registro(create_table_sql, insert_sql, insert_values):
    """Función para la inserción de registro de la tabla"""

    conexion = None
    try:
        # Establecer la conexión con la base de datos
        conexion = sqlite3.connect(DB)
        # Crear un objeto cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{DB_FILE}'!\n")
        # Crear la tabla productos si no existe
        cursor.execute(create_table_sql)
        # Confirmar la creación de la tabla
        conexion.commit()
        logging.info(
            f"✅ ¡Fue creo una tabla correctamente en la base de datos '{DB_FILE}'!\n"
        )
        # Insertar nuevos registros en la tabla
        cursor.executemany(insert_sql, insert_values)
        # Confirmar la inserción de los registros
        conexion.commit()
        logging.info(
            f"✅ ¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Insertar un nuevo registro en la tabla
        cursor.execute(
            insert_sql, (4, "Liliana", "Andradez", "3105", "+58-414-6782473")
        )
        # Confirmar la inserción del registro
        conexion.commit()
        logging.info(
            f"✅ ¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except sqlite3.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la inserción de registro(s) en la tabla!: {error}\n"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!"
            )


if __name__ == "__main__":
    insertar_registro(CREATE_TABLE_SQL, INSERT_SQL_SCRIPTS, MULTIPLE_COLUMNS)
