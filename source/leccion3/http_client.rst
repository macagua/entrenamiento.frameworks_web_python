.. _python_http_client:

Cliente HTTP
============

Ejecución en script
-------------------

Python le permite escribir y ejecutar vía script Python de un servidor HTTP de forma local.


Usted puede escribir y ejecutar un simple cliente HTTP desde linea de comando,
con el siguiente codigo fuente:

.. literalinclude:: ../../recursos/leccion3/httpclient.py
   :language: python
   :lines: 1-51

Guarde el archivo :file:`httpclient.py` y ejecutandolo con el siguiente comando:

.. code-block:: console

  $ python httpclient.py


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:
    :download:`httpclient.py <../../recursos/leccion3/httpclient.py>`.


.. tip::
    Para ejecutar el código :file:`httpclient.py`, abra una consola de comando,
    acceda al directorio donde se encuentra ambos programas:

    ::

        leccion3/
        └── httpclient.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 httpclient.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
