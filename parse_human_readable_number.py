# -*- coding: utf-8 -*-

def parse_human_readable_number(string):
    # Import modules ...
    import re

    # Extract digits (with decimal point) and letters separately ...
    val = float(re.sub(r"[A-Z]", "", string.upper()))                           # [?]
    units = re.sub(r"[0-9\.]", "", string).upper()

    # Scale value ...
    if units == "KB":
        val *= 1024.0                                                           # [B]
    elif units == "MB":
        val *= 1024.0 * 1024.0                                                  # [B]
    elif units == "GB":
        val *= 1024.0 * 1024.0 * 1024.0                                         # [B]
    elif units == "TB":
        val *= 1024.0 * 1024.0 * 1024.0 * 1024.0                                # [B]
    elif units == "PB":
        val *= 1024.0 * 1024.0 * 1024.0 * 1024.0 * 1024.0                       # [B]

    # Return answer ...
    return val
