"""
Zadanie 30

Napisz klasę, która będzie zawierała trzy metody:

    pobierz_napis - pobiera napis od użytkownika
    wyswietl_napis - wyświetla wczesniej pobrany napis od uzytkownika
    wyswietl_odwrocony_napis

Dla każdego stworzonego obiektu, metoda pobierz_napis może być wywołana tylko raz.
"""


class Napis:
    def __init__(self):
        self.napis_uzytkownika = input("Podaj napis: ")

    def pobierz_napis(self):
        """Pobiera napis od użytkownika."""
        return self.napis_uzytkownika

    def wyswietl_napis(self):
        """Wyświetla wczesniej pobrany napis od uzytkownika."""
        return napis1.pobierz_napis()

    def wyswietl_odwrocony_napis(self):
        """Wyswietla odwrocony napis."""
        lista = list(self.napis_uzytkownika)
        lista.reverse()
        odwrocony_napis = ''.join(lista)
        return odwrocony_napis


napis1 = Napis()
napis1.pobierz_napis()
print(napis1.wyswietl_napis())
print(napis1.wyswietl_odwrocony_napis())
