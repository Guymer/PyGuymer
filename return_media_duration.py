# -*- coding: utf-8 -*-

def return_media_duration(fname):
    # Import modules ...
    import json
    import subprocess

    # Find format info ...
    proc = subprocess.Popen(
        [
            "ffprobe",
            "-loglevel", "quiet",
            "-print_format", "json",
            "-show_format",
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
                "ffprobe",
                "-loglevel", "quiet",
                "-print_format", "json",
                "-show_format",
                "-f", "mjpeg",
                fname
            ],
            stderr = subprocess.PIPE,
            stdout = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            raise Exception(u"\"ffprobe\" command failed")

    # Return duration ...
    format = json.loads(stdout)[u"format"]
    dur = -1.0                                                                  # [s]
    if u"duration" in format:
        dur = float(format[u"duration"])                                        # [s]
    return dur
