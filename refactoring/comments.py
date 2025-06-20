import os

def init():
    port = get_port_or_default()
    start_server(port)


def start_server(port):
    print(port)


def get_port_or_default():
    port_as_string = os.environ.get('port')
    default_port = 8080
    port = default_port if port_as_string is None else int(port_as_string)
    return port
    