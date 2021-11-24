"""
Zadanie 20

Napisz funkcję, która akceptuje dowolną liczbę nazw plików i zwraca listę zawierającą tylko nazwy plików muzycznych.
Dla uproszczenia można wybrać kilka formatów i przyjąć, że tylko one są traktowane jako pliki muzyczne.

Jeśli ktoś nie przekaże jako parametr żadnej nazwy pliku, funkcja powinna zwrócić pustą listę

przefiltruj_pliki_muzyczne() => []
przefiltruj_pliki_muzyczne("zdjecie.jpg", "plik.mp3", "piosenka.wav", "program.exe") => ["plik.mp3", "piosenka.wav"]

"""


def przefiltruj_pliki_muzyczne(lista_plikow):

    try:
        filtered = []
        for t in lista_plikow:
            if '.mp3' in t or '.wav' in t:
                filtered.append(t)
        print(f"Przefiltrowane pliki muzyczne to: {filtered}.")
    except NameError:
        print("[]")


przefiltruj_pliki_muzyczne(('zdjecie.jpg', 'plik.mp3', 'piosenka.wav', 'program.exe'))
