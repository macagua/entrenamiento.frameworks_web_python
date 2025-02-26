.. -*- coding: utf-8 -*-

======================================================
Entrenamiento "Frameworks de Desarrollo Web en Python"
======================================================

Repositorio de manuales y recursos del entrenamiento "Frameworks de Desarrollo Web en
`Python 3.11`_" realizado por la empresa `Covantec R.L`_.

.. contents :: :local:


Estructura general
===================

La estructura general de contenidos esta confirmada por los principales archivos:

**00-entrenamiento_frameworks_web_python.odt**
  Describe el contenido del entrenamiento.

**source**
  Describe los contenidos de los módulos *1, 2, 3, 4, 5, 6, 7, 8* del entrenamiento.
  Además de otros temas complementarios de Python.


Obtener y compilar la documentación
===================================

El almacenamiento de este material está disponible en un repositorio Git
en Github.com "`entrenamiento.frameworks_web_python`_".

Si usted tiene una credenciales en este servidor y desea convertirse en un colaborador
de los materiales de este entrenamiento, usted debe seguir los siguientes pasos:


Dependencias
------------

Para construir estos recursos, debe ejecutar las dependencias, entonces debe ejecutar
los siguientes comando:

::

  $ sudo apt update && sudo apt upgrade -y
  $ sudo apt install -y python3-dev python3-pip python3-virtualenv python3-setuptools git
  $ sudo apt install -y texlive texlive-base texlive-latex-base texlive-extra-utils \
                        texlive-font-utils texlive-fonts-recommended texlive-latex-extra \
                        texlive-latex-recommended texlive-lang-spanish dvi2ps dvipng latexmk


Descargar repositorio
---------------------

Para descargar repositorio para modificar los recursos del entrenamiento, ejecute los
siguientes comando:

::

  $ cd $HOME
  $ git clone https://github.com/macagua/entrenamiento.frameworks_web_python.git
  $ git submodule update --init --recursive
  $ git submodule update --init --remote --recursive

Crear entorno virtual de Python para reconstruir este proyecto, ejecutando el siguiente
comando:

::

  $ cd ~/entrenamiento.frameworks_web_python
  $ virtualenv --python /usr/bin/python3 venv
  $ source ./venv/bin/activate

Luego instale dependencias del paquete ``Sphinx``, ejecutando el siguiente comando:

::

  (venv)$ pip3 install -r requirements-dev.txt


Recursos del entrenamiento
==========================

La herramienta ``Sphinx`` le permite generar los recursos usado en el entrenamiento,
en diversos formatos, actualmente se tiene bien soportado los siguientes:


Formato HTML
------------

Usted puede generar la documentación en HTML de los módulos *1, 2, 3, 4, 5, 6, 7, 8*;
ejecute los siguientes comando:

::

  (venv)$ make html

Una vez generado el formato HTML se puede abrir desde el directorio ``build/html/index.html``
con su navegador Web favorito (Mozilla Firefox, Google Chrome, etc).


Formato PDF
-----------

Usted puede generar la documentación en PDF de los módulos *1, 2, 3, 4, 5, 6, 7, 8*;
ejecute los siguientes comando:

::

  (venv)$ make pdf

Al finalizar exitosamente la ejecución del comando anterior, este genera un PDF
llamado ``entrenamiento_frameworks_web_python.pdf`` y se encuentra desde el directorio
``build/latex/``, desde allí puede abrir para visualizar con cualquier programas
de visor de PDF favorito (Evince, Acrobat Reader, etc).


Estatus de Calidad
==================

.. image:: https://readthedocs.org/projects/entrenamiento-frameworks-web-python/badge/?version=latest
   :target: https://entrenamiento-frameworks-web-python.rtfd.io/
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

Una copia de esta licencia en formato de texto se incluye en este paquete dentro del
directorio ``docs`` tanto en el idioma Ingles (LICENSE.rst) como el idioma Español
(LICENSE.es.rst).

.. _`Covantec R.L`: https://github.com/Covantec
.. _`Python 3.11`: https://docs.python.org/es/3.11/
.. _`entrenamiento.frameworks_web_python`: https://github.com/macagua/entrenamiento.frameworks_web_python
.. _`ticket de soporte`: https://github.com/macagua/entrenamiento.frameworks_web_python/issues/new
