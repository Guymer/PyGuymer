# -*- coding: utf-8 -*-

def optipng(fname):
    # Import modules ...
    import os
    import subprocess

    # Check that "optipng" is installed ...
    try:
        subprocess.check_call(
            [
                u"type",
                u"optipng"
            ],
            stdout = open(os.devnull, "wt"),
            stderr = open(os.devnull, "wt")
        )
    except subprocess.CalledProcessError:
        raise Exception(u"\"optipng\" is not installed")

    # Check that the image exists ...
    if not os.path.exists(fname):
        raise Exception(u"\"{:s}\" does not exist".format(fname))

    # Optimise PNG ...
    try:
        subprocess.check_call(
            [
                u"optipng",
                fname
            ],
            stdout = open(os.devnull, "wt"),
            stderr = open(os.devnull, "wt")
        )
    except subprocess.CalledProcessError:
        raise Exception(u"\"optipng\" failed")
