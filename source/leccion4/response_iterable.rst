.. _python_wsgi_response_iterable:

Respuesta Iterable
==================

Si el último script :ref:`wsgi_print_environment.py <python_wsgi_variables_entorno>`
funcionó, cambie la línea de retorno:

.. code-block:: python

    return [response_body.encode("utf-8")]

por la siguiente linea:

.. code-block:: python

    return response_body.encode("utf-8")

.. important::
    Luego ejecútalo el script de nuevo, el servidor estará atendiendo peticiones
    en la dirección en http://localhost:8080

En una máquina más antigua es posible notar que es más lenta. Lo que sucede
es que el servidor iteraba sobre la cadena y enviaba un solo byte a la vez
al cliente. Así que no olvide envolver la respuesta en un mejor rendimiento
iterable como una lista.

Si el iterable produce más de una cadena, la longitud del cuerpo de la
response será la suma de todas las longitudes de la cadena, como en este script:

.. literalinclude:: ../../recursos/leccion4/wsgi_response_iterable.py
   :language: python
   :lines: 1-61


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`wsgi_response_iterable.py <../../recursos/leccion4/wsgi_response_iterable.py>`.


.. tip::
    Para ejecutar el código :file:`wsgi_response_iterable.py`, abra una consola de
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente
    comando:

    .. code-block:: console

        python3 wsgi_response_iterable.py

    El servidor estará atendiendo peticiones en la dirección en http://localhost:8051


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
