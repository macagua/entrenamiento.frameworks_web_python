from db import *
from models import *


def consulta_estados():
    print("¡Consulta todos los estados!")
    # SELECT * FROM estados;
    estados = session.query(Estados).all()
    for estado in estados:
        print(estado)
    print("")


def consulta_ciudades():
    print("¡Consulta todas las ciudades!")
    # SELECT * FROM ciudades;
    ciudades = session.query(Ciudades).all()
    for ciudad in ciudades:
        print(ciudad)
    print("")


if __name__ == "__main__":
    consulta_estados()
    consulta_ciudades()
