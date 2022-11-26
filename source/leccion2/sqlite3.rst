.. _python_modulo_sqlite3:

sqlite3 - DB-API 2.0 interfaz para bases de datos SQLite
========================================================


.. note::
    **Propósito:** es una libraría proporciona una interfaz SQL compatible con
    la especificación :ref:`DB-API 2.0 <python_dbapi>` requiere SQLite 3.7.15 o
    posterior.

Una `base de datos <https://es.wikipedia.org/wiki/Base_de_datos>`_
es un conjunto de datos pertenecientes a un mismo contexto y
almacenados sistemáticamente para su posterior uso.

SQLite
^^^^^^

Es una libraría de C que provee una base de datos ligera basada en disco que no requiere
un proceso de servidor separado y permite acceder a la base de datos usando una variación
no estándar del lenguaje de consulta SQL. Algunas aplicaciones pueden usar SQLite para
almacenamiento interno. También es posible prototipar una aplicación usando SQLite y luego
transferir el código a una base de datos más grande como PostgreSQL u Oracle.

Insertar registro en una tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite3_record_insert.py
    :language: python
    :linenos:
    :lines: 1-55

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Fueron insertado(s) 3 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Consultar registros de tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite3_record_select.py
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


Actualizar registro de tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite3_record_update.py
    :language: python
    :linenos:
    :lines: 1-54

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Eliminar registro de tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sqlite3_record_delete.py
    :language: python
    :linenos:
    :lines: 1-44

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Registro eliminado correctamente!

    INFO:root:¡La conexión SQLite a la base de datos sistema.db fue cerrada!


Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en una tabla SQLite.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion12>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`sqlite3`: https://docs.python.org/es/3.7/library/sqlite3.html
