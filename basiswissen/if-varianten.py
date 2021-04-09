a = 10
b = 20

# was man normalerweise so macht
if a < b:
    print("test 1")
    minimum = a
else:
    print("test 2")
    minimum = b

# ternaerer Operator
minimum = a if a < b else b

# mit default-Wert
minimum = a           # Annahme, a ist kleiner als b
if b < a: 
    minimum = b       # falls Annahme falsch, dann b


# direkt im print-Statement
print("then: a" if a < b else "else: b")

print (minimum)
