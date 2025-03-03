.. _python_flask_instalacion:

Instalación
===========

Para instalar el framework :ref:`Flask <python_leccion6>` debe seguir los siguientes pasos:


Requisitos previos
------------------

- Instalar las :ref:`librerías del entorno de desarrollo <python_entorno_desarrollo>`.

- Instalar el :ref:`Python package installer - pip <python_entorno_desarrollo_pip>`.

- Instalar y activar un :ref:`entorno virtual Python <python_entorno_desarrollo_venv>`.

..
    Actualizar repositorios de paquetes disponibles para instalar, con el siguiente comando:

    ::

        sudo apt update && sudo apt upgrade -y

    Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        sudo apt install -y python3-dev
        sudo apt install -y python3-pip
        sudo apt install -y python3-virtualenv

    ::

        sudo apt install -y git


    Entorno virtual Python
    ----------------------

    Crear entorno virtual Python en directorio raíz con el siguiente comando:

    ::

        virtualenv --python /usr/bin/python3 ~/venv


    Activar el entorno virtual Python creado con el siguiente comando:

    ::

        source ~/venv/bin/activate


Instalar paquetes Python
------------------------

Para instalar las dependencias para usar del framework ``Flask``, con el siguiente comando:

.. code-block:: console

    pip3 install Flask==3.1.0

Puede probar si la instalación se realizo correctamente, ejecute el siguiente comando:

.. code-block:: console

    flask --version

Si muestra el numero de la versión instalada de ``Flask``, tiene
correctamente instalada la librería.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
