# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/hostname.py                                #
##############################################################################################

def hostname():
    # Import standard modules ...
    import socket

    # Get (potentially fully-qualified) hostname and return the first part ...
    return socket.gethostname().split(".")[0]
