"""Zadanie 8

Napisz program, który zapyta użytkownika o 10 liczb, a następnie obliczy ich:

   - sumę

   - średnią
"""

liczby = input("Podaj 10 liczb: ")
special_sign = [","]
for i in liczby:
    if i in special_sign:
        liczby = liczby.replace(i, "")
# print(liczby)

liczby = list(liczby)
print(liczby)

# suma = sum(liczby)
# print(suma)