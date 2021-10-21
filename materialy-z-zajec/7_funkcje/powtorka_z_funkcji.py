import random
def funkcja_z_domyslnym_returnem():
    print("Funkcja z domyślnym returnem")
    return None

def rzuc_kostka():
    print("No to losujemy: ")
    return 4 # rzucilismy kostką i tak wypadło
    # print("ciągne w funkcji")

funkcja_z_domyslnym_returnem()
wynik = rzuc_kostka()
print(wynik)

def rzuc_kostka_naprawde():
    wylosowana_liczba = random.randint(1, 6)
    # pass
szczesliwa_liczba = rzuc_kostka_naprawde()
print(szczesliwa_liczba)