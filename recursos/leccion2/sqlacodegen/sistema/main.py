"""Módulo principal del programa"""

import logging

from sqlalchemy import exc
from settings import DB_FILE, Base, engine, session
from models import Estados, Ciudades, Clientes, Productos, Pedidos

logging.basicConfig(level=logging.INFO)


def consulta_estados():
    """Consulta todos los estados"""

    print("✅ Lista de 10 Estados")
    # SELECT TOP 10 * FROM estados;
    todos_estados = session.query(Estados).limit(10).all()
    if len(todos_estados) == 0:
        logging.error("❌ ¡No hay ningún 'estado' con ese criterio en la base de datos!")
    else:
        row_count = 0
        for cada_estado in todos_estados:
            print(f"📜 {cada_estado}")
            row_count += 1
        logging.info(f"✅ ¡Consulta de los '{row_count}' estados!")


def consulta_ciudades():
    """Consulta todas las ciudades"""

    print("\n✅ Lista de 10 Ciudades")
    # SELECT TOP 10 * FROM ciudades;
    todos_ciudades = session.query(Ciudades).limit(10).all()
    if len(todos_ciudades) == 0:
        logging.error("❌ ¡No hay ningún 'ciudad' en la base de datos!")
    else:
        row_count = 0
        for cada_ciudad in todos_ciudades:
            print(f"📜 {cada_ciudad}")
            row_count += 1
        logging.info(f"✅ ¡Consulta de las '{row_count}' ciudades!")


def consulta_clientes():
    """Consulta todas las clientes"""

    print("\n✅ Lista de Clientes")
    # SELECT * FROM clientes;
    todos_clientes = session.query(Clientes).all()
    if len(todos_clientes) == 0:
        logging.error("❌ ¡No hay ningún 'cliente' en la base de datos!")
    else:
        row_count = 0
        for cada_cliente in todos_clientes:
            print(f"📜 {cada_cliente}")
            row_count += 1
        logging.info(f"✅ ¡Consulta de los '{row_count}' clientes!")


def consulta_productos():
    """Consulta todas las productos"""

    print("\n✅ Lista de Productos")
    # SELECT * FROM productos;
    todos_productos = session.query(Productos).all()
    if len(todos_productos) == 0:
        logging.error("❌ ¡No hay ningún 'producto' en la base de datos!")
    else:
        row_count = 0
        for cada_producto in todos_productos:
            print(f"📜 {cada_producto}")
            row_count += 1
        logging.info("✅ ¡Consulta de los '{row_count}' productos!")


def consulta_pedidos():
    """Consulta todas las pedidos"""

    print("\n✅ Lista de Pedidos")
    # SELECT * FROM pedidos;
    todos_pedidos = session.query(Pedidos).all()
    if len(todos_pedidos) == 0:
        logging.error("❌ ¡No hay ningún 'pedido' en la base de datos!\n")
    else:
        row_count = 0
        for cada_pedido in todos_pedidos:
            print(f"📜 {cada_pedido}")
            row_count += 1
        logging.info("✅ ¡Consulta de los '{row_count}' pedidos!")


if __name__ == "__main__":
    try:
        # Crea la base de datos y tablas
        Base.metadata.create_all(engine)
        # Consulta de productos
        consulta_estados()
        # Consulta de ciudades
        consulta_ciudades()
        # Consulta de clientes
        consulta_clientes()
        # Consulta de productos
        consulta_productos()
        # Consulta de pedidos
        consulta_pedidos()
    except exc.SQLAlchemyError as e:
        logging.error(
            f"❌ ERROR: ¡Se produjo un falla al establecer la conexión a la base de datos '{DB_FILE}': '{e}'!"
        )
    finally:
        if session:
            # Cerrar la conexión a la base de datos
            session.close()
            engine.dispose()
            logging.info(
                f"✅ ¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!"
            )
