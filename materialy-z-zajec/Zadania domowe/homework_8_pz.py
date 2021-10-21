"""Zadanie 8

Napisz program, który zapyta użytkownika o 10 liczb, a następnie obliczy ich:

   - sumę

   - średnią
"""

liczby = input("Podaj 10 liczb po spacji: ")

# split a string into a list where each word is a list item
liczby = [float(i) for i in liczby.split()]
print(liczby)
print(f"Suma wynosi: {sum(liczby)}")
print('Średnia wynosi: '+"{:.1f}".format(sum(liczby) / len(liczby)))
