.. _python_requests:

Librería requests
=================

La librería `requests <http://docs.python-requests.org>`_ permite hacer peticiones
mediante funciones que emulan los métodos del protocolo HTTP, regresando un objeto
que contiene los mensajes y datos de la respuesta del servidor a modo de atributos.

``requests`` presenta funcionalidades avanzadas como autenticación, conexiones seguras,
manejo de 'cookies', etc.

Para instalarlo ejecute el siguiente comando:

.. code-block:: console

    $ pip3 install requests


Para usarla desde la consola interactiva de comando Python, ejecute el siguiente comando:

.. code-block:: pycon

    >>> import requests

Puede consultar la ayuda del método *GET* de la librería, ejecute el siguiente comando:

.. code-block:: pycon

    >>> help(requests.get)

Eso da como resultado:

::

    Help on function get in module requests.api:

    get(url, params=None, **kwargs)
        Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response

**Ejemplo:**

Se utilizará la función ``requests.get()`` en el sitio `https://python.org/ <https://python.org/>`_
para abrir una conexión enviando una petición utilizando el método *GET*. Se desplegarán
los siguientes datos guardados en el objeto resultante, ligado al nombre ``sitio``.

.. code-block:: pycon

    >>> sitio = requests.get("https://python.org/")


Los encabezados de la petición contenidos en el atributo ``sitio.headers``.

.. code-block:: pycon

    >>> print(sitio.headers)

Eso da como resultado:

::

    {
        'Connection': 'keep-alive',
        'Content-Length': '50872',
        'Server': 'nginx',
        'Content-Type': 'text/html; charset=utf-8',
        'X-Frame-Options': 'DENY',
        'Via': '1.1 vegur, 1.1 varnish, 1.1 varnish',
        'Accept-Ranges': 'bytes',
        'Date': 'Fri, 11 Nov 2022 05:44:23 GMT',
        'Age': '868',
        'X-Served-By': 'cache-iad-kiad7000025-IAD, cache-pdk17821-PDK',
        'X-Cache': 'HIT, HIT',
        'X-Cache-Hits': '424, 2',
        'X-Timer': 'S1668145464.920838,VS0,VE0',
        'Vary': 'Cookie',
        'Strict-Transport-Security': 'max-age=63072000; includeSubDomains'
    }


El mensaje de estado resultante contenido en el atributo ``sitio.status_code``.

.. code-block:: pycon

    >>> print(sitio.status_code)

El contenido de la respuesta contenido en el atributo ``sitio.content``.

.. code-block:: pycon

    >>> print(sitio.content)


Eso da como resultado:

.. code-block:: pycon

    >>> b'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" lang="es" xml:lang="es">\n  <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <title>Cursos Pythonista \xe2\x80\x94 Pythonista</title>\n    <link rel="shortcut icon" type="image/x-icon" href="/++theme++barceloneta/barceloneta-favicon.ico" />\n    <link rel="apple-touch-icon" href="/++theme++barceloneta/barceloneta-apple-touch-icon.png" />\n    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/++theme++barceloneta/barceloneta-apple-touch-icon-144x144-precomposed.png" />\n    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/++theme++barceloneta/barceloneta-apple-touch-icon-114x114-precomposed.png" />\n    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/++theme++barceloneta/barceloneta-apple-touch-icon-72x72-precomposed.png" />\n    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="/++theme++barceloneta/barceloneta-apple-touch-icon-57x57-precomposed.png" />\n    <link rel="apple-touch-icon-precomp <a href="http://plone.com" target="_blank" title="Este sitio ha sido construido usando el CMS/WCM de Fuentes Abiertos Plone.">Powered by Plone &amp; Python</a>\n    </div>\n  </section>\n\n\n  \n\n</div>\n\n\n\t</div>\n</div>\n\n<script>\n  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n  })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');\n\n  ga(\'create\', \'UA-100381738-1\', \'auto\');\n  ga(\'send\', \'pageview\');\n\n</script>\n    </div>\n    </footer></body>\n</html>'


Se cerrará la conexión mediante el método ``sitio.close()``.

.. code-block:: pycon

    >>> sitio.close()


**Ejemplo:**

Se utilizará la función requests.get() en el sitio https://python.org/ (la cual no
existe) para abrir una conexión enviando una petición que incluye al método *GET*. Se
desplegarán los siguientes datos guardados en el objeto resultante, ligado al nombre ``sitio``.

-  El mensaje de estado resultante contenido en ``sitio.status_code``.

-  El contenido del atributo ``sitio.content``. En este caso, un mensaje de error.

En este caso se utilizará la declaración ``with`` para cerrar la conexión ta pronto se ejecute
el bloque de código inscrito.

.. code-block:: python

    with requests.get("https://python.org/") as sitio:
        print(sitio.status_code)
        print(sitio.content)

Eso da como resultado:

.. code-block:: python

    404
    b'{{"error_type": "NotFound"}}'



**Ejemplo:**

