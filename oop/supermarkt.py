# gesamtes Modul importieren
# import einkaufswagen

# nur die Klasse Einkaufswagen importieren
from einkaufswagen import Einkaufswagen

# nur die Klasse Artikel importieren
from artikel import Artikel

# Artikel im Lagerbestand festlegen 
artikel1 = Artikel(artikelnummer = 1, beschreibung = "Milch", artikelgruppe = 1, einheit = "l", preis = 1, vorraetig = 1, mehrwertsteuersatz = 7) 
artikel1.status()

artikel2 = Artikel(2, "Tee", 1, "g", 1, 1, 7) 
artikel2.status()

# erstellen von Einkaufswagen
korb = Einkaufswagen()
korb.setName("korb")
korb2 = Einkaufswagen()
korb2.setName("korb2")
korb3 = Einkaufswagen()
korb3.setName("korb3")

# Variablentyp ausgeben
print(type(korb))

waspassthinein = korb.volumen
print("in den Einkaufswagen passen %i Kilogramm" % waspassthinein)

korb.volumen = 30
waspassthinein = korb.volumen
print("in den Einkaufswagen passen %i Kilogramm" % waspassthinein)

material = korb.getMaterial()
print("Der korb ist aus %s" % material)

material = "Holz"
korb.setMaterial(material)
material = korb.getMaterial()
print("Der korb ist aus %s" % material)

print("Status des Korbs:")
korb.status()

# Artikel in korb2 hinzufuegen
artikelWarenkorb1 = Artikel(artikelnummer = 1, beschreibung = "Milch", artikelgruppe = 1, einheit = "l", preis = 1, vorraetig = 1, mehrwertsteuersatz = 7) 

wievieleWillIchReinTun = 200
wievieleGingenRein = korb2.legeArtikelInWarenkorb2(artikelWarenkorb1,
wievieleWillIchReinTun)
if wievieleGingenRein:
    print("%i x Milch hinzugefuegt" % wievieleGingenRein)
    if wievieleWillIchReinTun > wievieleGingenRein:
        print("fuer %i Artikel war kein Platz mehr" % (wievieleWillIchReinTun - wievieleGingenRein))
else:
    print("Fehlgeschlagen: keine Milch nicht hinzugefuegt")

#korb2.legeArtikelInWarenkorb("Tee")
korb2.showArtikelImKorb()
korb2.showArtikelImKorb2()

# Inhalt von Korb 3
#korb3.legeArtikelInWarenkorb("Kaffee")
#korb3.showArtikelImKorb()

# Inhalt von Korb 1
#korb.showArtikelImKorb()

del(korb2)
