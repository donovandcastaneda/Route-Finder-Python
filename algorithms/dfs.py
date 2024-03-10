import sys
import time
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')


def dfs(graph, start, goal, path=[], visited=set()):
   
    path = path + [start]
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result_path = dfs(graph, neighbor, goal, path, visited)
            if result_path:
                return result_path

    return None




