"""Zadanie

Napisz program który:

    Przypisuje zmiennej wartość będącą listą dowolnych elementów (np. imion uczestników zajęć)

    Wypisuje każde imię tak, żeby zaczynało się od małej litery

    Sortuje listę alfabetycznie i wypisuje pierwsze imię"""

imie1 = input("Podaj 1 imie:")
imie2 = input("Podaj 2 imie:")
imie3 = input("Podaj 3 imie:")
imie4 = input("Podaj 4 imie:")
imie5 = input("Podaj 5 imie:")

imiona = [imie1, imie2, imie3, imie4, imie5]
posortowane_imiona = sorted(imiona)
# for imie in imiona:
#     print(imie.lower())
#     print(imie[0].lower()+imie[1:])
#     male_imiona.append(male_imiona)
# posortowane_imiona = sorted(imiona)
imiona.sort()
print(imiona)
