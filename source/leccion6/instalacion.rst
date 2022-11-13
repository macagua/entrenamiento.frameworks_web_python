.. _python_flask_instalacion:

Instalación
===========

Para instalar el framework Flask debe seguir los siguientes pasos:


Requisitos previos
------------------

Actualizar repositorios de paquetes disponibles para instalar, con el siguiente comando:

::

	$ sudo apt update

Instalar dependencias mínimas necesarias, con el siguiente comando:

::

	$ sudo apt install python3-dev python3-pip python3-virtualenv git


Entorno virtual Python
----------------------

Crear entorno virtual Python en directorio raíz con el siguiente comando:

::

	$ cd $HOME
	$ virtualenv --python=/usr/bin/python3 venv


Activar el entorno virtual Python creado con el siguiente comando:

::

	$ source ~/venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework Flask, con el siguiente comando:

::

	$ pip3 install -U Flask

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando:

.. code-block:: console

  $ python3 -c "import flask ; print(flask.__version__)"

Si muestra el numero de la versión instalada de SQLAlchemy, tiene
correctamente instalada la librería.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
