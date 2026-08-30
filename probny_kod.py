from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    # Domyślne dane
    dane = {
        "grupa": "",
        "producent": "",
        "kompatybilnosc": "",
        "rodzaj": "",
        "kolor": "",
        "pochodzenie": "",
        "numer": "1"
    }

    kod = "Tu pojawi się kod"

    if request.method == "POST":

        # Pobieranie danych z formularza
        dane["grupa"] = request.form.get("grupa", "")
        dane["producent"] = request.form.get("producent", "")
        dane["kompatybilnosc"] = request.form.get(
            "kompatybilnosc",
            ""
        )
        dane["rodzaj"] = request.form.get("rodzaj", "")
        dane["kolor"] = request.form.get("kolor", "")
        dane["pochodzenie"] = request.form.get(
            "pochodzenie",
            ""
        )
        dane["numer"] = request.form.get(
            "numer",
            "1"
        )

        kodzik = ""

        # ==========================================
        # GRUPA
        # ==========================================

        if dane["grupa"] == "Materiały eksploatacyjne":
            kodzik += "ME"

        # ==========================================
        # PRODUCENT
        # ==========================================

        producenci = {
            "Hewlett Packard": "HP",
            "Brother": "BR",
            "Canon": "CA",
            "Epson": "EP"
        }

        kodzik += producenci.get(
            dane["producent"],
            ""
        )

        # ==========================================
        # KOMPATYBILNOŚĆ
        # ==========================================

        kodzik += producenci.get(
            dane["kompatybilnosc"],
            ""
        )

        # ==========================================
        # RODZAJ
        # ==========================================

        rodzaje = {
            "Tusz": "INK",
            "Toner": "TON",
            "Bębeb": "BB"
        }

        kodzik += rodzaje.get(
            dane["rodzaj"],
            ""
        )

        # ==========================================
        # KOLOR
        # ==========================================

        kolory = {
            "Czarny": "BK",
            "Niebieski": "C",
            "Różowy": "M",
            "Żółty": "Y",
            "Kolorowy": "CMY",
            "Zestaw": "CMYK"
        }

        kodzik += kolory.get(
            dane["kolor"],
            ""
        )

        # ==========================================
        # POCHODZENIE
        # ==========================================

        pochodzenie = {
            "Dystrybucja": "D",
            "Rynek": "R"
        }

        kodzik += pochodzenie.get(
            dane["pochodzenie"],
            ""
        )

        # ==========================================
        # NUMER
        # ==========================================

        try:

            numer = int(dane["numer"])

            # Numer zostaje dodany do kodu
            kodzik += str(numer)

            # Następny numer
            dane["numer"] = str(numer + 1)

        except ValueError:

            kodzik = "Wpisz poprawny numer!"

        kod = kodzik

    return render_template(
        "index.html",
        kod=kod,
        dane=dane
    )


if __name__ == "__main__":
    app.run(debug=True)
