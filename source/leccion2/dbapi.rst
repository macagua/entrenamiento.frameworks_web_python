.. _python_dbapi:

Interfaz DB-API
===============

En Python, ofrece el acceso a :doc:`bases de datos relacionales <./base_datos_relacional>`
estandarizado por la especificación Database API (DB-API), actualmente
en la versión 2.0 *(PEP 249: Python Database API Specification v2.0)*.

Gracias a esto, se puede acceder a cualquier base de datos utilizando la misma
interfaz (ya sea un motor remoto, local, `ODBC`_, etc.). Se puede comparar con DAO,
ADO, ADO.NET en el mundo Microsoft, o a `JDBC`_ en el mundo Java.

Esta especificación es un conjunto de clases y funciones comunes,
estandarizadas, similares para los distintos motores de bases de datos
o wrappers alrededor de estos, escritos en Python. Se desarrolla con la
finalidad de lograr la consistencia entre todos estos módulos, y ampliar
las posibilidades de crear código portable entre las distintas bases de datos.

.. warning::
    Cabe aclarar que la API trata principalmente de bases de datos SQL,
    relacionales, pero implementarla, en lo posible, en motores de base
    de datos `NoSQL`_ no sería conveniente.

Es decir, el mismo código se podría llegar a usar para cualquier base de datos,
tomando siempre los recaudos necesarios: (lenguaje SQL estándar, estilo de
parámetros soportado, etc.)

Para lograr esto, el manejo de bases de datos en Python siempre sigue
los siguientes pasos:


Importar el conector
--------------------

La forma mas comunes de importar la librería de implementación DB-API

.. code-block:: python
    :linenos:

    import databasepackage as base_datos

En general, la única método que se usa directamente en la librería
es ``connect``, ya que la mayoría de las demás operaciones se realizan
en objetos devueltos después de llamar a ``this``.


Conectar a la base de datos
---------------------------

Se puede conectar a la base de datos usando la método ``connect``
del módulo conector a usar.

Los dos objetos de nivel superior cuando se trabaja con DB-API son
la conexión y el cursor. Primero obtienes una conexión a una base de datos:

.. code-block:: python
    :linenos:

    conexion = base_datos.connect()

Hay varias formas de especificar los parámetros de conexión de la base
de datos. Para la mayoría de las librerías, los valores predeterminados
para el método de conexión se conectarán a una base de datos instalada
localmente configurada de manera predeterminada.

Algunas bases de datos tienen sus propias opciones, como ``sqlite3`` tiene
la opción para una base de datos en memoria no persistente:

.. code-block:: python
    :linenos:

    conexion = sqlite3.connect(":memory:")


Abrir un cursor
---------------

Se puede abrir un Cursor a la base de datos usando la método ``cursor``
del módulo conector a usar.

A continuación, se obtiene un cursor, que se utilizará para ejecutar comandos
transaccionales, consultas SQL y manipulación de datos.

.. code-block:: python
    :linenos:

    cursor = conexion.cursor()

La mejor manera de usar la conexión y el cursor es desde los controladores
de recursos. La mayoría de las librerías de bases de datos admiten el manejo
de recursos en la conexión, pero solo unas pocas lo admiten en el cursor.
Usando `with`_, tanto la conexión como el cursor se cierran después del uso.

.. code-block:: python
    :linenos:

    server_params = {
        "database": "nomina",  # Nombre de la base de datos
        "host": "localhost",  # Dirección IP, local o remota del motor de la base de datos
        "port": "5432",  # Puerto de conexión al motor de la base de datos
        "user": "postgres",  # Nombre del usuario de conexión a la base de datos
        "password": "postgres",  # Contraseña del usuario de conexión a la base de datos
    }

    with base_datos.connect(**server_params) as conexion:
        with conexion.cursor() as cursor:
            pass  # Los comandos SQL van aquí

Si solo se admite el manejo de recursos de conexión, entonces el cursor
debe estar envuelto en un bloque de sentencias ``try`` / ``finally`` para
garantizar que el cursor esté cerrado:

.. code-block:: python
    :linenos:

    with sqlite3.connect(":memory:") as conexion:
        cursor = conexion.cursor()
        try:
            pass  # Los comandos SQL van aquí
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

