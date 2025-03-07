.. _python_entorno_desarrollo:

Entorno de desarrollo
=====================

Para preparar el entorno de desarrollo, ejecute los siguientes pasos:

Requerimientos previos
----------------------

Actualizar repositorios de paquetes disponibles para instalar, con el
siguiente comando:

.. code-block:: console

    sudo apt update && sudo apt upgrade -y

Instalar dependencias mínimas necesarias, con el siguiente comando:

.. code-block:: console

    sudo apt install -y build-essential python3-dev

Instalar el cliente `git`_, con el siguiente comando:

.. code-block:: console

    sudo apt install -y git

Si ejecuto el comando anterior, entonces instalo las dependencias
básicas para el desarrollo en Python 3.


----


.. _python_entorno_desarrollo_pip:


Python package installer - pip
------------------------------

`pip`_ es el instalador de paquetes de Python. Se integra con la herramienta
:ref:`virtualenv <python_entorno_desarrollo_venv>`, no hace instalaciones parciales,
puede guardar el estado del paquete para reproducirlo, puede instalar desde fuentes
que no sean :term:`Egg`, y puede instalar desde repositorios de control de versiones.

Instalar la herramienta ``pip``, ejecute el siguiente comando:

.. code-block:: console

    sudo apt install -y python3-pip

Para comprobar que la instalación de la herramienta ``pip`` este correctamente hecha,
ejecute el siguiente comando:

.. code-block:: console

    pip3 -V

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: console

    pip 25.0.1 from /usr/bin/lib/python3.11/site-packages/pip (python 3.11)

Si muestra el numero de la versión instalada de ``pip``, tiene correctamente instalada
la paquete. Con esto, ya tiene todo listo para continuar.

----


.. _python_entorno_desarrollo_pip_cache:


Cache local de paquetes con pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Crear directorio cache para paquetes Python descargados. Cuando hay latencia de
Internet y se requiere la instalación de paquetes de Python por un archivo
``requirements.txt`` de la herramienta :ref:`pip <python_entorno_desarrollo_pip>`
pero la instalación falló, entonces puede evitar que la herramienta ``pip`` vuelva
a descargar los paquetes previamente descargados, ejecutando este comando:

Cree un directorio cache para los paquetes descargando con la herramienta :ref:`pip <python_entorno_desarrollo_pip>`,
ejecutando el siguiente comando:

.. code-block:: console

    mkdir -p ~/.cache/pip && mkdir ~/.pip


Cree el archivo de configuración de la herramienta :ref:`pip <python_entorno_desarrollo_pip>`,
ejecutando el siguiente comando:

.. code-block:: console

    printf '[global]\ndownload_cache = ~/.cache/pip\n' \
            >> ~/.pip/pip.conf

Asi cada ves que ejecute el comando ``pip3 install`` la herramienta :ref:`pip <python_entorno_desarrollo_pip>`
usara el directorio ``~/.cache/pip`` como directorio cache, esto permite agilizar la descarga
de paquetes, ya que :ref:`pip <python_entorno_desarrollo_pip>` primero buscara en ese archivo
primero, si no esta descargado, lo buscara en Internet en el repositorio :term:`PyPI`. Con esto,
ya tiene todo listo para continuar.


----


.. _python_entorno_desarrollo_pip_requirements:


Gestionar paquetes Python
^^^^^^^^^^^^^^^^^^^^^^^^^

Para gestionar paquetes Python dentro de un entorno virtual creado, con el siguiente comando:

.. code-block:: console

    pip3 install cookiecutter

