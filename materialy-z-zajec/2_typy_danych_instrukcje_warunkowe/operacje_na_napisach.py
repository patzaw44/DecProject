odpowiedz=input("Podaj swoje imie: ")
print(f"Twoja odpowiedz to: {odpowiedz.title()}.")

print(f"Dlugosc imienia to {len(odpowiedz)}")
print(odpowiedz[-1])
print(f"Dlugosc imienia to {len(odpowiedz)-1}")
print(f"Dlugosc imienia to {odpowiedz[len(odpowiedz)-1]}")
#zakresy:
print(f"{odpowiedz[:4]}")
print(f"{odpowiedz[0:4]}")
print(f"{odpowiedz[:]}")

print(f"{odpowiedz[::2]}")# pobierz co drugą literę