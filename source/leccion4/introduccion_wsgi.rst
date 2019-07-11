.. _python_introduccion_wsgi:

Introducción a WSGI
===================

Debajo de frameworks como Django, Flask, Bottle y cualquier otro framework web 
de Python, se encuentra el Web Server Gateway Interface, o WSGI, para abreviar. 
WSGI es para Python lo que son Servlets para Java: una especificación común para 
servidores web que permite que diferentes servidores web y framework de aplicaciones 
interactúen según una API común. Sin embargo, como con la mayoría de las cosas, 
la versión de Python es considerablemente más simple.

WSGI se define en PEP 3333, que le recomiendo que lea como referencia si desea 
obtener más información después de esta introducción rápida.

WSGI no es un servidor, un módulo de Python, un framework, una API o cualquier tipo 
de software. Es solo una especificación de interfaz mediante la cual el servidor y 
la aplicación se comunican. Tanto el lado del servidor como la interfaz de la 
aplicación se especifican en el PEP 3333. Si se escribe una aplicación (o framework 
o kit de herramientas) en la especificación WSGI, se ejecutará en cualquier servidor 
escrito en esa especificación.

.. _python_wsgi_app:

Aplicaciones WSGI
------------------

Las aplicaciones WSGI (lo que significa que cumplen con el WSGI) se pueden apilar. 
Los que están en la mitad de la pila se denominan middleware y deben implementar 
ambos lados de la interfaz, la aplicación y el servidor WSGI. Para la aplicación 
que se encuentra en la parte superior, se comportará como un servidor y para la 
aplicación (o servidor) a continuación como una aplicación.


.. _python_wsgi_server:

Servidor WSGI
--------------

Un servidor WSGI (lo que significa que cumple con el WSGI) solo recibe la solicitud 
del cliente, la pasa a la aplicación y luego envía la respuesta devuelta por la 
aplicación al cliente. No hace nada más. Todos los detalles explicitos deben ser 
suministrados por la aplicación o middleware.

No es necesario conocer la especificación WSGI para crear aplicaciones sobre frameworks 
o kits de herramientas. Para usar middleware, se debe tener una comprensión mínima de 
cómo apilarlos con la aplicación o el marco, a menos que el framework ya esté integrado 
o el framework proporcione algún tipo de envoltorio para integrar los que no lo están.

Python 2.5 y versiones posteriores vienen con un servidor WSGI que se utilizará en 
este tutorial. En 2.4 y anteriores se puede instalar. Para el código de producción, 
emplee un estándar probado en la industria como Apache con ``mod_wsgi``.

Todo el código en este tutorial es de bajo nivel y tiene el único propósito de demostrar 
la especificación WSGI en funcionamiento. No es para uso real. Para código de producción, 
apéguese a kits de herramientas, frameworks y middleware.


.. todo::
    TODO Terminar de escribir la sección "Introducción a WSGI".
