"""Módulo de configuraciones del programa"""

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = os.getenv("DB")
ENGINE = os.getenv("ENGINE_DB")
USER = os.getenv("USER")
PASSW = os.getenv("PASSW")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB = os.getenv("DB", "sistema.db")

engine = None

if ENGINE == "sqlite" and ENGINE is not None:
    if "DB_PATH" in globals() and "DB_FILE" in globals():
        # Conexión entre SQLAlchemy y SQLite3 DB API
        engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")
elif ENGINE == "mysql":
    if (
        "USER" in globals()
        and "PASSW" in globals()
        and "HOST" in globals()
        and "PORT" in globals()
        and "DB" in globals()
    ):
        # Conexión entre SQLAlchemy y MySQL DB API
        engine = create_engine(f"mysql+pymysql://{USER}:{PASSW}@{HOST}:{PORT}/{DB}")
elif ENGINE == "postgresql":
    if (
        "USER" in globals()
        and "PASSW" in globals()
        and "HOST" in globals()
        and "PORT" in globals()
        and "DB" in globals()
    ):
        # Conexión entre SQLAlchemy y PostgreSQL DB API
        engine = create_engine(f"postgresql://{USER}:{PASSW}@{HOST}:{PORT}/{DB}")
else:
    print(f"¡No se soporta ese tipo de conexión a base de datos {ENGINE}!")

if "engine" in globals():
    # Crear sesión con el engine de base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()
