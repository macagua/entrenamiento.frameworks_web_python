.. _python_django_hello_world:

Hello World
===========

El objeto de esta sección es hacer un demostración local de
`Hello World <https://es.wikipedia.org/wiki/Hola_mundo>`_ en Django.


Requisitos previos
------------------

Para trabajar una aplicación Django requiere instalar la siguiente
librería:

- :doc:`Django <./instalacion>` framework.


Estructura de proyecto
----------------------

Crear estructura de proyecto Django, con los siguientes comando:

::

    $ cd ~/
    $ django-admin startproject helloworld

Este comando crea un directorio el directorio :file:`helloworld` con varios
archivos dentro, a continuación se muestra:

::

    helloworld/
        manage.py
        helloworld/
            __init__.py
            settings.py
            urls.py
            wsgi.py

Si quiere entender para que funciona cada archivo consulte la
`documentación <https://docs.djangoproject.com/en/2.1/intro/tutorial01/#creating-a-project>`_.


Cree modulo Python llamado :file:`views.py` dentro del directorio
:file:`~/helloworld/helloworld`

::

    $ nano ~/helloworld/helloworld/views.py


Agregue el siguiente contenido al archivo :file:`~/helloworld/helloworld/views.py`.

.. literalinclude:: ../../recursos/leccion7/django-helloworld/helloworld/views.py
   :language: python
   :lines: 1-4


Adapte modulo Python llamado :file:`urls.py` dentro del directorio
:file:`~/helloworld/helloworld`

::

    $ nano ~/helloworld/helloworld/urls.py


Agregue el siguiente contenido al archivo :file:`~/helloworld/helloworld/urls.py`.

.. literalinclude:: ../../recursos/leccion7/django-helloworld/helloworld/urls.py
   :language: python
   :lines: 1-25


Ejecutar aplicación Django
--------------------------

Para ejecutar aplicación Web Django, con el siguiente comando:

::

    $ python3 manage.py runserver

Abrir en navegador favorito la siguiente dirección http://127.0.0.1:8000/

.. figure:: ../_static/images/django-helloworld.png
  :class: image-inline
  :alt: Hello World en Django
  :align: center

  Hello World en Django

Mostrara un mensaje **Hello, World!**, como la figura anterior.


.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/django-ve/django-helloworld


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
