"""Zadanie

Napisz program, który pyta użytkownika o wiek oraz stan konta i sprawdza, czy może on wejść na przedstawienie.
Zakładamy, że bilet na przedstawienie kosztuje 50 zł i jest ono dostępne od 16 lat."""

wiek = int(input("Podaj wiek: "))
stan_konta = float(input("Podaj stan konta: "))

if wiek >= 16 and stan_konta >= 50:
    print("Użytkownik może wejść na przedstawienie.")

else:
    print("Użytkownik nie może wejść na przedstawienie.")

