.. _python_flask_crud_app:

Aplicación CRUD
===============

Hacer un demo local de una aplicación `CRUD`_ en :doc:`Flask <./index>` , es decir,
una aplicación con las funciones básicas en bases de datos como *"Crear, Leer,
Actualizar y Borrar"*.


Requisitos previos
------------------

Para trabajar una aplicación ``Flask`` con bases de datos relacionales requiere
instalar las siguientes librerías:

- :ref:`Entorno de desarrollo <python_entorno_desarrollo>`.

- :ref:`Python package installer - pip <python_entorno_desarrollo_pip>`.

- :ref:`Entorno virtual Python <python_entorno_desarrollo_venv>`.

- Motor de base de datos :ref:`SQLite <python_sqlite3_instalar>`.

Para trabajar una aplicación ``Flask`` con bases de datos relacionales
requiere instalar las siguientes librerías:

- :ref:`Flask <python_flask>`.

- :ref:`SQLAlchemy <python_sqlalchemy>`.

- `Flask-SQLAlchemy <https://pypi.org/project/Flask-SQLAlchemy/>`_.

..
    Actualizar repositorios de paquetes disponibles para instalar,
    con el siguiente comando:

    Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        sudo apt install -y python3-dev python3-pip python3-virtualenv

    ::

        sudo apt install -y sqlite3


    Entorno virtual Python
    ----------------------

    Crear entorno virtual Python en directorio ``$HOME`` con el
    siguiente comando:

    ::

        virtualenv --python /usr/bin/python3 ~/venv


    Activarlo entorno virtual Python creado con el siguiente comando:

    ::

        source ~/venv/bin/activate




Estructura de proyecto
----------------------

Crear estructura de proyecto ``Flask``, con el siguiente comando:

.. code-block:: console

    mkdir -p ~/proyectos/flask/crud-app/templates && cd $_ && cd ../

Cree módulo Python llamado :file:`bookmanager.py` dentro del
directorio :file:`~/proyectos/flask/crud-app`, con el siguiente comando:

.. code-block:: console

    nano ~/proyectos/flask/crud-app/bookmanager.py

Agregue el siguiente contenido al archivo :file:`~/proyectos/flask/crud-app/bookmanager.py`.

.. literalinclude:: ../../recursos/leccion6/flask-crud-app/bookmanager.py
   :language: python
   :lines: 1-98


Cree plantilla HTML llamado :file:`home.html` dentro del directorio
:file:`~/proyectos/flask/crud-app/templates`, con el siguiente comando:

::

    nano ~/proyectos/flask/crud-app/templates/home.html

Agregue el siguiente contenido al archivo :file:`~/proyectos/flask/crud-app/templates/home.html`.

.. literalinclude:: ../../recursos/leccion6/flask-crud-app/templates/home.html
   :language: html
   :lines: 1-42


----


Para ejecutar el código del proyecto llamado ``crud-app`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── flask/
        └── crud-app/
            ├── bookmanager.py
            └── templates/
                └── home.html

Si tiene la estructura de archivo previa, entonces puede continuar los procesos de instalación,
configuración y ejecución del código fuente.


----


Instalar paquetes Python
------------------------

Para instalar el framework ``Flask`` usando la herramienta :ref:`pip <python_entorno_desarrollo_pip>`,
ejecute el siguiente comando:

.. code-block:: console

    pip3 install Flask==3.1.0 Flask-SQLAlchemy==3.1.1 SQLAlchemy==2.0.38

Si ejecuto el comando anterior, instalo las librerías necesarias para ejecutar.
De esta forma puede continuar.


Ejecutar aplicación Flask
-------------------------

Para ejecutar la aplicación Web ``Flask``, debe ejecutar el siguiente comando:

.. code-block:: console

    python3 bookmanager.py

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:8087


.. figure:: ../_static/images/flask-bookmanager.png
  :class: image-inline
  :alt: BookManager - una Aplicación CRUD Flask
  :align: center

  BookManager - una Aplicación CRUD ``Flask``.

La ejecución de la aplicación Web ``Flask`` crea la base de datos ``SQLite``
``book_database.sqlite3`` en el directorio :file:`~/proyectos/flask/crud-app/`.

Puede ver examinar la estructura de la base de datos ``SQLite``, de las siguientes formas:

- :ref:`SQLite Tools <python_sqlite3_tools_instalar>`.

- :ref:`DB Browser for SQLite <python_sqlite3_sqlitebrowser_instalar>`.

Por ejemplo, el ``DB Browser for SQLite`` mostrará gráficamente la estructura de la aplicación ``BookManager``,
como la siguiente figura:

.. figure:: ../_static/images/flask-bookmanager-sqlitebrowser-db.png
  :class: image-inline
  :alt: BookManager - DB Browser para SQLite
  :align: center

  BookManager - DB Browser para ``SQLite``

.. tip::
    La base de datos ``SQLite`` se crea automáticamente al ejecutar la aplicación ``BookManager``
    necesaria para el funcionamiento de la aplicación.

De esta forma puede interactuar con un ejemplo operaciones dentro una base de datos ``SQLite``.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`bookmanager.py <../../recursos/leccion6/flask-crud-app/bookmanager.py>`.

    - :download:`home.html <../../recursos/leccion6/flask-crud-app/templates/home.html>`.

.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/macagua/example.flask.crud-app

.. tip::
    Usando el articulo `"Building a CRUD application with Flask and SQLAlchemy" <https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2>`_.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`CRUD`: https://es.wikipedia.org/wiki/CRUD
