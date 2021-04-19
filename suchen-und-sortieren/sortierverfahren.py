def bubblesort(datenliste):
    sortierteDatenliste = datenliste
    for i in range(len(datenliste)):
        position = 0
        while position < len(datenliste) - 1:

            #print(sortierteDatenliste)
            if sortierteDatenliste[position] > sortierteDatenliste[position + 1]:
                # zwei elemente vertauschen
                merken = sortierteDatenliste[position]
                sortierteDatenliste[position] = sortierteDatenliste[position + 1]
                sortierteDatenliste[position + 1] = merken
            position = position + 1
    return sortierteDatenliste

def insertionsort(datenliste):
    sortierteDatenliste = datenliste
    if len(sortierteDatenliste) < 2:
        pass # liste schon sortiert
    else:
        sortiertVon = 0
        sortiertBis = 0
        for position in range(1, len(sortierteDatenliste)):
            aktuellerWert = sortierteDatenliste[position]
            print("teste %i ..." % aktuellerWert)
            einfuegeposition = sortiertBis
            while einfuegeposition > -1:
                if sortierteDatenliste[einfuegeposition] > aktuellerWert:
                    einfuegeposition = einfuegeposition - 1
                else:
                    break

            if einfuegeposition < 0:
                neueListe = [aktuellerWert]
                print(neueListe)
                neueListe += sortierteDatenliste[sortiertVon:sortiertBis + 1]
                print(neueListe)
                neueListe += sortierteDatenliste[sortiertBis + 2:]
                print(neueListe)
                sortierteDatenliste = neueListe
                sortiertBis += 1
            else:
                neueListe = sortierteDatenliste[sortiertVon:einfuegeposition + 1]
                print(neueListe)
                neueListe += [aktuellerWert]
                print(neueListe)
                neueListe += sortierteDatenliste[einfuegeposition + 1:sortiertBis + 1]
                print(neueListe)
                neueListe += sortierteDatenliste[sortiertBis + 2:]
                print(neueListe)
                sortiertBis += 1
                sortierteDatenliste = neueListe
    return sortierteDatenliste
