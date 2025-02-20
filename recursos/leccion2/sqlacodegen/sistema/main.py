"""Módulo principal del programa"""

from db import session
from models import Estados, Ciudades, Clientes, Productos, Pedidos


def consulta_estados():
    """Consulta todos los estados"""

    print("\n📜 Lista de Estados:\n")
    # SELECT * FROM estados;
    todos_estados = session.query(Estados).all()
    for cada_estado in todos_estados:
        print(f"{cada_estado}")


def consulta_ciudades():
    """Consulta todas las ciudades"""

    print("\n📜 Lista de Ciudades:\n")
    # SELECT * FROM ciudades;
    todos_ciudades = session.query(Ciudades).all()
    for cada_ciudad in todos_ciudades:
        print(f"{cada_ciudad}")


def consulta_clientes():
    """Consulta todas las clientes"""

    print("\n📜 Lista de Clientes:\n")
    # SELECT * FROM clientes;
    todos_clientes = session.query(Clientes).all()
    for cada_cliente in todos_clientes:
        print(f"{cada_cliente}")


def consulta_pedidos():
    """Consulta todas las pedidos"""

    print("\n📜 Lista de Pedidos:\n")
    # SELECT * FROM pedidos;
    todos_pedidos = session.query(Pedidos).all()
    for cada_pedido in todos_pedidos:
        print(f"{cada_pedido}")


def consulta_productos():
    """Consulta todas las productos"""

    print("\n📜 Lista de Productos:\n")
    # SELECT * FROM productos;
    todos_productos = session.query(Productos).all()
    for cada_producto in todos_productos:
        print(f"{cada_producto}")


if __name__ == "__main__":
    # Consulta de productos
    consulta_estados()
    # Consulta de ciudades
    consulta_ciudades()
    # Consulta de clientes
    consulta_clientes()
    # Consulta de pedidos
    consulta_pedidos()
    # Consulta de pedidos
    consulta_productos()
