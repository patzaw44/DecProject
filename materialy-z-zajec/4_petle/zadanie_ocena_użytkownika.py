"""Zadanie

Napisz program, który zapyta użytkownika o ocenę filmu w skali 1-10.

    w przypadku podania oceny, która wykracza za skalę (poniżej 1 lub powyżej 10), program powinien kontynuować pytanie,
     dopóki nie otrzyma poprawnej oceny po wprowadzeniu poprawnej oceny, program powinien wyświetlić komentarz
     odpowiadający ocenie:

1-3 -> "strata czasu"

4-6 -> "można obejrzeć na własną odpowiedzialność"

7-8 -> "zdecydowanie warty uwagi"

9-10 -> "genialny"""

ocena = int(input("Podaj ocenę filmu w sklai 1 do 10: "))

while not 1 <= ocena or ocena >= 10:
    ocena = int(input("Podaj ocenę filmu w sklai 1 do 10: "))
    if ocena <= 3:
        print("strata czasu")
    elif ocena <= 6:
        print("można obejrzeć na własną odpowiedzialność")
    elif ocena <= 8:
        print("zdecydowanie warty uwagi")
    elif ocena <=10:
        print("genialny")
