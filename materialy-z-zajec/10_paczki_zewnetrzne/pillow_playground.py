import os
from PIL import Image


def stworz_miniaturke(nazwa_pliku):
    plik_wyjsciowy = os.path.splitext(nazwa_pliku)[0] + "-thumbnail.png"
    with Image.open(nazwa_pliku) as im:
        im.thumbnail((200, 200))
        im.save(plik_wyjsciowy, "PNG")


stworz_miniaturke("avatar.png")
