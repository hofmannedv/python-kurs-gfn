# ranges testen

# durchlaufe von 0 bis 4: 5 Werte beginnend mit 0
for i in range(5):
    print(i)

# durchlaufe von 2 bis 4: 3 Werte beginnend mit 2
for i in range(2, 5):
    print(i)

# durchlaufe von 10 bis 20: nur gerade Zahlen
for i in range(10, 21, 2):
    print(i)

# durchlaufe von 20 bis 10: nur gerade Zahlen
for i in range(20, 9, -2):
    print(i)

# durchlaufe von 10 bis 20: nur gerade Zahlen, ohne range()
wert = 10
while wert <= 20:
    if wert % 2 == 0:
        print(wert)
    wert = wert + 1

for i in range(1, 5):
    copy(file to destination)
    if runtimeError:
        break
else:
    delete original
