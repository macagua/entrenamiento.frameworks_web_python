.. _python_fastapi_instalacion:

Instalación
===========

Para instalar el framework ``FastAPI`` debe seguir los siguientes pasos:


Requisitos previos
------------------

Actualizar repositorios de paquetes disponibles para instalar, con el siguiente comando:

::

    $ sudo apt update && sudo apt upgrade -y

Instalar dependencias mínimas necesarias, con el siguiente comando:

::

    $ sudo apt install -y python3-dev python3-pip python3-virtualenv git


Entorno virtual Python
----------------------

Crear entorno virtual Python en directorio raíz con el siguiente comando:

::

    $ cd $HOME
    $ virtualenv --python /usr/bin/python3 venv


Activar el entorno virtual Python creado con el siguiente comando:

::

    $ source ~/venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework ``FastAPI``, con el siguiente comando:

::

    $ pip3 install -U pip
    $ pip3 install "fastapi[standard]"

Puede probar si la instalación se realizo correctamente, ejecute el siguiente comando:

.. code-block:: console

  $ fastapi --version

Si muestra el numero de la versión instalada de ``FastAPI``, tiene
correctamente instalada la librería.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::
