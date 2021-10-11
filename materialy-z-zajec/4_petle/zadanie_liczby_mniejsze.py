"""Zadanie

Napisz program, który wypisuje liczby mniejsze od 100 które są parzyste i podzielne przez 5.

Wykonaj ćwiczenie dwukrotnie, raz z użyciem pętli for, raz z użyciem pętli while."""

#modulo !

for liczba in range(100):
    if liczba % 2 == 0 and liczba % 5 == 0:
        print( f"{liczba}")


liczba = 0
while liczba<100:
    if liczba % 2 == 0 and liczba % 5 == 0:
        print(liczba)
    liczba+=1

