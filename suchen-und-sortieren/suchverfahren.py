def sucheMitInOperator(datenliste, wert):
    # gibt position des wertes in der Liste zurueck
    position = -1 # wert nicht in datenliste
    durchlauf = 0 # wieviele Durchlaeufe haben wir
    if wert in datenliste:
        # wert ist datenliste vorhanden
        # index in der Liste bestimmen
        position = datenliste.index(wert)
    return position

def lineareSuche(datenliste, wert):
    # gibt position des wertes in der Liste zurueck
    position = -1 # wert nicht in datenliste
    durchlauf = 0 # wieviele Durchlaeufe haben wir

    for i in range(len(datenliste)):
        durchlauf = durchlauf + 1
        if datenliste[i] == wert:
            # wert in datenliste gefunden
            position = i
            break

    # gib index des suchtreffers + anzahl durchlaeufe zurueck
    return position, durchlauf

def lineareSucheAlleTreffer(datenliste, wert):
    # gibt alle positionen des wertes in der Liste zurueck
    positionen = [] # wert nicht in datenliste
    durchlauf = 0 # wieviele Durchlaeufe haben wir

    for i in range(len(datenliste)):
        durchlauf = durchlauf + 1
        if datenliste[i] == wert:
            # wert in datenliste gefunden, zur Liste ergaenzen
            # positionen += [i]    # Variante 1
            positionen.append(i)   # Variante 2

    return positionen, durchlauf

def binaereSuche(datenliste, wert):
    minElement = 0
    maxElement = len(datenliste)

    result = -1  # Element nicht in der Liste
    durchlauf = 0

    while True:
        durchlauf += 1
        median = (maxElement + minElement) // 2
        #print ("min:%i max:%i median:%i" % (minElement, maxElement, median))
        if minElement > maxElement:
            #print ("element %i not found" % number)
            break
        if datenliste[median] == wert:
            #print ("got %i at position %i" % (number, median))
            result = median
            break
        else:
            if datenliste[median] < wert:
                minElement = median + 1
            else:
                maxElement = median - 1

    return result, durchlauf
