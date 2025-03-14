.. _python_wsgi_variables_entorno:

Variables de entorno
====================

El servidor rellena el diccionario de entorno con variables similares a
`CGI`_ en cada solicitud del cliente. Es script generará todo el diccionario:

.. literalinclude:: ../../recursos/leccion4/wsgi_print_environment.py
   :language: python
   :lines: 1-51

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`wsgi_print_environment.py <../../recursos/leccion4/wsgi_print_environment.py>`.


.. tip::
    Para ejecutar el código :file:`wsgi_print_environment.py`, abra una consola de
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente
    comando:

    .. code-block:: console

        python3 wsgi_print_environment.py

    El servidor estará atendiendo peticiones en la dirección en http://localhost:8080


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`CGI`: https://docs.python.org/es/3/library/cgi.html
