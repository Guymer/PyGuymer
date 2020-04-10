# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/download_stream.py                         #
##############################################################################################

def download_stream(sess, url):
    # Load sub-functions ...
    from .download import download

    # Try to download the file and catch common errors ...
    resp = download(sess, "get", url)
    if resp is False:
        return False

    return resp.content
