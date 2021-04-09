def zusammenrechnen (zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

def zusammenrechnenListe (zahlenliste):
    gesamtsumme = 0
    for element in zahlenliste:
        gesamtsumme = zusammenrechnen(gesamtsumme, element)
    return gesamtsumme

def zusammenrechnenListe2 (zahlenliste):
    gesamtsumme = 0
    for element in zahlenliste:
        gesamtsumme += element
    return gesamtsumme

def zusammenrechnenListe3 (zahlenliste):
    # print("Berechne Summe für", zahlenliste)
    gesamtsumme = 0
    if len(zahlenliste) == 0:
        return gesamtsumme
    else:
        # print("rufe zusammenrechnenListe3 erneut auf ...")
        gesamtsumme = zahlenliste[0] + zusammenrechnenListe3(zahlenliste[1:])
        return gesamtsumme

# summe mit pop am Ende
def zusammenrechnenPop1 (zahlenliste):
    gesamtsumme = 0
    element = 0
    for element in range(len(zahlenliste)):
        gesamtsumme += zahlenliste.pop()
    return gesamtsumme

def zusammenrechnenPop2 (zahlenliste):
    gesamtsumme = 0
    while len(zahlenliste):
        gesamtsumme += zahlenliste.pop()
    return gesamtsumme

# Hauptprogramm
zahlenliste = [10, 5, 11, 3, 43]

# Variante 1 von Rolf mit Indizes, fest auf 5 Listenelemente
gesamtsumme = 0
zahlenliste = [10, 5, 11, 3, 43]
for i in range(5):
    gesamtsumme = zusammenrechnen(gesamtsumme, zahlenliste[i])
print("gesamtsumme: %i" % gesamtsumme)

# Variante 2 von Rolf mit Indizes, beliebige Listenlaenge
gesamtsumme = 0
zahlenliste = [10, 5, 11, 3, 43]
for i in range(len(zahlenliste)):
    gesamtsumme = zusammenrechnen(gesamtsumme, zahlenliste[i])
print("gesamtsumme: %i" % gesamtsumme)

# Variante 3: berechne die Summe der zahlenliste
gesamtsumme = 0
for element in zahlenliste:
    gesamtsumme = zusammenrechnen(gesamtsumme, element)
print("gesamtsumme: %i" % gesamtsumme)

# Variante 4: Aufruf mit Liste als Parameter
zahlenliste = [10, 5, 11, 3, 43]
gesamtsumme = zusammenrechnenListe(zahlenliste)
print("gesamtsumme: %i" % gesamtsumme)

# Variante 5: Aufruf mit Liste als Parameter (rekursiv)
zahlenliste = [10, 5, 11, 3, 43]
gesamtsumme = zusammenrechnenListe3(zahlenliste)
print("gesamtsumme: %i" % gesamtsumme)

