.. _python_sqlacodegen:

sqlacodegen
===========

.. note::
    **Propósito:** Generador de código de modelo automático para SQLAlchemy


`sqlacodegen`_ es una herramienta que lee la estructura de una base de datos
existente y genera el código de modelos :ref:`SQLAlchemy <python_sqlalchemy_modelos>`
apropiado, usando el estilo declarativo si es posible.

Esta herramienta se escribió como reemplazo de `sqlautocode`_, que sufría varios
problemas (incluida, entre otras, la incompatibilidad con Python 3 y la última
versión de :ref:`SQLAlchemy <python_sqlalchemy_modelos>`).

Características
---------------

- Soporta ``SQLAlchemy`` 0.8.x - 1.3.x

- Produce código declarativo que casi parece escrito a mano.

- Produce código compatible con PEP 8

- Determina con precisión las relaciones, incluidos muchos a muchos, uno a uno

- Detecta automáticamente la herencia de tablas unidas

- Excelente cobertura de prueba


Instalación
-----------

Para instalar la librería ``sqlacodegen`` debe seguir los siguientes pasos:

.. code-block:: console

    $> pip install git+https://github.com/agronholm/sqlacodegen.git@3.0.0rc1#egg=sqlacodegen

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando:

.. code-block:: console

    $ python -c "import sqlacodegen ; print(sqlacodegen.__name__)"

Si muestra el numero de la versión instalada de ``sqlacodegen``, tiene
correctamente instalada la librería. Con esto, ya tiene todo listo para continuar.

.. _python_sqlacodegen_uso:

Conexión al Engine
------------------

Luego configura el :ref:`engine <python_sqlalchemy_engine>` (cadena de conexión)
para la DB respectiva. Para esto se explican algunas configuraciones, para SQLite,
:ref:`MySQL <python_pkg_mysql>` y :ref:`PostgreSQL <python_pkg_postgresql>` a continuación:

.. tip::
    Cada cadena de conexión necesita que se instale la librería dependiente.


SQLite
^^^^^^

Para configurar el ``engine`` con ``SQLite`` debe definir la :ref:`cadena de conexión <python_sqlite3_conn_strs>`
que esta compuesto por varios parámetros.

Los parámetros deben ser reemplazadas con sus propios datos en la linea de comando a continuación:

.. code-block:: console

    $ sqlacodegen --generator declarative sqlite:///{RUTA_BD}/{ARCHIVO_BD} --outfile models.py

.. code-block:: console

    $.\sqlacodegen.exe --generator declarative sqlite:///sistema.db --outfile models.py


MySQL
^^^^^

Para configurar el ``engine`` con ``MySQL`` debe definir la :ref:`cadena de conexión <python_mysql_conn_strs>`
que esta compuesto por varios parámetros, los cuales deben ser reemplazadas con sus propios datos
en la linea de comando con el comando ``sqlacodegen``.

.. tip::
    Para conectarte al servidor ``MySQL`` necesite el paquete :ref:`PyMySQL <python_mysql_instalar>`.

Luego ya teniendo instalado el paquete ``PyMySQL`` debe ejecutar el siguiente comando
de ``sqlacodegen``, con el siguiente comando:

.. code-block:: console

    $ sqlacodegen --generator declarative mysql+pymysql://USER:PASSW@HOST:PORT/DB --outfile models.py

.. code-block:: console

    $> .\sqlacodegen.exe --generator declarative mysql+pymysql://USER:PASSW@HOST:PORT/DB --outfile models.py


PostgreSQL
^^^^^^^^^^

Para configurar el ``engine`` con ``PostgreSQL`` debe definir la :ref:`cadena de conexión <python_psycopg2_conn_strs>`
que esta compuesto por varios parámetros, los cuales deben ser reemplazadas con sus propios datos
en la linea de comando con el comando ``sqlacodegen``.

.. tip::
    Para conectarte al servidor ``PostgreSQL`` necesite el paquete :ref:`psycopg2 <python_psycopg2_instalar>`.

Luego ya teniendo instalado el paquete ``psycopg2`` debe ejecutar el siguiente comando
de ``sqlacodegen``, con el siguiente comando:

.. code-block:: console

    $ sqlacodegen --generator declarative postgresql://USER:PASSW@HOST:PORT/DB --outfile models.py

.. code-block:: console

    $> .\sqlacodegen.exe --generator declarative postgresql://USER:PASSW@HOST:PORT/DB --outfile models.py


Si necesita más tipos de cadenas de conexión o :ref:`engine <python_sqlalchemy_engine>`, puede
consultar el apartado `Engine Configuration`_ de la documentación oficial de ``SQLAlchemy``.


El anterior comando al ejecutar debe generar un modulo python llamado ``models.py`` que contiene el siguiente código:

.. code-block:: python
    :linenos:

    pass


.. _python_sqlacodegen_scaffolding:

Estructura de proyecto
----------------------

A continuación la estructura de proyecto ``sistema``

.. code-block:: console

    sistema/
    ├── db.py
    ├── __init__.py
    ├── main.py
    ├── models.py
    ├── requirements.txt
    ├── sistema.db
    └── venezuela_data.sql

*Archivo requirements.txt*

.. literalinclude:: ../../recursos/leccion12/sqlacodegen/sistema/requirements.txt
    :language: python
    :linenos:
    :lines: 1-2

*Archivo db.py*

.. literalinclude:: ../../recursos/leccion12/sqlacodegen/sistema/db.py
    :language: python
    :linenos:
    :lines: 1-18

*Archivo models.py*

.. literalinclude:: ../../recursos/leccion12/sqlacodegen/sistema/models.py
    :language: python
    :linenos:
    :lines: 1-100

*Archivo main.py*

.. literalinclude:: ../../recursos/leccion12/sqlacodegen/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-25


Teniendo creada la anterior estructura de proyecto

Vuelva a ejecutar ahora el modulo con el siguiente comando:

.. code-block:: console

   $> pip install -r requirements.txt
   $> python main.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    ¡Creación exitosa de la tabla productos!

    ¡Inserción exitosa de los 4 productos!


Asi de esta forma puede usar ``sqlacodegen`` para generar modelos ``SQLAlchemy`` desde una base de datos
existente e implementar las operaciones ingresar, consultar, actualizar y eliminar registro en las tablas.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion12>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`sqlacodegen`: https://pypi.org/project/sqlacodegen/
.. _`sqlautocode`: http://code.google.com/p/sqlautocode/
.. _`Engine Configuration`: https://docs.sqlalchemy.org/en/14/core/engines.html
