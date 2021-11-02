def podziel_po_dwukropku(wynik):
    lista_z_golami = wynik.split(":")
    return lista_z_golami


def pobierz_liczbe_goli(wynik):
    lista_z_golami = podziel_po_dwukropku(wynik)
    # krotka_z_golami = tuple(lista_z_golami)
    krotka_z_golami = (int(lista_z_golami[0]), int(lista_z_golami[1]))
    return krotka_z_golami


def glowna_funkcja():
    print("Uruchomiłeś skrypt / jako program / bezpośrednio / nie-import")
    wynik = input("Podaj wynik")
    print(pobierz_liczbe_goli(wynik))
    print(pobierz_liczbe_goli("1:11"))
    print(pobierz_liczbe_goli("2:2"))


print(__name__)
wykonuje_jako_plik = __name__ == '__main__'
if wykonuje_jako_plik:
    glowna_funkcja()
