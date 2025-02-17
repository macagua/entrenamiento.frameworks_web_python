.. _python_introduccion_http:

Introducción a HTTP
===================

El **protocolo Hypertext Transfer Protocol (HTTP)** fue creado por Tim Berners-Lee en
1989, es el protocolo utilizado para acceder y publicar en la Web. Significa en espanol
*Protocolo de transmisión de hipertexto*.

Actualmente el `World Wide Web Consortium (W3C) <https://www.w3.org/>`_ es la entidad
encargada de publicar la especificación del protocolo HTTP, entre otras cosas.

HTTP está basado en una arquitectura cliente-servidor en la que se intercambian peticiones
(requests) por parte del cliente y respuestas (responses) por parte del servidor.

Características
---------------

-  **Sin estado**. Es decir, que cada una de las transacciones request/response
   que se realizan no afectan al estado del cliente o del servidor, además de que
   cada transacción es totalmente independiente de el resto.

-  **Independiente del contenido**. Aún cuando es muy común que un servidor HTTP
   entregue documentos HTML, pero no existe restricción en el tipo de recurso al
   que se pueda acceder.

-  **Sin conexión**. Una vez que la transacción request/response es terminada, la
   conexión entre cliente y servidor es destruida.


Uniform Resource Identifiers (URI)

Como su nombre lo indica, los Identificadores Recursos Uniformes siempre apuntan
hacia un recurso al que se puede acceder.

**Sintaxis:**

::

   URI = "http:" "//" host [ ":" port ] [ abs\_path [ "?" query ]]

Peticiones, respuestas y sesiones
---------------------------------

Las comunicaciones entre el cliente y el servidor consisten en un serie
de intercambios de datos.

-  Un cliente por lo general envía una petición (request) a un servidor
   atendiendo a una dirección específica.

-  El servidor recibe la petición y procesa los datos. Dependiendo de la
   petición, el servidor puede enviar distintos mensajes que incluyen un
   estado específico.

-  A este intercambio de peticiones y respuestas entre un cliente y un
   servidor se conocen como sesión.

Los mensajes de estado son respuestas de un servidor con respecto a una
consulta o búsqueda de recursos. Está conformado por un número entero de
3 dígitos. Quizás el mensaje de estado más conocido es el *404* que se
emite cuando un recurso no es encontrado.

Tipos por el número inicial
''''''''''''''''''''''''''''

+------------+---------------------+
| **Método** | **Explicación**     |
+------------+---------------------+
| ``1xx``    | Información.        |
+------------+---------------------+
| ``2xx``    | Éxito.              |
+------------+---------------------+
| ``3xx``    | Redireccionamiento. |
+------------+---------------------+
| ``4xx``    | Error del cliente.  |
+------------+---------------------+
| ``5xx``    | Error del servidor. |
+------------+---------------------+

Puede consultar los mensajes de estado de HTTP en el siguiente
enlace: https://www.restapitutorial.com/httpstatuscodes

Métodos HTTP
------------

El protocolo HTTP define métodos o "verbos", los cuales permiten
realizar peticiones específicas entre un cliente y un servidor. Algunos
de los métodos más utilizados son:

+--------------+--------------------------------------------------------------------------+
| **Método**   | **Explicación**                                                          |
+--------------+--------------------------------------------------------------------------+
| ``GET``      | Se utiliza para obtener los datos de un recurso a partir de una URI. La  |
|              | información enviada mediante ``GET`` puede ser añadida a marcadores y    |
|              | puede ser registrada en las bitácoras del servidor.                      |
+--------------+--------------------------------------------------------------------------+
| ``HEAD``     | Es similar al método ``GET``, pero sólo proporciona el encabezado de la  |
|              | la petición y el mensaje de estado resultante.                           |
+--------------+--------------------------------------------------------------------------+
| ``POST``     | Se utiliza para crear un recurso. Los datos enviados no son expuestos en |
|              | la URI sino que son enviados dentro de la estructura de la petición.     |
+--------------+--------------------------------------------------------------------------+
| ``PUT``      | Es un método similar a ``POST``, pero puede ser utilizado para sustituir |
|              | un recurso existente o incluso crearlos en casos específicos.            |
+--------------+--------------------------------------------------------------------------+
| ``PATCH``    | Es un método que se utiliza para modificar parcialmente un recurso.      |
+--------------+--------------------------------------------------------------------------+

Existen algunos otros métodos como ``OPTIONS``, ``TRACE`` y ``CONNECT``,
pero no están contemplados en el alcance de este taller. Puede consultar
más al respecto en https://developer.mozilla.org/es/docs/Web/HTTP/Methods.

Idempotencia
''''''''''''

En matemática y lógica, la *"idempotencia"* es la propiedad para realizar una
acción determinada varias veces y aun así conseguir el mismo resultado que se
obtendría si se realizase una sola vez. Un elemento que cumple esta propiedad
es un elemento *"idempotente"*, o un *"idempotente"*.

Por consiguiente en un lenguaje de programación, un método es *"idempotente"*
cuando no importan las veces que se envíe la misma petición, ésta dará el
mismo resultado.

Seguridad
'''''''''

Un método se considera seguro si no modifica a los recursos a los que
accede.

+--------------+-----------------+------------+
| *Método*     | *Idempotente*   | *Seguro*   |
+==============+=================+============+
| ``GET``      | Sí              | Sí         |
+--------------+-----------------+------------+
| ``HEAD``     | Sí              | Sí         |
+--------------+-----------------+------------+
| ``DELETE``   | Sí              | No         |
+--------------+-----------------+------------+
| ``POST``     | Sí              | No         |
+--------------+-----------------+------------+
| ``PUT``      | Sí              | No         |
+--------------+-----------------+------------+
| ``PATCH``    | No              | No         |
+--------------+-----------------+------------+

Advertencia sobre los métodos seguros
'''''''''''''''''''''''''''''''''''''

La seguridad de un método depende de su implementación y aún cuando se
considera como una mala práctica, es posible que los métodos como ``GET``
sean capaces de modificar los recursos a los que acceden.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
