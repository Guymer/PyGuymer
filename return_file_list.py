# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/return_file_list.py                        #
##############################################################################################

def return_file_list(path):
    # Import modules ...
    import os

    # Load sub-functions ...
    from .return_file_list import return_file_list

    # Create empty list ...
    contents = []

    # Check it exists ...
    if os.path.exists(path):
        # Loop over folder contents ...
        for child in os.listdir(path):
            # Make file name ...
            item = os.path.join(path, child)

            # Check what to do ...
            if os.path.isdir(item):
                # Recursively run this function again and add to list ...
                contents += return_file_list(item)
            else:
                # Add to list ...
                contents.append(item)

    # Return sorted list ...
    contents.sort()
    return contents
