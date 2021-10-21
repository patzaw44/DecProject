"""Zadanie 9

Na zajęciach zrealizowaliśmy program, którego wymagania określono poniżej

Napisz grę, której celem jest odgadnięcie liczby wylosowanej przez komputer. Jeżeli:

    użytkownik trafi zadaną liczbę, gra się kończy.

    użytkownik poda liczbę mniejszą, komputer wyświetla napis "Podana liczba jest za mała, spróbuj ponownie"

    użytkownik poda liczbę większą, komputer wyświetla napis "Podana liczba jest za duża, spróbuj ponownie"

   W ramach zadania domowego, zmodyfikuj program tak, żeby użytkownik miał ograniczoną liczbę strzałów (np. 6).
   Wprowadź również system punktowy, który będzie premiował szybsze odgadnięcie liczby. Przykładowo:

za samo odgadnięcie użytkownik dostaje 10 punktów

za każdą zachowaną próbę użytkownik dostaje kolejne 10 punktów,
czyli

jeśli odgadł w pierwszej próbie, to powinien zdobyć 10 + 50 punktów (bo zostało mu 5 prób)

jeśli odgadł w ostatniej próbie, to powienien dostać 10 punktów (nie zostały mu żadne próby, więc nie ma bonusu)

    """


import random

wylosowana_liczba = random.randint(1, 100)
print(wylosowana_liczba)

# wariant 1
# while True:
#     liczba_uzytkownika = int(input("Podaj liczbę z zakresu 1-100: "))
#     if wylosowana_liczba == liczba_uzytkownika:
#         print("Zgadłeś")
#         break
#     elif liczba_uzytkownika > wylosowana_liczba:
#         print("Podana liczba jest za duża")
#     elif liczba_uzytkownika < wylosowana_liczba:
#         print("Podana liczba jest za mała")


# wariant 2
liczba_uzytkownika = int(input("Podaj liczbę z zakresu 1-100"))
while wylosowana_liczba != liczba_uzytkownika:
    if liczba_uzytkownika > wylosowana_liczba:
        print("Za duża")
    elif liczba_uzytkownika < wylosowana_liczba:
        print("Za mała")
    liczba_uzytkownika = int(input("Podaj liczbę z zakresu 1-100"))