from db import *

from sqlalchemy import Column, Integer, String, Float


class Productos(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    precio = Column(Float)

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __repr__(self):
        return f"Productos({self.nombre}, {self.categoria}, {self.precio})"

    def __str__(self):
        return self.nombre
