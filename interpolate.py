# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/interpolate.py                             #
##############################################################################################

def interpolate(x1, x2, y1, y2, x):
    return (y1 * (x2 - x) + y2 * (x - x1)) / (x2 - x1)
