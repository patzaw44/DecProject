def pobierz_liczbe_goli(wynik):
    return (int(wynik[0]), int(wynik[2]))

print(pobierz_liczbe_goli("1:0"))
print(pobierz_liczbe_goli("2:2"))