.. _python_django_instalacion:

Instalación
===========

Para instalar el framework Django debe seguir los siguientes pasos:


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

    $ source ~/venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework Django, con el siguiente comando:

::

    $ pip3 install -U Django


Puede probar la instalación hecha en el comando previo del framework Django, con el siguiente comando:

::

    $ python3 -m django --version


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion7>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
