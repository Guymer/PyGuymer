# -*- coding: utf-8 -*-

def does_file_have_RTP_hints(fname = "missing"):
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

    # Set default answer ...
    ans = False

    # Loop over streams ...
    for stream in json.loads(stdout)[u"streams"]:
        # Skip stream if it is not data ...
        if stream[u"codec_type"].strip().lower() != u"data":
            continue

        # Check if this data stream is RTP ...
        if stream[u"codec_tag_string"].strip().lower() == u"rtp":
            ans = True

    # Return answer ...
    return ans
