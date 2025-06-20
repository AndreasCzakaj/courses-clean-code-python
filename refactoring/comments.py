import os

def init():
    # get the port from env or use default
    port_as_string = os.environ.get('port')
    default_port = 8080
    port = default_port if port_as_string is None else int(port_as_string)

    # start server on given port
    print(port)
    