# -*- coding: utf-8 -*-

def add_map_background(axis, debug = False, name = u"natural-earth-1", resolution = u"medium0512px"):
    # Import modules ...
    import json
    import os

    # Initialize trigger ...
    default = True

    # Check if the environment variable has been defined ...
    if u"CARTOPY_USER_BACKGROUNDS" in os.environ:
        # Determine JSON path and check it exists ...
        jpath = os.path.join(os.environ[u"CARTOPY_USER_BACKGROUNDS"], u"images.json")
        if os.path.exists(jpath):
            # Load JSON and check keys exist ...
            info = json.load(open(jpath, "rt"))
            if name in info:
                if resolution in info[name]:
                    # Determine image path and check it exists ...
                    ipath = os.path.join(os.environ[u"CARTOPY_USER_BACKGROUNDS"], info[name][resolution])
                    if os.path.exists(ipath):
                        default = False

    # Draw background image ...
    if default:
        if debug:
            print u"INFO: Drawing default background."
        axis.stock_img()
    else:
        if debug:
            print u"INFO: Drawing user-requested background."
        axis.background_img(name = name, resolution = resolution)
