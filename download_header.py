# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/download_header.py                         #
##############################################################################################

def download_header(sess, url):
    # Load sub-functions ...
    from .download import download

    # Try to get the headers and catch common errors ...
    resp = download(sess, "head", url)
    if resp is False:
        return False

    return resp.headers
