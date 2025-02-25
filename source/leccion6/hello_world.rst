.. _python_flask_hello_world:

Hello World
===========

El objeto de esta sección es hacer un demostración local de
`Hello World <https://es.wikipedia.org/wiki/Hola_mundo>`_ en Flask.


Requisitos previos
------------------

Para trabajar una aplicación Flask requiere instalar la siguiente
librería:

- :doc:`Flask <./instalacion>` framework.


Estructura de proyecto
----------------------

Crear estructura de proyecto Flask, con los siguientes comando:

::

    $ mkdir -p ~/projects/flask-helloworld/ && cd $_

Cree módulo Python llamado :file:`hello.py` dentro del directorio :file:`~/projects/flask-helloworld`

::

    $ nano hello.py


Agregue el siguiente contenido al archivo :file:`~/projects/flask-helloworld/hello.py`.

.. literalinclude:: ../../recursos/leccion6/flask-helloworld/hello.py
   :language: python
   :lines: 1-9


Ejecutar aplicación Flask
-------------------------

Para ejecutar aplicación Web Flask, con el siguiente comando:

::

    $ flask --app hello run

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:5000

.. figure:: ../_static/images/flask-hello-world.png
  :class: image-inline
  :alt: Hello World en Flask
  :align: center

  Hello World en Flask

Mostrará un mensaje **Hello, World!**, como la figura anterior.


.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/macagua/example.flask.helloworld


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
