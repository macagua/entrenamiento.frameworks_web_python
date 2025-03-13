.. _python_dbapi:

Interfaz DB-API
===============

En Python, ofrece el acceso a :ref:`bases de datos relacionales <python_base_datos_relacional>`
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

La forma más comunes de importar el módulo de implementación DB-API

.. code-block:: python
    :class: no-copy

    import databasepackage as base_datos

En general, la única método que se usa directamente en el módulo
es ``connect``, ya que la mayoría de las demás operaciones se realizan
en objetos devueltos después de llamar a ``this``.


Conectar a la base de datos
---------------------------

Se puede conectar a la base de datos usando la método ``connect``
del módulo conector a usar.

Los dos objetos de nivel superior cuando se trabaja con DB-API son
la conexión y el cursor. Primero obtienes una conexión a una base de datos:

.. code-block:: python
    :class: no-copy

    conexion = base_datos.connect()

Hay varias formas de especificar los parámetros de conexión de la base
de datos. Para la mayoría de los módulos, los valores predeterminados
para el método de conexión se conectarán a una base de datos instalada
localmente configurada de manera predeterminada.

Algunas bases de datos tienen sus propias opciones, como el módulo :ref:`sqlite3 <python_modulo_sqlite3>` tiene
la opción para una base de datos en memoria no persistente:

.. code-block:: python

    conexion = sqlite3.connect(":memory:")


Abrir un cursor
---------------

Se puede abrir un Cursor a la base de datos usando la método ``cursor``
del módulo conector a usar.

A continuación, se obtiene un cursor, que se utilizará para ejecutar comandos
transaccionales, consultas SQL y manipulación de datos.

.. code-block:: python

    cursor = conexion.cursor()

La mejor manera de usar la conexión y el cursor es desde los controladores
de recursos. La mayoría de los módulos de bases de datos admiten el manejo
de recursos en la conexión, pero solo unas pocas lo admiten en el cursor.
Usando la sentencia :ref:`with <python_sent_with>`, tanto la conexión como el cursor se cierran después del uso.

.. code-block:: python

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
debe estar envuelto en un bloque de sentencias :ref:`try <python_sent_try_except>` / :ref:`finally <python_sent_finally>` para
garantizar que el cursor esté cerrado:

.. code-block:: python

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

Todas los módulos para bases de datos relacionales que soportan transacciones
iniciarán automáticamente una nueva cuando la primera declaración en un cursor
nuevo o inmediatamente después de una llamada al método ``commit()`` un cursor.
Todos los cursores en la conexión se ejecutarán dentro de esa transacción.

Si se utiliza la sentencia :ref:`with <python_sent_with>` para el manejo de recursos, la transacción se confirmará
al final del bloque. Si administra manualmente los recursos, esta transacción
debe confirmarse explícitamente antes de cerrar la conexión, o se revertirá
automáticamente.

El ``rollback`` se realizan con el método del mismo nombre:

.. code-block:: python

    conexion.rollback()

El ``commit`` se realizan con el método del mismo nombre:

.. code-block:: python

    conexion.commit()

La confirmación automática también se puede habilitar configurando
``conexion.autocommit = True`` en el módulo ``pyscopg2`` después de crear la
conexión pero antes de la primera ejecución.

El manejo de excepciones se puede hacer con la clase :ref:`Exception <python_exception>` genérica o con
las clases específicas para cada librería.


Ejecutar una consulta
---------------------

Se puede Ejecutar una consulta a la base de datos usando la método ``execute``
del cursor del conector a usado.

Un cursor tiene solo dos métodos, ``execute`` y ``executemany``, que se utilizan
para todas las consultas y `DML`_:

.. code-block:: python

    cursor.execute("SELECT * FROM clientes")

Para consultas que involucran parámetros, hay cinco estilos de sustitución integrados
en los métodos ``execute``:


.. _python_dbapi_execute_qmark:

**qmark**

.. code-block:: sql
    :linenos:

    INSERT INTO clientes
        (nombre, apellido, codigo_postal, telefono)
    VALUES
        (?, ?, ?, ?)


.. _python_dbapi_execute_numeric:

**numeric**

.. code-block:: sql
    :linenos:

    INSERT INTO clientes
        (nombre, apellido, codigo_postal, telefono)
    VALUES
        (:1, :2, :3, :4)


.. _python_dbapi_execute_named:

**named**

.. code-block:: sql
    :linenos:

    INSERT INTO clientes
        (nombre, apellido, codigo_postal, telefono)
    VALUES
        (:nombre, :apellido, :codigo_postal, :telefono)


.. _python_dbapi_execute_format:

**format**

.. code-block:: sql
    :linenos:

    INSERT INTO clientes
        (nombre, apellido, codigo_postal, telefono)
    VALUES
        (%s, %s, %s, %s)


.. _python_dbapi_execute_pyformat:

**pyformat**

.. code-block:: sql
    :linenos:

    INSERT INTO clientes
        (nombre, apellido, codigo_postal, telefono)
    VALUES
        (%(nombre)s, %(apellido)s, %(codigo_postal)s, %(telefono)s)

