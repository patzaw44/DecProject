"""Zadanie
Pozwól użytkownikowi na wprowadzenie napisu. Następnie wyświetl pozycję każdej literki w tym napisie. Przykładowo, dla
napisu Ala ma kota,

0=>A
1=>l
2=>a
3=>
4=>m
5=>a"""

napis= input("Wprowadź napis: ")

for indeks in range(len(napis)):
    print(f"{indeks} -> {napis[indeks]}")

# for indeks in napis:
#     print(indeks)