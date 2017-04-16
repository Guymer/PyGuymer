# -*- coding: utf-8 -*-

def return_dict_of_ISO_tracks(fname):
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

    # Clean up ...
    # NOTE: "lsdvd" sometimes returns invalid XML as it does not:
    #         * escape characters; or
    #         * remove invalid characters.
    stdout = unicode(stdout, "utf-8", "ignore").replace(u"&", u"&amp;")

    # Create empty dictionary ...
    ans = {}

    # Loop over all tracks ...
    for track in xml.etree.ElementTree.fromstring(stdout).findall(u"track"):
        # Append information ...
        ans[track.find(u"ix").text] = {
            u"length" : float(track.find(u"length").text)                       # [s]
        }

    # Return dictionary ...
    return ans
