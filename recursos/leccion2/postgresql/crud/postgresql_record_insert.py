"""Programa para la inserción de registro(s) de la tabla"""

import logging
import psycopg2
import os

logging.basicConfig(level=logging.INFO)

# Creando una lista de filas a ingresar
MULTIPLE_COLUMNS = [
    (1, "Leonardo", "Caballero", "5001", "+58-412-4734567"),
    (2, "Ana", "Poleo", "6302", "+58-426-5831297"),
    (3, "Pedro", "Lopez", "4001", "+58-414-2360943"),
]

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS clientes (
    id int unique not null,
    nombre varchar(25) not null,
    apellido varchar(25) not null,
    codigo_postal int not null,
    telefono varchar(11) not null,
    primary key(id)
);"""
INSERT_SQL = """INSERT INTO clientes VALUES (?, ?, ?, ?, ?);"""


def insertar_registro():
    """Función para la inserción de registro de la tabla"""

    try:
        credenciales = {
            host:"localhost",
            database:"mercantil",
            user:"postgres",
            password:"postgres"
        }
        # Establecer la conexión con la base de datos
        conexion = psycopg2.connect(**credenciales)

        # Crear un objeto cursor para ejecutar las consultas
        cursor = conexion.cursor()
        logging.info(f"¡Conectado a la base de datos {credenciales['database']}!\n")

        # Crear la tabla productos si no existe
        cursor.execute(CREATE_TABLE_SQL)

        # Insertar nuevos registros en la tabla
        cursor.executemany(INSERT_SQL, MULTIPLE_COLUMNS)
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )

        # Insertar un nuevo registro en la tabla
        cursor.execute(INSERT_SQL, (4, "Liliana", "Andradez", "4001", "+58-414-6782473"))
        logging.info(
            f"¡Fueron insertado(s) {cursor.rowcount} registro(s) correctamente en la tabla!\n"
        )
        cursor.close()

    except psycopg2.errors.Error as error:
        print("¡Fallo la inserción de registro(s) en la tabla!", error)
    finally:
        if conexion:
            conexion.close()
            logging.info(
                f"¡La conexión PostgreSQL a la base de datos {credenciales['database']} fue cerrada!\n"
            )


if __name__ == "__main__":
    insertar_registro()
