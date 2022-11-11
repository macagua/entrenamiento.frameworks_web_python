#!/usr/bin/env python

"""
Python's bundled WSGI server

Source code taken and improvements from the
"WSGI Tutorial" by Clodoaldo Pinto Neto at
http://wsgi.tutorial.codepoint.net/parsing-the-request-get
"""
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

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
</html>
"""


def application(environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ["QUERY_STRING"])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    age = d.get("age", [""])[0]  # Returns the first age value
    hobbies = d.get("hobbies", [])  # Returns a list of hobbies

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

    # Now content type is text/html
    response_headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body))),
    ]

    start_response(status, response_headers)
    return [response_body]


httpd = make_server("localhost", 8080, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()
