from settings import *
from mysql.connector import connect, Error, errorcode


def crear_conexion(servidor, puerto, usuario, contrasena, bd):
    """_summary_

    Args:
        servidor (str): IP o dirección DNS de conexión al servidor de la base de datos.
        puerto (str): Puerto de conexión al servidor de la base de datos, por defecto es '3306'.
        usuario (str): Usuario de conexión a la base de datos.
        contrasena (str): Contraseña del usuario de conexión a la base de datos.
        bd (str): Nombre de la base de datos a cual conectar.

    Returns:
        _type_: _description_
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
        print("¡Conexión a la base de datos MySQL fue exitosa!")
    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERROR: ¡Algo está mal con su nombre de usuario o contraseña!")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERROR: ¡La base de datos no existe!")
        else:
            print(f"ERROR: ¡Se produjo lo siguiente: '{e}'")

    return conexion_bd


# Crear conexión a base de datos MySQL
conexion = crear_conexion(
    HOST_CONEXION, PUERTO_CONEXION, USUARIO_BD, CONTRASENA_BD, NOMBRE_BD
)
# print(conexion, type(conexion))
