# -*- coding: utf-8 -*-

def list_media_audio_streams(fname):
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
        # HACK: Fallback and attempt to load it as a raw M-JPEG stream.
        proc = subprocess.Popen(
            [
                "ffprobe",
                "-loglevel", "quiet",
                "-print_format", "json",
                "-show_streams",
                "-f", "mjpeg",
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
