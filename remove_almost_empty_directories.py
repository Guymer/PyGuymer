# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/remove_almost_empty_directories.py         #
##############################################################################################

def remove_almost_empty_directories(path):
    # Import modules ...
    import os

    # Set counter ...
    i = 0

    # Loop over all the contents of the passed directory ...
    for root, dnames, fnames in os.walk(path, topdown = False):
        # Loop over all sub-directories ...
        for dname in dnames:
            # List its contents and check if the only content is a ".directory"
            # file ...
            if os.listdir(os.path.join(root, dname)) == [".directory"]:
                # Increment counter and remove directory ...
                i += 1
                os.remove(os.path.join(root, dname, ".directory"))
                os.rmdir(os.path.join(root, dname))

    # Return counter ...
    return i
