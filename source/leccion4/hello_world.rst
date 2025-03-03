.. _python_wsgi_hello_world:

Hello World en WSGI
===================

El objeto de esta sección es hacer un demostración local de
`Hello World <https://es.wikipedia.org/wiki/Hola_mundo>`_ en
:ref:`WSGI <python_leccion4>`.

.. _python_wsgi_helloworld_request_get:

Request GET
-----------

En pocas palabras, una aplicación compatible con :ref:`WSGI <python_leccion4>` debe proporcionar
una (función, clase) invocable que acepte un diccionario ``environ`` y una
función ``start_response``.

Para una comparación familiar de `PHP`_, puede pensar en el diccionario ``environ``
como una combinación de `$_SERVER`_, `$_GET`_ y `$_POST`_, con procesamiento
adicional requerido. Se espera que este invocable invoque la función ``start_response``
con el código de respuesta/datos de encabezado deseados, y luego devuelva un
byte iterable con el cuerpo de la respuesta.

.. literalinclude:: ../../recursos/leccion4/wsgi_hello_world_get_request.py
   :language: python
   :lines: 1-52


.. tip::
    Para ejecutar el código :file:`wsgi_hello_world_get_request.py` y :file:`wsgi_hello_world_post_request.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── wsgi/
            └── wsgi_hello_world_get_request.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 wsgi_hello_world_get_request.py


De esta forma puede una aplicación web ``WSGI`` simple que maneja una petición ``GET`` .


----


.. _python_wsgi_helloworld_request_post:

Request POST
------------

Ahora que esta familiarizado con la estructura básica de una aplicación
compatible con :ref:`WSGI <python_leccion4>`, ahora podemos experimentar
con un ejemplo más práctico. A continuación, proporcionamos al cliente un
formulario simple que publica un campo llamado ``name`` proporcionado para
que la aplicación lo salude en consecuencia.


.. literalinclude:: ../../recursos/leccion4/wsgi_hello_world_post_request.py
   :language: python
   :lines: 1-76

Aunque algo detallado, ha podido crear una aplicación web simple que maneja los
datos ``POST`` suministrados.


.. tip::
    Para ejecutar el código :file:`wsgi_hello_world_get_request.py` y :file:`wsgi_hello_world_post_request.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── wsgi/
            └── wsgi_hello_world_post_request.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 wsgi_hello_world_post_request.py

De esta forma puede una aplicación web ``WSGI`` simple que maneja una petición ``POST``.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`wsgi_hello_world_get_request.py <../../recursos/leccion4/wsgi_hello_world_get_request.py>`.

    - :download:`hello_world_post_request.py <../../recursos/leccion4/wsgi_hello_world_post_request.py>`.


----


Estos son los bloques de construcción muy simplificados utilizados en :ref:`framework web <python_leccion5_frameworks_web_populares>`
populares como :ref:`Flask <python_leccion6>` y :ref:`Django <python_leccion7>`.

De esta forma ha aprendido a crear aplicaciones web ``WSGI`` que maneja peticiones ``GET`` y ``POST``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`PHP`: https://www.php.net/
.. _`$_SERVER`: https://www.php.net/manual/es/reserved.variables.server.php
.. _`$_GET`: https://www.php.net/manual/es/reserved.variables.get.php
.. _`$_POST`: https://www.php.net/manual/es/reserved.variables.post.php
