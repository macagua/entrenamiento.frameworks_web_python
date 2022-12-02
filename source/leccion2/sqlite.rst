.. _python_modulo_sqlite3:

SQLite
======

.. note::
    **Propósito:** es una libraría proporciona una interfaz SQL compatible con
    la especificación :ref:`DB-API 2.0 <python_dbapi>` requiere SQLite 3.7.15 o
    posterior.

`SQLite`_, es una libraría de C que provee una base de datos ligera basada en
disco que no requiere un proceso de servidor separado y permite acceder a la base
de datos usando una variación no estándar del lenguaje de consulta SQL.

Algunas aplicaciones pueden usar SQLite para almacenamiento interno. También es posible
prototipar una aplicación usando SQLite y luego transferir el código a una base de
datos más grande como :ref:`PostgreSQL <python_pkg_postgresql>` u `Oracle <https://cx-oracle.readthedocs.io/en/latest/>`_.


.. _python_sqlite3_instalar:

Instalación
-----------

La librería ``sqlite3`` esta incluida en librería estándar de Python, puede probar la
instalación existe, ejecutando el siguiente comando:

.. code-block:: console

  $ python -c "import sqlite3 ; print(sqlite3.__package__)"

Si muestra el nombre del paquete  ``sqlite3``, tiene instalado la librería.

Adicionalmente puedes instalar administradores de base de datos nativos para sistemas
operativos, a continuación se presentan alternativas:

Plataforma Linux
^^^^^^^^^^^^^^^^

Para instalar administradores de base de datos nativos ``sqlite3`` para la plataforma
Linux debe seguir los siguientes pasos:

.. code-block:: console

  $ sudo apt install sqlite3 sqlitebrowser

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando:

.. code-block:: console

    $ sqlite3
    SQLite version 3.31.1 2020-01-27 19:55:54
    Enter ".help" for usage hints.
    Connected to a transient in-memory database.
    Use ".open FILENAME" to reopen on a persistent database.
    sqlite>

Si muestra la consola sqlite ``sqlite>``, tiene correctamente instalada el administrador
de base de datos nativa ``sqlite3`` por linea de comando.

Puede probar si la instalación del el administrador de base de datos nativo de ``sqlite3``
gráfico llamado ``sqlitebrowser`` se realizo correctamente, ejecutando el siguiente comando:

.. code-block:: console

    $ sqlitebrowser

Si muestra la interfaz gráfica de ``sqlite>``, tiene correctamente instalada el administrador
de base de datos nativo de ``sqlite3`` gráfico llamado ``sqlitebrowser``.


.. _python_sqlite3_conn_strs:

Cadenas de conexión
-------------------

Para definir el método ``connect`` debe definir las cadenas de conexión con
``SQLite`` como se describe a continuación:

``DB_PATH``
    Ruta absoluta o relativa del archivo de base de datos ``SQLite``.

``DB_FILE``
    Nombre del archivo de base de datos ``SQLite``.

A continuación presento un ejemplo en Python implementando una cadena de conexión
para una base de datos ``SQLite``:

.. code-block:: python
    :linenos:

    import os
    import sqlite3

    DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
    DB_FILE = "sistema.db"
    DB = DB_PATH + DB_FILE

    conexion = sqlite3.connect(DB)

El ejemplo anterior se describe a continuación:

    - En la linea 1, se importa la librería ``os`` de la librería estándar Python.

    - En la linea 2, se importa la librería ``sqlite3`` de la librería estándar Python.

    - En la linea 4, se define en la constante ``DB_PATH`` la ruta absoluta usada para guardar la base de datos.

    - En la linea 5, se define en la constante ``DB_FILE`` el nombre de la base de datos.

    - En la linea 6, se define en la constante ``DB`` la ruta completa usada para leer la base de datos.

De esta forma se crea una cadena de conexión para ``SQLite`` para ser usada por el método ``connect``.


Insertar registros
------------------

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite/sqlite3_record_insert.py
    :language: python
    :linenos:
    :lines: 1-55

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Fueron insertado(s) 3 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Consultar registros
-------------------

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite/sqlite3_record_select.py
    :language: python
    :linenos:
    :lines: 1-51

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    Total de filas son: 3

    Mostrar cada fila:

            Id: 1
            Nombre: Leonardo
            Código postal: Caballero
            Teléfono: 5001

            Id: 2
            Nombre: Ana
            Código postal: Poleo
            Teléfono: 6302

            Id: 3
            Nombre: Pedro
            Código postal: Lopez
            Teléfono: 4001

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Actualizar registros
--------------------

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite/sqlite3_record_update.py
    :language: python
    :linenos:
    :lines: 1-54

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Eliminar registros
------------------

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite/sqlite3_record_delete.py
    :language: python
    :linenos:
    :lines: 1-44

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Registro eliminado correctamente!

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en una tabla en una base de datos ``SQLite``.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion12>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`SQLite`: https://www.sqlite.org/index.html
.. _`sqlite3`: https://docs.python.org/es/3.7/library/sqlite3.html
