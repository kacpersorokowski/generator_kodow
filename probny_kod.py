from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)


# ============================================================
# PLIK DO PRZECHOWYWANIA NUMERU INDEKSOWEGO
# ============================================================

PLIK_NUMERU = "numer_indeksowy.json"


def wczytaj_numer():
    """
    Wczytuje ostatni zapisany numer.
    Jeśli plik nie istnieje, zaczynamy od 1.
    """

    if not os.path.exists(PLIK_NUMERU):
        return 1

    try:

        with open(PLIK_NUMERU, "r", encoding="utf-8") as plik:

            dane = json.load(plik)

            return int(dane.get("numer", 1))

    except (ValueError, TypeError, json.JSONDecodeError):

        return 1


def zapisz_numer(numer):
    """
    Zapisuje następny numer do pliku.
    """

    with open(
        PLIK_NUMERU,
        "w",
        encoding="utf-8"
    ) as plik:

        json.dump(
            {"numer": numer},
            plik,
            ensure_ascii=False,
            indent=4
        )


# ============================================================
# STRONA GŁÓWNA
# ============================================================

@app.route("/", methods=["GET", "POST"])
def index():

    kod = "Tu pojawi się kod"


    # Aktualny numer pobieramy z pliku
    aktualny_numer = wczytaj_numer()


    dane = {

        "grupa": "",

        "producent": "",

        "kompatybilnosc": "",

        "rodzaj": "",

        "kolor": "",

        "pochodzenie": "",

        "numer": str(aktualny_numer)

    }


    # ========================================================
    # GENEROWANIE KODU
    # ========================================================

    if request.method == "POST":


        dane["grupa"] = request.form.get(
            "grupa",
            ""
        )


        dane["producent"] = request.form.get(
            "producent",
            ""
        )


        dane["kompatybilnosc"] = request.form.get(
            "kompatybilnosc",
            ""
        )


        dane["rodzaj"] = request.form.get(
            "rodzaj",
            ""
        )


        dane["kolor"] = request.form.get(
            "kolor",
            ""
        )


        dane["pochodzenie"] = request.form.get(
            "pochodzenie",
            ""
        )


        dane["numer"] = request.form.get(
            "numer",
            str(aktualny_numer)
        )


        kodzik = ""


        # ====================================================
        # GRUPA
        # ====================================================

        if dane["grupa"] == "Materiały eksploatacyjne":

            kodzik += "ME"


        # ====================================================
        # PRODUCENT
        # ====================================================

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


        # ====================================================
        # KOMPATYBILNOŚĆ
        # ====================================================

        kodzik += producenci.get(
            dane["kompatybilnosc"],
            ""
        )


        # ====================================================
        # RODZAJ
        # ====================================================

        rodzaje = {

            "Tusz": "INK",

            "Toner": "TON",

            "Bębeb": "BB"

        }


        kodzik += rodzaje.get(
            dane["rodzaj"],
            ""
        )


        # ====================================================
        # KOLOR
        # ====================================================

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


        # ====================================================
        # POCHODZENIE
        # ====================================================

        pochodzenie = {

            "Dystrybucja": "D",

            "Rynek": "R"

        }


        kodzik += pochodzenie.get(
            dane["pochodzenie"],
            ""
        )


        # ====================================================
        # NUMER
        # ====================================================

        try:

            numer = int(dane["numer"])


            # Numer użyty w aktualnym kodzie

            kodzik += str(numer)


            # Następny numer

            nastepny_numer = numer + 1


            # Zapisujemy go na serwerze

            zapisz_numer(nastepny_numer)


            # Numer widoczny w formularzu po wygenerowaniu

            dane["numer"] = str(nastepny_numer)


        except ValueError:

            kodzik = "Wpisz poprawny numer!"


        kod = kodzik


    # ========================================================
    # WYŚWIETLENIE STRONY
    # ========================================================

    return render_template(

        "index.html",

        kod=kod,

        dane=dane

    )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)
