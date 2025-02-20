"""Python's bundled WSGI server

Source code taken and improvements from the
"WSGI Tutorial" by Clodoaldo Pinto Neto at
https://wsgi.tutorial.codepoint.net/parsing-the-request-get
"""

import logging
from urllib.parse import parse_qs
from html import escape

logging.basicConfig(level=logging.INFO)

# Server IP
HOST_NAME = "localhost"
# Server port
PORT_NUMBER = 8080
# HTTP Status
STATUS = "200 OK"

html = """<!DOCTYPE html>
<html>
<body>
   <form method="get" action="">
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
    # Returns a dictionary in which the values are lists
    environ_vars = parse_qs(environ["QUERY_STRING"])
    # As there can be more than one value for a variable then
    # a list is provided as a default value.
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
    # Now content type is text/html
    RESPONSE_HEADERS = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body))),
    ]
    # Start the response
    start_response(STATUS, RESPONSE_HEADERS)
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
        f"WSGI Server running on http://{HOST_NAME}:{PORT_NUMBER}/ use <Ctrl-C> to stop."
    )
    # Server serve forever
    server.serve_forever()
except KeyboardInterrupt:
    logging.error("<Ctrl-C> entered, stopping WSGI Server...")
    if server:
        # Close the server
        server.socket.close()
