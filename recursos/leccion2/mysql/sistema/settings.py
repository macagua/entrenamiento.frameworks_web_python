import os
from dotenv import load_dotenv

load_dotenv()

# Usuario de conexión a la base de datos.
USER = os.getenv("USER")

# Contraseña del usuario de conexión a la base de datos.
PASSW = os.getenv("PASSW")

# IP o dirección DNS de conexión al servidor de la base de datos.
HOST = os.getenv("HOST")

# Puerto de conexión al servidor de la base de datos, por defecto es '3306'.
PORT = int(os.getenv("PORT", 3306))

# Nombre de la base de datos a cual conectar.
DB = os.getenv("DB")

# Script CREATE DATABASE SQL para crear la base de datos
CREATE_DATABASE_SQL = """CREATE DATABASE %s;"""

# Script CREATE TABLE SQL para crear tabla(s)
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    codigo_postal INT NOT NULL,
    telefono VARCHAR(20) NOT NULL
);"""

# Lista de filas a ingresar
INSERT_MULTIPLE_COLUMNS = [
    (1, "Leonardo", "Caballero", "5001", "+58-412-4734567"),
    (2, "Ana", "Poleo", "6302", "+58-426-5831297"),
    (3, "Manuel", "Matos", "4001", "+58-414-2360943"),
]

# Script INSERT SQL a usar al ingresar datos
INSERT_SQL_SCRIPTS = """INSERT INTO clientes VALUES (%s, %s, %s, %s, %s);"""

# Script SELECT SQL a usar al consultar datos
SELECT_SQL_SCRIPTS = """SELECT * FROM clientes;"""

# Lista de filas a actualizar
UPDATE_MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]

# Script UPDATE SQL a usar al actualizar datos
UPDATE_SQL_SCRIPTS = """UPDATE clientes SET codigo_postal = %s WHERE id = %s;"""

# Script DELETE SQL a usar al eliminar datos
DELETE_SQL_SCRIPTS = """DELETE FROM clientes WHERE id = 3;"""
