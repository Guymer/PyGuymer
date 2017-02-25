# -*- coding: utf-8 -*-

def return_video_frame_rate(fname):
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

        # Check format ...
        if "/" not in stream[u"avg_frame_rate"]:
            raise Exception(u"\"avg_frame_rate\" did not contain a \"/\"")

        # Return frame rate ...
        return float(stream[u"avg_frame_rate"].split("/")[0]) / float(stream[u"avg_frame_rate"].split("/")[1])

    # Return error ...
    return -1.0
