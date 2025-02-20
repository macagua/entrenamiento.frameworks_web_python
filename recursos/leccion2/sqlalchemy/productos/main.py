from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import exc
from db import Base, engine, session
from models import Productos


def ingresar_data():
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (1,'Arroz','Granos','1.25');
    arroz = Productos(nombre="Arroz", categoria="Granos", precio=1.25)
    session.add(arroz)

    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (2, "Agua", "Líquidos", 0.3);
    agua = Productos(nombre="Agua", categoria="Líquidos", precio=0.3)
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (3, "Mantequilla", "Lácteos", 3.56);
    mantequilla = Productos("Mantequilla", "Lácteos", 3.56)
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (4, "Queso", "Lácteos", 8.56);
    queso = Productos("Queso", "Lácteos", 8.56)
    session.add_all([agua, mantequilla, queso])

    session.commit()
    print("¡Inserción exitosa de los 4 productos!\n")


def consultar_data():
    print("¡Consulta todos los productos!")
    # SELECT * FROM productos;
    todos_productos = session.query(Productos).all()
    for cada_producto in todos_productos:
        print(cada_producto)

    print("\n¡Consulta todos los productos con más atributos!")
    # SELECT * FROM productos;
    consulta = select(Productos)
    for producto in session.scalars(consulta):
        print(f"{producto.nombre} {str(producto.precio)}")


def consultar_id_data(producto_id):
    print("\n¡Consulta de producto en base a su clave primaria!")
    # SELECT * FROM productos WHERE id == 1
    producto = session.get(Productos, producto_id)
    print(producto)


def consultar_categoria_precio():
    print("\n¡Consulta de productos lácteos!")
    # SELECT * FROM productos WHERE categoria == "Lácteos" AND precio >= 3.0
    lacteos = (
        session.query(Productos)
        .filter(Productos.categoria == "Lácteos")
        .filter(Productos.precio >= 3.0)
    )
    for lacteo in lacteos:
        print(lacteo)


def consultar_nombre_tupla():
    print("\n¡Otra consulta de productos lácteos!")
    # SELECT id, nombre, categoria FROM productos WHERE categoria == "Lácteos"
    lacteos = session.query(Productos).filter(Productos.categoria == "Lácteos")
    for lacteo in lacteos:
        print(f"{lacteo.id}, {lacteo.nombre}, {lacteo.categoria}")


def consultar_nombre_primero():
    print("\n¡Consulta del primer producto!")
    # SELECT * FROM productos WHERE categoria == "Lácteos" LIMIT 1
    producto = session.query(Productos).filter(Productos.categoria == "Lácteos").first()
    if producto:
        print(producto)
    else:
        print("¡No hay ningún Producto con ese criterio en la base de datos!")


def consultar_nombre_unico():
    print("\n¡Consulta del único producto!")
    try:
        # SELECT * FROM productos WHERE categoria == "Lácteos"
        producto = (
            session.query(Productos).filter(Productos.categoria == "Líquidos").one()
        )
        print(producto)
    except exc.NoResultFound as err:
        print("¡No hay ningún Producto con ese criterio en la base de datos!")
    finally:
        engine.dispose()
        session.close()


def consultar_nombres_data(nombres):
    print("\n¡Consulta los productos cuyos nombres coincidan con los suministrados!")
    # SELECT * FROM productos WHERE nombre IN ("Agua", "Arroz")
    consulta = select(Productos).where(Productos.nombre.in_(nombres))
    for producto in session.scalars(consulta):
        print(producto)


def actualizar_data(producto_id):
    print("\n¡Actualiza el producto suministrado!")
    # SELECT * FROM productos WHERE id == 1 LIMIT 1
    # UPDATE productos SET precio = 11.50 WHERE id = 1;
    producto = session.query(Productos).filter(Productos.id == producto_id).first()
    print("Precio anterior:", producto, producto.precio)
    producto.precio = 11.50
    print("Precio nuevo:", producto, producto.precio)

    session.add(producto)
    session.commit()
    print("¡Actualización exitosa de precio del producto!\n")


def actualizar_otra_data(producto_id, precio_nuevo):
    print("¡Actualiza el producto suministrado!")
    # UPDATE productos SET precio = 3.33 WHERE id = 2;
    session.query(Productos).filter(Productos.id == producto_id).update(
        {Productos.precio: precio_nuevo}
    )
    session.commit()
    print("¡Actualización exitosa de precio del producto!\n")


def eliminar_data(producto_id):
    print("¡Elimina los productos suministrados!")
    # DELETE FROM productos WHERE id = 1;
    session.query(Productos).filter(Productos.id == producto_id).delete()
    session.commit()
    print("¡Eliminación exitosa del producto!\n")


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("¡Creación exitosa de la tabla productos!\n")
    ingresar_data()
    consultar_data()
    consultar_id_data(1)
    consultar_categoria_precio()
    consultar_nombre_tupla()
    consultar_nombre_primero()
    consultar_nombre_unico()
    consultar_nombres_data(["Agua", "Arroz"])
    actualizar_data(1)
    actualizar_otra_data(2, 3.33)
    eliminar_data(1)
