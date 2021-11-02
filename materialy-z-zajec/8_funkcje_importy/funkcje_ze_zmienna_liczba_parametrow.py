import a as a


def dodaj(a,b):
    return a + b
def dodaj2(a, *liczby):
    print(a, liczby)
# * wszystkie kolejne liczby lecą do krotki

def dodaj3(liczba1, liczba2, *liczby):
    print(liczba1, liczba2, liczby)
    wynik = liczba1 + liczba2
    wynik = wynik + sum(liczby)
    # wynik += sum(liczby)
    return wynik

wynik = dodaj(1,2)
print(wynik)

# dodaj2()
# dodaj2(1)
# dodaj2(1, 3, 4, 5, 56, 11)

# dodaj3(100, 214, 556, 44, 78, 788, 44)
print(dodaj3(1, 2, 10, 20))

def nowa_funkcja(*parametry, **opcje):
    print(parametry, opcje)


#słownik -> dwie gwiazdki
nowa_funkcja(argument1 = "cokolwiek", argument2 = 3)
nowa_funkcja(1, 2, argument1 = "cokolwiek", argument2 = 3)

def nowa_funkcja(*args, **kwargs):
    print(args, kwargs)

# def funkcja_z_typem(a:str, b:str):
#     return a + b
#
# funkcja_z_typem(1, 2)