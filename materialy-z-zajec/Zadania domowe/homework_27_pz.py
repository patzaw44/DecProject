"""
Zadanie 27

Odczytaj informacje o piosenkach z załączonego poniżej pliku json. Znajdź artystę, który pojawia się tam najwięcej
 razy.
"""
import json


with open("songs.json", mode="r", encoding="utf-8") as f:
    baza = json.load(f)
    print(type(baza))

# wyswietl w formie listy : wartosc["artysta"] -> dla wartosci w liscie
lista_artysci = [value['artist'] for value in baza]
# print(lista_artysci)


def liczba_pojawiajacych_sie_artystow():
    """ile razy pojawiają się artyści"""
    liczba_wyrazow = {}
    for wyraz in lista_artysci:
        liczba_wyrazow.setdefault(wyraz, 0)
        liczba_wyrazow[wyraz] = liczba_wyrazow[wyraz]+1
    print(liczba_wyrazow)


liczba_pojawiajacych_sie_artystow()


def najczestszy_artysta():
    """Artysta, który pojawia się tam najwięcej razy - dłuższa wersja."""
    przelicznik = 0
    artysta = lista_artysci[0]

    for x in lista_artysci:
        czestotliwosc = lista_artysci.count(x)
        if czestotliwosc > przelicznik:
            przelicznik = czestotliwosc
            artysta = x
    print(f"Najczęsciej pojawiający się artysta:{artysta}.")


najczestszy_artysta()


def najczestszy_artysta2():
    """Artysta, który pojawia się tam najwięcej razy - krótsza wersja."""
    zbior_artysci = set(lista_artysci)
    print(f"Najczęsciej pojawiający się artysta: {max(zbior_artysci, key=lista_artysci.count)}.")


najczestszy_artysta2()
