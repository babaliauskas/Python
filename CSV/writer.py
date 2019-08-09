from csv import writer

with open("CSV/cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Blue', 2])
    csv_writer.writerow(['Kitty', 1])
