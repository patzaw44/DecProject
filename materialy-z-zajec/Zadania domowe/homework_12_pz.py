"""Zadanie 12

Napisz program, który:

    pozwoli użytkownikowi na wprowadzenie wyrazu

    następnie policzy i wyświetli wynik punktowy w Scrabble na podstawie wcześniej zdefiniowanej punktacji

np. literka a to 1 punkt, literka b to 3 punkty itd.

-> zadanie można rozwiązać na wiele sposobów, więc do Ciebie zależy wybór jak taka punktacja będzie przechowywana

-> należy uwzględnić, że jakaś literka w wyrazie podanym przez użytkownika nie będzie uwzględniona w punktacji
(można przyjąć, że dostaje on za nią 0 punktów)"""


def obliczanie_punktow(wyraz):
    punktacja = {'a': 1, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 5, 'g': 3, 'h': 3, 'i': 1, 'j': 3, 'k': 2, 'l': 2, 'm': 2,
                 'n': 1, 'o': 1, 'p': 2, 'q': 5, 'r': 1, 's': 1, 't': 2, 'u': 3, 'w': 1, 'v': 5, 'y': 2, 'x': 3, 'z': 1}
    suma = 0
    for litera in wyraz:
        if litera not in punktacja:
            punktacja[litera] = 0
        suma += punktacja[litera]
    print(f"Suma wynosi: {suma}.")


obliczanie_punktow(wyraz=input("Wprowadź wyraz: ").lower())
