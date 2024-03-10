import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from eucildean_distance import euclidean_distance



def dls(graph, start, goal, depth, path, cities_coordinates, distance=0):
    if start == goal:
        return path + [start], distance
    if depth <= 0:
        return None, 0
    for neighbor in graph.get(start, []):
        if neighbor not in path:  
            new_distance = distance + euclidean_distance(cities_coordinates[start], cities_coordinates[neighbor])
            result_path, total_distance = dls(graph, neighbor, goal, depth - 1, path + [start], cities_coordinates, new_distance)
            if result_path:
                return result_path, total_distance
    return None, 0




def iddfs(graph, start, goal, max_depth, cities_coordinates):
    for depth in range(max_depth):
        result_path, total_distance = dls(graph, start, goal, depth, [], cities_coordinates, 0)
        if result_path:
            return result_path, total_distance
    return None, 0






