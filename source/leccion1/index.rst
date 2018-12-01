.. -*- coding: utf-8 -*-


.. _python_leccion1:

Fast-Track en Python
====================


Vía rápida de programación en Python
------------------------------------

Esta práctica ofrece una introducción rápida a la programación en Python:


#. Uso del fuertemente tipado en Python 3:

.. literalinclude:: ../../recursos/leccion1/fuertemente_tipados.py
    :language: python
    :lines: 1-25


#. Uso tipado dinámico en Python 3:

.. literalinclude:: ../../recursos/leccion1/tipado_dinamico.py
    :language: python
    :lines: 1-20


#. Uso de Clases en Python 3:

   .. note::
        Usando el código ejemplo https://gist.github.com/macagua/c3b8141f5eaf44b891d536861d42bf7f


----


Preparar entorno de desarrollo
------------------------------

#. Actualizar repositorios de paquetes disponibles para instalar, con el siguiente 
   comando:

    ::

        sudo apt-get update

#. Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        sudo apt-get install python3-dev python3-pip python3-virtualenv ipython3

#. Creación de entornos virtuales Python, con los siguientes comando:

    ::

        mkdir $HOME/virtualenv && cd $_
        virtualenv --python /usr/bin/python3 python3
        source $HOME/virtualenv/python3/bin/activate

#. Crear directorio cache para paquetes Python descargados. Cuando hay latencia de 
   Internet y se requiere la instalación de paquetes de Python por un archivo 
   ``requeriments.txt`` de pip pero la instalación falló, entonces puede evitar que 
   la herramienta ``pip`` vuelva a descargar los paquetes previamente descargados, 
   ejecutando este comando:

   .. note::
       Usando el código ejemplo https://gist.github.com/macagua/a365ef25212e151e79bee213197ed0fb

#. Gestionar paquetes Python dentro de un entorno virtual creado, con los siguientes 
   comando:

    ::

        pip install httpie
        http --help

#. Instalar paquetes Python con latencia de conexión a Internet. Cuando hay latencia 
   de Internet y se requiere la instalación de paquetes de Python, ejecute este 
   comando con el parámetro habilitado por el tiempo de espera:

   .. note::
       Usando el código ejemplo https://gist.github.com/macagua/e5078c1ce8e005a6790c25e916f72e1b

#. Desactivar entorno virtual creado, con el siguiente comando:

    ::

        deactivate


----


Introspección a Python
----------------------

#. Actualizar repositorios de paquetes disponibles para instalar, con el siguiente 
   comando:

    ::

        sudo apt-get update

#. Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        sudo apt-get install ipython3

#. Invocar la consola del interprete Python 3, con el siguiente comando:

    ::

        python3

#. Invocar la consola interactiva del interprete Python 3, con el siguiente comando:

    ::

        ipython3


----


Comando GNU/Linux
-----------------

+------------+-----------+-----------+-----------------+-----------------+
| Nombre     | Opciones  | Valores   | Meta Carácter   | Otros comandos  |
+------------+-----------+-----------+-----------------+-----------------+
| pwd        |                                                           | 
+------------+-----------------------------------------------------------+
| man        | ``ls``                                                    | 
+------------+-----------------------------------------------------------+
| ls         | ``-lhap``                                                 |
+------------+-----------------------------------------------------------+
| env        |                                                           |
+------------+-----------------------------------------------------------+
| echo       | ``$HOME``                                                 |
+------------+-----------------------------------------------------------+
| mkdir      | ``$HOME/virtualenv``                                      | 
+------------+-----------------------------------------------------------+
| mkdir      | ``~/.pip``                                                |
+------------+-----------------------------------------------------------+
| nano       | ``~/.pip/pip.conf``                                       |
+------------+-----------+-----------------------------------------------+
| mkdir      | ``-p``    | ``$HOME/demo/prueba/{css,js,images}``         |
+------------+-----------+-----------------------------------------------+
| mkdir      | ``-p``    | ``~/.cache/pip``                              |
+------------+-----------+-----------------------------------------------+
| apt-get    | update    |                                               |
+------------+-----------+-----------------------------------------------+
| apt-get    | install   | python3-dev                                   |
+------------+-----------+-----------+-----------------+-----------------+
| apt-cache  | search    | python3-  |        \|       | ``grep "mysql"``|
+------------+-----------+-----------+-----------------+-----------------+
| http       | ``--help``            |        \|       | ``less``        |
+------------+-----------+-----------+-----------------+-----------------+
| pip        | search    | httpie                                        |
+------------+-----------+-----------------------------------------------+
| pip        | install   | httpie                                        |
+------------+-----------+-----------------------------------------------+
| pip        | uninstall | httpie                                        |
+------------+-----------+-----------+-----------------+-----------------+
| printf     | |pip_conf|            |        >>       | ~/.pip/pip.conf |
+------------+-----------------------+-----------------+-----------------+

.. |pip_conf| replace:: ``'[global]\ndownload_cache = ~/.cache/pip\n'``

.. todo::
    TODO Terminar de escribir la sección "Fast-Track en Python".


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los 
    siguientes enlaces: 
    :download:`fuertemente_tipados.py <../../recursos/leccion1/fuertemente_tipados.py>`
    y :download:`tipado_dinamico.py <../../recursos/leccion1/tipado_dinamico.py>`.


.. tip::
    Para ejecutar el código :file:`fuertemente_tipados.py` y :file:`tipado_dinamico.py`, 
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas: 

    ::

        leccion9/
        ├── fuertemente_tipados.py
        └── tipado_dinamico.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python fuertemente_tipados.py
        python errores_propios.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_leccion1>` 
    del entrenamiento para ampliar su conocimiento en esta temática.


.. commets:
	http://jupyter.org
	https://ipython.org/ipython-doc/3/notebook/notebook.html#introduction
	Primeros pasos con Jupyter Notebook https://www.adictosaltrabajo.com/tutoriales/primeros-pasos-con-jupyter-notebook/
	https://github.com/Covantec/training.python_web/blob/master/notebooks/Networking%20%26%20Sockets.ipynb