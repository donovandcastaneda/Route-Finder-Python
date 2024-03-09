import csv
def load_towns(file_path):
    towns = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            town = row[0]  # Assuming town is the first column
            latitude = float(row[1])  # Assuming latitude is the second column
            longitude = float(row[2])  # Assuming longitude is the third column
            towns[town] = (latitude, longitude)
    return towns


# Assuming your file is located at 'files/coordinates.csv'
cities_coordinates = load_towns("files/coordinates.csv")
print(cities_coordinates)



