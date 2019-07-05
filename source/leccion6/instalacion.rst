.. _python_flash_instalacion:

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

	$ sudo apt install sqlitebrowser


Entorno virtual Python
----------------------

Crear entorno virtual Python en directorio ``$HOME`` con el siguiente comando:

::
	
	$ virtualenv --python=/usr/bin/python3 venv


Activarlo entorno virtual Python creado con el siguiente comando:
	
	$ source ~/venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework Flask, con el siguiente comando:

::

	$ pip3 install -U Flask
