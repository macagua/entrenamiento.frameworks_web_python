.. _python_dbapi:

Interfaz DB-API
===============

Python, ofrece el acceso a bases de datos estandarizado 
por la especificación Database API (DB-API), actualmente 
en la versión 2.0 *(PEP 249: Python Database API Specification v2.0)*.


La `Python DB API 2.0 <http://legacy.python.org/dev/peps/pep-0249/>`_, 
es un conjunto de clases y funciones comunes, estandarizadas, 
similares para los distintos motores de bases de datos o wrappers 
alrededor de estos, escritos en Python. Se desarrolla con la 
finalidad de lograr la consistencia entre todos estos módulos, y 
ampliar las posibilidades de crear código portable entre las 
distintas bases de datos. 

.. warning::
    Cabe aclarar que la API trata principalmente de bases de datos SQL, 
    relacionales, pero implementarla, en lo posible, en motores NoSQL 
    no sería conveniente.

La librería :doc:`SQLAlchemy <./sqlalchemy>` es el kit de herramientas 
SQL de Python y el mapeador relacional de objetos.

Gracias a esto, se puede acceder a cualquier base de datos 
utilizando la misma interfaz (ya sea un motor remoto, local, ODBC, 
etc). Se puede comparar con DAO, ADO, ADO.NET en el mundo Microsoft, 
o a JDBC en el mundo Java.

O sea, el mismo código se podría llegar a usar para cualquier 
base de datos, tomando siempre los recaudos necesarios (lenguaje SQL 
estándar, estilo de parámetros soportado, etc.)

Por ello, el manejo de bases de datos en Python siempre sigue estos 
pasos:

- Importar el conector.

- Conectarse a la base de datos (función ``connect`` del módulo conector).

- Abrir un Cursor (método cursor de la conexión).

- Ejecutar una consulta (método ``execute`` del cursor).

- Obtener los datos (método ``fetch`` o iterar sobre el cursor).

- Cerrar el cursor (método ``close`` del cursor).
