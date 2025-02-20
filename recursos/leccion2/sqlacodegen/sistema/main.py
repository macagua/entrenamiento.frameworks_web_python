"""Módulo principal del programa"""

from db import session
from models import Estados, Ciudades


def consulta_estados():
    """Consulta todos los estados"""

    print("¡Consulta todos los estados!")
    # SELECT * FROM estados;
    estados = session.query(Estados).all()
    for estado in estados:
        print(estado)
    print("")


def consulta_ciudades():
    """Consulta todas las ciudades"""

    print("¡Consulta todas las ciudades!")
    # SELECT * FROM ciudades;
    ciudades = session.query(Ciudades).all()
    for ciudad in ciudades:
        print(ciudad)
    print("")


if __name__ == "__main__":
    consulta_estados()
    consulta_ciudades()
