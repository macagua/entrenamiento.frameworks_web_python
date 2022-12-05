.. _python_pkg_mysql:

MySQL
=====

.. note::
    **Propósito:** Controlador `MySQL`_ escrito en Python que no depende de las bibliotecas
    cliente MySQL C e implementa la especificación :ref:`DB API v2.0 (PEP-249) <python_dbapi>`.

A diferencia de :ref:`SQLite <python_modulo_sqlite3>`, no hay un módulo Python SQL
predeterminado que pueda usar para conectarse a una base de datos MySQL. En su lugar,
deberá instalar un controlador Python SQL para MySQL para poder interactuar con una
base de datos MySQL desde una aplicación de Python.

.. tip::
    Uno de esos controladores es `PyMySQL`_.


.. _python_mysql_instalar:

Instalación
-----------

Para conectarte al servidor ``MySQL`` necesita el paquete `PyMySQL`_. Esto
significa que debe instalar ``PyMySQL`` ejecutando el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install PyMySQL

   .. group-tab:: Windows

      .. code-block:: console

          > pip install PyMySQL


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import pymysql ; print(pymysql.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import pymysql ; print(pymysql.__version__)"


Si muestra el numero de la versión instalada de ``PyMySQL``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.


.. _python_mysql_conn_strs:

Cadenas de conexión
-------------------

Para definir el método ``connect`` debe definir las cadenas de conexión con
``MySQL`` como se describe a continuación:

``USER``
    Usuario de conexión a la base de datos.

``PASSW``
    Contraseña del usuario de conexión a la base de datos.

``HOST``
    IP o dirección DNS de conexión al servidor de la base de datos.

``PORT``
    Puerto de conexión al servidor de la base de datos, por defecto es **3306**.

``DB``
    Nombre de la base de datos a cual conectar.

A continuación presento un ejemplo en Python implementando una cadena de conexión
para una base de datos ``MySQL``:

.. code-block:: python
    :linenos:

    import pymysql

    USER = "root"
    PASSW = "root"
    HOST = "localhost"
    PORT = 3306
    DB = "sistema"

    conexion_bd = pymysql.connect(
        user=USER, password=PASSW, host=HOST, port=PORT, database=DB
    )

El ejemplo anterior se describe a continuación:

    - En la linea 1, se importa la librería ``pymysql``.

    - En la linea 3, se define en la constante ``USER``, del usuario de conexión a la base de datos.

    - En la linea 4, se define en la constante ``PASSW``, de la contraseña del usuario de conexión a la base de datos.

    - En la linea 5, se define en la constante ``HOST``, la IP o dirección DNS de conexión al servidor de la base de datos.

    - En la linea 6, se define en la constante ``PORT``, el puerto de conexión al servidor de la base de datos.

    - En la linea 7, se define en la constante ``DB``, el nombre de la base de datos a cual conectar.

    - En la linea 8, se define en el método ``connect``, el cual establece la conexión a la base de datos.

De esta forma se crea una cadena de conexión para ``MySQL`` para ser usada por el método ``connect``.


Insertar registros
------------------

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:


Consultar registros
-------------------

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:


Actualizar registros
--------------------

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:


Eliminar registros
------------------

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. todo::
    TODO Terminar de escribir esta sección.

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en una tabla en una base de datos ``MySQL``.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion12>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`MySQL`: https://www.mysql.com/
.. _`PyMySQL`: https://pymysql.readthedocs.io/en/latest/
