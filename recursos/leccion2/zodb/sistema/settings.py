"""Módulo de configuraciones"""

import os
from pathlib import Path
import ZODB, ZODB.FileStorage

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = ZODB.FileStorage.FileStorage(DB_PATH + "inventario.fs")
DB_FILE_NAME = os.path.basename(DB_FILE.getName())
DB = ZODB.DB(DB_FILE)

# Lista de nodos a ingresar
INSERT_MULTIPLE_COLUMNS = [
    (1, "Carro"),
    (2, "Bici"),
    (3, "Motocicleta"),
]

# Lista de nodos a actualizar
UPDATE_MULTIPLE_COLUMNS = [
    (1, "Vehiculo"),
    (2, "Bicicleta"),
]

# Lista de nodos a eliminar
DELETE_MULTIPLE_COLUMNS = [1, 2]
