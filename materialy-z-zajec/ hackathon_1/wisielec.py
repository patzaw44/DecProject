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
  ? co się stanie jeżeli użytkownik wstawi tą samą literę


"""
import random

obrazy = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
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
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lista = ["pogopa", "chamura", "drezewa", "trawnika"]

zycia = 6
wynik = random.choice(lista)
print(wynik)

# wynik_lista = list(wynik)
podloga = (len(wynik)* "_ ")
print(podloga)


wykorzystane = []

podloga =[]
for litera in wynik:
    podloga+="_"


while zycia > 0:
    litera_uzytkownika = input("Podaj literę: ").lower()
    for indeks in range(len(wynik)-1):
        if wynik[indeks] == litera_uzytkownika:
            podloga[indeks] = wynik[indeks]
    print(' '.join(podloga))
    # litera_uzytkownika = input("Podaj literę: ").lower()

    if litera_uzytkownika not in wynik:
        print("Niestety, podaj kolejną literę")
        zycia -= 1
        if zycia == 0:
            print("Koniec gry.")
    print(obrazy[zycia])
