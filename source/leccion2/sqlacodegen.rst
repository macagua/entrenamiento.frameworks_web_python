.. _python_sqlacodegen:

Autogenerar modelos SQLAlchemy
==============================

.. note::
    **Propósito:** Generador automático de código fuente de modelos :ref:`SQLAlchemy <python_sqlalchemy>`.


`sqlacodegen`_ es una herramienta que lee la estructura de una base de datos
existente y genera el código de modelos :ref:`SQLAlchemy <python_sqlalchemy_modelos>`
apropiado, usando el estilo declarativo si es posible.

Esta herramienta se escribió como reemplazo de `sqlautocode`_, que sufría varios
problemas (incluida, entre otras, la incompatibilidad con Python 3 y la última
versión de :ref:`SQLAlchemy <python_sqlalchemy_modelos>`).

Características
---------------

- Soporta :ref:`SQLAlchemy <python_sqlalchemy>` 0.8.x - 1.4.x.

- Produce código declarativo que casi parece escrito a mano.

- Produce código compatible con PEP 8.

- Determina con precisión las relaciones, incluidos muchos a muchos, uno a uno.

- Detecta automáticamente la herencia de tablas unidas.

- Excelente cobertura de prueba.


Instalación
-----------

Para instalar la herramienta ``sqlacodegen`` debe seguir el siguientes paso, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          pip3 install sqlacodegen
..
  pip3 install git+https://github.com/agronholm/sqlacodegen.git@3.0.0rc1#egg=sqlacodegen

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install sqlacodegen


