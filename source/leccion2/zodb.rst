.. _python_modulo_zodb:

ZODB
=====

`ZODB`_ ofrece una base de datos orientada a objetos para Python que proporciona un alto grado de transparencia.

- ✅ No hay lenguaje separado para las operaciones de base de datos

- ✅ Muy poco impacto en su código para hacer objetos persistentes

- ✅ Ningún mapeador de base de datos que oculte parcialmente la base de datos.

- ✅ Utilizar un mapeo objeto-relacional no es como utilizar una base de datos orientada a objetos.

- ✅ Casi ninguna costura entre el código y la base de datos.

- ✅ Las relaciones entre objetos se gestionan de forma muy natural, lo que permite crear grafos de objetos complejos sin uniones.

``ZODB`` es una base de datos transaccional ACID.

``ZODB`` funciona con Python 3.7 y versiones superiores. También funciona con PyPy.


📌 **Ventajas de ZODB**:

- ✅ Fácil de usar, sin necesidad de instalar bases de datos.

- ✅ Útil para almacenar estructuras de datos complejas (listas, diccionarios, objetos).

📌 **Desventajas**:

- ❌ No es ideal para grandes volúmenes de datos.

- ❌ No permite consultas avanzadas como SQL.


----


¿Qué es la ZODB?
-----------------

``ZODB`` es un sistema de persistencia para objetos Python.  Los lenguajes de programación
que escriben objetos automáticamente en el disco y los vuelven a leer cuando son requeridos
por un programa en ejecución.  Al instalar el ``ZODB``, añades estas facilidades a Python.

Es ciertamente posible construir tu propio sistema para hacer persistentes los objetos Python.
Los puntos de partida habituales son el módulo :mod:`pickle`, para convertir objetos en una
representación de cadena, y varios módulos de bases de datos, como los módulos :mod:`gdbm` o
:mod:`bsddb`, que proporcionan formas de escribir cadenas en el disco y leerlas de vuelta.
Es sencillo combinar el módulo :mod:`pickle` y un módulo de base de datos para almacenar y
recuperar objetos, y de hecho el módulo :mod:`shelve`, incluido en la biblioteca estándar
de Python, lo hace.

El inconveniente es que el programador tiene que gestionar explícitamente los objetos, leyendo
un objeto cuando se necesita y escribiéndolo en el disco cuando el objeto ya no es necesario.
La ZODB gestiona los objetos por ti, manteniéndolos en una caché, escribiéndolos en disco cuando
se modifican y eliminándolos de la caché si no se han utilizado durante un tiempo.


----


OODBs vs. BD relacionales
^^^^^^^^^^^^^^^^^^^^^^^^^

Otra forma de verlo es que ZODB es una base de datos orientada a objetos (OODB) específica
de Python. Las bases de datos de objetos comerciales para C++ o Java a menudo exigen pasar
por el aro, como utilizar un preprocesador especial o evitar determinados tipos de datos.
Como veremos, el ZODB tiene que pasar por algunos obstáculos, pero en comparación, la
naturalidad del ZODB es asombrosa.

Las bases de datos relacionales (RDB) son mucho más comunes que las OODB. Las bases de
datos relacionales almacenan la información en tablas; una tabla consta de cualquier
número de filas, cada una de las cuales contiene varias columnas de información. (Las
filas se denominan más formalmente relaciones, de donde procede el término "base de
datos relacional").

Veamos un ejemplo concreto. El ejemplo procede de mi trabajo diario en la Bolsa de MEMS,
en una versión muy simplificada. El trabajo consiste en hacer un seguimiento de los procesos,
que son listas de pasos de fabricación que deben realizarse en una fábrica de semiconductores.
Una ejecución pertenece a un usuario concreto, y tiene un nombre y un número de identificación
asignados. Las ejecuciones constan de una serie de operaciones; una operación es un único paso
a realizar, como depositar algo en una oblea o grabar algo en ella.

Las operaciones pueden tener parámetros, que son información adicional necesaria para realizar
una operación. Por ejemplo, si vas a depositar algo en una oblea, necesitas saber dos cosas:
1) qué estás depositando, y 2) cuánto debe depositarse. Puede depositar 100 micras de óxido
2) de silicio o 1 micra de cobre.

El traslado de estas estructuras a una base de datos relacional es sencillo:

::

   CREATE TABLE runs (
     int      run_id,
     varchar  owner,
     varchar  title,
     int      acct_num,
     primary key(run_id)
   );

   CREATE TABLE operations (
     int      run_id,
     int      step_num,
     varchar  process_id,
     PRIMARY KEY(run_id, step_num),
     FOREIGN KEY(run_id) REFERENCES runs(run_id),
   );

   CREATE TABLE parameters (
     int      run_id,
     int      step_num,
     varchar  param_name,
     varchar  param_value,
     PRIMARY KEY(run_id, step_num, param_name)
     FOREIGN KEY(run_id, step_num)
        REFERENCES operations(run_id, step_num),
   );

En Python, escribiría tres clases llamadas :class:`Run`, :class:`Operation`, y :class:`Parameter`.
No presentaré código para definir estas clases, ya que ese código carece de interés en este momento.
Cada clase contendría un único método para empezar, un método :meth:`__init__` que asigna valores
por defecto, como 0 o ``None``, a cada atributo de la clase.

No es difícil escribir código Python que cree una instancia :class:`Run` y la rellene con los datos
de las tablas relacionales; con un poco más de esfuerzo, se puede construir una herramienta sencilla,
normalmente llamada mapeador objeto-relacional, para hacerlo automáticamente.

