.. _python_pkg_mysql:

MySQL
=====

.. note::
    **Propósito:** Controlador `MySQL`_ escrito en Python que no depende de las bibliotecas
    cliente MySQL C e implementa la especificación :ref:`DB API <python_dbapi>` v2.0 (PEP-249).

A diferencia de :ref:`SQLite <python_modulo_sqlite3>`, no hay un módulo Python SQL
predeterminado que pueda usar para conectarse a una base de datos MySQL. En su lugar,
deberá instalar un controlador Python SQL para MySQL para poder interactuar con una
base de datos MySQL desde una aplicación de Python.

.. tip::
    Uno de esos controladores es `mysql-connector-python`_.


.. _python_mysql_instalar:

Instalación
-----------

Para conectarte al servidor ``MySQL`` necesita el paquete `mysql-connector-python`_. Esto
significa que debe instalar ``mysql-connector-python`` ejecutando el siguiente comando:

.. code-block:: console

  $ pip install mysql-connector-python

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando:

.. code-block:: console

  $ python -c "import mysql.connector ; print(mysql.connector.__version__)"

Si muestra el numero de la versión instalada de ``mysql-connector-python``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.


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
.. _`mysql-connector-python`: https://pypi.org/project/mysql-connector-python/
