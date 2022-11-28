import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert, select, update, delete


DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_ARCHIVO = "productos.sqlite3"

# Configurar conexiones entre SQLAlchemy y SQLite3 DB API
engine = create_engine(f"sqlite:///{DIR_ARCHIVO}{DB_ARCHIVO}")

# Crear sesión con el engine de base de datos
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
