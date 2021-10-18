"""Zadanie

Napisz program, który zliczy ile razy powtarza się każde ze słów z wybranej przez Ciebie piosenki.

Look at the stars, Look how they shine for you

"""

przykladowy_tekst = "Look at the stars, Look how they shine for you, shine, shine"

# 1) pozbycie sie niechcianych znaków
print(przykladowy_tekst)
oczyszczony_tekst = przykladowy_tekst.replace("\n", " ").replace(".", "").replace(",", "").strip()

# 2) podziel zdanie na slowa:

slowa = (oczyszczony_tekst.split(" "))
print(slowa)

# 3) policz slowa
licznik_slow = {}
nowy_slownik = {}
for slowo in slowa:
    if slowo in licznik_slow:
        licznik_slow[slowo] += 1
    else:
        licznik_slow[slowo] = 1
    wystapienia = nowy_slownik.get(slowo,0)
    nowy_slownik[slowo] = wystapienia + 1

print(licznik_slow)