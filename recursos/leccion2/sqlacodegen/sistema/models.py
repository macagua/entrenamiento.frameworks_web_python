""" Modulo de modelos de SQLAlchemy """

from db import Base

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship


class Estados(Base):
    """Clase de Estados

    Args:
        Base (Base): clase base declarativa

    Returns:
        class 'models.Estados': Clase de Estados
    """

    __tablename__ = "estados"

    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(25), nullable=False)
    codigo = Column(String(2), nullable=False)

    ciudades = relationship("Ciudades", back_populates="estados")

    def __repr__(self):
        return f"Estados({self.nombre}, {self.codigo})"

    def __str__(self):
        return self.nombre


class Productos(Base):
    """Clase de Productos

    Args:
        Base (Base): clase base declarativa

    Returns:
        class 'models.Productos': Clase de Productos
    """

    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(11), nullable=False)
    descripcion = Column(String(25), nullable=False)
    categoria = Column(String(25), nullable=False)
    precio = Column(Integer, nullable=False)
    status = Column(Enum("y", "n"), nullable=False)

    pedidos = relationship("Pedidos", back_populates="producto")

    def __repr__(self):
        return f"Productos({self.nombre}, {self.categoria}, {self.precio})"

    def __str__(self):
        return self.nombre


class Ciudades(Base):
    """Clase de Ciudades

    Args:
        Base (Base): clase base declarativa

    Returns:
        class 'models.Ciudades': Clase de Ciudades
    """

    __tablename__ = "ciudades"

    id = Column(Integer, primary_key=True, unique=True)
    id_estado = Column(
        ForeignKey("estados.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    nombre = Column(String(25), nullable=False)
    capital = Column(Integer, nullable=False)

    estados = relationship("Estados", back_populates="ciudades")
    clientes = relationship("Clientes", back_populates="ciudades")

    def __repr__(self):
        return f"Ciudades({self.nombre}, {self.estados})"

    def __str__(self):
        return self.nombre


class Clientes(Base):
    """Clase de Clientes

    Args:
        Base (Base): clase base declarativa

    Returns:
        class 'models.Clientes': Clase de Clientes
    """

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(25), nullable=False)
    apellido = Column(String(25), nullable=False)
    codigo_postal = Column(
        ForeignKey("ciudades.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    telefono = Column(String(11), nullable=False)

    ciudades = relationship("Ciudades", back_populates="clientes")
    pedidos = relationship("Pedidos", back_populates="cliente")

    def __repr__(self):
        return f"Clientes({self.nombre} {self.apellido}, {self.telefono}, {self.ciudades}, {self.pedidos})"

    def __str__(self):
        return self.nombre + " " + self.apellido


class Pedidos(Base):
    """Clase de Pedidos de ventas

    Args:
        Base (Base): clase base declarativa

    Returns:
        class 'models.Pedidos': Clase de Pedidos de ventas
    """

    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, unique=True)
    cliente_id = Column(ForeignKey("clientes.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    producto_id = Column(ForeignKey("productos.id"), nullable=False)
    status = Column(Enum("y", "n"), nullable=False)

    cliente = relationship("Clientes", back_populates="pedidos")
    producto = relationship("Productos", back_populates="pedidos")

    def __repr__(self):
        return f"Pedidos({self.producto} {self.fecha}, {self.status})"

    def __str__(self):
        return self.producto + " " + self.fecha
