import csv
with open("plik.csv", encoding="utf-8") as csvfile:
    print(csvfile)
    reader = csv.reader(csvfile)
    print(reader)
    for wiersz in reader:
        print(wiersz)
