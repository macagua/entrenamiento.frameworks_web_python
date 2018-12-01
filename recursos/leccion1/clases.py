# -*- coding: utf8 -*-
"""
   Ejemplo de Programación Orientado a Objetos usando la 
   Herencia simple de Clase en Python.
"""

import sys


class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa al Persona"""
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.cedula), self.nombre, 
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"


class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ', '.join(self.tareas)

def poblar_persona():
    """Función que crea objetos desde la clase Persona"""

    # Dos instancias de Objeto Persona
    persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
    persona2 = Persona("V-23569874", "Ana", "Poleo", "F")

    print(persona1.__doc__[25:34])
    print(len(persona1.__doc__[25:34]) * "=")

    print("\n" + str(persona1) + "\n")

    print("- Cedula de identidad: {0}.".format(persona1.cedula))
    print("- Nombre completo: {0} {1}.".format(persona1.nombre,
        persona1.apellido))
    print("- Genero: {0}.".format(persona1.getGenero(persona1.sexo)))
    print("- {0} {1} dijo: {2}".format(persona1.nombre, 
        persona1.apellido, persona1.hablar("Hola Ana :-*")))

    print(persona1.hablar("\nHola, Soy una Persona") + \
        ", me llamo '"+ persona1.nombre +" "+ persona1.apellido + \
        "', con cédula '"+  persona1.cedula +"'.")

    print("\nOtra " + persona1.__doc__[25:34])
    print((len(persona1.__doc__[25:34])+5) * "-")

    print("\n" + str(persona2) + "\n")

    print("- Cedula de identidad: {0}.".format(persona2.cedula))
    print("- Nombre completo: {0} {1}.".format(persona2.nombre,
        persona2.apellido))
    print("- Genero: {0}.".format(
        persona2.getGenero(persona2.__getattribute__('sexo'))))
    print("- {0} {1} dijo: {2}".format(persona2.nombre, 
        persona2.apellido, persona2.hablar("Hola Leonardo ^_^")))

    print(persona2.hablar("\nHola, Soy otra Persona") + \
        ", me llamo '"+ persona2.__getattribute__('nombre') +" "+ \
        persona2.__getattribute__('apellido') +"', con cédula '"+  \
        persona2.__getattribute__('cedula') +"'.")

def poblar_supervisor():
    """Función que crea objetos desde la clase Supervisor"""

    # Una instancia de Objeto Supervisor
    supervisor1 = Supervisor(
        "V-16987456", "Pedro", "Pérez", "No se", "El chivo")

    print("\n" + supervisor1.__doc__[26:37])
    print(len(supervisor1.__doc__[26:37]) * "=")

    print("\n" + str(supervisor1) + "\n")

    # Atributo(s) y Método(s) heredado de la clase Persona
    print("- Cedula de identidad: {0}.".format(supervisor1.cedula))
    print("- Nombre completo: {0} {1}.".format(
        supervisor1.nombre, supervisor1.apellido))
    print("- Genero: {0}.".format(
        supervisor1.getGenero(supervisor1.sexo)))
    print("- {0} {1} dijo: {2}".format(
        supervisor1.nombre, supervisor1.apellido, 
        supervisor1.hablar("A trabajar Leonardo!!!".upper())))

    # Atributo(s) y Método(s) heredado de la clase Supervisor
    print("- Rol: {0}.".format(supervisor1.rol))
    print("- N. Tareas: {0}.".format(supervisor1.consulta_tareas()))

    # Mostrar los atributos y métodos propios de la clase Supervisor 
    # y los heredados de la clase Persona

    print("""\nHola, Soy el {0} {1} {2}, mi cédula es '{3}', 
mi genero '{4}', con el rol '{5}' y mis tareas
asignadas '{6}'.""".format(
        supervisor1.__doc__[26:37].lower(),
        supervisor1.nombre, supervisor1.apellido, supervisor1.cedula, 
        supervisor1.getGenero(supervisor1.sexo), supervisor1.rol,
        supervisor1.consulta_tareas()))

if __name__ == '__main__':
    """Inicia el programa Python"""
    if len(sys.argv) == 2:
        if sys.argv[1] == "persona":
            poblar_persona()
        elif sys.argv[1] == "supervisor":
            poblar_supervisor()
    else:
        print("ERROR: Introdujo cero (0) o más de dos (2) argumentos")
        print("SOLUCIÓN: Introduce los argumentos correctamente")
        print("Ejemplo: python clases.py persona")
        print("Ejemplo: python clases.py supervisor")
elif __name__ == "clases":
    initialize()
else:
    print(
        "Este programa esta mal configurado, debes llamar a su modulo.")
