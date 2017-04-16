# -*- coding: utf-8 -*-

def return_MP4_video_profile(fname):
    # Import modules ...
    import json
    import subprocess

    # Find stream info ...
    proc = subprocess.Popen(
        [
            u"ffprobe",
            u"-loglevel", u"quiet",
            u"-probesize", u"1G",
            u"-analyzeduration", u"1800M",
            u"-print_format", u"json",
            u"-show_streams",
            fname
        ],
        stderr = subprocess.PIPE,
        stdout = subprocess.PIPE
    )
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise Exception(u"\"ffprobe\" command failed")

    # Loop over streams ...
    for stream in json.loads(stdout)[u"streams"]:
        # Skip stream if it is not video ...
        if stream[u"codec_type"].strip().lower() != u"video":
            continue

        # Skip stream if it is not H.264 video ...
        if stream[u"codec_name"].strip().upper() != u"H264":
            continue

        # Return profile ...
        return stream[u"profile"]

    # Return error ...
    return u"ERROR"
