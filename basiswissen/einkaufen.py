# Einkaufswagen-Modul verwenden

import einkaufswagen

# Liste der verfuegbaren Artikel/Waren
lagerbestand = []

# Liste der Artikel im Einkaufswagen
einkaufsliste = []

# neuen Artikel fuer unsere Warenliste anlegen
artikel1 = einkaufswagen.leererArtikel()
print(artikel1)

artikel2 = einkaufswagen.leererArtikel()
print(artikel2)

artikel3 = einkaufswagen.artikelAnlegen("Banane",1.09, 57837)
print(artikel3)

artikel4 = einkaufswagen.artikelAnlegen(name="Milch",preis=0.71, artikelnummer=1234)
print(artikel4)

# Warenliste ergaenzen -- Name, Artikelnummer und Preis
lagerbestand.append(artikel3)
lagerbestand.append(artikel4)
print(lagerbestand)

# Einkaufsliste fuellen -- Artikelnummer und Anzahl
einkaufsliste.append(
    einkaufswagen.eingekaufterArtikel(artikel3,2)
)
einkaufsliste.append(
    einkaufswagen.eingekaufterArtikel(artikel4,1)
)
einkaufsliste.append(
    einkaufswagen.eingekaufterArtikel(artikel3,1)
)
print(einkaufsliste)

einkaufswagen.kassenzettel(einkaufsliste,lagerbestand)

print(einkaufswagen.listeZusammenfassen(einkaufsliste))
print(einkaufswagen.einkaufslisteKomprimieren (einkaufsliste))
