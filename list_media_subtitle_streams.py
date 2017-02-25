# -*- coding: utf-8 -*-

def list_media_subtitle_streams(fname):
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
        if stream[u"codec_type"].strip().lower() != u"subtitle":
            continue

        # Print information ...
        ist = int(stream[u"index"])
        langcode = stream[u"tags"][u"language"]
        print "Stream {0:2d} is in \"{1:3s}\".".format(ist, langcode)
