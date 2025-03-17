.. _python_flask_crud_api:

API REST
=========

El objeto de esta sección es hacer un demostración local de `API REST`_
en :doc:`Flask <./index>`.


Requisitos previos
------------------

Para trabajar una aplicación ``Flask`` requiere instalar las siguientes
librerías:

- :doc:`Flask <./instalacion>` framework.

- :ref:`SQLAlchemy <python_sqlalchemy>`.

- Motor de base de datos :ref:`SQLite <python_sqlite3_instalar>`.


Estructura de proyecto
----------------------

Crear estructura de proyecto ``Flask``, con los siguientes comando:

::

    mkdir -p ~/proyectos/flask/api/ && cd $_

Cree módulo Python llamado :file:`app.py` dentro del directorio :file:`~/proyectos/flask/api`

::

    nano app.py


Agregue el siguiente contenido al archivo :file:`~/proyectos/flask/api/app.py`.

.. literalinclude:: ../../recursos/leccion6/flask-api/app.py
   :language: python
   :lines: 1-147


----


Para ejecutar el código del proyecto llamado ``api`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── flask/
        └── api/
            └── app.py

Si tiene la estructura de archivo previa, entonces puede continuar los procesos de instalación,
configuración y ejecución del código fuente.


----


Instalar paquetes Python
------------------------

Para instalar el framework ``Flask`` usando la herramienta :ref:`pip <python_entorno_desarrollo_pip>`,
ejecute el siguiente comando:

.. code-block:: console

    pip3 install Flask==3.1.0 Flask-SQLAlchemy==3.1.1 SQLAlchemy==2.0.38


Ejecutar aplicación Flask
-------------------------

Para ejecutar aplicación Web Flask, con el siguiente comando:

.. code-block:: console

    flask run


Abra una nueva ventana de terminal para probar la API utilizando un cliente HTTP
como comando `curl <https://curl.se/>`_.


----


Hacer peticiones
-----------------

El comando ``curl`` le permite probar rápidamente una API desde el terminal sin
la necesidad de tener que descargar una aplicación específica.

request GET con response 200
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    curl -X GET http://127.0.0.1:5000/

El comando anterior muestra cómo realizar una petición ``GET`` para obtener los usuarios
registrados por defecto en la base de datos como una operación ``READ`` en una aplicación
``CRUD``.

request POST formato JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    curl -X POST http://localhost:5000/create -H "Content-Type: application/json" -d '{"name": "John Doe", "address": "123 Main St"}'

El comando anterior muestra como realizar una petición ``POST`` con formato ``json``.
Es decir, en realidad está insertando un nuevo usuario en la base de datos como una operación
``CREATE``. en una aplicación ``CRUD``.

request GET con response 200
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    curl -X GET http://127.0.0.1:5000/detail/4

El comando anterior muestra cómo realizar una solicitud ``GET`` para obtener información detallada
sobre del usuario con el id ``4`` como una operación ``READ`` en una aplicación ``CRUD``.

request PUT formato JSON
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    curl -X PUT http://127.0.0.1:5000/update/4 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "address": "456 Elm St"}'

El comando anterior muestra como realizar una petición ``PUT`` con formato ``json``.
Es decir, se está actualizando la información del usuario con el id ``4`` como un ``UPDATE``.
en una aplicación ``CRUD``.

request DELETE
^^^^^^^^^^^^^^^

.. code-block:: console

    curl -X DELETE http://127.0.0.1:5000/delete/4

El comando anterior muestra como realizar una petición ``DELETE`` con formato ``json``.
Es decir, en realidad estás borrando la información del usuario con el id ``4`` como
operación ``DELETE`` de una aplicación ``CRUD``.

De esta forma hago las peticiones a la API usando el comando :ref:`curl <python_http_client_curl>`.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`app.py <../../recursos/leccion6/flask-api/app.py>`.

.. note::
    El código ejemplo usado puede encontrarlo en: https://github.com/macagua/example.flask.api


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`API REST`: https://es.wikipedia.org/wiki/API_REST
