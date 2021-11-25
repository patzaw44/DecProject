"""
Zadanie 26

Napisz własny generator imion i nazwisk. Przygotuj dwa pliki: jeden z imionami, drugi z nazwiskami (można więcej,
jeżeli chcemy mieć podział na płeć). Zapytaj użytkownika ile tożsamości (imię + nazwisko) chce wygenerować,

wygeneruj je na podstawie imion i nazwisk ze wspomnianych plików, a następnie zapisz do nowego pliku
"""
from imie import imie
from nazwisko import nazwisko
import random
newcalosc = []


def generator_tozsamosci(ile_osob):
    for i in range(ile_osob):
        los_imie = random.choice(imie)
        los_nazwisko = random.choice(nazwisko)
        calosc = [f"{los_imie}  {los_nazwisko}"]
        newcalosc.extend(calosc)
    print(f"{newcalosc}")
    # Zapis do 'generator.txt' -> zamiana listy na str
    str_newcalosc = ', '.join(newcalosc)
    print(f"{str_newcalosc}")
    zapis = open("generator_zapis.txt", "w", encoding="UTF-8")
    zapis.writelines(str_newcalosc)
    zapis.close()


generator_tozsamosci(int(input("Ile chcesz tożsamości: ")))
