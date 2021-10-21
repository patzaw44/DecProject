def usuwanie_znakow(napis, niechciane_znaki ="?!-.,"):
    for znak in niechciane_znaki:
        napis = napis.replace(znak, "")
    return napis
zmodyfikowany_napis = usuwanie_znakow("Ala ma kota??!!!", "?!")
print(zmodyfikowany_napis)
kolejny_napis = usuwanie_znakow("!!!! Ala ma kota ?? ... ala  ...")
print(kolejny_napis)
jeszcze_jeden_napis = usuwanie_znakow("Ala ma kota!", "a")
print(jeszcze_jeden_napis)