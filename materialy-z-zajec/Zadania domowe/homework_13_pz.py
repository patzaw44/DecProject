"""
Zadanie 13

Wybierz tekst dwóch wybranych przez Ciebie piosenek. Napisz program, który:

    znajdzie słowa, które występują w obu piosenkach

    słowa unikalne dla obu piosenek
"""
song_one = """" Start spreading the news
I am leaving today
I want to be a part of it
New York, New York
These vagabond shoes
They are longing to stray
Right through the very heart of it
New York, New York
I want to wake up in a city
That never sleeps
And find I am king of the hill
Top of the heap
These small town blues
They are melting away
I will make a brand new start of it
In old New York
If I can make it there
I will make it anywhere
It is up to you
New York, New York
New York, New York
I want to wake up in a city
That does not sleep
And find that I am number one
Top of the list
Head of the heap
King of the hill
These little town blues
They have all melted away
I am gonna make a brand new start of it
In old New York
And
If I can make it there
I will make it practically anywhere
It is up to you
New York, New York
New York"""

song_two = """That is life
That is what all the people say
You are riding high in April, shot down in May
But I know I am gonna change that tune
When I am back on top, back on top in June
I said that is life
And as funny as it may seem
Some people get their kicks
Stomping on a dream
But I do not let it, let it get me down
Cause this fine old world, it keeps spinning around
I have been a puppet, a pauper, a pirate, a poet
A pawn and a king
I have been up and down and over and out
And I know one thing
Each time I find myself
Flat on my face
I pick myself up and get
Back in the race
That is life
I tell you, I can not deny it
I thought of quitting, baby
But my heart just is not gonna buy it
And if I did not think it was worth one single try
I would jump right on a big bird and then I would fly
I have been a puppet, a pauper, a pirate, a poet
A pawn and a king
I've been up and down and over and out
And I know one thing
Each time I find myself laying
Flat on my face
I just pick myself up and get
Back in the race
That is life
That is life and I can not deny it
Many times I thought of cutting out but my heart will not buy it
But if there is nothing shaking come this here July
I am gonna roll myself up
In a big ball and die
My, my """


list_user = uzytkownik.split(" ")

print(list_user)
liczba_liter = {}
for litera in list_user:
    liczba_liter.setdefault(litera,0)
    liczba_liter[litera] = liczba_liter[litera]+1
print(liczba_liter )