"""
Zadanie 15

Napisz program, który zapyta użytkownika o jakieś zdanie, a następnie policzy i wypisze liczbę małych
 i dużych liter w tym zdaniu.
 """
# uzytkownik = input("Napisz jakieś zdanie: ")
# uzytkownik = uzytkownik.split(' ')
# bez_spacji = ''.join(uzytkownik)


def obliczanie_liter(uzytkownik):
    # print(uzytkownik)
    liczba_liter = {}
    for litera in uzytkownik:
        liczba_liter.setdefault(litera, 0)
        liczba_liter[litera] = liczba_liter[litera]+1
    print(liczba_liter)


obliczanie_liter(uzytkownik=''.join((input("Napisz jakieś zdanie: ")).split(' ')))
