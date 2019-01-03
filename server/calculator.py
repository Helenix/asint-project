from math import radians, cos, sin, asin, sqrt

class Calculator:
    def findDistance(point1, point2):
        lat1 = point1[0]
        lng1 = point1[1]
        lat2 = point2[0]
        lng2 = point2[1]

        lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])

        dlng = lng2 - lng1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 

        return c*r*1000