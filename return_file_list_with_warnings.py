# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/return_file_list_with_warnings.py          #
##############################################################################################

def return_file_list_with_warnings(path):
    # Import modules ...
    import os

    # Load sub-functions ...
    from .make_path_safe import make_path_safe
    from .return_file_list_with_warnings import return_file_list_with_warnings

    # Create empty list ...
    contents = []

    # Check it exists ...
    if os.path.exists(path):
        # Loop over folder contents ...
        for child in os.listdir(path):
            # Make file name ...
            item = os.path.join(path, child)

            # Test if this part is illegal and print the full path for
            # identification ...
            if not child.startswith(u".") and child != make_path_safe(child):
                print u"\"{0:s}\" is illegal".format(item)

            # Check what to do ...
            if os.path.isdir(item):
                # Recursively run this function again and add to list ...
                contents += return_file_list_with_warnings(item)
            else:
                # Add to list ...
                contents.append(item)

    # Return sorted list ...
    contents.sort()
    return contents
