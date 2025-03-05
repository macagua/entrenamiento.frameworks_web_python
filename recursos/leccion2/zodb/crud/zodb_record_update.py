"""Modulo de actualizar registros en la ZODB"""

import logging
import os
import transaction
import ZODB, ZODB.FileStorage
from ZODB.POSException import StorageError
from pathlib import Path

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = ZODB.FileStorage.FileStorage(DB_PATH + "Data.fs")
DB = ZODB.DB(DB_FILE)


def actualizar_registro():
    """Función para la actualización de registro de la tabla"""
    conexion = None
    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = DB.open()
        # Crear la instancia de conexion y llamar al método open de db
        nodo = conexion.root()
        logging.info(f"✅ ¡Conectado a la base de datos {os.path.basename(DB_FILE.getName())}!\n")
        # Actualizar el nodo 'producto1'
        print(nodo['producto1'].descripcion)
        nodo['producto1'].descripcion='Vehiculo'
        print(nodo['producto1'].descripcion)
        # Actualizar el nodo 'producto2'
        print(nodo['producto2'].descripcion)
        nodo['producto2'].descripcion='Motocicleta'
        print(nodo['producto2'].descripcion)
        # Actualizar el nodo 'producto3'
        print(nodo['producto3'].descripcion)
        nodo['producto3'].descripcion='Bici'
        print(nodo['producto3'].descripcion)
        # Guardar los cambios en la base de datos
        transaction.commit()
    except StorageError as error:
        logging.error(f"❌ ¡Fallo la actualización de registro(s) en la ZODB!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión ZODB a la base de datos {os.path.basename(DB_FILE.getName())} fue cerrada!\n"
            )


if __name__ == "__main__":
    actualizar_registro()
