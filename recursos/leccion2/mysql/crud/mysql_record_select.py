"""Programa para la consulta de registro(s) de la tabla"""

import logging
import pymysql
import os

logging.basicConfig(level=logging.INFO)

SELECT_SCRIPTS = """SELECT * FROM clientes;"""


def consultar_registro():
    """Función para la consulta de registro(s) de la tabla"""

    conexion = None
    credenciales = {
        "host": "localhost",  # Servidor MySQL (localhost si está en tu máquina)
        "user": "root",  # Usuario de MySQL
        "password": "root",  # Contraseña de MySQL
        "database": "sistema",  # Nombre de la base de datos
    }
    try:
        # Establecer la conexión con la base de datos
        conexion = pymysql.connect(
            host=credenciales["host"],
            user=credenciales["user"],
            password=credenciales["password"],
            database=credenciales["database"],
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
    except pymysql.err.Error as error:
        print("¡Fallo la consulta de registro(s) en la tabla!", error)
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"¡La conexión MySQL a la base de datos '{credenciales['database']}' fue cerrada!\n"
            )


if __name__ == "__main__":
    consultar_registro()
