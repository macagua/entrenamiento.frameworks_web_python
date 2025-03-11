"""Programa para operaciones CRUD de registros de productos de un Inventario con ZODB"""

import logging
import transaction
from settings import (
    DB,
    DB_FILE,
    DB_FILE_NAME,
    INSERT_MULTIPLE_COLUMNS,
    UPDATE_MULTIPLE_COLUMNS,
    DELETE_MULTIPLE_COLUMNS,
)
from classes.producto import Producto
from ZODB.POSException import StorageError

logging.basicConfig(level=logging.INFO)


def insertar_registro(conn, nodo_raiz, registros):
    """Función para la inserción dek nodo de la base de datos

    Args:
        conn (Connection): Representación conexión a la base de datos ZODB
        nodo_raiz (list): Nodo raiz de la base de datos
        registros (list): Lista de filas a ingresar
    """
    try:
        if "productos" not in nodo_raiz:
            nodo_raiz["productos"] = []
        for registro in registros:
            producto = Producto(registro[0], registro[1])
            nodo_raiz["productos"].append(producto)
        # Guardar los cambios en la base de datos
        transaction.commit()
        # print(nodo_raiz["productos"])
        logging.info(
            f"✅ ¡Fueron insertado(s) {len(registros)} registro(s) correctamente en la ZODB!\n"
        )
    except StorageError as error:
        logging.error(f"❌ ¡Fallo la inserción de registro(s) en la ZODB!: {error}")


def consultar_registro(conn, nodo_raiz):
    """Muestra todos los productos de la base de datos

    Args:
        conn (Connection): Representación conexión a la base de datos ZODB
        nodo_raiz (list): Nodo raiz de la base de datos
    """
    # Mostrar los nodos de la DB
    print("📜 Lista de registros:\n")
    # Mostrar los elementos de nodos
    cantidad_nodo = 0
    # Si es el nodo 'productos' existe
    if "productos" in nodo_raiz and nodo_raiz["productos"]:
        for i, producto in enumerate(nodo_raiz["productos"]):
            cantidad_nodo = i + 1
            print(f"  Producto {i + 1}:")
            print(f"    ID: {producto.id}")
            print(f"    Descripción: {producto.descripcion}")
    else:
        print("❌ No hay productos registrados en el Inventario")
    print(f"\n📜 Total de producto(s) en Inventario: {cantidad_nodo}.\n")
    logging.info(
        f"✅ ¡Fueron consultados {cantidad_nodo} registro(s) correctamente en la ZODB!\n"
    )


def actualizar_registro(conn, nodo_raiz, registros):
    """Función para la actualización dek nodo de la base de datos

    Args:
        conn (Connection): Representación conexión a la base de datos ZODB
        nodo_raiz (list): Nodo raiz de la base de datos
        registros (list): Lista de filas a actualizar
    """
    try:
        actualizados = 0
        for i, registro in enumerate(registros):
            if (
                i < len(nodo_raiz["productos"])
                and registro[0] == nodo_raiz["productos"][i].id
            ):
                descripcion_anterior = nodo_raiz["productos"][i].descripcion
                nodo_raiz["productos"][i].descripcion = registro[1]
                actualizados += 1
                print(
                    f"📜 El producto '{descripcion_anterior}' fue actualizado con '{registro[1]}'.\n"
                )
        # Guardar los cambios en la base de datos
        transaction.commit()
        # print(f"{nodo_raiz['productos']}\n")
        logging.info(
            f"✅ ¡Fueron actualizados {actualizados} registro(s) correctamente en la ZODB!\n"
        )
    except StorageError as error:
        logging.error(f"❌ ¡Fallo la actualización de registro(s) en la ZODB!: {error}")


def eliminar_registro(conn, nodo_raiz, registros):
    """Función para la eliminación dek nodo de la base de datos

    Args:
        conn (Connection): Representación conexión a la base de datos ZODB
        nodo_raiz (list): Nodo raiz de la base de datos
        registros (list): Lista de filas a eliminar
    """
    try:
        eliminados = []
        # Ordenar en reversa para eliminar desde el final
        for id_eliminar in sorted(registros, reverse=True):
            if "productos" in nodo_raiz and 0 <= id_eliminar - 1 < len(
                nodo_raiz["productos"]
            ):
                producto_eliminado = nodo_raiz["productos"][id_eliminar - 1].descripcion
                eliminados.append(nodo_raiz["productos"].pop(id_eliminar - 1))
                print(
                    f"📜 El producto '{producto_eliminado}' fue eliminado correctamente.\n"
                )

        # Guardar los cambios en la base de datos
        transaction.commit()
        logging.info(
            f"✅ ¡Fueron eliminados {len(eliminados)} registro(s) correctamente en la ZODB!\n"
        )
    except StorageError as error:
        logging.error(f"❌ ¡Fallo la eliminación de registro(s) en la ZODB!: {error}")


if __name__ == "__main__":
    conexion = None
    try:
        conexion = DB.open()
        nodo_principal = conexion.root()
        logging.info(f"✅ ¡Conectado a la base de datos '{DB_FILE_NAME}!'\n")
        # import pdb; pdb.set_trace()
        insertar_registro(conexion, nodo_principal, INSERT_MULTIPLE_COLUMNS)
        consultar_registro(conexion, nodo_principal)
        actualizar_registro(conexion, nodo_principal, UPDATE_MULTIPLE_COLUMNS)
        eliminar_registro(conexion, nodo_principal, DELETE_MULTIPLE_COLUMNS)
    except StorageError as e:
        logging.error(
            f"❌ ERROR: ¡Se produjo un falla al establecer la conexión a la base de datos '{DB_FILE_NAME}': '{e}'!"
        )
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                f"✅ ¡La conexión ZODB a la base de datos '{DB_FILE_NAME}' fue cerrada!"
            )
