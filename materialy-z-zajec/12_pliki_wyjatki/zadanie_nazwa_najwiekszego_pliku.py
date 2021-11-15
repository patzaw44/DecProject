"""
Zadanie

Napisz program, który wyświetli nazwę największego pliku w tym katalogu.
"""
#  wylistować pliki i foldery z katalogu
#  przefiltrować, żeby zostały tylko pliki
#  pobrać rozmiar dla danego pliku
#  znaleźć najwiekszy rozmiar i odpowiadający mu plik
import os


def wylistuj_katalog():
    return os.listdir()


def przefiltruj_tylko_pliki(pliki_i_foldery):
    tylko_pliki = []
    for plik in pliki_i_foldery:
        if os.path.isfile(plik):
            tylko_pliki.append(plik)
    return tylko_pliki


def pobierz_rozmiar_pliku(sciezka_do_pliku):
    rozmiar = os.path.getsize(sciezka_do_pliku)
    return rozmiar


def znajdz_najwiekszy_plik(lista_plikow):
    najwiekszy_plik = {
        "nazwy": "",
        "rozmiar": 0
    }
    for plik in lista_plikow:
        rozmiar_pliku = pobierz_rozmiar_pliku(plik)
        obecnie_najwiekszy = najwiekszy_plik["rozmiar"]
        if rozmiar_pliku > obecnie_najwiekszy:
            najwiekszy_plik["nazwa"] = plik
            najwiekszy_plik["rozmiar"] = rozmiar_pliku
    return najwiekszy_plik


pliki_i_foldery = wylistuj_katalog()
print(pliki_i_foldery, len(pliki_i_foldery))
pliki = przefiltruj_tylko_pliki(pliki_i_foldery)
print(pliki, len(pliki))
# print(pobierz_rozmiar_pliku(pliki[0]), pliki[0])
print(znajdz_najwiekszy_plik(pliki))