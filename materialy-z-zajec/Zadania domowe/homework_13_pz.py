"""
Zadanie 13

Wybierz tekst dwóch wybranych przez Ciebie piosenek. Napisz program, który:

    znajdzie słowa, które występują w obu piosenkach

    słowa unikalne dla obu piosenek
"""
song_one = """"start spreading the news
I am leaving today
I want to be a part of it
New York New York
these vagabond shoes
they are longing to stray
right through the very heart of it
New York New York
I want to wake up in a city
that never sleeps
and find I am king of the hill
top of the heap
these small town blues
they are melting away
I will make a brand new start of it
in old New York
if I can make it there
I will make it anywhere
it is up to you
New York New York
New York New York
I want to wake up in a city
that does not sleep
and find that I am number one
top of the list
head of the heap
king of the hill
these little town blues
they have all melted away
I am gonna make a brand new start of it
in old New York
and if I can make it there
I will make it practically anywhere
it is up to you
New York New York
New York"""

song_two = """that is life
that is what all the people say
you are riding high in April shot down in May
but I know I am gonna change that tune
when I am back on top back on top in June
I said that is life
and as funny as it may seem
some people get their kicks
stomping on a dream
but I do not let it let it get me down
cause this fine old world, it keeps spinning around
I have been a puppet a pauper a pirat a poet
a pawn and a king
I have been up and down and over and out
and I know one thing
each time I find myself
flat on my face
I pick myself up and get
back in the race
that is life
I tell you I can not deny it
I thought of quitting baby
but my heart just is not gonna buy it
and if I did not think it was worth one single try
I would jump right on a big bird and then I would fly
I have been a puppet a pauper a pirate a poet
a pawn and a king
I have been up and down and over and out
and I know one thing
each time I find myself laying
flat on my face
I just pick myself up and get
back in the race
that is life
that is life and I can not deny it
many times I thought of cutting out but my heart will not buy it
but if there is nothing shaking come this here July
I am gonna roll myself up
in a big ball and die
my my"""

# tworzenie listy poprzez rozdzielenie, tam gdzie jest spacja; rozdzielenie wyrazów poprzez dodanie/n;
# tworzenie listy poprzez rozdzielenie tam gdzie jest "\n"

song_one = '\n'.join(song_one.split(" ")).split("\n")
# song_one = song_one.split("\n")
song_two = '\n'.join(song_two.split(" ")).split("\n")
# print(song_two)

# tworzenie zbiorów:
song_ny = set(song_one)
song_life = set(song_two)

# print(song_ny)
# print(song_life)

# difference->różne elementy, union-> złączenie zbiorów
rozne_wyrazy = (song_ny.difference(song_life)).union(song_life.difference(song_ny))

ladniejsze_wyswietlenie = ', '.join(rozne_wyrazy)
print(f"Różne wyrazy : {ladniejsze_wyswietlenie}")
# print(rozne_wyrazy)

# intersection-> wspólne elementy zbiorów
wspolne_wyrazy = song_ny.intersection(song_life)
ladniejsze_wyswietlenie = ', '.join(wspolne_wyrazy)
print(f"Wspólne wyrazy : {ladniejsze_wyswietlenie}")
# print(wspolne_wyrazy)