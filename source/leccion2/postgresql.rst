.. _python_pkg_postgresql:

PostgreSQL
==========

.. note::
    **Propósito:** Es un Adaptador Python de base de datos `PostgreSQL`_.

Psycopg, es el adaptador de base de datos PostgreSQL más popular para el lenguaje
de programación Python. Sus principales características son la implementación completa
de la especificación Python :ref:`DB-API 2.0 <python_dbapi>` y la seguridad de
subprocesos (varios subprocesos pueden compartir la misma conexión).

Fue diseñado para aplicaciones con múltiples subprocesos que crean y destruyen muchos
cursores y hacen una gran cantidad de ":ref:`INSERT <python_base_ingresar_registro>`"
o ":ref:`UPDATE <python_base_actualizar_registro>`" simultáneos.

`psycopg2`_ se implementa principalmente en C como un envoltorio de `libpq`_, lo que
resulta en que sea eficiente y seguro. Cuenta con cursores del lado del cliente y del lado
del servidor, comunicación asíncrona y notificaciones, compatibilidad con sentencias ``COPY``.
Muchos tipos de Python son compatibles de forma inmediata y están adaptados para coincidir
con los tipos de datos de ``PostgreSQL``; la adaptación se puede ampliar y personalizar gracias
a un sistema flexible de adaptación de objetos.

.. note::
    ``psycopg2`` es compatible tanto con Unicode como con Python 3.


.. _python_psycopg2_instalar:

Instalación
-----------

Para conectarte al servidor ``PostgreSQL`` necesita el paquete `psycopg2`_. Esto significa
que debe instalar ``psycopg2`` ejecutando los siguientes comandos:

.. code-block:: console

    $ sudo apt install build-essential libpq-dev python3-dev
    $ pip install psycopg2

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando:

.. code-block:: console

  $ python -c "import psycopg2 ; print(psycopg2.__version__)"

Si muestra el numero de la versión instalada de ``psycopg2``, tiene
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
registro en una tabla en una base de datos ``PostgreSQL``.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion12>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`PostgreSQL`: https://www.postgresql.org/
.. _`psycopg2`: https://pypi.org/project/psycopg2/
.. _`psycopg2`: https://pypi.org/project/psycopg2/
.. _`libpq`: https://www.postgresql.org/docs/current/static/libpq.html
