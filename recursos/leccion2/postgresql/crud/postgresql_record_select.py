"""Programa para la consulta de registro(s) de la tabla"""

import logging
import psycopg2
import os

logging.basicConfig(level=logging.INFO)

# Script SELECT SQL a usar al consultar datos
SELECT_SCRIPTS = """SELECT * FROM clientes;"""


def consultar_registro():
    """Función para la consulta de registro(s) de la tabla"""

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
        # Crear un objeto cursor para ejecutar las consultas
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos '{credenciales['database']}'!\n")
        # Realizar consulta la tabla clientes
        cursor.execute(SELECT_SCRIPTS)
        # Recuperar los registros de la consulta
        registros = cursor.fetchall()
        # Mostrar los registros de la tabla
        print(f"Total de filas son: {len(registros)} \n")
        print("Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]} {fila[2]}")
            print(f"\tCódigo postal: {fila[3]}")
            print(f"\tTeléfono: {fila[4]}\n")
        # Cerrar el cursor
        cursor.close()
    except psycopg2.errors.Error as error:
        logging.error(f"¡Fallo la consulta de registro(s) en la tabla!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión PostgreSQL a la base de datos '{credenciales['database']}' fue cerrada!\n"
            )


if __name__ == "__main__":
    consultar_registro()
