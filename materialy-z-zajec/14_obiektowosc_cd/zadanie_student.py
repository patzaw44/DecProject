"""Zadanie

Zdefiniuj klasę Student, która będzie zawierała następujące atrybuty

    imię, nazwisko
    kierunek i uczelnię
    nr_legitimacji
    listę ocen

Chcemy dopisać do niej następujące metody

    obliczanie średniej ocen
    sprawdzanie poprawności nr legitimacji
    metodę do stworzenia studenta informatyki PG

Na podstawie opisu zaproponuj typ metody i ją zaimplementuj"""


class Student:

    def __init__(self, imie, nazwisko, nr_indeksu, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.oceny = oceny

    def __str__(self):
        return f"Osoba {self.imie} {self.nazwisko} {self.nr_indeksu} {self.oceny}."


osoba1 = Student("Jan", "Kowalski", 221458, [4,4,5,1])

print(osoba1)

# metoda w klasie zweryfikowac
#  srednia w klasie
