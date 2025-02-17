import urllib.parse
import html
import os
import sys
from pathlib import Path

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
        """Set HTTP headers"""

        # send code 200 response
        self.send_response(200)
        # send header first
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy", "default-src 'self'")
        self.send_header("X-XSS-Protection", "1; mode=block")
        # send file content to client
        self.end_headers()

    def do_GET(self):
        """Handle GET command"""

        ROOT_DIR = Path(os.path.dirname(__file__))  # file location
        try:
            if self.path.endswith(".html"):
                # Sanitize and validate path
                requested_path = ROOT_DIR / self.path.lstrip("/")
                if not requested_path.is_file() or not str(requested_path).startswith(
                    str(ROOT_DIR)
                ):
                    raise OSError("Invalid path")

                with open(requested_path) as f:  # open requested file
                    # set headers
                    self._set_headers()
                    # send file content to client
                    self.wfile.write(bytes(f.read(), "utf-8"))
                f.close()
                return
        except OSError:
            self.send_error(404, "File not found")

    def do_POST(self):
        """Handle POST command"""
        try:
            # Read the form data posted
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length > 1048576:  # Limit to 1MB
                raise ValueError("Content too large")

            post_data = self.rfile.read(content_length)
            form = urllib.parse.parse_qs(post_data.decode("utf-8"))

            # Get data from fields
            message = form.get("message", [""])[0] or "Default"

            # Sanitize user input
            message = html.escape(message)

            # HTML template response
            html_response = f"""<!DOCTYPE html>
<html>
  <body>
    <h1>POST verb demo</h1>
    <p>The message is '{message}'.</p>
    <br />
    <p>This is a POST verb!</p>
  </body>
</html>\n"""

            # set HTTP headers
            self._set_headers()
            # Write the response
            self.wfile.write(bytes(html_response, "utf-8"))
        except Exception as e:
            self.send_error(400, "Bad Request")


def run():
    server = None
    try:
        print("HTTP Server is starting...")
        server_address = (HOST_NAME, int(PORT_NUMBER))
        server = HTTPServer(server_address, MyHTTPRequestHandler)
        print(
            f"HTTP Server running on http://{HOST_NAME}:{PORT_NUMBER}/ use <Ctrl-C> to stop."
        )
        server.serve_forever()
    except KeyboardInterrupt:
        print(" o <Ctrl-C> entered, stopping HTTP Server...")
        if server:
            server.socket.close()


if __name__ == "__main__":
    """Starting Python program"""
    run()
else:
    print("This program is bad configured, you should be call to the module...")
