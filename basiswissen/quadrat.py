# gebe die Quadratzahlen von 10 bis 20 aus
# - for-Schleife

#exponent = 2

#for zahl in range(10,21):
#    quadrat = zahl ** exponent
#    print("Das Quadrat von %i is %i" % (zahl, quadrat))

# - while-Schleife (nur gerade Zahlen)
zahl = 10
while zahl <= 20:
    print("berechne Quadrat fuer %i" % zahl)
    if zahl % 2 == 0:
        if zahl > 16:
            print ("Rechenaufwand zu hoch. Will nicht mehr. Breche ab.")
            break

        quadratzahl = zahl ** 2
        print("Quadratzahl von %i ist %i" % (zahl, quadratzahl))

    zahl += 1

zahlenliste = [3, 7, 1, 45, 12]
gesamtsumme = sum(zahlenliste)
durchschnitt = gesamtsumme / len(zahlenliste)

gesamtsumme = 0
for element in zahlenliste:
    gesamtsumme += element




