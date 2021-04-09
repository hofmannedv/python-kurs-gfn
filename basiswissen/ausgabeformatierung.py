temperatur = 15.4
temperaturS = str(temperatur)

# Idee: geht so nicht
#print("heute beträgt die Temperatur" + temperatur + "Grad")

# Umwandlung in String
print("heute betraegt die Temperatur " + str(temperatur) + " Grad")
print("heute betraegt die Temperatur " + temperaturS + " Grad")

#print("heute betraegt die Temperatur %i Grad" % temperatur)
print("heute betraegt die Temperatur %s Grad" % temperaturS)
#print("heute betraegt die Temperatur %i Grad" % int(temperaturS))
print("heute betraegt die Temperatur %.2f Grad" % temperatur)
print("heute betraegt die Temperatur", temperatur, "Grad")
