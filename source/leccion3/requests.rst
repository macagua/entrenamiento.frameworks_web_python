.. _python_http_client_requests:

Librería requests
=================

La librería `requests`_ permite hacer peticiones mediante funciones que emulan los
métodos del protocolo HTTP, regresando un objeto que contiene los mensajes y datos
de la respuesta del servidor a modo de atributos.

``requests`` presenta funcionalidades avanzadas como autenticación, conexiones seguras,
manejo de 'cookies', etc.

Instalación
-----------

Para instalarlo ejecute el siguiente comando:

.. code-block:: console

    $ virtualenv --python /usr/bin/python3 venv
    $ source ./venv/bin/activate
    $ pip3 install -U pip
    $ pip3 install requests

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. code-block:: console

    $ python3 -c "import requests ; print(requests.__version__)"

Si muestra el numero de la versión instalada de ``requests``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.

----

Uso
---

Para usarla desde la :ref:`consola interactiva de Python <python_interactivo>`,
ejecute el siguiente comando:

.. code-block:: pycon

    >>> import requests

Puede consultar la ayuda del método ``GET`` de la librería, ejecute el siguiente comando:

.. code-block:: pycon

    >>> help(requests.get)

Eso da como resultado:

::

    Help on function get in module requests.api:

    get(url, params=None, **kwargs)
        Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response


Puede consultar la ayuda del método ``POST`` de la librería, ejecute el siguiente comando:

.. code-block:: pycon

    >>> help(requests.post)

Eso da como resultado:

::

    Help on function post in module requests.api:

    post(url, data=None, json=None, **kwargs)
        Sends a POST request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response



Ejemplos prácticos
-------------------

El sitio https://httpbin.org/ incluye ejemplos ilustrativos de los posibles
usos del protocolo HTTP.

request GET con response 200
''''''''''''''''''''''''''''

Se utilizará la función ``requests.get()`` en el sitio https://httpbin.org/headers
para abrir una conexión enviando una petición utilizando el método ``GET``. Se desplegarán
los siguientes datos guardados en el objeto resultante, asignado al nombre ``website_request``.

.. code-block:: pycon

    >>> website_request = requests.get("https://httpbin.org/headers")


Los encabezados de la petición contenidos en el atributo ``website_request.headers``.

.. code-block:: pycon

    >>> print(website_request.headers)

Eso da como resultado:

::

    {
        'Date': 'Sun, 16 Feb 2025 14:44:55 GMT',
        'Content-Type': 'application/json',
        'Content-Length': '225',
        'Connection': 'keep-alive',
        'Server': 'gunicorn/19.9.0',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

El mensaje de estado resultante contenido en el atributo ``website_request.status_code``.

.. code-block:: pycon

    >>> print(website_request.status_code)
    >>> 200

El contenido de la respuesta contenido en el atributo ``website_request.content``.

.. code-block:: pycon

    >>> print(website_request.content)



Eso da como resultado:

.. code-block:: pycon

    >>> b'{\n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.32.2", \n    "X-Amzn-Trace-Id": "Root=1-67b1f9e7-36514b17484bc9ac228fd167"\n  }\n}\n'

Se cerrará la conexión mediante el método ``website_request.close()``.

.. code-block:: pycon

    >>> website_request.close()

----

request GET recurso imágenes con response 200
'''''''''''''''''''''''''''''''''''''''''''''

Se utilizará ``requests.get()`` para obtener un recurso que corresponde a una imagen.

.. code-block:: pycon

    >>> pig_image_request = requests.get("https://httpbin.org/image/png")

Puede mostrar el contenido del request con lo siguiente:

.. code-block:: pycon

    >>> print(pig_image_request.content)

Para desplegar una imagen se utilizará la función ``Image`` del módulo ``iPython.display``.

**Nota:** El paquete ``IPython`` está disponible dentro de la paquete
`ipython <https://pypi.org/project/ipython/>`_. Para instalarlo ejecute el siguiente comando:

    .. code-block:: console

        $ pip3 install ipython

.. code-block:: pycon

    >>> from IPython.display import Image

.. code-block:: pycon

    >>> Image(pig_image_request.content)


Eso da como resultado:

    |pig_image_request_png|

Se cerrará la conexión mediante el método ``pig_image_request.close()``.

.. code-block:: pycon

    >>> pig_image_request.close()

----

