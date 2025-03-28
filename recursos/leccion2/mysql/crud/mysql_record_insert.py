"""Programa para la inserción de registro(s) de la tabla"""

import logging
import pymysql

logging.basicConfig(level=logging.INFO)

# Script CREATE TABLE SQL para crear tabla clientes
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    codigo_postal INT NOT NULL,
    telefono VARCHAR(20) NOT NULL
);"""

# Creando una lista de filas a ingresar
MULTIPLE_COLUMNS = [
    (1, "Leonardo", "Caballero", "5001", "+58-412-4734567"),
    (2, "Ana", "Poleo", "6302", "+58-426-5831297"),
    (3, "Manuel", "Matos", "4001", "+58-414-2360943"),
]

# Script INSERT SQL a usar al ingresar datos
INSERT_SQL_SCRIPTS = """INSERT INTO clientes VALUES (%s, %s, %s, %s, %s);"""


def insertar_registro(create_table_sql, insert_sql, insert_values):
    """Función para la inserción de registro de la tabla"""

    conexion = None
    credenciales = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "sistema",
    }
    try:
        # Establecer la conexión con la base de datos
        conexion = pymysql.connect(
            host=credenciales["host"],
            user=credenciales["user"],
            password=credenciales["password"],
            database=credenciales["database"],
        )
        # Crear un objeto cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{credenciales['database']}'!\n")
        # Crear la tabla productos si no existe
        cursor.execute(create_table_sql)
        # Confirmar la creación de la tabla
        conexion.commit()
        logging.info(
            f"✅ ¡Fue creo una tabla correctamente en la base de datos '{credenciales['database']}'!\n"
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
    except pymysql.err.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la inserción de registro(s) en la tabla!: {error}"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión MySQL a la base de datos '{credenciales['database']}' fue cerrada!"
            )


if __name__ == "__main__":
    insertar_registro(CREATE_TABLE_SQL, INSERT_SQL_SCRIPTS, MULTIPLE_COLUMNS)
