.. _python_entorno_desarrollo:

Entorno de desarrollo
=====================

Para preparar el entorno de desarrollo, ejecute los siguientes pasos:

Requerimientos previos
----------------------

Actualizar repositorios de paquetes disponibles para instalar, con el
siguiente comando:

.. code-block:: console

    $ sudo apt update

Instalar dependencias mínimas necesarias, con el siguiente comando:

.. code-block:: console

    $ sudo apt install python3-dev python3-pip python3-virtualenv


Entornos virtuales Python
^^^^^^^^^^^^^^^^^^^^^^^^^

Creación de entornos virtuales Python, con los siguientes comando:

.. code-block:: console

    $ mkdir $HOME/virtualenv && cd $_
    $ virtualenv --python /usr/bin/python3 python3
    $ source $HOME/virtualenv/python3/bin/activate

Para desactivar entorno virtual creado, con el siguiente comando:

.. code-block:: console

    $ deactivate


Cache local de paquetes con Pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Crear directorio cache para paquetes Python descargados. Cuando hay latencia de
Internet y se requiere la instalación de paquetes de Python por un archivo
``requeriments.txt`` de la herramienta ``pip`` pero la instalación falló, entonces
puede evitar que la herramienta ``pip`` vuelva a descargar los paquetes previamente
descargados, ejecutando este comando:

.. code-block:: console

    $ mkdir -p ~/.cache/pip && mkdir ~/.pip
    $ printf '[global]\ndownload_cache = ~/.cache/pip\n' \
            >> ~/.pip/pip.conf


Gestionar paquetes Python
^^^^^^^^^^^^^^^^^^^^^^^^^

Para gestionar paquetes Python dentro de un entorno virtual creado, con el siguiente comando:

.. code-block:: console

    $ pip3 install cookiecutter

El paquete `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ se instalo previamente puede usarlo vía script de linea de comando, con el siguiente:

.. code-block:: console

    $ cookiecutter --help

Ademas si requiere instalar paquetes Python con latencia de conexión a Internet. Cuando hay latencia
de Internet y se requiere la instalación de paquetes de Python, ejecute este
comando con el parámetro ``--timeout`` habilitado para el tiempo de espera:

.. code-block:: console

    $ pip3 install cookiecutter --timeout 120

También puede gestionar una lista de instalación de paquetes y sus versiones para indicar
a la herramienta ``pip`` que los instale con un solo comando, para esto cree y edite un
archivo, ejecutando lo siguiente:

.. code-block:: console

    $ nano requirements.txt

Agregue el siguiente contenido:

.. code-block:: console

    cookiecutter==1.6.0

Guarde el archivo y procede a ejecutar la herramienta ``pip``, con el parámetro ``-r``
seguido de la ruta absoluta o relativa del archivo previamente creado.

.. code-block:: console

    $ pip3 install -r requirements.txt

Luego de la instalación puede ejecuta el comando ``pip3 freeze`` el cual ofrece una salida de
paquetes instalados en formato de archivos `requirements <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`_.
Los paquetes se enumeran en un ordenan de forma tal que no distingue entre mayúsculas y minúsculas.

::

    $ pip3 freeze
    arrow==1.2.3
    binaryornot==0.4.4
    certifi==2022.9.24
    chardet==5.0.0
    charset-normalizer==2.1.1
    click==8.1.3
    cookiecutter==2.1.1
    idna==3.4
    importlib-metadata==5.0.0
    Jinja2==3.1.2
    jinja2-time==0.2.0
    MarkupSafe==2.1.1
    python-dateutil==2.8.2
    python-slugify==6.1.2
    PyYAML==6.0
    requests==2.28.1
    six==1.16.0
    text-unidecode==1.3
    typing_extensions==4.4.0
    urllib3==1.26.12
    zipp==3.10.0

Usted puede actualizar el archivo ``requirements.txt`` con el resultado de la ejecución el comando
``pip3 freeze`` ejecutando el siguiente comando:

.. code-block:: console

    $ pip3 freeze > requirements.txt

Así de esta forma congela las versiones usadas para el proceso de instalación de sus paquetes Python.


----


.. important::
    Usted puede descargar el archivo usado en esta sección haciendo clic en el
    siguiente enlace: :download:`requirements.txt <../../recursos/leccion1/requirements.txt>`.


.. tip::
    Para ejecutar el archivo :file:`requirements.txt`, abra una consola de comando, active el entorno
    virtual Python, y te ubicas en el directorio donde descargo el archivo, entonces ejecute el siguiente
    comando:

    .. code-block:: console

        pip3 install -r requirements.txt


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
