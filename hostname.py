# -*- coding: utf-8 -*-

def hostname():
    # Import standard modules ...
    import socket

    # Get (potentially fully-qualified) hostname and return the first part ...
    return socket.gethostname().split(".")[0]
