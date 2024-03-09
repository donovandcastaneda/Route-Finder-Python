



def create_map(file_path):
    adjacenties = {}
    with open(file_path, 'r') as file:
        for line in file:
            town1, town2 = line.strip().split()
            if town1 not in adjacenties:
                adjacenties[town1] = []
            if town2 not in adjacenties:
                adjacenties[town2] = []
            adjacenties[town1].append(town2)
            adjacenties[town2].append(town1)  
    return adjacenties

graph = create_map("files/Adjacencies.txt")
print(graph)



