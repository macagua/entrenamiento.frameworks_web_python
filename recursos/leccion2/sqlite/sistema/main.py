"""Programa para realizar operaciones a base de datos SQLite"""

import logging
from settings import (
    DB_FILE,
    INSERT_MULTIPLE_COLUMNS,
    INSERT_SQL_SCRIPTS,
    SELECT_SQL_SCRIPTS,
    UPDATE_MULTIPLE_COLUMNS,
    UPDATE_SQL_SCRIPTS,
    DELETE_SQL_SCRIPTS,
)
import os
from sqlite3 import Error, OperationalError, ProgrammingError, connect

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB = DB_PATH + (DB_FILE or "")


def crear_conexion(ruta):
    """Crear conexión con un servidor SQLite

    Args:
        ruta (str): La ruta completa usada para leer la base de datos

    Returns:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
    """
    conexion_bd = None
    try:
        # Establecer la conexión con la base de datos
        conexion_bd = connect(ruta)
        logging.info(
            f"¡Conexión a la base de datos '{os.path.basename(ruta)}' fue exitosa!\n"
        )
    except ProgrammingError as e:
        logging.error(f"ERROR: ¡Se produjo una falla de programación: '{e}'!")
    except OperationalError as e:
        logging.error(f"ERROR: Se produjo lo siguiente: '{e}'")
    return conexion_bd


def insertar_registro(conexion_bd, insert_values, insert_sql):
    """Función para la inserción de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        insert_values (list): Lista de filas a ingresar
        insert_sql (str): Script INSERT SQL a usar al ingresar datos
    """
    try:
        # Crear un objeto cursor para ejecutar script SQL
        cursor = conexion_bd.cursor()
        # Insertar nuevos registros en la tabla
        cursor.executemany(insert_sql, insert_values)
        # Confirmar la inserción de los registros
        conexion_bd.commit()
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la inserción de registro(s) en la tabla!: {error}")


def consultar_registro(conexion_bd, select_sql):
    """Función para la consulta de registro(s) de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        select_sql (str): Script SELECT SQL a usar al consultar datos
    """
    try:
        # Crear un objeto cursor para ejecutar script SQL
        cursor = conexion_bd.cursor()
        # Realizar consulta la tabla clientes
        cursor.execute(select_sql)
        # Recuperar los registros de la consulta
        registros = cursor.fetchall()
        # Mostrar los registros de la tabla
        print(f"Total de filas son: {len(registros)} \n")
        print("Mostrar cada fila: \n")
        for fila in registros:
            print(f"\tId: {fila[0]}")
            print(f"\tNombre: {fila[1]}")
            print(f"\tApellido: {fila[2]}")
            print(f"\tCódigo postal: {fila[3]}\n")
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la consulta de registro(s) en la tabla!: {error}")


def actualizar_registro(conexion_bd, update_values, update_sql):
    """Función para la actualización de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        update_values (list): Lista de filas a actualizar
        update_sql (str): _description_
    """
    try:
        # Crear un objeto cursor para ejecutar script SQL
        cursor = conexion_bd.cursor()
        # Actualizar nuevos registros en la tabla
        cursor.executemany(update_sql, update_values)
        # Guardar los cambios en la base de datos
        conexion_bd.commit()
        logging.info(
            f"¡Fueron actualizado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la actualización de registro(s) en la tabla!: {error}")


def eliminar_registro(conexion_bd, delete_sql):
    """Función para la eliminación de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos SQLite
        delete_sql (str): Script DELETE SQL a usar al eliminar datos
    """
    try:
        # Crear un objeto cursor para ejecutar script SQL
        cursor = conexion_bd.cursor()
        # Eliminar un fila de registro simple
        cursor.execute(delete_sql)
        # Guardar los cambios en la base de datos
        conexion_bd.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la eliminación de registro(s) en la tabla!: {error}")


if __name__ == "__main__":
    # Crear conexión a SQLite
    conexion = crear_conexion(DB)
    insertar_registro(conexion, INSERT_MULTIPLE_COLUMNS, INSERT_SQL_SCRIPTS)
    consultar_registro(conexion, SELECT_SQL_SCRIPTS)
    actualizar_registro(conexion, UPDATE_MULTIPLE_COLUMNS, UPDATE_SQL_SCRIPTS)
    eliminar_registro(conexion, DELETE_SQL_SCRIPTS)
