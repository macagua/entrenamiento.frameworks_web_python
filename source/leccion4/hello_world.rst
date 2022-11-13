.. _python_wsgi_hello_world:

Hello World en WSGI
===================

El objeto de esta sección es hacer un demostración local de
`Hello World <https://es.wikipedia.org/wiki/Hola_mundo>`_ en WSGI.

.. _python_wsgi_helloworld_request_get:

Solicitud del GET
-----------------

En pocas palabras, una aplicación compatible con WSGI debe proporcionar
una (función, clase) invocable que acepte un diccionario ``environ`` y una
función ``start_response``.

Para una comparación familiar de PHP, puede pensar en el diccionario ``environ``
como una combinación de `$_SERVER`_, `$_GET`_ y `$_POST`_, con procesamiento
adicional requerido. Se espera que este invocable invoque la función ``start_response``
con el código de respuesta/datos de encabezado deseados, y luego devuelva un
byte iterable con el cuerpo de la respuesta.

.. literalinclude:: ../../recursos/leccion4/hello_world_get_request.py
   :language: python
   :lines: 1-28

.. _python_wsgi_helloworld_request_post:

Solicitud del POST
------------------

Ahora que esta familiarizado con la estructura básica de una aplicación
compatible con WSGI, ahora podemos experimentar con un ejemplo más práctico.
A continuación, proporcionamos al cliente un formulario simple que publica un
campo llamado ``name`` proporcionado para que la aplicación lo salude en
consecuencia.


.. literalinclude:: ../../recursos/leccion4/hello_world_post_request.py
   :language: python
   :lines: 1-56

Aunque algo detallado, ha podido crear una aplicación web simple que maneja los
datos ``POST`` suministrados utilizando la clase ``FieldStorage`` de los módulos
`CGI`_. Estos son los bloques de construcción muy simplificados utilizados en marcos
populares como :ref:`Flask <python_leccion6>` y :ref:`Django <python_leccion7>`.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`hello_world_get_request.py <../../recursos/leccion4/hello_world_get_request.py>`
    y :download:`hello_world_post_request.py <../../recursos/leccion4/hello_world_post_request.py>`.


.. tip::
    Para ejecutar el código :file:`hello_world_get_request.py` y :file:`hello_world_post_request.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    ::

        leccion4/
        ├── hello_world_get_request.py
        └── hello_world_post_request.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python3 hello_world_get_request.py
        python3 hello_world_post_request.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`$_SERVER`: https://www.php.net/manual/es/reserved.variables.server.php
.. _`$_GET`: https://www.php.net/manual/es/reserved.variables.get.php
.. _`$_POST`: https://www.php.net/manual/es/reserved.variables.post.php
.. _`CGI`: https://docs.python.org/es/3/library/cgi.html
