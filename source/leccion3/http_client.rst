.. _python_http_client:

Cliente HTTP
============

Python le permite escribir y ejecutar vía script Python de un cliente HTTP de forma local.

Ejecución en script
-------------------

Usted puede escribir y ejecutar un simple cliente HTTP usando la librería :ref:`http.client <python_http_client>`
desde línea de comando, con el siguiente código fuente:

.. literalinclude:: ../../recursos/leccion3/httpclient.py
   :language: python
   :lines: 1-56

Guarde el archivo :file:`httpclient.py` y ejecutándolo con el siguiente comando:

.. code-block:: console

  $ python3 httpclient.py


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:
    :download:`httpclient.py <../../recursos/leccion3/httpclient.py>`.


.. tip::
    Para ejecutar el código :file:`httpclient.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    ::

        leccion3/
        └── httpclient.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 httpclient.py


----

.. _python_http_external_clients:

Clientes externos
------------------

Existen varias herramientas clientes del :ref:`protocolo HTTP <python_introduccion_http>`:

- :ref:`requests <python_http_client_requests>`.

- :ref:`cURL <python_http_client_curl>`.

- :ref:`httpie <python_http_client_httpie>`.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html



..
  .. disqus::
