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
            path, total_distance = reconstruct_path(came_from, current, cities_coordinates)  # Adjusted call
            print(f"Total distance: {total_distance}")  # Print the total distance
            return path


        for neighbor in graph[current]:
            # Calculate tentative_g_score as the current g_score plus the distance between current and the neighbor
            tentative_g_score = g_score[current] + euclidean_distance(cities_coordinates[current], cities_coordinates[neighbor])
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + euclidean_distance(cities_coordinates[neighbor], cities_coordinates[goal])
                if not any(neighbor == item[1] for item in open_set.queue):
                    open_set.put((f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current, cities_coordinates):
    total_path = []
    total_distance = 0

    # Start from the goal and work back to the start
    while current in came_from:
        next_node = came_from[current]
        total_path.append(current)

        # Ensure current is in cities_coordinates to prevent KeyError
        if current in cities_coordinates and next_node in cities_coordinates:
            distance = euclidean_distance(cities_coordinates[current], cities_coordinates[next_node])
            total_distance += distance

        current = next_node

    total_path.append(current)  # Append the start node
    total_path.reverse()  # The path was constructed in reverse
    return total_path, total_distance



