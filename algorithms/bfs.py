import sys
import time
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from collections import deque


visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(graph, start, goal):
    visited = set([start])
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == goal:
            return path

        for next_vertex in graph.get(vertex, []):
            if next_vertex not in visited:
                visited.add(next_vertex)
                new_path = list(path)
                new_path.append(next_vertex)
                queue.append(new_path)

    return None

