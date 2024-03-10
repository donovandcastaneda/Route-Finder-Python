import sys
import time
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/data')
sys.path.append('/Users/donovancastaneda/Documents/School Documents/Homework/route-finder/algorithms')

from graph import graph
from coordinates import cities_coordinates

from bfs import bfs
from dfs import dfs
from iddfs import iddfs
from a_star_search import a_star_search
from best_first_search import best_first_search



def display_town_selection(towns):
    for index, town in enumerate(sorted(towns), start=1):
        print(f"{index}. {town}")
    print()


def get_town_by_selection(towns, prompt):
    while True:
        try:
            choice = int(input(prompt)) - 1  # Adjust for zero-based indexing
            if 0 <= choice < len(towns):
                return towns[choice]  # Return the town name directly
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Please enter a number.")
            
            
            
def select_route_finding_method():
    methods = ["Breadth First Search", "Depth First Search", "Iterative Deepening - Depth First Search", "A* Search", "Best First Search"]
    print("Available route finding methods:")
    for index, method in enumerate(methods, start=1):
        print(f"{index}. {method}")
    print()

    while True:
        try:
            choice = int(input("Select the number corresponding to the method: ")) - 1
            if 0 <= choice < len(methods):
                return methods[choice]
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Please enter a number.")
            
            
            
            
            
            

def main():
    while True:  # Start of the loop

        all_towns = set(graph.keys()) | {town for neighbors in graph.values() for town in neighbors}
        towns_list = sorted(all_towns)

        print("Available towns:")
        display_town_selection(towns_list)

        start_town = get_town_by_selection(towns_list, "Select the number corresponding to the starting town: ")  # This is a town name
        print(f"Starting town selected: {start_town}")

        end_town = get_town_by_selection(towns_list, "Select the number corresponding to the ending town: ")  # This is a town name
        print(f"Ending town selected: {end_town}")
        
        selected_method = select_route_finding_method()
        print(f"Route finding method selected: {selected_method}")
        
        if selected_method == "Breadth First Search":
            start_time = time.time()
            path, distance = bfs(graph, start_town, end_town, cities_coordinates)
            end_time = time.time()
        elif selected_method == "Depth First Search":
            start_time = time.time()
            path, distance = dfs(graph, start_town, end_town, cities_coordinates)
            end_time = time.time()

        elif selected_method == "Iterative Deepening - Depth First Search":
            max_depth = 10 
            start_time = time.time()
            path, distance = iddfs(graph, start_town, end_town, max_depth, cities_coordinates)  # Adjusted to unpack properly
            end_time = time.time()

        elif selected_method == "A* Search":
            start_time = time.time()
            path, distance = a_star_search(start_town, end_town, graph, cities_coordinates)
            end_time = time.time()

        elif selected_method == "Best First Search":
            start_time = time.time()
            path, distance = best_first_search(start_town, end_town, graph, cities_coordinates)
            end_time = time.time()

        if path:
            print("Path found from", start_town, "to", end_town, ":", " -> ".join(path))
            print(f"Total distance: {distance:.2f} units") 

        else:
            print(f"No path could be found from {start_town} to {end_town}.")
        print(f"{selected_method} completed in {end_time - start_time:.4f} seconds.")
        
        print("Do you want to perform another search?")
        print("1. Yes")
        print("2. No")
        try:
            repeat = int(input("Select an option (1/2): ").strip())
            if repeat == 2:
                break  
            elif repeat != 1:
                print("Invalid selection, please select 1 for Yes or 2 for No.")
        except ValueError:
            print("Please enter a number (1 for Yes or 2 for No).")



if __name__ == "__main__":
    main()

