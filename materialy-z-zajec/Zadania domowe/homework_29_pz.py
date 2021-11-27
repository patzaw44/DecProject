"""
Zadanie 29

Napisz program, który zapyta użytkownika o nazwę pliku, którego zawartość ma zostać wyświetlona.
W przypadku podania nazwy nieistniejącego pliku program powinien wyświetlić stosowny komunikat i
ponowić pytanie o nazwę pliku
"""

def pobierz_nazwe_pliku(nazwa):
    if nazwa:
        with open(nazwa, encoding='UTF-8') as f:
            print("Plik istnieje.")

    else:
        print(f"Plik {nazwa} nie istnieje. Spróbuj ponownie!")


pobierz_nazwe_pliku(input("Podaj nazwę pliku: "))
