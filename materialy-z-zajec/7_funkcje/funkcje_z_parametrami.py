def oblicz_cene_brutto(cena_netto):
    cena_brutto = cena_netto * 1.23
    # return cena_brutto
    return cena_netto * 1.23

def oblicz_cene_brutto_v2(cena_netto, stawka_vat):
    return cena_netto * (1 + stawka_vat)


def oblicz_cene_brutto_v3(cena_netto, kategoria):
    if kategoria == "usługi":
        vat = 0.08
    else:
        vay = 0.23
    return cena_netto * (1 + vat)

cena = int(input("Podaj cenę netto: "))
cena_brutto = oblicz_cene_brutto(cena)
print(cena_brutto)

