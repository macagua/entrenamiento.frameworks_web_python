.. _python_sqlalchemy:

SQLAlchemy
==========

Muchas aplicaciones manipulan información que persiste en una base de datos.
En Python existen múltiples conectores para acceder y trabajar con una base
de datos, puedes usar directamente conectores que implementan la interfaz de
comunicación con las bases de datos relacionales más conocidas, como
:ref:`PostgreSQL <python_pkg_postgresql>`, :ref:`MySQL <python_pkg_mysql>`,
`cx_Oracle`_, bases de datos *NoSQL* como `MongoDB`_, etc. O en su lugar, puedes
usar `SQLAlchemy`_.

.. figure:: ../_static/images/sqlalchemy_logo.png
    :align: center
    :width: 60%

    Logotipo de SQLAlchemy


La librería ``SQLAlchemy`` es el kit de herramientas SQL de Python y el
mapeador relacional de objetos.


``SQLAlchemy`` es el kit de herramientas SQL de Python y el Mapeador
relacional de objetos que ofrece a los desarrolladores de aplicaciones
la máxima potencia y flexibilidad de SQL. Esta proporciona un conjunto
completo de patrones de persistencia conocidos a nivel empresarial,
diseñados para un acceso a bases de datos eficiente y de alto
rendimiento, adaptados a un lenguaje de dominio simple y Pythonic.


Características
---------------

Las principales características de ``SQLAlchemy`` incluyen:

- Un ORM de potencia industrial, construido desde el núcleo en el
  mapa de identidad, la unidad de trabajo y los patrones del mapeador
  de datos. Estos patrones permiten la persistencia transparente de
  objetos utilizando un sistema de configuración declarativo. Los
  modelos de dominio se pueden construir y manipular de forma natural,
  y los cambios se sincronizan con la transacción actual automáticamente.

- Un sistema de consulta orientado a la relación, que expone explícitamente
  toda la gama de capacidades de SQL, incluidas combinaciones, subconsultas,
  correlaciones y casi todo lo demás, en términos del modelo de objetos.
  Las consultas de escritura con el ORM utilizan las mismas técnicas de
  composición relacional que utiliza al escribir SQL. Si bien puede caer
  en SQL literal en cualquier momento, virtualmente nunca es necesario.

- Un sistema completo y flexible de carga impaciente para colecciones
  y objetos relacionados. Las colecciones se almacenan en caché dentro
  de una sesión y se pueden cargar en un acceso individual, todo de una
  vez mediante uniones, o por consulta por colección en todo el conjunto
  de resultados.

- Un sistema de construcción Core SQL y una capa de interacción :ref:`DBAPI <python_dbapi>`.
  ``SQLAlchemy`` Core es independiente del ORM y es una capa de abstracción
  de base de datos completa por derecho propio, e incluye un lenguaje de
  expresión SQL basado en Python extensible, metadatos de esquema,
  agrupación de conexiones, coacción de tipos y tipos personalizados.

- Se supone que todas las restricciones de clave primaria y externa son
  compuestas y naturales. Por supuesto, las claves primarias de enteros
  sustitutos siguen siendo la norma, pero ``SQLAlchemy`` nunca asume ni
  codifica los códigos de este modelo.

- Base de datos de introspección y generación. Los esquemas de la base
  de datos se pueden "reflejar" en un solo paso en las estructuras de
  Python que representan los metadatos de la base de datos; esas mismas
  estructuras pueden generar declaraciones ``CREATE`` de inmediato, todas
  dentro del Core, independientemente del ORM.

.. _python_sqlalchemy_funcionamiento:

¿Cómo funciona?
---------------

``SQLAlchemy`` proporciona una interfaz única para comunicarte con los diferentes
drivers de bases de datos Python que implementan el estándar *Python*
:ref:`DBAPI <python_dbapi>`.

