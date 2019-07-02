.. -*- coding: utf-8 -*-


.. _python_entorno_desarrollo:

Entorno de desarrollo
=====================

Para preparar el entorno de desarrollo, ejecute los siguientes pasos:


#. Actualizar repositorios de paquetes disponibles para instalar, con el siguiente 
   comando:

    ::

        $ sudo apt-get update

#. Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        $ sudo apt-get install python3-dev python3-pip python3-virtualenv

#. Creación de entornos virtuales Python, con los siguientes comando:

    ::

        $ mkdir $HOME/virtualenv && cd $_
        $ virtualenv --python /usr/bin/python3 python3
        $ source $HOME/virtualenv/python3/bin/activate

#. Crear directorio cache para paquetes Python descargados. Cuando hay latencia de 
   Internet y se requiere la instalación de paquetes de Python por un archivo 
   ``requeriments.txt`` de la herramienta ``pip`` pero la instalación falló, entonces 
   puede evitar que la herramienta ``pip`` vuelva a descargar los paquetes previamente 
   descargados, ejecutando este comando:

    ::

        $ mkdir -p ~/.cache/pip && mkdir ~/.pip && printf '[global]\ndownload_cache = ~/.cache/pip\n' >> ~/.pip/pip.conf

#. Gestionar paquetes Python dentro de un entorno virtual creado, con los siguientes 
   comando:

    ::

        $ pip install httpie
        $ http --help

#. Instalar paquetes Python con latencia de conexión a Internet. Cuando hay latencia 
   de Internet y se requiere la instalación de paquetes de Python, ejecute este 
   comando con el parámetro ``--timeout`` habilitado para el tiempo de espera:

    ::

        pip install -r requirements.txt --timeout 120

#. Desactivar entorno virtual creado, con el siguiente comando:

    ::

        $ deactivate


----


Introspección a Python
----------------------

#. Actualizar repositorios de paquetes disponibles para instalar, con el siguiente 
   comando:

    ::

        $ sudo apt-get update

#. Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        $ sudo apt-get install ipython3

#. Invocar la consola del interprete Python 3, con el siguiente comando:

    ::

        $ python3

#. Invocar la consola interactiva del interprete Python 3, con el siguiente comando:

    ::

        $ ipython3


Así de esta forma tiene instalado y configurado mínimamente el entorno de desarrollo 
en Python bajo GNU/Linux.
