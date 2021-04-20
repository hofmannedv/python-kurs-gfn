
def bubblesort(datenliste):
    sortierteDatenliste = datenliste
    for i in range(len(datenliste)):
        position = 0
        while position < len(datenliste) - 1:

            #print(sortierteDatenliste)
            if sortierteDatenliste[position] > sortierteDatenliste[position + 1]:
                # zwei elemente vertauschen
                merken = sortierteDatenliste[position]
                sortierteDatenliste[position] = sortierteDatenliste[position + 1]
                sortierteDatenliste[position + 1] = merken
            position = position + 1
    return sortierteDatenliste

def insertionsort(datenliste):
    sortierteDatenliste = datenliste
    if len(sortierteDatenliste) < 2:
        pass # liste schon sortiert
    else:
        sortiertVon = 0
        sortiertBis = 0
        for position in range(1, len(sortierteDatenliste)):
            aktuellerWert = sortierteDatenliste[position]
            print("teste %i ..." % aktuellerWert)
            einfuegeposition = sortiertBis
            while einfuegeposition > -1:
                if sortierteDatenliste[einfuegeposition] > aktuellerWert:
                    einfuegeposition = einfuegeposition - 1
                else:
                    break

            # Element am Anfang (vor der sortierten Liste) einfuegen
            if einfuegeposition < 0:
                neueListe = [aktuellerWert]
                print(neueListe)
                neueListe += sortierteDatenliste[sortiertVon:sortiertBis + 1]
                print(neueListe)
            else:
                # Element zwischendrin in der sortierten Liste einfuegen
                neueListe = sortierteDatenliste[sortiertVon:einfuegeposition + 1]
                print(neueListe)
                neueListe += [aktuellerWert]
                print(neueListe)
                neueListe += sortierteDatenliste[einfuegeposition + 1:sortiertBis + 1]
                print(neueListe)

            neueListe += sortierteDatenliste[sortiertBis + 2:]
            print(neueListe)
            sortiertBis += 1
            sortierteDatenliste = neueListe
    return sortierteDatenliste

def partition(arr, low, high):
    i = (low-1)           # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        return