Este estándar, especifica cómo las librerías Python que se integran con las
bases de datos deben exponer sus interfaces. Por tanto, al usar ``SQLAlchemy``
no interactuarás directamente con dicho API, sino con la interfaz que precisamente
proporciona ``SQLAlchemy``. Esto es lo que permite cambiar el motor de base de datos
de una aplicación sin modificar apenas el código que interactúa con los datos.

En definitiva, al usar ``SQLAlchemy`` es necesario instalar también un driver que
implemente la interfaz :ref:`DBAPI <python_dbapi>` para la base de datos que vayas a utilizar.

Ejemplos de estos drivers son:

-  :ref:`psycopg <python_pkg_postgresql>` para conexiones a *PostgreSQL*.

-  :ref:`PyMySQL <python_pkg_mysql>` para conexiones a *MySQL*.

-  `cx_Oracle`_ para conexiones a *Oracle*.


.. _python_sqlalchemy_instalar:

Instalación
-----------

Para instalar la librería ``SQLAlchemy`` debe ejecutar el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          pip3 install SQLAlchemy

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install SQLAlchemy


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import sqlalchemy ; print(sqlalchemy.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import sqlalchemy ; print(sqlalchemy.__version__)"


Si muestra el número de la versión instalada de ``SQLAlchemy``, tiene correctamente instalada
la librería. Con esto, ya tiene todo listo para continuar.


----


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``SQLAlchemy`` debe ejecutar los siguientes comandos:

Crear el directorio ``~/proyectos/sqlalchemy/sistema`` con el siguiente comando:

.. code-block:: console

    mkdir -p ~/proyectos/sqlalchemy/sistema && cd $_


El comando anterior crea la siguiente estructura de directorios:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── sqlalchemy/
        └── sistema/

Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.


----

.. _python_sqlalchemy_engine:

Crear el Engine
---------------

Lo primero que hay que hacer para trabajar con SQLAlchemy es crear un ``engine``.
El ``engine`` es el punto de entrada a la base de datos, es decir, el que permite
a ``SQLAlchemy`` comunicarse con esta.

El motor se usa principalmente para manejar dos elementos: los pools de conexiones
y el dialecto a utilizar.

Vamos a crear un ``engine``. Para ello, añade un nuevo módulo Python llamado
:file:`settings.py` al directorio ``sistema`` con el siguiente contenido:

.. code-block:: python
    :linenos:

    import os
    from sqlalchemy import create_engine

    DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
    DB_FILE = "sistema.db"

    # Configurar conexiones entre SQLAlchemy y SQLite3 DB API
    engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")

Como puedes observar, a la función ``create_engine()`` se le pasa la cadena
de conexión a la base de datos. En este caso, la cadena de conexión a la base de
datos SQLite es ``"sqlite:///{DB_PATH}{DB_FILE}"``.

Crear el ``engine`` no hace que la aplicación se conecte a la base de datos
inmediatamente, este hecho se pospone para cuando es necesario.

.. _python_sqlalchemy_pool_conexiones:

Pool de conexiones
------------------

``SQLAlchemy`` utiliza el patrón *Pool de objetos* para manejar las conexiones a la
base de datos.

Esto quiere decir que cuando se usa una conexión a la base de datos, esta ya está creada
previamente y es reutilizada por el programa. La principal ventaja de este patrón es que
mejora el rendimiento de la aplicación, dado que abrir y gestionar una conexión de base
de datos es una operación costosa y que consume muchos recursos.

Al crear un ``engine`` con la función ``create_engine()``, se genera un pool ``QueuePool``
que viene configurado como un *pool* de 5 conexiones como máximo. Esto se puede modificar
en la configuración de ``SQLAlchemy``.

.. _python_sqlalchemy_dialectos_base_datos:

Dialectos de base de datos
--------------------------

A pesar de que el lenguaje SQL es universal, cada motor de base de datos
introduce ciertas variaciones propietarias sobre dicho lenguaje. A esto se le
conoce como dialecto.

Una de las ventajas de usar ``SQLAlchemy`` es que, en principio, no te tienes que
preocupar del dialecto a utilizar. El ``engine`` configura el dialecto por ti y
se encarga de hacer las traducciones necesarias a código SQL. Esta es una de
las razones por las que puedes cambiar el motor de base de datos realizando muy
pocos cambios en tu código.

.. _python_sqlalchemy_sesiones:

Sesiones
--------

Una vez creado el ``engine``, lo siguiente que debes hacer para trabajar con
``SQLAlchemy`` es crear una sesión. Una sesión viene a ser como una transacción,
es decir, un conjunto de operaciones de base de datos que, bien se ejecutan todas
de forma atómica, bien no se ejecuta ninguna (si ocurre un fallo en alguna de las
operaciones).

Desde el punto de vista de ``SQLAlchemy``, una sesión registra una lista de objetos
creados, modificados o eliminados dentro de una misma transacción, de manera que,
cuando se confirma la transacción, se reflejan en base de datos todas la
operaciones involucradas (o ninguna si ocurre cualquier error).

Va a crear una sesión en el proyecto. Abre el archivo :file:`settings.py` y añade lo siguiente:

.. code-block:: python
    :linenos:

    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
    DB_FILE = "sistema.db"

    engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")

    Session = sessionmaker(bind=engine)
    session = Session()

Para crear una sesión se utiliza el método factoría ``sessionmaker()`` asociado a un
``engine``. Después de crear la factoría, objeto ``Session``, hay que hacer llamadas
a la misma para obtener las sesiones, objeto ``session``.


.. _python_sqlalchemy_modelos:

Crear los modelos
-----------------

En este punto, ya tiene casi todo listo para interactuar con el ORM.
Ahora le voy a conocer donde realmente ocurre la *magia*: los `modelos`_.

Los modelos son las clases que representan las tablas de base de datos. En el ejemplo
tenemos la tabla ``productos``, por tanto, dado que esta usando un ORM, tiene
que crear el modelo (o clase) equivalente a la misma.

Para que se pueda realizar el mapeo de forma automática de una clase a una tabla,
y viceversa, vamos a utilizar una clase base en los modelos que implementa toda
esta lógica.

De nuevo, abre el archivo :file:`settings.py` y modificarlo para que su contenido sea como
el que te muestro a continuación:

.. code-block:: python
    :linenos:

    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
    DB_FILE = "sistema.db"

    # Configurar conexiones entre SQLAlchemy y SQLite3 DB API
    engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")
    # Crear sesión con el engine de base de datos
    Session = sessionmaker(bind=engine)
    session = Session()
    # Crear base declarativa
    Base = declarative_base()

Al final del mismo hemos creado una clase llamada ``Base`` con el método
``declarative_base()``. Esta clase será de la que hereden todos los modelos y tiene
la capacidad de realizar el mapeo correspondiente a partir de la
meta información (atributos de clase, nombre de la clase, etc.) que encuentre,
precisamente, en cada uno de los modelos.

A continuación, le presento como debe quedar el archivo :file:`settings.py`:

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/settings.py
    :language: python
    :linenos:
    :lines: 1-24

Por tanto, lo siguiente que debe hacer es crear el modelo ``Productos``. Crea un
nuevo archivo en el directorio ``productos`` llamado :file:`models.py` y
añade el código que te muestro a continuación:

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/models.py
    :language: python
    :linenos:
    :lines: 1-34

Así de esta forma tiene definido una clase modelo llamado ``Productos`` la cual mapea
la tabla ``productos``.

.. _python_sqlalchemy_mapeo_clase_tabla:

Mapeo entre la clase y la tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La clase ``Productos`` del código anterior representa la tabla ``productos``.

Para que se pueda realizar el mapeo automático *clase-tabla*, la clase hereda
de la clase ``Base`` que creo en la sección anterior y que se encuentra en el
módulo :file:`settings.py`. Además, hay que especificar el nombre de la tabla a través
del atributo de clase ``__tablename__``.

Por otro lado, cada una de las columnas de la tabla tienen su correspondiente
representación en la clase a través de atributos de tipo ``Column``. En este
caso concreto, los atributos son los siguientes: ``id``, ``nombre``, ``categoria``
y ``precio``.

Como puedes observar, ``SQLAlchemy`` define distintos tipos de datos para las
columnas (``Integer``, ``String`` o ``Float``, entre otros). En función del
dialecto seleccionado, estos tipos se mapearán al tipo correcto de la base de
datos utilizada.

Por último, y no menos importante, es necesario que al menos un atributo de la
clase se especifique como ``primary_key``. En el ejemplo es el atributo ``id``.
Este será el atributo que representa a la *clave primaria* de la tabla.

.. note::
  En la mayoría de motores de bases de datos, al especificar una columna de tipo
  ``Integer`` como ``primary_key``, se generará una columna de tipo entero con
  valores que se incrementan de manera automática. Además, al crear un objeto no
  es necesario indicar el valor de esta columna ya que lo establecerá la base de
  datos cuando se confirmen los cambios.


.. _python_sqlalchemy_create:

Crear tablas
------------

Una vez definidos los modelos, hay que crear las tablas correspondientes.

Crea un nuevo archivo Python en el directorio ``productos`` llamado
:file:`main.py`. En este archivo será donde escribas el código de ejemplo del
programa.

Añade el siguiente código fuente al archivo :file:`main.py`:

.. code-block:: python
    :linenos:

    from db import *
    from models import Productos

    if __name__ == "__main__":
        Base.metadata.create_all(engine)
        print("¡Creación exitosa de la tabla productos!\n")

Lo importante en este punto es la línea ``Base.metadata.create_all(engine)``.
En ella estamos indicando a ``SQLAlchemy`` que cree, si no existen, las tablas de todos
los modelos que encuentre en la aplicación. Sin embargo, para que esto ocurra es necesario
que cualquier modelo se haya importado previamente antes de llamar a la función ``create_all()``.

.. important::
    Si un modelo no ha sido importado en el código antes de llamar a la función ``create_all()``,
    no se tendrá en cuenta para crear su tabla correspondiente.

Ejecuta ahora el programa con el siguiente comando:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ¡Creación exitosa de la tabla productos!

   .. group-tab:: Windows

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ¡Creación exitosa de la tabla productos!


Se ha creado la tabla ``productos`` en la base de datos ``sistema.db``. Verás que aparece un
archivo con dicho nombre en el directorio ``productos``.


.. _python_sqlalchemy_insertar_modelo:

Insertar registros
------------------

Va a crear varias filas en la tabla ``productos``. Como te he indicado anteriormente,
una fila de una tabla se corresponde con un objeto Python. Por tanto, para crear una
fila debemos instanciar un objeto de la clase ``Productos``, añadirlo a la sesión y
finalmente aplicar los cambios.

Añade un método ``ingresar_data()`` del archivo :file:`main.py` con el siguiente código:

.. code-block:: python
    :linenos:

    from db import *
    from models import Productos


    def ingresar_data():
        arroz = Productos(nombre="Arroz", categoria="Granos", precio=1.25)
        session.add(arroz)
        print(arroz.id)
        agua = Productos(nombre="Agua", categoria="Líquidos", precio=0.3)
        mantequilla = Productos("Mantequilla", "Lácteos", 3.56)
        queso = Productos("Queso", "Lácteos", 8.56)
        session.add_all([agua, mantequilla, queso])
        session.commit()
        print(arroz.id)
        print("¡Inserción exitosa de los 4 productos!\n")


    if __name__ == "__main__":
        Base.metadata.create_all(engine)
        print("¡Creación exitosa de la tabla productos!\n")
        ingresar_data()

Te explico paso a paso el código y lo que ocurre. Inicialmente se crea el objeto ``arroz``
de tipo ``Productos``. Seguidamente, se añade a la sesión con ``session.add(arroz)``.
Después se muestra el valor del atributo ``id`` que es ``None``, puesto que todavía no se han
confirmado los cambios en la base de datos. A continuación, se crea y se añade a la sesión los
objetos ``agua``, ``mantequilla`` y ``queso`` usando ``session.add_all([agua, mantequilla, queso])``.
Por último, se hace un ``commit()`` de la sesión actual para confirmar los cambios en la base
de datos y se muestra, de nuevo, el valor del atributo ``id`` del objeto ``arroz``. En esta ocasión
puedes observar que su valor es ``1`` y que coincide con el valor de la columna ``id``
de la primera fila de la tabla ``productos``.

Ejecuta ahora el programa con el siguiente comando:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ¡Creación exitosa de la tabla productos!

          ¡Inserción exitosa de los 4 productos!

   .. group-tab:: Windows

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ¡Creación exitosa de la tabla productos!

          ¡Inserción exitosa de los 4 productos!


.. _python_sqlalchemy_consultas:

Consultar registros
-------------------

Las consultas devuelven modelos

Una vez que te he mostrado cómo guardar datos en la base de datos usando el ORM de
``SQLAlchemy``, en esta última parte del tutorial vas a descubrir cómo hacer los principales
tipos de consultas.

Las consultas a la base de datos se realizan fundamentalmente a través de la función
``query`` del objeto ``session``. Esta función recibe como parámetro el nombre de la clase
sobre la que realizar las consultas y devuelve un objeto ``Query`` con la consulta a realizar.

Siguiendo con el ejemplo, para realizar consultas sobre la clase ``Productos`` deberíamos
ejecutar el siguiente código:

.. code-block:: python

    productos = session.query(Productos)

La variable ``productos`` es de tipo ``Query`` pero todavía no se ha ejecutado sobre la base
de datos, para ello, debemos indicarle qué operación queremos realizar. Las más comunes son
las siguientes:


.. _python_sqlalchemy_obtener_objeto_por_id:

Obtener un objeto a partir de su id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    producto = session.query(Productos).get(1)

El método ``get()`` devuelve un objeto del tipo indicado en la ``Query`` a partir de su
``primary_key``. Si no encuentra el objeto, devuelve ``None``.


.. _python_sqlalchemy_consulta_todos:

Obtener los objetos de una consulta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para obtener todos los objetos de un tabla o consulta, simplemente hay que llamar al
método ``all()``. Este método devuelve una lista con los objetos devueltos por la
consulta:

.. code-block:: python

    productos = session.query(Productos).all()

También puedes llamar al método ``first()``. El método ``first()`` devuelve el primer objeto encontrado
por la consulta. Es útil si sabes que solo existe un elemento que cumpla una determinada condición.


.. _python_sqlalchemy_consulta_contar_filas:

Contar el número de elementos devueltos por una consulta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si quieres contar el número de elementos que devuelve una consulta, utiliza el método ``count()``:

.. code-block:: python

    contar_productos = session.query(Productos).count()


.. _python_sqlalchemy_consulta_aplicar_filtros:

Aplicar filtros a una consulta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para aplicar un filtro a una consulta, lo que sería la cláusula *WHERE* de *SQL*,
puedes llamar al método ``filter_by(keyword)``:

.. code-block:: python

    agua = session.query(Productos).filter_by(nombre="Agua").first()

Para aplicar un filtro a una consulta, lo que sería la cláusula *WHERE* de *SQL*,
puedes llamar al método ``filter()``:

.. code-block:: python

    menos_de_1 = session.query(Productos).filter(Productos.precio < 1).all()


.. _python_sqlalchemy_actualizar:

Actualizar registros
--------------------

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. code-block:: python
    :linenos:

    session.query(Productos).filter(Productos.id == 1).update({Productos.precio: 11.50})
    session.commit()

El método ``update()`` le permite actualizar la fila del registro, tratando las columnas como un
tipo :ref:`diccionario <python_dict>`.


.. _python_sqlalchemy_eliminar:

Eliminar registros
------------------

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. code-block:: python
    :linenos:

    session.query(Productos).filter(Productos.id == 1).delete()
    session.commit()

El método ``delete()`` le permite eliminar el registro en base a la clave primaria del campo ``id``.


.. _python_sqlalchemy_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``SQLAlchemy``, a continuación la estructura de proyecto llamado ``sistema``:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── sqlalchemy/
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

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/.env.example
    :language: text
    :linenos:
    :lines: 1-2

*Archivo* :file:`settings.py`

Módulo de configuraciones del programa.

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/settings.py
    :language: python
    :linenos:
    :lines: 1-24

*Archivo* :file:`models.py`

Módulo de :ref:`modelos <python_sqlalchemy_modelos>` de :ref:`SQLAlchemy <python_sqlalchemy>`.

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/models.py
    :language: python
    :linenos:
    :lines: 1-34

*Archivo* :file:`main.py`

Módulo principal del programa.

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-185

*Archivo* :file:`requirements.txt`

Archivo de `requirements.txt`_ de la herramienta de gestión de paquetes `pip`_.

.. literalinclude:: ../../recursos/leccion2/sqlalchemy/sistema/requirements.txt
    :language: python
    :linenos:
    :lines: 1-3


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

          INFO:root:✅ ¡Creación exitosa de la tabla 'productos' en la base de datos 'sistema.db'!

          INFO:root:✅ ¡Inserción exitosa de los '4' productos!

          ✅ ¡Consulta todos los productos!
          📜 Producto: Arroz (Granos) - $1.25
          📜 Producto: Agua (Líquidos) - $0.30
          📜 Producto: Mantequilla (Lácteos) - $3.56
          📜 Producto: Queso (Lácteos) - $8.56
          INFO:root:✅ ¡Consulta exitosa de '4' productos!

          ✅ ¡Consulta el 'nombre' y 'precio' de todos los productos!
          📜 Arroz 1.25
          📜 Agua 0.3
          📜 Mantequilla 3.56
          📜 Queso 8.56
          INFO:root:✅ ¡Consulta exitosa del 'nombre' y 'precio' de todos los productos!

          ✅ ¡Consulta de producto en base a su clave primaria!
          📜 Producto: Arroz (Granos) - $1.25
          INFO:root:✅ ¡Consulta exitosa del producto 'Arroz'!

          ✅ ¡Consulta de productos 'lacteos' con precio mayor a '3.0'!
          📜 Producto: Mantequilla (Lácteos) - $3.56
          📜 Producto: Queso (Lácteos) - $8.56
          INFO:root:✅ ¡Consulta exitosa de los productos 'lacteos' con precio mayor a '3.0'!

          ✅ ¡Otra consulta de productos 'lácteos'!
          📜 3, Mantequilla, Lácteos
          📜 4, Queso, Lácteos
          INFO:root:✅ ¡Consulta exitosa de todos los productos 'lacteos'!

          ✅ ¡Consulta del primer producto!
          📜 Producto: Mantequilla (Lácteos) - $3.56

          ✅ ¡Consulta del único producto!
          📜 Producto: Agua (Líquidos) - $0.30
          INFO:root:✅ ¡Consulta exitosa del único producto!

          ✅ ¡Consulta los productos cuyos nombres coincidan con los suministrados!
          📜 Producto: Arroz (Granos) - $1.25
          📜 Producto: Agua (Líquidos) - $0.30
          INFO:root:✅ ¡Consulta exitosa de producto(s) cuyo(s) nombres coincidan con 'Agua' y 'Arroz'!

          ✅ ¡Actualiza el producto suministrado!
          📜 Precio anterior: Producto: Arroz (Granos) - $1.25 1.25
          📜 Precio nuevo: Producto: Arroz (Granos) - $11.50 11.5
          INFO:root:✅ ¡Actualización exitosa de precio del producto 'Arroz'!

          INFO:root:✅ ¡Actualización exitosa del producto 'Agua' con el precio '3.33'!

          INFO:root:✅ ¡Eliminación exitosa del producto 'Arroz'!

          INFO:root:✅ ¡La conexión SQLite a la base de datos 'sistema.db' fue cerrada!

      La ejecución anterior generar la siguiente estructura:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── sqlalchemy/
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

          INFO:root:✅ ¡Creación exitosa de la tabla 'productos' en la base de datos 'sistema.db'!

          INFO:root:✅ ¡Inserción exitosa de los '4' productos!

          ✅ ¡Consulta todos los productos!
          📜 Producto: Arroz (Granos) - $1.25
          📜 Producto: Agua (Líquidos) - $0.30
          📜 Producto: Mantequilla (Lácteos) - $3.56
          📜 Producto: Queso (Lácteos) - $8.56
          INFO:root:✅ ¡Consulta exitosa de '4' productos!

          ✅ ¡Consulta el 'nombre' y 'precio' de todos los productos!
          📜 Arroz 1.25
          📜 Agua 0.3
          📜 Mantequilla 3.56
          📜 Queso 8.56
          INFO:root:✅ ¡Consulta exitosa del 'nombre' y 'precio' de todos los productos!

          ✅ ¡Consulta de producto en base a su clave primaria!
          📜 Producto: Arroz (Granos) - $1.25
          INFO:root:✅ ¡Consulta exitosa del producto 'Arroz'!

          ✅ ¡Consulta de productos 'lacteos' con precio mayor a '3.0'!
          📜 Producto: Mantequilla (Lácteos) - $3.56
          📜 Producto: Queso (Lácteos) - $8.56
          INFO:root:✅ ¡Consulta exitosa de los productos 'lacteos' con precio mayor a '3.0'!

          ✅ ¡Otra consulta de productos 'lácteos'!
          📜 3, Mantequilla, Lácteos
          📜 4, Queso, Lácteos
          INFO:root:✅ ¡Consulta exitosa de todos los productos 'lacteos'!

          ✅ ¡Consulta del primer producto!
          📜 Producto: Mantequilla (Lácteos) - $3.56

          ✅ ¡Consulta del único producto!
          📜 Producto: Agua (Líquidos) - $0.30
          INFO:root:✅ ¡Consulta exitosa del único producto!

          ✅ ¡Consulta los productos cuyos nombres coincidan con los suministrados!
          📜 Producto: Arroz (Granos) - $1.25
          📜 Producto: Agua (Líquidos) - $0.30
          INFO:root:✅ ¡Consulta exitosa de producto(s) cuyo(s) nombres coincidan con 'Agua' y 'Arroz'!

          ✅ ¡Actualiza el producto suministrado!
          📜 Precio anterior: Producto: Arroz (Granos) - $1.25 1.25
          📜 Precio nuevo: Producto: Arroz (Granos) - $11.50 11.5
          INFO:root:✅ ¡Actualización exitosa de precio del producto 'Arroz'!

          INFO:root:✅ ¡Actualización exitosa del producto 'Agua' con el precio '3.33'!

          INFO:root:✅ ¡Eliminación exitosa del producto 'Arroz'!

          INFO:root:✅ ¡La conexión SQLite a la base de datos 'sistema.db' fue cerrada!

      La ejecución anterior generar la siguiente estructura:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── sqlalchemy/
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


Así de esta forma puede ingresar, consultar, actualizar y eliminar registro en una
tabla usando ``SQLAlchemy``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`SQLAlchemy`: https://pypi.org/project/SQLAlchemy/
.. _`MongoDB`: https://www.mongodb.com/
.. _`cx_Oracle`: https://cx-oracle.readthedocs.io/en/latest/
.. _`modelos`: https://docs.sqlalchemy.org/en/14/core/schema.html
.. _`dotenv`: https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn
.. _`python-dotenv`: https://pypi.org/project/python-dotenv/
.. _`requirements.txt`: https://pip.pypa.io/en/stable/reference/requirements-file-format/
.. _`pip`: https://pip.pypa.io/en/stable/
