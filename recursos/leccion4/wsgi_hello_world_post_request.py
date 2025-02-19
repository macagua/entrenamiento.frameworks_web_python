"""Source code taken and improvements from the article
"Understanding Python WSGI with Examples" by Edd Mann at
https://eddmann.com/posts/understanding-python-wsgi-with-examples/
"""

from urllib.parse import parse_qs

# Server IP
HOST_NAME = "127.0.0.1"
# Server port
PORT_NUMBER = 8080

# Form HTML
form = b"""<!DOCTYPE html>
<html>
    <head>
        <title>Hello User!</title>
    </head>
    <body>
        <form method="post">
            <label>Hello</label>
            <input type="text" name="name">
            <input type="submit" value="Go">
        </form>
    </body>
</html>\n"""


def application(environ, start_response):
    html_document = form

    if environ["REQUEST_METHOD"] == "POST":
        try:
            request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        except (ValueError):
            request_body_size = 0
        # Read the request body
        request_body = environ["wsgi.input"].read(request_body_size)
        post = parse_qs(request_body.decode("utf-8"))
        name = post.get("name", ["World"])[0]
        html_document = b"Hello, " + bytes(name, "utf-8") + b"!"
    # Start the response
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return [html_document]


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
            server.socket.close()


if __name__ == "__main__":
    """Starting WSGI server"""
    run()
else:
    print(
        "This script should be run directly and not imported as a module.\n"
        "Please execute it using 'python wsgi_hello_world_post_request.py'."
    )
