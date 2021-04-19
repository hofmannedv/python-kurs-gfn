import suchverfahren
import time
from random import randint

def generate_array(length):
    myarray = []
    for i in range(length):
        myarray.append(randint(1, length * 15))
    return myarray

# array mit festen 8000 Werten
# datenliste = [4, 8, 12, 21, 3, 19, 76, 43] * 10000000
datenliste = generate_array(800000)
suchwert = 20
startZeit = time.time()
sortierteDatenliste = sorted(datenliste)
endZeit = time.time()
print("Sortieren der Daten: %.2f s" % (endZeit - startZeit))

# print(datenliste)
# print(sortierteDatenliste)

# einfache, lineare Suche
print("Einfache, lineare Suche")
startZeit = time.time()
#print("Datenliste:", datenliste)
position, durchlauf = suchverfahren.lineareSuche(datenliste, suchwert)
endZeit = time.time()
print("Wert 8 gefunden an Position", position)
print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

# einfache, lineare Suche, sortierte Daten
print("Einfache, lineare Suche, sortierte Daten")
startZeit = time.time()
#print("Datenliste:", datenliste)
position, durchlauf = suchverfahren.lineareSuche(sortierteDatenliste, suchwert)
endZeit = time.time()
# print("Wert 8 gefunden an Position", position)
print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

# binaere Suche, sortierte Daten
print("Binaere Suche, sortierte Daten")
startZeit = time.time()
#print("Datenliste:", datenliste)
position, durchlauf = suchverfahren.binaereSuche(sortierteDatenliste, suchwert)
endZeit = time.time()
# print("Wert 8 gefunden an Position", position)
print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

# einfache, lineare Suche, Mehrfachtreffer
print("Einfache, lineare Suche, Mehrfachtreffer")
#print("Datenliste:", datenliste)
startZeit = time.time()
positionen, durchlauf= suchverfahren.lineareSucheAlleTreffer(datenliste, suchwert)
# print("Wert 8 gefunden an Position", positionen)
endZeit = time.time()
print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

# einfache, lineare Suche, Mehrfachtreffer, sortierte Liste
print("Einfache, lineare Suche, Mehrfachtreffer, sortierte Liste")
#print("Datenliste:", datenliste)
startZeit = time.time()
positionen, durchlauf= suchverfahren.lineareSucheAlleTreffer(sortierteDatenliste, suchwert)
#print("Wert 8 gefunden an Position", positionen)
endZeit = time.time()
print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

# Suche mit in-Operator
print("Suche mit in-Operator")
startZeit = time.time()
position = suchverfahren.sucheMitInOperator(datenliste, suchwert)
# print("Wert 8 gefunden an Position", position)
endZeit = time.time()
#print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

# Suche mit in-Operator, sortierte Liste
print("Suche mit in-Operator, sortierte Liste")
startZeit = time.time()
position = suchverfahren.sucheMitInOperator(sortierteDatenliste, suchwert)
# print("Wert 8 gefunden an Position", position)
endZeit = time.time()
#print("Notwendig waren %i Durchlaeufe" % durchlauf)
print("Zeitdauer: %.2f s" % (endZeit - startZeit))
print("")

