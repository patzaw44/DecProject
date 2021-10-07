"""Zadanie

Napisz program, który poprosi użytkownika o podanie słowa, a następnie wypisze na ekran czy dane słowo jest palindromem."""

slowo = input("Wypisz słowo: ")
odwrocone_slowo = slowo[::-1]
print(odwrocone_slowo)

print(slowo == odwrocone_slowo)