Si no se admite el manejo de recursos de conexión, ambos tienen métodos
``close()`` que deben llamarse como parte de un bloque finalmente:

.. code-block:: python
    :linenos:

    conexion = sqlite3.connect(":memory:")
    cursor = conexion.cursor()
    try:
        pass  # Los comandos SQL van aquí
    except Exception as e:
        print(e)
    finally:
        if conexion:
            conexion.close()
        if cursor:
            cursor.close()

Todas las librerías para bases de datos relacionales que soportan transacciones
iniciarán automáticamente una nueva cuando la primera declaración en un cursor
nuevo o inmediatamente después de una llamada al método ``commit()`` un cursor.
Todos los cursores en la conexión se ejecutarán dentro de esa transacción.

Si se utiliza `with`_ para el manejo de recursos, la transacción se confirmará
al final del bloque. Si administra manualmente los recursos, esta transacción
debe confirmarse explícitamente antes de cerrar la conexión, o se revertirá
automáticamente. La reversión y la confirmación se realizan con los métodos
del mismo nombre:

.. code-block:: python
    :linenos:

    conexion.rollback()
    conexion.commit()

La confirmación automática también se puede habilitar configurando
``conexion.autocommit = True`` en la librería ``pyscopg2`` después de crear la
conexión pero antes de la primera ejecución.

El manejo de excepciones se puede hacer con la clase `Exception`_ genérica o con
las clases específicas para cada librería.


Ejecutar una consulta
---------------------

Se puede Ejecutar una consulta a la base de datos usando la método ``execute``
del cursor del conector a usado.

Un cursor tiene solo dos métodos, ``execute`` y ``executemany``, que se utilizan
para todas las consultas y `DML`_:

.. code-block:: python
    :linenos:

    cursor.execute("SELECT * FROM empleados")

Para consultas que involucran parámetros, hay cinco estilos de sustitución integrados
en los métodos ``execute``:


.. _python_dbapi_execute_qmark:

**qmark**

.. code-block:: sql
    :linenos:

    INSERT INTO empleados
        (nombre, apellido, fecha_nacimiento)
    VALUES
        (?, ?, ?)


.. _python_dbapi_execute_numeric:

**numeric**

.. code-block:: sql
    :linenos:

    INSERT INTO empleados
        (nombre, apellido, fecha_nacimiento)
    VALUES
        (:1, :2, :3)


.. _python_dbapi_execute_named:

**named**

.. code-block:: sql
    :linenos:

    INSERT INTO empleados
        (nombre, apellido, fecha_nacimiento)
    VALUES
        (:nombre, :apellido, :fecha_nacimiento)


.. _python_dbapi_execute_format:

**format**

.. code-block:: sql
    :linenos:

    INSERT INTO empleados
        (nombre, apellido, fecha_nacimiento)
    VALUES
        (%s, %s, %s)


.. _python_dbapi_execute_pyformat:

**pyformat**

.. code-block:: sql
    :linenos:

    INSERT INTO empleados
        (nombre, apellido, fecha_nacimiento)
    VALUES
        (%(nombre)s, %(apellido)s, %(fecha_nacimiento)s)

Se recomienda encarecidamente utilizar una de estas formas de sustitución en lugar de realizar
una construcción o reemplazo directo de cadenas. Usar los operadores de formato integrados de
Python no es la forma correcta de hacer esto.

Solo se requiere que cada DB-API admita uno de estos, pero la mayoría de las librerías admiten
más de uno.

- ``sqlite3``: :ref:`qmark <python_dbapi_execute_qmark>`, :ref:`numeric <python_dbapi_execute_numeric>` y :ref:`named <python_dbapi_execute_named>`.

- pyscopg: :ref:`format <python_dbapi_execute_format>` y :ref:`pyformat <python_dbapi_execute_pyformat>`.

- PyMySQL: :ref:`format <python_dbapi_execute_format>`.

- cx_Oracle: :ref:`named <python_dbapi_execute_named>`.

