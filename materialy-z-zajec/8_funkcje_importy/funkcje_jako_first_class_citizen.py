def moja_funkcja():
    print("Witam")

def inna_funkcja():
    print("Cześć")

lista_funkcji = [moja_funkcja, inna_funkcja]

for funkcja in lista_funkcji:
    print(funkcja())

nowa_funkcja = moja_funkcja

nowa_funkcja()

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

kalkulator = {
    "dodaj": dodaj,
    "odejmij": odejmij
}

operacja = input("co chcesz zrobić?")
dzialanie = kalkulator[operacja]