El paquete `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ se instalo
previamente puede usarlo vía script de línea de comando, con el siguiente:

.. code-block:: console

    cookiecutter --help

Ademas si requiere instalar paquetes Python con latencia de conexión a Internet. Cuando hay
latencia de Internet y se requiere la instalación de paquetes de Python, ejecute este
comando con el parámetro ``--timeout`` habilitado para el tiempo de espera:

.. code-block:: console

    virtualenv --python /usr/bin/python3 venv

.. code-block:: console

    source ./venv/bin/activate

.. code-block:: console

    pip3 install -U pip && pip3 install cookiecutter --timeout 120

También puede gestionar una lista de instalación de paquetes y sus versiones para indicar
a la herramienta ``pip`` que los instale con un solo comando, para esto cree y edite un
archivo, ejecutando lo siguiente:

.. code-block:: console

    nano requirements.txt

Agregue el siguiente contenido:

.. code-block:: console

    cookiecutter==2.6.0

Guarde el archivo y procede a ejecutar la herramienta ``pip``, con el parámetro ``-r``
seguido de la ruta absoluta o relativa del archivo previamente creado.

.. code-block:: console

    pip3 install -r requirements.txt

Luego de la instalación puede ejecuta el comando ``cookiecutter -V`` el cual ofrece
una salida de la versión.

.. code-block:: console

    cookiecutter -V

Luego de la instalación puede ejecuta el comando ``pip3 freeze`` el cual ofrece una salida de
paquetes instalados en formato de archivos `requirements <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`_.
Los paquetes se enumeran en un ordenan de forma tal que no distingue entre mayúsculas y minúsculas.

.. code-block:: console

    pip3 freeze

Si ejecuto el comando anterior, debería mostrar algo parecido al siguiente mensaje:

.. code-block:: console
    :class: no-copy

    arrow==1.3.0
    binaryornot==0.4.4
    certifi==2025.1.31
    chardet==5.2.0
    charset-normalizer==3.4.1
    click==8.1.8
    cookiecutter==2.6.0
    idna==3.10
    Jinja2==3.1.6
    markdown-it-py==3.0.0
    MarkupSafe==3.0.2
    mdurl==0.1.2
    Pygments==2.19.1
    python-dateutil==2.9.0.post0
    python-slugify==8.0.4
    PyYAML==6.0.2
    requests==2.32.3
    rich==13.9.4
    six==1.17.0
    text-unidecode==1.3
    types-python-dateutil==2.9.0.20241206
    urllib3==2.3.0

Usted puede actualizar el archivo ``requirements.txt`` con el resultado de la ejecución el comando
``pip3 freeze`` ejecutando el siguiente comando:

.. code-block:: console

    pip3 freeze > requirements.txt

Así de esta forma congela las versiones usadas para el proceso de instalación de sus paquetes Python.


----


.. _python_entorno_desarrollo_venv:


Entornos virtuales Python
^^^^^^^^^^^^^^^^^^^^^^^^^

Para la instalación de la herramienta de entornos virtuales en Python,
ejecute el siguiente comando:

.. tabs::

   .. group-tab:: PIP

      .. code-block:: console

          pip3 install virtualenv

   .. group-tab:: Ubuntu/Debian Linux

      .. code-block:: console

          sudo apt install -y python3-virtualenv

Cree un directorio raíz para almacenar los diversos entornos virtuales,
ejecutando el siguiente comando:

.. code-block:: console

    mkdir ~/virtualenv && cd $_

Cree un entorno virtual llamado ``python3``, ejecutando el siguiente comando:

.. code-block:: console

    virtualenv --python /usr/bin/python3 python3

Activar el entorno virtual llamado ``python3``, ejecutando el siguiente comando:

.. code-block:: console

    source ~/virtualenv/python3/bin/activate

Para desactivar entorno virtual creado, con el siguiente comando:

.. code-block:: console

    deactivate

De esta forma, puedes tener un directorio común para almacenar diversos entornos virtuales.
Con herramientas como ``virtualenv`` puede gestionar diversos entornos virtuales de Python
para diversas versiones de Python, por ejemplo:

Diversas versiones de Python, es posible que requiera trabajar con un proyecto Python que
requiera la versión ``3.9`` y y al otro proyecto que requiera la versión ``3.11``, para estés
caso puede gestionar la instalación de las dos versiones de Python con la herramienta `pyenv`_
y luego crear dos entornos virtuales para cada version, con los siguientes comandos:

Crear y activar un entorno virtual para la versión Python ``3.9``, ejecutando el siguiente comando:

.. code-block:: console

    virtualenv --python ~/.pyenv/shims/python3.9 ~/virtualenv/python39 && source ~/virtualenv/python39/bin/activate


Crear y activar un entorno virtual para la versión Python ``3.11``, ejecutando el siguiente comando:

.. code-block:: console

    virtualenv --python ~/.pyenv/shims/python3.11 ~/virtualenv/python311 && source ~/virtualenv/python311/bin/activate


En estos casos anteriores, hemos creado dos entornos virtuales como ``python39`` y ``python311``,
esto le permite crear diversos entornos virtuales para proyectos, con el nombre que quiera,
podría ser un entorno virtual para llamado ``acme_inc`` para un cliente llamado **ACME Industry**
o otro entorno virtual llamado ``test-django`` para unas pruebas de un proyecto de Django.

.. tip::

   Normalmente es muy común conseguir en las instrucciones de instalación de entornos virtuales
   para diversos proyectos Python, con los siguientes nombres ``.env``, ``.venv`` y ``venv``.


Con esto, ya tiene todo listo para continuar.


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


..
  .. disqus::

.. _`git`: https://git-scm.com/
.. _`pip`: https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes)
.. _`pyenv`: https://github.com/pyenv/pyenv
