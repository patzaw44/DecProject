"""
Zadanie

Napisz program, który wylicza i informuje użytkownika o cenie jego wakacji:

    wybierz 3 dostępne lokalizacje

    dla każdej z tych lokalizacji ustal cenę za lot, cenę za wypożyczenie samochodu (dziennie) oraz
    cenę za nocleg (dziennie)

    zapytaj użytkownika o liczbę nocy, lokalizację oraz liczbę dni, którą zamierza spędzić na miejscu

    program powinien wypisać całkowitą sumę, którą użytkownik musi zapłacić wraz z poszczególnymi
    składowymi (np. lot kosztuje 500, samochód 400, nocleg 1500)

"""
lokalizacje = {
    "USA": {
        "lot": 1000,
        "nocleg": 200,
        "samochód": 80
    },
    "Niemcy": {
        "lot": 200,
        "nocleg": 300,
        "samochód": 90
    },
    "Japonia": {
        "lot": 1500,
        "nocleg": 250,
        "samochód": 120
    }
}


def pobierz_lokalizacje():
    while True:
        panstwo = input("Jaki cel podróży")
        if panstwo in lokalizacje:
            return panstwo


def pobierz_liczbe(wskazowka):
    while True:
        liczba = input(wskazowka)
        if liczba.isdigit():
            return int(liczba)


def oblicz_koszt_podrozy(panstwo, liczba_nocy, liczba_samochod):
    kosztorys = lokalizacje[panstwo]
    przelot = kosztorys["lot"] * 2
    nocleg = kosztorys["nocleg"] * liczba_nocy
    samochod = kosztorys["samochód"] * liczba_samochod
    return przelot + nocleg + samochod


panstwo = pobierz_lokalizacje()
liczba_nocy = pobierz_liczbe("Podaj liczbę nocy")
dni_samochod = pobierz_liczbe("Na ile dni chcesz samochód")

koszt = oblicz_koszt_podrozy(panstwo=panstwo, liczba_nocy=liczba_nocy, liczba_samochod=dni_samochod)
print(koszt)