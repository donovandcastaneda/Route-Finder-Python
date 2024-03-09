import csv
import math
from queue import PriorityQueue
import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from graph import graph
from coordinates import cities_coordinates
from eucildean_distance import euclidean_distance
from collections import deque






def a_star_search(start, goal, graph, cities_coordinates):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = euclidean_distance(cities_coordinates[start], cities_coordinates[goal])

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            return reconstruct_path(came_from, current)

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

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

# Example usage
start = "Anthony"  
goal = "Hillsboro"
path = a_star_search(start, goal, graph, cities_coordinates)
print("Path found:", path)