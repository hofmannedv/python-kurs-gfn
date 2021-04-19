
# Klasse definieren
class Einkaufswagen:

    def __init__(self):
        """Beschreibung zur Methode"""

        print("Objekt der Klasse Einkaufswagen wird angelegt")
        # Klassenvariablen
        self.material = "Metall"
        self.mitRaedern = True
        self.volumen = 20 # Artikel, oder Kubikmeter
        self.name = "Einkaufswagen"
        self.artikelImKorb = []

        return

    def __del__(self):
        name = self.getName()
        print("Objekt der Klasse Einkaufswagen (%s) wird entfernt" % name)
        return

    def getMaterial(self):
        return self.material

    def setMaterial(self, wert):
        self.material = wert
        return

    def getMitRaedern(self):
        return self.mitRaedern

    def setMitRaedern(self, wert):
        self.mitRaedern = wert
        return

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, wert):
        self.volumen = wert
        return

    def getName(self):
        return self.name

    def setName(self, wert):
        self.name = wert
        return

    def status(self):
        print("Material: %s" % self.getMaterial())
        print("Hat Raeder:", self.getMitRaedern())
        print("Volumen: %i Liter" % self.getVolumen())
        print("Name: %s" % self.getName())
        return

    # - artikel in den Einkaufswagen legen
    def legeArtikelInWarenkorb(self, artikel):
        # akzeptiert Zeichenketten als Artikel
        if not self.istMaximaleArtikelMengeErreicht():
            # hat geklappt
            self.artikelImKorb.append(artikel)
            return True
        # ging schief
        return False

    def legeArtikelInWarenkorb2(self, artikel, menge):
        if self.istMaximaleArtikelMengeErreicht():
            # kein Platz mehr
            return 0
        else:
            # passen _alle_ Artikel noch in den Korb hinein?
            if len(self.artikelImKorb) + menge <= self.getVolumen():
                # hat geklappt
                self.artikelImKorb += [artikel] * menge
                return menge
            else:
                # geht doch nicht, aber vielleicht gehen ja einige
                anzahl = self.getVolumen() - len(self.artikelImKorb)
                self.artikelImKorb += [artikel] * anzahl
                # so viele passten hinein
                return anzahl

    # - artikel wieder herausnehmen
    def entferneArtikelAusWarenkorb(self, artikel):
        if artikel in self.artikelImKorb:
            # hat geklappt
            self.artikelImKorb.remove(artikel)
            return True
        # ging schief
        return False

    # - testen, ob die maximale menge erreicht ist, die in den Wagen passt
    def istMaximaleArtikelMengeErreicht(self):
        if len(self.getArtikelImKorb()) == self.getVolumen():
            return True
        return False

    # - sortieren der artikel
    def sortiereArtikelImKorb(self):
        self.artikelImKorb.sort()
        return

    # - warenwert berechnen
    def berechneWarenwert(self):
        warenwert = 0
            - artikelweise im Warenkorb durchgehen
            - preis des Artikels auslesen
            - zur gesamtsumme hinzuaddieren
        return warenwert

    # - artikelliste beziehen
    def getArtikelImKorb(self):
        return self.artikelImKorb

    # - artikelliste ausgeben
    def showArtikelImKorb(self):
        print("Inhalt von Warenkorb %s:" % self.getName())
        for artikel in self.getArtikelImKorb():
            print(artikel)
        return

    def showArtikelImKorb2(self):
        print("Inhalt von Warenkorb %s:" % self.getName())
        for artikel in self.getArtikelImKorb():
            print(artikel.getBeschreibung())
        return

if __name__ == "__main__":
    print("Ausfuehrung des Moduls")

    print("Modultest/Klasse")
    korb = Einkaufswagen()
