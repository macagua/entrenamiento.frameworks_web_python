"""Programa para la consulta de registro(s) de la tabla"""

import logging
import psycopg2
import os

logging.basicConfig(level=logging.INFO)

SQL_SCRIPTS = """SELECT * FROM clientes;"""


def consultar_registro():
    """Función para la consulta de registro(s) de la tabla"""

    try:
        credenciales = {
            host:"localhost",
            database:"mercantil",
            user:"postgres",
            password:"postgres"
        }
        # Establecer la conexión con la base de datos
        conexion = psycopg2.connect(**credenciales)

        # Crear un objeto cursor para ejecutar las consultas
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {credenciales['database']}!\n")

        # Realizar consulta la tabla clientes
        cursor.execute(SQL_SCRIPTS)
        registros = cursor.fetchall()

        print(f"Total de filas son: {len(registros)} \n")
        print("Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]} {fila[2]}")
            print(f"\tCódigo postal: {fila[3]}")
            print(f"\tTeléfono: {fila[5]}\n")

        cursor.close()

    except psycopg2.errors.Error as error:
        print("¡Fallo la consulta de registro(s) en la tabla!", error)
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión PostgreSQL a la base de datos {credenciales['database']} fue cerrada!\n"
            )


if __name__ == "__main__":
    consultar_registro()
