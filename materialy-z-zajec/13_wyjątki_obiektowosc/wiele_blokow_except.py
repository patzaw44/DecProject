liczby= input("Podaj 3 liczby rozdzielone przecinkiem:")

lista_liczb = liczby.split(",")

try:
    print(f"Trzecia liczba to {lista_liczb[2]}")
except IndexError:
    print("Podałeś za mało liczb!")

