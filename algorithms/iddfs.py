import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from graph import graph


def dls(graph, start, goal, depth, path):
    if start == goal:
        return path + [start]
    if depth <= 0:
        return None
    for neighbor in graph.get(start, []):
        if neighbor not in path:  
            result_path = dls(graph, neighbor, goal, depth - 1, path + [start])
            if result_path:
                return result_path
    return None



def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        result_path = dls(graph, start, goal, depth, [])
        if result_path:
            return result_path
    return None




