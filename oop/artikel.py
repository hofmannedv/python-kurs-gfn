
# Klasse definieren
# Artikelbeschreibung fuer den Lagerbestand
class Artikel:

    # Initialisierungsfunktion mit Default-Werten
    def __init__(self, artikelnummer = 0, beschreibung = "Artikel", artikelgruppe = 1, einheit = "kg", preis = 0, vorraetig = 0, mehrwertsteuersatz = 19):
        print("Objekt der Klasse Artikel wird angelegt")
        # Klassenvariablen anlegen
        self.setArtikelnummer(artikelnummer)
        self.setBeschreibung(beschreibung)
        self.setArtikelgruppe(artikelgruppe)
        self.setEinheit(einheit)
        self.setPreis(preis)
        self.setVorraetig(vorraetig) # wieviele davon auf Lager sind
        self.setMehrwertsteuer(mehrwertsteuersatz)

        return

    def getArtikelnummer(self):
        return self.artikelnummer

    def setArtikelnummer(self, wert):
        self.artikelnummer = wert
        return

    def getBeschreibung(self):
        return self.beschreibung

    def setBeschreibung(self, wert):
        self.beschreibung = wert
        return

    def getArtikelgruppe(self):
        return self.artikelgruppe

    def setArtikelgruppe(self, wert):
        self.artikelgruppe = wert
        return

    def getPreis(self):
        return self.preis

    def setPreis(self, wert):
        self.preis = wert
        return

    def getVorraetig(self):
        return self.vorraetig

    def setVorraetig(self, wert):
        self.vorraetig = wert
        return

    def getMehrwertsteuer(self):
        return self.mehrwertsteuersatz

    def setMehrwertsteuer(self, wert):
        self.mehrwertsteuersatz = wert
        return

    def getEinheit(self):
        return self.einheit

    def setEinheit(self, wert):
        self.einheit = wert
        return

    def status(self):
        print("Artikelnummer:", self.getArtikelnummer())
        print("Beschreibung:", self.getBeschreibung())
        print("Artikelgruppe:", self.getArtikelgruppe())
        print("Einheit:", self.getEinheit())
        print("Preis:", self.getPreis())
        print("Ist Vorraetig:", self.getVorraetig())
        print("Mehrwertsteuer:", self.getMehrwertsteuer())
        return
