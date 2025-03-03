.. _python_http_client_httpie:

Cliente httpie
--------------

`HTTPie`_ (pronunciado aitch-tee-tee-pie) es un :ref:`cliente HTTP <python_http_client>`
de línea de comandos sustituto del :ref:`cURL <python_http_client_curl>`. Su objetivo es
hacer que la interacción de CLI con los servicios web sea lo más amigable
posible para los usuarios.

.. figure:: ../_static/images/httpie_vs_curl.png
  :class: image-inline
  :alt: HTTPie vs cURL
  :align: center

  HTTPie vs cURL

Proporciona un simple comando ``http`` que permite enviar solicitudes
HTTP arbitrarias utilizando una sintaxis simple y natural, y muestra
resultados en color. HTTPie se puede usar para probar, depurar y, en
general, interactuar con servidores HTTP.

Características
'''''''''''''''

HTTPie consiste en un solo comando ``http`` diseñado para la depuración
e interacción sin problemas con los servidores HTTP, las API RESTful y
los servicios web, lo cual logra mediante las siguientes características
principales:

- Sintaxis de comando expresiva e intuitiva.

- Salida de terminal formateada y coloreada.

- Soporte JSON incorporado.

- Formularios y archivos subidos.

- HTTPS, proxies y soporte de autenticación.

- Datos de solicitud arbitrarios.

- Encabezados personalizados.

- Sesiones persistentes.

- Descargas tipo Wget.

- Soporte Python 2.7 y 3.x.

- Soporte para datos de solicitud arbitrarios y encabezados.

- Soporte para Linux, macOS y Windows.

- Extensiones (Plugins).

- Documentación.

- Cobertura de prueba (Test coverage).


Instalación
'''''''''''

Es una aplicación Python de línea de comando, por lo que puedo instalarla con:

.. code-block:: console

    virtualenv --python /usr/bin/python3 venv && source ./venv/bin/activate

Es una aplicación de línea de comando, por lo que puedo instalarla con el siguiente
comando:

.. code-block:: console

    pip3 install httpie

Una vez instalado puedes ejecutar con el siguiente comando:

.. code-block:: console

    http --version

Si muestra el numero de la versión instalada de ``http``, tiene
correctamente instalada la herramienta.

Uso
'''

Con esta interfaz de línea de comandos (o CLI), puede especificarse la URL de un servidor
(es decir, la ubicación a la que se envía la solicitud) y los datos que se van a enviar a
ese servidor.

.. code-block:: console

    http https://httpie.io/

Aunque las plataformas API suelen tener interfaces muy intuitivas para solicitar y transferir
datos a una URL, el comando ``http`` puede ser una herramienta muy útil para usar con el
terminal, y estos son algunos de sus usos más comunes.


Guardar contenido de una URL
*****************************

De la misma forma en que puedes usar el comando ``http`` para descargar imágenes, puedes guardar
el contenido de una URL (como una página web) en un archivo. Este es un ejemplo que usa la
página de proyecto ``http``:

.. code-block:: console

    http -o httpie.html https://httpie.io/

En este ejemplo, el código de origen de la página de proyecto ``http`` se guarda en un archivo
denominado :file:`httpie.html`.


----


Descargar ficheros a un dispositivo
************************************

Como el terminal tiene acceso al sistema de archivos, también puedes descargar imágenes fácilmente
desde direcciones URL.

Por ejemplo, esta es la URL del logotipo de Python.org, y con el comando ``http``, puedes descargar
un archivo comprimido de la siguiente forma:

.. code-block:: console

    http -d https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tar.xz

Con el comando ``http`` y la URL de un archivo comprimido, pueden obtenerse los datos binarios del
archivo comprimido y almacenarse en el disco duro con el mismo nombre del archivo original ``Python-3.11.11.tar.xz``.

Por ejemplo, esta es la URL del logotipo de Python.org, y con el comando ``http``, puedes descargar
la imagen de la siguiente forma:

.. code-block:: console

    http -d https://www.python.org/static/img/python-logo.png -o python-logo.png

Con el comando ``http`` y la URL de la imagen, pueden obtenerse los datos binarios del logotipo y
almacenarse en un archivo de imagen (con una extensión ``.png`` como la del archivo original) que
luego puede guardarse en el disco duro.


----


Probar rápidamente una API desde el terminal
********************************************

Como ya hemos visto, el comando ``http`` permite probar rápidamente una API desde el terminal sin
tener que descargar una aplicación específica.


request GET con response 200
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    http GET https://jsonplaceholder.typicode.com/todos/1

request POST formato x-www-form-urlencoded
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    http --form POST https://jsonplaceholder.typicode.com/posts name='HTTPie' type='article'

request POST formato json
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    echo -n '{"name": "HTTPie", "type": "article"}' | http POST https://jsonplaceholder.typicode.com/posts

request PUT formato json
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    http PUT https://jsonplaceholder.typicode.com/posts/1 Content-Type:application/json <<< '{"name": "JSON", "type": "post"}'

request DELETE
^^^^^^^^^^^^^^^

.. code-block:: console

    http DELETE https://jsonplaceholder.typicode.com/posts/1


De esta forma aprendió a usar el comando ``http``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`HTTPie`: https://httpie.io/
