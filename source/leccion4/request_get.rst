.. _python_wsgi_request_get:

Solicitud del GET
=================

Ejecute el script :ref:`print_environment.py <python_wsgi_variables_entorno>` nuevamente
y esta vez llámelo así:

::

    http://localhost:8051/?age=10&hobbies=software&hobbies=tunning

Compruebe las variables ``QUERY_STRING`` y las ``REQUEST_METHOD`` en el diccionario ``environ``:

.. code-block:: console

    QUERY_STRING: age=10&hobbies=software&hobbies=tunning
    REQUEST_METHOD: GET

Cuando el método de solicitud es ``GET`` las variables del formulario se enviarán en la URL en
la parte llamada cadena de consulta, es decir, todo lo que se encuentra después del caracter
``?`` en la URL.

Observe que la variable ``hobbies`` aparece dos veces. Puede ocurrir cuando hay casillas de
verificación en el formulario o cuando el usuario escribe la misma variable más de una vez
en la URL.

Es posible escribir código para analizar la cadena de consulta y recuperar esos valores, pero
es más fácil usar la función ``cgi.parse_qs()`` que devuelve un diccionario con los valores
como `listas`_.

Siempre tenga cuidado con la entrada del usuario. Desinfectarlo para evitar la inyección de
secuencias de comandos. La función ``cgi.escape()`` se puede utilizar para eso.

La etiqueta HTML ``form`` en este script indica al navegador que realice una solicitud GET
(``method="get"``):

.. literalinclude:: ../../recursos/leccion4/get_request.py
   :language: python
   :lines: 1-80


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/get_request.py>`.


.. tip::
    Para ejecutar el código :file:`get_request.py`, abra una consola de
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente
    comando:

    .. code-block:: console

        python3 get_request.py

    El servidor estará atendiendo peticiones en la dirección en http://localhost:8080

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`listas`: https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion3/tipo_listas.html
