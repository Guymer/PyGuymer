# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/convert_bytes_to_pretty_bytes.py           #
##############################################################################################

def convert_bytes_to_pretty_bytes(size = 0):
    # Convert input to float and set default units ...
    size = float(size)
    unit = "B"

    # Convert to useful units ...
    if size >= 1024.0:
        size /= 1024.0
        unit = "KiB"
    if size >= 1024.0:
        size /= 1024.0
        unit = "MiB"
    if size >= 1024.0:
        size /= 1024.0
        unit = "GiB"
    if size >= 1024.0:
        size /= 1024.0
        unit = "TiB"
    if size >= 1024.0:
        size /= 1024.0
        unit = "PiB"

    # Return answer ...
    return size, unit
