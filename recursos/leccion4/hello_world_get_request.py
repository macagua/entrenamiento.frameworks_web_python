"""
Source code taken and improvements from the article
"Understanding Python WSGI with Examples" by Edd Mann at
https://eddmann.com/posts/understanding-python-wsgi-with-examples/
"""

# Server IP
HOST_NAME = "127.0.0.1"
# Server port
PORT_NUMBER = 8080


def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Hello, world!"]


if __name__ == "__main__":
    try:
        from wsgiref.simple_server import make_server

        httpd = make_server(HOST_NAME, PORT_NUMBER, app)
        print(
            f"HTTP Server running on http://{HOST_NAME}:{PORT_NUMBER}/ use <Ctrl-C> to stop."
        )
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(" o <Ctrl-C> entered, stopping web server....")
