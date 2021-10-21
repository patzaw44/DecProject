def opisz_prostokat(a, b, c, d):
    print(f" a=> {a}, b=> {b}, c=> {c}, d=> {d} ")

opisz_prostokat(1, 2, 3, 4)
opisz_prostokat(a=1, b=2, c=3, d=4)
# można mieszać, jeżeli jest przypisane do zmiennej:
opisz_prostokat(d=4, c=3, a=1, b=2)
