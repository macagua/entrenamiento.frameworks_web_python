.. _python_leccion2:

Persistencia de datos
=====================

La librería estándar incluye una variedad de módulos para datos persistentes.
El patrón más común para almacenar datos de objetos de Python para su reutilización
es serializarlos con el módulo ``pickle`` y luego escribirlos directamente en un
archivo o almacenarlos usando uno de los muchos formatos de base de datos de pares
*clave-valor* disponibles con la API del módulo ``dbm`` . Si no le importa el formato
``dbm`` subyacente, el módulo ``shelve`` proporciona la mejor interfaz de persistencia.

Si le importa, puede usar uno de los otros módulos basados en directamente
el módulo ``dbm``.

- ``pickle`` y cPickle: serialización de objetos de Python

- ``sqlite3`` - Base de datos relacional integrada SQLite3

Para la serialización en la web, el módulo ``json`` puede ser una mejor
opción, ya que su formato es más portátil.

En esta lección se busca introducir al uso de Base de datos relacional
con programación en Python, sus características, modos de instalación,
soporte comunitario, y los recursos mas destacados disponibles en
la Web para tomar en cuenta. A continuación el temario de esta lección:

.. toctree::
   :maxdepth: 2

   pickle
   base_datos_relacional
   dbapi
   sqlite3
   sqlalchemy

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
