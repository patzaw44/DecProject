""""
Zadanie 17
Poznaliśmy metodę na napisach, która nazywała się replace.
Napisz własną funkcję, która nie będzie korzystała z metody replace, ale odtworzy jej zachowanie dla zmieniania
pojedynczego znaku.

Funkcja powinna przyjąć 3 argumenty:

1) napis, który chcemy zmodyfikować
2) stary znak
3) nowy znak

np. my_replace("1234", "1", "9") -> "9234" """


def zamiana_znaku(napis, stary_znak, nowy_znak):
    """Funkcja zamieniająca stary znak na nowy."""
    napis = list(napis)
    print(type(napis))
    try:
        znak_indeks = napis.index(stary_znak)
        napis[znak_indeks] = nowy_znak
        napis = ''.join(napis)
        print(f"Po zamianie: {napis}")
    except ValueError:
        print("Brak podanego znaku.")


zamiana_znaku(napis="1234", stary_znak="1", nowy_znak="9")
