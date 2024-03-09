import csv
def load_towns(file_path):
    towns = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) 
        for row in csv_reader:
            town = row[0] 
            latitude = float(row[1])  
            longitude = float(row[2]) 
            towns[town] = (latitude, longitude)
    return towns


cities_coordinates = load_towns("files/coordinates.csv")



