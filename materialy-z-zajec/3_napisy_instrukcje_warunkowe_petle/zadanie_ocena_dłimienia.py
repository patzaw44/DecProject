"""Zadanie

Napisz program, który umożliwi wprowadzenie imienia użytkownika, a następnie oceni, czy jest ono długie czy nie.
Uznajmy, że imiona dłuższe niż 8 znaków (czyli od 9 w górę) są długie, zaś pozostałe traktujemy jako krótkie.

Program powinien wyświetlić użytkownikowi informację (napis) z decyzją,
np. "Twoje imię zostało sklasyfikowane jako krótkie"""

imie = input("Wprowadz imie:")
new_imie =len(imie)
print(new_imie)
if new_imie <= 8:
    print("Twoje imię zostało sklasyfikowane jako krótkie.")
else:
    print("Twoje imię zostało sklasyfikowane jako długie.")