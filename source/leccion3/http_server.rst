.. _python_http_server:

Servidor HTTP
=============

Un servidor HTTP en Python esta disponible mediante la librería `http.server`_ el uso de esta
puede ejecutarse por línea de comando usando el interprete Python o desde script Python.

Archivos a servir
------------------

El `http.server`_ en Python puede servir archivos estáticos, como archivos HTML, a continuación
unos archivos:

test.html
^^^^^^^^^

.. literalinclude:: ../../recursos/leccion3/test.html
   :language: html
   :lines: 1-9

..
  index.html
  ^^^^^^^^^^

..
  .. literalinclude:: ../../recursos/leccion3/index.html
    :language: html
    :lines: 1-1571

  index2.html
  ^^^^^^^^^^^

..
  .. literalinclude:: ../../recursos/leccion3/index2.html
    :language: html
    :lines: 1-1571


.. important::
    Usted puede descargar los archivos HTML en esta sección haciendo clic en los
    siguientes enlaces:
    :download:`index2.html <../../recursos/leccion3/index2.html>`,
    :download:`index.html <../../recursos/leccion3/index.html>`,
    y :download:`test.html <../../recursos/leccion3/test.html>`.

Cree y guarde con el contenido los anteriores archivos dentro de una carpeta llamada ``leccion3``
para usar en las siguientes prácticas.


.. tip::
    La estructura de la carpeta llamada ``leccion3`` donde se encuentra los archivos HTML,
    como se muestra a continuación:

    ::

        leccion3/
        ├── index2.html
        ├── index.html
        └── test.html

----

Línea de comando
-----------------

Python le permite la ejecución en línea de comando usando el interprete Python de un servidor
HTTP de forma local.

En Python 3 usted puede desplegar un simple servidor HTTP desde línea de comando, ejecutando dentro
de la carpeta llamada ``leccion3`` el siguiente comando:

.. code-block:: console

  $ python3 -m http.server
  Serving HTTP on 0.0.0.0 port 8000 ...

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) las siguientes direcciones:

- http://localhost:8000/
- http://localhost:8000/index2.html
- http://localhost:8000/test.html

Si desea cambiar el puerto de ejecución del servidor HTTP local, ejecute dentro de la carpeta llamada
``leccion3`` el siguiente comando:

.. code-block:: console

  $ python3 -m http.server 8001
  Serving HTTP on 0.0.0.0 port 8001 ...


De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) las siguientes direcciones:

- http://localhost:8001/
- http://localhost:8001/index2.html
- http://localhost:8001/test.html

Si desea cambiar la IP de ejecución del servidor HTTP local, ejecute dentro de la carpeta llamada
``leccion3`` el siguiente comando:

.. code-block:: console

  $ python3 -m http.server 8080 --bind 127.0.0.1
  Serving HTTP on 127.0.0.1 port 8080 ...


De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) las siguientes direcciones:

- http://127.0.0.1:8080/
- http://127.0.0.1:8080/index2.html
- http://127.0.0.1:8080/test.html


De esta forma, puede usar la librería `http.server`_ para servir archivos estáticos, como archivos HTML.

----

Ejecución en script
-------------------

Python le permite la ejecución vía script de un servidor HTTP de forma local, este tiene un comportamiento
básico que le demuestra al menos dos métodos HTTP ``GET`` y ``POST``. Usted puede desplegar un simple
servidor HTTP usando las librerías :ref:`urllib <python_urllib>` y `http.server`_ con el siguiente código
fuente:

.. literalinclude:: ../../recursos/leccion3/httpserver.py
   :language: python
   :lines: 1-115


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:
    :download:`httpserver.py <../../recursos/leccion3/httpserver.py>`,
    :download:`index2.html <../../recursos/leccion3/index2.html>`,
    :download:`index.html <../../recursos/leccion3/index.html>`,
    y :download:`test.html <../../recursos/leccion3/test.html>`.


.. tip::
    Para ejecutar el código :file:`httpserver.py` abra una consola de comando,
    acceda al directorio donde se encuentra el programa y los archivos a servir:

    ::

        leccion3/
        ├── httpserver.py
        ├── index2.html
        ├── index.html
        └── test.html

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python3 httpserver.py

    Para probar el funcionamiento del script del servidor HTTP, abra otra ventana de la
    terminal de comando, donde puede usar el :ref:`cliente cURL <python_http_client_curl>`
    para hacer una petición ``GET`` al recurso :file:`test.html`, ejecutando el siguiente
    comando:

    .. code-block:: console

      $ curl -X GET 127.0.0.1:8085/test.html
      <!DOCTYPE html>
      <html>
        <head>
          <title>HTTP GET verb</title>
        </head>
        <body>
          <h1>This is a GET verb!</h1>
        </body>
      </html>

    Para probar el funcionamiento del script del servidor HTTP, abra otra ventana de la
    terminal de comando, donde puede usar el :ref:`cliente cURL <python_http_client_curl>`
    para hacer una petición ``GET`` al recurso :file:`index.html`, ejecutando el siguiente
    comando:

    .. code-block:: console

      $ curl -X GET 127.0.0.1:8085/index.html

    Para probar el funcionamiento del script del servidor HTTP, abra otra ventana de la
    terminal de comando, donde puede usar el :ref:`cliente cURL <python_http_client_curl>`
    para hacer una petición ``GET`` al recurso :file:`index2.html`, ejecutando el siguiente
    comando:

    .. code-block:: console

      $ curl -X GET 127.0.0.1:8085/index2.html

    Para probar el funcionamiento del script del servidor HTTP, abra otra ventana de la
    terminal de comando, donde puede usar el :ref:`cliente cURL <python_http_client_curl>`
    para hacer una petición ``POST`` enviando un mensaje ``Python``, ejecutando el siguiente
    comando:

    .. code-block:: console

      $ curl -X POST -d "message=Python" 127.0.0.1:8085
      <!DOCTYPE html>
      <html>
        <body>
          <h1>POST verb demo</h1>
          <p>The message is 'Python'.</p>
          <br />
          <p>This is a POST verb!</p>
        </body>
      </html>

    Para probar el funcionamiento del script del servidor HTTP, abra otra ventana de la
    terminal de comando, donde puede usar el :ref:`cliente cURL <python_http_client_curl>`
    para hacer una petición ``POST`` enviando un mensaje vació, ejecutando el siguiente
    comando:

    .. code-block:: console

      $ curl -X POST -d "message=" 127.0.0.1:8085
      <!DOCTYPE html>
      <html>
        <body>
          <h1>POST verb demo</h1>
          <p>The message is 'Default'.</p>
          <br />
          <p>This is a POST verb!</p>
        </body>
      </html>


De esta forma pudo simular el comportamiento de un servidor HTTP de forma local, con al
menos dos métodos HTTP ``GET`` y ``POST``.

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


.. disqus::

.. _`http.server`: https://docs.python.org/3/library/http.server.html
