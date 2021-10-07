"""Zadanie

Napisz program, który pobiera od użytkownika wynik z testu w % i wyświetla odpowiadającą temu wynikowi ocenę.

Przykładowa skala ocen:

91 % – 100 % -> 5

75 % – 90 % -> 4

51 % – 74 % -> 3

30 % – 50 % -> 2

0 % – 29 % -> 1"""

wynik = int(input("Podaj wynik testu w %: "))

if 91 <= wynik <= 100:
    print("Ocena to: 5. ")
elif 75 <= wynik <= 90:
    print("Ocena to: 4. ")
elif 51 <= wynik <= 74:
    print("Ocena to: 3. ")
elif 30 <= wynik <= 50:
    print("Ocena to: 2. ")
elif 0 <= wynik <= 29:
    print("Ocena to: 1. ")