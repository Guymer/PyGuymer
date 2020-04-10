# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/download_text.py                           #
##############################################################################################

def download_text(sess, url):
    # Load sub-functions ...
    from .download import download

    # Try to download the page and catch common errors ...
    resp = download(sess, "get", url)
    if resp is False:
        return False

    return resp.text.encode("utf8", "xmlcharrefreplace")
