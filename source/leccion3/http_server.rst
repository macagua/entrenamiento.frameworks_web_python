.. _python_http_server:

Servidor HTTP
=============

Un servidor HTTP en Python puede ejecutarse por linea de comando usando el interprete Python
o desde script Python.


Ejecución en linea de comando
-----------------------------

Python le permite la ejecución en linea de comando usando el interprete Python de un servidor
HTTP de forma local.


En Python 3 usted puede desplegar un simple servidor HTTP desde linea de comando, ejecutando
el siguiente comando:

::

  $ python3 -m http.server
  Serving HTTP on 0.0.0.0 port 8000 ...

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://localhost:8000/

Si desea cambiar el puerto de ejecución del servidor HTTP local, ejecute el siguiente comando:

::

  $ python3 -m http.server 8001
  Serving HTTP on 0.0.0.0 port 8001 ...


De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://localhost:8001/

Si desea cambiar la IP de ejecución del servidor HTTP local, ejecute el siguiente comando:

::

  $ python3 -m http.server 8080 --bind 127.0.0.1
  Serving HTTP on 127.0.0.1 port 8080 ...


----

Ejecución en script
-------------------

Python le permite la ejecución vía script Python de un servidor HTTP de forma local.


En Python 3 usted puede desplegar un simple servidor HTTP con el siguiente código fuente:

.. literalinclude:: ../../recursos/leccion3/httpserver.py
   :language: python
   :lines: 1-116


Archivos estáticos a servir
---------------------------

El servidorHTTP en Python puede servir archivos estáticos, como archivos HTML, como el siguiente archivo:

index.html
^^^^^^^^^^

.. literalinclude:: ../../recursos/leccion3/index.html
   :language: html
   :lines: 1-1571


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:
    :download:`httpserver.py <../../recursos/leccion3/httpserver.py>`,
    y :download:`index.html <../../recursos/leccion3/index.html>`.


.. tip::
    Para ejecutar el código :file:`httpserver.py` abra una consola de comando,
    acceda al directorio donde se encuentra ambos programas:

    ::

        leccion3/
        ├── httpserver.py
        └── index.html

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python httpserver.py


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
