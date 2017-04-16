# -*- coding: utf-8 -*-

def return_video_frame_rate(fname):
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
        # HACK: Fallback and attempt to load it as a raw M-JPEG stream.
        proc = subprocess.Popen(
            [
                u"ffprobe",
                u"-loglevel", u"quiet",
                u"-probesize", u"1G",
                u"-analyzeduration", u"1800M",
                u"-print_format", u"json",
                u"-show_streams",
                u"-f", u"mjpeg",
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
        a = stream[u"avg_frame_rate"].split("/")[0]                             # [#]
        b = stream[u"avg_frame_rate"].split("/")[1]                             # [s]
        fps = -1.0                                                              # [Hz]
        if int(b) != 0:
            fps = float(a) / float(b)                                           # [Hz]
        return fps

    # Return error ...
    return -1.0
