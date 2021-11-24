"""
Zadanie 23

Napisz program, który będzie zawierał funkcję, która dla tekstu przekazanego jako parametr zwróci listę wszystkich dat,
 które wystąpiły w tym tekście. Dla uproszczenia można uznać, że interesują nas tylko daty w formacie YYYY-MM-DD.
 Do znalezienia dat użyj modułu z wyrażeniami regularnymi re

"""
import re


def lista_wszystkich_dat(tekst):
    data = re.compile(r'\d\d\d\d-\d\d-\d\d')   # lub \d{3}-\d{2}-\d{2}
    szukanie = data.findall(tekst)
    print(f'Znaleziono daty: {szukanie}')


lista_wszystkich_dat("Tekst z dnia 2021-08-24, innego dnia 2020-08-28.")
