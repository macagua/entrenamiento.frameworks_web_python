import cgi
import os
import sys
import time

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import urllib.request
except ImportError:
    print("use python3 instead python")
    sys.exit(1)

# Server IP
HOST_NAME = "127.0.0.1"

# Server port
PORT_NUMBER = "8085"


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """Create custom HTTPRequestHandler class"""

    def _set_headers(self):
        """set HTTP headers"""

        # send code 200 response
        self.send_response(200)
        # send header first
        self.send_header("Content-type", "text/html")
        self.send_header("Last-Modified", self.date_time_string(time.time()))
        # send file content to client
        self.end_headers()

    def do_HEAD(self):
        """do the HTTP HEAD"""

        # set HTTP headers
        self._set_headers()

    def do_GET(self):
        """handle GET command"""

        rootdir = os.path.dirname(__file__)  # file location
        try:
            if self.path.endswith(".html"):
                f = open(rootdir + self.path)  # open requested file
                # set headers
                self._set_headers()
                # send file content to client
                self.wfile.write(bytes(f.read(), "utf-8"))
                f.close()
                return

        except OSError:
            self.send_error(404, "file not found")

    def do_POST(self):
        """handle POST command"""

        # set HTTP headers
        self._set_headers()

        # Create instance of FieldStorage
        # for parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": self.headers["Content-Type"],
            },
        )

        # Begin the response
        self._set_headers()

        # Get data from fields
        message = form.getvalue("message")

        html_response = """<!DOCTYPE html>
<html>
  <body>
    <h1>POST verb demo</h1>
    <p>The message is '%s'.</p>
    <br />
    <p>This is a POST verb!</p>
  </body>
</html>
        """ % (
            message
        )
        self.wfile.write(bytes(html_response, "utf-8"))
        # b"abcde".decode("utf-8")
        # html_response.decode("utf-8")
        # self.wfile.write(bytes(html_response, "utf-8").decode("utf-8"))


def run():
    try:
        print("HTTP Server is starting...")
        server_address = (HOST_NAME, int(PORT_NUMBER))
        server = HTTPServer(server_address, MyHTTPRequestHandler)
        print(
            f"HTTP Server running on http://{HOST_NAME}:{PORT_NUMBER}/ use <Ctrl-C> to stop."
        )
        server.serve_forever()
    except KeyboardInterrupt:
        print(" o <Ctrl-C> entered, stopping web server....")
        server.socket.close()


if __name__ == "__main__":
    """Starting Python program"""
    run()
elif __name__ == "httpserver":
    initialize()
else:
    print("This program is bad configured, you should be call to the module....")
