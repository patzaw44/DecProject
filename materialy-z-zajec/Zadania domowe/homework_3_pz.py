"""Napisz program, który pobiera od użytkownika tytuł ulubionej piosenki, a następnie

- wypisuje z ilu znaków się składa
- wypisuje ile razy występuje literka "a"
- wypisuje, czy w tytule występuje spacja
- wypisuje tytuł ze wstawionymi znakami specjalnymi (np. #, * lub -) pomiędzy każdy znak tytułu
np. "Let it be" -> "L-e-t- -i-t- -b-e"

- wypisuje tytuł z usuniętymi spacjami"""

title_song = input("Enter the title of your favorite song: ")

# długość znaków
print(len(title_song))

# ile razy występuje literka "a"
print(title_song.count("a"))

# wypisuje, czy w tytule występuje spacja
if title_song.find(' ') != -1:
    print("W tytule występuje spacja.")
else:
    print("W tytule nie występuje spacja.")

print(title_song.isspace())

# wypisuje tytuł ze wstawionymi znakami specjalnymi (np. #, * lub -) pomiędzy każdy znak tytułu
# print(title_song.split('-')