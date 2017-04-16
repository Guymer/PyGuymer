# -*- coding: utf-8 -*-

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
