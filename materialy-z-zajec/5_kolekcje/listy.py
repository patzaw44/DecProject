# zachowana kolejność, mutowalne
# środek listy elementy

moja_lista = [10, 12, 13, 14]
lista_napisow = ["1,2,3", "kolejny napis"]
roznorodna_lista = [1, "aa", 2.0, True, 2]
print(moja_lista)
print(len(moja_lista))
print(len(lista_napisow))
print(len(roznorodna_lista))

#dodać element do listy:
print(moja_lista)
moja_lista.append(17) #moja_lista = moja_lista.append(10) nie wolno tak robić !! wyjdzie NONE i wyczyszczenie listy!!
print(moja_lista)

#w napisach jest inaczej:
napis = "abc"
print(napis)
napis.upper() # aby drugi print wyszedł inny powinno być: napis = napis.upper()
print(napis)

print(moja_lista[-1])

l = list("Patrycja")
print(l)
l[0]="t"
print(l)
napis = " ".join(l)
print(napis)

