"""
Python's bundled WSGI server

Source code taken and improvements from the
"WSGI Tutorial" by Clodoaldo Pinto Neto at
https://wsgi.tutorial.codepoint.net/parsing-the-request-post
"""

import logging
from urllib.parse import parse_qs
from html import escape

logging.basicConfig(level=logging.INFO)

# Server IP
HOST_NAME = "localhost"
# Server port
PORT_NUMBER = 8080

html = """<!DOCTYPE html>
<html>
<body>
   <form method="post" action="">
        <p>
           Age: <input type="text" name="age" value="%(age)s">
        </p>
        <p>
            Hobbies:
            <input
                name="hobbies" type="checkbox" value="software"
                %(checked-software)s
            > Software
            <input
                name="hobbies" type="checkbox" value="tunning"
                %(checked-tunning)s
            > Auto Tunning
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
        Age: %(age)s<br>
        Hobbies: %(hobbies)s
    </p>
</body>
</html>\n"""


def application(environ, start_response):
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except ValueError:
        request_body_size = 0
    request_body = (
        environ.get("wsgi.input").read(request_body_size)
        if environ.get("wsgi.input")
        else b""
    )
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    if request_body:
        environ_vars = parse_qs(request_body.decode())
    else:
        environ_vars = {}
    age = environ_vars.get("age", [""])[0]  # Returns the first age value.
    hobbies = environ_vars.get("hobbies", [])  # Returns a list of hobbies.
    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]
    response_body = html % {  # Fill the above html template in
        "checked-software": ("", "checked")["software" in hobbies],
        "checked-tunning": ("", "checked")["tunning" in hobbies],
        "age": age or "Empty",
        "hobbies": ", ".join(hobbies or ["No Hobbies?"]),
    }
    # HTTP Status
    STATUS = "200 OK"
    # Now content type is text/html
    RESPONSE_HEADERS = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body))),
    ]
    # Start the response
    try:
        start_response(STATUS, RESPONSE_HEADERS)
    except Exception as e:
        logging.error(f"Error starting response: {e}")
        start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
        return [b"Internal Server Error"]
    return [response_body.encode("utf-8")]


server = None
try:
    from wsgiref.simple_server import make_server

    # Instantiate the server
    server = make_server(
        HOST_NAME,  # The host name
        PORT_NUMBER,  # A port number where to wait for the request
        application,  # The application object name, in this case a function
    )
    logging.info(
        f" WSGI Server running on http://{HOST_NAME}:{PORT_NUMBER}/ use <Ctrl-C> to stop."
    )
    # Server serve forever
    server.serve_forever()
except KeyboardInterrupt:
    logging.error(" <Ctrl-C> entered, stopping WSGI Server...")
    if server:
        # Close the server
        server.socket.close()
