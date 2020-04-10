# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/convert_spreadsheet_to_unix.py             #
##############################################################################################

def convert_spreadsheet_to_unix(val):
    return 86400 * (val - 25569)
