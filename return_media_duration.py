# -*- coding: utf-8 -*-

def return_media_duration(fname):
    # Import modules ...
    import json
    import subprocess

    # Find format info ...
    proc = subprocess.Popen(
        [
            u"ffprobe",
            u"-loglevel", u"quiet",
            u"-probesize", u"2G",
            u"-analyzeduration", u"1800M",
            u"-print_format", u"json",
            u"-show_format",
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
                u"-probesize", u"2G",
                u"-analyzeduration", u"1800M",
                u"-print_format", u"json",
                u"-show_format",
                u"-f", u"mjpeg",
                fname
            ],
            stderr = subprocess.PIPE,
            stdout = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            raise Exception(u"\"ffprobe\" command failed")

    # Return duration ...
    form = json.loads(stdout)[u"format"]
    dur = -1.0                                                                  # [s]
    if u"duration" in form:
        dur = float(form[u"duration"])                                          # [s]
    return dur
