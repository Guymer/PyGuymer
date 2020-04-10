# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/exiftool.py                                #
##############################################################################################

def exiftool(fname):
    # Import modules ...
    import os
    import subprocess

    # Check that "exiftool" is installed ...
    try:
        subprocess.check_call(
            [
                u"type",
                u"exiftool"
            ],
            stdout = open(os.devnull, "wt"),
            stderr = open(os.devnull, "wt")
        )
    except subprocess.CalledProcessError:
        raise Exception(u"\"exiftool\" is not installed")

    # Check that the image exists ...
    if not os.path.exists(fname):
        raise Exception(u"\"{:s}\" does not exist".format(fname))

    # Strip all metadata ...
    try:
        subprocess.check_call(
            [
                u"exiftool",
                fname
            ],
            stdout = open(os.devnull, "wt"),
            stderr = open(os.devnull, "wt")
        )
    except subprocess.CalledProcessError:
        raise Exception(u"\"exiftool\" failed")
