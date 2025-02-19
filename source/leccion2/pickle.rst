.. _python_modulo_pickle:

Serialización de objetos
========================

.. note::
    **Propósito:** es una libraría para implementa protocolos binarios para serializar
    y deserializar una estructura de objetos Python, es decir, convertirlos en un flujo
    de bytes que se puede almacenar o transmitir por una red.

La *serialización* es el proceso de convertir un objeto en una secuencia de bytes
para almacenarlo o transmitirlo a la memoria, a una base de datos o a un archivo.
Su propósito principal es guardar el estado de un objeto para poder volver a
crearlo cuando sea necesario. El proceso inverso se denomina *deserialización*.

Por ejemplo, guardar una :ref:`lista <python_list>` de Python en un archivo de texto o base de datos,
y luego cargarlo cuando sea necesario, para ser tratado con su tipo de datos.

Formatos comunes entre los distintos lenguajes de programación incluyen XML y JSON.

Python ofrece tres módulos diferentes en la biblioteca estándar que le permiten serializar y deserializar objetos:

.. _python_pickle:

pickle
------

.. todo::
    TODO Terminar de escribir esta sección.


.. _python_pickle_serializar:

Serializar
^^^^^^^^^^

.. todo::
    TODO terminar de escribir esta sección.


.. _python_pickle_deserializar:

Deserializar
^^^^^^^^^^^^

.. todo::
    TODO terminar de escribir esta sección.


.. _python_pickle_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``pickle`` para operaciones CRUD en un archivo de registros serializados:

.. literalinclude:: ../../recursos/leccion2/pickle/main.py
    :language: python
    :linenos:
    :lines: 1-202

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`main.py <../../recursos/leccion2/pickle/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    ::

        leccion2/
        └── pickle/
            └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 main.py

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en un archivo serializado de objetos python ``pickle``.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`

.. _`pickle`: https://docs.python.org/es/3.11/library/pickle.html