Si desea indicar al menos uno de los estilos que admite su librería DB-API, cada librería tiene
una variable global ``paramstyle`` que tiene el valor, por ejemplo, ``sqlite3.paramstyle``

Use marcadores de posición en la declaración y luego pase una :ref:`tupla <python_tuple>`
para parámetros posicionales o un :ref:`diccionario <python_dict>` para parámetros con nombre.

**qmark**

.. code-block:: python
    :linenos:

    cursor.execute("SELECT * FROM empleados WHERE nombre = ?", ("Leonardo",))

**numeric**

.. code-block:: python
    :linenos:

    cursor.execute("SELECT * FROM empleados WHERE nombre = :1", ("Leonardo",))

**named**

.. code-block:: python
    :linenos:

    cursor.execute("SELECT * FROM empleados WHERE nombre = :nombre", {"nombre": "Leonardo"})

**format**

.. code-block:: python
    :linenos:

    cursor.execute("SELECT * FROM empleados WHERE nombre = %s", ("Leonardo",))

**pyformat**

.. code-block:: python
    :linenos:

    cursor.execute(
        "SELECT * FROM empleados WHERE nombre = %(nombre)s", {"nombre": "Leonardo"}
    )


Consultar registros
-------------------

Se puede Obtener los datos a la base de datos usando la método ``fetch``
del cursor del conector a usado o iterar sobre el cursor.

Las llamadas a el método ``execute`` siempre devuelven ``None``. En realidad, no se extraen
resultados de la base de datos hasta que hacemos una llamada para buscarlos.

Se usan los métodos de búsqueda para obtener resultados de la consulta:

.. code-block:: python
    :linenos:

    cursor.fetchall()  # devuelve una lista
    cursor.fetchone()  # devuelve un objecto
    cursor.fetchmany(size=N)  # devuelve una lista

Diferentes bases de datos también proporcionan extensiones propietarias para funciones no
especificadas en DB-API. Por ejemplo, ``psycopg`` hace que el objeto cursor sea iterable, por
lo que puede recorrer de manera escalable un conjunto de resultados potencialmente grande:

.. code-block:: python
    :linenos:

    cursor.execute(
        "SELECT * FROM empleados WHERE nombre = %(nombre)s", {"nombre": "Leonardo"}
    )

    for registro in cursor:
        print(registro)


Cerrar el cursor
-----------------

Se puede Cerrar el cursor a la base de datos usando la método ``close``
del cursor del conector a usado.

.. code-block:: python
    :linenos:

    conexion.close()


Librerías mas populares
-----------------------

Las librerías de bases de datos relacionales más populares son:

- :ref:`sqlite3 <python_modulo_sqlite3>` para conexiones a *SQLite*.

- `psycopg2 <https://www.psycopg.org/docs/>`_ para conexiones a PostgreSQL.

- `mysql <http://dev.mysql.com/doc/connector-python/en/>`_ para conexiones a MySQL.

- `cx_Oracle <https://cx-oracle.readthedocs.io/en/latest/>`_ para conexiones a Oracle.

- `pypyodbc <https://pypi.org/project/pypyodbc/>`_, `pyodbc <https://pypi.org/project/pyodbc/>`_, `pymssql <https://pymssql.readthedocs.io/en/latest/>`_ para conexiones a MS SQL Server.

La librería :ref:`SQLAlchemy <python_sqlalchemy>` es el kit de herramientas
SQL de Python y el mapeador relacional de objetos.

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`JDBC`: https://es.wikipedia.org/wiki/Java_Database_Connectivity
.. _`ODBC`: https://es.wikipedia.org/wiki/Open_Database_Connectivity
.. _`NoSQL`: https://es.wikipedia.org/wiki/NoSQL
.. _`with`: https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion9/errores.html#sentencia-with
.. _`Exception`: https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion9/exceptions.html#python-exception
.. _`DML`: https://es.wikipedia.org/wiki/Lenguaje_de_manipulaci%C3%B3n_de_datos
.. _`The Novice’s Guide to the Python 3 DB-API`: https://philvarner.github.io/pages/novice-python3-db-api.html
.. _`Acceso A Bases De Datos Desde Python - Interfaz Db-Api`: https://wiki.python.org.ar/dbapi/
