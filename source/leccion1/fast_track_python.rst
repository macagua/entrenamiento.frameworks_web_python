.. _python_fast_track_python:

Vía rápida en Python
====================

Esta práctica ofrece una introducción rápida a la programación en Python:


Fuertemente tipado
------------------

Python 3 es fuertemente *tipado*, esto significa que el tipo de valor no cambia
repentinamente. Una cadena que contiene solo dígitos no se convierte mágicamente
en un número. Cada cambio de tipo requiere una conversión explícita.

.. code-block:: console
    :class: no-copy

    >>> valor1 = 2
    >>> valor2 = "5"
    >>> total = valor1 + valor2
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> total = valor1 + int(valor2)
    >>> total
    7
    >>> print("El total es: " + str(total))
    El total es: 7

..
    .. ipython::

        In [1]: valor1 = 2

        In [2]: valor2 = "5"

        In [3]: total = valor1 + valor2
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[3], line 1
        ----> 1 total = valor1 + valor2

        TypeError: unsupported operand type(s) for +: 'int' and 'str'

        In [4]: total = valor1 + int(valor2)

        In [5]: print("El total es: " + str(total))
        El total es: 7

        In [6]: print(f"El total es: {str(total)}")
        El total es: 7


Tipado dinámico
---------------

Python 3 es *tipado* dinámico, significa que los objetos en tiempo de ejecución
(valores) tienen un tipo, a diferencia del *tipado* estático donde las variables
tienen un tipo.

.. code-block:: console
    :class: no-copy

    >>> variable = 11
    >>> print(variable, type(variable))
    11 <class 'int'>
    >>> variable = "activo"
    >>> print(variable, type(variable))
    activo <class 'str'>

..
    .. ipython::

        In [1]: variable = 11

        In [2]: print(variable, type(variable))
        11 <class 'int'>

        In [3]: variable = "activo"

        In [4]: print(variable, type(variable))
        activo <class 'str'>

POO y Clases
------------

Python 3 soporta POO y Clases, significa que todo el Python es un objeto. A
continuación se muestra el uso de la Programación Orientado a Objetos implementando
la técnica *herencia simple* de Clases en Python 3:

.. literalinclude:: ../../recursos/leccion1/clases.py
   :language: python
   :linenos:
   :lines: 4-179


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`tipado_dinamico.py <../../recursos/leccion1/tipado_dinamico.py>`.

    - :download:`fuertemente_tipados.py <../../recursos/leccion1/fuertemente_tipados.py>`.

    - :download:`clases.py <../../recursos/leccion1/clases.py>`.


.. tip::
    Para ejecutar el código :file:`fuertemente_tipados.py`, :file:`tipado_dinamico.py`
    y :file:`clases.py`, abra una consola de comando, acceda al directorio donde se
    encuentra los programas:

    .. code-block:: console
        :class: no-copy

        leccion1/
        ├── clases.py
        ├── fuertemente_tipados.py
        └── tipado_dinamico.py

    Si tiene la estructura de archivo previa, entonces ejecute los siguientes comandos,
    cada uno por separado dentro de una consola de comandos:

    .. code-block:: console

        python3 fuertemente_tipados.py

    .. code-block:: console

        python3 tipado_dinamico.py

    .. code-block:: console

        python3 clases.py persona

    .. code-block:: console

        python3 clases.py supervisor


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion1>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. commets:
    http://jupyter.org
    https://ipython.org/ipython-doc/3/notebook/notebook.html#introduction
    Primeros pasos con Jupyter Notebook https://www.adictosaltrabajo.com/tutoriales/primeros-pasos-con-jupyter-notebook/
    https://github.com/Covantec/training.python_web/blob/master/notebooks/Networking%20%26%20Sockets.ipynb
