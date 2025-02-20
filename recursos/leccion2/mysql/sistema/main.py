"""
Programa para realizar operaciones a base de datos MySQL
"""

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
from pymysql.constants.ER import DBACCESS_DENIED_ERROR, BAD_DB_ERROR
from pymysql import (
    Error,
    OperationalError,
    ProgrammingError,
    IntegrityError,
    connect,
    err,
)

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
    credenciales = {
        "host": servidor,
        "port": puerto,
        "user": usuario,
        "password": contrasena,
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
    except Error as err:
        if err.args[0] == DBACCESS_DENIED_ERROR:
            logging.error(
                "\x1b[1;31mERROR: ¡Algo está mal con su nombre de usuario o contraseña!"
            )
        elif err.args[0] == BAD_DB_ERROR:
            logging.error("\x1b[1;31mERROR: ¡La base de datos no existe!")
        else:
            logging.error(f"\x1b[1;31mERROR: ¡Se produjo lo siguiente: '{err}'")
    return conexion_bd


def crear_base_datos(conexion_bd, create_database_sql, bd):
    """Creación la base de datos

    Args:
        conexion_bd (Connection): Representación de un socket con un servidor MySQL
        create_database_sql (str): Script CREATE DATABASE SQL para crear la base de datos
        bd (str): Nombre de la base de datos a crear.
    """
    conexion_bd.autocommit = True
    # Crear un objeto cursor para ejecutar script SQL
    cursor = conexion_bd.cursor()
    try:
        # Insertar una base de datos en el servidor MySQL
        cursor.execute(create_database_sql, bd)
        logging.info(f"¡Creación exitosa de la base de datos '{bd}'!\n")
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
    """Inserción de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos MySQL
        insert_values (list): Lista de filas a ingresar
        insert_sql (str): Script INSERT SQL a usar al ingresar datos
    """
    try:
        # Crear un objeto cursor para ejecutar script SQL
        cursor = conexion_bd.cursor()
        # Confirmar la creación de la tabla
        conexion_bd.commit()
        # Insertar nuevos registros en la tabla
        cursor.executemany(insert_sql, insert_values)
        # Confirmar la inserción de los registros
        conexion_bd.commit()
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Insertar un nuevo registro en la tabla
        cursor.execute(
            insert_sql, (4, "Liliana", "Andradez", "4001", "+58-414-6782473")
        )
        # Confirmar la inserción del registro
        conexion_bd.commit()
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        # Cerrar el cursor
        cursor.close()
    except IntegrityError as error:
        logging.error(f"¡Registro duplicado por clave primaria!: {error}")
    except Error as error:
        logging.error(f"¡Fallo la inserción de registro(s) en la tabla!: {error}")


def consultar_registro(conexion_bd, select_sql):
    """Consulta de registro(s) de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos MySQL
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
            print(f"\tNombre: {fila[1]} {fila[2]}")
            print(f"\tCódigo postal: {fila[3]}")
            print(f"\tTeléfono: {fila[4]}\n")
        # Cerrar el cursor
        cursor.close()
    except Error as error:
        logging.error(f"¡Fallo la consulta de registro(s) en la tabla!: {error}")


def actualizar_registro(conexion_bd, update_values, update_sql):
    """Actualización de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos MySQL
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
    """Eliminación de registro de la tabla

    Args:
        conexion_bd (Connection): Representación conexión a la base de datos MySQL
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
    # Crear conexión con un servidor MySQL
    conexion = crear_conexion(HOST, PORT, USER, PASSW, DB)
    # Crear la base de datos
    # crear_base_datos(conexion, CREATE_DATABASE_SQL, DB)
    # Crear la tabla dentro de la base de datos
    crear_tablas(conexion, CREATE_TABLE_SQL)
    insertar_registro(conexion, INSERT_MULTIPLE_COLUMNS, INSERT_SQL_SCRIPTS)
    consultar_registro(conexion, SELECT_SQL_SCRIPTS)
    actualizar_registro(conexion, UPDATE_MULTIPLE_COLUMNS, UPDATE_SQL_SCRIPTS)
    eliminar_registro(conexion, DELETE_SQL_SCRIPTS)
