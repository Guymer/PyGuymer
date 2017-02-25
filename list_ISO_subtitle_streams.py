# -*- coding: utf-8 -*-

def list_ISO_subtitle_streams(fname, usr_track = None):
    # Import modules ...
    import subprocess
    import xml.etree.ElementTree

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

        # Loop over all subtitle channels ...
        for subp in track.findall("subp"):
            # Print information ...
            ist = int(subp.find("ix").text)
            ist_id = subp.find("streamid").text
            content = subp.find("content").text
            langcode = subp.find("langcode").text
            language = subp.find("language").text
            print "Stream {0:2d} ({1:s}) is \"{2:s}\" content in \"{3:2s} ({4:s})\".".format(ist, ist_id, content, langcode, language)

        # Stop looping ...
        break
