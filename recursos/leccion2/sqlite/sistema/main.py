""" Programa para realizar operaciones a base de datos SQLite """

from settings import *
import logging
import os

from sqlite3 import Error, OperationalError, ProgrammingError, connect

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB = DB_PATH + DB_FILE


def crear_conexion(ruta):
    """Crear conexión con un servidor SQLite

    Args:
        ruta (str): La ruta completa usada para leer la base de datos

    Returns:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
    """
    conexion_bd = None
    try:
        conexion_bd = connect(ruta)
        logging.info(
            f"¡Conexión a la base de datos '{os.path.basename(ruta)}' fue exitosa!\n"
        )
    except ProgrammingError as e:
        print(f"ERROR: ¡Se produjo una falla de programación: '{e}'!")
    except OperationalError as e:
        print(f"ERROR: Se produjo lo siguiente: '{e}'")

    return conexion_bd


def insertar_registro(conexion_bd, insert_values, insert_sql):
    """Función para la inserción de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        insert_values (list): Lista de filas a ingresar
        insert_sql (str): Script INSERT SQL a usar al ingresar datos
    """

    try:
        cursor = conexion_bd.cursor()
        count = cursor.executemany(insert_sql, insert_values)
        conexion.commit()
        logging.info(
            "¡Fueron insertado(s) {} registro(s) correctamente en la tabla!\n".format(
                cursor.rowcount
            )
        )
        cursor.close()
    except Error as error:
        print("¡Fallo la inserción de registro(s) en la tabla!", error)


def consultar_registro(conexion_bd, select_sql):
    """Función para la consulta de registro(s) de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        select_sql (str): Script SELECT SQL a usar al consultar datos
    """

    try:
        cursor = conexion_bd.cursor()
        cursor.execute(select_sql)
        registros = cursor.fetchall()

        print(f"Total de filas son: {len(registros)} \n")
        print("Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]}")
            print(f"\tCódigo postal: {fila[2]}")
            print(f"\tTeléfono: {fila[3]}\n")

        cursor.close()

    except Error as error:
        print("¡Fallo la consulta de registro(s) en la tabla!", error)


def actualizar_registro(conexion_bd, update_values, update_sql):
    """Función para la actualización de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        update_values (list): Lista de filas a actualizar
        update_sql (str): _description_
    """

    try:
        cursor = conexion_bd.cursor()
        count = cursor.executemany(update_sql, update_values)
        conexion.commit()
        logging.info(
            "¡Fueron actualizado(s) {} registro(s) correctamente en la tabla!\n".format(
                cursor.rowcount
            )
        )
        cursor.close()

    except Error as error:
        print("¡Fallo la actualización de registro(s) en la tabla!", error)


def eliminar_registro(conexion_bd, delete_sql):
    """Función para la eliminación de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        delete_sql (str): Script DELETE SQL a usar al eliminar datos
    """

    try:
        cursor = conexion_bd.cursor()
        cursor.execute(delete_sql)
        conexion.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        cursor.close()

    except Error as error:
        print("¡Fallo la eliminación de registro(s) en la tabla!", error)


if __name__ == "__main__":
    conexion = crear_conexion(DB)
    insertar_registro(conexion, INSERT_MULTIPLE_COLUMNS, INSERT_SQL_SCRIPTS)
    consultar_registro(conexion, SELECT_SQL_SCRIPTS)
    actualizar_registro(conexion, UPDATE_MULTIPLE_COLUMNS, UPDATE_SQL_SCRIPTS)
    eliminar_registro(conexion, DELETE_SQL_SCRIPTS)
