import sys
import time
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
from graph import graph



# depth limited search used in id-dfs
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


start_town = 'Anthony'
end_town = 'Wichita'
max_depth = 10 

start_time = time.time()  
path = iddfs(graph, start_town, end_town, max_depth)
end_time = time.time()  

if path:
    print("Path found from", start_town, "to", end_town, ":", " -> ".join(path))
else:
    print(f"No path could be found from {start_town} to {end_town}.")
print(f"Search completed in {end_time - start_time:.4f} seconds.")

