tekst="""Wlazl kotek na płotek
imruga, ladna to piosenka ..."""

odpowiedz = input("Podaj słowo: ")

print(odpowiedz.lower() in tekst.lower())
print(odpowiedz.upper() in tekst.upper())

plik = "plik.mp3"
print(tekst[::-1])
print(plik.endswith((".mp3")))