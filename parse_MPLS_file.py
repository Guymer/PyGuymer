# -*- coding: utf-8 -*-

def parse_MPLS_file(br, ip):
    # NOTE: see https://github.com/lerks/BluRay/wiki
    # NOTE: see https://en.wikibooks.org/wiki/User:Bdinfo/mpls

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
        fobj.seek(info[u"header"][u"PlayListStartAddress"], os.SEEK_SET)
        res, length2 = pyguymer.MPLS.load_PlayList(fobj)
        info[u"PlayList"] = res

        # Load PlayListMark section ...
        fobj.seek(info[u"header"][u"PlayListMarkStartAddress"], os.SEEK_SET)
        res, length3 = pyguymer.MPLS.load_PlayListMark(fobj)
        info[u"PlayListMark"] = res

        # Load ExtensionData section ...
        fobj.seek(info[u"header"][u"ExtensionDataStartAddress"], os.SEEK_SET)
        res, length4 = pyguymer.MPLS.load_ExtensionData(fobj)
        info[u"ExtensionData"] = res

    # Return answer ...
    return info
