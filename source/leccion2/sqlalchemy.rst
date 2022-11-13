.. _python_sqlalchemy:

Librería SQLAlchemy
===================

La librería `SQLAlchemy <https://pypi.org/project/SQLAlchemy/>`_
es el kit de herramientas SQL de Python y el mapeador relacional
de objetos.


``SQLAlchemy`` es el kit de herramientas SQL de Python y el Mapeador
relacional de objetos que ofrece a los desarrolladores de aplicaciones
la máxima potencia y flexibilidad de SQL. Esta proporciona un conjunto
completo de patrones de persistencia conocidos a nivel empresarial,
diseñados para un acceso a bases de datos eficiente y de alto
rendimiento, adaptados a un lenguaje de dominio simple y Pythonic.


Características
---------------

Las principales características de SQLAlchemy incluyen:

- Un ORM de potencia industrial, construido desde el núcleo en el
  mapa de identidad, la unidad de trabajo y los patrones del mapeador
  de datos. Estos patrones permiten la persistencia transparente de
  objetos utilizando un sistema de configuración declarativo. Los
  modelos de dominio se pueden construir y manipular de forma natural,
  y los cambios se sincronizan con la transacción actual automáticamente.

- Un sistema de consulta orientado a la relación, que expone explícitamente
  toda la gama de capacidades de SQL, incluidas combinaciones, subconsultas,
  correlaciones y casi todo lo demás, en términos del modelo de objetos.
  Las consultas de escritura con el ORM utilizan las mismas técnicas de
  composición relacional que utiliza al escribir SQL. Si bien puede caer
  en SQL literal en cualquier momento, virtualmente nunca es necesario.

- Un sistema completo y flexible de carga impaciente para colecciones
  y objetos relacionados. Las colecciones se almacenan en caché dentro
  de una sesión y se pueden cargar en un acceso individual, todo de una
  vez mediante uniones, o por consulta por colección en todo el conjunto
  de resultados.

- Un sistema de construcción Core SQL y una capa de interacción DBAPI.
  SQLAlchemy Core es independiente del ORM y es una capa de abstracción
  de base de datos completa por derecho propio, e incluye un lenguaje de
  expresión SQL basado en Python extensible, metadatos de esquema,
  agrupación de conexiones, coacción de tipos y tipos personalizados.

- Se supone que todas las restricciones de clave primaria y externa son
  compuestas y naturales. Por supuesto, las claves primarias de enteros
  sustitutos siguen siendo la norma, pero SQLAlchemy nunca asume ni codifica
  los códigos de este modelo.

- Base de datos de introspección y generación. Los esquemas de la base
  de datos se pueden "reflejar" en un solo paso en las estructuras de
  Python que representan los metadatos de la base de datos; esas mismas
  estructuras pueden generar declaraciones CREATE de inmediato, todas
  dentro del Core, independientemente del ORM.

Instalación
-----------

Para instalar la librería SQLAlchemy debe seguir los siguientes
pasos:


Requisitos previos
^^^^^^^^^^^^^^^^^^

Actualizar repositorios de paquetes disponibles para instalar, con
el siguiente comando:

.. code-block:: console

  $ sudo apt update

Instalar dependencias mínimas necesarias, con el siguiente comando:

.. code-block:: console

  $ sudo apt install python3-dev python3-pip python3-virtualenv git


Entorno virtual Python
^^^^^^^^^^^^^^^^^^^^^^

Crear entorno virtual Python en directorio raíz con el siguiente
comando:

.. code-block:: console

  $ virtualenv --python=/usr/bin/python3 ~/venv


Activar el entorno virtual Python creado con el siguiente comando:

.. code-block:: console

  $ source ~/venv/bin/activate


Instalar paquetes Python
^^^^^^^^^^^^^^^^^^^^^^^^

Para instalar las dependencias para usar la librería SQLAlchemy,
con el siguiente comando:

.. code-block:: console

  $ pip3 install -U SQLAlchemy

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando:

.. code-block:: console

  $ python3 -c "import sqlalchemy ; print(sqlalchemy.__version__)"

Si muestra el numero de la versión instalada de SQLAlchemy, tiene
correctamente instalada la librería.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
