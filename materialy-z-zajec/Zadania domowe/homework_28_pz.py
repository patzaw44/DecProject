"""Zadanie 28

Napisz program, który wyświetli tylko zakomentowane linijki we wszystkich plikach Pythonowych w bieżącym folderze"""


def sprawdz_czy_komentarz(linijka):
    return linijka.startswith("#")


def znajdz_komentarze_w_pliku(nazwa_pliku):
    lista_komentarzy = []
    with open(nazwa_pliku, mode='r', encoding="utf-8") as f:
        for linijka in f:
            oczyszczona_linijka = linijka.strip()
            if sprawdz_czy_komentarz(oczyszczona_linijka):
                lista_komentarzy.append(oczyszczona_linijka)
                print(oczyszczona_linijka)
    return lista_komentarzy


znajdz_komentarze_w_pliku("homework_27_pz.py")
