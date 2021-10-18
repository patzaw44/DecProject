'''Zadanie

Wcielamy się w rolę wykładowcy, który dostał dwie listy: listę osób na roku oraz listę osób,
który podpisały swoją obecność na wykładzie.

uczniowie_na_roku = ["Mateusz", "Jan", "Ania", "Kasia", "Ola", "Jacek", "Rafał", "Karolina"]
uczniowie_na_wykladzie = ['Rafał', 'Jacek', 'Ola', 'Jan', 'Karolina', 'Kasia']

Napisz program, który znajdzie osoby nieobecne'''
uczniowie_na_roku = ["Mateusz", "Jan", "Ania", "Kasia", "Ola", "Jacek", "Rafał", "Karolina"]
uczniowie_na_wykladzie = ['Rafał', 'Jacek', 'Ola', 'Jan', 'Karolina', 'Kasia']


print(uczniowie_na_roku)
zbior_ucz_roku = set(uczniowie_na_roku)
zbior_ucz_wyk = set(uczniowie_na_wykladzie)

brakujacy_uczniowie = zbior_ucz_roku.difference(uczniowie_na_wykladzie)
print(f"Opuscili zajecia: {brakujacy_uczniowie}.")
