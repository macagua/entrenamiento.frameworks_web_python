.. _python_http_client_curl:

Cliente cURL
------------

`cURL`_, *el comando cURL (Client URL o cURL)*, es un
:ref:`cliente HTTP <python_http_client>` por línea de comandos el cual
permite el intercambio de datos entre un dispositivo y un servidor a través
de un terminal de comando.


.. figure:: ../_static/images/curl_logo.svg
  :class: image-inline
  :alt: cURL
  :align: center

  cURL

Características
'''''''''''''''

- Escrito en `C <https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)>`_ y usa
  la librería ``libcurl``.

- Admite muchos otros protocolos además de HTTP(S).

- Admite cualquier cantidad de URL en la línea de comando.

- Puede enviar ``POST`` binarios.

- Admite múltiples métodos HTTP en una sola línea de comando para diferentes URL.

- Documentado en una página man para documentación fuera de línea.

- Admite solicitudes HTTP/1.0.

- Características URL "globbing" para rangos y secuencias.

- Permite modificaciones de encabezado más invasivas, como pasar letras no válidas
  en encabezados personalizados (Höst:), reemplazar Content-Length:en un ``POST``
  y eliminar el Host:encabezado de una solicitud. O simplemente agregar un encabezado
  sin espacio después de los dos puntos.

- Admite globos oculares felices o uso explícito de ipv4/ipv6.

- Admite trucos de conexión personalizados como --resolve y --connect-to.

- Compatibilidad con HTTP/2 (tanto para ``HTTP://`` como para ``HTTPS://`` URL).

- Compatibilidad con HTTP/3.

- Ofrece compresión usando ``gzip``, ``brotli`` y ``zstd``.

- Se envía de forma predeterminada en macOS y Windows 10.


Instalación
'''''''''''

Es una aplicación de línea de comando, por lo que puedo instalarla con el siguiente comando:

.. code-block:: console

    $ sudo apt update && sudo apt upgrade -y
    $ sudo apt install -y curl

Una vez instalado puedes ejecutar con el siguiente comando:

.. code-block:: console

    $ curl --version

Si muestra el numero de la versión instalada de ``curl``, tiene
correctamente instalada la herramienta.

Uso
'''

Con esta interfaz de línea de comandos (o CLI), puede especificarse la URL de un servidor
(es decir, la ubicación a la que se envía la solicitud) y los datos que se van a enviar a
ese servidor.

.. code-block:: console

    $ curl https://curl.se/

Aunque las plataformas API suelen tener interfaces muy intuitivas para solicitar y transferir
datos a una URL, el comando ``curl`` puede ser una herramienta muy útil para usar con el
terminal, y estos son algunos de sus usos más comunes.


Guardar contenido de una URL
*****************************

De la misma forma en que puedes usar el comando ``curl`` para descargar imágenes, puedes guardar
el contenido de una URL (como una página web) en un archivo. Este es un ejemplo que usa la
página de proyecto ``curl``:

.. code-block:: console

    $ curl -o curl.html https://curl.se/

En este ejemplo, el código de origen de la página de proyecto ``curl`` se guarda en un archivo
denominado :file:`curl.html`.

----

Descargar ficheros a un dispositivo
************************************

Como el terminal tiene acceso al sistema de archivos, también puedes descargar imágenes fácilmente
desde direcciones URL.

Por ejemplo, esta es la URL del logotipo de Python.org, y con el comando ``curl``, puedes descargar
la imagen de la siguiente forma:

.. code-block:: console

    $ curl https://www.python.org/static/img/python-logo.png > python-logo.png

Con el comando ``curl`` y la URL de la imagen, pueden obtenerse los datos binarios del logotipo y
almacenarse en un archivo de imagen (con una extensión ``.png`` como la del archivo original) que
luego puede guardarse en el disco duro.


----

Probar rápidamente una API desde el terminal
********************************************

Como ya hemos visto, el comando ``curl`` permite probar rápidamente una API desde el terminal sin
tener que descargar una aplicación específica.


request GET con response 200
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ curl -X GET https://jsonplaceholder.typicode.com/todos/1

request POST formato x-www-form-urlencoded
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ curl -X POST -d "name=cURL&type=article" https://jsonplaceholder.typicode.com/posts

request POST formato json
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ curl -X POST -d '{"name": "cURL", "type": "article"}' -H "Content-Type: application/json" https://jsonplaceholder.typicode.com/posts

request PUT formato json
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ curl -X PUT -d '{"name": "json", "type": "post"}' -H "Content-Type: application/json" https://jsonplaceholder.typicode.com/posts/1

request DELETE
^^^^^^^^^^^^^^^

.. code-block:: console

    $ curl -X DELETE https://jsonplaceholder.typicode.com/posts/1


De esta forma aprendió a usar el comando ``curl``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


.. disqus::

.. _`cURL`: https://curl.se/
