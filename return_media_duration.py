# -*- coding: utf-8 -*-

def return_media_duration(fname, playlist = None):
    # Check input ...
    if fname.startswith(u"bluray:") and playlist is None:
        raise Exception("a Blu-ray was specified but no playlist was supplied")

    # Import modules ...
    import json
    import subprocess

    # Find format info ...
    if fname.startswith(u"bluray:"):
        proc = subprocess.Popen(
            [
                u"ffprobe",
                u"-loglevel", u"quiet",
                u"-probesize", u"3G",
                u"-analyzeduration", u"1800M",
                u"-print_format", u"json",
                u"-show_format",
                u"-playlist", u"{0:d}".format(playlist),
                fname
            ],
            stderr = subprocess.PIPE,
            stdout = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            raise Exception(u"\"ffprobe\" command failed")
    else:
        proc = subprocess.Popen(
            [
                u"ffprobe",
                u"-loglevel", u"quiet",
                u"-probesize", u"3G",
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
                    u"-probesize", u"3G",
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
