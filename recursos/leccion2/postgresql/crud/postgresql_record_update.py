"""Programa para la actualización de registro de la tabla"""

import logging
import psycopg2

logging.basicConfig(level=logging.INFO)

# Creando una lista de filas a actualizar
MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

# Script UPDATE SQL a usar al actualizar datos
UPDATE_SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = %s WHERE id = %s;"""


def actualizar_registro(update_sql, update_values):
    """Función para la actualización de registro de la tabla"""

    conexion = None
    credenciales = {
        "host": "127.0.0.1",
        "port": "5433",
        "database": "sistema",
        "user": "postgres",
        "password": "postgres",
    }
    try:
        # Establecer la conexión con la base de datos
        conexion = psycopg2.connect(
            host=credenciales["host"],
            port=credenciales["port"],
            database=credenciales["database"],
            user=credenciales["user"],
            password=credenciales["password"],
        )
        # Crear un cursor para la base de datos
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{credenciales['database']}'!\n")
        # Actualizar nuevos registros en la tabla
        cursor.executemany(update_sql, update_values)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info(
            f"✅ ¡Fueron actualizado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except psycopg2.errors.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la actualización de registro(s) en la tabla!: {error}"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión PostgreSQL a la base de datos '{credenciales['database']}' fue cerrada!"
            )


if __name__ == "__main__":
    actualizar_registro(UPDATE_SQL_SCRIPTS, MULTIPLE_COLUMNS)
