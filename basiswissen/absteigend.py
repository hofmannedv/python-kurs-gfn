# (C) 2021 Frank Hofmann
# Released under GNU Public License (GPL)

def absteigend (zahlenliste):
    # aufsteigend sortieren
    zahlenliste.sort()
    # liste umdrehen
    umgedreht = reversed(zahlenliste)
    umgedrehteListe = []
    for item in umgedreht:
        umgedrehteListe.append(item)

    return umgedrehteListe

def absteigend2 (zahlenliste):
    # aufsteigend sortieren
    zahlenliste.sort()
    # liste umdrehen
    umgedrehteListe = list(reversed(zahlenliste))

    return umgedrehteListe

def aufsteigend (zahlenliste):
    sortierteListe = list(sorted(zahlenliste))
    return sortierteListe

def aufsteigend2 (zahlenliste):
    return zahlenliste.sort()

zahlenliste = [5, 10, 4, 9, 11]
print("Unsortiert: ", zahlenliste)
print("Absteigend sortiert 1:", absteigend(zahlenliste)) 
print("Absteigend sortiert 2:", absteigend2(zahlenliste)) 
print("Aufsteigend sortiert:", aufsteigend(zahlenliste)) 
