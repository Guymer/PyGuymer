# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/return_dict_of_bluray_playlists.py         #
##############################################################################################

def return_dict_of_bluray_playlists(dname, threshold = 60.0):
    # Import modules ...
    import glob
    import json
    import os
    import subprocess

    # Create empty dictionary ...
    ans = {}

    # Loop over playlists ...
    for fname in glob.iglob(os.path.join(dname, u"BDMV", u"PLAYLIST", u"*.mpls")):
        # Extract number ...
        playlist = int(os.path.basename(fname).split(u".")[0])

        # Find format info ...
        proc = subprocess.Popen(
            [
                u"ffprobe",
                u"-loglevel", u"quiet",
                u"-probesize", u"3G",
                u"-analyzeduration", u"1800M",
                u"-print_format", u"json",
                u"-show_format",
                u"-playlist", u"{0:d}".format(playlist),
                u"bluray:{0:s}".format(dname)
            ],
            stderr = subprocess.PIPE,
            stdout = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            print u"WARNING: \"ffprobe\" command failed on playlist \"{0:d}\" of \"{1:s}\"".format(playlist, fname)
            continue

        # Append information if this playlist is worthwhile ...
        info = json.loads(stdout)[u"format"]
        if u"duration" in info:
            if float(info[u"duration"]) >= threshold:
                ans["{0:d}".format(playlist)] = info

    # Return dictionary ...
    return ans
