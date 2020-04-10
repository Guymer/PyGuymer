# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/save_array_as_PPM.py                       #
##############################################################################################

def save_array_as_PPM(img, fname):
    # Write out PPM ...
    with open(fname, "wb") as fobj:
        fobj.write(u"P6 {0:d} {1:d} 255 ".format(img.shape[1], img.shape[0]))
        img.tofile(fobj)
