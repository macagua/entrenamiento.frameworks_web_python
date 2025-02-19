.. _python_wsgi_request_get:

Solicitud del GET
=================

Ejecute el script :ref:`print_environment.py <python_wsgi_variables_entorno>` nuevamente
y esta vez llámalo así:

::

    http://localhost:8051/?age=10&hobbies=software&hobbies=tunning

Compruebe las variables ``QUERY_STRING`` y las ``REQUEST_METHOD`` en el diccionario ``environ``:

.. code-block:: console

    QUERY_STRING: age=10&hobbies=software&hobbies=tunning
    REQUEST_METHOD: GET

Cuando el método de solicitud es ``GET`` las variables del formulario se enviarán en la URL en
la parte llamada cadena de consulta, es decir, todo lo que se encuentra después del carácter
``?`` en la URL.

Observe que la variable ``hobbies`` aparece dos veces. Puede ocurrir cuando hay casillas de
verificación en el formulario o cuando el usuario escribe la misma variable más de una vez
en la URL.

Es posible escribir código para analizar la cadena de consulta y recuperar esos valores, pero
es más fácil usar la función ``parse_qs()`` que devuelve un diccionario con los valores
como `listas`_.

Siempre tenga cuidado con la entrada de datos del usuario. Debe desinfectar los valores enviados
por el formulario para evitar la inyección de secuencias de comandos maliciosos. La función
``escape()`` se puede utilizar para eso.

La etiqueta HTML ``form`` en este script indica al navegador que realice una solicitud ``GET``
(``method="get"``):

.. literalinclude:: ../../recursos/leccion4/wsgi_get_request.py
   :language: python
   :lines: 1-96


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/wsgi_get_request.py>`.


.. tip::
    Para ejecutar el código :file:`wsgi_get_request.py`, abra una consola de
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente
    comando:

    .. code-block:: console

        python3 wsgi_get_request.py

    De esta forma, una vez ejecutado el comando, el servidor estará atendiendo peticiones,
    puede abrir desde con su navegador Web favorito (Mozilla Firefox, Google Chrome, etc)
    la siguiente dirección http://localhost:8080

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`listas`: https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion3/tipo_listas.html
