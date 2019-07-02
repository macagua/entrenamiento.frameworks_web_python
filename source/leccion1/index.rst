.. -*- coding: utf-8 -*-


.. _python_leccion1:

Fast-Track en Python
====================


Vía rápida de programación en Python
------------------------------------

Esta práctica ofrece una introducción rápida a la programación en Python:


#. **Python 3 es fuertemente tipado:** esto significa que el tipo de valor no cambia 
   repentinamente. Una cadena que contiene solo dígitos no se convierte mágicamente 
   en un número. Cada cambio de tipo requiere una conversión explícita.

   ::
 
       >>> valor1 = 2
       >>> valor2 = "5"
       >>> total = valor1 + valor2
       Traceback (most recent call last):
         File "<stdin>", line 1, in <module>
       TypeError: unsupported operand type(s) for +: 'int' and 'str'
       >>> total = valor1 + int(valor2)
       >>> print ("El total es: " + str(total))
       7

#. **Python 3 es tipado dinámico:** significa que los objetos en tiempo de ejecución 
   (valores) tienen un tipo, a diferencia del tipado estático donde las variables tienen 
   un tipo.

   ::
 
       >>> variable = 11
       >>> print (variable, type(variable))
       11 <class 'int'>
       >>> variable = "activo"
       >>> print (variable, type(variable))
       activo <class 'str'>


#. **Python 3 soporta POO y Clases:** significa que todo el Python es un objeto. A 
   continuación se muestra el uso de la Programación Orientado a Objetos implementando 
   la técnica *herencia simple* de Clases en Python 3:

   .. literalinclude:: ../../recursos/leccion1/clases.py
       :language: python
       :lines: 7-160


----


Preparar entorno de desarrollo
------------------------------

#. Actualizar repositorios de paquetes disponibles para instalar, con el siguiente 
   comando:

    ::

        sudo apt-get update

#. Instalar dependencias mínimas necesarias, con el siguiente comando:

    ::

        sudo apt-get install python3-dev python3-pip python3-virtualenv

#. Creación de entornos virtuales Python, con los siguientes comando:

    ::

        mkdir $HOME/virtualenv && cd $_
        virtualenv --python /usr/bin/python3 python3
        source $HOME/virtualenv/python3/bin/activate

#. Crear directorio cache para paquetes Python descargados. Cuando hay latencia de 
   Internet y se requiere la instalación de paquetes de Python por un archivo 
   ``requeriments.txt`` de la herramienta ``pip`` pero la instalación falló, entonces 
   puede evitar que la herramienta ``pip`` vuelva a descargar los paquetes previamente 
   descargados, ejecutando este comando:

    ::

        mkdir -p ~/.cache/pip && mkdir ~/.pip && printf '[global]\ndownload_cache = ~/.cache/pip\n' >> ~/.pip/pip.conf

#. Gestionar paquetes Python dentro de un entorno virtual creado, con los siguientes 
   comando:

    ::

        pip install httpie
        http --help

#. Instalar paquetes Python con latencia de conexión a Internet. Cuando hay latencia 
   de Internet y se requiere la instalación de paquetes de Python, ejecute este 
   comando con el parámetro ``--timeout`` habilitado para el tiempo de espera:

    ::

        pip install -r requirements.txt --timeout 120

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
| python     | clases.py | persona                                       |
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
    :download:`tipado_dinamico.py <../../recursos/leccion1/tipado_dinamico.py>`, 
    :download:`fuertemente_tipados.py <../../recursos/leccion1/fuertemente_tipados.py>`, 
    y :download:`clases.py <../../recursos/leccion1/clases.py>`.


.. tip::
    Para ejecutar el código :file:`fuertemente_tipados.py`, :file:`tipado_dinamico.py` 
    y :file:`clases.py`, abra una consola de comando, acceda al directorio donde se 
    encuentra ambos programas:

    ::

        leccion1/
        ├── clases.py
        ├── fuertemente_tipados.py
        └── tipado_dinamico.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python fuertemente_tipados.py
        python tipado_dinamico.py
        python clases.py persona
        python clases.py supervisor


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_leccion1>` 
    del entrenamiento para ampliar su conocimiento en esta temática.

.. commets:
	http://jupyter.org
	https://ipython.org/ipython-doc/3/notebook/notebook.html#introduction
	Primeros pasos con Jupyter Notebook https://www.adictosaltrabajo.com/tutoriales/primeros-pasos-con-jupyter-notebook/
	https://github.com/Covantec/training.python_web/blob/master/notebooks/Networking%20%26%20Sockets.ipynb