Puede probar si la instalación se realizo correctamente, ejecutando el siguiente
comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import sqlacodegen ; print(sqlacodegen.__name__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import sqlacodegen ; print(sqlacodegen.__name__)"


Si muestra el nombre del paquete como ``sqlacodegen``, tiene correctamente instalada
la herramienta. Con esto, ya tiene todo listo para continuar.


----


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``sqlacodegen`` debe ejecutar los siguientes comandos:

Crear el directorio ``~/proyectos/sqlacodegen/sistema`` con el siguiente comando:

.. code-block:: console

    mkdir -p ~/proyectos/sqlacodegen/sistema && cd $_


El comando anterior crea la siguiente estructura de directorios:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── sqlacodegen/
        └── sistema/

Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.


----

.. _python_sqlacodegen_uso:

Conexión al Engine
------------------

Luego configura el :ref:`engine <python_sqlalchemy_engine>` (cadena de conexión)
para la DB respectiva. Para esto se explican algunas configuraciones, para :ref:`SQLite <python_modulo_sqlite3>`,
:ref:`MySQL <python_pkg_mysql>` y :ref:`PostgreSQL <python_pkg_postgresql>`
a continuación:

.. tip::
    Cada cadena de conexión necesita que se instale el módulo dependiente.

.. _python_sqlacodegen_sqlite:

SQLite
^^^^^^

Para configurar el ``engine`` con :ref:`SQLite <python_modulo_sqlite3>` debe definir
la :ref:`cadena de conexión <python_sqlite3_conn_strs>` que esta compuesto por varios
parámetros.

Los parámetros deben ser reemplazadas con sus propios datos en la línea de comando:

.. code-block:: console

    sqlacodegen --generator declarative sqlite:///{DB_PATH}/{DB_FILE} --outfile file.py

A continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          sqlacodegen --generator declarative sqlite:///db.sqlite3 --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          .\sqlacodegen.exe --generator declarative sqlite:///db.sqlite3 --outfile models.py

.. _python_sqlacodegen_mysql:

MySQL
^^^^^

Para configurar el ``engine`` con :ref:`MySQL <python_pkg_mysql>` debe definir la
:ref:`cadena de conexión <python_mysql_conn_strs>` que esta compuesto por varios parámetros,
los cuales deben ser reemplazadas con sus propios datos en la línea de comando con el comando
:command:`sqlacodegen`.

.. tip::
    Para conectarte al servidor ``MySQL`` necesite el módulo :ref:`PyMySQL <python_mysql_instalar>`.

Luego ya teniendo instalado el módulo ``PyMySQL`` debe ejecutar el siguiente comando
de ``sqlacodegen``, los parámetros deben ser reemplazadas con sus propios datos en la
línea de comando:

.. code-block:: console

    sqlacodegen --generator declarative mysql+pymysql://USER:PASSW@HOST:PORT/DB --outfile file.py

A continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          sqlacodegen --generator declarative mysql+pymysql://root:root@localhost:3306/sistema \
            --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          .\sqlacodegen.exe --generator declarative mysql+pymysql://root:root@localhost:3306/sistema --outfile models.py

.. _python_sqlacodegen_psycopg2:

PostgreSQL
^^^^^^^^^^

Para configurar el ``engine`` con :ref:`PostgreSQL <python_pkg_postgresql>` debe definir la
:ref:`cadena de conexión <python_psycopg2_conn_strs>` que esta compuesto por varios parámetros,
los cuales deben ser reemplazadas con sus propios datos en la línea de comando con el comando
:command:`sqlacodegen`.

.. tip::
    Para conectarte al servidor ``PostgreSQL`` necesite el módulo :ref:`psycopg2 <python_psycopg2_instalar>`.

Luego ya teniendo instalado el módulo ``psycopg2`` debe ejecutar el siguiente comando
de ``sqlacodegen``, los parámetros deben ser reemplazadas con sus propios datos en la
línea de comando:

.. code-block:: console

    sqlacodegen --generator declarative postgresql://USER:PASSW@HOST:PORT/DB --outfile file.py

A continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          sqlacodegen --generator declarative postgresql://root:root@localhost:3306/sistema \
            --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          .\sqlacodegen.exe --generator declarative postgresql://root:root@localhost:3306/sistema --outfile models.py


Si necesita más tipos de cadenas de conexión o :ref:`engine <python_sqlalchemy_engine>`, puede
consultar el apartado `Engine Configuration`_ de la documentación oficial de ``SQLAlchemy``.

.. _python_sqlacodegen_ejecutar:

Generación de modelos
---------------------

Luego de haber definido la :ref:`cadena de conexión <python_sqlacodegen_uso>` a la base
de datos, puede realizar la generación de modelos ``SQLAlchemy``, ejecutando el siguiente
comando, el cual a continuación se presentan el correspondiente comando de tu sistema
operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          sqlacodegen --generator declarative sqlite:///sistema.db --outfile models.py

   .. group-tab:: Windows

      .. code-block:: console

          .\sqlacodegen.exe --generator declarative sqlite:///sistema.db --outfile models.py

El anterior comando al ejecutar debe generar un módulo python llamado :file:`models.py`
que contiene el siguiente código:

.. code-block:: python
    :linenos:

    from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
    from sqlalchemy.orm import declarative_base, relationship

    Base = declarative_base()


    class Estados(Base):
        __tablename__ = "estados"

        id = Column(Integer, primary_key=True, unique=True)
        nombre = Column(String(25), nullable=False)
        codigo = Column(String(2), nullable=False)

        ciudades = relationship("Ciudades", back_populates="estados")


    class Productos(Base):
        __tablename__ = "productos"

        id = Column(Integer, primary_key=True, unique=True)
        nombre = Column(String(11), nullable=False)
        descripcion = Column(String(25), nullable=False)
        categoria = Column(String(25), nullable=False)
        precio = Column(Integer, nullable=False)
        status = Column(Enum("y", "n"), nullable=False)

        pedidos = relationship("Pedidos", back_populates="producto")


    class Ciudades(Base):
        __tablename__ = "ciudades"

        id = Column(Integer, primary_key=True, unique=True)
        id_estado = Column(
            ForeignKey("estados.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
        )
        nombre = Column(String(25), nullable=False)
        capital = Column(Integer, nullable=False)

        estados = relationship("Estados", back_populates="ciudades")
        clientes = relationship("Clientes", back_populates="ciudades")


    class Clientes(Base):
        __tablename__ = "clientes"

        id = Column(Integer, primary_key=True, unique=True)
        nombre = Column(String(25), nullable=False)
        apellido = Column(String(25), nullable=False)
        codigo_postal = Column(
            ForeignKey("ciudades.id", ondelete="CASCADE", onupdate="CASCADE"),
            nullable=False,
        )
        telefono = Column(String(11), nullable=False)

        ciudades = relationship("Ciudades", back_populates="clientes")
        pedidos = relationship("Pedidos", back_populates="cliente")


    class Pedidos(Base):
        __tablename__ = "pedidos"

        id = Column(Integer, primary_key=True, unique=True)
        cliente_id = Column(ForeignKey("clientes.id"), nullable=False)
        fecha = Column(Date, nullable=False)
        producto_id = Column(ForeignKey("productos.id"), nullable=False)
        status = Column(Enum("y", "n"), nullable=False)

        cliente = relationship("Clientes", back_populates="pedidos")
        producto = relationship("Productos", back_populates="pedidos")


Este es el código fuente de modelos ``SQLAlchemy`` generado en base a la base
de datos ``sistema.db``. Más adelante se mejorara esta código fuente para obtener
una mejor representación de los objetos.

.. _python_sqlacodegen_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``sqlacodegen``, a continuación la estructura de proyecto llamado ``sistema``:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── sqlacodegen/
        └── sistema/
            ├── .env.example
            ├── __init__.py
            ├── main.py
            ├── models.py
            ├── requirements.txt
            └── settings.py

A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`.env.example`

Archivo plantilla `dotenv`_ del paquete adicional `python-dotenv`_.

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/.env.example
    :language: text
    :linenos:
    :lines: 1-10

*Archivo* :file:`settings.py`

Módulo de configuraciones del programa.

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/settings.py
    :language: python
    :linenos:
    :lines: 1-55

*Archivo* :file:`models.py`

Módulo de :ref:`modelos <python_sqlalchemy_modelos>` de :ref:`SQLAlchemy <python_sqlalchemy>`.

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/models.py
    :language: python
    :linenos:
    :lines: 1-145

*Archivo* :file:`main.py`

Módulo principal del programa.

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-120

*Archivo* :file:`requirements.txt`

Archivo de `requirements.txt`_ de la herramienta de gestión de paquetes `pip`_.

.. literalinclude:: ../../recursos/leccion2/sqlacodegen/sistema/requirements.txt
    :language: python
    :linenos:
    :lines: 1-3,5


Teniendo creada la anterior estructura de proyecto, vuelva a ejecutar ahora el módulo con
el siguiente comando, el cual a continuación se presentan el correspondiente comando de tu
sistema operativo:

.. tabs::

   .. group-tab:: Linux

      Antes de ejecutar debes instalar sus dependencias, con el siguiente comando:

      .. code-block:: console

          pip3 install -r requirements.txt

      Además debe crear el archivo :file:`.env` en base a la plantilla :file:`.env.example`
      y editarlo, con el siguiente comando:

      .. code-block:: console

          cp .env.example .env && nano .env

      .. tip::
        El archivo :file:`.env` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      .. note::
        Para conexiones a base de datos :ref:`MySQL <python_mysql_conn_strs>` y :ref:`PostgreSQL <python_psycopg2_conn_strs>`
        debe definir las variables que por defecto no están definidas.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`main.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          INFO:root:✅ ¡Creación exitosa de las tablas en la base de datos 'sistema.db'!

          ✅ Lista de 10 Estados
          📜 Estado: Amazonas
          📜 Estado: Anzoátegui
          📜 Estado: Apure
          📜 Estado: Aragua
          📜 Estado: Barinas
          📜 Estado: Bolívar
          📜 Estado: Carabobo
          📜 Estado: Cojedes
          📜 Estado: Delta Amacuro
          📜 Estado: Falcón
          INFO:root:✅ ¡Consulta de los '10' estados!

          ✅ Lista de 10 Ciudades
          📜 Ciudad: Maroa, Estado: Amazonas.
          📜 Ciudad: Puerto Ayacucho, Estado: Amazonas.
          📜 Ciudad: San Fernando de Atabapo, Estado: Amazonas.
          📜 Ciudad: Anaco, Estado: Anzoátegui.
          📜 Ciudad: Aragua de Barcelona, Estado: Anzoátegui.
          📜 Ciudad: Barcelona, Estado: Anzoátegui.
          📜 Ciudad: Boca de Uchire, Estado: Anzoátegui.
          📜 Ciudad: Cantaura, Estado: Anzoátegui.
          📜 Ciudad: Clarines, Estado: Anzoátegui.
          📜 Ciudad: El Chaparro, Estado: Anzoátegui.
          INFO:root:✅ ¡Consulta de las '10' ciudades!

          ✅ Lista de Clientes
          📜 Cliente: Leonardo Caballero
          📜 Cliente: Ana Poleo
          📜 Cliente: Manuel Matos
          📜 Cliente: Liliana Andradez
          INFO:root:✅ ¡Consulta de los '4' clientes!

          ✅ Lista de Productos
          ERROR:root:❌ ¡No hay ningún 'producto' en la base de datos!

          ✅ Lista de Pedidos
          ERROR:root:❌ ¡No hay ningún 'pedido' en la base de datos!

          INFO:root:✅ ¡La conexión SQLite a la base de datos 'sistema.db' fue cerrada!

      La ejecucion anterior generar la siguiente estructura:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── sqlacodegen/
              └── sistema/
                  ├── __init__.py
                  ├── .env
                  ├── .env.example
                  ├── main.py
                  ├── models.py
                  ├── requirements.txt
                  ├── settings.py
                  └── sistema.db

      *Archivo* :file:`sistema.db`

      Archivo de base de datos de :ref:`SQLite <python_modulo_sqlite3>` llamado :file:`sistema.db`
      la cual no se incluye ya que cada vez que se inicia el programa :file:`main.py` se elimina y crea
      nuevamente, para cuidar la creación de los datos iniciales.

   .. group-tab:: Windows

      Antes de ejecutar debes instalar sus dependencias, con el siguiente comando:

      .. code-block:: console

          pip3 install -r requirements.txt

      Además debe crear el archivo :file:`.env` en base a la plantilla :file:`.env.example`
      y editarlo, con el siguiente comando:

      .. code-block:: console

          copy .env.example .env

      Editar el archivo :file:`.env`, con el siguiente comando:

      .. code-block:: console

          notepad.exe .env &

      .. tip::
        El archivo :file:`.env` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      .. note::
        Para conexiones a base de datos :ref:`MySQL <python_mysql_conn_strs>` y :ref:`PostgreSQL <python_psycopg2_conn_strs>`
        debe definir las variables que por defecto no están definidas.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`main.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          INFO:root:✅ ¡Creación exitosa de las tablas en la base de datos 'sistema.db'!

          ✅ Lista de 10 Estados
          📜 Estado: Amazonas
          📜 Estado: Anzoátegui
          📜 Estado: Apure
          📜 Estado: Aragua
          📜 Estado: Barinas
          📜 Estado: Bolívar
          📜 Estado: Carabobo
          📜 Estado: Cojedes
          📜 Estado: Delta Amacuro
          📜 Estado: Falcón
          INFO:root:✅ ¡Consulta de los '10' estados!

          ✅ Lista de 10 Ciudades
          📜 Ciudad: Maroa, Estado: Amazonas.
          📜 Ciudad: Puerto Ayacucho, Estado: Amazonas.
          📜 Ciudad: San Fernando de Atabapo, Estado: Amazonas.
          📜 Ciudad: Anaco, Estado: Anzoátegui.
          📜 Ciudad: Aragua de Barcelona, Estado: Anzoátegui.
          📜 Ciudad: Barcelona, Estado: Anzoátegui.
          📜 Ciudad: Boca de Uchire, Estado: Anzoátegui.
          📜 Ciudad: Cantaura, Estado: Anzoátegui.
          📜 Ciudad: Clarines, Estado: Anzoátegui.
          📜 Ciudad: El Chaparro, Estado: Anzoátegui.
          INFO:root:✅ ¡Consulta de las '10' ciudades!

          ✅ Lista de Clientes
          📜 Cliente: Leonardo Caballero
          📜 Cliente: Ana Poleo
          📜 Cliente: Manuel Matos
          📜 Cliente: Liliana Andradez
          INFO:root:✅ ¡Consulta de los '4' clientes!

          ✅ Lista de Productos
          ERROR:root:❌ ¡No hay ningún 'producto' en la base de datos!

          ✅ Lista de Pedidos
          ERROR:root:❌ ¡No hay ningún 'pedido' en la base de datos!

          INFO:root:✅ ¡La conexión SQLite a la base de datos 'sistema.db' fue cerrada!

      La ejecucion anterior generar la siguiente estructura:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── sqlacodegen/
              └── sistema/
                  ├── __init__.py
                  ├── .env
                  ├── .env.example
                  ├── main.py
                  ├── models.py
                  ├── requirements.txt
                  ├── settings.py
                  └── sistema.db

      *Archivo* :file:`sistema.db`

      Archivo de base de datos de :ref:`SQLite <python_modulo_sqlite3>` llamado :file:`sistema.db`
      la cual no se incluye ya que cada vez que se inicia el programa :file:`main.py` se elimina y crea
      nuevamente, para cuidar la creación de los datos iniciales.


Así de esta forma puede usar ``sqlacodegen`` para generar modelos ``SQLAlchemy`` desde
una base de datos existente e implementar las operaciones ingresar, consultar, actualizar
y eliminar registro en las tablas.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`sqlacodegen`: https://pypi.org/project/sqlacodegen/
.. _`sqlautocode`: https://code.google.com/archive/p/sqlautocode
.. _`Engine Configuration`: https://docs.sqlalchemy.org/en/14/core/engines.html
.. _`dotenv`: https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn
.. _`python-dotenv`: https://pypi.org/project/python-dotenv/
.. _`requirements.txt`: https://pip.pypa.io/en/stable/reference/requirements-file-format/
.. _`pip`: https://pip.pypa.io/en/stable/
