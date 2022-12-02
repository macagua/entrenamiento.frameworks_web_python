""" Programa para realizar operaciones a base de datos MySQL """

import logging

from settings import *
from pymysql import Error, OperationalError, ProgrammingError, connect, constants, err

logging.basicConfig(level=logging.INFO)


def crear_conexion(servidor, puerto, usuario, contrasena, bd):
    """Crear conexión con un servidor MySQL

    Args:
        servidor (str): IP o dirección DNS de conexión al servidor de la base de datos.
        puerto (int): Puerto de conexión al servidor de la base de datos.
        usuario (str): Usuario de conexión a la base de datos.
        contrasena (str): Contraseña del usuario de conexión a la base de datos.
        bd (str): Nombre de la base de datos a cual conectar.

    Returns:
        conexion_bd (Connection): Representación de un socket con un servidor MySQL
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
    except Error as err:
        if err == constants.ER.ACCESS_DENIED_ERROR:
            print(
                "\x1b[1;31mERROR: ¡Algo está mal con su nombre de usuario o contraseña!"
            )
        elif err == constants.ER.BAD_DB_ERROR:
            print("\x1b[1;31mERROR: ¡La base de datos no existe!")
        else:
            print(f"\x1b[1;31mERROR: ¡Se produjo lo siguiente: '{err}'")

    return conexion_bd


def crear_base_datos(conexion_bd, bd):
    """Crear la base de datos

    Args:
        conexion_bd (Connection): Representación de un socket con un servidor MySQL
        bd (str): Nombre de la base de datos a cual conectar.
    """

    conexion_bd.autocommit = True
    cursor = conexion_bd.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {bd}")
        logging.info(f"¡Creación exitosa de la base de datos '{bd}'!\n")
    except err.SyntaxError:
        print("ERROR: ¡SQL Invalida!")
    except ProgrammingError as e:
        print(f"ERROR: ¡Se produjo una falla de programación: '{e}'!")
    except OperationalError as e:
        print(f"ERROR: Se produjo lo siguiente: '{e}'")


if __name__ == "__main__":
    # Crear conexión con un servidor MySQL
    conexion = crear_conexion(HOST, PORT, USER, PASSW, DB)
    # Crear la base de datos
    crear_base_datos(conexion, DB)
