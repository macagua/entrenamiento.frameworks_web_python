.. _python_http_examples:

HTTP en Python
==============


El :ref:`Protocolo Hypertext Transfer Protocol (HTTP) <python_introduccion_http>` es el estándar de
comunicación utilizado en la web para la transferencia de información entre clientes (navegadores,
aplicaciones, scripts) y servidores. Python 3 ofrece varias bibliotecas para interactuar con servicios
HTTP, permitiendo realizar solicitudes y manejar respuestas de manera sencilla.

Solicitudes HTTP
-----------------

Al usar el ``HTTP``, podemos realizar diferentes tipos de solicitudes, como las siguiente:

+--------------+--------------------------------+
| **Método**   | **Explicación**                |
+--------------+--------------------------------+
| ``GET``      | Obtener datos de un servidor.  |
+--------------+--------------------------------+
| ``POST``     | Obtener datos de un servidor.  |
+--------------+--------------------------------+
| ``PUT``      | Actualizar recursos.           |
+--------------+--------------------------------+
| ``DELETE``   | Eliminar recursos.             |
+--------------+--------------------------------+


Bibliotecas disponibles
-----------------------

En Python, existen varias bibliotecas principales para interactuar con el protocolo HTTP.
Las más comunes son:

.. _python_http_client_lib:

**http.client**
'''''''''''''''

Python incluye la biblioteca estándar `http.client`_, que permite realizar solicitudes
HTTP de bajo nivel. Sin embargo, su uso es más complejo en comparación con
otras bibliotecas modernas.

Ejemplo de una solicitud ``GET`` con la biblioteca `http.client`_ desde la
:ref:`consola interactiva de Python <python_interactivo>`, ejecute el siguiente comando:

.. code-block:: pycon
   :class: no-copy

    >>> import http.client
    >>>
    >>> conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    >>> conn.request("GET", "/posts/1")
    >>>
    >>> response = conn.getresponse()
    >>> print(response.status, response.reason)
    >>> print(response.read().decode())
    >>>
    >>> conn.close()


----


.. _python_urllib:


**urllib**
'''''''''''

El módulo estándar `urllib`_ proporciona herramientas para manejar URLs y realizar
solicitudes HTTP. Es más fácil de usar que :ref:`http.client <python_http_client_lib>`,
pero sigue siendo más complejo que alternativas modernas.

Ejemplo con el módulo ``urllib.request`` desde la
:ref:`consola interactiva de Python <python_interactivo>`, ejecute el
siguiente comando:

.. code-block:: pycon
   :class: no-copy

    >>> import urllib.request
    >>>
    >>> url = "https://jsonplaceholder.typicode.com/posts/1"
    >>> response = urllib.request.urlopen(url)
    >>>
    >>> print(response.status)  # Código de estado HTTP
    >>> print(response.read().decode())  # Contenido de la respuesta


----


.. _python_requests:


**requests**
'''''''''''''

La biblioteca :ref:`requests <python_http_client_requests>` es la opción más popular y fácil
de usar para interactuar con HTTP en Python. No está incluida en la biblioteca estándar, ya
que es externa, más se puede instalar ejecutando el siguiente comando:

.. code-block:: console

    pip3 install requests


Ejemplo de una solicitud ``GET`` con la librería :ref:`requests <python_http_client_requests>`
desde la :ref:`consola interactiva de Python <python_interactivo>`, ejecute el siguiente
comando:

.. code-block:: pycon
   :class: no-copy

    >>> import requests
    >>>
    >>> url = "https://jsonplaceholder.typicode.com/posts/1"
    >>> response = requests.get(url)
    >>>
    >>> print(response.status_code)  # Código de estado HTTP
    >>> print(response.json())  # Respuesta en formato JSON


Ejemplo de una solicitud ``POST`` con la librería :ref:`requests <python_http_client_requests>`
desde la :ref:`consola interactiva de Python <python_interactivo>`, ejecute el siguiente comando:

.. code-block:: pycon
   :class: no-copy

    >>> import requests
    >>>
    >>> url = "https://jsonplaceholder.typicode.com/posts"
    >>> data = {"title": "Nuevo Post", "body": "Contenido del post", "userId": 1}
    >>>
    >>> response = requests.post(url, json=data)
    >>> print(response.status_code)
    >>> print(response.json())


Conclusión
----------

Python 3 ofrece múltiples formas de interactuar con el protocolo HTTP. Aunque los módulos
estándar (:ref:`http.client <python_http_client_lib>` y :ref:`urllib <python_urllib>`) son útiles,
la biblioteca :ref:`requests <python_requests>` es la opción más recomendada debido a su facilidad
de uso, soporte para autenticación, manejo de sesiones y compatibilidad con JSON.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`http.client`: https://docs.python.org/3/library/http.client.html
.. _`urllib`: https://docs.python.org/3/library/urllib.html
