import csv

def wywolaj_zwykly_czytacz():
    with open('plik.csv', encoding="utf-8") as csvfile:
        print(csvfile)
        czytacz = csv.reader(csvfile)
        print(czytacz)
        numer_wiersza = 0
        for wiersz in czytacz:
            if numer_wiersza == 0:
                numer_wiersza += 1
                continue
            numer_wiersza += 1
            imie = wiersz[0]
            pensja = int(wiersz[4]) # wiersz[-1]
            if pensja > 2000:
                print(imie)
            # print(wiersz)

def wywolaj_slownikowy_czytacz():
    with open("plik.csv", encoding="utf-8") as plik_csv:
        czytacz = csv.DictReader(plik_csv)
        for wiersz in czytacz:
            print(wiersz['stanowisko'])

wywolaj_slownikowy_czytacz()
