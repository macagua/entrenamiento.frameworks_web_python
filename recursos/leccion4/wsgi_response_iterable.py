"""Python's bundled WSGI server

Source code taken and improvements from the
"WSGI Tutorial" by Clodoaldo Pinto Neto at
https://wsgi.tutorial.codepoint.net/response-iterable
"""

# Server IP
HOST_NAME = "localhost"
# Server port
PORT_NUMBER = 8080
# HTTP Status
STATUS = "200 OK"


def application(environ, start_response):
    # Sorting and stringifying the environment key, value pairs
    response_body = [f"{key}: {value}" for key, value in sorted(environ.items())]
    response_body = "\n".join(response_body)
    # Adding strings to the response body
    response_body = [
        "The Beginning\n",
        "*" * 30 + "\n",
        response_body,
        "\n" + "*" * 30,
        "\nThe End",
    ]
    # So the content-length is the sum of all string's lengths
    content_length = sum(len(s) for s in response_body)
    # HTTP Headers
    RESPONSE_HEADERS = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(content_length)),
    ]
    # Start the response
    start_response(STATUS, RESPONSE_HEADERS)
    return [s.encode("utf-8") for s in response_body]


server = None
try:
    from wsgiref.simple_server import make_server

    # Instantiate the server
    server = make_server(
        HOST_NAME,  # The host name
        PORT_NUMBER,  # A port number where to wait for the request
        application,  # The application object name, in this case a function
    )
    print(
        f" WSGI Server running on http://{HOST_NAME}:{PORT_NUMBER}/ use <Ctrl-C> to stop."
    )
    # Server serve forever
    server.serve_forever()
    # Wait for a single request, serve it and quit
    server.handle_request()
except KeyboardInterrupt:
    print(" <Ctrl-C> entered, stopping WSGI Server...")
    if server:
        # Close the server
        server.socket.close()
