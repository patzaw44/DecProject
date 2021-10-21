"""Zadanie

Napisz program, który będzie zawierał funkcję oblicz_wyplate. Funkcja ta powinna obliczać wynagrodzenie,
które ma otrzymać użytkownik:

    użytkownik wprowadza liczbę przepracowanych godzin

    użytkownik wprowadza stawkę godzinową

    nadgodziny (wszystko, co powyżej 160h) są liczone ze współczynnikiem 1.5"""

# # 1 sposób lekko zmieniony:
# def oblicz_wyplate(liczba_przepracowanych_godzin, stawka_godzinowa):
#     if liczba_przepracowanych_godzin >= 160:
#         nadgodziny = int(input("Wprowadź liczbę nadgodzin: "))
#         wyplata = (liczba_przepracowanych_godzin * stawka_godzinowa) + (1.5 * nadgodziny)
#         return wyplata
#     else:
#         wyplata = liczba_przepracowanych_godzin * stawka_godzinowa
#         return wyplata
#
# liczba_przepracowanych_godzin = float(input("Wprowadź liczbę przepracowanych godzin: "))
# stawka_godzinowa = float(input("Wprowadź stawkę gozinową: "))
#
# print(oblicz_wyplate(liczba_przepracowanych_godzin, stawka_godzinowa))

# 2 sposób lekko zmieniony:
# ZMIENNE GLOBALNE
PODSTAWOWA_LICZBA_GODZIN = 160
PRZELICZNIK_NADGODZIN = 1.5

def oblicz_wyplate_v2(liczba_przepracowanych_godzin, stawka_godzinowa):
    if liczba_przepracowanych_godzin > PODSTAWOWA_LICZBA_GODZIN:
        nadgodziny = liczba_przepracowanych_godzin-PODSTAWOWA_LICZBA_GODZIN
    else:
        nadgodziny = 0
    wynagrodzenie_podstawowe = min(liczba_przepracowanych_godzin,PODSTAWOWA_LICZBA_GODZIN) * stawka_godzinowa
    wynagrodzenie_nadgodziny = nadgodziny * stawka_godzinowa * PRZELICZNIK_NADGODZIN
    wynagrodzenie = wynagrodzenie_podstawowe + wynagrodzenie_nadgodziny
    print(f"Podstawa -> {wynagrodzenie_podstawowe} zł, nadgodziny -> {wynagrodzenie_nadgodziny}zł.")
    return wynagrodzenie

liczba_przepracowanych_godzin = float(input("Wprowadź liczbę przepracowanych godzin: "))
stawka_godzinowa = float(input("Wprowadź stawkę godzinową: "))

# print(oblicz_wyplate(liczba_przepracowanych_godzin, stawka_godzinowa))
print(oblicz_wyplate_v2(liczba_przepracowanych_godzin, stawka_godzinowa))