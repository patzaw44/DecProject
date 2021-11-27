"""  “Smaczne.pl” - aplikacja konsolowa, która umożliwia zamówienie dania na dowóz z wybranej restauracji
(Patrycja + Jarosław)

wczytanie z pliku kilku restauracji wraz z ich lokalizacją i menu
zapytanie użytkownika o jego obecną lokalizację
wyliczenie kosztów dowozu dla każdej z restauracji (uzależnienie kosztu dowozu od odległości między klientem
 a restauracją)
wybór dań z menu i podsumowanie zamówienia """


from logo import logo, menu_obraz, zamowienie
from menu import restauracje
from menu_wybranej_restauracji import menu_wloska, menu_chinczyk, menu_hiszpanska

print(logo)
# wczytanie z pliku kilku restauracji wraz z ich lokalizacją i menu
# print(restauracje)


def wybor_restauracji(restauracja):
    # print(f"Wybrano restauracje: {restauracja}, której menu i lokalizacja to: {restauracje[restauracja]}.")
    print(f"WYBRANO RESTAURACJE: {restauracja}\n"
          f"LOKALIZACJA RESTAURACJI: {restauracje[restauracja]['lokalizacja']}\n")
    return restauracja


def wyswietl_lokalizacje_uzytkownika(lokalizacja_uzytkownik):
    lista_lokalizacji = []
    # for restauracja in restauracje:
    #    lista_lokalizacji.append(restauracja([0][0]))
    print(f"Twoja lokalizacja to: {lokalizacja_uzytkownik}.")
    return lokalizacja_uzytkownik


def wyliczenie_kosztow_dostawy(lokalizacja):
    if lokalizacja == restauracje[wybrana_restauracja]['lokalizacja']:
        dostawa = 0
    else:
        dostawa = 10
    print(f"Dostawa wynosi: {dostawa}zł.")
    return dostawa


def wyswietl_menu_restauracji(wybor_restauracji):
    print(menu_obraz)
    if wybrana_restauracja == 'Chinczyk':
        print(menu_chinczyk)
    elif wybrana_restauracja == 'Wloska':
        print(menu_wloska)
    elif wybrana_restauracja == 'Hiszpanska':
        print(menu_hiszpanska)


def lista_potraw(indeks):
    lista_zamowienia = []
    konkretne_menu = restauracje[wybrana_restauracja]['menu'][indeks]
    lista_zamowienia.append(konkretne_menu)
    # Stworzenie listy krotek:

    # print(restauracje[wybrana_restauracja]['menu'])

    while True:
        print("Aktualne zamówienie", lista_zamowienia)
        kontynuacja = input("Czy kontynuujesz zamówienie? Wpisz (T/N): ")
        if kontynuacja == 'N':
            break
        pozycja_w_menu = int(input("Wypisz nr potrawy z menu (od 0 do 3):"))
        konkretne_menu = restauracje[wybrana_restauracja]['menu'][pozycja_w_menu]
        lista_zamowienia.append(konkretne_menu)

    print(f"Końcowe zamówienie to {lista_zamowienia}")
    return lista_zamowienia


def podsumowanie_zamowienia(lista_zamowienia, koszt_dostawy):
    print(lista_zamowienia)
    koszty_zamowienia = []
    for k in lista_zamowienia:
        kwota = k[1]
        koszty_zamowienia.append(kwota)
    # print(koszty_zamowienia)

    koszty_zamowienia = sum(koszty_zamowienia)
    koszty_calkowite = koszty_zamowienia + koszt_dostawy
    print(f"Twoje całkowite koszty zamówienia + dostawa : {koszty_calkowite}. ")
    return koszty_calkowite


def zapis_do_pliku(koszty_calkowite, lista_zamowienia):
    with open("zamówienie.txt", mode="w", encoding="utf-8") as f:
        f.write(f"{zamowienie}\nKońcowe zamówienie to {lista_zamowienia}\nDo zapłaty za powyższe zamówienie:"
                f" {koszty_calkowite} zł.")


wybrana_restauracja = wybor_restauracji(input("Wybierz restauracje - Chinczyk, Wloska, Hiszanska:  ").title())
lokalizacja = wyswietl_lokalizacje_uzytkownika(input("Podaj swoją obecną lokalizację: ").title())
koszt_dostawy = wyliczenie_kosztow_dostawy(lokalizacja)
wyswietl_menu_restauracji(wybor_restauracji)
potrawa = lista_potraw(int(input("Wpisz nr potrawy z menu (od 0 do 3):")))
do_zapisu = podsumowanie_zamowienia(potrawa, koszt_dostawy)
zapis_do_pliku(do_zapisu, potrawa)