Se utilizará la función requests.get() para acceder
a https://www.python.org/ (el cual hace un redireccionamiento
a `https://python.org/ <https://python.org/>`_) para abrir una
conexión enviando una petición con el método *GET*. Se desplegarán los
siguientes datos guardados en el objeto resultante, ligado al
nombre ``sitio``.

-  El mensaje de estado resultante, perteneciente a ``sitio.status_code``.

-  Los encabezados de la petición pertenecientes a ``sitio.headers``.

En este caso se utilizará la declaración ``with`` para cerrar la conexión ta pronto se
ejecute el bloque de código inscrito.

.. code-block:: python

    with requests.head("https://python.org/") as sitio:
        print(sitio.status_code)
        print(sitio.headers)

Eso da como resultado:

.. code-block:: pycon

    301
    {'Date': 'Thu, 22 Feb 2018 19:19:13 GMT', 'Server': 'Apache/2.4.18 (Ubuntu)', 'Location': 'https://pythonista.io/', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html; charset=iso-8859-1'}


Ejemplos prácticos para el uso de HTTP
--------------------------------------

El sitio https://httpbin.org/ incluye ejemplos ilustrativos de los posibles
usos del protocolo HTTP.

**Ejemplo:**

Se utilizará ``requests.get()`` para obtener un recurso que corresponde
a una imagen.

.. code-block:: pycon

    >>> cerdo = requests.get("https://httpbin.org/image/png")

.. code-block:: pycon

    >>> print(cerdo.content)

Eso da como resultado:

.. code-block:: pycon

    >>> b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00d\x00\x00\x00d\x08\x02\x00\x00\x00\xff\x80\x02\x03\x00\x00\x1faIDATx\x9c\xdd}wXS\xd9\xd6\xfeJ#\xa1\x17\xc1 \x02\xa1\x08\xc1J\x19\x11E\x10\x1c\x11\x14\x10\xf8tl(\xea\xd8FGGT\xac\x9f\\\xeb\x8c\x0eV\xd4\xb1\xdca\xe4\n\xb6\x11\x1bEA\x14QA\x94&\x82\xa2B\x00EzoI \x10\x92\xf3\xfbc\x87\x10!\xc4$D\x7fw\xbe\xf7\xe1\xe199gg\xadu\xde\xb3\xf7>{\xaf\xbd\xd6\x0e\x0e\xc30\x00`\xb3\xd9\xc7\x8e\x1dKJJ\xca\xc9\xc9\xe9\xec\xec$\x93\xc9\x14\n\x85\xdc\x03UUU\x1a\x8dfjjjbbbjj\x8a\x0eTTT`\x10\xc00\xac\xbc\xbc\xbc\xb0\xb0\x90\xc1`0\x18\x8c\xf2\xf2r&\x93\xc9b\xb1\x98L&\x93\xc9\xe4\xf3\xf9\xea"000\xb0\xec\x81\x89\x89\t\x81@\x18\x8c\xea\xf6\xf6\xf6\xd2\xd2\xd2\x8f\x1f?~\xfc\xf8\x11\x1d|\xfa\xf4\x89\xcdfw\x8a\x80\xc3\xe1\x90\xc9d;;;77\xb7\xa0\xa0 UUU\x81\xd1\xa9\xa9\xa9&&&2\xe9\xc3\xe3\xf1vvvAAAw\xef\xdemmm\xc5\xa4Fyy\xf9\x993g\xa6O\x9f\xae\xac\xac,\xdf\xad*))9;;\x1f;v\xac\xa4\xa4Dz\xbd\xad\xad\xadw\xef\xde\r\n\n\xb2\xb3\xb3\xc3\xe3\xf12i411IMM\xc50\x0c\xc7f\xb3\xad\xac\xac\xca\xcb\xcb\x01\xc0\xd6\xd4t2\x9d\xae\xa9\xa2\xc2\xe1r;\xb9\xdcN.\x17\x1d\xb4wu\x9574|\xac\xabk\xeb\xe8\xe8/\x8b@ \xd8\xd9\xd9yyy-_\xbe\xdc\xc8\xc8H\xac\xbe\xfc\xfc\xfc\xe8\xe8\xe8\x98\x98\x98\xec\xec\xec\xfeWU\xc9d\x9a\x9e\x9e\x86\xb2\xb2\x86\x8a\x8a:\x85\xa2\xa1\xa2\x82\x03`r8m\xed\xed\xe8\x7fYC\x83X\xd5c\xc6\x8c\xf1\xf3\xf3\xf3\xf5\xf5\x1d?~\xbcX\xbd\xe5\xe5\xe5\xe1\xe1\xe1\xf7\xee\xdd\xcb\xc9\xc9\xe1\xf1x\xfd\x0bh(+\x9b\x0e\x1dj\xa4\xab\xab\xa2\xa4D&\x91($\x12\x99DB\x07\xad\xed\xedi\x85\x85\xaf>~\x04\x00##\xa3\x82\x82\x02\xdc\xbe}\xfb\xf6\xec\xd9\x03\x00!\x8b\x16m\xf3\xf5\x1d\x90^\x00\x00hb\xb1J\xeb\xeb?\xd6\xd5\xbd)+{\xf2\xf6mzQQ\'\x97+\xbc\x8a\xc7\xe3g\xce\x9c\xb9z\xf5j///\x02\x81\xc0\xe3\xf1\xd2\xd2\xd2bbbbbbJJJD\xe5\x18\xeb\xea\xce\xb0\xb1\x19cdd5|\xb8\xd5\xf0\xe1\x86::8\x1cN\xb2\xea\xea\xe6\xe6\x82\xaa\xaa\xc2\xaa\xaaw\x15\x15\x0f\xf2\xf2\n\xab\xaaD\xaf\x1a\x1a\x1a\xfa\xf8\xf8\xf8\xf9\xf9\xb9\xba\xba\x92H$\x1e\x8fw\xef\xde\xbd?\xff\xfc3!!\x81\xcf\xe7\x0b\x8b\x91I\xa4\x89\x16\x16\xae\xa3G\x8f566\x1d:\xd4DOOGMM\xb2\xde\xc311\xdb\xaf\\\x01\x80}\xfb\xf6\xe1\xa6L\x99\x92\x92\x922\x8eF\xcb=|\x18Y\\\xd1\xd8\xf8Wr\xf2\xd3w\xef\xf08\x1c\x1e\x87\xc3\xe3\xf1d"\xd1\xd6\xd4t\x92\xa5\xa5\x83\x85\x856j\xbd\x00\x00\xc0\xe1r\x9f\x17\x16>~\xfb6177K\x84\x0e\x03\x03\x03{{\xfb\x97/_VTT\x88*\xb6\xa6\xd1|\xed\xed\xfd\xec\xedmMM%\x9b\xf8E\x14TV\xc6dgGgff\x14\x17\xa3n\x17AWW\xd7\xde\xde>77\xb7\xba\xbaZx\xd2\xde\xdc\xdc\xc3\xc6f\xea\xe8\xd1\x8et:\x85D\x02\x80f6;\x9d\xc1H/*z\xc1`d\x16\x17\xb7\xb6\xb7\x0b\x0b\x9bQ\xa9\xcb\xa7N\xdd0s\xa6\xba\xb22\x00`\x18f\xb3m\xdb\xebO\x9f\xa6L\x99\x82\xb3\xb0\xb0(**\n\x982%r\xfdz\x00\xc8\xfb\xf4i\xfc\x8e\x1d\xdd\xe2j,\x00\xe0p8\xba\x81\xc1\xb41c\xd6\xcd\x981r\xf8p\xd1Ko\xca\xca\xfeLJ\xba\x9c\x9a\xda\xc2f\x8b\x9e\'\x12\x08\xceVV~\x13&\xf8\x8c\x1fo\xa2\xa77H\x8e\xfa\xa3\xa6\xa5%6;;:++9?_\xb4\x9a\x03\x80\x96\xaa\xeabg\xe7\xd5nnc\x8d\x8d\xd1\x19>\x86\xdd\xcb\xc99\x9d\x90\96(ZZZ\x18\x0c\x06\xfa\x99\xd1\xc2\xc2\xc2\x8a\x8a\n)\x7ff\xd4\xd2\xd2\xf2\xeb54\xc9\xf8\x7f\xba\xe7w\xc2\x98Sl\xa3\x00\x00\x00\x00IEND\xaeB`\x82'

