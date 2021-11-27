"""Zadanie 12

Napisz program, który:

    pozwoli użytkownikowi na wprowadzenie wyrazu

    następnie policzy i wyświetli wynik punktowy w Scrabble na podstawie wcześniej zdefiniowanej punktacji

np. literka a to 1 punkt, literka b to 3 punkty itd.

-> zadanie można rozwiązać na wiele sposobów, więc do Ciebie zależy wybór jak taka punktacja będzie przechowywana

-> należy uwzględnić, że jakaś literka w wyrazie podanym przez użytkownika nie będzie uwzględniona w punktacji
(można przyjąć, że dostaje on za nią 0 punktów)"""

WYRAZ = list(input("Wprowadź wyraz: ").lower())
print(WYRAZ)
PUNKTACJA = {'a': 1, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 5, 'g': 3, 'h': 3, 'i': 1, 'j': 3, 'k': 2, 'l': 2, 'm': 2,
             'n': 1, 'o': 1, 'p': 2, 'q': 5, 'r': 1, 's': 1, 't': 2, 'u': 3, 'w': 1, 'v': 5, 'y': 2, 'x': 3, 'z': 1}




def obliczanie_punktow():

    wyraz_pkty = {litera: PUNKTACJA.get(litera) for litera in WYRAZ}
    # if WYRAZ != PUNKTACJA:
    # # wyraz_pkty.pop((not PUNKTACJA.keys(), 0))
    #     new_wyraz = {"0": 0}
    #     WYRAZ.append(new_wyraz)

    if not WYRAZ in wyraz_pkty.keys():
            print("))))")



    # if wyraz_pkty.values() == "None":
    #     # wyraz_pkty.pop((not PUNKTACJA.keys(), 0))
    #     new_wyraz = {"0": 0}
    #     WYRAZ.append(new_wyraz)
    # print(wyraz_pkty)
    pkty = int(sum(wyraz_pkty.values()))
    print(f"Suma wynosi: {pkty}.")

obliczanie_punktow()

# punktacja ={"a": 1, "ą":22, "b": 3, "c": 5, "ć":6, "d": 7, "e": 0, "ę":70, "f": 2, "g": 3, "h": 1, "i": 1, "j": 1, "k": 0, "l": 2, "ł":6, "m": 4, "n": 4, "ń":8, "o": 0, "ó":23, "p": 0, "r" : 0, "s" : 3, "ś": 50, "t" : 1, "u" : 1, "w" : 1, "y":19, "ź": 40, "ż": 50, "z": 12}
# slowo = input("Podaj proszę słowo:").lower()
#
# suma = 0
# for litera in slowo:
#     if litera not in punktacja:
#         punktacja[litera] = 10
#     suma += punktacja[litera]
#
# print(f"Suma punktów za podane słowo wynosi {suma}")