(Véase `<https://legacy.python.org/workshops/1997-10/proceedings/shprentz.html>`_
para la implementación más exitosa de Joel Shprentz, el sistema de Shprentz se ha utilizado para trabajo real).

Sin embargo, es difícil hacer que un mapeador objeto-relacional sea razonablemente rápido; una
implementación simplona como la mía es bastante lenta porque tiene que hacer varias consultas
para acceder a todos los datos de un objeto. Los mapeadores objeto-relacionales de mayor
rendimiento almacenan en caché los objetos para mejorar el rendimiento, y sólo realizan
consultas SQL cuando realmente lo necesitan.

Eso ayuda si quieres acceder al número de ejecución 123 de repente. Pero, ¿qué ocurre si desea
encontrar todas las ejecuciones en las que un paso tiene un parámetro denominado "grosor" con
un valor de 2.0?  En la versión relacional, tiene dos opciones poco atractivas:

#. Escriba una consulta SQL especializada para este caso: ``SELECT run_id FROM operations
   WHERE param_name = 'thickness' AND param_value = 2.0``

   Si este tipo de consultas son habituales, puede acabar teniendo muchas consultas especializadas.
   Cuando se reorganicen las tablas de la base de datos, habrá que modificar todas estas consultas.

#. Un mapeador objeto-relacional no ayuda mucho. Escanear a través de las ejecuciones significa que
   el mapeador realizará las consultas SQL necesarias para leer la ejecución nº 1, y luego un simple
   bucle de Python puede comprobar si alguno de sus pasos tiene el parámetro que estás buscando.
   Repite para la carrera #2, 3, y así sucesivamente. Esto hace un gran número de consultas SQL, y
   por lo tanto es increíblemente lento.

Una base de datos de objetos como ZODB simplemente almacena punteros internos de objeto a objeto, por
lo que leer un solo objeto es mucho más rápido que hacer un montón de consultas SQL y ensamblar los
resultados. Por lo tanto, escanear todas las ejecuciones sigue siendo ineficiente, pero no extremadamente
ineficiente.


----


.. _python_zodb_instalar:

Instalación
-----------

Para conectarte a una ``ZODB`` necesita el paquete `ZODB`_. Esto
significa que debe instalar ``ZODB`` ejecutando el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip3 install ZODB==6.0

   .. group-tab:: Windows

      .. code-block:: console

          > pip3 install ZODB==6.0

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip3 freeze | grep "ZODB"

   .. group-tab:: Windows

      .. code-block:: console

          > pip3 freeze | grep "ZODB"


Si muestra el numero de la versión instalada de ``ZODB``, tiene correctamente instalada
la paquete. Con esto, ya tiene todo listo para continuar.


----


Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``ZODB`` para operaciones CRUD en un archivo de registros serializados:

.. literalinclude:: ../../recursos/leccion2/zodb/main.py
    :language: python
    :linenos:
    :lines: 1-96

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`main.py <../../recursos/leccion2/zodb/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    ::

        zodb/
        ├── filestorage/
        └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python3 main.py


    La salida esperada será similar a la siguiente:

    ::

        ✅ ¡La conexión ZODB a la base de datos 'data.fs' fue establecida!

        ✅ Cliente 'Leonardo Caballero' creado con éxito.
        ✅ Cliente 'Ana Poleo' creado con éxito.
        ✅ Cliente 'Manuel Matos' creado con éxito.

        📜 Lista de Clientes:
        ID: 1, Nombre: Leonardo, Apellido: Caballero, Código postal: 5001, Teléfono: +58-412-4734567
        ID: 2, Nombre: Ana, Apellido: Poleo, Código postal: 6302, Teléfono: +58-426-5831297
        ID: 3, Nombre: Manuel, Apellido: Matos, Código postal: 4001, Teléfono: +58-414-2360943
        ✅ Cliente con ID: '1' actualizado con éxito.

        📜 Lista de Clientes:
        ID: 1, Nombre: Leonardo, Apellido: Caballero, Código postal: 5001, Teléfono: +58-416-5831297
        ID: 2, Nombre: Ana, Apellido: Poleo, Código postal: 6302, Teléfono: +58-426-5831297
        ID: 3, Nombre: Manuel, Apellido: Matos, Código postal: 4001, Teléfono: +58-414-2360943
        ✅ Cliente con ID: '3' eliminado con éxito.

        📜 Lista de Clientes:
        ID: 1, Nombre: Leonardo, Apellido: Caballero, Código postal: 5001, Teléfono: +58-416-5831297
        ID: 2, Nombre: Ana, Apellido: Poleo, Código postal: 6302, Teléfono: +58-426-5831297

        ✅ ¡La conexión ZODB a la base de datos 'data.fs' fue cerrada!
        ✅ ¡La base de datos ZODB 'data.fs' fue cerrada!


    La estructura de directorio debe ser similar a la siguiente:

    ::

        zodb/
        ├── filestorage/
        │   ├── data.fs
        │   ├── data.fs.index
        │   ├── data.fs.lock
        │   └── data.fs.tmp
        └── main.py

.. tip::
    En lugar de una base de datos real, usaremos un archivo ``data.fs`` para almacenar los
    datos en una lista de diccionarios.

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en un archivo serializado de objetos python ``ZODB``.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`

.. _`ZODB`: https://zodb-docs.readthedocs.io/en/latest/
