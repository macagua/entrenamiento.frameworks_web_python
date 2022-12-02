""" Programa para realizar operaciones a base de datos PostgreSQL """

import logging

from settings import *
from psycopg2 import OperationalError, ProgrammingError, connect, errors

logging.basicConfig(level=logging.INFO)


def crear_conexion(servidor, puerto, usuario, contrasena, bd):
    """Crear conexión con un servidor PostgreSQL

    Args:
        servidor (str): IP o dirección DNS de conexión al servidor de la base de datos.
        puerto (int): Puerto de conexión al servidor de la base de datos.
        usuario (str): Usuario de conexión a la base de datos.
        contrasena (str): Contraseña del usuario de conexión a la base de datos.
        bd (str): Nombre de la base de datos a cual conectar.

    Returns:
        conexion_bd (Connection): Representación de un socket con un servidor PostgreSQL
    """

    conexion_bd = None
    config = {
        "user": usuario,
        "password": contrasena,
        "host": servidor,
        "port": puerto,
        "database": bd,
    }

    try:
        conexion_bd = connect(**config)
        logging.info(
            f"¡Conexión a la base de datos '{config['database']}' fue exitosa!\n"
        )
    except OperationalError as e:
        print(f"ERROR: Se produjo lo siguiente: {e}")

    return conexion_bd


def crear_base_datos(conexion_bd, bd):
    """Crear la base de datos

    Args:
        conexion_bd (Connection): Representación de un socket con un servidor PostgreSQL
        bd (str): Nombre de la base de datos a cual conectar.
    """

    conexion_bd.autocommit = True
    cursor = conexion_bd.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {bd}")
        logging.info(f"¡Creación exitosa de la base de datos '{bd}'!\n")
    except errors.SyntaxError:
        print("ERROR: ¡SQL Invalida!")
    except ProgrammingError as e:
        print(f"ERROR: ¡Se produjo una falla de programación: '{e}'!")
    except OperationalError as e:
        print(f"ERROR: Se produjo lo siguiente: '{e}'")


if __name__ == "__main__":
    # Crear conexión con un servidor PostgreSQL
    conexion = crear_conexion(HOST, PORT, USER, PASSW, DB)
    # Crear la base de datos
    crear_base_datos(conexion, DB)
