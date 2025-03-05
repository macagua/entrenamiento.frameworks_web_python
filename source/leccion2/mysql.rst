.. _python_pkg_mysql:

MySQL
=====

.. note::
    **Propósito:** El motor de base de datos relacionales `MySQL`_, tiene un adaptador Python e
    implementa la especificación :ref:`DB API v2.0 (PEP-249) <python_dbapi>`, el objeto de esta
    guía es para explicar y demostrar como usarlo como desarrollador.

.. figure:: ../_static/images/mysql_textlogo.png
    :align: center
    :width: 60%

    Logotipo de MySQL

`PyMySQL`_, es un paquete contiene una librería cliente MySQL puramente en Python,
basada en la especificación :ref:`PEP 249 <python_dbapi>`.

A diferencia de :ref:`SQLite <python_modulo_sqlite3>`, no hay un módulo Python SQL
predeterminado en la librería estándar de Python, que pueda usar para conectarse a una
base de datos ``MySQL``. En su lugar, deberá instalar un controlador Python SQL
para ``MySQL`` para poder interactuar con base de datos desde aplicaciones de Python.

.. tip::
    Es el adaptador de base de datos `MySQL`_ más popular para el lenguaje de programación *Python*.


.. _python_pymysql_instalar:

Instalación
-----------

Para conectarte al servidor ``MySQL`` necesita el paquete `PyMySQL`_. Esto
significa que debe instalar ``PyMySQL`` ejecutando los siguientes comandos correspondiente
a cada sistema operativo, los cuales se presentan a continuación:

