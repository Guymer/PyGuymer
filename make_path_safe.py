# -*- coding: utf-8 -*-

def make_path_safe(path):
    # Loop over characters ...
    for illegal_char in u"\\", u"/", u":", u"*", u"?", u"\"", u"<", u">", u"|", u"%":
        path = path.replace(illegal_char, u"")

    # Make the file visible ...
    if path[0:1] == u".":
        path = u" " + path

    return path
