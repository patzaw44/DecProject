"""
Zadanie 22
Napisz program, który otwiera plik przewoz_osob_gdynia.csv, a następnie wyświetla daty dla których liczba osób była
największa i najmniejsza.
"""

import csv


def min_max_przewoz_data():
    plik = 'przewoz_osob_gdynia.csv'

    with open(plik) as f:
        reader = csv.reader(f)
        naglowek = next(reader)
        # print(naglowek)
        # zwracane :['tys_osob', 'month']
        for indeks, naglowek_kolumny in enumerate(naglowek):
            print(indeks, naglowek_kolumny)
        data_csv, wartosc_csv = [], []
        for row in reader:
            wartosc_csv.append(row[0])
            data_csv.append(row[1])
            fwartosc_csv = [float(x) for x in wartosc_csv]

        # print(fwartosc_csv)
        # print(data_csv)
        minim = str(min(fwartosc_csv))
        maks = str(max(fwartosc_csv))
        print(f'Data dla których liczba osób była najmniejsza ({minim} osób): {data_csv[wartosc_csv.index(minim)]}.')
        print(f'Data dla których liczba osób była największa ({maks} osób): {data_csv[wartosc_csv.index(maks)]}.')


min_max_przewoz_data()
