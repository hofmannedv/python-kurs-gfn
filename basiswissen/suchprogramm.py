
# importiere Extra-Module
# import suchen                     # ganzes Modul
from suchen import binarySearch   # nur die gewuenschte Funktion

sortedNumberList = [1, 5, 12, 13, 17, 18, 19, 24, 26, 32, 33, 36, 37, 38, 47, 54, 60, 72, 75, 80, 89, 90, 92, 93, 95, 99, 100, 102, 103, 104]
zahl = 37

# suche mit der Index-Funktion
position = sortedNumberList.index(zahl)
print("Position von %i ist %i" % (zahl, position))

# suche mit der binarySearch-Funktion
position = binarySearch(sortedNumberList, zahl)
print("Position von %i ist %i" % (zahl, position))
