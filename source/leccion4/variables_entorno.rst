.. _python_wsgi_variables_entorno:

Variables de entorno
====================

El servidor rellena el diccionario de entorno con variables similares a
`CGI`_ en cada solicitud del cliente. Es script generará todo el diccionario:

.. literalinclude:: ../../recursos/leccion4/print_environment.py
   :language: python
   :lines: 1-44


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/print_environment.py>`.


.. tip::
    Para ejecutar el código :file:`print_environment.py`, abra una consola de
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente
    comando:

    .. code-block:: console

        python print_environment.py

    El servidor estará atendiendo peticiones en la dirección en http://localhost:8051

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`CGI`: https://docs.python.org/es/3/library/cgi.html
