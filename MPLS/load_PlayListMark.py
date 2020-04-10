# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/MPLS/load_PlayListMark.py                  #
##############################################################################################

def load_PlayListMark(fobj):
    # NOTE: see https://github.com/lerks/BluRay/wiki/PlayListMark

    # Import modules ...
    import struct

    # Initialize variables ...
    ans = {}
    length3 = 0                                                                                                         # [B]

    # Read the binary data ...
    ans[u"Length"], = struct.unpack(u">I", fobj.read(4))
    ans[u"NumberOfPlayListMarks"], = struct.unpack(u">H", fobj.read(2));                                                length3 += 2
    ans[u"PlayListMarks"] = []
    for i in xrange(ans[u"NumberOfPlayListMarks"]):
        tmp = {}
        fobj.read(1);                                                                                                   length3 += 1
        tmp[u"MarkType"], = struct.unpack(u">B", fobj.read(1));                                                         length3 += 1
        tmp[u"RefToPlayItemID"], = struct.unpack(u">H", fobj.read(2));                                                  length3 += 2
        tmp[u"MarkTimeStamp"], = struct.unpack(u">I", fobj.read(4));                                                    length3 += 4
        tmp[u"EntryESPID"], = struct.unpack(u">H", fobj.read(2));                                                       length3 += 2
        tmp[u"Duration"], = struct.unpack(u">I", fobj.read(4));                                                         length3 += 4
        ans[u"PlayListMarks"].append(tmp)

    # Pad out the read ...
    if length3 != ans[u"Length"]:
        l = ans[u"Length"] - length3                                                                                    # [B]
        fobj.read(l);                                                                                                   length3 += l

    # Return answer ...
    return ans, length3
