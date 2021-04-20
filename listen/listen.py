from knoten import ListNode
from einfacheliste import SingleLinkedList

werteListe = [17, 85, 96, 40, 13]
knotenListe = []

# Liste von Knoten erzeugen
for wert in werteListe:
    # einen einzelnen Knoten anlegen
    knoten = ListNode(wert)
    knotenListe.append(knoten)

print(knotenListe)
for knoten in knotenListe:
    print("Neuer Knoten:")
    knoten.status()

# finde den Knoten in der Knotenliste mit dem Wert 40
# und gib dessen Objektreferenz aus
for knoten in knotenListe:
    if knoten.getData() == 40:
        knoten.status()
        print(knoten)
        break

# Objekt einfach-verlinkte Liste bauen
einfachVerlinkteListe = SingleLinkedList()

# Inhalt ausgeben - leere Liste
einfachVerlinkteListe.outputList()

# alle knoten hinzufuegen
for knoten in knotenListe:
    einfachVerlinkteListe.addListitem(knoten)
    einfachVerlinkteListe.outputList()
    print(" ")

print(einfachVerlinkteListe.search(40))
