"""Módulo de clase Cliente"""

import persistent


class Cliente(persistent.Persistent):
    """Clase Cliente"""

    def __init__(self, id, nombre, apellido, codigo_postal, telefono):
        """Método constructor de clase de Cliente

        Args:
            id (int): ID del Cliente
            nombre (str): Nombre del Cliente
            apellido (str): Apellido del Cliente
            codigo_postal (str): Código postal del Cliente
            telefono (str): Teléfono  del Cliente
        """
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.codigo_postal = codigo_postal
        self.telefono = telefono

    def __str__(self):
        """Método de representación de informal del objeto,
        usado para crear la salida que se le mostrará al usuario"""
        return f"({self.__class__.__name__}) Id: {self.id}, Nombre completo: {self.nombre} {self.apellido}."

    def __repr__(self):
        """Método de representación de formal del objeto,
        usado para depuración y desarrollo"""
        return f"<{self.__class__.__name__}:(id={repr(self.id)}, Nombre completo={repr(self.nombre)} {repr(self.apellido)})>"

    def actualizar(self, nombre=None, apellido=None, codigo_postal=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if codigo_postal:
            self.codigo_postal = codigo_postal
        if telefono:
            self.telefono = telefono
