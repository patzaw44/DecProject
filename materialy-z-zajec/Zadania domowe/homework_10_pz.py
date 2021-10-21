"""Zadanie 10

Napisz program, który wylosuje użytkownikowi słowo z przygotowanej wcześniej listy słów.

Następnie powinien on wyświetlić użytkownikowi to słowo z pomieszaną kolejnością liter

Zadaniem użytkownika jest odgadnięcie, jakie to słowo

Wskazówka, przydatne mogą się okazać metody modułu random

import random
help(random.choice)
help(random.shuffle)
"""

import random

slowa = ["książka", "zakładka", "płyta", "odtwarzacz", "lampka", "koc"]
# losowanie wyrazu
wyraz = random.choice(slowa)
# print(wyraz)
pomieszane_litery = list(wyraz)
print(pomieszane_litery)
# pomieszane litery w wyrazie
random.shuffle(pomieszane_litery)
print(pomieszane_litery)

zagadka = input("Proszę o odgadnięcie słowa: ")

if zagadka == wyraz:
    print("Brawo! To jest prawidłowy wyraz!")
else:
    print("Niestety, to nie jest prawidłowy wyraz.")
