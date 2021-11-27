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


class Zamowienie:
    def __init__(self):
        self.restauracja = input("Wybierz restauracje - Chinczyk, Wloska, Hiszanska:  ").title()
        self.lokalizacja = input("Podaj swoją obecną lokalizację: ").title()
        self.potrawa = int(input("Wypisz nr potrawy z menu (od 0 do 3):"))
        self.koszt_dostawy = 0

    def wybor_restauracji(self):
        wybrana_restauracja = self.restauracja
        # print(f"Wybrano restauracje: {restauracja}, której menu i lokalizacja to: {restauracje[restauracja]}.")
        print(f"WYBRANO RESTAURACJE: {wybrana_restauracja}\n"
              f"LOKALIZACJA RESTAURACJI: {restauracje[wybrana_restauracja]['lokalizacja']}\n")
        return wybrana_restauracja


    def wyswietl_lokalizacje_uzytkownika(self):
        lokalizacja_uzytkownik = self.lokalizacja
        lista_lokalizacji = []
        # for restauracja in restauracje:
        #    lista_lokalizacji.append(restauracja([0][0]))
        print(f"Twoja lokalizacja to: {lokalizacja_uzytkownik}.")
        return lokalizacja_uzytkownik

    def wyliczenie_kosztow_dostawy(self):
        if self.lokalizacja == restauracje[self.restauracja]['lokalizacja']:
            dostawa = 0
        else:
            dostawa = 10
        self.dostawa = dostawa
        print(f"Dostawa wynosi: {dostawa}zł.")


    def wyswietl_menu_restauracji(self):
        print(menu_obraz)
        if self.restauracja == 'Chinczyk':
            print(menu_chinczyk)
        elif self.restauracja == 'Wloska':
            print(menu_wloska)
        elif self.restauracja == 'Hiszpanska':
            print(menu_hiszpanska)


    def lista_potraw(self):
        lista_zamowienia = []
        konkretne_menu = restauracje[self.restauracja]['menu'][self.potrawa]
        lista_zamowienia.append(konkretne_menu)
        # Stworzenie listy krotek:

        # print(restauracje[wybrana_restauracja]['menu'])

        while True:
            print("Aktualne zamówienie", lista_zamowienia)
            kontynuacja = input("Czy kontynuujesz zamówienie? Wpisz (T/N): ")
            if kontynuacja == 'N':
                break
            pozycja_w_menu = int(input("Wypisz nr potrawy z menu (od 0 do 3):"))
            konkretne_menu = restauracje[self.restauracja]['menu'][pozycja_w_menu]
            lista_zamowienia.append(konkretne_menu)

        print(f"Końcowe zamówienie to {lista_zamowienia}")
        self.lista_zamowienia = lista_zamowienia


    def podsumowanie_zamowienia(self):
        print(self.lista_zamowienia)
        koszty_zamowienia = []
        for k in self.lista_zamowienia:
            kwota = k[1]
            koszty_zamowienia.append(kwota)
        # print(koszty_zamowienia)

        koszty_zamowienia = sum(koszty_zamowienia)
        koszty_calkowite = koszty_zamowienia + self.dostawa
        print(f"Twoje całkowite koszty zamówienia + dostawa : {koszty_calkowite}. ")
        self.koszty_calkowite = koszty_calkowite

    def zapis_do_pliku(self):
        with open("zamówienie.txt", mode="w", encoding="utf-8") as f:
            f.write(f"{zamowienie}\nKońcowe zamówienie to {self.lista_zamowienia}\nDo zapłaty za powyższe zamówienie:"
                    f" {self.koszty_calkowite} zł.")


zamowienie1 = Zamowienie()
wybrana_restauracja = zamowienie1.wybor_restauracji()
lokalizacja = zamowienie1.wyswietl_lokalizacje_uzytkownika()
zamowienie1.wyswietl_menu_restauracji()
koszt_dostawy = zamowienie1.wyliczenie_kosztow_dostawy()

potrawa = zamowienie1.lista_potraw()
zamowienie1.podsumowanie_zamowienia()
zamowienie1.zapis_do_pliku()



