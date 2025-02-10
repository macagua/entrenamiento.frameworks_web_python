.. _python_pkg_postgresql:

PostgreSQL
==========

.. note::
    **Propósito:** Es un Adaptador Python de base de datos `PostgreSQL`_.

`psycopg`_, es el adaptador de base de datos PostgreSQL más popular para el lenguaje
de programación Python. Sus principales características son la implementación completa
de la especificación Python :ref:`DB-API 2.0 <python_dbapi>` y la seguridad de
subprocesos (varios subprocesos pueden compartir la misma conexión).

Fue diseñado para aplicaciones con múltiples subprocesos que crean y destruyen muchos
cursores y hacen una gran cantidad de ":ref:`INSERT <python_base_ingresar_registro>`"
o ":ref:`UPDATE <python_base_actualizar_registro>`" simultáneos.

`psycopg`_ se implementa principalmente en C como un envoltorio de `libpq`_, lo que
resulta en que sea eficiente y seguro. Cuenta con cursores del lado del cliente y del lado
del servidor, comunicación asíncrona y notificaciones, compatibilidad con sentencias ``COPY``.
Muchos tipos de Python son compatibles de forma inmediata y están adaptados para coincidir
con los tipos de datos de ``PostgreSQL``; la adaptación se puede ampliar y personalizar gracias
a un sistema flexible de adaptación de objetos.

.. note::
    ``psycopg`` es compatible tanto con Unicode como con Python 3.


.. _python_psycopg2_instalar:

Instalación
-----------

Para conectarte al servidor ``PostgreSQL`` necesita el paquete `psycopg2`_. Esto
significa que debe instalar ``psycopg2`` ejecutando los siguientes comandos, el
cual a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ sudo apt install build-essential libpq-dev python3-dev
          $ pip install psycopg2

   .. group-tab:: Windows

      .. code-block:: console

          > pip install psycopg2


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import psycopg2 ; print(psycopg2.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import psycopg2 ; print(psycopg2.__version__)"


Si muestra el numero de la versión instalada de ``psycopg2``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.


.. _python_psycopg2_conn_strs:

Cadenas de conexión
-------------------

Para definir el método ``connect`` debe definir las cadenas de conexión con
``PostgreSQL`` como se describe a continuación:

``USER``
    Usuario de conexión a la base de datos.

``PASSW``
    Contraseña del usuario de conexión a la base de datos.

``HOST``
    IP o dirección DNS de conexión al servidor de la base de datos.

``PORT``
    Puerto de conexión al servidor de la base de datos, por defecto es **5492**.

``DB``
    Nombre de la base de datos a cual conectar.

A continuación presento un ejemplo en Python implementando una cadena de conexión
para una base de datos ``PostgreSQL``:

.. code-block:: python
    :linenos:

    import psycopg2

    USER = "root"
    PASSW = "root"
    HOST = "localhost"
    PORT = 5492
    DB = "sistema"

    conexion_bd = psycopg2.connect(
        user=USER, password=PASSW, host=HOST, port=PORT, database=DB
    )

El ejemplo anterior se describe a continuación:

    - En la linea 1, se importa la librería ``psycopg2``.

    - En la linea 3, se define en la constante ``USER``, del usuario de conexión a la base de datos.

    - En la linea 4, se define en la constante ``PASSW``, de la contraseña del usuario de conexión a la base de datos.

    - En la linea 5, se define en la constante ``HOST``, la IP o dirección DNS de conexión al servidor de la base de datos.

    - En la linea 6, se define en la constante ``PORT``, el puerto de conexión al servidor de la base de datos.

    - En la linea 7, se define en la constante ``DB``, el nombre de la base de datos a cual conectar.

    - En la linea 8, se define en el método ``connect``, el cual establece la conexión a la base de datos.

De esta forma se crea una cadena de conexión para ``PostgreSQL`` para ser usada por el método ``connect``.


Insertar registros
------------------

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_insert.py
    :language: python
    :linenos:
    :lines: 1-72

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_insert.py <../../recursos/leccion2/postgresql/crud/postgresql_record_insert.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_insert.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        leccion2/
        └── postgresql/
            └── crud/
                └── postgresql_record_insert.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python postgresql_record_insert.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Fueron insertado(s) 3 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión PostgreSQL a la base de datos sistema.db fue cerrada!


Consultar registros
-------------------

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_select.py
    :language: python
    :linenos:
    :lines: 1-55

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_select.py <../../recursos/leccion2/postgresql/crud/postgresql_record_select.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_select.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        leccion2/
        └── postgresql/
            └── crud/
                └── postgresql_record_select.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python postgresql_record_select.py

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

    INFO:root:¡La conexión PostgreSQL a la base de datos sistema.db fue cerrada!


Actualizar registros
--------------------

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_update.py
    :language: python
    :linenos:
    :lines: 1-57

----

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_update.py <../../recursos/leccion2/postgresql/crud/postgresql_record_update.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_update.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        leccion2/
        └── postgresql/
            └── crud/
                └── postgresql_record_update.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python postgresql_record_update.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión PostgreSQL a la base de datos sistema.db fue cerrada!


Eliminar registros
------------------

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_delete.py
    :language: python
    :linenos:
    :lines: 1-52

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_delete.py <../../recursos/leccion2/postgresql/crud/postgresql_record_delete.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_delete.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        leccion2/
        └── postgresql/
            └── crud/
                └── postgresql_record_delete.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python postgresql_record_delete.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos sistema.db!

    INFO:root:¡Registro eliminado correctamente!

    INFO:root:¡La conexión PostgreSQL a la base de datos sistema.db fue cerrada!


Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en una tabla en una base de datos ``PostgreSQL``.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`PostgreSQL`: https://www.postgresql.org/
.. _`psycopg`: https://www.psycopg.org/docs/
.. _`psycopg2`: https://pypi.org/project/psycopg2/
.. _`libpq`: https://www.postgresql.org/docs/current/libpq.html
