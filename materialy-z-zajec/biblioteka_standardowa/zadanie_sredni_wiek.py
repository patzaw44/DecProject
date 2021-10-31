import csv
with open("zadanie_sredni_wiek.py.csv", encoding="utf-8") as csvfile:
    print(csvfile)
    reader = csv.reader(csvfile)
    print(reader)
    for wiersz in reader:
        print(wiersz)