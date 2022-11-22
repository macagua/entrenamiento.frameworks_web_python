.. _python_http_clients:

Clientes HTTP
=============

Existen varias herramientas clientes para el protocolo

.. _python_http_client_curl:

Cliente cURL
============

- Escrito en C y usa la libreria ``libcurl``.

- Admite muchos otros protocolos además de HTTP(S).

- Admite cualquier cantidad de URL en la línea de comando.

- Puede enviar POST binarios.

- Admite múltiples métodos HTTP en una sola línea de comando para diferentes URL.

- Documentado en una página man para documentación fuera de línea.

- Admite solicitudes HTTP/1.0.

- Características URL "globbing" para rangos y secuencias.

- Permite modificaciones de encabezado más invasivas, como pasar letras no válidas en encabezados personalizados ( Höst:), reemplazar Content-Length:en un POST y eliminar el Host:encabezado de una solicitud. O simplemente agregar un encabezado sin espacio después de los dos puntos.

- Admite globos oculares felices o uso explícito de ipv4/ipv6.

- Admite trucos de conexión personalizados como --resolve y --connect-to.

- Compatibilidad con HTTP/2 (tanto para HTTP:// como para HTTPS:// URL).

- Compatibilidad con HTTP/3.

- Ofrece compresión usando gzip, brotli y zstd.

- Se envía de forma predeterminada en macOS y Windows 10.


.. _python_http_client_httpie:

Cliente httpie
==============

HTTPie (pronunciado aitch-tee-tee-pie) es un cliente HTTP de línea de
comandos sustituto del `cURL <https://curl.se/>`_. Su objetivo es
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
---------------

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
-----------

Es una aplicación Python, por lo que puedo instalarla con:

.. code-block:: console

    $ pip3 install httpie

Uso
---

Una vez instalado podéis ejecutar el "Hello World":

.. code-block:: console

    $ http httpie.org

El uso de la herramienta tiene la siguiente sintaxis,

.. code-block:: console

    $ http [flags] [metodo] <url> [item [item]]


.. todo::
    TODO Terminar de escribir sobre el paquete "httpie".


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
