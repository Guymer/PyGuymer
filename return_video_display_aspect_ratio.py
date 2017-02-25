# -*- coding: utf-8 -*-

def return_video_display_aspect_ratio(fname):
    # Import modules ...
    import json
    import subprocess

    # Find stream info ...
    proc = subprocess.Popen(
        [
            "ffprobe",
            "-loglevel", "quiet",
            "-print_format", "json",
            "-show_streams",
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

        # Return display aspect ratio ...
        return stream[u"display_aspect_ratio"]

    # Return error ...
    return u"ERROR"
