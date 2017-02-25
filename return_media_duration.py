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
        raise Exception(u"\"ffprobe\" command failed")

    # Return duration ...
    return float(json.loads(stdout)[u"format"][u"duration"])                    # [s]
