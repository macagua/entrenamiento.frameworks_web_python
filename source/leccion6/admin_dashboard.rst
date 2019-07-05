.. _python_flash_admin_dashboard:

Admin Dashboard
===============

Hacer un demo local de Flask Admin Dashboard


Requisitos previos
------------------

Actualizar repositorios de paquetes disponibles para instalar, con el siguiente comando:

::

	$ sudo apt update

Instalar dependencias mínimas necesarias, con el siguiente comando:

::

	$ sudo apt install python3-dev python3-pip python3-virtualenv git sqlitebrowser


Descargar código
-----------------

Usted puede descargar código desde Github, ejecutando el siguiente comando:

::

	$ cd ~/ && git clone https://github.com/jonalxh/Flask-Admin-Dashboard.git
	$ cd ~/Flask-Admin-Dashboard


Entorno virtual Python
----------------------

Crear entorno virtual Python en directorio file:`~/Flask-Admin-Dashboard` con el siguiente comando:

::
	
	$ virtualenv --python=/usr/bin/python3 venv


Activarlo entorno virtual Python creado con el siguiente comando:
	
	$ source ./venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework Flask, con el siguiente comando:

::

	$ pip install -r requirements.txt


Ejecutar aplicación Flask
-------------------------

Para ejecutar aplicación Web Flask, con los siguientes comandos:

::

    $ chmod +x app.py
    $ ./app.py

Abrir en navegador >>> http://127.0.0.1:5000/admin/

.. comments:

	.. figure:: ../_static/flask-admin-dashboard-index.png
	  :class: image-inline
	  :alt: Flash Admin Dashboard - Index
	  :align: center

	  Flash Admin Dashboard - Index

.. figure:: https://raw.githubusercontent.com/Covantec/entrenamiento.frameworks_web_python/master/source/_static/flask-admin-dashboard-index.png
  :class: image-inline
  :alt: Flash Admin Dashboard - Index
  :align: center

  Flash Admin Dashboard - Index

.. comments:

	.. figure:: ../_static/flask-admin-dashboard-login.png
	  :class: image-inline
	  :alt: Flash Admin Dashboard - Inicio de sesión
	  :align: center

	  Flash Admin Dashboard - Inicio de sesión

.. figure:: https://raw.githubusercontent.com/Covantec/entrenamiento.frameworks_web_python/master/source/_static/flask-admin-dashboard-login.png
  :class: image-inline
  :alt: Flash Admin Dashboard - Inicio de sesión
  :align: center

  Flash Admin Dashboard - Inicio de sesión

.. comments:

	.. figure:: ../_static/flask-admin-dashboard.png
	  :class: image-inline
	  :alt: Flash Admin Dashboard
	  :align: center

	  Flash Admin Dashboard

.. figure:: https://raw.githubusercontent.com/Covantec/entrenamiento.frameworks_web_python/master/source/_static/flask-admin-dashboard.png
  :class: image-inline
  :alt: Flash Admin Dashboard
  :align: center

  Flash Admin Dashboard

.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/jonalxh/Flask-Admin-Dashboard
