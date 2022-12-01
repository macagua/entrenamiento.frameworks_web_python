from settings import *
from psycopg2 import (
    Error,
    OperationalError,
    ProgrammingError,
    connect,
    errors,
    errorcodes,
)


def crear_conexion(servidor, puerto, usuario, contrasena, bd):

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
        print("¡Conexión a la base de datos PostgreSQL fue exitosa!")
    except errors.SyntaxError:
        print("ERROR: ¡SQL Invalida!")
    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERROR: ¡Algo está mal con su nombre de usuario o contraseña!")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERROR: ¡La base de datos no existe!")
        else:
            print(f"ERROR: ¡Se produjo lo siguiente: '{e}'!")

    return conexion_bd


def crear_base_datos(conexion_bd, bd):

    conexion_bd.autocommit = True
    cursor = conexion_bd.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {bd}")
        print("¡Creación exitosa de la base de datos {bd}!\n")
    except ProgrammingError as e:
        print(f"ERROR: ¡Se produjo una falla de programación: '{e}'!")
    except OperationalError as e:
        print(f"ERROR: ¡Se produjo lo siguiente: '{e}'!")


if __name__ == "__main__":
    # Configurar conexion entre SQLAlchemy y PostgreSQL DB API
    conexion = crear_conexion(
        HOST_CONEXION, PUERTO_CONEXION, USUARIO_BD, CONTRASENA_BD, NOMBRE_BD
    )
    # Crear la base de datos
    crear_base_datos(conexion, NOMBRE_BD)
