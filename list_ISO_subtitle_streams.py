# -*- coding: utf-8 -*-

def list_ISO_subtitle_streams(fname, usr_track = None):
    # Import modules ...
    import subprocess
    import xml.etree.ElementTree

    # Load sub-functions ...
    from .return_dict_of_ISO_subtitle_streams import return_dict_of_ISO_subtitle_streams
    from .return_dict_of_ISO_tracks import return_dict_of_ISO_tracks

    # Check input ...
    if not fname.endswith(".iso"):
        raise Exception("an ISO was not passed")

    # Check if the user has chosen a track ...
    if usr_track is None:
        # Obtain track information ...
        info = return_dict_of_ISO_tracks(fname)

        # Loop over tracks ...
        for track in sorted(info.keys()):
            # Print information ...
            print "Track {0:s} is {1:4.2f} hours long.".format(track, info[track][u"length"] / 3600.0)
    else:
        # Obtain subtitle stream information ...
        info = return_dict_of_ISO_subtitle_streams(fname, usr_track)

        # Loop over subtitle streams ...
        for stream in sorted(info.keys()):
            print "Stream {0:s} ({1:s}) is \"{2:s}\" content in \"{3:2s} ({4:s})\".".format(stream, info[stream][u"ist_id"], info[stream][u"content"], info[stream][u"langcode"], info[stream][u"language"])