request GET con response 404
''''''''''''''''''''''''''''

Se utilizará la función ``requests.get()`` en el sitio https://httpbin.org/get/1 (el cual no
existe) para abrir una conexión enviando una petición que incluye al método ``GET``. Se
desplegarán los siguientes datos guardados en el objeto resultante, asignado al nombre ``resource_request``.

-  El mensaje de estado resultante contenido en ``resource_request.status_code``.

-  El contenido del atributo ``resource_request.content``. En este caso, un mensaje de error.

En este caso se utilizará la declaración ``with`` para cerrar la conexión ta pronto se ejecute
el bloque de código inscrito.

.. code-block:: python

    with requests.get("https://httpbin.org/get/1") as resource_request:
        print(resource_request.status_code)
        print(resource_request.content)

Eso da como resultado:

.. code-block:: python

    404
    b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n'


----

request GET con response 302
''''''''''''''''''''''''''''

Se utilizará la función ``requests.get()`` para acceder a https://httpbin.org/redirect/5
(el cual hace un redireccionamiento a https://httpbin.org/redirect/4) para abrir una
conexión enviando una petición con el método ``GET``. Se desplegarán los siguientes datos guardados
en el objeto resultante, asignado al nombre ``request_redirect``.

-  El mensaje de estado resultante, perteneciente a ``request_redirect.status_code``.

-  Los encabezados de la petición pertenecientes a ``request_redirect.headers``.

En este caso se utilizará la declaración ``with`` para cerrar la conexión ta pronto se
ejecute el bloque de código inscrito.

.. code-block:: python

    with requests.head("https://httpbin.org/redirect/5") as request_redirect:
        print(request_redirect.status_code)
        print(request_redirect.headers)

Eso da como resultado:

::

    302
    {
        'Date': 'Sun, 16 Feb 2025 14:55:27 GMT',
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': '247',
        'Connection': 'keep-alive',
        'Server': 'gunicorn/19.9.0',
        'Location': '/relative-redirect/4',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }


----

request POST con response 200
'''''''''''''''''''''''''''''

Se utilizará ``requests.post()`` para enviar datos en formato JSON
utilizando el método ``POST`` a https://httpbin.org. El servidor enviará
de regreso el contenido de la petición.

.. code-block:: pycon


    >>> import requests
    >>>
    >>> url = "https://httpbin.org/post"
    >>> data = {"saludo": "Hola"}
    >>>
    >>> response = requests.post(url, json=data)
    >>> print(response.status_code)
    >>> print(response.json())


Eso da como resultado:

::

    200
    {
        'args': {},
        'data': '{"saludo": "Hola"}',
        'files': {},
        'form': {},
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '18',
            'Content-Type': 'application/json',
            'Host': 'httpbin.org',
            'User-Agent': 'python-requests/2.32.2',
            'X-Amzn-Trace-Id': 'Root=1-67b150b3-28bbeb2d4beea271757039a4'
        },
        'json': {'saludo': 'Hola'},
        'origin': '81.61.15.74',
        'url': 'https://httpbin.org/post'
    }

----

Manejo de errores y excepciones
-------------------------------

Al realizar solicitudes HTTP con `requests`_, es importante manejar errores y excepciones.
Por ejemplo desde la :ref:`consola interactiva de Python <python_interactivo>`,
ejecute el siguiente comando:

.. code-block:: pycon

    >>> import requests
    >>>
    >>> url = "https://httpbin.org/post"
    >>> data = {"saludo": "Hola"}
    >>>
    >>> try:
    ...     response = requests.post(url, json=data)
    ...     response.raise_for_status()
    ...     print(response.status_code)
    ...     print(response.json())
    ... except requests.exceptions.RequestException as e:
    ...     print(f"Error en la solicitud: {e}")
    ...


Eso da como resultado:

::

    200
    {
        'args': {}, 'data': '{"saludo": "Hola"}',
        'files': {},
        'form': {},
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '18',
            'Content-Type': 'application/json',
            'Host': 'httpbin.org',
            'User-Agent': 'python-requests/2.32.2',
            'X-Amzn-Trace-Id': 'Root=1-67b21619-720c122a355c14eb3ebf11c6'
        },
        'json': {'saludo': 'Hola'},
        'origin': '81.61.15.74',
        'url': 'https://httpbin.org/post'
    }


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


.. disqus::


.. |pig_image_request_png| image:: ../_static/images/cerdo.png
   :class: image-inline
   :alt: Imagen generada
   :align: middle

.. _`requests`: https://docs.python-requests.org/en/latest/
