# -*- coding: utf-8 -*-

def find_middle_of_great_circle(lon1_deg = 0.0, lat1_deg = 0.0, lon2_deg = 0.0, lat2_deg = 0.0):
    # NOTE: math.sqrt() has been replaced with math.hypot() where possible.
    # NOTE: math.atan() has been replaced with math.atan2() where possible.

    # Import modules ...
    import math

    # Convert to radians ...
    lon1_rad = math.radians(lon1_deg)                                           # [rad]
    lat1_rad = math.radians(lat1_deg)                                           # [rad]
    lon2_rad = math.radians(lon2_deg)                                           # [rad]
    lat2_rad = math.radians(lat2_deg)                                           # [rad]

    # Calculate mid-point ...
    Bx = math.cos(lat2_rad) * math.cos(lon2_rad - lon1_rad)
    By = math.cos(lat2_rad) * math.sin(lon2_rad - lon1_rad)
    lat3_rad = math.atan2(
        math.sin(lat1_rad) + math.sin(lat2_rad),
        math.sqrt((math.cos(lat1_rad) + Bx) * (math.cos(lat1_rad) + Bx) + By * By)
    )                                                                           # [rad]
    lon3_rad = lon1_rad + math.atan2(By, math.cos(lat1_rad) + Bx)               # [rad]

    # Return middle point ...
    return math.degrees(lon3_rad), math.degrees(lat3_rad)
