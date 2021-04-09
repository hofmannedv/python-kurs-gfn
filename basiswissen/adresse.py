adressliste = []

adresse1 = {
    "name": "Lina Lustig",
    "strasse": "Dorfstrasse 1",
    "ort": "Kiliwauwau an der Knatter",
    "plz": 12345
}

adresse2 = {
    "name": "Donald Duck",
    "strasse": "Am Speicher 1",
    "ort": "Entenhausen",
    "plz": 56789
}

adresse3 = {
    "name": "Donald Duck",
    "strasse": "Am Speicher 1",
    "ort": "Entenhausen",
    "plz": 56789
}

#adressliste = [adresse1, adresse2]
#adressliste.append(adresse1)
#adressliste.append(adresse2)
for neueAdresse in [adresse1, adresse2, adresse3]:
    adressliste.append(neueAdresse)

print(adressliste)
