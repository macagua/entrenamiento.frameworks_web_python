.. _python_django_practicas:

Prácticas
=========

Prácticas en Django

Ejecución de un proyecto Django
-------------------------------

Instalación de Django

1) Crear el directorio ~/proyects/django/acme con los siguientes comando:

.. code-block:: console

	mkdir -p ~/proyects/django/acme && cd $_

2) Crear y activar entorno virtual en ~/proyects/django/acme con Python 3, con los siguientes comando:

.. code-block:: console

	virtualenv --python=/usr/bin/python3 venv

	source ./venv/bin/activate

3) Instalar ultima versión Django, con el siguiente comando:

.. code-block:: console

	pip3 install Django==2.1.2

4) Crear proyecto Django, con el siguiente comando:

.. code-block:: console

	django-admin startproject acmeweb

5) Ejecutar proyecto Django, con los siguientes comando:

.. code-block:: console

	cd acmeweb
	python3 manage.py runserver 127.0.0.1:8000

6) Realizar el tutorial de "Escribiendo su primera aplicación en Django, parte 1" https://docs.djangoproject.com/es/2.1/intro/tutorial01/

7) Realizar el tutorial de "Escribiendo su primera aplicación en Django, parte 2" https://docs.djangoproject.com/es/2.1/intro/tutorial02/

8) Adecuar el archivo "polls/admin.py" de la siguiente forma:

.. code-block:: python

	from django.contrib import admin
	from polls.models import Question, Choice

	class QuestionAdmin(admin.ModelAdmin):
	    model = Question
	    extra = 3
	    list_display = ('question_text', 'pub_date')
	    list_filter = ['pub_date']
	    search_fields = ['question_text']


	class ChoiceAdmin(admin.ModelAdmin):
	    fieldsets = [
	        ('The Question', {
	            'fields': [
	                'question'
	            ]
	        }),
	        ('Choices text of Question', {
	            'fields': [
	                'choice_text'
	            ]
	        }),
	        ('Total of votes', {
	            'fields': [
	                'votes'
	            ]
	        }),
	    ]
	    list_display = ('choice_text', 'question', 'votes')
	    list_filter = ['choice_text']
	    search_fields = ['question__question_text', 'choice_text']

	admin.site.register(Question, QuestionAdmin)
	admin.site.register(Choice, ChoiceAdmin)

----

Gestión de usuarios con el Django Admin
---------------------------------------

Usando al Django Admin http://localhost:8000/admin/ y el usuario previamente creado "admin" realice lo siguiente:

2) Debe acceder a la aplicación "Authentication and Authorization > Groups" crear el grupo llamado "Departamento 1" con los siguientes permisos:

::

	polls | choice | Can add choice
	polls | choice | Can change choice
	polls | choice | Can delete choice
	polls | choice | Can view choice

	polls | question | Can add question
	polls | question | Can change question
	polls | question | Can delete question
	polls | question | Can view question

3) Debe acceder a la aplicación "Authentication and Authorization > Groups" crear el grupo llamado "Departamento 2" con los siguientes permisos:

	polls | choice | Can add choice
	polls | choice | Can change choice
	polls | choice | Can view choice

	polls | question | Can add question
	polls | question | Can change question
	polls | question | Can view question

3) Debe acceder a la aplicación "Authentication and Authorization > Groups" crear el grupo llamado "Departamento 3" con los siguientes permisos:

::

	polls | choice | Can add choice
	polls | choice | Can view choice

	polls | question | Can add question
	polls | question | Can view question

3) Luego de crear los grupos de usuario, debe acceder a la aplicación "Authentication and Authorization > Users" para crear varios usuarios con los siguientes detalles:

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


4) Iniciar sesión de usuario con cada usuario previamente cargado y verificar permisos de acceso para agregar, buscar, modificar, eliminar para el modulo "Polls".


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
