.. _python_wsgi_variables_entorno:

Variables de entorno
====================

El servidor rellena el diccionario de entorno con variables similares a
CGI en cada solicitud del cliente. generará todo el diccionario:This script



.. literalinclude:: ../../recursos/leccion4/print_environment.py
   :language: python
   :lines: 1-44

Para ejecutar este script, guárdelo como el nombre, ``print_environment.py``
abra la terminal, navegue hasta el directorio donde se guardó y escriba
``python3 environment.py`` en la línea de comando.

El servidor estará atendiendo peticiones en la direccion en http://localhost:8051


.. todo::
    TODO Terminar de escribir la sección "Introducción a WSGI".


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
