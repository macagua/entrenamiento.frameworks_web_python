.. _python_pkg_postgresql:

PostgreSQL
==========

.. note::
    **Propósito:** Es un Adaptador Python de base de datos `PostgreSQL`_.

.. figure:: ../_static/images/postgresql_logo.png
    :align: center
    :width: 60%

    Logotipo de PostgreSQL

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

          $ sudo apt install -y build-essential libpq-dev python3-dev postgresql-client-common postgresql-client
          $ pip3 install psycopg2

   .. group-tab:: Windows

      .. code-block:: console

          > pip3 install psycopg2

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python3 -c "import psycopg2 ; print(psycopg2.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python3 -c "import psycopg2 ; print(psycopg2.__version__)"


Si muestra el numero de la versión instalada de ``psycopg2``, tiene correctamente instalada
la paquete. Con esto, ya tiene todo listo para continuar.

Servidor PostgreSQL
''''''''''''''''''''

Para instalar el servidor ``PostgreSQL`` existen varias formas de realizarlo, para en este caso
se realizara con la tecnología `Docker`_. Esto significa que debe instalar en tu sistema operativo:

- `Docker Engine`_.

- `Docker Desktop`_.

Luego de instalar las herramientas necesarias, debe ejecutar el siguiente comando correspondiente:

.. code-block:: console

    docker run -d --name postgres -p 5433:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=sistema -v pg_data:/var/lib/postgresql/data --restart always postgres:latest


El comando anterior crea un contenedor Docker llamado ``postgres`` con las siguientes características:

..
    .. code-block:: console

        docker exec -it postgres psql -U postgres -c "CREATE DATABASE sistema;"
        docker exec -it postgres psql -U postgres -c "DROP DATABASE sistema;"

    El comando anterior crea una base de datos llamada ``sistema`` en el servidor ``PostgreSQL``.

.. code-block:: console

    docker exec -it postgres psql -U postgres -c "SELECT datname FROM pg_database;"

El comando anterior muestra las bases de datos creadas en el servidor ``PostgreSQL``.

.. code-block:: console

    docker exec -it postgres psql -U postgres -d sistema -c "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
..
    docker exec -it postgres psql -U postgres -d sistema -c "\dt"

El comando anterior muestra las tablas creadas en la base de datos ``sistema``.

De esta forma ha instalado y ejecutado el servidor ``PostgreSQL`` necesario para las próximas script
Python a ejecutar. Con esto, ya tiene todo listo para continuar.

