"""Zadanie

Stwórz klasę Prostokąt, która posiada atrybuty reprezentujące:

    długość prostokąta,
    szerokość prostokąta,
    jego współrzędne (x, y) na mapie (lewy górny róg).
    inicjalizator, który inicjalizuje wszystkie atrybuty. Współrzędne (x,y) mają wynosić (0,0) jeżeli ich się
    nie poda (wartości domyślne).

Stwórz 3 rózne prostokąty o różnych wymiarach oraz współrzędnych, wyświetl wszystkie 4 wartości oraz oblicz pole"""

class prostokat:


    def dane(self):
        self.dlugosc = int(input("Podaj długość boku prostokąta: "))
        self.szerokosc = int(input("Podaj szerokość boku prostokąta: "))

    def pole(self):
        self.pole= self.dlugosc*self