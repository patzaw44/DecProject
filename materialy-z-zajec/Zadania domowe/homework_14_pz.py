"""
Zadanie 14

Napisz program (używając funkcji), który przyjmuje od użytkownika napis składający się ze słów rozdzielonych myślnikiem,
 a następnie zwraca napis ze słowami posortowanymi alfabetycznie (również oddzielone myślnikami)

np. kot-pies-albatros-czapla-delfin --> albatros-czapla-delfin-kot-pies
"""


def posortowany_tekst_uzytkownika(uzytkownik):
    print('-'.join(uzytkownik))
    uzytkownik.sort()
    print('-'.join(uzytkownik))


posortowany_tekst_uzytkownika(uzytkownik=input("Napisz cokolwiek: ").split(' '))
