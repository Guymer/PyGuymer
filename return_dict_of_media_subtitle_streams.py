# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/return_dict_of_media_subtitle_streams.py   #
##############################################################################################

def return_dict_of_media_subtitle_streams(fname, playlist = None):
    # Check input ...
    if fname.startswith(u"bluray:") and playlist is None:
        raise Exception("a Blu-ray was specified but no playlist was supplied")

    # Import modules ...
    import json
    import subprocess

    # Load sub-functions ...
    from .parse_MPLS_file import parse_MPLS_file

    # Create empty dictionary ...
    ans = {}

    # Find stream info ...
    if fname.startswith(u"bluray:"):
        proc = subprocess.Popen(
            [
                u"ffprobe",
                u"-loglevel", u"quiet",
                u"-probesize", u"3G",
                u"-analyzeduration", u"1800M",
                u"-print_format", u"json",
                u"-show_streams",
                u"-playlist", u"{0:d}".format(playlist),
                fname
            ],
            stderr = subprocess.PIPE,
            stdout = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            print u"WARNING: \"ffprobe\" command failed on playlist \"{0:d}\" of \"{1:s}\"".format(playlist, fname)
            return ans
    else:
        proc = subprocess.Popen(
            [
                u"ffprobe",
                u"-loglevel", u"quiet",
                u"-probesize", u"3G",
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
                    u"-probesize", u"3G",
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
                print u"WARNING: \"ffprobe\" command failed on \"{0:s}\"".format(fname)
                return ans

    # Loop over streams ...
    for stream in json.loads(stdout)[u"streams"]:
        # Skip stream if it is incomplete ...
        if u"codec_type" not in stream:
            continue

        # Skip stream if it is not subtitle ...
        if stream[u"codec_type"].strip().lower() != u"subtitle":
            continue

        # Append information ...
        ans[str(stream[u"index"])] = stream

    # Check if it is a Blu-ray ...
    if fname.startswith(u"bluray:"):
        # Attempt to load the MPLS file for this playlist ...
        nfo = parse_MPLS_file(
            br = fname[len(u"bluray:"):],
            ip = playlist
        )

        # Check key ...
        if u"PlayList" in nfo:
            # Check key ...
            if u"PlayItems" in nfo[u"PlayList"]:
                # Loop over PlayItems ...
                for PlayItem in nfo[u"PlayList"][u"PlayItems"]:
                    # Loop over subtitle stream list names ...
                    for name in [u"PrimaryPGStreamEntries", u"SecondaryPGStreamEntries"]:
                        # Loop over PGStreamEntries ...
                        for PGStreamEntry in PlayItem[u"STNTable"][name]:
                            # Check keys ...
                            if u"StreamEntry" in PGStreamEntry and u"StreamAttributes" in PGStreamEntry:
                                # Check keys ...
                                if u"RefToStreamPID" in PGStreamEntry[u"StreamEntry"] and u"LanguageCode" in PGStreamEntry[u"StreamAttributes"]:
                                    # Loop over streams ...
                                    for stream in ans.iterkeys():
                                        # Check if this is the stream ...
                                        if PGStreamEntry[u"StreamEntry"][u"RefToStreamPID"] == ans[stream][u"id"]:
                                            # Add language code to the stream
                                            # information ...
                                            ans[stream][u"langcode"] = PGStreamEntry[u"StreamAttributes"][u"LanguageCode"]

    # Make sure that each stream has a language code ...
    for stream in ans.iterkeys():
        if u"langcode" not in ans[stream]:
            ans[stream][u"langcode"] = u"?"

    # Return dictionary ...
    return ans
