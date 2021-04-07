shoppingCart = ["birne", "apple", "banana", "kiwi"]
print(shoppingCart[2]) # banana
print(shoppingCart[-1]) # kiwi

# Liste rueckwarts durchlaufen
print("Liste rueckwarts durchlaufen")
i = 3
while i >= 0:
    print (i, shoppingCart[i])
    i = i - 1

# spezifische Reihenfolge
print("Liste spezifisch durchlaufen")
reihenfolge = [2, 3, 0, 1]
for i in reihenfolge:
    print (i, shoppingCart[i])

# mit Range-Funktion
for i in range(4):
    print (i, shoppingCart[i])

# mir Range und len - egal wie lang die Liste ist
anzahlElemente = len(shoppingCart)
for i in range(anzahlElemente):
    print (i, shoppingCart[i])

for i in range(len(shoppingCart)):
    print (i, shoppingCart[i])

position = 0
for element in shoppingCart:
    print(position, element)
    position = position + 1

# ersten beiden Elemente ausgeben
print("nur 1. und 2. Element")
print(shoppingCart[:2])

# letzte beiden Elemente ausgeben
print("nur 3. und 4. Element")
print(shoppingCart[-2:])

# nur vorletztes Element ausgeben -> Liste mit einem Element
print("nur 3. Element")
print(shoppingCart[-2:-1])

# nur vorletztes Element ausgeben -> Liste mit einem Element
print("nur 3. Element")
print([shoppingCart[-2]])

# nur vorletztes Element ausgeben -> String
print("nur 3. Element")
print(shoppingCart[-2])

# nur letzte Element ausgeben als Liste 
print("nur 3. und 4. Element")
print([shoppingCart[-2:]])

# print([shoppingCart[-2:]][0][0])