.. tabs::

   .. group-tab:: Linux


      Para trabajar una aplicación con bases de datos relacionales ``PostgreSQL`` requiere
      instalar las siguientes librerías:

      #. :ref:`Entorno de desarrollo <python_entorno_desarrollo>`.

      #. :ref:`Python package installer - pip <python_entorno_desarrollo_pip>`.

      #. :ref:`Entorno virtual Python <python_entorno_desarrollo_venv>`.

      #. Paquete ``PyMySQL``, ejecutando el siguiente comando:

         .. code-block:: console

             pip3 install PyMySQL

      #. Motor de base de datos :ref:`MySQL <python_mysql_instalar>`.

   .. group-tab:: Windows

      #. :ref:`Entorno virtual Python <python_entorno_desarrollo_venv>`.

      #. Paquete ``PyMySQL``, ejecutando el siguiente comando:

         .. code-block:: console

             pip3 install PyMySQL

      #. Motor de base de datos :ref:`MySQL <python_mysql_instalar>`.

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import pymysql ; print(pymysql.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import pymysql ; print(pymysql.__version__)"


Si muestra el numero de la versión instalada de ``PyMySQL``, tiene correctamente instalada
la paquete. Con esto, ya tiene todo listo para continuar.


.. _python_mysql_instalar:

Servidor MySQL
'''''''''''''''

Para instalar el servidor ``MySQL`` existen varias formas de realizarlo, para en este caso
se realizara con la tecnología `Docker`_. Esto significa que debe instalar en tu sistema operativo:

- `Docker Engine`_.

- `Docker Desktop`_.

Luego de instalar las herramientas necesarias, debe ejecutar el siguiente comando correspondiente:

.. code-block:: console

    docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=sistema -p 3306:3306 -v my_data:/var/lib/mysql --restart always mysql:latest


El comando anterior crea un contenedor Docker llamado ``mysql`` con la version ``latest``,
ejecutándose en el puerto ``3306`` con un punto de montaje ``my_data``.


De esta forma ha instalado y ejecutado el servidor ``MySQL`` necesario para las próximas script
Python a ejecutar. Con esto, ya tiene todo listo para continuar.

Estructura de archivos
''''''''''''''''''''''

Para crear la estructura de archivos del proyecto ``MySQL`` debe ejecutar los siguientes comandos:

Crear el directorio ``~/proyectos/mysql/crud`` con el siguiente comando:

.. code-block:: console

    mkdir -p ~/proyectos/mysql/crud && cd $_


El comando anterior crea la siguiente estructura de directorios:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── mysql/
        └── crud/

Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.


----


.. _python_mysql_conn_strs:

Cadenas de conexión
-------------------

Para definir el método ``connect`` debe definir las cadenas de conexión con ``MySQL``
como se describe a continuación:

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

- En la línea 1, se importa la librería ``pymysql``.

- En la línea 3, se define en la constante ``USER``, del usuario de conexión a la base de datos.

- En la línea 4, se define en la constante ``PASSW``, de la contraseña del usuario de conexión a la base de datos.

- En la línea 5, se define en la constante ``HOST``, la IP o dirección DNS de conexión al servidor de la base de datos.

- En la línea 6, se define en la constante ``PORT``, el puerto de conexión al servidor de la base de datos.

- En la línea 7, se define en la constante ``DB``, el nombre de la base de datos a cual conectar.

- En la línea 8, se define en el método ``connect``, el cual establece la conexión a la base de datos.

De esta forma se crea una cadena de conexión para ``MySQL`` para ser usada por el método ``connect``.


----


Insertar registros
------------------

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/mysql/crud/mysql_record_insert.py
    :language: python
    :linenos:
    :lines: 1-87


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`mysql_record_insert.py <../../recursos/leccion2/mysql/crud/mysql_record_insert.py>`.


.. tip::
    Para ejecutar el código :file:`mysql_record_insert.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── mysql/
            └── crud/
                └── mysql_record_insert.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 mysql_record_insert.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console
        :class: no-copy

        INFO:root:¡Conectado a la base de datos 'sistema'!

        INFO:root:¡Fue creo una tabla correctamente en la base de datos 'sistema'!

        INFO:root:¡Fueron insertado(s) 3 registro(s) correctamente en la tabla!

        INFO:root:¡Fueron insertado(s) 1 registro(s) correctamente en la tabla!

        INFO:root:¡La conexión MySQL a la base de datos 'sistema' fue cerrada!


Puede probar si la base de datos ``sistema`` fue creada correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          docker exec -i mysql mysql -u root -proot -e "SHOW DATABASES;" mysql

   .. group-tab:: Windows

      .. code-block:: console

          docker exec -i mysql mysql -u root -proot -e "SHOW DATABASES;" mysql


Puede probar si el usuario ``root`` de la base de datos ``sistema`` fue creada correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          docker exec -i mysql mysql -u root -proot -e "SELECT user FROM mysql.user;" mysql

   .. group-tab:: Windows

      .. code-block:: console

          docker exec -i mysql mysql -u root -proot -e "SELECT user FROM mysql.user;" mysql

Puede probar si la tabla ``clientes`` en la base de datos ``sistema`` fue creada correctamente, ademas
si sus registros fueron cargados en la tabla, ejecutando el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          docker exec -i mysql mysql -u root -proot -e "USE sistema; SHOW TABLES; SELECT * FROM clientes;" mysql

   .. group-tab:: Windows

      .. code-block:: console

          docker exec -i mysql mysql -u root -proot -e "USE sistema; SHOW TABLES; SELECT * FROM clientes;" mysql


De esta forma puede ingresar registros en una tabla dentro una base de datos ``MySQL``.


----


Consultar registros
-------------------

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/mysql/crud/mysql_record_select.py
    :language: python
    :linenos:
    :lines: 1-59


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`mysql_record_select.py <../../recursos/leccion2/mysql/crud/mysql_record_select.py>`.


.. tip::
    Para ejecutar el código :file:`mysql_record_select.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── mysql/
            └── crud/
                └── mysql_record_select.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 mysql_record_select.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console
        :class: no-copy

        INFO:root:¡Conectado a la base de datos 'sistema'!

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
                Código postal: 3105
                Teléfono: +58-414-6782473

        INFO:root:¡La conexión MySQL a la base de datos 'sistema' fue cerrada!


De esta forma puede consultar registros en una tabla dentro una base de datos ``MySQL``.


----


Actualizar registros
--------------------

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/mysql/crud/mysql_record_update.py
    :language: python
    :linenos:
    :lines: 1-60


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`mysql_record_update.py <../../recursos/leccion2/mysql/crud/mysql_record_update.py>`.


.. tip::
    Para ejecutar el código :file:`mysql_record_update.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── mysql/
            └── crud/
                └── mysql_record_update.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 mysql_record_update.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console
        :class: no-copy

        INFO:root:¡Conectado a la base de datos 'sistema'!

        INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

        INFO:root:¡La conexión MySQL a la base de datos 'sistema' fue cerrada!


De esta forma puede actualizar registros en una tabla dentro una base de datos ``MySQL``.


----


Eliminar registros
------------------

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/mysql/crud/mysql_record_delete.py
    :language: python
    :linenos:
    :lines: 1-52


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`mysql_record_delete.py <../../recursos/leccion2/mysql/crud/mysql_record_delete.py>`.


.. tip::
    Para ejecutar el código :file:`mysql_record_delete.py`
    abra una consola de comando, acceda al directorio donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── mysql/
            └── crud/
                └── mysql_record_delete.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 mysql_record_delete.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console
        :class: no-copy

        INFO:root:¡Conectado a la base de datos 'sistema'!

        INFO:root:¡Registro eliminado correctamente!

        INFO:root:¡La conexión MySQL a la base de datos 'sistema' fue cerrada!


De esta forma puede eliminar registros en una tabla dentro una base de datos ``MySQL``.

.. note::
    Asi de esta forma puede realizar las operaciones de ingresar, consultar, actualizar
    y eliminar registro en una tabla en una base de datos ``MySQL`` de forma separada
    en programas Python, en la siguiente práctica se mostrara un caso real de uso de todos
    estas operaciones en un solo programa Python.


----


.. _python_mysql_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``MySQL``, a continuación la estructura de proyecto llamado ``MySQL``:


A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo .env.example*

Archivo plantilla `dotenv`_, es un archivo de *configuración de variables de entorno*
para el proyecto. Ademas, es usado para  `establecer variables de entorno`_ con
``Docker``, `Docker Compose`_ y del paquete adicional `python-dotenv`_.

.. literalinclude:: ../../recursos/leccion2/mysql/sistema/.env.example
    :language: text
    :linenos:
    :lines: 1-8

*Archivo requirements.txt*

Archivo de `requirements.txt`_ de la herramienta de gestión de paquetes `pip`_.

.. literalinclude:: ../../recursos/leccion2/mysql/sistema/requirements.txt
    :language: python
    :linenos:
    :lines: 1-4

*Archivo settings.py*

Modulo de configuraciones del programa.

.. literalinclude:: ../../recursos/leccion2/mysql/sistema/settings.py
    :language: python
    :linenos:
    :lines: 1-57

*Archivo main.py*

Modulo de principal del programa.

.. literalinclude:: ../../recursos/leccion2/mysql/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-244

*Archivo docker-compose.yml*

Para instalar el servidor ``MySQL`` existen varias formas de realizarlo, para en este caso
se realizara con la tecnología `Docker`_. Esto significa que debe instalar en tu sistema operativo:

- `Docker Compose`_.

El primer paso para configurar un entorno de desarrollo con ``Docker Compose`` es crear el archivo
de configuración ``docker-compose.yml``. Este archivo define los servicios, contenedores, redes y
volúmenes necesarios para tu aplicación.

A continuación se presenta el archivo ``docker-compose.yml`` con la configuración necesaria:

.. literalinclude:: ../../recursos/leccion2/mysql/sistema/docker-compose.yml
    :language: yaml
    :linenos:
    :lines: 1-25


----


Para ejecutar el código del proyecto llamado ``sistema`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── mysql/
        └── sistema/
            ├── docker-compose.yml
            ├── __init__.py
            ├── .env.example
            ├── main.py
            ├── requirements.txt
            └── settings.py


Si tiene la estructura de archivo previa, entonces puede continuar los procesos de instalación,
configuración y ejecución del código fuente.

.. tabs::

   .. group-tab:: Linux

      Antes de ejecutar debes instalar sus dependencias, con el siguiente comando:

      .. code-block:: console

          pip3 install -r requirements.txt

      Ademas debe crear el archivo ``.env`` en base a la plantilla ``.env.example``
      y editarlo, con el siguiente comando:

      .. code-block:: console

          cp .env.example .env && nano .env

      .. tip::
        El archivo ``.env`` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      Debe crear y editar el archivo ``docker-compose.yml``, con el siguiente comando:

      .. tip::
        Para ejecutar el comando del instalador del servidor ``MySQL`` con `Docker`_ debe crear
        un archivo llamado ``docker-compose.yml`` en el directorio ``sistema/`` con el contenido
        anterior de dicho archivo, ejecutando el siguiente comando:

      .. code-block:: console

          nano docker-compose.yml

      .. tip::
        Si tiene creado el archivo con el contenido, entonces puede ejecutar la instalación un
        servidor ``MySQL``, ejecutando el siguiente comando:

      .. code-block:: console

          docker-compose up -d

      De esta forma crea el contenedor Docker llamado ``mysql``, necesario para ejecutar el script Python.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`main.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          INFO:root:¡Conexión a la base de datos 'sistema' fue exitosa!

          INFO:root:¡Fueron creado(s) 0 tabla(s) correctamente en la base de datos!

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
                  Código postal: 3105
                  Teléfono: +58-414-6782473

          INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

          INFO:root:¡Registro eliminado correctamente!

   .. group-tab:: Windows

      Antes de ejecutar debes instalar sus dependencias, con el siguiente comando:

      .. code-block:: console

          pip3 install -r requirements.txt

      Ademas debe crear el archivo ``.env`` en base a la plantilla ``env.example`` , con
      el siguiente comando:

      .. code-block:: console

          copy .env.example .env

      Editar el archivo ``.env``, con el siguiente comando:

      .. code-block:: console

          notepad.exe .env &

      .. tip::
        El archivo ``.env`` se definen las configuraciones de conexión a la base de datos,
        puede modificarlo cambiar valores de la conexión.

      Debe crear y editar el archivo ``docker-compose.yml``, con el siguiente comando:

      .. tip::
        Para ejecutar el comando del instalador del servidor ``MySQL`` con `Docker`_ debe crear
        un archivo llamado ``docker-compose.yml`` en el directorio ``sistema/`` con el contenido
        anterior, ejecutando el siguiente comando:

      .. code-block:: console

          notepad.exe docker-compose.yml

      .. tip::
        Si tiene creado el archivo con el contenido, entonces puede ejecutar la instalación un
        servidor ``MySQL``, ejecutando el siguiente comando:

      .. code-block:: console

          docker-compose up -d

      De esta forma crea el contenedor Docker llamado ``mysql``, necesario para ejecutar el script Python.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`main.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 main.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          INFO:root:¡Conexión a la base de datos 'sistema' fue exitosa!

          INFO:root:¡Fueron creado(s) 0 tabla(s) correctamente en la base de datos!

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
                  Código postal: 3105
                  Teléfono: +58-414-6782473

          INFO:root:¡Fueron actualizado(s) 2 registro(s) correctamente en la tabla!

          INFO:root:¡Registro eliminado correctamente!


Asi de esta forma puede ingresar, consultar, actualizar y eliminar registro en una
tabla usando ``MySQL``.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`docker-compose.yml <../../recursos/leccion2/mysql/sistema/docker-compose.yml>`.

    - :download:`__init__.py <../../recursos/leccion2/mysql/sistema/__init__.py>`.

    - :download:`.env.example <../../recursos/leccion2/mysql/sistema/.env.example>`.

    - :download:`main.py <../../recursos/leccion2/mysql/sistema/main.py>`.

    - :download:`requirements.txt <../../recursos/leccion2/mysql/sistema/requirements.txt>`.

    - :download:`settings.py <../../recursos/leccion2/mysql/sistema/settings.py>`.


Asi de esta forma puede replicar una practica real de un proyecto para realizar operaciones
en una base de datos ``MySQL``, aplicando buenas prácticas de código funcional.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::


.. _`MySQL`: https://es.wikipedia.org/wiki/MySQL
.. _`PyMySQL`: https://pymysql.readthedocs.io/en/latest/
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
