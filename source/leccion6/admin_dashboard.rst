.. _python_flask_admin_dashboard:

Aplicación Admin
================

El objeto de esta sección es hacer un demostración local de una interfaz
"Administrativa - (Admin)" que integre un "Dashboard" en :doc:`Flask <./index>`.

Requisitos previos
-------------------

Para hacer un demostración local de un aplicación Dashboard de
``Flask-Admin`` requiere instalar las siguientes librerías:

- :ref:`Flask <python_flask>`.

- `Flask-Admin <https://pypi.org/project/Flask-Admin/>`_.

- `Flask-SQLAlchemy <https://pypi.org/project/Flask-SQLAlchemy/>`_.

- `Flask-Security <https://pypi.org/project/Flask-Security/>`_.

- :ref:`SQLAlchemy <python_sqlalchemy>`.

- `AdminLTE <https://adminlte.io>`_.

- Motor de base de datos :ref:`SQLite <python_sqlite3_instalar>`.

..
    Actualizar repositorios de paquetes disponibles para instalar, con
    el siguiente comando:

    .. code-block:: console

        sudo apt update && sudo apt upgrade -y

    Instalar dependencias mínimas necesarias, con el siguiente comando:

    .. code-block:: console

        sudo apt install -y python3-dev python3-pip python3-virtualenv

    .. code-block:: console

        sudo apt install -y git

    .. code-block:: console

        sudo apt install -y sqlite3


Descargar código
-----------------

Usted puede descargar código desde Github, ejecutando el siguiente comando:

.. code-block:: console

    cd ~/ && git clone https://github.com/macagua/example.flask.admin-dashboard.git flask-admin-dashboard


Acceda al directorio llamado ``flask-admin-dashboard``, ejecutando el siguiente comando:

.. code-block:: console

    cd ~/flask-admin-dashboard


..
    Entorno virtual Python
    -----------------------

    Crear entorno virtual Python en directorio :file:`~/flask-admin-dashboard` con el siguiente comando:

    .. code-block:: console

        virtualenv --python /usr/bin/python3 venv


    Activarlo entorno virtual Python creado con el siguiente comando:

        source ./venv/bin/activate


Instalar paquetes Python
-------------------------

Para instalar las dependencias para usar del framework ``Flask``, con el siguiente comando:

.. code-block:: console

    pip3 install -r requirements.txt


Ejecutar aplicación Flask
--------------------------

Para ejecutar aplicación Web ``Flask``, con los siguientes comandos:

.. code-block:: console

    python3 ./app.py

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
librería `Flask-Admin <https://pypi.org/project/Flask-Admin/>`_ que incluye un
Dashboard construido bajo la GUI de `AdminLTE <https://adminlte.io>`_, como se
muestra en la siguiente figura:

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

.. code-block:: console

    sqlitebrowser sample_db.sqlite

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

..
  .. disqus::
