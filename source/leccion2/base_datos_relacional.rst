.. _python_base_datos_relacional:

Base de datos relacional
========================

Es un tipo de :doc:`bases de datos <./index>`
(BD) que cumple con el modelo relacional (el modelo más utilizado
actualmente para implementar las BD ya planificadas).

El sistema de gestión de bases de datos relacionales o Relational
Database Management System (RDBMS), es el software utilizado para
mantener las bases de datos relacionales.

Structured Query Language
-------------------------

Por defecto todos los sistemas de bases de datos relacionales utilizan
el *Structured Query Language* (`SQL <https://es.wikipedia.org/wiki/SQL>`_)
para consultar y mantener la base de datos.

Crear una tabla
^^^^^^^^^^^^^^^

Si requiere crear una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sistema/sistema.sql
    :language: sql
    :linenos:
    :lines: 47-58


Insertar registro en una tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 2-7


Consultar registros de tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 10-11


Actualizar registro de tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 14-15


Eliminar registro de tabla
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion2/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 18


Asi de esta forma puede crear una tabla, ingresar, consultar, actualizar y eliminar
registro a dicha tabla.

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion2/sistema/sistema_data.sql>`.


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion11>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
