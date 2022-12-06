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

- Soporta ``SQLAlchemy`` 0.8.x - 1.4.x.

- Produce código declarativo que casi parece escrito a mano.

- Produce código compatible con PEP 8.

- Determina con precisión las relaciones, incluidos muchos a muchos, uno a uno.

- Detecta automáticamente la herencia de tablas unidas.

- Excelente cobertura de prueba.


Instalación
-----------

Para instalar la librería ``sqlacodegen`` debe seguir el siguientes paso, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install git+https://github.com/agronholm/sqlacodegen.git@3.0.0rc1#egg=sqlacodegen

   .. group-tab:: Windows

      .. code-block:: console

          > pip install git+https://github.com/agronholm/sqlacodegen.git@3.0.0rc1#egg=sqlacodegen


Puede probar si la instalación se realizo correctamente, ejecutando el siguiente
comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import sqlacodegen ; print(sqlacodegen.__name__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import sqlacodegen ; print(sqlacodegen.__name__)"


Si muestra el nombre del paquete como ``sqlacodegen``, tiene correctamente instalada
la librería. Con esto, ya tiene todo listo para continuar.

.. _python_sqlacodegen_uso:

Conexión al Engine
------------------

Luego configura el :ref:`engine <python_sqlalchemy_engine>` (cadena de conexión)
para la DB respectiva. Para esto se explican algunas configuraciones, para SQLite,
:ref:`MySQL <python_pkg_mysql>` y :ref:`PostgreSQL <python_pkg_postgresql>`
a continuación:

.. tip::
    Cada cadena de conexión necesita que se instale la librería dependiente.


SQLite
^^^^^^

Para configurar el ``engine`` con ``SQLite`` debe definir la :ref:`cadena de conexión <python_sqlite3_conn_strs>`
que esta compuesto por varios parámetros.

Los parámetros deben ser reemplazadas con sus propios datos en la linea de comando:

.. code-block:: console

    $ sqlacodegen --generator declarative sqlite:///{DB_PATH}/{DB_FILE} --outfile file.py

A continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ sqlacodegen --generator declarative sqlite:///sistema.db --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          > .\sqlacodegen.exe --generator declarative sqlite:///sistema.db --outfile models.py


El anterior comando al ejecutar debe generar un modulo python llamado ``models.py`` que contiene el siguiente código:

.. code-block:: python
    :linenos:

    from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
    from sqlalchemy.orm import declarative_base, relationship

    Base = declarative_base()


    class Estados(Base):
        __tablename__ = 'estados'

        id = Column(Integer, primary_key=True, unique=True)
        nombre = Column(String(25), nullable=False)
        codigo = Column(String(2), nullable=False)

        ciudades = relationship('Ciudades', back_populates='estados')


    class Productos(Base):
        __tablename__ = 'productos'

        id = Column(Integer, primary_key=True, unique=True)
        nombre = Column(String(11), nullable=False)
        descripcion = Column(String(25), nullable=False)
        categoria = Column(String(25), nullable=False)
        precio = Column(Integer, nullable=False)
        status = Column(Enum('y', 'n'), nullable=False)

        pedidos = relationship('Pedidos', back_populates='producto')


    class Ciudades(Base):
        __tablename__ = 'ciudades'

        id = Column(Integer, primary_key=True, unique=True)
        id_estado = Column(ForeignKey('estados.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
        nombre = Column(String(25), nullable=False)
        capital = Column(Integer, nullable=False)

        estados = relationship('Estados', back_populates='ciudades')
        clientes = relationship('Clientes', back_populates='ciudades')


    class Clientes(Base):
        __tablename__ = 'clientes'

        id = Column(Integer, primary_key=True, unique=True)
        nombre = Column(String(25), nullable=False)
        apellido = Column(String(25), nullable=False)
        codigo_postal = Column(ForeignKey('ciudades.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
        telefono = Column(String(11), nullable=False)

        ciudades = relationship('Ciudades', back_populates='clientes')
        pedidos = relationship('Pedidos', back_populates='cliente')


    class Pedidos(Base):
        __tablename__ = 'pedidos'

        id = Column(Integer, primary_key=True, unique=True)
        cliente_id = Column(ForeignKey('clientes.id'), nullable=False)
        fecha = Column(Date, nullable=False)
        producto_id = Column(ForeignKey('productos.id'), nullable=False)
        status = Column(Enum('y', 'n'), nullable=False)

        cliente = relationship('Clientes', back_populates='pedidos')
        producto = relationship('Productos', back_populates='pedidos')


Este es el código fuente de modelos ``SQLAlchemy`` generado en base a la base
de datos ``sistema.db``. Mas adelante se mejorara esta código para obtener una
mejor representación de los objetos.


MySQL
^^^^^

Para configurar el ``engine`` con ``MySQL`` debe definir la :ref:`cadena de conexión <python_mysql_conn_strs>`
que esta compuesto por varios parámetros, los cuales deben ser reemplazadas con sus propios datos
en la linea de comando con el comando ``sqlacodegen``.

.. tip::
    Para conectarte al servidor ``MySQL`` necesite el paquete :ref:`PyMySQL <python_mysql_instalar>`.

Luego ya teniendo instalado el paquete ``PyMySQL`` debe ejecutar el siguiente comando
de ``sqlacodegen``, los parámetros deben ser reemplazadas con sus propios datos en la
linea de comando:

.. code-block:: console

    $ sqlacodegen --generator declarative mysql+pymysql://USER:PASSW@HOST:PORT/DB \
        --outfile file.py

A continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ sqlacodegen --generator declarative mysql+pymysql://root:root@localhost:3306/sistema \
            --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          > .\sqlacodegen.exe --generator declarative mysql+pymysql://root:root@localhost:3306/sistema --outfile models.py


PostgreSQL
^^^^^^^^^^

Para configurar el ``engine`` con ``PostgreSQL`` debe definir la :ref:`cadena de conexión <python_psycopg2_conn_strs>`
que esta compuesto por varios parámetros, los cuales deben ser reemplazadas con sus propios datos
en la linea de comando con el comando ``sqlacodegen``.

.. tip::
    Para conectarte al servidor ``PostgreSQL`` necesite el paquete :ref:`psycopg2 <python_psycopg2_instalar>`.

Luego ya teniendo instalado el paquete ``psycopg2`` debe ejecutar el siguiente comando
de ``sqlacodegen``, los parámetros deben ser reemplazadas con sus propios datos en la
linea de comando:

.. code-block:: console

    $ sqlacodegen --generator declarative postgresql://USER:PASSW@HOST:PORT/DB \
        --outfile file.py

A continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ sqlacodegen --generator declarative postgresql://root:root@localhost:3306/sistema \
            --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          > .\sqlacodegen.exe --generator declarative postgresql://root:root@localhost:3306/sistema --outfile models.py


Si necesita más tipos de cadenas de conexión o :ref:`engine <python_sqlalchemy_engine>`, puede
consultar el apartado `Engine Configuration`_ de la documentación oficial de ``SQLAlchemy``.


.. _python_sqlacodegen_scaffolding:

Estructura de proyecto
----------------------

A continuación la estructura de proyecto ``sistema``

.. code-block:: console

    sistema/
    ├── .env.example
    ├── db.py
    ├── __init__.py
    ├── main.py
    ├── models.py
    ├── requirements.txt
    └── sistema.db

*Archivo .env.example*

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/.env.example
    :language: text
    :linenos:
    :lines: 1-9

*Archivo requirements.txt*

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/requirements.txt
    :language: python
    :linenos:
    :lines: 1-6

*Archivo db.py*

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/db.py
    :language: python
    :linenos:
    :lines: 1-54

*Archivo models.py*

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/models.py
    :language: python
    :linenos:
    :lines: 1-147

*Archivo main.py*

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-31


Teniendo creada la anterior estructura de proyecto, vuelva a ejecutar ahora el modulo con
el siguiente comando, el cual a continuación se presentan el correspondiente comando de tu
sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install -r requirements.txt
          $ cp .env.example .env
          $ python main.py

      .. tip::
        El archivo ``.env`` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      .. note::
        Para conexiones a base de datos ``MySQL`` y ``PostgreSQL`` debe definir las variables
        que por defecto no están definidas.

   .. group-tab:: Windows

      .. code-block:: console

          > pip install -r requirements.txt
          > copy .env.example .env
          > python main.py

      .. tip::
        El archivo ``.env`` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      .. note::
        Para conexiones a base de datos ``MySQL`` y ``PostgreSQL`` debe definir las variables
        que por defecto no están definidas.

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    ¡Consulta todos los estados!

    ¡Consulta todas las ciudades!


Asi de esta forma puede usar ``sqlacodegen`` para generar modelos ``SQLAlchemy`` desde una base de datos
existente e implementar las operaciones ingresar, consultar, actualizar y eliminar registro en las tablas.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion12>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`sqlacodegen`: https://pypi.org/project/sqlacodegen/
.. _`sqlautocode`: http://code.google.com/p/sqlautocode/
.. _`Engine Configuration`: https://docs.sqlalchemy.org/en/14/core/engines.html
