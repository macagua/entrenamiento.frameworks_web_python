#!/usr/bin/env python

"""
Python's bundled WSGI server

Source code taken and improvements from the
"WSGI Tutorial" by Clodoaldo Pinto Neto at
http://wsgi.tutorial.codepoint.net/parsing-the-request-post
"""

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

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
</html>
"""


def application(environ, start_response):

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except (ValueError):
        request_body_size = 0

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ["wsgi.input"].read(request_body_size)
    d = parse_qs(request_body)

    age = d.get("age", [""])[0]  # Returns the first age value.
    hobbies = d.get("hobbies", [])  # Returns a list of hobbies.

    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % {  # Fill the above html template in
        "checked-software": ("", "checked")["software" in hobbies],
        "checked-tunning": ("", "checked")["tunning" in hobbies],
        "age": age or "Empty",
        "hobbies": ", ".join(hobbies or ["No Hobbies?"]),
    }

    status = "200 OK"

    response_headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body))),
    ]

    start_response(status, response_headers)
    return [response_body]


httpd = make_server("localhost", 8080, application)
httpd.serve_forever()
