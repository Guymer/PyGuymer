# -*- coding: utf-8 -*-

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
