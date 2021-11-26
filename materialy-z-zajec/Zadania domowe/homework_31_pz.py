"""
Zadanie 31

Stwórz klasę BazaFilmow w ramach, której korzystasz z danych zawartych w pliku movies.json (załączony poniżej).
Każdy pojedynczy film powinien być reprezentowany przez klasę Film.

    odpowiednio przetwórz dane z pliku, żeby otrzymać listę instancji klasy Film
    klasa BazaFilmow powinna zawierać metodę do sortowania filmów po nazwie
    klasa BazaFilmow powinna zawierać metodę do sortowania filmów po roku
    klasa BazaFilmow powinna zawierać metodę do obliczenia różnicy w latach między najstarszym, a najnowszym filmem

"""
import json


class BazaFilmow:
    def __init__(self, dane):
        self.dane = dane

    def wyswietl_dane(self):
        return self.dane


class Film:
    def wyswietl_liste_filmow(BazaFilmow):
        dane_film = dane
        lista = list(dane_film[0])
        print(lista)


with open("movies.json", mode="r", encoding="utf-8") as f:
    dane = json.load(f)
    print(type(dane))

filmowo = BazaFilmow(dane)
filmowo.wyswietl_dane()
print(filmowo.wyswietl_dane())
filmowo2 = Film()
filmowo2.wyswietl_liste_filmow()
