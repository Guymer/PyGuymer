# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/buffer_points.py                           #
##############################################################################################

def buffer_points(points, dist, nang = 19, simp = 0.1, debug = False):
    """
    This function reads in a list of (lon,lat)-tuples representing coordinates
    (in degrees) that exist on the surface of the Earth and returns a
    [Multi]Polygon of them buffered by a constant distance (in metres).
    """

    # Import modules ...
    import multiprocessing
    import shapely
    import shapely.ops
    import shapely.validation

    # Load sub-functions ...
    from .buffer_point import buffer_point

    # Check argument ...
    if not isinstance(points, list):
        raise TypeError("\"points\" is not a list")

    # Create pool of workers and create empty lists ...
    pool = multiprocessing.Pool()
    results = []
    buffs = []

    # Loop over points in points list and add buffer job to worker pool...
    for point in points:
        results.append(pool.apply_async(buffer_point, (point[0], point[1], dist, nang, debug)))

    # Loop over parallel jobs and append simplified results to list ...
    for result in results:
        buffs.append(result.get().simplify(simp))

    # Destroy pool of workers ...
    pool.close()
    pool.join()

    # Convert list to (unified) Polygon and check it ...
    buffs = shapely.ops.unary_union(buffs)
    if not buffs.is_valid:
        raise Exception("\"buffs\" is not a valid [Multi]Polygon ({0:s})".format(shapely.validation.explain_validity(buffs)))

    # Return answer ...
    return buffs
