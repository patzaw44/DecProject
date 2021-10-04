#odpowiedz = input("Podaj swoje imie: ")

#print(f"Twoja odpowiedz to: {odpowiedz.title()}.")


import datetime
obecna_data= datetime.date.today()
obecny_rok = obecna_data.year

# obecny_rok = 2021
#1 sposob:
# wiek = input("Podaj swoj wiek:")
# wiek = int(wiek)
#2 sposob:
wiek = int(input("Podaj swoj wiek:"))
rok_urodzenia = obecny_rok - wiek
print(f"Twoja data urodzenia to : {rok_urodzenia}.")