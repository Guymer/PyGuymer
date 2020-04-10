# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/find_instances_of_a_file.py                #
##############################################################################################

def find_instances_of_a_file(path, basename):
    # Import modules ...
    import os

    # Load sub-functions ...
    from .find_instances_of_a_file import find_instances_of_a_file

    # Create empty list ...
    contents = []

    # Loop over folder contents ...
    for child in os.listdir(path):
        # Make file name ...
        item = os.path.join(path, child)

        # Check what to do ...
        if os.path.isdir(item):
            # Recursively run this function again and add to list ...
            contents += find_instances_of_a_file(item, basename)
        elif child == basename:
            # Add to list ...
            contents.append(item)

    # Return sorted list ...
    contents.sort()
    return contents
