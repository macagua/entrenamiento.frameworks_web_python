.. _python_flash_crud_app:

Aplicación CRUD
===============

Hacer un demo local de una aplicación Flask 
`CRUD <https://es.wikipedia.org/wiki/CRUD>`_, es decir, 
una aplicación con las funciones básicas en bases de datos 
como "Crear, Leer, Actualizar y Borrar".


Requisitos previos
------------------

Para trabajar una aplicación Flask con bases de datos relacionales 
requiere instalar las siguientes librerías:

- `Flask <https://pypi.org/project/Flask/>`_.

- `Flask-SQLAlchemy <https://pypi.org/project/Flask-SQLAlchemy/>`_.

- `SQLAlchemy <https://pypi.org/project/SQLAlchemy/>`_.

Actualizar repositorios de paquetes disponibles para instalar, 
con el siguiente comando:

::

	$ sudo apt update

Instalar dependencias mínimas necesarias, con el siguiente comando:

::

	$ sudo apt install python3-dev python3-pip python3-virtualenv git sqlitebrowser


Entorno virtual Python
----------------------

Crear entorno virtual Python en directorio ``$HOME`` con el 
siguiente comando:

::

	$ virtualenv --python=/usr/bin/python3 venv


Activarlo entorno virtual Python creado con el siguiente comando:

::

	$ source ~/venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework Flask, con 
el siguiente comando:

::

	$ pip3 install Flask==1.0.2 Flask-SQLAlchemy==2.4.0 SQLAlchemy==1.3.5


Estructura de proyecto
^^^^^^^^^^^^^^^^^^^^^^

Crear estructura de proyecto Flask, con el siguiente comando:

::

	$ mkdir -p ~/projects/flask-crud-app/templates && cd $_ && cd ../

Cree modulo Python llamado :file:`bookmanager.py` dentro del 
directorio :file:`~/projects/flask-crud-app`, con el siguiente comando:

::

	$ nano ~/projects/flask-crud-app/bookmanager.py

Agregue el siguiente contenido al archivo :file:`~/projects/flask-crud-app/bookmanager.py`.

.. literalinclude:: ../../recursos/leccion6/flask-crud-app/bookmanager.py
   :language: python
   :lines: 7-66


Cree plantilla HTML llamado :file:`home.html` dentro del directorio 
:file:`~/projects/flask-crud-app/templates`, con el siguiente comando:

::

	$ nano ~/projects/flask-crud-app/templates/home.html

Agregue el siguiente contenido al archivo :file:`~/projects/flask-crud-app/templates/home.html`.

.. literalinclude:: ../../recursos/leccion6/flask-crud-app/templates/home.html
   :language: python
   :lines: 1-33


Crear base de datos
^^^^^^^^^^^^^^^^^^^

Crear base de datos SQLite, con los siguientes comando:

::

	$ cd ~/projects/flask-crud-app/
	$ python3
	>>> from bookmanager import db
	>>> db.create_all()
	>>> exit()


Ejecutar aplicación Flask
^^^^^^^^^^^^^^^^^^^^^^^^^

Ejecutar aplicación Web Flask, con el siguiente comando: 

::

	$ python3 bookmanager.py

Abrir en navegador >>> http://127.0.0.1:8087

.. comments:

	.. figure:: ../_static/flask-bookmanager.png
	  :class: image-inline
	  :alt: BookManager - una Aplicación CRUD Flash
	  :align: center

	  BookManager - una Aplicación CRUD Flash

.. figure:: https://raw.githubusercontent.com/Covantec/entrenamiento.frameworks_web_python/master/source/_static/flask-bookmanager.png
  :class: image-inline
  :alt: BookManager - una Aplicación CRUD Flash
  :align: center

  BookManager - una Aplicación CRUD Flash


.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/macagua/flask-crud-app

.. tip::
    Usando el articulo `"Building a CRUD application with Flask and SQLAlchemy" <https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2>`_.
