.. _python_flask_introduccion:

Introducción
============

`Flask <https://flask.palletsprojects.com/en/2.2.x/>`_ es un framework minimalista
escrito en Python que permite crear aplicaciones web rápidamente
y con un mínimo número de líneas de código. Está basado en la
especificación `WSGI <https://wsgi.readthedocs.io/en/latest/>`_ de
`Werkzeug <https://palletsprojects.com/p/werkzeug/>`_ y el motor
de plantillas `Jinja2 <https://palletsprojects.com/p/jinja/>`_
con licencia BSD.

.. figure:: ../_static/images/flask-framework.png
  :class: image-inline
  :alt: Flask framework
  :align: center

  Flask framework

Características
---------------

- Contiene servidor de desarrollo y depurador.

- Soporte integrado para pruebas unitarias.

- Envío de request RESTful.

- Utiliza plantillas de Jinja2.

- Soporte para cookies seguras (sesiones del lado del cliente).

- 100% compatible con WSGI 1.0.

- Basado en Unicode.

- Amplia documentación.

- Compatibilidad con Google App Engine.

- Extensiones disponibles para mejorar las características deseadas.


Model View Controller
---------------------

Del Ingles Model View Controller - MVC, el Modelo-vista-controlador,
es un patrón de arquitectura de software, que separa los datos y la
lógica de negocio de una aplicación de su representación y el módulo
encargado de gestionar los eventos y las comunicaciones. Para ello MVC
propone la construcción de tres componentes distintos que son el modelo,
la vista y el controlador, es decir, por un lado define componentes para
la representación de la información, y por otro lado para la interacción
del usuario.

Este patrón de arquitectura de software se basa en las ideas
de reutilización de código y la separación de conceptos, características
que buscan facilitar la tarea de desarrollo de aplicaciones y su posterior
mantenimiento.

El patrón de diseño MVC es soportado en Flask se divide en tres capas:

Capa Modelo
^^^^^^^^^^^

- `Tutorial SQLAlchemy (Capa modelo) <https://docs.sqlalchemy.org/en/20/orm/tutorial.html>`_.

- `Select, Insert, Delete - Flask-SQLAlchemy) <https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/>`_.

Capa Vista
^^^^^^^^^^

- `Sistema de plantillas Jinja2 (Capa vista) <https://jinja.palletsprojects.com/en/2.10.x/templates/>`_.

Capa Controlador
^^^^^^^^^^^^^^^^

- `Documentación Flask (Capa Controlador) <https://flask.palletsprojects.com/en/2.2.x/>`_.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
