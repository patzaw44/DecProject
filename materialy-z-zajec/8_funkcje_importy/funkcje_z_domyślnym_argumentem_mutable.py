def funkcja(moja_lista=[]):
    print(moja_lista)
    moja_lista.append("obiekt")
    print(moja_lista)


def lepsza_funkcja(moja_lista=None):
    if moja_lista is None:
        moja_lista = []
    print(moja_lista)
    moja_lista.append("obiekt")
    print(moja_lista)

funkcja([1, 2])
lepsza_funkcja()
lepsza_funkcja()
lepsza_funkcja()
# funkcja()
# funkcja()