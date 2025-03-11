"""Programa que simula un inventario de productos"""

import os
import sys
from pathlib import Path
import pickle


class Producto:
    """Clase Producto"""

    def __init__(self, id, descripcion):
        """Método constructor de clase de Producto

        Args:
            id (int): ID del producto
            descripcion (str): Descripción del producto
        """
        self.id = id
        self.descripcion = descripcion

    def __str__(self):
        """Método de representación de informal del objeto,
        usado para crear la salida que se le mostrará al usuario"""
        return f"Id: {self.id}\nDescripción: {self.descripcion}"

    def __repr__(self):
        """Método de representación de formal del objeto,
        usado para depuración y desarrollo"""
        return f"{self.__class__.__name__}:({repr(self.id)}, {repr(self.descripcion)})"


class Inventario:
    """Clase Inventario"""

    def __init__(self):
        """Método constructor de clase de Inventario"""
        self._DB_DIR = (
            os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
        )
        self.productos = []
        self.archivo = self._DB_DIR + "inventario.pkl"
        self.leer_datos()

    def __str__(self):
        """Método de representación de informal del objeto,
        usado para crear la salida que se le mostrará al usuario"""
        return f"Ruta BD: {self.archivo}"

    def __repr__(self):
        """Método de representación de formal del objeto,
        usado para depuración y desarrollo"""
        return f"{self.__class__.__name__}:({repr(self.archivo)})"

    def leer_datos(self):
        """Leer el archivo de almacenamiento"""
        try:
            Path(self._DB_DIR).mkdir(parents=True, exist_ok=True)
            with open(self.archivo, "rb") as bd:
                self.productos = pickle.load(bd)
        except FileNotFoundError:
            print("El archivo no existe en la ubicación")

    def guardar_datos(self):
        """Guarda los datos"""
        try:
            if os.path.isfile(self.archivo):
                os.remove(self.archivo)
            with open(self.archivo, "wb") as bd:
                pickle.dump(self.productos, bd)
        except OSError:
            print("El archivo no existe en la ubicación")

    def existe(self, codigo):
        """Valida si existe el producto

        Args:
            codigo (int): ID del producto
        """
        if self.productos:
            for producto in self.productos:
                if producto.id == codigo:
                    return True
        return False

    def buscar(self, codigo):
        """Buscar el producto en el Inventario

        Args:
            codigo (int): ID del producto
        """
        for posicion, producto in enumerate(self.productos):
            if producto.id == codigo:
                return posicion, producto
        return 0, None

    def agregar_registro(self, codigo):
        """Agregar el producto

        Args:
            codigo (int): ID del producto
        """
        descripcion = input("Descripción: ")
        producto = Producto(codigo, descripcion)
        self.productos.append(producto)
        self.guardar_datos()

    def mostrar_registro(self, codigo):
        """Mostrar el producto

        Args:
            codigo (int): ID del producto
        """
        if self.existe(codigo):
            posicion, producto = self.buscar(codigo)
            print(producto)
        else:
            print("¡El producto no existe!")
        input("Presione ENTER para continuar")

    def actualizar_registro(self, codigo):
        """Actualizar el producto

        Args:
            codigo (int): ID del producto
        """
        if self.existe(codigo):
            posicion, producto = self.buscar(codigo)
            print(producto)
            print("Escribe nuevos datos: ")
            descripcion = input("Descripción: ")
            self.productos[posicion].descripcion = descripcion
            self.guardar_datos()
            print("¡Actualizado exitosamente!")
        else:
            print("¡El producto no existe!")
        input("Presione ENTER para continuar")

    def eliminar_registro(self, codigo):
        """Eliminar el producto

        Args:
            codigo (int): ID del producto
        """
        if self.existe(codigo):
            posicion, producto = self.buscar(codigo)
            print(producto)
            confirmar = input("¿Estas seguro? (S/N): ").upper()
            if confirmar in ("s", "S", "si", "Si", "SI"):
                del self.productos[posicion]
                self.guardar_datos()
                print("¡Eliminado exitosamente!")
        else:
            print("¡El producto no existe!")
        input("Presione ENTER para continuar")

    def menu_principal(self):
        """Menu principal del programa"""
        try:
            # Instancia de la clase Inventario
            inventario = Inventario()
            while True:
                print("\n==============")
                print("MENÚ PRINCIPAL")
                print("==============\n")
                opciones_menu = "1) Crear\n"
                opciones_menu += "2) Consultar\n"
                opciones_menu += "3) Actualizar\n"
                opciones_menu += "4) Eliminar\n"
                opciones_menu += "5) Salir\n"
                opciones_menu += "\nElija uno: "
                # Solicitar al usuario que elija una opción
                opcion = int(input(opciones_menu))
                # Opciones del menú
                if opcion == 1:
                    codigo = int(input("Id de Producto: "))
                    if not inventario.existe(codigo):
                        inventario.agregar_registro(codigo)
                        print("¡Registro exitoso!")
                    else:
                        print("¡Producto ya existe!")
                    input("Presione ENTER para continuar")
                elif opcion == 2:
                    codigo = int(input("Id de Producto: "))
                    inventario.mostrar_registro(codigo)
                elif opcion == 3:
                    codigo = int(input("Id de Producto: "))
                    inventario.actualizar_registro(codigo)
                elif opcion == 4:
                    codigo = int(input("Id de Producto: "))
                    inventario.eliminar_registro(codigo)
                elif opcion == 5:
                    break
        except KeyboardInterrupt:
            print(" <Ctrl-C> introducido, saliendo del programa...\n")
            sys.exit()


if __name__ == "__main__":
    # Instancia de la clase Inventario
    app = Inventario()
    # Llamar al método menu_principal
    app.menu_principal()
