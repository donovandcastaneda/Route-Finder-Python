import time  
from queue import PriorityQueue
import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')

from eucildean_distance import euclidean_distance



def best_first_search(start, goal, graph, cities_coordinates):
    start_time = time.time()
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}


    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            end_time = time.time()  
            path = reconstruct_path(came_from, current)
            execution_time = end_time - start_time
            print(f"Path reconstructed: {' -> '.join(path)}")
            print(f"Goal reached in {execution_time:.4f} seconds") 
            return path

        for neighbor in graph[current]:
            if neighbor not in came_from:
                priority = euclidean_distance(cities_coordinates[neighbor], cities_coordinates[goal])
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    print("No path found")
    return None

def reconstruct_path(came_from, current):
    path = [current]
    visited = set([current])  # Keep track of visited nodes to detect cycles

    while current in came_from:
        current = came_from[current]
        if current in visited:
            break  # Break the loop to prevent infinite cycling
        visited.add(current)
        path.append(current)

    path.reverse()
    return path







