"""Programa para la inserción de registro(s) de la ZODB"""

import logging
import os
import persistent
import transaction
import ZODB, ZODB.FileStorage
from ZODB.POSException import StorageError
from pathlib import Path

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = ZODB.FileStorage.FileStorage(DB_PATH + "Data.fs")
DB = ZODB.DB(DB_FILE)


class Producto(persistent.Persistent):
    """Clase Producto"""

    def __init__(self, id, descripcion):
        """Método constructor de clase de Producto

        Args:
            id (int): ID del producto
            descripcion (str): Descripción del producto
        """
        self.id = id
        self.descripcion = descripcion

    def __str__(self):
        """Método de representación de informal del objeto,
        usado para crear la salida que se le mostrará al usuario"""
        return f"Id: {self.id}\nDescripción: {self.descripcion}"

    def __repr__(self):
        """Método de representación de formal del objeto,
        usado para depuración y desarrollo"""
        return f"{self.__class__.__name__}:({repr(self.id)}, {repr(self.descripcion)})"


def insertar_registro():
    """Función para la inserción de registro de la ZODB"""

    conexion = None
    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = DB.open()
        # Crear la instancia de conexion y llamar al método open de db
        nodo = conexion.root()
        logging.info(
            f"✅ ¡Conectado a la base de datos {os.path.basename(DB_FILE.getName())}!\n"
        )
        # Crear una instancia de la clase Producto
        producto1 = Producto(1, "Carro")
        nodo["producto1"] = producto1
        # Crear una instancia de la clase Producto
        producto2 = Producto(2, "Moto")
        nodo["producto2"] = producto2
        # Crear una instancia de la clase Producto
        producto3 = Producto(3, "Bicicleta")
        nodo["producto3"] = producto3
        # Crear una lista de instancia de objetos Producto
        nodo["productos"] = [producto1, producto2, producto3]
        # Confirmar la inserción del registro
        transaction.commit()
        logging.info(
            "✅ ¡Fueron insertado(s) los registro(s) correctamente en la ZODB!\n"
        )
    except StorageError as error:
        logging.error(f"❌ ¡Fallo la inserción de registro(s) en la ZODB!: {error}")
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión ZODB a la base de datos {os.path.basename(DB_FILE.getName())} fue cerrada!\n"
            )


if __name__ == "__main__":
    insertar_registro()
