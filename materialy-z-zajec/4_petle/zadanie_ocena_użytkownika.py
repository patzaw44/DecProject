"""Zadanie

Napisz program, który zapyta użytkownika o ocenę filmu w skali 1-10.

    w przypadku podania oceny, która wykracza za skalę (poniżej 1 lub powyżej 10), program powinien kontynuować pytanie,
     dopóki nie otrzyma poprawnej oceny po wprowadzeniu poprawnej oceny, program powinien wyświetlić komentarz
     odpowiadający ocenie:

1-3 -> "strata czasu"

4-6 -> "można obejrzeć na własną odpowiedzialność"

7-8 -> "zdecydowanie warty uwagi"

9-10 -> "genialny"""

# ocena = int(input("Podaj ocenę filmu w sklai 1 do 10: "))
while True:
    ocena_filmu = int(input("Podaj ocenę filmu w sklai 1 do 10: "))
    if ocena_filmu < 1 or ocena_filmu > 10:
        print ("nieprawidłowa ocena")
    else:
        break
print(ocena_filmu)


    # ocena = int(input("Podaj ocenę filmu w sklai 1 do 10: "))
if 1 <= ocena_filmu <= 3:
        print("strata czasu")
elif 4 <= ocena_filmu <= 6:
        print("można obejrzeć na własną odpowiedzialność")
elif 7 <= ocena_filmu <= 8:
        print("zdecydowanie warty uwagi")
elif 9 <= ocena_filmu <=10:
        print("genialny")

