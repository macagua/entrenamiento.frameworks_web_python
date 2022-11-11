#!/usr/bin/env python

"""
Python's bundled WSGI server

Source code taken and improvements from the
"WSGI Tutorial" by Clodoaldo Pinto Neto at
http://wsgi.tutorial.codepoint.net/environment-dictionary
"""

# Server IP
HOST_NAME = "127.0.0.1"
# Server port
PORT_NUMBER = 8080

from wsgiref.simple_server import make_server


def application(environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    response_body = [f"{key}: {value}" for key, value in sorted(environ.items())]
    response_body = "\n".join(response_body)

    status = "200 OK"
    response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body))),
    ]
    start_response(status, response_headers)

    # return [response_body]
    return response_body


# Instantiate the server
httpd = make_server(
    "localhost",  # The host name
    8080,  # A port number where to wait for the request
    application,  # The application object name, in this case a function
)

# Wait for a single request, serve it and quit
httpd.handle_request()
