"""Zadanie

Napisz program, który:

    przypisze do zmiennej cenę za litr paliwa

    przypisze do zmiennej średnie spalanie na 100 km

    następnie zapyta użytkownika o cenę, którą jest w stanie zapłacić oraz długość trasy w km, jaką chce pokonać

Program powinien wypisać komunikat z decyzją czy uda się przejechać podaną trasę po zatankowaniu auta za przytoczoną
kwotę."""


cena_paliwa = float(input("Wpisz cenę za litr paliwa: "))
srednie_spalanie = float(input("Wpisz średnie spalanie na 100 km: "))

cena_uzytkownika = float(
    input("Wpisz cenę, którą jesteś w stanie zapłacić za paliwo: "))
dlugosc_trasy = float(input("Wpisz długość trasy w km, jaką chcesz pokonać: "))

# KOSZT PALIWA = (DYSTANS / 100) * CENA PALIWA * ŚREDNIE SPALANIE
koszt = (dlugosc_trasy / 100) * cena_paliwa * srednie_spalanie

print(f"Koszt paliwa: {koszt:.2f}zł")
if cena_uzytkownika >= koszt:
    print(
        "Uda Ci się przejechać podaną trasę po zatankowaniu auta za przytoczoną kwotę!"
    )
else:
    print("Nie uda się!")

