"""
Zadanie 14

Napisz program (używając funkcji), który przyjmuje od użytkownika napis składający się ze słów rozdzielonych myślnikiem,
 a następnie zwraca napis ze słowami posortowanymi alfabetycznie (również oddzielone myślnikami)

np. kot-pies-albatros-czapla-delfin --> albatros-czapla-delfin-kot-pies
"""

UZYTKOWNIK = input("Napisz cokolwiek: ").split(' ')
# uzytkownik = uzytkownik.split(' ')
# print(uzytkownik)


def tekst_uzytkownika():
    print('-'.join(UZYTKOWNIK))


def posortowany_tekst_uzytkownika():
    UZYTKOWNIK.sort()
    print('-'.join(UZYTKOWNIK))


tekst_uzytkownika()
posortowany_tekst_uzytkownika()