Estructura de archivos
''''''''''''''''''''''

Para crear la estructura de archivos del proyecto ``PostgreSQL`` debe ejecutar los siguientes comandos:

Crear el directorio ``~/proyectos/postgresql/crud`` con el siguiente comando:

.. code-block:: console

    mkdir -p ~/proyectos/postgresql/crud && cd $_


El comando anterior crea la siguiente estructura de directorios:

::

    proyectos/
    └── postgresql/
        └── crud/

Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.


----


.. _python_psycopg2_conn_strs:

Cadenas de conexión
-------------------

Para definir el método ``connect`` debe definir las cadenas de conexión con ``PostgreSQL``
como se describe a continuación:

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

    USER = "postgres"
    PASSW = "postgres"
    HOST = "localhost"
    PORT = 5432
    DB = "sistema"

    conexion_bd = psycopg2.connect(
        user=USER, password=PASSW, host=HOST, port=PORT, database=DB
    )

El ejemplo anterior se describe a continuación:

    - En la línea 1, se importa la librería ``psycopg2``.

    - En la línea 3, se define en la constante ``USER``, del usuario de conexión a la base de datos.

    - En la línea 4, se define en la constante ``PASSW``, de la contraseña del usuario de conexión a la base de datos.

    - En la línea 5, se define en la constante ``HOST``, la IP o dirección DNS de conexión al servidor de la base de datos.

    - En la línea 6, se define en la constante ``PORT``, el puerto de conexión al servidor de la base de datos.

    - En la línea 7, se define en la constante ``DB``, el nombre de la base de datos a cual conectar.

    - En la línea 8, se define en el método ``connect``, el cual establece la conexión a la base de datos.

De esta forma se crea una cadena de conexión para ``PostgreSQL`` para ser usada por el método ``connect``.


----


Insertar registros
------------------

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_insert.py
    :language: python
    :linenos:
    :lines: 1-89


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_insert.py <../../recursos/leccion2/postgresql/crud/postgresql_record_insert.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_insert.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        proyectos/
        └── postgresql/
            └── crud/
                └── postgresql_record_insert.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 postgresql_record_insert.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos 'sistema'!

    INFO:root:¡Fueron insertado(s) 3 registro(s) correctamente en la tabla!

    INFO:root:¡Fueron insertado(s) 1 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión PostgreSQL a la base de datos 'sistema' fue cerrada!

----


Consultar registros
-------------------

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_select.py
    :language: python
    :linenos:
    :lines: 1-62


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_select.py <../../recursos/leccion2/postgresql/crud/postgresql_record_select.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_select.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        proyectos/
        └── postgresql/
            └── crud/
                └── postgresql_record_select.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 postgresql_record_select.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Total de filas son: 3

    Mostrar cada fila:

            Id: 1
            Nombre: Leonardo Caballero
            Código postal: 5001
            Teléfono: +58-412-4734567

            Id: 2
            Nombre: Ana Poleo
            Código postal: 6302
            Teléfono: +58-426-5831297

            Id: 3
            Nombre: Manuel Matos
            Código postal: 4001
            Teléfono: +58-414-2360943

    INFO:root:¡La conexión PostgreSQL a la base de datos 'sistema' fue cerrada!

De esta forma puede consultar registros en una tabla dentro una base de datos ``PostgreSQL``.


----


Actualizar registros
--------------------

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_update.py
    :language: python
    :linenos:
    :lines: 1-63

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_update.py <../../recursos/leccion2/postgresql/crud/postgresql_record_update.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_update.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        proyectos/
        └── postgresql/
            └── crud/
                └── postgresql_record_update.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 postgresql_record_update.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos 'sistema'!

    INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

    INFO:root:¡La conexión PostgreSQL a la base de datos 'sistema' fue cerrada!

De esta forma puede actualizar registros en una tabla dentro una base de datos ``PostgreSQL``.


----


Eliminar registros
------------------

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/postgresql/crud/postgresql_record_delete.py
    :language: python
    :linenos:
    :lines: 1-55


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`postgresql_record_delete.py <../../recursos/leccion2/postgresql/crud/postgresql_record_delete.py>`.


.. tip::
    Para ejecutar el código :file:`postgresql_record_delete.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    ::

        proyectos/
        └── postgresql/
            └── crud/
                └── postgresql_record_delete.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 postgresql_record_delete.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conectado a la base de datos 'sistema'!

    INFO:root:¡Registro eliminado correctamente!

    INFO:root:¡La conexión PostgreSQL a la base de datos 'sistema' fue cerrada!

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en una tabla en una base de datos ``PostgreSQL``.


----


.. _python_postgresql_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``PostgreSQL``, a continuación la estructura de proyecto llamado ``PostgreSQL``:


A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo .env.example*

Archivo plantilla `dotenv`_, es un archivo de *configuración de variables de entorno*
para el proyecto. Ademas, es usado para  `establecer variables de entorno`_ con
``Docker``, `Docker Compose`_ y del paquete adicional `python-dotenv`_.

.. literalinclude:: ../../recursos/leccion2/postgresql/sistema/.env.example
    :language: text
    :linenos:
    :lines: 1-8

*Archivo requirements.txt*

Archivo de `requirements.txt`_ de la herramienta de gestión de paquetes `pip`_.

.. literalinclude:: ../../recursos/leccion2/postgresql/sistema/requirements.txt
    :language: python
    :linenos:
    :lines: 1-3

*Archivo settings.py*

Modulo de configuraciones del programa.

.. literalinclude:: ../../recursos/leccion2/postgresql/sistema/settings.py
    :language: python
    :linenos:
    :lines: 1-58

*Archivo main.py*

Modulo de principal del programa.

.. literalinclude:: ../../recursos/leccion2/postgresql/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-201

*Archivo docker-compose.yml*

Para instalar el servidor ``PostgreSQL`` existen varias formas de realizarlo, para en este caso
se realizara con la tecnología `Docker`_. Esto significa que debe instalar en tu sistema operativo:

- `Docker Compose`_.

El primer paso para configurar un entorno de desarrollo con ``Docker Compose`` es crear el archivo
de configuración ``docker-compose.yml``. Este archivo define los servicios, contenedores, redes y
volúmenes necesarios para tu aplicación.

A continuación se presenta el archivo ``docker-compose.yml`` con la configuración necesaria:

.. literalinclude:: ../../recursos/leccion2/postgresql/sistema/docker-compose.yml
    :language: yaml
    :linenos:
    :lines: 1-24


----


Teniendo creada la anterior estructura de proyecto, vuelva a ejecutar ahora el módulo con
el siguiente comando, el cual a continuación se presentan el correspondiente comando de tu
sistema operativo:

.. tabs::

   .. group-tab:: Linux

      Antes de ejecutar debes instalar sus dependencias, con el siguiente comando:

      .. code-block:: console

          $ pip3 install -r requirements.txt

      Ademas debe crear y editar el archivo ``.env``, con el siguiente comando:

      .. code-block:: console

          $ cp .env.example .env
          $ nano .env

      .. tip::
        El archivo ``.env`` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      Debe crear y editar el archivo ``docker-compose.yml``, con el siguiente comando:

      .. tip::
        Para ejecutar el comando del instalador del servidor ``PostgreSQL`` con `Docker`_ debe crear
        un archivo llamado ``docker-compose.yml`` en el directorio ``sistema/`` con el contenido
        anterior de dicho archivo, ejecutando el siguiente comando:

      .. code-block:: console

          $ nano docker-compose.yml

      .. tip::
        Si tiene creado el archivo con el contenido, entonces puede ejecutar la instalación un
        servidor ``PostgreSQL``, ejecutando el siguiente comando:

      .. code-block:: console

          $ docker-compose up -d

      De esta forma crea el contenedor Docker llamado ``postgresql``, necesario para ejecutar el script Python.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`main.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          $ python3 main.py

   .. group-tab:: Windows

      Antes de ejecutar debes instalar sus dependencias, con el siguiente comando:

      .. code-block:: console

          > pip3 install -r requirements.txt

      Ademas debe crear y editar el archivo ``.env``, con el siguiente comando:

      .. code-block:: console

          > copy .env.example .env
          > notepad.exe .env &

      .. tip::
        El archivo ``.env`` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      Debe crear y editar el archivo ``docker-compose.yml``, con el siguiente comando:

      .. tip::
        Para ejecutar el comando del instalador del servidor ``PostgreSQL`` con `Docker`_ debe crear
        un archivo llamado ``docker-compose.yml`` en el directorio ``sistema/`` con el contenido
        anterior, ejecutando el siguiente comando:

      .. code-block:: console

          > notepad.exe docker-compose.yml

      .. tip::
        Si tiene creado el archivo con el contenido, entonces puede ejecutar la instalación un
        servidor ``PostgreSQL``, ejecutando el siguiente comando:

      .. code-block:: console

          > docker-compose up -d

      De esta forma crea el contenedor Docker llamado ``postgresql``, necesario para ejecutar el script Python.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`main.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          > python3 main.py


El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    INFO:root:¡Conexión a la base de datos 'sistema' fue exitosa!

    INFO:root:¡Fueron creado(s) -1 tabla(s) correctamente en la base de datos!

    INFO:root:¡Fueron insertado(s) 3 registro(s) correctamente en la tabla!

    INFO:root:¡Fueron insertado(s) 1 registro(s) correctamente en la tabla!

    Total de filas son: 4

    Mostrar cada fila:

            Id: 1
            Nombre: Leonardo Caballero
            Código postal: 5001
            Teléfono: +58-412-4734567

            Id: 2
            Nombre: Ana Poleo
            Código postal: 6302
            Teléfono: +58-426-5831297

            Id: 3
            Nombre: Manuel Matos
            Código postal: 4001
            Teléfono: +58-414-2360943

            Id: 4
            Nombre: Liliana Andradez
            Código postal: 4001
            Teléfono: +58-414-6782473

    INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

    INFO:root:¡Registro eliminado correctamente!


Asi de esta forma puede ingresar, consultar, actualizar y eliminar registro en una
tabla usando ``PostgreSQL``.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`docker-compose.yml <../../recursos/leccion2/postgresql/sistema/docker-compose.yml>`.

    - :download:`__init__.py <../../recursos/leccion2/postgresql/sistema/__init__.py>`.

    - :download:`.env.example <../../recursos/leccion2/postgresql/sistema/.env.example>`.

    - :download:`main.py <../../recursos/leccion2/postgresql/sistema/main.py>`.

    - :download:`requirements.txt <../../recursos/leccion2/postgresql/sistema/requirements.txt>`.

    - :download:`settings.py <../../recursos/leccion2/postgresql/sistema/settings.py>`.


.. tip::
    Para ejecutar el código del proyecto llamado ``postgresql`` abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    ::

        proyectos/
        └── postgresql/
            └── sistema/
                ├── docker-compose.yml
                ├── __init__.py
                ├── .env.example
                ├── main.py
                ├── requirements.txt
                └── settings.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 main.py


Asi de esta forma puede replicar una practica real de un proyecto para realizar operaciones
en una base de datos ``PostgreSQL``, aplicando buenas prácticas de código funcional.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`PostgreSQL`: https://www.postgresql.org/
.. _`psycopg`: https://www.psycopg.org/docs/
.. _`psycopg2`: https://pypi.org/project/psycopg2/
.. _`libpq`: https://www.postgresql.org/docs/current/libpq.html
.. _`dotenv`: https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn
.. _`establecer variables de entorno`: https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/
.. _`Docker`: https://www.docker.com/
.. _`Docker Engine`: https://docs.docker.com/engine/
.. _`Docker Desktop`: https://docs.docker.com/desktop/
.. _`Docker Compose`: https://docs.docker.com/compose/
.. _`entorno virtual`: https://plone-spanish-docs.readthedocs.io/es/latest/python/creacion_entornos_virtuales.html
.. _`python-dotenv`: https://pypi.org/project/python-dotenv/
.. _`requirements.txt`: https://pip.pypa.io/en/stable/reference/requirements-file-format/
.. _`pip`: https://pip.pypa.io/en/stable/
