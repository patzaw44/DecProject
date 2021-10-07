temperatura = 44

# powyzej 30 st->upał
# powyzej 20 st ->letnio
# miedzy 7-20-> jesiennie/wiosenno
# ponizej 7->zimowo

if temperatura > 30:
    print("Upał.")
elif temperatura > 20:
    print("Ubierz się letnio.")
elif 7 <= temperatura <= 20:
    print("Ubierz się jesiennie/wiosenno.")
else:
    print("Ubierz się zimowo.")

