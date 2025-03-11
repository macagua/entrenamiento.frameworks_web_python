"""Módulo de clase Producto"""

import persistent


class Producto(persistent.Persistent):
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
        return f"({self.__class__.__name__}) Id: {self.id}, Descripción: {self.descripcion}."

    def __repr__(self):
        """Método de representación de formal del objeto,
        usado para depuración y desarrollo"""
        return f"<{self.__class__.__name__}:(id={repr(self.id)}, descripcion={repr(self.descripcion)})>"
