stadtliste = ["Berlin", "New York", "Paris", "Köln", "Oslo"]

testliste = ["Frankfurt", "Berlin", "Paris"]
for teststadt in testliste:
    if teststadt not in stadtliste:
        print("Stadt", teststadt, "nicht gefunden")
    else:
        print("Stadt", teststadt, "in der Liste enthalten")

