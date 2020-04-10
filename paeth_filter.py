# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/paeth_filter.py                            #
##############################################################################################

def paeth_filter(a, b, c):
    # Find differences ...
    pi = a + b - c
    pa = abs(pi - a)
    pb = abs(pi - b)
    pc = abs(pi - c)

    # Return best point ...
    if pa <= pb and pa <= pc:
        return a
    elif pb <= pc:
        return b
    else:
        return c
