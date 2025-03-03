.. _python_django_admin_user_management:

Usuarios con el Django Admin
=============================

Práctica de gestionar usuarios y permisos con la interfaz web del ``Django Admin`` de ``Django``.

Prácticas en ``Django``.


Requisitos previos
------------------

Para trabajar una aplicación ``Django`` requiere instalar la siguiente
librería:

- Requisitos previos para :doc:`Django <./instalacion>` framework.


Estructura de proyecto
----------------------

Crear estructura de proyecto ``Django``, con el siguiente comando:

.. code-block:: console

    mkdir -p ~/proyectos/django/acmeweb && cd $_

Ejecutar el comando ``django-admin`` dentro del directorio
:file:`~/proyectos/django`, con el siguiente comando:

.. code-block:: console

    django-admin startproject acmeweb && cd $_


Este comando crea un directorio el directorio :file:`acmeweb` con varios
archivos dentro, a continuación se muestra:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── django/
        └── acmeweb/
            ├── acmeweb/
            │   ├── asgi.py
            │   ├── __init__.py
            │   ├── settings.py
            │   ├── urls.py
            │   └── wsgi.py
            └── manage.py


Si tiene la estructura de archivo previa, entonces puede continuar los procesos de ejecución
del código fuente.

.. tip::

    Si quiere entender para que funciona cada archivo consulte la
    `documentación <https://docs.djangoproject.com/en/5.1/intro/tutorial01/#creating-a-project>`_.



Ejecutar aplicación Django
--------------------------

Para ejecutar aplicación Web ``Django``, con el siguiente comando:

.. code-block:: console

    python3 manage.py runserver

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:8000/

.. figure:: ../_static/images/django-index.png
  :class: image-inline
  :alt: Landing Page en Django
  :align: center

  Landing Page en Django

Mostrará el **Landing Page de Django**, como la figura anterior.

Realizar el tutorial de "`Escribiendo su primera aplicación en Django, parte 1 <https://docs.djangoproject.com/es/5.1/intro/tutorial01/>`_".

Realizar el tutorial de "`Escribiendo su primera aplicación en Django, parte 2 <https://docs.djangoproject.com/es/5.1/intro/tutorial02/>`_".

De esta forma, ya debe tener activado el Django Admin, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:8000/admin/

.. figure:: ../_static/images/django-index.png
  :class: image-inline
  :alt: Landing Page en Django Admin
  :align: center

  Landing Page en Django Admin

Mostrará el **Landing Page de Django Admin**, como la figura anterior.

Usando al Django Admin http://localhost:8000/admin/ y el usuario previamente creado ``admin`` realice lo siguiente:

Debe acceder a la aplicación "Authentication and Authorization > Groups" crear
el grupo llamado "Departamento 1" con los siguientes permisos:

::

    polls | choice | Can add choice
    polls | choice | Can change choice
    polls | choice | Can delete choice
    polls | choice | Can view choice

    polls | question | Can add question
    polls | question | Can change question
    polls | question | Can delete question
    polls | question | Can view question

Debe acceder a la aplicación "Authentication and Authorization > Groups" crear
el grupo llamado "Departamento 2" con los siguientes permisos:

::

    polls | choice | Can add choice
    polls | choice | Can change choice
    polls | choice | Can view choice

    polls | question | Can add question
    polls | question | Can change question
    polls | question | Can view question

Debe acceder a la aplicación "Authentication and Authorization > Groups" crear
el grupo llamado "Departamento 3" con los siguientes permisos:

::

    polls | choice | Can add choice
    polls | choice | Can view choice

    polls | question | Can add question
    polls | question | Can view question

Luego de crear los grupos de usuario, debe acceder a la aplicación
"Authentication and Authorization > Users" para crear varios usuarios con los
siguientes detalles:

::

    Nombre: usuario1
    Contraseña: rdswer34k#
    Groups: Departamento 3
    Staff user

    Nombre: usuario2
    Contraseña: rdsw34k#er
    Groups: Departamento 2
    Staff user

    Nombre: usuario3
    Contraseña: w34ker#rds
    Groups: Departamento 1
    Staff user


Iniciar sesión de usuario con cada usuario previamente cargado y verificar los siguientes
permisos de acceso para agregar, buscar, modificar, eliminar para el módulo ``Polls``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion7>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
