"""  “Smaczne.pl” - aplikacja konsolowa, która umożliwia zamówienie dania na dowóz z wybranej restauracji
(Patrycja + Jarosław)

wczytanie z pliku kilku restauracji wraz z ich lokalizacją i menu
zapytanie użytkownika o jego obecną lokalizację
wyliczenie kosztów dowozu dla każdej z restauracji (uzależnienie kosztu dowozu od odległości między klientem
 a restauracją)
wybór dań z menu i podsumowanie zamówienia """


from logo import logo
from menu import restauracje

print(logo)
# wczytanie z pliku kilku restauracji wraz z ich lokalizacją i menu
# print(restauracje)

def wybor_restauracji(restauracja):
    # print(f"Wybrano restauracje: {restauracja}, której menu i lokalizacja to: {restauracje[restauracja]}.")
    print(f"Wybrano restauracje: {restauracja}\n"
          f"LOKALIZACJA: {restauracje['Wloska']['lokalizacja']}\n"
          f"MENU (potrawa - cena): {restauracje['Wloska']['menu']}")
    return restauracja


def wyswietl_lokalizacje_uzytkownika(lokalizacja_uzytkownik):
    lista_lokalizacji = []
    # for restauracja in restauracje:
    #    lista_lokalizacji.append(restauracja([0][0]))
    print(f"Twoja lokalizacja to: {lokalizacja_uzytkownik}.")
    return lokalizacja_uzytkownik

def wyliczenie_kosztow_dostawy(lokalizacja):
    if lokalizacja == 'Gdansk':
        if restauracje['lokalizacja'] == 'Gdansk':
            dostawa = 0
        if restauracje['lokalizacja'] == 'Gdynia':
            dostawa = 5
        if restauracje['lokalizacja']=='Rumia':
            dostawa = 15
    return dostawa

# def zamowienie():
#     restauracja = 'Wloska'
#     if restauracja == restauracje[restauracja]:
#         rachunek = []
#         for rachunek in transakcje:
#             typ_transakcji = transakcja[0]
#             kwota = transakcja[1]
#             if typ_transakcji == "W":
#                 wyplata.append(kwota)
#             elif typ_transakcji == "D":
#                 wplata.append(kwota)



wybrana_restauracja = wybor_restauracji(input("Wybierz restauracje - Chinczyk, Wloska, Hiszanska:  ").title())
lokalizacja = wyswietl_lokalizacje_uzytkownika(input("Podaj swoją obecną lokalizację: ").title())
koszt_dostawy = wyliczenie_kosztow_dostawy(lokalizacja)
print()