import random

from faker import Faker
from flask import Flask

app = Flask(__name__)

fake = Faker()


@app.route("/")
def hello_world():
    return f"<marquee>Witamy, cześć, {fake.first_name()}</marquee>"


@app.route("/inna")
def another():
    return "No cześć"

@app.route("/lotto")
def wygeneruj_liczby():
    liczby = []
    for i in range(6):
        wylosowana_liczba = random.randint(1, 49)
        while wylosowana_liczba in liczby:
            wylosowana_liczba = random.randint(1, 49)
        liczby.append(wylosowana_liczba)
    return str(sorted(liczby))


app.run()