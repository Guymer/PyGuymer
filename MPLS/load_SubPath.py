# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/MPLS/load_SubPath.py                       #
##############################################################################################

def load_SubPath(fobj, length2):
    # NOTE: see https://github.com/lerks/BluRay/wiki/SubPath

    # Import modules ...
    import struct

    # Load sub-functions ...
    from .load_SubPlayItem import load_SubPlayItem

    # Initialize variables ...
    ans = {}
    length2a = 0                                                                                                        # [B]

    # Read the binary data ...
    ans[u"Length"], = struct.unpack(u">I", fobj.read(4));                                                               length2 += 4
    fobj.read(1);                                                                                                       length2 += 1; length2a += 1
    ans[u"SubPathType"], = struct.unpack(u">B", fobj.read(1));                                                          length2 += 1; length2a += 1
    ans[u"MiscFlags1"], = struct.unpack(u">H", fobj.read(2));                                                           length2 += 2; length2a += 2
    ans[u"NumberOfSubPlayItems"], = struct.unpack(u">B", fobj.read(1));                                                 length2 += 1; length2a += 1
    ans[u"SubPlayItems"] = []
    for i in xrange(ans[u"NumberOfSubPlayItems"]):
        res, length2, length2a, length2b = load_SubPlayItem(fobj, length2, length2a)
        ans[u"SubPlayItems"].append(res)

    # Pad out the read ...
    if length2a != ans[u"Length"]:
        l = ans[u"Length"] - length2a                                                                                   # [B]
        fobj.read(l);                                                                                                   length2 += l; length2a += l

    return ans, length2, length2a
