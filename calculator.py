from math import radians, cos, sin, asin, sqrt

class Calculator:
    def findDistance(point1, point2):
        lat1 = point1[0]
        long1 = point1[1]
        lat2 = point2[0]
        long2 = point2[1]

        lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])

        dlong = long2 - long1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 

        return c*r*1000