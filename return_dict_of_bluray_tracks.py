# -*- coding: utf-8 -*-

def return_dict_of_bluray_tracks(fname):
    # Import modules ...
    import json
    import subprocess

    # Create empty dictionary and initialize counter ...
    ans = {}
    i = 0

    # Loop over all tracks ...
    while True:
        # Find format info ...
        proc = subprocess.Popen(
            [
                "ffprobe",
                "-loglevel", "quiet",
                "-print_format", "json",
                "-show_format",
                "-playlist", "{0:d}".format(i),
                "bluray:{0:s}".format(fname)
            ],
            stderr = subprocess.PIPE,
            stdout = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            # Assume that the only reason the command failed is that we have run out of playlists to probe ...
            break

        # Append information ...
        ans["{0:d}".format(i)] = {
            u"length" : float(json.loads(stdout)[u"format"][u"duration"])       # [s]
        }

        # Increment counter ...
        i += 1

    # Return list ...
    return ans