Se recomienda encarecidamente utilizar una de estas formas de sustitución en lugar de realizar
una construcción o reemplazo directo de cadenas. Usar los operadores de formato integrados de
Python no es la forma correcta de hacer esto.

Solo se requiere que cada DB-API admita uno de estos, pero la mayoría de los módulos admiten
más de uno.

- ``sqlite3``: :ref:`qmark <python_dbapi_execute_qmark>`, :ref:`numeric <python_dbapi_execute_numeric>` y :ref:`named <python_dbapi_execute_named>`.

- ``pyscopg``: :ref:`format <python_dbapi_execute_format>` y :ref:`pyformat <python_dbapi_execute_pyformat>`.

- ``PyMySQL``: :ref:`format <python_dbapi_execute_format>`.

- ``cx_Oracle``: :ref:`named <python_dbapi_execute_named>`.

Si desea indicar al menos uno de los estilos que admite su librería DB-API, cada librería tiene
una variable global ``paramstyle`` que tiene el valor, por ejemplo, ``sqlite3.paramstyle``

Use marcadores de posición en la declaración y luego pase una :ref:`tupla <python_tuple>`
para parámetros posicionales o un :ref:`diccionario <python_dict>` para parámetros con nombre.

**qmark**

.. code-block:: python

    cursor.execute("SELECT * FROM clientes WHERE nombre = ?", ("Leonardo",))

**numeric**

.. code-block:: python

    cursor.execute("SELECT * FROM clientes WHERE nombre = :1", ("Leonardo",))

**named**

.. code-block:: python

    cursor.execute("SELECT * FROM clientes WHERE nombre = :nombre", {"nombre": "Leonardo"})

**format**

.. code-block:: python

    cursor.execute("SELECT * FROM clientes WHERE nombre = %s", ("Leonardo",))

**pyformat**

.. code-block:: python

    cursor.execute(
        "SELECT * FROM clientes WHERE nombre = %(nombre)s", {"nombre": "Leonardo"}
    )


Consultar registros
-------------------

Se puede Obtener los datos a la base de datos usando la método ``fetch``
del cursor del conector a usado o iterar sobre el cursor.

Las llamadas a el método ``execute`` siempre devuelven ``None``. En realidad, no se extraen
resultados de la base de datos hasta que hacemos una llamada para buscarlos.

Se usan los métodos de búsqueda para obtener resultados de la consulta:

Devolver una lista de objectos

.. code-block:: python

    cursor.fetchall()

Devolver un objecto

.. code-block:: python

    cursor.fetchone()

Devolver una lista de 5 objectos

.. code-block:: python

    cursor.fetchmany(size=5)

Diferentes bases de datos también proporcionan extensiones propietarias para funciones no
especificadas en DB-API. Por ejemplo, :ref:`psycopg <python_pkg_postgresql>` hace que el
objeto cursor sea iterable, por lo que puede recorrer de manera escalable un conjunto de
resultados potencialmente grande:

.. code-block:: python
    :linenos:

    cursor.execute(
        "SELECT * FROM clientes WHERE nombre = %(nombre)s", {"nombre": "Leonardo"}
    )

    for registro in cursor:
        print(registro)


Cerrar el cursor
-----------------

Se puede cerrar el cursor a la base de datos usando la método ``close``
del cursor del conector a usado.

.. code-block:: python

    conexion.close()


Módulos más populares
---------------------

Las módulos Python más populares para el manejo de bases de datos relacionales son:

- :ref:`sqlite3 <python_modulo_sqlite3>` para conexiones a *SQLite*.

- :ref:`psycopg <python_pkg_postgresql>` para conexiones a *PostgreSQL*.

- :ref:`PyMySQL <python_pkg_mysql>` para conexiones a *MySQL*.

- `cx_Oracle`_ para conexiones a *Oracle*.

- `pypyodbc`_, `pyodbc`_, `pymssql`_ para conexiones a *MS SQL Server*.

- :ref:`SQLAlchemy <python_sqlalchemy>` es el kit de herramientas SQL de Python y el
  mapeador relacional de objetos.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`JDBC`: https://es.wikipedia.org/wiki/Java_Database_Connectivity
.. _`ODBC`: https://es.wikipedia.org/wiki/Open_Database_Connectivity
.. _`NoSQL`: https://es.wikipedia.org/wiki/NoSQL
.. _`DML`: https://es.wikipedia.org/wiki/Lenguaje_de_manipulaci%C3%B3n_de_datos
.. _`Acceso A Bases De Datos Desde Python - Interfaz Db-Api`: https://wiki.python.org.ar/dbapi/
.. _`cx_Oracle`: https://cx-oracle.readthedocs.io/en/latest/
.. _`pypyodbc`: https://pypi.org/project/pypyodbc/
.. _`pyodbc`: https://pypi.org/project/pyodbc/
.. _`pymssql`: https://pymssql.readthedocs.io/en/latest/
