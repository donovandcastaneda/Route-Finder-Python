import sys
import time
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from eucildean_distance import euclidean_distance


def dfs(graph, start, goal, cities_coordinates, path=[], visited=set(), distance=0):
    if start not in path:
        path = path + [start]

    if start == goal:
        return path, distance

    if start not in visited:
        visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_distance = distance
            if path:
                # Calculate the distance from the current node to the neighbor
                new_distance += euclidean_distance(cities_coordinates[start], cities_coordinates[neighbor])

            result_path, total_distance = dfs(graph, neighbor, goal, cities_coordinates, path, visited, new_distance)
            if result_path:
                return result_path, total_distance

    return None, 0





