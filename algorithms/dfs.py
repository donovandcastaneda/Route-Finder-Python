import sys
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from graph import graph


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

start_town = 'Anthony'
end_town = 'Wichita'

# Find a path using DFS
path = dfs(graph, start_town, end_town)

# Print the result
if path:
    print("Path found from", start_town, "to", end_town, ":", " -> ".join(path))
else:
    print(f"No path could be found from {start_town} to {end_town}.")
