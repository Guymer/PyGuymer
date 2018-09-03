# -*- coding: utf-8 -*-

def buffer_multipolygon(geoms, dist, nang = 19, simp = 0.1, debug = False):
    # Import modules ...
    import shapely
    import shapely.geometry
    import shapely.ops
    import shapely.validation

    # Load sub-functions ...
    from .buffer_polygon import buffer_polygon

    # Check argument ...
    if not isinstance(geoms, shapely.geometry.multipolygon.MultiPolygon):
        raise TypeError("\"geoms\" is not a MultiPolygon")
    if not geoms.is_valid:
        raise Exception("\"geoms\" is not a valid MultiPolygon ({0:s})".format(shapely.validation.explain_validity(geoms)))

    # Create empty list ...
    buffs = []

    # Loop over Polygons ...
    for geom in geoms.geoms:
        # Buffer Polygon ...
        buff = buffer_polygon(geom, dist, nang, simp, debug)

        # Check how many polygons describe the buffer and append them to the list ...
        if isinstance(buff, shapely.geometry.multipolygon.MultiPolygon):
            for tmp1 in buff.geoms:
                if not tmp1.is_valid:
                    raise Exception("\"tmp1\" is not a valid Polygon ({0:s})".format(shapely.validation.explain_validity(tmp1)))
                tmp2 = tmp1.simplify(simp)
                if tmp2.is_valid:
                    buffs.append(tmp2)
                else:
                    buffs.append(tmp1)
        elif isinstance(buff, shapely.geometry.polygon.Polygon):
            if not buff.is_valid:
                raise Exception("\"buff\" is not a valid Polygon ({0:s})".format(shapely.validation.explain_validity(buff)))
            tmp1 = buff.simplify(simp)
            if tmp1.is_valid:
                buffs.append(tmp1)
            else:
                buffs.append(buff)
        else:
            raise Exception("\"buff\" is an unexpected type")

    # Convert list to (unified) Polygon and check it ...
    buffs = shapely.ops.unary_union(buffs)
    if not buffs.is_valid:
        raise Exception("\"buffs\" is not valid")

    # Return answer ...
    return buffs
