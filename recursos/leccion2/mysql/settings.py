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
PORT = int(os.getenv("PORT"))

# Nombre de la base de datos a cual conectar.
DB = os.getenv("DB")
