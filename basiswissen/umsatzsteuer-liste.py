""" Skript zur Berechnung der Umsatzsteuer
    Version 1
    keine Parameter
"""

# preise als Liste
preise = [10, 5, 6, 3, 17]
umsatzsteuer = 0.19 # Zuweisung einer Fliesskommazahl

gesamtsumme = 0
for wert in preise:
    # Anweisungen in der Schleife
    ust = wert * umsatzsteuer
    einzelbetrag = wert + ust
    print(einzelbetrag)
    gesamtsumme = gesamtsumme + einzelbetrag

print("Gesamtsumme: ", gesamtsumme)

# ohne for-Schleife
preise = [5, 4.5, 6]
zwischensumme = sum(preise)

ust = zwischensumme * umsatzsteuer
gesamtsumme = zwischensumme + ust

print("Gesamtsumme: ", gesamtsumme)
