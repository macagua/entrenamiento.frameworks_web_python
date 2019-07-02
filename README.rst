.. -*- coding: utf-8 -*-

======================================================
Entrenamiento "Frameworks de Desarrollo Web en Python"
======================================================

Repositorio de manuales y recursos del entrenamiento *"Frameworks de Desarrollo Web 
en Python"* realizado por la empresa Covantec R.L.

.. contents :: :local:


Estructura general
===================

La estructura general de contenidos esta confirmada por los principales archivos:

**00-entrenamiento_frameworks_web_python.odt**
  Describe el contenido del entrenamiento.

**source**
  Describe los contenidos de las lecciones *1, 2, 3, 4, 5, 6, 7* del entrenamiento. 
  Además de otros temas complementarios de Python.


Obtener y compilar la documentación
===================================

El almacenamiento de este material está disponible en un repositorio Git en Github.com "`entrenamiento.frameworks_web_python`_". 

Si usted tiene una credenciales en este servidor y desea convertirse en un colaborador 
de los materiales de este entrenamiento, usted debe seguir los siguientes pasos:


Dependencias
------------

Para construir estos recursos, debe ejecutar las dependencias, entonces debe ejecutar 
los siguientes comando:

::

  $ sudo apt install python3-dev python-pip python-setuptools git
  $ sudo apt install texlive-latex-base texlive-latex-recommended texlive-lang-spanish
  $ sudo pip install virtualenv


Descargar repositorio
---------------------

Para descargar repositorio para modificar los recursos del entrenamiento, ejecute los 
siguientes comando:

::

  $ cd $HOME
  $ git clone https://github.com/Covantec/entrenamiento.frameworks_web_python.git

Crear entorno virtual de Python para reconstruir este proyecto, ejecutando el siguiente 
comando:

::

  $ cd ~/entrenamiento.frameworks_web_python
  $ virtualenv --python=/usr/bin/python venv
  $ source ./venv/bin/activate

Luego instale dependencias Sphinx, ejecutando el siguiente comando:

::

  (venv)$ pip install -r requirements.txt


Recursos del entrenamiento
==========================

La herramientas Sphinx le permite generar los recursos usado en el entrenamiento, 
en diversos formatos, actualmente se tiene bien soportado los siguientes:


Formato HTML
------------

Usted puede generar la documentación en HTML del módulo *1, 2, 3, 4, 5, 6, 7*; 
ejecute los siguientes comando:

::

  (venv)$ make html

Una vez generado el formato HTML se puede abrir desde el directorio ``build/html/index.html``
con su navegador Web favorito (Mozilla Firefox, Google Chrome, etc).


Formato PDF
-----------
  
Usted puede generar la documentación en PDF del módulo *1, 2, 3, 4, 5, 6, 7*; 
ejecute los siguientes comando:

::

  (venv)$ make latexpdf

Al finalizar exitosamente la ejecución del comando anterior, este genera un PDF 
llamado ``entrenamientoframeworks_web_python.pdf`` y se encuentra desde el directorio 
``build/latex/``,  desde allí puede abrir para visualizar con cualquier programas 
de visor de PDF favorito (Evince, Acrobat Reader, etc).


Estatus de Calidad
==================

.. image:: https://readthedocs.org/projects/entrenamiento-frameworks-web-python/badge/?version=latest
   :target: http://entrenamiento-frameworks-web-python.rtfd.io/
   :align: left
   :alt: entrenamiento-frameworks-web-python ReadTheDocs build status


Colabora
========

¿Tiene alguna idea?, ¿Encontró un error? Por favor, hágalo saber 
registrando un `ticket de soporte`_.


Licencia
========

Esta obra está licenciada bajo la licencia Creative Commons 
Atribución-CompartirIgual 3.0 Venezuela. Para ver una copia de esta licencia, 
visite https://creativecommons.org/licenses/by-sa/3.0/ve/ o envíe una carta a 
Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 
94041, EE.UU.

Una copia de esta licencia en formato de texto se incluye en este paquete 
dentro del directorio ``docs`` tanto en el idioma Ingles (LICENSE.rst) como 
el idioma Español (LICENSE.es.rst).

.. _`entrenamiento.frameworks_web_python`: https://github.com/Covantec/entrenamiento.frameworks_web_python
.. _`ticket de soporte`: https://github.com/Covantec/entrenamiento.frameworks_web_python/issues/new
