from csv import reader

with open('CSV/fighters.csv') as file:
    csv_reader = reader(file)
    name = 0
    country = 1
    height = 2
    for fighter in csv_reader:
        print(f"{fighter[name]} is from {fighter[country]}")
