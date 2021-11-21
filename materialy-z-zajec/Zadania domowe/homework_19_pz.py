"""zadanie 19
Napisz program (z użyciem funkcji), który
przyjmuje od użytkownika 3 liczby: dolny zakres, górny zakres oraz ilość liczb
następnie losuje zadaną ilość liczb z podanego przedziału

Przykład: Użytkownik podaje liczby 1, 20, 5 -> program ma wylosować 5 liczb z zakresu 1-20 (włącznie)"""
import random


def losowanie(dolny_zakres, gorny_zakres, ilosc):
    for i in range(ilosc):
        print(random.randint(dolny_zakres, gorny_zakres))


losowanie(dolny_zakres=int(input(f"Podaj liczbę min: ")),
          gorny_zakres=int(input(f"Podaj liczbę max: ")),
          ilosc=int(input(f"Podaj liczbę losowanych liczb: ")))
