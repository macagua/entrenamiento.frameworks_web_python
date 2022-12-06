import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert, select, update, delete

load_dotenv()

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = os.getenv("DB")

# Configurar conexiones entre SQLAlchemy y SQLite3 DB API
engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")

# Crear sesión con el engine de base de datos
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
