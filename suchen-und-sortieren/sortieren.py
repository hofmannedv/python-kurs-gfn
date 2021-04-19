import sortierverfahren
import time

#daten = [16,9,4,3,8]*100
#startZeit = time.time()
#print("Daten (unsortiert)", daten)
#sortierteDaten = sortierverfahren.bubblesort(daten)
#endZeit = time.time()
#print("Sortieren der Daten: %.2f s" % (endZeit - startZeit))
#print("Daten (sortiert)", sortierteDaten)

daten = [16,4,9,56,12,3,61,8]
startZeit = time.time()
print("Daten (unsortiert)", daten)
sortierteDaten = sortierverfahren.insertionsort(daten)
endZeit = time.time()
print("Sortieren der Daten: %.2f s" % (endZeit - startZeit))
print("Daten (sortiert)", sortierteDaten)
