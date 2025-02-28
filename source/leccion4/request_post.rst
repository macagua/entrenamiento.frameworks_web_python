.. _python_wsgi_request_post:

Petición POST
=============

La petición ``POST`` en :ref:`WSGI <python_leccion4>` es una forma de enviar datos al servidor
a través de la URL.

Cuando el método de solicitud es ``POST``, la cadena de consulta se enviará en el cuerpo de
la solicitud HTTP en lugar de en la URL. El cuerpo de la solicitud se encuentra en el
archivo ``wsgi.input`` proporcionado por el servidor :ref:`WSGI <python_leccion4>` como
variable de entorno.

Es necesario conocer el tamaño del cuerpo de la respuesta como un número entero para leerlo
desde ``wsgi.input``. El `PEP 3333 <https://peps.python.org/pep-3333/>`_ dice que la variable
``CONTENT_LENGTH``, que contiene el tamaño del cuerpo, puede estar vacía o faltante, así que
léala en un bloque ``try`` / ``except``.

La etiqueta HTML ``form`` en este script indica al navegador que realice una solicitud ``POST``
(``method="post"``):

.. literalinclude:: ../../recursos/leccion4/wsgi_post_request.py
   :language: python
   :lines: 1-114


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/wsgi_post_request.py>`.


.. tip::
    Para ejecutar el código :file:`wsgi_post_request.py`, abra una consola de
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente
    comando:

    .. code-block:: console

        python3 wsgi_post_request.py

    De esta forma, una vez ejecutado el comando, el servidor estará atendiendo peticiones,
    puede abrir desde con su navegador Web favorito (Mozilla Firefox, Google Chrome, etc)
    la siguiente dirección http://localhost:8080

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::
