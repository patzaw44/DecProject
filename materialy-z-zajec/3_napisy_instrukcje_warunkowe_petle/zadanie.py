"""Zadanie

Napisz program, który zapyta użytkownika o 3 słowa. Otrzymane słowa połącz w jeden napis i wyświetl
w następujących konfiguracjach:

   - slowo1slowo2slowo3
   - zamieniona kolejność: słowo3słowo1slowo2
    - każde z wielkiej litery: Słowo1Słowo2Słowo3
    każde ze słów bez dwóch pierwszych znaków oraz ostatniego znaku: owoowoowo
    co druga litera każdego ze słów: soosoosoo
"""

word_a = input("Napisz słowo nr 1: ")
word_b = input("Napisz słowo nr 2: ")
word_c = input("Napisz słowo nr 3: ")

print(word_a+word_b+word_c)
print(word_c+word_a+word_b)
print(word_a.title()+word_b.title()+word_c.title())

print(word_a[2:-1]*3)
print(word_b[2:-1]*3)
print(word_c[2:-1]*3)

print(word_a[::2]*3)
print(word_b[::2]*3)
print(word_b[::2]*3)