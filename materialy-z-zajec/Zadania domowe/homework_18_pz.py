"""
Zadanie 18
Napisz funkcję, która przyjmie jako argument historię transakcji i na tej podstawie obliczy aktualne saldo konta.

Wariant prostszy (transakcje jako lista liczb):

transakcje = [1000, -400, 200, 1500, -500] # itp.
Wariant bardziej zaawansowany (transakcje jako lista krotek):

# D - deposit - wpłata na konto
# W - withdrawal - wypłata z konta
transakcje = [(D, 1000), (W, 400), (D, 200), (D, 1500), (W, 500)]"""


def obl_salda_lista(transakcje):
    aktualne_saldo = sum(transakcje)
    print(f"Twoje aktualne saldo: {aktualne_saldo} zł.")


obl_salda_lista(transakcje=[1000, -400, 200, 1500, -500])


def obl_salda_krotka():
    transakcje = [('D', 1000), ('W', 400), ('D', 200), ('D', 1500), ('W', 500)]
    wyplata = []
    wplata = []
    transakcje_lista = list(sum(transakcje, ()))

    # print(transakcje_lista)

    for t in str(transakcje_lista):
        # Stworzenie dwoch list, tylko z liczbami: wplaty i wyplaty
        if "W" in t:
            wyplata=[(transakcje_lista[transakcje_lista.index(t)+1])]
            wyplata.append(t)

        if "D" == t:
            wplata = [(transakcje_lista[transakcje_lista.index(t)+1])]
            wplata.append(t)

    print(wyplata)
    print(wplata)

    # aktualne_saldo = sum(wplata)-sum(wyplata)
    # print(aktualne_saldo)


obl_salda_krotka()


# 2 pomysl :z krotki-> slownik, w slowniku powstają dwie listy D i W.... saldo = D-W

