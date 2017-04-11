# -*- coding: utf-8 -*-

def list_bluray_audio_streams(fname, usr_playlist):
    # Import modules ...
    import json
    import subprocess

    # Check input ...
    if usr_playlist == -1:
        raise Exception("no playlist was requested")

    # Find stream info ...
    proc = subprocess.Popen(
        [
            "ffprobe",
            "-loglevel", "quiet",
            "-print_format", "json",
            "-show_streams",
            "-playlist", "{0:d}".format(usr_playlist),
            "bluray:{0:s}".format(fname)
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
        if stream[u"codec_type"].strip().lower() != u"audio":
            continue

        # Print information ...
        ia = int(stream[u"index"])
        langcode = u"und"
        if u"tags" in stream:
            if u"language" in stream[u"tags"]:
                langcode = stream[u"tags"][u"language"]
        form = stream[u"codec_name"].upper()
        frequency = int(stream[u"sample_rate"])                                 # [Hz]
        channels = int(stream[u"channels"])
        print "Stream {0:2d} is in \"{1:3s}\" using {2:s} at {3:,d} Hz with {4:d} channels.".format(ia, langcode, form, frequency, channels)
