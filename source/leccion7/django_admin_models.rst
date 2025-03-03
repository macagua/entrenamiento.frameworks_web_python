.. _python_django_admin_models:

Habilitar Modelos en Django Admin
==================================

Práctica de habilitar los modelos con la interfaz web del `Django Admin`_ de :doc:`Django <./index>`.


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

Realizar el tutorial de "`Escribiendo su primera aplicación en Django, parte 1`_".

Realizar el tutorial de "`Escribiendo su primera aplicación en Django, parte 2`_".

Luego de realizar ambos tutoriales anteriores, la estructura del proyecto
tiene que estar como la siguiente:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── django/
        └── acmeweb
            ├── acmeweb
            │   ├── asgi.py
            │   ├── __init__.py
            │   ├── settings.py
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── polls
                ├── admin.py
                ├── apps.py
                ├── __init__.py
                ├── migrations
                │   └── __init__.py
                ├── models.py
                ├── tests.py
                └── views.py


Si llego hasta el final del tutorial de "`Escribiendo su primera aplicación en Django, parte 2`_"
el archivo :file:`polls/admin.py` debe contener el siguiente código fuente:

.. code-block:: python

    from django.contrib import admin

    from .models import Question

    admin.site.register(Question)


Si tiene el código fuente anterior, y ejecutado el ``runserver`` puede abrir desde con su navegador
Web favorito (Mozilla Firefox, Google Chrome, etc) la siguiente dirección: http://127.0.0.1:8000/admin/polls/question/

El código fuente anterior, da como resultado la habilitación del modelo ``Question`` dentro de la
interfaz web ``Django Admin`` como se muestra a continuación:

.. figure:: ../_static/images/django_question_model.png
  :class: image-inline
  :alt: Modelo Question desde el Django Admin
  :align: center

  Modelo ``Question`` desde el ``Django Admin``

Mostrará el listado predeterminado del modelo ``Question``, como la figura anterior.

Seguidamente presione la combinación de tecla :keys:`Crtl+c` para finalizar
la ejecución del ``runserver``.

A continuación debe adecuar el archivo :file:`polls/admin.py` para agregar el modelo ``Choice``, con el
siguiente contenido:

.. code-block:: python

    from django.contrib import admin

    from .models import Question, Choice

    admin.site.register(Question)
    admin.site.register(Choice)


Si tiene el código fuente anterior, y ejecutado el ``runserver`` puede abrir desde con su navegador
Web favorito (Mozilla Firefox, Google Chrome, etc) la siguiente dirección: http://127.0.0.1:8000/admin/polls/choice/

El código fuente anterior, da como resultado la habilitación del modelo ``Choice`` dentro de la
interfaz web ``Django Admin`` como se muestra a continuación:

.. figure:: ../_static/images/django_choice_model.png
  :class: image-inline
  :alt: Modelo Choice desde el Django Admin
  :align: center

  Modelo ``Choice`` desde el ``Django Admin``

Mostrará el listado predeterminado del modelo ``Choice``, como la figura anterior.

clase ModelAdmin
^^^^^^^^^^^^^^^^

La `clase ModelAdmin`_ es la representación de un modelo en la interfaz de administración ``Django Admin``.
Por lo general, se almacenan en un archivo llamado :file:`admin.py` en su aplicación.

A continuación, debe adecuar el archivo :file:`polls/admin.py` para extender comportamientos de la gestión
de los modelos ``Question`` y ``Choice`` en la interfaz ``Django Admin``, agregando el siguiente contenido:

.. code-block:: python

    from django.contrib import admin
    from .models import Question, Choice


    class QuestionAdmin(admin.ModelAdmin):
        model = Question
        extra = 3
        list_display = ("question_text", "pub_date")
        list_filter = ["pub_date"]
        search_fields = ["question_text"]


    class ChoiceAdmin(admin.ModelAdmin):
        fieldsets = [
            ("The Question", {"fields": ["question"]}),
            ("Choices text of Question", {"fields": ["choice_text"]}),
            ("Total of votes", {"fields": ["votes"]}),
        ]
        list_display = ("choice_text", "question", "votes")
        list_filter = ["choice_text"]
        search_fields = ["question__question_text", "choice_text"]


    admin.site.register(Question, QuestionAdmin)
    admin.site.register(Choice, ChoiceAdmin)

Detenga el ``runserver`` presionando la combinación de teclas ::kbd:`Crtl + c` y
inicie de nuevo el ``runserver``, con el siguiente comando:

.. code-block:: console

    python3 manage.py runserver

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:8000/admin/polls/question/

.. figure:: ../_static/images/django_question_modeladmin.png
  :class: image-inline
  :alt: El admin.ModelAdmin extiende el modelo Question en el Django Admin
  :align: center

  El ``admin.ModelAdmin`` extiende el modelo ``Question`` en el ``Django Admin``

Mostrará el listado del modelo ``Question``, extendiendo los comportamientos de la gestión de los
modelos desde la ``Django Admin``, como la figura anterior.

De esta forma, una vez ejecutado el comando, se puede abrir desde con su navegador Web favorito
(Mozilla Firefox, Google Chrome, etc) la siguiente dirección http://127.0.0.1:8000/admin/polls/choice/

.. figure:: ../_static/images/django_choice_modeladmin.png
  :class: image-inline
  :alt: El admin.ModelAdmin extiende el modelo Choice en el Django Admin
  :align: center

  El ``admin.ModelAdmin`` extiende el modelo ``Choice`` en el ``Django Admin``

Mostrará el listado del modelo ``Choice``, extendiendo los comportamientos de la gestión de los
modelos desde la ``Django Admin``, como la figura anterior.

De esta forma, ha aprendió nociones básicas para habilitar la gestión de los modelos dentro de
la interfaz `Django Admin`_.

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion7>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`Django Admin`: https://docs.djangoproject.com/en/5.1/intro/tutorial02/#introducing-the-django-admin
.. _`Escribiendo su primera aplicación en Django, parte 1`: https://docs.djangoproject.com/es/5.1/intro/tutorial01/
.. _`Escribiendo su primera aplicación en Django, parte 2`: https://docs.djangoproject.com/es/5.1/intro/tutorial02/
.. _`clase ModelAdmin`: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#modeladmin-objects
