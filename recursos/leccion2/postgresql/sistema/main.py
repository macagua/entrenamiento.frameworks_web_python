"""Programa para realizar operaciones a base de datos PostgreSQL"""

import logging
from settings import (
    USER,
    PASSW,
    HOST,
    PORT,
    DB,
    CREATE_DATABASE_SQL,
    CREATE_TABLE_SQL,
    INSERT_MULTIPLE_COLUMNS,
    INSERT_SQL_SCRIPTS,
    SELECT_SQL_SCRIPTS,
    UPDATE_MULTIPLE_COLUMNS,
    UPDATE_SQL_SCRIPTS,
    DELETE_SQL_SCRIPTS,
)
from psycopg2.errors import Error, DatabaseError, OperationalError, ProgrammingError
from psycopg2 import connect

logging.basicConfig(level=logging.INFO)


def crear_conexion(servidor, puerto, usuario, contrasena, bd):
    """Creación conexión con un servidor PostgreSQL

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
    credenciales = {
        "user": usuario,
        "password": contrasena,
        "host": servidor,
        "port": puerto,
        "database": bd,
    }
    try:
        # Establecer la conexión con la base de datos
        conexion_bd = connect(
            host=credenciales["host"],
            port=credenciales["port"],
            user=credenciales["user"],
            password=credenciales["password"],
            database=credenciales["database"],
        )
        logging.info(
            f"¡Conexión a la base de datos '{credenciales['database']}' fue exitosa!\n"
        )
    except OperationalError as e:
        logging.error(
            f"ERROR: Se produjo n error de operación de la base de datos: {e}"
        )
    except DatabaseError as e:
        logging.error(f"ERROR: Se produjo lo siguiente: {e}")
    return conexion_bd


def crear_base_datos(conexion_bd, create_database_sql, bd):
    """Creación la base de datos

    Args:
        conexion_bd (Connection): Representación de un socket con un servidor PostgreSQL
        create_database_sql (str): Script CREATE DATABASE SQL para crear la base de datos
        bd (str): Nombre de la base de datos a crear.
    """
    # Crear un objeto cursor para ejecutar script SQL
    cursor = conexion_bd.cursor()
    try:
        # Crear una base de datos en el servidor MySQL
        cursor.execute(create_database_sql)
        logging.info(f"¡Creación exitosa de la base de datos '{bd}'!\n")
    except SyntaxError as e:
        logging.error("ERROR: ¡SQL Invalida: '{e}'!")
    except ProgrammingError as e:
        logging.error(f"ERROR: ¡Se produjo una falla de programación: '{e}'!")
    except OperationalError as e:
        logging.error(f"ERROR: Se produjo lo siguiente: '{e}'")
    return conexion_bd


def crear_tablas(conexion_bd, create_table_sql):
    """Creación de tabla(s) dentro de la base de datos

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos MySQL
        create_table_sql (str): Script CREATE TABLE SQL para crear tabla(s)
    """
    try:
        # Crear un objeto cursor para ejecutar script SQL
        cursor = conexion_bd.cursor()
        # Crear la tabla(s) si no existe
        cursor.execute(create_table_sql)
        # Confirmar la creación de la tabla
        conexion_bd.commit()
        logging.info(
            f"¡Fueron creado(s) {cursor.rowcount} tabla(s) correctamente en la base de datos!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la creación de tabla(s) en la base de datos!: {error}")


def insertar_registro(conexion_bd, insert_values, insert_sql):
    """pass"""
    try:
        # Crear un objeto cursor para ejecutar las consultas
        cursor = conexion_bd.cursor()
        # Insertar nuevos registros en la tabla
        cursor.executemany(INSERT_SQL_SCRIPTS, INSERT_MULTIPLE_COLUMNS)
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Insertar un nuevo registro en la tabla
        cursor.execute(
            INSERT_SQL_SCRIPTS, (4, "Liliana", "Andradez", "4001", "+58-414-6782473")
        )
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la inserción de registro(s) en la tabla!: {error}")


def consultar_registro(conexion_bd, select_sql):
    """pass"""
    try:
        # Crear un objeto cursor para ejecutar las consultas
        cursor = conexion_bd.cursor()
        # Realizar consulta la tabla clientes
        cursor.execute(SELECT_SQL_SCRIPTS)
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
    except Error as error:
        logging.error(f"¡Fallo la consulta de registro(s) en la tabla!: {error}")


def actualizar_registro(conexion_bd, update_values, update_sql):
    """pass"""
    try:
        # Crear un objeto cursor para ejecutar las actualizaciones
        cursor = conexion_bd.cursor()
        # Actualizar nuevos registros en la tabla
        cursor.executemany(UPDATE_SQL_SCRIPTS, UPDATE_MULTIPLE_COLUMNS)
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
    """pass"""
    try:
        # Crear un objeto cursor para ejecutar las eliminaciones
        cursor = conexion_bd.cursor()
        # Eliminar un fila de registro simple
        cursor.execute(DELETE_SQL_SCRIPTS)
        # Guardar los cambios en la base de datos
        conexion_bd.commit()
        logging.info("¡Registro eliminado correctamente!\n")
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la eliminación de registro(s) en la tabla!: {error}")


if __name__ == "__main__":
    # Crear conexión a la base de datos "sistema" del servidor PostgreSQL
    conexion = crear_conexion(HOST, PORT, USER, PASSW, DB)
    # Crear la tabla "clientes" dentro de la base de datos
    crear_tablas(conexion, CREATE_TABLE_SQL)
    insertar_registro(conexion, INSERT_MULTIPLE_COLUMNS, INSERT_SQL_SCRIPTS)
    consultar_registro(conexion, SELECT_SQL_SCRIPTS)
    actualizar_registro(conexion, UPDATE_MULTIPLE_COLUMNS, UPDATE_SQL_SCRIPTS)
    eliminar_registro(conexion, DELETE_SQL_SCRIPTS)
