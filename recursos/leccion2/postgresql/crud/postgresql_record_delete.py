"""Programa para la eliminación de registro de la tabla"""

import logging
import psycopg2

logging.basicConfig(level=logging.INFO)

# Script DELETE SQL a usar al eliminar datos
DELETE_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""


def eliminar_registro():
    """Función para la eliminación de registro de la tabla"""

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
        # Crear un objeto cursor para ejecutar las eliminaciones
        cursor = conexion.cursor()
        logging.info(f"✅ ¡Conectado a la base de datos '{credenciales['database']}'!\n")
        # Eliminar un fila de registro simple
        cursor.execute(DELETE_SCRIPTS)
        # Guardar los cambios en la base de datos
        conexion.commit()
        logging.info("✅ ¡Registro eliminado correctamente!\n")
        # Cerrar el cursor
        cursor.close()
    except psycopg2.Error as error:
        logging.error(
            f"❌ ERROR: ¡Fallo la eliminación de registro(s) en la tabla!: {error}"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión PostgreSQL a la base de datos '{credenciales['database']}' fue cerrada!\n"
            )


if __name__ == "__main__":
    eliminar_registro()
