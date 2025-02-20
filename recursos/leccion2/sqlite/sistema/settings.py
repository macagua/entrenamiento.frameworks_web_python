import os
from dotenv import load_dotenv

load_dotenv()

# Nombre del archivo de base de datos.
DB_FILE = os.getenv("DB")

# Lista de filas a ingresar
INSERT_MULTIPLE_COLUMNS = [
    (1, "Leonardo", "Caballero", "5001", "+58-412-4734567"),
    (2, "Ana", "Poleo", "6302", "+58-426-5831297"),
    (3, "Manuel", "Matos", "4001", "+58-414-2360943"),
]

# Script INSERT SQL a usar al ingresar datos
INSERT_SQL_SCRIPTS = """INSERT INTO clientes VALUES (?, ?, ?, ?, ?);"""

# Script SELECT SQL a usar al consultar datos
SELECT_SQL_SCRIPTS = """SELECT * FROM clientes;"""

# Lista de filas a actualizar
UPDATE_MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

# Script UPDATE SQL a usar al actualizar datos
UPDATE_SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = ? WHERE id = ?;"""

# Script DELETE SQL a usar al eliminar datos
DELETE_SQL_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""
