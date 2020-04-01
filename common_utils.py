from math import radians, sin, cos, sqrt, asin

def distance(slat,slon,elat,elon):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(float(slon))
    lon2 = radians(float(elon))
    lat1 = radians(float(slat))
    lat2 = radians(float(elat))

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)