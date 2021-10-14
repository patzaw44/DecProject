"""Zadanie

Napisz grę, której celem jest odgadnięcie losowej liczby. Jeżeli:

    użytkownik trafi zadaną liczbę, gra się kończy.

    użytkownik poda liczbę mniejszą, komputer wyświetla napis "Podana liczba jest za mała, spróbuj ponownie"

    użytkownik poda liczbę większą, komputer wyświetla napis "Podana liczba jest za duża, spróbuj ponownie"

Dla ułatwienia, podano kod, który generuje liczbę z zakresu 1-100"""

import random
wylosowana_liczba = random.randint(1, 100) #losowanie jednej liczby do 100
# print(random.randrange(1,100, 2)) #losowanie liczby nieparzstych bez 100
print(wylosowana_liczba)



# #wariant 1
# while True:#while 2>1; petla nieskonczona az zgadnie uzytkownik
#     liczba_uzytkownika = int(input("Podaj liczbę z zakresu 1-100: "))
#     if wylosowana_liczba == liczba_uzytkownika:
#         print("Zgadłeś")
#         break # odgadniecie petli powoduje wyjscie z petli
#     elif liczba_uzytkownika > wylosowana_liczba:
#         print("Podana liczba jest za duża")
#     elif liczba_uzytkownika < wylosowana_liczba:
#         print("Spróbuj jeszcze raz")

# wariant 2

liczba_uzytkownika = int(input("Podaj liczbe z zakresu 1-100: "))
while wylosowana_liczba != liczba_uzytkownika:
    if liczba_uzytkownika> wylosowana_liczba:
        print("Za duża")
    elif liczba_uzytkownika < wylosowana_liczba:
        print("Za mała")
    liczba_uzytkownika = int(input("Podaj liczbę z zakresu 1-100: "))
print("Zgadłeś")