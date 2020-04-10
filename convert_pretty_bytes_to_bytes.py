# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/convert_pretty_bytes_to_bytes.py           #
##############################################################################################

def convert_pretty_bytes_to_bytes(string):
    # Import modules ...
    import re

    # Extract digits (with decimal point) and letters separately ...
    val = float(re.sub(r"[A-Z]", u"", string.upper()))                          # [?]
    units = re.sub(r"[0-9\.]", u"", string).upper()

    # Scale value ...
    if units == u"KB" or units == u"KiB":
        val *= 1024.0                                                           # [B]
    elif units == u"MB" or units == u"MiB":
        val *= 1024.0 * 1024.0                                                  # [B]
    elif units == u"GB" or units == u"GiB":
        val *= 1024.0 * 1024.0 * 1024.0                                         # [B]
    elif units == u"TB" or units == u"TiB":
        val *= 1024.0 * 1024.0 * 1024.0 * 1024.0                                # [B]
    elif units == u"PB" or units == u"PiB":
        val *= 1024.0 * 1024.0 * 1024.0 * 1024.0 * 1024.0                       # [B]

    # Return answer ...
    return val
