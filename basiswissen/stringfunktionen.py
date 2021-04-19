
def stringUmdrehen (zeichenkette):
    # "hamburg -> grubmah"
    for i in range(len(zeichenkette) -1 , -1, -1):
        print(zeichenkette[i])
    return

def stringUmdrehen2 (zeichenkette):
    # mit while-Schleife
    # durchlaufen der Schleife von hinten nach vorne
    position = len(zeichenkette) - 1
    while position > -1:
        print(zeichenkette[position])
        position = position - 1

    return

def stringUmdrehen3(zeichenkette):
    # Position = max. Index für die neue Liste; da 0 der erste Indexwert ist, hier die Länge 
    position = len(zeichenkette)
    while position > 0:
        position = position - 1         # mit -1 von rechts nach links
        print("aktueller index: ", str(position), "zeichenkette[position]: ", zeichenkette[position])

def stringFinden(zeichenkette, suchmuster):
    # finde alle nicht ueberlappenden Vorkommen des Suchmusters 
    # in der Zeichenkette
    position = zeichenkette.find(suchmuster)
    while position > -1:
        print ("Suchmuster %s an Position %i gefunden" % (suchmuster, position))
        # setze an Folgeposition fort
        position = zeichenkette.find(suchmuster, position + 1)
    return

def findword(originalstring, searchedword):
    flag = True
    position = 0
    matchlist = []

    while flag:
        position = originalstring.find(searchedword, position)

        if position >= 0:
            position += 1
            matchlist.append(position)
        else:
            flag = False

    if len(matchlist) > 0:
        print("Positionen des Suchstrings \"%s\": %s " %(searchedword, str(matchlist)))
    else:
        print("Zeichenkette konnte nicht gefunden werden")

def zaehleWorte(text):
    # anzahl Worte im Text
    anzahl = 0
    for zeile in text:
        anzahl = anzahl + len(zeile.split())

    return anzahl

def ausgabeTabelle(wortliste):
    breite = 0
    for eintrag in wortliste:
        if len(eintrag) > breite:
            breite = len(eintrag)

    formatstring = "%" + "-" + str(int(breite*1.5)) + "s"
    for eintrag in wortliste:
        print(formatstring % eintrag + "Test")
        

print(ausgabeTabelle(["Hamburg", "Basel"]))

print(zaehleWorte([
    "das ist die erste Zeile", 
    "Zeile mit noch mehr Text"
]))

#stringUmdrehen("zweibrücken")
#stringUmdrehen2("hamburg")
#stringUmdrehen3("heidelberg")

#stringFinden("Alibaba", "ba")
