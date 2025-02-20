import http.client
import sys


def run(http_server):
    """Run HTTP Client"""
    print("HTTP Client is starting...")

    connection = None
    try:
        # create a connection
        connection = http.client.HTTPConnection(http_server, timeout=10)

        while 1:
            command = input(
                '\nEnter a input command (example GET test.html, type "exit" to end it): '
            )
            command = command.split()

            if command[0] == "exit":  # type exit to end it
                print("\nStopping web client....")
                break

            # request command to server
            connection.request(command[0], command[1])

            # get response from server
            response = connection.getresponse()

            # print server response and data
            print(response.status, response.reason)
            data_received = response.read()
            print(data_received)
        if connection:
            connection.close()
    except KeyboardInterrupt:
        print(" <Ctrl-C> entered, stopping HTTP Client...")
        if connection:
            connection.close()


if __name__ == "__main__":
    """Starting HTTP Client"""

    if not sys.argv[1:]:
        print(
            " Fatal: You forgot to include the URL like 127.0.0.1:8085 from the httpserver.py module on the command line."
        )
        print(f"Usage: python3 {sys.argv[0]} IP:PORT")
        sys.exit(2)
    else:
        # get http server ip, for example 127.0.0.1:8085
        http_server = sys.argv[1]
    run(http_server)
else:
    print("This program is bad configured, you should be call to the module...")
