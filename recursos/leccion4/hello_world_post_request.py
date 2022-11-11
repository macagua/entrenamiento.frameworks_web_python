"""
Source code taken and improvements from the article
"Understanding Python WSGI with Examples" by Edd Mann at
https://eddmann.com/posts/understanding-python-wsgi-with-examples/
"""

import cgi

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
</html>
"""


def app(environ, start_response):
    html = form

    if environ["REQUEST_METHOD"] == "POST":
        post_env = environ.copy()
        post_env["QUERY_STRING"] = ""
        post = cgi.FieldStorage(
            fp=environ["wsgi.input"], environ=post_env, keep_blank_values=True
        )
        html = b"Hello, " + bytes(post["name"].value, "utf-8") + b"!"

    start_response("200 OK", [("Content-Type", "text/html")])
    return [html]


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
