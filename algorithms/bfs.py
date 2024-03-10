import sys
import time
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from collections import deque
from eucildean_distance import euclidean_distance


def bfs(graph, start, goal, cities_coordinates):
    visited = set([start])
    queue = deque([([start], 0)])

    while queue:
        path, distance = queue.popleft()
        vertex = path[-1]

        if vertex == goal:
            return path, distance

        for next_vertex in graph.get(vertex, []):
            if next_vertex not in visited:
                visited.add(next_vertex)
                new_distance = distance + euclidean_distance(cities_coordinates[vertex], cities_coordinates[next_vertex])
                queue.append((path + [next_vertex], new_distance))

    return None, 0

