
def binarySearch (sortedNumberList, number):

    minElement = 0
    maxElement = len(sortedNumberList)

    result = -1  # Element nicht in der Liste

    while True:
        median = (maxElement + minElement) // 2
        print ("min:%i max:%i median:%i" % (minElement, maxElement, median))
        if minElement > maxElement:
            print ("element %i not found" % number)
            break
        if sortedNumberList[median] == number:
            print ("got %i at position %i" % (number, median))
            result = median
            break
        else:
            if sortedNumberList[median] < number:
                minElement = median + 1
            else:
                maxElement = median - 1

    return result
