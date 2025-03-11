import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = os.getenv("DB", "sistema.db")

engine = None

# Configurar conexiones entre SQLAlchemy y SQLite3 DB API
engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")

if "engine" in globals():
    # Crear sesión con el engine de base de datos
    Session = sessionmaker(bind=engine)
    session = Session()
    # Crear base declarativa
    Base = declarative_base()
