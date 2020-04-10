# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/parse_MPLS_file.py                         #
##############################################################################################

def parse_MPLS_file(br, ip):
    # Import modules ...
    import os
    import pyguymer.MPLS

    # Create dictionary to hold information ...
    info = {}

    # Open file ...
    with open(os.path.join(br, u"BDMV/PLAYLIST/{0:05d}.mpls".format(ip)), "rb") as fobj:
        # Load header ...
        res, length0 = pyguymer.MPLS.load_header(fobj)
        info[u"header"] = res

        # Load AppInfoPlayList section ...
        res, length1 = pyguymer.MPLS.load_AppInfoPlayList(fobj)
        info[u"AppInfoPlayList"] = res

        # Load PlayList section ...
        if info[u"header"][u"PlayListStartAddress"] != 0:
            fobj.seek(info[u"header"][u"PlayListStartAddress"], os.SEEK_SET)
            res, length2 = pyguymer.MPLS.load_PlayList(fobj)
            info[u"PlayList"] = res

        # Load PlayListMark section ...
        if info[u"header"][u"PlayListMarkStartAddress"] != 0:
            fobj.seek(info[u"header"][u"PlayListMarkStartAddress"], os.SEEK_SET)
            res, length3 = pyguymer.MPLS.load_PlayListMark(fobj)
            info[u"PlayListMark"] = res

        # Load ExtensionData section ...
        if info[u"header"][u"ExtensionDataStartAddress"] != 0:
            fobj.seek(info[u"header"][u"ExtensionDataStartAddress"], os.SEEK_SET)
            res, length4 = pyguymer.MPLS.load_ExtensionData(fobj)
            info[u"ExtensionData"] = res

    # Return answer ...
    return info
