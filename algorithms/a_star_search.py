import time
from queue import PriorityQueue

import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')

from eucildean_distance import euclidean_distance


def a_star_search(start, goal, graph, cities_coordinates):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {start: None}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = euclidean_distance(cities_coordinates[start], cities_coordinates[goal])

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path, total_distance = reconstruct_path(came_from, current, cities_coordinates)
            return path, total_distance  # Ensure both path and distance are returned

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + euclidean_distance(cities_coordinates[current], cities_coordinates[neighbor])
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + euclidean_distance(cities_coordinates[neighbor], cities_coordinates[goal])
                if not any(neighbor == item[1] for item in open_set.queue):
                    open_set.put((f_score[neighbor], neighbor))

    return None, 0  # Return None for the path and 0 for the distance if no path is found

def reconstruct_path(came_from, current, cities_coordinates):
    total_path = [current]
    total_distance = 0

    while came_from[current] is not None:
        current = came_from[current]
        total_path.append(current)

    total_path.reverse()

    # Calculate the total distance based on the reconstructed path
    for i in range(len(total_path) - 1):
        total_distance += euclidean_distance(cities_coordinates[total_path[i]], cities_coordinates[total_path[i + 1]])

    return total_path, total_distance
