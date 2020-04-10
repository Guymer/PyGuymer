# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/make_path_safe.py                          #
##############################################################################################

def make_path_safe(path):
    # Loop over characters ...
    for illegal_char in u"\\", u"/", u":", u"*", u"?", u"\"", u"<", u">", u"|", u"%":
        path = path.replace(illegal_char, u"")

    # Make the file visible ...
    if path[0:1] == u".":
        path = u" " + path

    return path
