"""Source code taken and improvements from the article
"Understanding Python WSGI with Examples" by Edd Mann at
https://eddmann.com/posts/understanding-python-wsgi-with-examples/
"""

# Server IP
HOST_NAME = "127.0.0.1"
# Server port
PORT_NUMBER = 8080
# HTTP Status
STATUS = "200 OK"
# HTTP Headers
HEADERS = [("Content-Type", "text/html")]


def application(environ, start_response):
    # Start the response
    start_response(STATUS, HEADERS)
    return [b"Hello, world!"]


def run():
    """Run WSGI Server"""
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
        server.serve_forever()
    except KeyboardInterrupt:
        print(" <Ctrl-C> entered, stopping WSGI Server...")
        if server:
            # Close the server
            server.socket.close()


if __name__ == "__main__":
    """Starting WSGI server"""
    run()
else:
    print(
        "This script should be run directly and not imported as a module.\n"
        "Please execute it using 'python wsgi_hello_world_get_request.py'."
    )
