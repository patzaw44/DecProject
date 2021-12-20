"""
Stwórz klasę Pracownik, która będzie zawierała następujące atrybuty i metody
• (a) imię i nazwisko
• (a) data zatrudnienia
• (a) wypłata podstawowa
• (m) oblicz staż pracy
• (m) oblicz wypłatę
Następnie stwórz klasę Manager, która będzie dziedziczyła po klasie Pracownik
• dodaj atrybut przechowujący datę objęcia stanowiska
• nadpisz atrybut wypłata podstawowa poprzez przypisanie do niego nowej wartości
• nadpisz metodę do obliczania wypłata, żeby uwzględnić bonus za stanowisko (np. mnożnik
1.5x)
• dodaj nową metodę, która obliczy jak długa dana osoba przebywa na stanowisku
"""
import datetime


class Pracownik:
    def __init__(self, imie, nazwisko, data_zatrudnienia, wyplata_podstawowa, obl_staz_pracy, obl_wyplate):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_zatrudnienia = data_zatrudnienia
        self. wyplata_podstawowa = wyplata_podstawowa
        self.obl_staz_pracy = obl_staz_pracy
        self.obl_wyplate = obl_wyplate

class Manager(Pracownik):
    super()

    def dlugosc_pracy(self):
        obl_staz_pracy = self.data_zatrudnienia - datetime



