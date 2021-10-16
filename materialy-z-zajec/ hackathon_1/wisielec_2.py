"""
1 - stworzyć listę
2 - losowo wylosować wyraz z listy
3 - input: uzytkownik odgaduje literę
4- wyswietlenie wyrazu z "podłogą" np. _ _ _ _
5- sprawdzenie czy dana litera jest w wylosowanym słowie np, s
6- ponowne wyswietlenie wyrazu z "podłogą" np. _ s _ _ -> podstawianie litery do odpowiedniego indeksu
7- ponowne zapytanie uzytkownika o litere - petla
8- jezeli nie ma "podłogi" uzytkownik wygrał

  ? wyswietlenie grafiki
"""
import random

fajerwerki = """

                                 .''.
       .''.             *''*    :_\/_:     .
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
obrazy = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Witamy w grze wisielec!")

lista = ["pogoda", "chmura", "drzewa", "trawnik"]

zycia = 7
wynik = random.choice(lista)
# print(wynik)

podloga = (len(wynik) * "_ ")
print(podloga)
wykorzystane = []

podloga = []
for litera in wynik:
    podloga += "_"


while zycia > 0:
    litera_uzytkownika = input("Podaj literę: ").lower()
    for indeks in range(len(wynik)):
        if wynik[indeks] == litera_uzytkownika:
            podloga[indeks] = wynik[indeks]
    print(' '.join(podloga))

    if litera_uzytkownika not in wynik:
        print("Niestety, podaj kolejną literę")
        zycia -= 1
        if zycia == 0:
            print("Przegrałeś, koniec gry.")
        print(obrazy[zycia])

    if podloga.count("_") == 0:
        print("Wygrałeś!")
        print(fajerwerki)
        break
    wykorzystane.append(litera_uzytkownika)
    proby = len(wykorzystane)
    print(f"Na razie wykorzystałeś następujące litery: {wykorzystane}.")
    print(f"Liczba prób: {proby}")