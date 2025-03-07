"""Modulo de buscar registros en la ZODB"""

import logging
import os
import ZODB, ZODB.FileStorage
from ZODB.POSException import StorageError
from pathlib import Path

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = ZODB.FileStorage.FileStorage(DB_PATH + "Data.fs")
DB = ZODB.DB(DB_FILE)


def consultar_registro():
    """Función para la consulta de registro(s) de la ZODB"""

    conexion = None
    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = DB.open()
        # Crear la instancia de conexion y llamar al método open de db
        nodo = conexion.root()
        logging.info(
            f"✅ ¡Conectado a la base de datos {os.path.basename(DB_FILE.getName())}!\n"
        )
        # Mostrar los nodos de la DB
        print("Todos los registros: ")
        # Mostrar los elementos de nodos
        print(nodo.items())
        # Mostrar los valores de nodos
        print("Todos los valores: ")
        print(nodo.values())
        # Mostrar el nodo 'producto1'
        if "producto1" in nodo.items():
            print("Producto: ", nodo["producto1"])
            print(f"\tId: {nodo['producto1'].id}")
            print(f"\tDescripción del producto: {nodo['producto1'].descripcion}")
        else:
            print("❌ No tiene registros el la ZODB")
    except StorageError as error:
        logging.error(f"❌ ¡Fallo la consulta de registro(s) en la ZODB!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión ZODB a la base de datos {os.path.basename(DB_FILE.getName())} fue cerrada!\n"
            )


if __name__ == "__main__":
    consultar_registro()
