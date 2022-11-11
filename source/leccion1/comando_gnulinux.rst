.. _python_comando_linux:

Comando GNU/Linux
=================

Esta sección es un repaso sobre el funcionamiento de los comando básicos
de GNU/Linux, ya que es de mucha utilidad, para seguir la recetas de
instalación o configuración en Python, ya que trabaja vía comando.

Por lo general un comando en GNU/Linux, esta conformado de la siguiente forma:

	``nombre-comando  opciones  valores  meta-caracter  otros-comando``

Explicación

- ``nombre-comando``, nombre del comando que va a ejecutar.

- ``opciones``, opciones disponibles del comando que va a ejecutar.

- ``valores``, valor(es) de las opciones del comando que va a ejecutar.

- ``meta-caracter``, carácter usado para procesar flujo de información de la
  salida y entrada de datos entre comandos a ejecutar.

- ``otros-comando``, otro comando que recibe la entrada de datos desde otra
  ejecución.


Ejemplos
--------

A continuación una tabla de ejemplo de comando detallado:

+------------+-----------+-----------+-----------------+-----------------+
| Nombre     | Opciones  | Valores   | Meta Carácter   | Otros comando   |
+------------+-----------+-----------+-----------------+-----------------+
| pwd        |                                                           |
+------------+-----------------------------------------------------------+
| man        | ``ls``                                                    |
+------------+-----------------------------------------------------------+
| ls         | ``-lhap``                                                 |
+------------+-----------------------------------------------------------+
| env        |                                                           |
+------------+-----------------------------------------------------------+
| echo       | ``$HOME``                                                 |
+------------+-----------------------------------------------------------+
| mkdir      | ``$HOME/virtualenv``                                      |
+------------+-----------------------------------------------------------+
| mkdir      | ``~/.pip``                                                |
+------------+-----------------------------------------------------------+
| nano       | ``~/.pip/pip.conf``                                       |
+------------+-----------+-----------------------------------------------+
| mkdir      | ``-p``    | ``$HOME/demo/prueba/{css,js,images}``         |
+------------+-----------+-----------------------------------------------+
| mkdir      | ``-p``    | ``~/.cache/pip``                              |
+------------+-----------+-----------------------------------------------+
| apt-get    | update    |                                               |
+------------+-----------+-----------------------------------------------+
| apt-get    | install   | python3-dev                                   |
+------------+-----------+-----------+-----------------+-----------------+
| apt-cache  | search    | python3-  |        \|       | ``grep "mysql"``|
+------------+-----------+-----------+-----------------+-----------------+
| http       | ``--help``            |        \|       | ``less``        |
+------------+-----------+-----------+-----------------+-----------------+
| pip        | search    | httpie                                        |
+------------+-----------+-----------------------------------------------+
| pip        | install   | httpie                                        |
+------------+-----------+-----------------------------------------------+
| pip        | uninstall | httpie                                        |
+------------+-----------+-----------+-----------------+-----------------+
| python     | clases.py | persona                                       |
+------------+-----------+-----------+-----------------+-----------------+
| printf     | |pip_conf|            |        >>       | ~/.pip/pip.conf |
+------------+-----------------------+-----------------+-----------------+

.. |pip_conf| replace:: ``'[global]\ndownload_cache = ~/.cache/pip\n'``

Así de esta forma entiende de forma practica la ejecución y composición de
comando en GNU/Linux.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
