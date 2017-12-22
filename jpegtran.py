# -*- coding: utf-8 -*-

def jpegtran(fname):
    # Import modules ...
    import os
    import subprocess

    # Check that "jpegtran" is installed ...
    try:
        subprocess.check_call(
            [
                u"type",
                u"jpegtran"
            ],
            stdout = open(os.devnull, "wt"),
            stderr = open(os.devnull, "wt")
        )
    except subprocess.CalledProcessError:
        raise Exception(u"\"jpegtran\" is not installed")

    # Check that the JP[E]G exists ...
    if not os.path.exists(fname):
        raise Exception(u"\"{0:s}\" does not exist".format(fname))

    # Optimise JP[E]G ...
    try:
        subprocess.check_call(
            [
                u"jpegtran",
                u"-copy", u"all",
                u"-optimise",
                u"-outfile", fname,
                u"-perfect",
                fname
            ],
            stdout = open(os.devnull, "wt"),
            stderr = open(os.devnull, "wt")
        )
    except subprocess.CalledProcessError:
        raise Exception(u"\"jpegtran\" failed")
