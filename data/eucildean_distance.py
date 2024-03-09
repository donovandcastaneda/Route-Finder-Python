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

city1 = 'Abilene'
city2 = 'Wichita'

coord1 = cities_coordinates[city1]
coord2 = cities_coordinates[city2]

distance = euclidean_distance(coord1, coord2)

print(f"Euclidean distance between {city1} and {city2}: {distance:.4f}")


