import ZODB, ZODB.FileStorage
import os
import persistent
import transaction

# Configurar la base de datos y abrir la conexión
_DB_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"

# Archivo de la base de datos ZODB
DB = "Data.fs"

storage = ZODB.FileStorage.FileStorage(_DB_DIR + DB)
zodb = ZODB.DB(storage)
conexion = zodb.open()
print(f"✅ ¡La conexión ZODB a la base de datos '{DB}' fue establecida!\n")
root = conexion.root()


class Cliente(persistent.Persistent):
    def __init__(self, id, nombre, apellido, codigo_postal, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.codigo_postal = codigo_postal
        self.telefono = telefono

    def actualizar(self, nombre=None, apellido=None, codigo_postal=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if codigo_postal:
            self.codigo_postal = codigo_postal
        if telefono:
            self.telefono = telefono


def crear_cliente(id, nombre, apellido, codigo_postal, telefono):
    if id in root:
        print("❌ Error: El cliente ya existe.")
        return
    root[id] = Cliente(id, nombre, apellido, codigo_postal, telefono)
    transaction.commit()
    print(f"✅ Cliente '{nombre} {apellido}' creado con éxito.")


def leer_clientes():
    print("\n📜 Lista de Clientes:")
    for id, cliente in root.items():
        print(
            f"ID: {id}, Nombre: {cliente.nombre}, Apellido: {cliente.apellido}, Código postal: {cliente.codigo_postal}, Teléfono: {cliente.telefono}"
        )


def actualizar_cliente(
    id, nombre=None, apellido=None, codigo_postal=None, telefono=None
):
    if id not in root:
        print("❌ Error: Cliente no encontrado.")
        return
    root[id].actualizar(nombre, apellido, codigo_postal, telefono)
    transaction.commit()
    print(f"✅ Cliente con ID: '{id}' actualizado con éxito.")


def eliminar_cliente(id):
    if id not in root:
        print("❌ Error: Cliente no encontrado.")
        return
    del root[id]
    transaction.commit()
    print(f"✅ Cliente con ID: '{id}' eliminado con éxito.")


# Crear clientes
crear_cliente(1, "Leonardo", "Caballero", "5001", "+58-412-4734567")
crear_cliente(2, "Ana", "Poleo", "6302", "+58-426-5831297")
crear_cliente(3, "Manuel", "Matos", "4001", "+58-414-2360943")
crear_cliente(4, "Liliana", "Andradez", "3105", "+58-414-6782473")

# Leer clientes
leer_clientes()

# Actualizar clientes
actualizar_cliente(1, telefono="+58-416-5831297")
leer_clientes()

# Eliminar clientes
eliminar_cliente(4)
leer_clientes()

# Cerrar la conexión a la base de datos
print(f"\n✅ ¡La conexión ZODB a la base de datos '{DB}' fue cerrada!")
conexion.close()
# Cerrar la base de datos
print(f"✅ ¡La base de datos ZODB '{DB}' fue cerrada!")
zodb.close()
