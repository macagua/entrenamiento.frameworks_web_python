.. _python_flask_crud_api:

API REST
=========

El objeto de esta sección es hacer un demostración local de
`API REST <https://es.wikipedia.org/wiki/API_REST>`_ en ``Flask``.


Requisitos previos
------------------

Para trabajar una aplicación ``Flask`` requiere instalar la siguiente
librería:

- :doc:`Flask <./instalacion>` framework.


Estructura de proyecto
----------------------

Crear estructura de proyecto ``Flask``, con los siguientes comando:

::

    $ mkdir -p ~/projects/flask-api/ && cd $_

Cree módulo Python llamado :file:`app.py` dentro del directorio :file:`~/projects/flask-api`

::

    $ nano app.py


Agregue el siguiente contenido al archivo :file:`~/projects/flask-api/app.py`.

.. literalinclude:: ../../recursos/leccion6/flask-api/app.py
   :language: python
   :lines: 1-147


Ejecutar aplicación Flask
-------------------------

Para ejecutar aplicación Web Flask, con el siguiente comando:

::

    $ flask run


Open a new terminal windows for testing the API using a HTTP client
as `curl <https://curl.se/>`_ command.


----


Hacer peticiones
=================

El comando ``curl`` le permite probar rápidamente una API desde el terminal sin
la necesidad de tener que descargar una aplicación específica.

request GET con response 200
-----------------------------

.. code-block:: console

    $ curl -X GET http://127.0.0.1:5000/

El comando anterior muestra cómo realizar una petición ``GET`` para obtener los usuarios
registrados por defecto en la base de datos como una operación ``READ`` en una aplicación
``CRUD``.

request POST formato JSON
--------------------------

.. code-block:: console

    $ curl -X POST http://localhost:5000/create -H "Content-Type: application/json" -d '{"name": "John Doe", "address": "123 Main St"}'

El comando anterior muestra como realizar una petición ``POST`` con formato ``json``.
Es decir, en realidad está insertando un nuevo usuario en la base de datos como una operación
``CREATE``. en una aplicación ``CRUD``.

request GET con response 200
-----------------------------

.. code-block:: console

    $ curl -X GET http://127.0.0.1:5000/detail/4

El comando anterior muestra cómo realizar una solicitud ``GET`` para obtener información detallada
sobre del usuario con el id ``4`` como una operación ``READ`` en una aplicación ``CRUD``.

request PUT formato JSON
-------------------------

.. code-block:: console

    $ curl -X PUT http://127.0.0.1:5000/update/4 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "address": "456 Elm St"}'

El comando anterior muestra como realizar una petición ``PUT`` con formato ``json``.
Es decir, se está actualizando la información del usuario con el id ``4`` como un ``UPDATE``.
en una aplicación ``CRUD``.

request DELETE
---------------

.. code-block:: console

    $ curl -X DELETE http://127.0.0.1:5000/delete/4

El comando anterior muestra como realizar una petición ``DELETE`` con formato ``json``.
Es decir, en realidad estás borrando la información del usuario con el id ``4`` como
operación ``DELETE`` de una aplicación ``CRUD``.

De esta forma hago las peticiones a la API usando el comando ``curl``.

.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/macagua/example.flask.api


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
