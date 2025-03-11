"""Módulo de modelos de SQLAlchemy"""

from settings import Base

from sqlalchemy import Column, Float, Integer, String


class Productos(Base):
    """Clase de Productos

    Args:
        Base (Base): clase base declarativa

    Returns:
        class 'models.Productos': Clase de Productos
    """

    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __repr__(self):
        return f"<Productos(nombre={self.nombre}, categoria={self.categoria}, precio={self.precio})>"

    def __str__(self):
        return f"Producto: {self.nombre} ({self.categoria}) - ${self.precio:.2f}"
