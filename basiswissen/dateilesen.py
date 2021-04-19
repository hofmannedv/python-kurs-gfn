dateiinhalt = [
    "Heute ist ein wunderbarer Tag.",
    "Lernt Python."
]

# Zeilenumbrueche ergaenzen
for zeilenindex in range(len(dateiinhalt)):
    zeile = dateiinhalt[zeilenindex] + "\n"
    dateiinhalt[zeilenindex] = zeile

# Schreibvorgang -- bestehende Datei ersetzen
with open("ausgabe.txt", "w") as fileHandle:
    fileHandle.writelines (dateiinhalt)

# Schreibvorgang -- an bestehende Datei anfuegen
with open("ausgabe.txt", "a") as fileHandle:
    fileHandle.writelines (dateiinhalt)

# Lesevorgang -- aus Datei lesen
with open("ausgabe.txt", "r") as fileHandle:
    content = fileHandle.readlines()

print(content)
