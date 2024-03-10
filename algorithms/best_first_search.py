import time  
from queue import PriorityQueue
import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')

from eucildean_distance import euclidean_distance


def best_first_search(start, goal, graph, cities_coordinates):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {start: None}  # Initialize with start as its own predecessor to signify the start

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path, total_distance = reconstruct_path(came_from, current, cities_coordinates)
            return path, total_distance

        for neighbor in graph[current]:
            if neighbor not in came_from:  # Check if not visited
                priority = euclidean_distance(cities_coordinates[neighbor], cities_coordinates[goal])
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    return None, 0  # Return 0 distance if no path is found


def reconstruct_path(came_from, current, cities_coordinates):
    path = []
    total_distance = 0

    while current is not None:  # Stop when reaching the start of the path
        path.append(current)
        next_node = came_from.get(current)  # Use .get to safely handle None

        if next_node is None or current == next_node:  # Check if at the start or a cycle
            break

        # Calculate distance only if there's a valid next node
        if next_node in cities_coordinates and current in cities_coordinates:
            distance = euclidean_distance(cities_coordinates[current], cities_coordinates[next_node])
            total_distance += distance

        current = next_node

    path.reverse()  # The path is constructed in reverse order
    return path, total_distance