Para desplegar una imagen se utilizará la función ``Image`` del módulo ``iPython.display``.

**Nota:** El paquete ``IPython`` sólo está disponible si se tiene instalado iPython o Jupyter.

.. code-block:: pycon

    >>> from IPython.display import Image

.. code-block:: pycon

    >>> Image(cerdo.content)


Eso da como resultado:

    |cerdo_png|

Se cerrará la conexión mediante el método ``cerdo.close()``.

.. code-block:: pycon

    >>> cerdo.close()

**Ejemplo:**

Se utilizará ``requests.post()`` para enviar datos en formato JSON
utilizando el método *POST* a https://httpbin.org. El servidor enviará
de regreso el contenido de la petición.

.. code-block:: pycon

    >>> respuesta = requests.post("https://httpbin.org/post", json = {"saludo": "Hola"})

.. code-block:: pycon

    >>> respuesta.json()

Eso da como resultado:

::

    {
        'args': {},
        'data': '{"saludo": "Hola"}',
        'files': {},
        'form': {},
        'headers': {'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Length': '18',
        'Content-Type': 'application/json',
        'Host': 'httpbin.org',
        'User-Agent': 'python-requests/2.22.0'},
        'json': {'saludo': 'Hola'},
        'origin': '200.82.210.213, 200.82.210.213',
        'url': 'https://httpbin.org/post'
    }

.. |cerdo_png| image:: ../_static/images/cerdo.png
   :class: image-inline
   :alt: Imagen generada
   :align: middle

.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
