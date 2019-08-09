from csv import DictReader

with open('CSV/fighters.csv') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # print(row)
        print(row['Name'])
