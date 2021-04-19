# Modul Einkaufswagen

def leererArtikel():
    artikel = {
        "name": "",        # Name des Artikels
        "preis": 0,        # Preis des Artikels
        "artikelnummer": 0 # Artikelnummer
    }
    return artikel

def artikelAnlegen(name, preis, artikelnummer):
    neuerArtikel = leererArtikel()
    neuerArtikel["name"] = name
    neuerArtikel["preis"] = preis
    neuerArtikel["artikelnummer"] = artikelnummer
    return neuerArtikel

def artikelName(artikel):
    return artikel["name"]

def artikelPreis(artikel):
    return artikel["preis"]

def artikelNummer(artikel):
    return artikel["artikelnummer"]

def artikelAusgeben(artikel):
    print(artikelName(artikel), ": ", artikelPreis(artikel))
    return

def eingekaufterArtikel(artikel, anzahl):
    ware = {
        "artikelnummer": artikelNummer(artikel),
        "anzahl": anzahl
    }
    return ware

def gesamtsumme(artikelliste, warenliste):
    # liefert Betrag, der zu bezahlen ist
    Gesamtsumme = 0
    for artikel in artikelliste:
        nummer = artikel["artikelnummer"]
        anzahl = artikel["anzahl"]
        for ware in warenliste:
            if artikelNummer(ware) == nummer:
                preis = artikelPreis(artikel)
                zwischensumme = preis * anzahl
                Gesamtsumme = Gesamtsumme + zwischensumme
                break

    return Gesamtsumme

def kassenzettel(artikelliste, warenliste):
    # Artikelname, Anzahl, Einzelpreis, Zwischensumme, Gesamtsumme
    gesamtsumme = 0
    for artikel in artikelliste:
        nummer = artikel["artikelnummer"]
        anzahl = artikel["anzahl"]
        for ware in warenliste:
            if artikelNummer(ware) == nummer:
                preis = artikelPreis(ware)
                bezeichnung = artikelName(ware)
                print("%s %.2f * %i: %.2f" % (bezeichnung, preis, anzahl, anzahl * preis))
                gesamtsumme += preis * anzahl
                break

    print ("Gesamtsumme: %.2f" % gesamtsumme)
    return gesamtsumme

def listeZusammenfassen(einkaufsliste):
    neueListe = []
    for element in einkaufsliste:
        nummer1 = element["artikelnummer"]
        anzahl1 = element["anzahl"]

        elementGefunden = False

        for eintrag in neueListe:
            nummer2 = eintrag["artikelnummer"]
            if nummer1 == nummer2:
                anzahl2 = eintrag["anzahl"]
                eintrag["anzahl"] = anzahl1 + anzahl2
                elementGefunden = True
                break

        if not elementGefunden:
            neueListe.append(element)

    return neueListe

# unfertige Variante
def einkaufslisteKomprimieren(einkaufsliste):
    newList = []
    while einkaufsliste:
        element = einkaufsliste.pop(0)
        an = element["artikelnummer"]
        anzahl = element['anzahl']

        zwList = [] + einkaufsliste
        while zwList:
            element2 = zwList.pop(0)
            anLE = element2["artikelnummer"]
            if an == anLE:
                anzahl = anzahl + element2["anzahl"]
        newList.append({"artikelnummer": an, "anzahl": anzahl})

    return newList

