"""Ejemplo de Programación Orientado a Objetos usando
la Herencia simple de Clase en Python."""

import sys


class Persona:
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa al Persona"""
        doc = self.__doc__[25:34] if self.__doc__ else "Persona"
        return "{}: {}, {} {}, {}.".format(
            doc,
            str(self.cedula),
            self.nombre,
            self.apellido,
            self.getGenero(self.sexo),
        )

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ("Masculino", "Femenino")
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
        self.tareas = ["10", "11", "12", "13"]

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        doc = self.__doc__[26:37] if self.__doc__ else "Supervisor"
        return "{}: {} {}, rol: '{}', sus tareas: {}.".format(
            doc,
            self.nombre,
            self.apellido,
            self.rol,
            self.consulta_tareas(),
        )

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ", ".join(self.tareas)


def poblar_persona():
    """Función que crea objetos desde la clase Persona"""

    # Dos instancias de Objeto Persona
    persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
    persona2 = Persona("V-23569874", "Ana", "Poleo", "F")

    persona1_doc = persona1.__doc__[25:34] if persona1.__doc__ else "Persona"
    print(persona1_doc)
    print(len(persona1_doc) * "=")

    print("\n" + str(persona1) + "\n")

    print(f"- Cedula de identidad: {persona1.cedula}.")
    print(f"- Nombre completo: {persona1.nombre} {persona1.apellido}.")
    print(f"- Genero: {persona1.getGenero(persona1.sexo)}.")
    print(
        "- {} {} dijo: {}".format(
            persona1.nombre, persona1.apellido, persona1.hablar("Hola Ana :-*")
        )
    )

    print(
        persona1.hablar("\nHola, Soy una Persona")
        + ", me llamo '"
        + persona1.nombre
        + " "
        + persona1.apellido
        + "', con cédula '"
        + persona1.cedula
        + "'."
    )

    print("\nOtra " + persona1_doc)
    print((len(persona1_doc) + 5) * "-")

    print("\n" + str(persona2) + "\n")

    # Atributo(s) y Método(s) heredado de la clase Persona
    print(f"- Cedula de identidad: {persona2.cedula}.")
    print(f"- Nombre completo: {persona2.nombre} {persona2.apellido}.")
    print("- Genero: {}.".format(persona2.getGenero(persona2.__getattribute__("sexo"))))
    print(
        "- {} {} dijo: {}".format(
            persona2.nombre, persona2.apellido, persona2.hablar("Hola Leonardo ^_^")
        )
    )
    print(
        persona2.hablar("\nHola, Soy otra Persona")
        + ", me llamo '"
        + persona2.__getattribute__("nombre")
        + " "
        + persona2.__getattribute__("apellido")
        + "', con cédula '"
        + persona2.__getattribute__("cedula")
        + "'."
    )


def poblar_supervisor():
    """Función que crea objetos desde la clase Supervisor"""

    # Una instancia de Objeto Supervisor
    supervisor1 = Supervisor("V-16987456", "Manuel", "Matos", "No se", "El chivo")

    supervisor1_doc = (
        supervisor1.__doc__[26:37] if supervisor1.__doc__ else "Supervisor"
    )
    print("\n" + supervisor1_doc)
    print(len(supervisor1_doc) * "=")

    print("\n" + str(supervisor1) + "\n")

    # Atributo(s) y Método(s) heredado de la clase Persona
    print(f"- Cedula de identidad: {supervisor1.cedula}.")
    print(f"- Nombre completo: {supervisor1.nombre} {supervisor1.apellido}.")
    print(f"- Genero: {supervisor1.getGenero(supervisor1.sexo)}.")
    print(
        "- {} {} dijo: {}".format(
            supervisor1.nombre,
            supervisor1.apellido,
            supervisor1.hablar("A trabajar Leonardo!!!".upper()),
        )
    )

    # Atributo(s) y Método(s) heredado de la clase Supervisor
    print(f"- Rol: {supervisor1.rol}.")
    print(f"- N. Tareas: {supervisor1.consulta_tareas()}.")

    # Mostrar atributo(s) y método(s) propios de la clase Supervisor
    # y los heredados de la clase Persona
    print(
        """\nHola, Soy el {} {} {}, mi cédula es '{}',
mi genero '{}', con el rol '{}' y mis tareas
asignadas '{}'.""".format(
            supervisor1_doc.lower(),
            supervisor1.nombre,
            supervisor1.apellido,
            supervisor1.cedula,
            supervisor1.getGenero(supervisor1.sexo),
            supervisor1.rol,
            supervisor1.consulta_tareas(),
        )
    )


if __name__ == "__main__":
    """Inicia el programa Python"""
    if len(sys.argv) == 2:
        if sys.argv[1] == "persona":
            poblar_persona()
        elif sys.argv[1] == "supervisor":
            poblar_supervisor()
    else:
        print("ERROR: Ingreso cero (0) o más de dos (2) argumentos")
        print("SOLUCIÓN: Introduce los argumentos correctamente")
        print("Ejemplo: python clases.py persona")
        print("Ejemplo: python clases.py supervisor")
else:
    print("El programa esta mal configurado, debe llamar a su módulo")
