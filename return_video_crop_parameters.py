# -*- coding: utf-8 -*-

def return_video_crop_parameters(fname, playlist = None):
    # Check input ...
    if fname.startswith(u"bluray:") and playlist is None:
        raise Exception("a Blu-ray was specified but no playlist was supplied")

    # Import modules ...
    import subprocess

    # Load sub-functions ...
    from .return_media_duration import return_media_duration
    from .return_video_height import return_video_height
    from .return_video_width import return_video_width

    # Initialize variables ...
    dur = return_media_duration(fname, playlist)                                # [s]
    w = return_video_width(fname, playlist)                                     # [px]
    h = return_video_height(fname, playlist)                                    # [px]
    x1 = w                                                                      # [px]
    x2 = 0                                                                      # [px]
    y1 = h                                                                      # [px]
    y2 = 0                                                                      # [px]

    # Loop over times ...
    for i in xrange(7):
        # Deduce time ...
        t = 0.1 * float(i + 2) * dur - 1.0                                      # [s]

        # Find crop parameters ...
        if fname.startswith(u"bluray:"):
            proc = subprocess.Popen(
                [
                    u"ffmpeg",
                    u"-probesize", u"3G",
                    u"-analyzeduration", u"1800M",
                    u"-playlist", u"{0:d}".format(playlist),
                    u"-ss", u"{0:.3f}".format(t),
                    u"-i", fname,
                    u"-an",
                    u"-sn",
                    u"-t", u"2.0",
                    u"-vf", u"cropdetect",
                    u"-y",
                    u"-f", u"null",
                    u"/dev/null"
                ],
                stderr = subprocess.PIPE,
                stdout = subprocess.PIPE
            )
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                raise Exception(u"\"ffmpeg\" command failed")
        else:
            proc = subprocess.Popen(
                [
                    u"ffmpeg",
                    u"-probesize", u"3G",
                    u"-analyzeduration", u"1800M",
                    u"-ss", u"{0:.3f}".format(t),
                    u"-i", fname,
                    u"-an",
                    u"-sn",
                    u"-t", u"2.0",
                    u"-vf", u"cropdetect",
                    u"-y",
                    u"-f", u"null",
                    u"/dev/null"
                ],
                stderr = subprocess.PIPE,
                stdout = subprocess.PIPE
            )
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                # HACK: Fallback and attempt to load it as a raw M-JPEG stream.
                proc = subprocess.Popen(
                    [
                        u"ffmpeg",
                        u"-probesize", u"3G",
                        u"-analyzeduration", u"1800M",
                        u"-ss", u"{0:.3f}".format(t),
                        u"-f", u"mjpeg",
                        u"-i", fname,
                        u"-an",
                        u"-sn",
                        u"-t", u"2.0",
                        u"-vf", u"cropdetect",
                        u"-y",
                        u"-f", u"null",
                        u"/dev/null"
                    ],
                    stderr = subprocess.PIPE,
                    stdout = subprocess.PIPE
                )
                stdout, stderr = proc.communicate()
                if proc.returncode != 0:
                    raise Exception(u"\"ffmpeg\" command failed")

        # Clean up ...
        stderr = unicode(stderr, "utf-8", "ignore")
        stdout = unicode(stdout, "utf-8", "ignore")

        # Loop over lines ...
        for line in stderr.split(u"\n"):
            # Skip irrelevant lines ...
            if not line.startswith(u"[Parsed_cropdetect"):
                continue

            # Extract information and loop over key+value pairs ...
            info = line.strip().split(u"]")[-1]
            for keyvalue in info.split():
                # Skip irrelevant key+value pairs ...
                if keyvalue.count(u":") != 1:
                    continue

                # Extract key and value and update variables ...
                key, value = keyvalue.split(u":")
                if key == u"x1":
                    x1 = min(x1, int(value))                                    # [px]
                if key == u"x2":
                    x2 = max(x2, int(value))                                    # [px]
                if key == u"y1":
                    y1 = min(y1, int(value))                                    # [px]
                if key == u"y2":
                    y2 = max(y2, int(value))                                    # [px]

    # Check results ...
    #if x1 >= x2:
        #raise Exception(u"failed to find cropped width")
    #if y1 >= y2:
        #raise Exception(u"failed to find cropped height")

    # Return largest extent (and cropped width and height) ...
    return x1, y1, x2, y2, x2 - x1 + 1, y2 - y1 + 1
