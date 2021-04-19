import random
datumsliste = ["1.1.2021", "2.1.2021", "3.1.2021", "4.1.2021"]
dachzeile = "Datum\tTemperaturwert"
logdaten = []
for datum in datumsliste:
    eintrag = {
        "datum": datum,
        "temperatur" : random.randint(1,30)
    }
    logdaten.append(eintrag)

ausgabe = []
ausgabe.append(dachzeile)
for eintrag in logdaten:
    ausgabe.append("%s\t%i" % (eintrag["datum"], eintrag["temperatur"]))

# Zeilenumbrueche ergaenzen
for zeilenindex in range(len(ausgabe)):
    zeile = ausgabe[zeilenindex] + "\n"
    ausgabe[zeilenindex] = zeile

# Schreibvorgang -- bestehende Datei ersetzen
with open("ausgabe.txt", "w") as fileHandle:
    fileHandle.writelines (ausgabe)


