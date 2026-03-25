from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/kotki/<ile1>/<kolor1>")
def kotki(ile1, kolor1):
    ile1 = int(ile1)

    if ile1 < 20:
        tekst = "<p>Widzę że lubisz kotki i masz ich " + str(ile1) + "</p>"
    else:
        tekst = "<p>Widzę że lubisz kotki i masz ich tak dużo!!!</p>"
    if kolor1 == "czarny":
        tekst += "<p>Masz czarnego kotka! W nocy musi być straszny!</p>"
    elif kolor1 == "bialy":
        tekst += "<p>Masz białego kotka :O!</p>"
    elif kolor1 == "zielony":
        tekst += "<p>Zielony?!?!? Ale że zielony KOT!!!</p>"
    elif kolor1 == "szary":
        tekst += "<p>WoW! Szary koteczek!!</p>"
    elif kolor1 == "brazowy":
        tekst += "<p>Mój koteczek też jest brązowo-czarny!</p>"
    else:
        tekst += "<p>Rzadki kolor kotka, albo jestem zbyt leniwy by dodać elify :( Albo użyłeś polskiego Znaku!</p>"

    return tekst


@app.route("/pieski/<ile>/<kolor>")
def pieski(ile, kolor):
    ile = int(ile)

    if ile < 20:
        tekst = "<p>Widzę że lubisz pieski i masz ich " + str(ile) + "</p>"
    else:
        tekst = "<p>Widzę że lubisz pieski i masz ich tak dużo!!!</p>"

    if kolor == "czarny":
        tekst += "<p>Masz czarnego psa! Trudno go dostrzec!</p>"
    elif kolor == "bialy":
        tekst += "<p>Masz białego pieska :O! Mój też jest biały!!</p>"
    elif kolor == "zielony":
        tekst += "<p>Zielony?!?!? Ale że zielony pies!!! W trawie się wytarzał?</p>"
    elif kolor == "szary":
        tekst += "<p>WoW! Szary piesio!!</p>"
    elif kolor == "brazowy":
        tekst += "<p>MEEGAAA fajny piesek!</p>"
    else:
        tekst += "<p>Rzadki kolor psa, albo jestem zbyt leniwy by dodać elify :( Albo użyłeś polskiego Znaku!</p>"

    return tekst
if __name__ == "__main__":
    app.run(debug=True)