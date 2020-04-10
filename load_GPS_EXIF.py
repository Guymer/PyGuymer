# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/load_GPS_EXIF.py                           #
##############################################################################################

def load_GPS_EXIF(fname, python = True):
    # Load sub-functions ...
    from .load_GPS_EXIF1 import load_GPS_EXIF1
    from .load_GPS_EXIF2 import load_GPS_EXIF2

    # Check what the user wants ...
    if python:
        # Will use the Python module "exifread" ...
        return load_GPS_EXIF1(fname)
    else:
        # Will use the binary "exiftool" ...
        return load_GPS_EXIF2(fname)
