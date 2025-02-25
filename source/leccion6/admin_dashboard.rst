.. _python_flask_admin_dashboard:

Aplicación Admin
================

El objeto de esta sección es hacer un demostración local de una
interfaz "Administrativa - (Admin)" que integre un "Dashboard" en ``Flask``.

Requisitos previos
-------------------

Para hacer un demostración local de un aplicación Dashboard de
``Flask-Admin`` requiere instalar las siguientes librerías:

- `Flask <https://pypi.org/project/Flask/>`_.

- `Flask-Admin <https://pypi.org/project/Flask-Admin/>`_.

- `Flask-SQLAlchemy <https://pypi.org/project/Flask-SQLAlchemy/>`_.

- `Flask-Security <https://pypi.org/project/Flask-Security/>`_.

- `SQLAlchemy <https://pypi.org/project/SQLAlchemy/>`_.

- `AdminLTE <https://adminlte.io>`_.

Actualizar repositorios de paquetes disponibles para instalar, con
el siguiente comando:

::

    $ sudo apt update && sudo apt upgrade -y

Instalar dependencias mínimas necesarias, con el siguiente comando:

::

    $ sudo apt install -y python3-dev python3-pip python3-virtualenv
    $ sudo apt install -y git
    $ sudo apt install -y sqlite3


Descargar código
-----------------

Usted puede descargar código desde Github, ejecutando el siguiente comando:

::

    $ cd ~/ && git clone https://github.com/macagua/example.flask.admin-dashboard.git flask-admin-dashboard
    $ cd ~/flask-admin-dashboard


Entorno virtual Python
-----------------------

Crear entorno virtual Python en directorio :file:`~/flask-admin-dashboard` con el siguiente comando:

::

    $ virtualenv --python /usr/bin/python3 venv


Activarlo entorno virtual Python creado con el siguiente comando:

    $ source ./venv/bin/activate


Instalar paquetes Python
-------------------------

Para instalar las dependencias para usar del framework ``Flask``, con el siguiente comando:

::

    $ pip3 install -r requirements.txt


Ejecutar aplicación Flask
--------------------------

Para ejecutar aplicación Web ``Flask``, con los siguientes comandos:

::

    $ python3 ./app.py

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:5000/admin/


Flask Authentication
---------------------

La aplicación Dashboard de ``Flask-Admin`` usa el plugin
`Flask-Security <https://pypi.org/project/Flask-Security/>`_ para
la autenticación de usuarios de la aplicación, como se muestra
en la siguiente figura:

.. figure:: ../_static/images/flask-admin-dashboard-index.png
  :class: image-inline
  :alt: Aplicación Dashboard de Flask-Admin - Vista de Inicio
  :align: center

  Aplicación Dashboard de ``Flask-Admin`` - Vista de Inicio

.. figure:: ../_static/images/flask-admin-dashboard-login.png
  :class: image-inline
  :alt: Aplicación Dashboard de Flask-Admin -  Vista de Inicio de sesión
  :align: center

  Aplicación Dashboard de ``Flask-Admin`` - Vista de Inicio de sesión


Dashboard Admin
----------------

La aplicación Dashboard de ``Flask-Admin`` usa su propio interfaz Admin usando la
librería `Flask-Admin <https://pypi.org/project/Flask-Admin/>`_ que
incluye un Dashboard construido bajo la GUI de `AdminLTE <https://adminlte.io>`_,
como se muestra en la siguiente figura:

.. figure:: ../_static/images/flask-admin-dashboard.png
  :class: image-inline
  :alt: Aplicación Dashboard de Flask-Admin
  :align: center

  Aplicación Dashboard de ``Flask-Admin``


DB Browser para SQLite
-----------------------

La aplicación Dashboard de ``Flask-Admin`` usa la base de datos de ``SQLite``
para almacenar sus datos, usted puede ver gráficamente la estructura y registros
de la base de datos, con el siguiente comando:

::

    $ sqlitebrowser sample_db.sqlite

Este mostrará el DB Browser para ``SQLite`` para SQLite de la aplicación Dashboard de
``Flask-Admin``, como la siguiente figura:

.. figure:: ../_static/images/flask-admin-dashboard-sqlitebrowser-db.png
  :class: image-inline
  :alt: Base de datos del Dashboard de Flask-Admin - DB Browser para SQLite
  :align: center

  Base de datos del Dashboard de ``Flask-Admin`` - DB Browser para ``SQLite``

Como puede ver en la figura anterior la aplicación Dashboard de ``Flask-Admin``
tiene su propia estructura de datos por cada plugin ``Flask`` o modelos de su
aplicación.

..
    .. note::
        El código ejemplo usado puede encontrarlo en: https://github.com/macagua/example.flask.admin-dashboard


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
