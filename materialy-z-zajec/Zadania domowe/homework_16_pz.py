"""
Zadanie 16

Napisz program do generowania haseł o długości zadanej przez użytkownika.

Hasło powinno się zmieniać wraz z każdym uruchomieniem programu.

Pamiętaj, że dobre hasło powinno zawierać zarówno małe jak i duże litery, cyfry oraz znaki specjalne (np. #?%&).
"""
import random
liczba_liter = int(input("Podaj liczbę liter: "))
liczba_liczb = int(input("Podaj liczbę liczb: "))
liczba_znakow = int(input("Podaj liczbę znaków specjalnych: "))


znaki_specjalne = [',', '.', ':', ';', '!', '%', '#', '$', '*', '/']
litery_male = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
           'x', 'c' 'v', 'b', 'n', 'm']

liczby = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


litery_duze = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'z', 'x', 'c' 'v', 'b', 'n', 'm']
zamiana_na_duze_litery = (''.join(litery_duze)).upper()
litery_duze = list(zamiana_na_duze_litery)
litery_mix = litery_male + litery_duze
# print(litery_mix)


def generowanie_hasla():
    haslo = []

    for a in range(1, liczba_liter + 1):
        haslo += random.choice(litery_mix)

    for a in range(1, liczba_znakow + 1):
        haslo += random.choice(znaki_specjalne)

    for a in range(1, liczba_liczb + 1):
        haslo += random.choice(liczby)

    # print(haslo)
    random.shuffle(haslo)
    # print(haslo)
    ladniejsze_wyswietlenie = ''.join(haslo)
    print(f"Twoje hasło : {ladniejsze_wyswietlenie}")


generowanie_hasla()
