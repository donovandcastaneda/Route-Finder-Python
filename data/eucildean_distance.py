import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from coordinates import cities_coordinates
from math import sqrt


def euclidean_distance(coord1, coord2):

    # Calculate differences
    latitude_difference = coord1[0] - coord2[0]
    longitude_difference = coord1[1] - coord2[1]
    
    distance = sqrt(latitude_difference**2 + longitude_difference**2)
    
    return distance




