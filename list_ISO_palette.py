# -*- coding: utf-8 -*-

def list_ISO_palette(fname, usr_track = None):
    # Import modules ...
    import numpy
    import subprocess
    import xml.etree.ElementTree

    # Load sub-functions ...
    from .yuv2rgb import yuv2rgb

    # Find track info ...
    proc = subprocess.Popen(
        [
            "lsdvd",
            "-x",
            "-Ox",
            fname
        ],
        stderr = subprocess.PIPE,
        stdout = subprocess.PIPE
    )
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise Exception(u"\"lsdvd\" command failed")

    # Clean up ...
    # NOTE: "lsdvd" sometimes returns invalid XML as it does not: escape characters; or remove invalid characters.
    stdout = unicode(stdout, "utf-8", "ignore").replace(u"&", u"&amp;")

    # Loop over all tracks ...
    for track in xml.etree.ElementTree.fromstring(stdout).findall("track"):
        # Extract track ID ...
        it = int(track.find("ix").text)

        # Check if the user has chosen a track ...
        if usr_track is None:
            # Print length ...
            length = float(track.find("length").text) / 3600.0e0                # [hr]
            print "Track {0:2d} is {1:4.2f} hours long.".format(it, length)
            continue

        # Skip if this track is not the chosen one ...
        if it != int(usr_track):
            continue

        # Create empty list ...
        vals = []

        # Loop over all colours in the palette ...
        for color in track.find("palette").findall("color"):
            # Convert YUV to RGB ...
            yuv = numpy.zeros((1, 1, 3), dtype = numpy.uint8)
            yuv[0, 0, 0] = int(color.text[0:2], 16)
            yuv[0, 0, 1] = int(color.text[2:4], 16)
            yuv[0, 0, 2] = int(color.text[4:6], 16)
            rgb = yuv2rgb(yuv)
            vals.append(format(rgb[0, 0, 0], "x").rjust(2, '0') + format(rgb[0, 0, 1], "x").rjust(2, '0') + format(rgb[0, 0, 2], "x").rjust(2, '0'))

        # Print palette ...
        print ",".join(vals)

        # Stop looping ...
        break
