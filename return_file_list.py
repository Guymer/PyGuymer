# -*- coding: utf-8 -*-

def return_file_list(path):
    # Import modules ...
    import os

    # Create empty list ...
    contents = []

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